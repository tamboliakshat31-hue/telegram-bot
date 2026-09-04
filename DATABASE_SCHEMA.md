# Subscription Plans Database Schema

This document describes the database schema for managing subscriptions.

## Users Table

```sql
CREATE TABLE users (
    user_id BIGINT PRIMARY KEY,
    username VARCHAR(255),
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    phone_number VARCHAR(20),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    last_active TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    is_premium BOOLEAN DEFAULT FALSE
);
```

## Subscriptions Table

```sql
CREATE TABLE subscriptions (
    subscription_id SERIAL PRIMARY KEY,
    user_id BIGINT NOT NULL,
    plan_type VARCHAR(50), -- '1_day', '7_days', '30_days', 'lifetime'
    price DECIMAL(10, 2),
    payment_status VARCHAR(20), -- 'pending', 'completed', 'failed'
    start_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    end_date TIMESTAMP,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE
);
```

## Payments Table

```sql
CREATE TABLE payments (
    payment_id SERIAL PRIMARY KEY,
    user_id BIGINT NOT NULL,
    subscription_id INT NOT NULL,
    amount DECIMAL(10, 2),
    currency VARCHAR(10) DEFAULT 'INR',
    payment_method VARCHAR(50), -- 'razorpay', 'paypal', etc.
    transaction_id VARCHAR(255) UNIQUE,
    status VARCHAR(20), -- 'success', 'failed', 'pending'
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    completed_at TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(user_id),
    FOREIGN KEY (subscription_id) REFERENCES subscriptions(subscription_id)
);
```

## Messages Table

```sql
CREATE TABLE messages (
    message_id SERIAL PRIMARY KEY,
    user_id BIGINT NOT NULL,
    chat_id BIGINT NOT NULL,
    message_text TEXT,
    message_type VARCHAR(50), -- 'text', 'photo', 'video', 'document'
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE
);
```

## Sample Data

### Users
```sql
INSERT INTO users (user_id, username, first_name) VALUES
(123456789, 'john_doe', 'John');
```

### Subscriptions
```sql
INSERT INTO subscriptions (user_id, plan_type, price, payment_status, end_date) VALUES
(123456789, '30_days', 399.00, 'completed', CURRENT_TIMESTAMP + INTERVAL '30 days');
```

## Queries

### Get active subscriptions
```sql
SELECT * FROM subscriptions 
WHERE payment_status = 'completed' 
AND end_date > CURRENT_TIMESTAMP;
```

### Get expired subscriptions
```sql
SELECT * FROM subscriptions 
WHERE end_date <= CURRENT_TIMESTAMP;
```

### Get user subscription status
```sql
SELECT u.*, s.plan_type, s.end_date 
FROM users u 
LEFT JOIN subscriptions s ON u.user_id = s.user_id 
WHERE u.user_id = $1;
```
