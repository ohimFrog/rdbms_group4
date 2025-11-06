CREATE TABLE IF NOT EXISTS drug (
    id SERIAL PRIMARY KEY,
    lang_id INTEGER REFERENCES lang(id),
    product_name VARCHAR(700) NOT NULL,
    company_id INTEGER REFERENCES company(id),
    effect VARCHAR(500),
    dosage VARCHAR(1000),
    dprecaution VARCHAR(1500),
    interaction VARCHAR(1000),
    side_effect VARCHAR(1200),
    storage VARCHAR(300)
)

CREATE TABLE IF NOT EXISTS company (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL
)

CREATE TABLE IF NOT EXISTS lang (
    id SERIAL PRIMARY KEY,
    code VARCHAR(10) NOT NULL,
    name VARCHAR(100) NOT NULL
)

CREATE TABLE IF NOT EXISTS user (
    id SERIAL PRIMARY KEY,
    username VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    password_hash VARCHAR(255) NOT NULL
)

CREATE TABLE IF NOT EXISTS feedback (
    id SERIAL PRIMARY KEY,
    drug_id INTEGER REFERENCES drug(id),
    user_name VARCHAR(255),
    comments TEXT,
    positive BOOLEAN,
)