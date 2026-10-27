import { Component } from '@angular/core';
import { RouterLink, RouterLinkActive, RouterOutlet } from '@angular/router';
import { FooterComponent } from './footer.component';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [RouterLink, RouterLinkActive, RouterOutlet, FooterComponent],
  template: `
    <header class="site-header">
      <nav class="navbar navbar-expand-lg container py-3">
        <a routerLink="/" class="navbar-brand-custom">
        <img
          src="https://res.cloudinary.com/gxybnegl/image/upload/v1793080258/aqua_tech.png"
          alt="Aakash AquaTech Logo"
          class="navbar-company-logo"
        />

        <span class="navbar-brand-text">
          <strong>Aakash AquaTech</strong>
          <small>PURE WATER. BETTER LIVING.</small>
        </span>
      </a>
        <button
          class="navbar-toggler"
          type="button"
          data-bs-toggle="collapse"
          data-bs-target="#mainNav"
          aria-controls="mainNav"
          aria-expanded="false"
          aria-label="Toggle navigation"
        >
          <span class="navbar-toggler-icon"></span>
        </button>

        <div class="collapse navbar-collapse" id="mainNav">
          <div class="navbar-nav ms-auto">
            <a
              class="nav-link"
              routerLink="/"
              routerLinkActive="active"
              [routerLinkActiveOptions]="{ exact: true }"
            >Home</a>

            <a
              class="nav-link"
              routerLink="/catalogue"
              routerLinkActive="active"
            >Catalogue</a>

            <a
              class="nav-link"
              routerLink="/about"
              routerLinkActive="active"
            >About</a>

            <a
              class="nav-link"
              routerLink="/contact"
              routerLinkActive="active"
            >Contact</a>
          </div>
        </div>
      </nav>
    </header>

    <main>
      <router-outlet />
    </main>

   <app-footer/>
  `
})
export class AppComponent {
  year = new Date().getFullYear();
}