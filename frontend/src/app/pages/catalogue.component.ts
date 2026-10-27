import { Component, OnInit, inject } from '@angular/core';
import { ActivatedRoute, RouterLink } from '@angular/router';
import { FormsModule } from '@angular/forms';
import { debounceTime, distinctUntilChanged, Subject } from 'rxjs';

import { CatalogueService } from '../catalogue.service';
import { Brand, Category, Product } from '../models';

@Component({
  standalone: true,
  imports: [FormsModule, RouterLink],

  template: `
    <section class="page-banner">
      <div class="container">
        <small>DISCOVER YOUR OPTIONS</small>
        <h1>Product catalogue</h1>
        <p>Search products and narrow the list by brand or category.</p>
      </div>
    </section>

    <section class="section">
      <div class="container">
        <div class="filters">
          <div>
            <label class="form-label">Search products</label>
            <input
              class="form-control"
              placeholder="Name, model or description..."
              [(ngModel)]="search"
              (ngModelChange)="onSearchChange($event)"
            />
          </div>

          <div>
            <label class="form-label">Brand</label>
            <select
              class="form-select"
              [(ngModel)]="brand"
              (ngModelChange)="load()"
            >
              <option value="">All brands</option>
              @for (b of brands; track b.id) {
                <option [value]="b.slug">{{ b.name }}</option>
              }
            </select>
          </div>

          <div>
            <label class="form-label">Category</label>
            <select
              class="form-select"
              [(ngModel)]="category"
              (ngModelChange)="load()"
            >
              <option value="">All categories</option>
              @for (c of categories; track c.id) {
                <option [value]="c.slug">{{ c.name }}</option>
              }
            </select>
          </div>

          <button
            type="button"
            class="btn btn-outline-brand"
            (click)="reset()"
          >
            Reset
          </button>
        </div>

        @if (loading) {
          <p class="text-center py-5">Loading products...</p>
        } @else if (error) {
          <div class="alert alert-warning">{{ error }}</div>
        } @else {
          <p class="results">
            {{ products.length }} product(s) found
          </p>

          @if (products.length === 0) {
            <div class="empty">
              <h3>No matching products</h3>
              <p>Try changing your search or filters.</p>
            </div>
          } @else {
            <div class="row g-4">
              @for (p of products; track p.id) {
                <div class="col-12 col-sm-6 col-lg-4">
                  <article class="product-card">
                    <a [routerLink]="['/product', p.slug]">
                      <img [src]="p.image_url" [alt]="p.name" />
                    </a>

                    <div class="p-3">
                      <small class="meta">
                        {{ p.brand.name }} · {{ p.category.name }}
                      </small>

                      <h3>
                        <a [routerLink]="['/product', p.slug]">
                          {{ p.name }}
                        </a>
                      </h3>

                      <p>{{ p.description }}</p>

                      <div class="d-flex justify-content-between border-top pt-3">
                        <b>
                          @if (p.mrp === null) {
                            Price on request
                          } @else {
                            MRP ₹{{ p.mrp }}
                          }
                        </b>

                        <a [routerLink]="['/product', p.slug]">
                          Details ↗
                        </a>
                      </div>
                    </div>
                  </article>
                </div>
              }
            </div>
          }
        }
      </div>
    </section>
  `
})
export class CatalogueComponent implements OnInit {
  private api = inject(CatalogueService);
  private route = inject(ActivatedRoute);
  private searchChanges = new Subject<string>();

  brands: Brand[] = [];
  categories: Category[] = [];
  products: Product[] = [];

  search = '';
  brand = '';
  category = '';

  loading = true;
  error = '';

  ngOnInit(): void {
    this.api.getBrands().subscribe({
      next: (data) => {
        this.brands = data;
      },
      error: (error) => {
        console.error('Failed to load brands:', error);
      }
    });

    this.api.getCategories().subscribe({
      next: (data) => {
        this.categories = data;
      },
      error: (error) => {
        console.error('Failed to load categories:', error);
      }
    });

    this.searchChanges
      .pipe(
        debounceTime(350),
        distinctUntilChanged()
      )
      .subscribe(() => {
        this.load();
      });

    this.route.queryParamMap.subscribe((params) => {
      this.brand = params.get('brand') ?? '';
      this.load();
    });
  }

  onSearchChange(value: string): void {
    this.searchChanges.next(value);
  }

  load(): void {
    this.loading = true;
    this.error = '';

    this.api.getProducts({
      search: this.search,
      brand: this.brand,
      category: this.category
    }).subscribe({
      next: (data) => {
        this.products = data;
        this.loading = false;
      },
      error: (error) => {
        console.error('Failed to load products:', error);
        this.error = 'Could not load products from the API. Check the backend and database.';
        this.loading = false;
      }
    });
  }

  reset(): void {
    this.search = '';
    this.brand = '';
    this.category = '';
    this.load();
  }
}