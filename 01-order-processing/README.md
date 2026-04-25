# Order Processor

Automated Shopify order processing pipeline.

## Problem It Solves

Manual order processing is slow, error-prone, 
and doesn't scale. This system automatically:
- Filters pending orders
- Detects fraudulent orders
- Calculates tax and shipping
- Generates processing reports

## How It Works
Order arrives
↓
Skip if pending
↓
Check fraud rules
↓
Calculate tax (17%)
↓
Apply shipping rules
↓
Generate report

## Fraud Detection Rules

- High risk country flag
- High value + new customer flag
- Automatic skip on fraud detection

## Shipping Rules

- International → 1,500 PKR flat
- Domestic + above 3,000 PKR → Free
- Domestic + below 3,000 PKR → 300 PKR

## Tech Stack

- Python 3.11
- No external libraries (pure Python)

## Sample Output
======== Automated Order Processing ========
Order #5001
Customer: Adil Safi (adil@gmail.com)
Items:

Laptop Stand
Mouse
Keyboard
Subtotal: 7500.0 PKR
Tax (17%): 1275.0 PKR
Shipping: Free
Total: 8775.0 PKR

📊 PROCESSING REPORT
Total orders received: 5
Pending (skipped): 1
Flagged (fraud): 2
Successfully processed: 2
Total revenue: 14,040.0 PKR
