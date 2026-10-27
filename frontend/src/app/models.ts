export interface Brand {
  id: number;
  name: string;
  slug: string;
  description: string;
  logo_url?: string | null;
}

export interface Category {
  id: number;
  name: string;
  slug: string;
  description: string;
}



export interface SpecificationItem {
  name: string;
  value: string;
}

export interface Specification {
  title: string;
  items: SpecificationItem[];
}

export interface ProductFeature {
  image?: string | null;
  title: string;
  description: string;
}

export interface Product {
  id: number;
  name: string;
  slug: string;
  model_number: string;
  description: string;
  image_url: string;
  mrp: number | null;
  featured: boolean;
  brand: Brand;
  category: Category;

  highlights: string[];
  specifications: Specification[];
  features: ProductFeature[];
}
