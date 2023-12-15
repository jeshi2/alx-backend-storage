-- Create the users table with specified attributes if not exists
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(255) NOT NULL UNIQUE,
    name VARCHAR(255),
    country ENUM('US', 'CO', 'TN') DEFAULT 'US' NOT NULL
);

-- Add the country column to the existing table if not exists
ALTER TABLE users
ADD COLUMN IF NOT EXISTS country ENUM('US', 'CO', 'TN') DEFAULT 'US' NOT NULL;