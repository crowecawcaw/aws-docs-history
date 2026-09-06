

# Working with foreign key constraints in Aurora DSQL
<a name="working-with-foreign-key-constraints"></a>

With foreign key constraints in Aurora DSQL, you can push an application's referential integrity logic into the database. Aurora DSQL supports the `NO ACTION`, `RESTRICT`, `CASCADE`, `SET NULL`, and `SET DEFAULT` referential actions. It also supports the `MATCH FULL` and `MATCH SIMPLE` match types, and deferrable foreign key constraints. For the full syntax breakdown, see [Foreign key constraints](create-table-syntax-support.md#create-table-foreign-keys).

## How Aurora DSQL maintains referential integrity
<a name="fk-dsql-occ"></a>

Aurora DSQL maintains referential integrity in two steps: snapshot verification as the transaction runs, and conflict resolution at commit time. Together, these steps guarantee that a committed transaction never violates a foreign key constraint.

**Snapshot verification.** Every transaction in Aurora DSQL runs against a consistent snapshot of the database taken at its start time. When you insert or update a referencing row, Aurora DSQL reads the referenced table at your transaction's start-time snapshot to confirm the referenced key exists. When you delete or update a referenced key, Aurora DSQL reads the referencing table in the transaction snapshot. It confirms that no referencing rows exist (for `RESTRICT`) or that the operation leaves no orphaned rows (for `NO ACTION`). Because this verification reads from the transaction start-time snapshot instead of taking a lock, other transactions can continue to modify the referenced and referencing tables in parallel.

**Commit-time resolution.** Snapshot verification ensures that the constraint held at the transaction's start time, but not between start and commit. A concurrent transaction can delete the referenced row or insert a conflicting referencing row after your transaction started. To adjudicate these conflicts, Aurora DSQL implicitly applies the `KEY SHARE` clause to referenced rows to detect whether any concurrent change invalidated your snapshot. If Aurora DSQL detects a conflict, it fails the transaction with a serialization error. For more information about how the `KEY SHARE` clause affects concurrent transactions, see [Concurrency control in Aurora DSQL](working-with-concurrency-control.md).

**Referential integrity checks incur extra reads**  
All data manipulation language (DML) operations on referenced or referencing tables incur extra reads to guarantee referential integrity. Before you add a foreign key constraint to a table, benchmark the workload and validate that the performance characteristics meet your expectations.

## Example scenarios
<a name="fk-occ-examples"></a>

In the following scenario, the `orders` table has a foreign key constraint on its `product_id` column that references the `products` table. This makes `products` the referenced table and `orders` the referencing table.

```
CREATE TABLE products (
    product_id integer PRIMARY KEY,
    name text,
    price numeric
);
CREATE TABLE orders (
    order_id integer PRIMARY KEY,
    product_id integer REFERENCES products,
    quantity integer
);
INSERT INTO products VALUES (1, 'Widget', 9.99);
```

### Conflict: concurrent delete and insert
<a name="fk-example-conflict"></a>

In this scenario, one session deletes a referenced row while another session inserts a referencing row.

```
-- Session A
BEGIN;
DELETE FROM products WHERE product_id = 1;

-- Session B
BEGIN;
INSERT INTO orders VALUES (100, 1, 5);

-- Session A
COMMIT;  -- succeeds

-- Session B
COMMIT;  -- fails with serialization error
ERROR: change conflicts with another transaction (OC000) (SQLSTATE 40001)
```

Both sessions run at the same time. Aurora DSQL resolves the conflict at commit. You can't end up with an order that points to a deleted product.

### No conflict: non-key column update
<a name="fk-example-no-conflict"></a>

In this scenario, one session updates a non-key column on the referenced row while another session inserts a referencing row.

```
-- Session A
BEGIN;
UPDATE products SET name = 'Super Widget' WHERE product_id = 1;

-- Session B
BEGIN;
INSERT INTO orders VALUES (101, 1, 3);

-- Session A
COMMIT;  -- succeeds

-- Session B
COMMIT;  -- succeeds
```

Updating `name` (a non-key column) doesn't conflict with the foreign key on `product_id`. The referencing row only cares that the referenced row's key columns stay the same.

## Best practices with foreign keys in Aurora DSQL
<a name="fk-occ-best-practices"></a>

Implement retry logic  
Conflicts cause errors instead of waits. Design your workload to retry failed transactions. For more information about concurrency in Aurora DSQL, see [Concurrency control in Aurora DSQL](working-with-concurrency-control.md).

Minimize key-column churn on heavily-referenced rows  
If multiple referencing rows reference the same row and its key columns change often, consider restructuring the schema. Move frequently-changing values to non-key columns so that the referenced column stays stable. Changing non-key columns on the referenced table doesn't conflict with referencing inserts.