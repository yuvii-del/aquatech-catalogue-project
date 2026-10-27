import { Component, OnInit, inject } from '@angular/core';
import { ActivatedRoute, RouterLink } from '@angular/router';
import { CatalogueService } from '../catalogue.service';
import { Product } from '../models';

@Component({
  selector: 'app-product-detail',
  standalone: true,
  imports: [RouterLink],
  template: `
    <section class="page-banner">
      <div class="container">
        <a routerLink="/catalogue" class="back-link">
          ← Back to Catalogue
        </a>

        <small class="d-block mt-3">PRODUCT DETAILS</small>
        <h1>{{ product?.name || 'Product Details' }}</h1>
        <p>Discover product features and contact us for enquiries.</p>
      </div>
    </section>

    <section class="section">
      <div class="container">

        @if (loading) {
          <div class="text-center py-5">
            <p>Loading product details...</p>
          </div>
        } @else if (error) {
          <div class="alert alert-warning">
            {{ error }}
          </div>

          <a routerLink="/catalogue" class="btn btn-outline-brand">
            Browse Catalogue
          </a>
        } @else if (product) {

          <!-- Product overview -->
          <div class="row g-4 align-items-start">
            <div class="col-12 col-md-6">
              <div class="product-detail-image-wrapper">
                <img
                  [src]="product.image_url"
                  [alt]="product.name"
                  class="product-detail-image"
                />
              </div>
            </div>

            <div class="col-12 col-md-6 product-detail-info">
              <small class="meta">
                {{ product.brand.name }} ·
              {{ product.category.name }}
              </small>

              <h2 class="mt-3">{{ product.name }}</h2>

              <p class="product-model">
                <strong>Model Number:</strong>
                {{ product.model_number }}
              </p>

              <p class="product-description">
                {{ product.description }}
              </p>

              <div class="product-detail-price">
                @if (product.mrp === null) {
                  <span>Price on request</span>
                } @else {
                  <span>Leaflet MRP: ₹{{ product.mrp }}</span>
                }
              </div>

              <div class="product-detail-actions">
                <a
                  [href]="whatsappLink"
                  target="_blank"
                  rel="noopener noreferrer"
                  class="btn btn-success"
                >
                  Enquire on WhatsApp
                </a>

                <a
                  routerLink="/catalogue"
                  class="btn btn-outline-brand"
                >
                  ← Back to Catalogue
                </a>
              </div>

              <div class="product-note mt-4">
                <strong>Need assistance?</strong>
                <p>
                  Contact our team for product availability, pricing,
                  installation, and service information.
                </p>
              </div>
            </div>
          </div>

          <!-- Product highlights -->
          <section class="product-info-section">
            <h2>Product Highlights</h2>

            @if (highlights.length > 0) {
              <ul class="highlights-list">
                @for (highlight of highlights; track $index) {
                  <li>{{ highlight }}</li>
                }
              </ul>
            } @else {
              <p class="empty-message">
                No product highlights are available.
              </p>
            }
          </section>

          <!-- Technical specifications -->
          <section class="product-info-section">
            <h2>Technical Specifications</h2>

            @if (specifications.length > 0) {
              @for (spec of specifications; track $index) {
                <div class="specification-group">
                  <h3>{{ spec.title }}</h3>

                  <table class="specification-table">
                    <tbody>
                      @for (item of spec.items; track $index) {
                        <tr>
                          <th>{{ item.name }}</th>
                          <td>{{ item.value }}</td>
                        </tr>
                      }
                    </tbody>
                  </table>
                </div>
              }
            } @else {
              <p class="empty-message">
                No technical specifications are available.
              </p>
            }
          </section>

          <!-- Product features -->
          <section class="product-info-section">
            <h2>Product Features</h2>

            @if (features.length > 0) {
              <div class="features-grid">
                @for (feature of features; track $index) {
                  <article class="feature-card">
                    @if (feature.image) {
                      <img
                        [src]="feature.image"
                        [alt]="feature.title"
                        loading="lazy"
                      />
                    }

                    <h3>{{ feature.title }}</h3>
                    <p>{{ feature.description }}</p>
                  </article>
                }
              </div>
            } @else {
              <p class="empty-message">
                No product features are available.
              </p>
            }
          </section>

        }
      </div>
    </section>
  `,
  styles: [`
    .product-info-section {
      margin-top: 40px;
      padding: 28px;
      background: #fff;
      border: 1px solid #e5e7eb;
      border-radius: 14px;
    }

    .product-info-section h2 {
      margin-bottom: 22px;
      color: #123b56;
      font-size: 25px;
      font-weight: 700;
    }

    .highlights-list {
      margin: 0;
      padding-left: 24px;
      color: #475569;
      line-height: 1.9;
    }

    .highlights-list li {
      padding: 4px 0;
    }

    .specification-group {
      margin-bottom: 28px;
    }

    .specification-group:last-child {
      margin-bottom: 0;
    }

    .specification-group h3,
    .feature-card h3 {
      margin-bottom: 14px;
      color: #087e8b;
      font-size: 18px;
      font-weight: 600;
    }

    .specification-table {
      width: 100%;
      border-collapse: collapse;
    }

    .specification-table th,
    .specification-table td {
      padding: 13px 15px;
      border-bottom: 1px solid #e5e7eb;
      text-align: left;
      vertical-align: top;
    }

    .specification-table th {
      width: 40%;
      color: #334155;
      font-weight: 600;
    }

    .specification-table td {
      color: #475569;
    }

    .features-grid {
      display: grid;
      grid-template-columns: repeat(3, minmax(0, 1fr));
      gap: 20px;
    }

    .feature-card {
      padding: 20px;
      border: 1px solid #e5e7eb;
      border-radius: 12px;
      background: #fff;
    }

    .feature-card img {
      display: block;
      width: 100%;
      height: 160px;
      margin-bottom: 18px;
      object-fit: contain;
    }

    .feature-card p,
    .empty-message {
      margin-bottom: 0;
      color: #475569;
      line-height: 1.7;
    }

    @media (max-width: 767px) {
      .product-info-section {
        margin-top: 28px;
        padding: 18px;
      }

      .features-grid {
        grid-template-columns: 1fr;
      }

      .specification-table th,
      .specification-table td {
        padding: 10px 8px;
        overflow-wrap: anywhere;
      }
    }
  `]
})
export class ProductDetailComponent implements OnInit {
  private route = inject(ActivatedRoute);
  private api = inject(CatalogueService);

  product: Product | null = null;
  loading = true;
  error = '';
  whatsappLink = '';

  get highlights(): string[] {
    return this.product?.highlights ?? [];
  }

  get specifications(): Product['specifications'] {
    return this.product?.specifications ?? [];
  }

  get features(): Product['features'] {
    return this.product?.features ?? [];
  }

  ngOnInit(): void {
    this.route.paramMap.subscribe(params => {
      const slug = params.get('slug');

      if (!slug) {
        this.error = 'Product slug is missing.';
        this.loading = false;
        return;
      }

      this.loading = true;
      this.error = '';
      this.product = null;

      this.api.getProduct(slug).subscribe({
        next: (data: Product) => {
          console.log('Product API response:', data);
          console.log('Highlights:', data.highlights);
          console.log('Specifications:', data.specifications);
          console.log('Features:', data.features);

          this.product = {
            ...data,
            highlights: Array.isArray(data.highlights)
              ? data.highlights
              : [],
            specifications: Array.isArray(data.specifications)
              ? data.specifications
              : [],
            features: Array.isArray(data.features)
              ? data.features
              : []
          };

          const message = encodeURIComponent(
            `Hello AquaTech, I am interested in ${data.name} ` +
            `(Model: ${data.model_number}). Please share more details.`
          );

          // Replace with your actual WhatsApp Business number.
          const whatsappNumber = '91XXXXXXXXXX';

          this.whatsappLink =
            `https://wa.me/${whatsappNumber}?text=${message}`;

          this.loading = false;
        },

        error: err => {
          console.error('Product loading failed:', err);

          this.error = err.status === 404
            ? 'This product was not found.'
            : 'Unable to load product details. Please try again.';

          this.loading = false;
        }
      });
    });
  }
}

