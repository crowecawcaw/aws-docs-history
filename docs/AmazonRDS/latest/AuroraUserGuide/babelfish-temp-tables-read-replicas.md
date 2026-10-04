

# Babelfish temporary tables on read replicas
<a name="babelfish-temp-tables-read-replicas"></a>

Starting with **Babelfish 6.2.0** and **Babelfish 5.8.0**, Babelfish supports local temporary tables and table variables on Aurora PostgreSQL read replicas. With this support, SQL Server Management Studio (SSMS) and T-SQL applications that use temporary tables and table variables as intermediate scratch space can connect and operate normally against read replicas without any application changes.

**Topics**
+ [Why temporary tables on read replicas matter](#babelfish-temp-tables-ro-why)
+ [Enabling temporary tables on Aurora read replicas](#babelfish-temp-tables-ro-enabling)
+ [Supported operations](#babelfish-temp-tables-ro-supported)
+ [Limitations and considerations](#babelfish-temp-tables-ro-limitations)

## Why temporary tables on read replicas matter
<a name="babelfish-temp-tables-ro-why"></a>

Amazon Aurora PostgreSQL read replicas let you scale the read operations of your application. By connecting to the reader endpoint of the cluster, Aurora can spread the load for read-only connections across as many Aurora Replicas as you have in the cluster. Aurora Replicas also help to increase availability. If the writer instance in a cluster becomes unavailable, Aurora automatically promotes one of the reader instances to take its place as the new writer.

SQL Server applications and tooling rely heavily on session-local temporary tables (`#temp`) and table variables (`DECLARE @t TABLE`) – not just in application code, but at the driver and tooling level. SQL Server Management Studio (SSMS), the standard SQL Server management tool, creates temporary tables internally for IntelliSense, query result caching, and object scripting. Prior to Babelfish 6.2.0 and Babelfish 5.8.0, any attempt to create a temporary table or table variable on an Aurora replica failed with:

```
ERROR: cannot execute CREATE TABLE in a read-only transaction
```

This error blocked two critical customer use cases:
+ **SSMS connected to an Aurora replica** – SSMS could not function because its internal IntelliSense mechanism creates temporary tables automatically on connection.
+ **Read-heavy application workloads** – T-SQL applications commonly stage intermediate query results in local temporary tables and table variables before aggregation or joining. These patterns failed entirely on read replicas, forcing customers to route workloads to the primary writer or restructure application logic.

Starting with Babelfish 6.2.0 and Babelfish 5.8.0, both limitations are resolved. Local temporary tables and table variables are fully supported on read replicas. Only session-local temporary objects – temporary tables and table variables – are exempt, because they are never written to shared storage.

## Enabling temporary tables on Aurora read replicas
<a name="babelfish-temp-tables-ro-enabling"></a>

Temporary table support on read replicas is controlled by the GUC parameter `babelfishpg_tsql.enable_temp_table_on_ro`.

### New parameter groups
<a name="babelfish-temp-tables-ro-enabling-new"></a>

For clusters created on Aurora PostgreSQL 18.6 and Aurora PostgreSQL 17.11 or later, `enable_temp_table_on_ro` is **enabled by default**. No action is required.

### Existing parameter groups
<a name="babelfish-temp-tables-ro-enabling-existing"></a>

Clusters upgraded to Aurora PostgreSQL 17.11 or Aurora PostgreSQL 18.6 from an earlier version can update the Aurora cluster parameter group. For more information, see [Modifying parameters in a DB parameter group in Amazon Aurora](USER_WorkingWithParamGroups.Modifying.md). The change takes effect immediately – no cluster restart is required.

```
aws rds modify-db-cluster-parameter-group \
  --db-cluster-parameter-group-name {{your-cluster-parameter-group-name}} \
  --parameters \
    "ParameterName=babelfishpg_tsql.enable_temp_table_on_ro,ParameterValue=on,ApplyMethod=immediate"
```

## Supported operations
<a name="babelfish-temp-tables-ro-supported"></a>

The following temporary table and table variable operations are supported on Babelfish read replicas.

### Local temporary table DDL
<a name="babelfish-temp-tables-ro-supported-ddl"></a>
+ `CREATE TABLE #tablename (...)` – creates a session-local temporary table on the read replica.
+ `SELECT col1, col2 INTO #tablename FROM source WHERE ...` – creates and populates a temporary table from a read query in a single statement.
+ `DROP TABLE #tablename` – explicitly drops a temporary table within the session; all temporary tables are also dropped automatically when the session ends.
+ `TRUNCATE TABLE #tablename` – removes all rows from a temporary table without dropping it.

### Local temporary table DML
<a name="babelfish-temp-tables-ro-supported-dml"></a>
+ `INSERT INTO #tablename ...`
+ `SELECT ... FROM #tablename`
+ `UPDATE #tablename SET ...`
+ `DELETE FROM #tablename WHERE ...`

### Table variables
<a name="babelfish-temp-tables-ro-supported-tablevars"></a>

`DECLARE @variable_name TABLE (...)` – declares a session-local table variable. Table variables are scoped to the batch or stored procedure in which they are declared and are dropped automatically at the end of that scope.

### Procedural and dynamic SQL patterns
<a name="babelfish-temp-tables-ro-supported-procedural"></a>
+ Stored procedures and batches that create temporary tables and read from permanent tables execute end-to-end on read replicas.
+ `sp_executesql` with dynamic SQL that creates and uses temporary tables works on read replicas.

## Limitations and considerations
<a name="babelfish-temp-tables-ro-limitations"></a>

The following limitations apply to temporary tables and table variables on read replicas.

### Unsupported operations
<a name="babelfish-temp-tables-ro-limitations-unsupported"></a>

**Temporary tables that reference user-defined objects are not supported.** Temporary table definitions that reference user-defined types (UDTs), user-defined functions (UDFs), or other user-defined objects in column definitions or constraints are blocked on read replicas. Use only built-in system types and system functions in temporary table definitions on read replicas.

### Per-session temporary object limit
<a name="babelfish-temp-tables-ro-limitations-object-limit"></a>

A single session can hold up to **65,536 temp objects** due to the pre-defined buffer pool size. If you exceed this limit, you see the following error:

```
Unable to allocate oid for temp table. Drop some temporary tables or start a new session
```

You can drop some temporary tables to create new ones or reset the session (drop and re-create the connection) to reset the limit.