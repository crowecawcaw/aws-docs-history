

# Limitations and notes for the Maxio connector

The following are limitations and notes for the Maxio connector:
+ Maxio is supported as a source only. Writing to Maxio is not supported.
+ Job bookmarks are not supported.
+ 200 records per read without partitioning. Maxio returns no next-page value, so each read is one 200-record page. customer, invoice, product, component, product-family, credit-note and subscription-component-usage go past it with date partitioning; the other entities are capped at 200 (allocation at Maxio's 50 most recent).
+ invoice: `subscription_id` supports equality only. Range predicates on it are rejected by Maxio (HTTP 422). Use range on `created_at`.
+ Nested discovery lists the first 200 subscriptions as parents, for the same pagination reason.
+ The `subscription-component-usage` and `allocation` entities read one subscription-and-component pair at a time. Usage is capped at one 200-record page for each pair; use the `created_at` date range (partitioning via `since_date`/`until_date`) to read more. Allocations return at most the 50 most recent records for each pair.