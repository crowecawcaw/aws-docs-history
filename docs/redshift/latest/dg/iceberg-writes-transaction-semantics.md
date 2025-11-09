Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Transaction semantics

Redshift Iceberg write queries support ACID and snapshot isolation. Write transactions
have guaranteed atomicity and do not produce partial updates when a query fails
unexpectedly.

Multiple Iceberg transactions can run concurrently, and if two transactions try to
modify the same table or partition concurrently, the transaction commit fails. This
ensures data integrity. When this happens, you must resolve the conflicts manually and
rerun the failed queries. Amazon Redshift doesn't automatically retry and resolve the
conflicts.

A single Iceberg write query is always treated as a single auto-commit transaction.
When an Iceberg write query, such as CREATE or INSERT query, is included in an explicit
transaction block, no other queries can run within the same transaction block. The
transaction will fail.

Following are some examples. The first example demonstrates that a single statement
query always auto-commits after the query finishes. In this scenario, you're creating a
new sales orders table:

```
CREATE TABLE sales_schema.orders (
    order_id int,
    customer_id int,
    order_date date,
    total_amount decimal(10,2)
) USING ICEBERG LOCATION 's3://my-data-lake/sales/orders/';
```

This example is an explicit transaction block for inserting a customer order using
three-part notation for an S3 table bucket. The transaction doesn't auto-commit after
the INSERT query, but instead commits and inserts the order data with the COMMIT
command:

```
BEGIN;
INSERT INTO "analytics_bucket@s3tablescatalog".sales_db.orders VALUES (12345, 9876, '2024-10-30', 299.99);
COMMIT;
```

This example is an explicit transaction block rollback scenario where you're testing
an order insertion but decide to cancel it. The transaction doesn't auto-commit after
the INSERT query, but instead rolls back with the ROLLBACK command without inserting the
test order.

```
BEGIN;
INSERT INTO sales_schema.orders VALUES (12346, 5432, '2024-10-30', 150.75);
ROLLBACK;
```

This final example demonstrates how, when you try to run another statement within the
same transaction block as the INSERT query, the transaction fails without inserting the
order data. In this scenario, you're attempting to insert an order and immediately query
the table:

```
BEGIN;
INSERT INTO sales_schema.orders VALUES (12347, 7890, '2024-10-30', 425.50);
SELECT * FROM sales_schema.orders WHERE order_id = 12347;
```

The only exception to this is the `DROP TABLE` statement, which always
behaves as an auto-commit statement and can't run within an explicit transaction block.
This is to maintain the same behavior as the `DROP TABLE` on an external
table. For more information, see [DROP TABLE](r_DROP_TABLE.md "r_DROP_TABLE.md").

###### Note

Iceberg write SQLs cannot be executed from within stored procedure.
