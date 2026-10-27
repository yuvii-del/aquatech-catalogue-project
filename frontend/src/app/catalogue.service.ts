import { Injectable, inject } from '@angular/core';
import { HttpClient, HttpParams } from '@angular/common/http';
import { Observable } from 'rxjs';
import { Brand, Category, Product } from './models';

@Injectable({providedIn:'root'})
export class CatalogueService {
  private http = inject(HttpClient);
  private api = 'http://127.0.0.1:8000/api';
  getBrands(): Observable<Brand[]> { return this.http.get<Brand[]>(`${this.api}/brands`); }
  getCategories(): Observable<Category[]> { return this.http.get<Category[]>(`${this.api}/categories`); }
  getProducts(filters:{search?:string;brand?:string;category?:string;featured?:boolean}={}):Observable<Product[]> {
    let params = new HttpParams();
    if (filters.search?.trim()) params=params.set('search',filters.search.trim());
    if (filters.brand) params=params.set('brand',filters.brand);
    if (filters.category) params=params.set('category',filters.category);
    if (filters.featured !== undefined) params=params.set('featured',String(filters.featured));
    return this.http.get<Product[]>(`${this.api}/products`,{params});
  }
  getProduct(slug:string):Observable<Product> { return this.http.get<Product>(`${this.api}/products/${encodeURIComponent(slug)}`); }
}
