# Temporal tables for ANSI SQL

This topic provides reference information about temporal database tables in Microsoft SQL Server and their compatibility with Amazon Aurora PostgreSQL. You can understand the functionality of temporal tables in SQL Server, including their use of DATETIME2 columns and querying methods. The topic also explains common scenarios where temporal tables are useful for tracking data change history.

| Feature compatibility          | AWS SCT / AWS DMS automation level | AWS SCT action code index | Key differences |
| ------------------------------ | ---------------------------------- | ------------------------- | --------------- |
| Two star feature compatibility | No automation                      | N/A                       | N/A             |

## SQL Server Usage

Temporal database tables were introduced in ANSI SQL 2011. T-SQL began supporting system versioned temporal tables in SQL Server 2016.

Each temporal table has two explicitly defined `DATETIME2` columns known as period columns. The system uses these columns to record the period of availability for each row when it is modified. An additional history table retains the previous version of the data. The system can automatically create the history table, or a user can specify an existing table.

To query the history table, use `FOR SYSTEM TIME` after the table name in the `FROM` clause and combine it with the following options:

- `ALL` — all changes.
- `CONTAINED IN` — change is valid only within a period.
- `AS OF` — change was valid somewhere in a specific period.
- `BETWEEN` — change was valid from a time range.

Temporal Tables are mostly used when to track data change history as described in the following scenarios.

### Anomaly Detection

Use this option when searching for data with unusual values. For example, detecting when a customer returns items too often.

```
CREATE TABLE Products_returned
(
  ProductID int NOT NULL PRIMARY KEY CLUSTERED,
  ProductName varchar(60) NOT NULL,
  return_count INT NOT NULL,
  ValidFrom datetime2(7) GENERATED ALWAYS AS ROW START NOT NULL,
  ValidTo datetime2(7) GENERATED ALWAYS AS ROW END NOT NULL,
  PERIOD FOR SYSTEM_TIME (ValidFrom, ValidTo)
)
WITH( SYSTEM_VERSIONING = ON (HISTORY_TABLE = dbo.ProductHistory,
  DATA_CONSISTENCY_CHECK = ON ))
```

Query the Product table and run calculations on the data.

```
SELECT
  ProductId,
  LAG (return_count, 1, 1)
  over (partition by ProductId order by ValidFrom) as PrevValue,
  return_count,
  LEAD (return_count, 1, 1)
  over (partition by ProductId order by ValidFrom) as NextValue ,
  ValidFrom, ValidTo from Product
FOR SYSTEM_TIME ALL
```

### Audit

Track changes to critical data such as salaries or medical data.

```
CREATE TABLE Employee
(
  EmployeeID int NOT NULL PRIMARY KEY CLUSTERED,
  Name nvarchar(60) NOT NULL,
  Salary decimal (6,2) NOT NULL,
  ValidFrom datetime2 (2) GENERATED ALWAYS AS ROW START,
  ValidTo datetime2 (2) GENERATED ALWAYS AS ROW END,
  PERIOD FOR SYSTEM_TIME (ValidFrom, ValidTo)
)
WITH (SYSTEM_VERSIONING = ON (HISTORY_TABLE = dbo.EmployeeTrackHistory));
```

Use `FOR SYSTEM_TIME ALL` to retrieve changes from the history table.

```
SELECT * FROM Employee
  FOR SYSTEM_TIME ALL WHERE
    EmployeeID = 1000 ORDER BY ValidFrom;
```

### Other Scenarios

Additional scenarios include the following:

- Fixing row-level corruption.
- Slowly changing dimension.
- Over time changes analysis.

For more information, see [Temporal tables](https://docs.microsoft.com/en-us/sql/relational-databases/tables/temporal-tables?view=sql-server-ver15 "https://docs.microsoft.com/en-us/sql/relational-databases/tables/temporal-tables?view=sql-server-ver15") in the _SQL Server documentation_.

## PostgreSQL Usage

PostgreSQL provides an extension for supporting temporal tables, but it’s not supported by Amazon Aurora. A workaround will be to create table triggers to update a custom history table to track changes to data. For more information, see [Triggers](chap-sql-server-aurora-pg.tsql.md "chap-sql-server-aurora-pg.tsql.md").
