import { Component } from '@angular/core';
import { RouterLink } from '@angular/router';

@Component({
  selector: 'app-contact',
  standalone: true,
  imports: [RouterLink],
  template: `
    <section class="page-banner">
      <div class="container">
        <small>GET IN TOUCH</small>
        <h1>Contact Aakash AquaTech</h1>
        <p>We are here to help with product enquiries and service assistance.</p>
      </div>
    </section>

    <section class="section">
      <div class="container">
        <div class="row g-4">
          <div class="col-12 col-md-4">
            <div class="contact-card">
              <h3>Our Products</h3>
              <p>Explore our water purification products.</p>
              <a routerLink="/catalogue">Browse Catalogue →</a>
            </div>
          </div>

          <div class="col-12 col-md-4">
            <div class="contact-card">
              <h3>Product Support</h3>
              <p>Contact our team for product details and availability.</p>
              <a routerLink="/about">About Us →</a>
            </div>
          </div>

          <div class="col-12 col-md-4">
            <div class="contact-card">
              <h3>WhatsApp Enquiry</h3>
              <p>Ask us about products and services.</p>
              <a
                href="https://wa.me/91XXXXXXXXXX?text=Hello%20Aakash%20AquaTech"
                target="_blank"
                rel="noopener noreferrer"
              >Chat on WhatsApp →</a>
            </div>
          </div>
        </div>
      </div>
    </section>
  `
})
export class ContactComponent {}