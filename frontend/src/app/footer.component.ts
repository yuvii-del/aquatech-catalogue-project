import { Component } from '@angular/core';
import { RouterLink } from '@angular/router';

@Component({
  selector: 'app-footer',
  standalone: true,
  imports: [RouterLink],
  template: `
    <footer class="site-footer">
      <div class="container footer-content">
        <div class="footer-brand">
          <a routerLink="/" class="footer-logo">
          <img
            src="https://res.cloudinary.com/gxybnegl/image/upload/v1793080258/aqua_tech.png"
            alt="Aakash AquaTech Logo"
            class="footer-brand-logo"
          />

          <span>
            <strong>Aakash AquaTech</strong>
            <small>PURE WATER. BETTER LIVING.</small>
          </span>
        </a>

          <p>
            Explore water purification products for homes and businesses.
            Contact our team for product enquiries and service assistance.
          </p>
        </div>

        <div class="footer-links">
          <h5>Quick Links</h5>
          <a routerLink="/">Home</a>
          <a routerLink="/catalogue">Product Catalogue</a>
          <a routerLink="/about">About Us</a>
          <a routerLink="/contact">Contact Us</a>
        </div>

        <div class="footer-contact">
          <h5>Contact Us</h5>
          <p>Need help choosing a product?</p>
          <a routerLink="/contact" class="footer-contact-link">
            Get in touch →
          </a>
          <a
            href="https://wa.me/91XXXXXXXXXX?text=Hello%20Aakash%20AquaTech"
            target="_blank"
            rel="noopener noreferrer"
            class="footer-whatsapp"
          >
            WhatsApp Enquiry
          </a>
        </div>
      </div>

      <div class="footer-bottom">
        <div class="container">
          <span>© {{ year }} Aakash AquaTech. All rights reserved.</span>
          <span>Pure Water. Better Living.</span>
        </div>
      </div>
    </footer>
  `
})
export class FooterComponent {
  year = new Date().getFullYear();
}