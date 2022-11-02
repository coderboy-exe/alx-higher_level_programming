-- creates the table force_name (should not fail if table exists)
-- force_name description: id INT, name VARCHAR(256) can’t be null

CREATE TABLE IF NOT EXISTS force_name (
       id INT,
       name VARCHAR(256) NOT NULL
);
