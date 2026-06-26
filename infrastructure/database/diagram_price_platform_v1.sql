-- Tabla de tiendas
CREATE TABLE stores (
  id SERIAL PRIMARY KEY,
  name VARCHAR NOT NULL UNIQUE,
  website VARCHAR NOT NULL UNIQUE,
  country VARCHAR NOT NULL,
  created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

-- Tabla de marcas
CREATE TABLE brands (
  id SERIAL PRIMARY KEY,
  name VARCHAR NOT NULL UNIQUE,
  slug VARCHAR NOT NULL UNIQUE,
  created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

-- Tabla de categorías
CREATE TABLE categories (
  id SERIAL PRIMARY KEY,
  name VARCHAR NOT NULL,
  slug VARCHAR NOT NULL UNIQUE,
  parent_id INT REFERENCES categories(id),
  created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

-- Tabla de productos
CREATE TABLE products (
  id SERIAL PRIMARY KEY,
  name VARCHAR NOT NULL,
  slug VARCHAR NOT NULL UNIQUE,
  description TEXT,
  brand_id INT REFERENCES brands(id) ON DELETE SET NULL,
  category_id INT REFERENCES categories(id) ON DELETE SET NULL,
  created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

-- Tabla de variantes de producto
CREATE TABLE product_variants (
  id SERIAL PRIMARY KEY,
  product_id INT NOT NULL REFERENCES products(id) ON DELETE CASCADE,
  sku VARCHAR UNIQUE,
  ean VARCHAR UNIQUE,
  color VARCHAR,
  storage VARCHAR,
  ram VARCHAR,
  model_number VARCHAR,
  created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  CONSTRAINT uq_product_variant UNIQUE (product_id, color, storage, ram)
);

-- Tabla de ofertas de producto
CREATE TABLE product_offers (
  id SERIAL PRIMARY KEY,
  product_variant_id INT NOT NULL REFERENCES product_variants(id) ON DELETE CASCADE,
  store_id INT NOT NULL REFERENCES stores(id) ON DELETE CASCADE,
  product_url VARCHAR,
  last_price NUMERIC(12,2),
  last_scraped_at TIMESTAMP,
  is_available BOOLEAN NOT NULL DEFAULT TRUE,
  created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  CONSTRAINT uq_variant_store UNIQUE (product_variant_id, store_id)
);

-- Tabla de historial de precios
CREATE TABLE price_history (
  id SERIAL PRIMARY KEY,
  offer_id INT NOT NULL REFERENCES product_offers(id) ON DELETE CASCADE,
  price NUMERIC(12,2),
  original_price NUMERIC(12,2),
  discount_percentage NUMERIC(5,2),
  currency CHAR(3) NOT NULL,
  scraped_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

-- Índices para búsquedas frecuentes
CREATE INDEX idx_products_name ON products(name);
CREATE INDEX idx_products_slug ON products(slug);
CREATE INDEX idx_brands_slug ON brands(slug);
CREATE INDEX idx_categories_slug ON categories(slug);
CREATE INDEX idx_product_variants_product ON product_variants(product_id);
CREATE INDEX idx_product_variants_sku ON product_variants(sku);
CREATE INDEX idx_product_variants_ean ON product_variants(ean);
CREATE INDEX idx_product_offers_store ON product_offers(store_id);
CREATE INDEX idx_price_history_offer ON price_history(offer_id);
CREATE INDEX idx_price_history_scraped ON price_history(scraped_at);
