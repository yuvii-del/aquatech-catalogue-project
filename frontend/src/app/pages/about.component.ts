import { Component } from '@angular/core';
import { RouterLink } from '@angular/router';

@Component({
  standalone: true,
  imports: [RouterLink],
  template: `
    <section class="page-banner">
      <div class="container">
        <small>ABOUT US</small>
        <h1>Welcome to Aakash Aqua Tech</h1>
        <p>Water purification solutions for homes, businesses, and industries.</p>
      </div>
    </section>

    <section class="section">
      <div class="container">
        <div class="row align-items-center g-5">
          <div class="col-12 col-lg-6">
            <div class="about-image">
              <div class="water-icon">💧</div>
              <h2>Pure Water. Better Living.</h2>
              <p>Reliable water purification and service solutions.</p>
            </div>
          </div>

          <div class="col-12 col-lg-6">
            <small class="meta">WHO WE ARE</small>
            <h2 class="about-heading">
              Your Partner in Water Purification
            </h2>

            <p class="about-text">
              Aakash AquaTech helps customers explore water purification products
              and service options for their needs.
            </p>

            <p class="about-text">
              From product selection to maintenance enquiries, our goal is
              to make finding the right water solution easier.
            </p>

            <div class="about-points">
              <div>✓ Product catalogue</div>
              <div>✓ Home and business solutions</div>
              <div>✓ Service and maintenance enquiries</div>
            </div>

            <a routerLink="/catalogue" class="btn btn-brand mt-4">
              Explore Products →
            </a>
          </div>
        </div>
      </div>
    </section>

    <section class="section about-highlight">
      <div class="container text-center">
        <h2>Find the Right Water Solution</h2>
        <p>
          Browse available products and contact us for more information.
        </p>
        <a routerLink="/catalogue" class="btn btn-brand">
          Browse Catalogue
        </a>
      </div>
    </section>
  `
})
export class AboutComponent {}