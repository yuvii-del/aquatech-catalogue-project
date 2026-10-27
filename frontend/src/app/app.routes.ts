import { Routes } from '@angular/router';

import { HomeComponent } from './pages/home.component';
import { CatalogueComponent } from './pages/catalogue.component';
import { ProductDetailComponent } from './pages/product-detail.component';
import { AboutComponent } from './pages/about.component';

export const routes: Routes = [
  {
    path: '',
    component: HomeComponent,
    title: 'AquaTech | Home'
  },
  {
    path: 'catalogue',
    component: CatalogueComponent,
    title: 'Product Catalogue | AquaTech'
  },
  {
    path: 'product/:slug',
    component: ProductDetailComponent,
    title: 'Product Details | AquaTech'
  },
  {
    path: 'about',
    component: AboutComponent,
    title: 'About | AquaTech'
  },
  {
    path: 'contact',
    loadComponent: () =>
      import('./pages/contact.component').then(
        (m) => m.ContactComponent
      ),
    title: 'Contact | AquaTech'
  },
  {
    path: '**',
    redirectTo: ''
  }
];