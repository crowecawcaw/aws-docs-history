# DDL and distributed transactions in Aurora DSQL

Data definition language (DDL) behaves differently in Aurora DSQL from PostgreSQL. Aurora DSQL features
a Multi-AZ distributed and shared-nothing database layer built on top of multi-tenant compute
and storage fleets. Because no single primary database node or leader exists, the database
catalog is distributed. Thus, Aurora DSQL manages DDL schema changes as distributed
transactions.

Specifically, DDL behaves differently in Aurora DSQL as follows:

**Concurrency control errors**

Aurora DSQL returns a concurrency control violation error if you run one transaction
while another transaction updates a resource. For example, consider the following
sequence of actions:

1. In session 1, a user adds a column to the table `mytable`.
2. In session 2, a user attempts to insert a row into `mytable`.

Aurora DSQL returns the error `SQL Error [40001]: ERROR: schema has been updated
 by another transaction, please retry: (OC001).`

**DDL and DML in the same transaction**

Transactions in Aurora DSQL can contain only one DDL statement and can't have both DDL
and DML statements. This restriction means that you can't create a table and insert data
into the same table within the same transaction. For example, Aurora DSQL supports the
following sequential transactions.

```
BEGIN;
  CREATE TABLE mytable (ID_col integer);
COMMIT;

BEGIN;
  INSERT into FOO VALUES (1);
COMMIT;
```

Aurora DSQL doesn't support the following transaction, which includes both
`CREATE` and `INSERT` statements.

```
BEGIN;
  CREATE TABLE FOO (ID_col integer);
  INSERT into FOO VALUES (1);
COMMIT;
```

**Asynchronous DDL**

In standard PostgreSQL, DDL operations such as `CREATE INDEX` lock the
affected table, making it unavailable for reads and writes from other sessions. In
Aurora DSQL, these DDL statements run asynchronously using a background manager. Access to
the affected table isn't blocked. Thus, DDL on large tables can run without downtime or
performance impact. For more information about the asynchronous job manager in Aurora DSQL,
see [Asynchronous indexes in Aurora DSQL](working-with-create-index-async.md "working-with-create-index-async.md").
