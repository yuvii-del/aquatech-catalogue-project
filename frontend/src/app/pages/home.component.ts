import { Component, OnInit, inject } from '@angular/core';
import { RouterLink } from '@angular/router';
import { CatalogueService } from '../catalogue.service';
import { Product } from '../models';

@Component({
  selector: 'app-home',
  standalone: true,
  imports: [RouterLink],
  template: `
    <!-- Hero Section -->
    <section class="hero">
      <div class="container hero-grid">
        <div class="hero-content">
          <span class="eyebrow">WATER SOLUTIONS CATALOGUE</span>

          <h1>
            Find the right water solution for
            <em>your space.</em>
          </h1>

          <p class="lead-copy">
            Explore products by brand and category in one simple catalogue.
          </p>

          <a routerLink="/catalogue" class="btn btn-brand btn-lg mt-3">
            Browse catalogue →
          </a>

          <p class="hero-small mt-4">
            Simple browsing · Clear product details · Mobile friendly
          </p>
        </div>

        <div class="hero-art">
          <div class="company-logo-circle">
            <img
              src="https://res.cloudinary.com/gxybnegl/image/upload/v1793080258/aqua_tech.png"
              alt="Aakash AquaTech company logo"
              class="hero-company-logo"
            />
          </div>

          <div class="iso-card">
            <img
              src="https://res.cloudinary.com/gxybnegl/image/upload/v1793080258/ISO.png"
              alt="ISO certification"
              class="iso-logo"
            />
          </div>
        </div>
      </div>
    </section>

    <!-- Browse by Brand -->
    <section class="section">
      <div class="container">
        <div class="section-title">
          <div>
            <small>START EXPLORING</small>
            <h2>Browse by brand</h2>
          </div>

          <a routerLink="/catalogue">View all products →</a>
        </div>

        <div class="row g-3 brand-grid">
          @for (brand of brandCards; track brand.slug) {
            <div class="col-12 col-md-4">
              <a
                class="brand-tile"
                [routerLink]="['/catalogue']"
                [queryParams]="{ brand: brand.slug }"
              >
                <b>{{ brand.symbol }}</b>

                <span>
                  <strong>{{ brand.name }}</strong>
                  <small>{{ brand.caption }}</small>
                </span>

                <i>↗</i>
              </a>
            </div>
          }
        </div>

        <!-- Featured Products -->
        <div class="section-title featured-heading">
          <div>
            <small>FEATURED</small>
            <h2>Featured products</h2>
          </div>

          <a routerLink="/catalogue">Explore all →</a>
        </div>

        @if (loading) {
          <div class="loading-message">
            <p>Loading catalogue...</p>
          </div>
        } @else if (error) {
          <div class="alert alert-warning">
            {{ error }}
          </div>
        } @else if (products.length === 0) {
          <div class="empty">
            <h3>No featured products available</h3>
            <p>
              Explore our complete catalogue to browse available products.
            </p>

            <a routerLink="/catalogue" class="btn btn-brand">
              View all products →
            </a>
          </div>
        } @else {
          <div class="row g-4 product-grid">
            @for (p of products; track p.id) {
              <div class="col-12 col-sm-6 col-lg-4">
                <article class="product-card">
                  <a
                    [routerLink]="['/product', p.slug]"
                    class="product-image-link"
                  >
                    <img
                      [src]="p.image_url"
                      [alt]="p.name"
                      loading="lazy"
                    />
                  </a>

                  <div class="product-card-content">
                    <small class="meta">
                      {{ p.brand.name }} · {{ p.category.name }}
                    </small>

                    <h3>
                      <a [routerLink]="['/product', p.slug]">
                        {{ p.name }}
                      </a>
                    </h3>

                    <p class="product-description">
                      {{ p.description }}
                    </p>

                    <div class="product-card-footer">
                      <strong>
                        @if (p.mrp === null) {
                          Price on request
                        } @else {
                          MRP ₹{{ p.mrp }}
                        }
                      </strong>

                      <a [routerLink]="['/product', p.slug]">
                        View details →
                      </a>
                    </div>
                  </div>
                </article>
              </div>
            }
          </div>
        }
      </div>
    </section>

    <!-- Bottom Call to Action -->
    <section class="cta">
      <div class="container cta-content">
        <div>
          <span class="cta-eyebrow">AQUATECH CATALOGUE</span>

          <h2>Find the right water solution for your needs.</h2>

          <p>
            Explore products and contact our team for assistance.
          </p>
        </div>

        <a routerLink="/catalogue" class="btn btn-light btn-lg">
          Explore products →
        </a>
      </div>
    </section>
  `,

  styles: [`
    :host {
      display: block;
      width: 100%;
      overflow-x: clip;
    }

    /* Hero section */
    .hero {
      width: 100%;
      padding: 64px 0 72px;
      background:
        radial-gradient(
          circle at 78% 42%,
          rgba(209, 244, 239, 0.75),
          transparent 36%
        ),
        linear-gradient(115deg, #ffffff 0%, #f1fbf9 100%);
    }

    .hero-grid {
      display: grid;
      grid-template-columns: minmax(0, 1.15fr) minmax(300px, 0.85fr);
      align-items: center;
      gap: 48px;
    }

    .hero-content {
      min-width: 0;
    }

    .eyebrow {
      display: inline-block;
      margin-bottom: 20px;
      color: #087e8b;
      font-size: 11px;
      font-weight: 700;
      letter-spacing: 1.6px;
    }

    .hero h1 {
      max-width: 680px;
      margin: 0 0 20px;
      color: #15363b;
      font-size: clamp(38px, 4.2vw, 64px);
      font-weight: 750;
      line-height: 1.12;
      letter-spacing: -2px;
    }

    .hero h1 em {
      color: #087e8b;
      font-style: normal;
    }

    .lead-copy {
      max-width: 500px;
      margin-bottom: 0;
      color: #64748b;
      font-size: 17px;
      line-height: 1.8;
    }

    .hero-small {
      color: #64748b;
      font-size: 12px;
    }

    /* Company logo */
    .hero-art {
      position: relative;
      display: flex;
      align-items: center;
      justify-content: center;
      min-width: 0;
      min-height: 340px;
      padding: 24px 50px 24px 20px;
    }

    .company-logo-circle {
      display: flex;
      align-items: center;
      justify-content: center;
      width: 250px;
      height: 250px;
      flex: 0 0 auto;
      overflow: hidden;
      box-sizing: border-box;
      border: 3px solid #159b9e;
      border-radius: 50%;
      background: #fff;
      box-shadow: 0 16px 40px rgba(8, 126, 139, 0.12);
    }

    .hero-company-logo {
      display: block;
      width: 100%;
      height: 100%;
      object-fit: contain;
    }

    /* ISO certification */
    .iso-card {
      position: absolute;
      top: 12%;
      right: 0;
      z-index: 2;
      display: flex;
      align-items: center;
      justify-content: center;
      width: 125px;
      height: 115px;
      padding: 10px;
      box-sizing: border-box;
      border: 1px solid #e5e7eb;
      border-radius: 16px;
      background: #fff;
      box-shadow: 0 12px 28px rgba(15, 50, 60, 0.09);
    }

    .iso-logo {
      display: block;
      width: 100%;
      height: 100%;
      object-fit: contain;
    }

    /* Main content sections */
    .section {
      width: 100%;
      padding: 56px 0 64px;
      background: #fff;
    }

    .section-title {
      display: flex;
      align-items: flex-end;
      justify-content: space-between;
      gap: 20px;
      margin-bottom: 24px;
    }

    .section-title small {
      display: block;
      margin-bottom: 10px;
      color: #087e8b;
      font-size: 10px;
      font-weight: 700;
      letter-spacing: 1.5px;
    }

    .section-title h2 {
      margin: 0;
      color: #15363b;
      font-size: clamp(25px, 3vw, 34px);
      font-weight: 700;
      letter-spacing: -0.8px;
    }

    .section-title > a {
      flex-shrink: 0;
      color: #087e8b;
      font-size: 14px;
      font-weight: 600;
      text-decoration: none;
    }

    .section-title > a:hover {
      text-decoration: underline;
    }

    /* Brand cards */
    .brand-grid {
      margin-bottom: 56px;
    }

    .brand-tile {
      display: flex;
      align-items: center;
      gap: 14px;
      min-height: 105px;
      height: 100%;
      padding: 20px;
      color: #15363b;
      text-decoration: none;
      border: 1px solid #e2ecec;
      border-radius: 14px;
      background: #fff;
      transition:
        transform 0.2s ease,
        box-shadow 0.2s ease,
        border-color 0.2s ease;
    }

    .brand-tile:hover {
      transform: translateY(-3px);
      border-color: #159b9e;
      box-shadow: 0 10px 25px rgba(8, 126, 139, 0.08);
    }

    .brand-tile > b {
      display: flex;
      align-items: center;
      justify-content: center;
      width: 44px;
      height: 44px;
      flex-shrink: 0;
      color: #087e8b;
      font-size: 20px;
      border-radius: 12px;
      background: #eaf7f6;
    }

    .brand-tile > span {
      display: flex;
      flex: 1;
      flex-direction: column;
      gap: 5px;
      min-width: 0;
    }

    .brand-tile strong {
      font-size: 14px;
      overflow-wrap: anywhere;
    }

    .brand-tile small {
      color: #64748b;
      font-size: 12px;
    }

    .brand-tile > i {
      color: #087e8b;
      font-size: 16px;
      font-style: normal;
    }

    .featured-heading {
      margin-bottom: 24px;
    }

    /* Product cards */
    .product-grid {
      align-items: stretch;
    }

    .product-card {
      height: 100%;
      overflow: hidden;
      border: 1px solid #e5ecec;
      border-radius: 14px;
      background: #fff;
      transition:
        transform 0.2s ease,
        box-shadow 0.2s ease;
    }

    .product-card:hover {
      transform: translateY(-3px);
      box-shadow: 0 12px 28px rgba(15, 50, 60, 0.08);
    }

    .product-image-link {
      display: flex;
      align-items: center;
      justify-content: center;
      height: 240px;
      padding: 20px;
      background: #f8fbfb;
    }

    .product-image-link img {
      display: block;
      width: 100%;
      height: 100%;
      object-fit: contain;
    }

    .product-card-content {
      display: flex;
      flex-direction: column;
      padding: 20px;
    }

    .meta {
      color: #64748b;
      font-size: 12px;
    }

    .product-card h3 {
      margin: 12px 0;
      font-size: 20px;
      font-weight: 700;
    }

    .product-card h3 a {
      color: #15363b;
      text-decoration: none;
    }

    .product-card h3 a:hover {
      color: #087e8b;
    }

    .product-description {
      flex: 1;
      color: #64748b;
      font-size: 14px;
      line-height: 1.7;
    }

    .product-card-footer {
      display: flex;
      flex-wrap: wrap;
      align-items: center;
      justify-content: space-between;
      gap: 12px;
      margin-top: 12px;
      padding-top: 16px;
      border-top: 1px solid #e5ecec;
    }

    .product-card-footer strong {
      color: #15363b;
      font-size: 14px;
    }

    .product-card-footer a {
      color: #087e8b;
      font-size: 13px;
      font-weight: 600;
      text-decoration: none;
    }

    .product-card-footer a:hover {
      text-decoration: underline;
    }

    .loading-message,
    .empty {
      padding: 32px 20px;
      text-align: center;
      border: 1px solid #e2ecec;
      border-radius: 14px;
      background: #fbfdfd;
    }

    .loading-message p,
    .empty p {
      margin: 0;
      color: #64748b;
    }

    .empty h3 {
      margin-bottom: 10px;
      color: #15363b;
      font-size: 20px;
    }

    .empty .btn {
      margin-top: 20px;
    }

    /* Bottom CTA */
    .cta {
      position: relative;
      display: block;
      width: 100%;
      margin: 0;
      padding: 44px 0;
      color: #fff;
      background: linear-gradient(120deg, #087e8b, #075b68);
    }

    .cta-content {
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 30px;
    }

    .cta-eyebrow {
      display: block;
      margin-bottom: 10px;
      color: #c4f0eb;
      font-size: 10px;
      font-weight: 700;
      letter-spacing: 1.5px;
    }

    .cta h2 {
      max-width: 620px;
      margin: 0;
      color: #fff;
      font-size: clamp(25px, 3vw, 36px);
      font-weight: 700;
      line-height: 1.3;
    }

    .cta p {
      margin: 12px 0 0;
      color: #e0f2f1;
      font-size: 14px;
    }

    .cta .btn {
      flex-shrink: 0;
      color: #075b68;
      font-weight: 600;
    }

    /* Tablet */
    @media (max-width: 991px) {
      .hero-grid {
        grid-template-columns: minmax(0, 1fr) minmax(260px, 0.8fr);
        gap: 24px;
      }

      .hero h1 {
        font-size: clamp(36px, 5vw, 48px);
        letter-spacing: -1.3px;
      }

      .company-logo-circle {
        width: 210px;
        height: 210px;
      }

      .iso-card {
        width: 105px;
        height: 100px;
      }
    }

    /* Mobile */
    @media (max-width: 767px) {
      .hero {
        padding: 40px 0 32px;
      }

      .hero-grid {
        grid-template-columns: minmax(0, 1fr);
        gap: 20px;
      }

      .hero h1 {
        font-size: clamp(36px, 9vw, 46px);
        letter-spacing: -1.2px;
      }

      .lead-copy {
        font-size: 15px;
      }

      .hero-art {
        min-height: 265px;
        padding: 20px 45px 20px 15px;
      }

      .company-logo-circle {
        width: 195px;
        height: 195px;
      }

      .iso-card {
        top: 2%;
        right: 0;
        width: 90px;
        height: 85px;
        padding: 7px;
      }

      .section {
        padding: 40px 0;
      }

      .section-title {
        align-items: flex-start;
        gap: 12px;
      }

      .section-title h2 {
        font-size: 26px;
      }

      .section-title > a {
        padding-top: 18px;
        font-size: 12px;
      }

      .brand-grid {
        margin-bottom: 40px;
      }

      .brand-tile {
        min-height: 90px;
      }

      .product-image-link {
        height: 220px;
      }

      .cta {
        padding: 34px 0;
      }

      .cta-content {
        align-items: flex-start;
        flex-direction: column;
        gap: 22px;
      }

      .cta h2 {
        font-size: 27px;
      }
    }

    @media (prefers-reduced-motion: reduce) {
      .brand-tile,
      .product-card {
        transition: none;
      }
    }
  `]
})
export class HomeComponent implements OnInit {
  private api = inject(CatalogueService);

  products: Product[] = [];
  loading = true;
  error = '';

  brandCards = [
    {
      name: 'Aakash AquaTech',
      slug: 'aakash-aquatech',
      caption: 'Company catalogue',
      symbol: 'A'
    },
    {
      name: 'KENT',
      slug: 'kent',
      caption: 'Brand catalogue',
      symbol: 'K'
    },
    {
      name: 'Aquaguard',
      slug: 'aquaguard',
      caption: 'Brand catalogue',
      symbol: 'Q'
    }
  ];

  ngOnInit(): void {
    this.api.getProducts({ featured: true }).subscribe({
      next: (products) => {
        this.products = products;
        this.loading = false;
      },
      error: (err) => {
        console.error('Failed to load featured products:', err);

        this.error =
          'Could not load products. Please check the backend connection.';

        this.loading = false;
      }
    });
  }
}