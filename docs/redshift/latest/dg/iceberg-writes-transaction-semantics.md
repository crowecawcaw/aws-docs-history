

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# Transaction semantics
<a name="iceberg-writes-transaction-semantics"></a>

Amazon Redshift Iceberg write queries support ACID transactions. Write transactions are atomic: when a query or transaction fails, Amazon Redshift doesn't publish a partial update to the table.

By default, each Iceberg write query runs as its own auto-commit transaction, and Amazon Redshift publishes its changes as one Iceberg snapshot when the query finishes. You can also group multiple data manipulation language (DML) statements that write to one Iceberg table into a multi-statement transaction. Amazon Redshift then publishes all of the transaction's changes as one Iceberg snapshot when the transaction commits.

The following example creates a table with a single auto-commit statement:

```
CREATE TABLE sales_schema.orders (
    order_id int,
    customer_id int,
    order_date date,
    total_amount decimal(10,2)
) USING ICEBERG LOCATION 's3://my-data-lake/sales/orders/';
```

## Multi-statement transactions
<a name="iceberg-writes-multi-statement-transactions"></a>

You can run a multi-statement transaction in any of the following ways:
+ An explicit transaction block that starts with `BEGIN` or `START TRANSACTION` and ends with `COMMIT` or `END`. To discard the transaction's changes, end the block with `ROLLBACK` or `ABORT`.
+ A single query string that contains multiple statements separated by semicolons.
+ A JDBC connection with `autoCommit` set to `false`. The driver starts a transaction before your first statement, and the transaction ends when your application calls `commit()` or `rollback()`.

The following example applies a nightly batch of point-of-sale (POS) changes to a `sales` table. The `MERGE` statement adds new sales and corrects existing ones from the `pos_sales` Iceberg staging table. The `DELETE` statement removes the voided sales listed in the `pos_voids` Iceberg staging table. The `SELECT` statement checks the day's total before the transaction commits.

```
BEGIN;

-- Add new sales and correct existing ones
MERGE INTO iceberg_schema.sales USING iceberg_schema.pos_sales p
  ON sales.sale_id = p.sale_id
  WHEN MATCHED THEN UPDATE SET amount = p.amount
  WHEN NOT MATCHED THEN INSERT VALUES (p.sale_id, p.store_id, p.sale_date, p.amount);

-- Remove voided sales
DELETE FROM iceberg_schema.sales
  WHERE sale_id IN (SELECT sale_id FROM iceberg_schema.pos_voids);

-- Check the day's total, which includes both changes
SELECT sum(amount) FROM iceberg_schema.sales
  WHERE sale_date = '2026-10-06';

-- COMMIT if the total is correct; otherwise ROLLBACK
COMMIT;
```

The `SELECT` statement sees the changes from the `MERGE` and `DELETE` statements, because reads of the table that a transaction writes include the transaction's uncommitted changes. Other sessions and other engines don't see any of the changes until `COMMIT`. They see the table as it was either before the batch or after it, but never in between.

If any statement in the transaction fails, or if you end the transaction with `ROLLBACK`, Amazon Redshift doesn't publish any of the transaction's changes. The following example inserts an order, updates it, and then rolls back both changes:

```
BEGIN;
INSERT INTO "analytics-bucket@s3tablescatalog".sales_db.orders VALUES (12346, 5432, '2026-10-06', 150.75);
UPDATE "analytics-bucket@s3tablescatalog".sales_db.orders SET total_amount = 160.75 WHERE order_id = 12346;
ROLLBACK;  -- discards both the INSERT and the UPDATE
```

## Statements allowed in a multi-statement transaction
<a name="iceberg-writes-transaction-statements-allowed"></a>

A transaction that writes to an Iceberg table can read from any tables, but it can write to only that one Iceberg table. The following table shows which statements you can run in a transaction that contains an Iceberg write.


| Statement | Behavior | 
| --- | --- | 
| SELECT from any tables, including Iceberg tables, Redshift managed storage (RMS) tables, and other external tables, in any database | Allowed | 
| INSERT, UPDATE, DELETE, and MERGE on one Iceberg table | Allowed. Published as one snapshot at COMMIT. | 
| REFRESH MATERIALIZED VIEW on one Iceberg materialized view | Allowed. The materialized view is the transaction's write target. | 
| A write to a second Iceberg table | Not allowed | 
| Any other write, before or after the Iceberg write, such as DML on an RMS table or temporary table, COPY, UNLOAD, GRANT, REVOKE, ANALYZE, or DDL | Not allowed | 
| Iceberg DDL: CREATE TABLE, CREATE TABLE AS, ALTER TABLE, CREATE MATERIALIZED VIEW, DROP TABLE, and DROP MATERIALIZED VIEW | Not allowed | 

When you run a statement that isn't allowed, the statement fails and Amazon Redshift aborts the transaction. None of the changes made earlier in the transaction are published. In the following example, the second `DELETE` statement fails because it writes to a second Iceberg table:

```
BEGIN;
DELETE FROM iceberg_schema.sales
  WHERE sale_id IN (SELECT sale_id FROM iceberg_schema.pos_voids);
DELETE FROM iceberg_schema.pos_voids;  -- fails: a second Iceberg table
COMMIT;                                -- rolls back
```

To write to another table, run that write in its own transaction, before or after the Iceberg transaction. Run Iceberg DDL statements, such as `CREATE TABLE` and `ALTER TABLE`, as standalone statements outside a transaction block. If your client turns off autocommit, turn it on before you run Iceberg DDL statements.

## Referencing the table in a transaction
<a name="iceberg-writes-transaction-referencing"></a>

Amazon Redshift identifies an Iceberg table in a transaction by the name that you use to reference it. Use the same name for the table throughout the transaction. If you reference one table through two names, for example through two external schemas, or through an external schema and the `awsdatacatalog` catalog, Amazon Redshift treats the two names as two different tables. A write through the second name fails, and a read through the second name doesn't include the transaction's uncommitted changes. For more information, see [Referencing Iceberg tables in Amazon Redshift](https://docs.aws.amazon.com/redshift/latest/dg/referencing-iceberg-tables.html).

## Isolation guarantees
<a name="iceberg-writes-transaction-isolation"></a>

A transaction on Iceberg tables gives you the following guarantees:
+ **Atomic publish**: Other sessions and engines see none of a transaction's changes until `COMMIT`, and then see all of them in one snapshot.
+ **Read your own writes**: Reads of the Iceberg table that a transaction writes include the transaction's uncommitted changes, as long as the transaction uses the same name for the table.
+ **Repeatable reads**: The first statement that reads or writes an Iceberg table in a transaction fixes the version of that table for the rest of the transaction. Later reads of the table in the same transaction don't see changes that other sessions commit in the meantime.

Amazon Redshift fixes the version of each Iceberg table when the transaction first reads or writes that table, not when the transaction begins. If a transaction first accesses an Iceberg table later in the transaction, that read can include changes that other sessions committed after the transaction started.

Reads of RMS tables in the same transaction use the Amazon Redshift transaction snapshot, so they might not reflect the same point in time as reads of Iceberg tables. For more information, see [Isolation levels in Amazon Redshift](https://docs.aws.amazon.com/redshift/latest/dg/c_serial_isolation.html).

## Files from transactions that don't commit
<a name="iceberg-writes-transaction-orphan-files"></a>

As each statement in a multi-statement transaction runs, Amazon Redshift writes data files and intermediate metadata files to the table location. If the transaction doesn't commit, no snapshot references these files, and they become orphan files. To remove them, set up orphan file removal for the table. For more information, see [Best practices](iceberg-writes-best-practices.md).

## Troubleshooting multi-statement transactions
<a name="iceberg-writes-transaction-troubleshooting"></a>

If a statement in a multi-statement transaction fails, Amazon Redshift aborts the transaction and doesn't publish any of its changes. The following are common errors and how to resolve them:
+ `Only a single Iceberg table can be written to in a multi-statement transaction involving Iceberg writes` or `Cannot write to a different database after an Iceberg write to a data lake catalog in the same transaction.` – The transaction writes to more than one table. Run each write to another table in its own transaction. If you reference the same Iceberg table through two names, such as two external schemas, use one name throughout the transaction.
+ `Iceberg DDL is not allowed in multi-statement transaction` – Run Iceberg DDL statements as standalone statements outside a transaction block.
+ `current transaction is aborted, commands ignored until end of transaction block` – An earlier statement in the transaction failed, so the transaction can't commit. Run `ROLLBACK` to end the transaction.

## Resolving concurrent write conflicts
<a name="iceberg-writes-transaction-conflicts"></a>

Multiple sessions and engines can write to the same Iceberg table at the same time. If another writer commits to the table while your write is running, and the two sets of changes don't overlap, Amazon Redshift can rebase your changes onto the latest version of the table and commit them without running the write again. If Amazon Redshift can't rebase your changes, for example because both writes changed the same data, the commit fails. When this happens, run the write again. For more information, see [Resolving concurrent write conflicts for Apache Iceberg tables in Amazon Redshift](https://docs.aws.amazon.com/redshift/latest/dg/iceberg-write-conflicts.html).

**Note**  
Iceberg write statements can't run inside a stored procedure.