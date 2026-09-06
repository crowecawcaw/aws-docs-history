

# DDL and distributed transactions in Aurora DSQL
<a name="working-with-ddl"></a>

Data definition language (DDL) behaves differently in Aurora DSQL from PostgreSQL. Aurora DSQL features a Multi-AZ distributed and shared-nothing database layer built on top of multi-tenant compute and storage fleets. Because no single primary database node or leader exists, the database catalog is distributed. Thus, Aurora DSQL manages DDL schema changes as distributed transactions.

Specifically, DDL behaves differently in Aurora DSQL as follows:

**Concurrency control responses**  
Because the database catalog is distributed, Aurora DSQL manages DDL schema changes as distributed transactions that update the catalog version. Sessions that have a cached copy of the catalog at an earlier version can receive a concurrency control response with SQLSTATE code `40001` and OCC code `OC001` when they next interact with storage.  
For example, consider the following sequence of actions:  

1. In session 1, a user adds a column to the table `mytable`. This updates the catalog version.

1. In session 2, a user attempts to insert a row into `mytable`. This session still has the previous catalog version cached.

   Aurora DSQL returns `SQL Error [40001]: ERROR: schema has been updated by another transaction (OC001)`.
An OC001 response can also occur when the schema change has already completed before the affected transaction starts. Aurora DSQL query processors discover catalog changes reactively during query execution, so a session that has been idle might still be operating with a stale catalog version. On retry, the session refreshes its catalog cache and the transaction typically succeeds.

**DDL and DML in the same transaction**  
Transactions in Aurora DSQL can contain only one DDL statement and can't have both DDL and DML statements. This restriction means that you can't create a table and insert data into the same table within the same transaction. For example, Aurora DSQL supports the following sequential transactions.  

```
BEGIN;
  CREATE TABLE mytable (ID_col integer);
COMMIT;

BEGIN;
  INSERT into FOO VALUES (1);
COMMIT;
```
Aurora DSQL doesn't support the following transaction, which includes both `CREATE` and `INSERT` statements.  

```
BEGIN;
  CREATE TABLE FOO (ID_col integer);
  INSERT into FOO VALUES (1);
COMMIT;
```

**Asynchronous DDL**  
In standard PostgreSQL, DDL operations such as `CREATE INDEX` lock the affected table, making it unavailable for reads and writes from other sessions. In Aurora DSQL, these DDL statements run asynchronously using a background manager. Access to the affected table isn't blocked. Thus, DDL on large tables can run without downtime or performance impact. For more information about the asynchronous job manager in Aurora DSQL, see [Asynchronous indexes in Aurora DSQL](working-with-create-index-async.md).