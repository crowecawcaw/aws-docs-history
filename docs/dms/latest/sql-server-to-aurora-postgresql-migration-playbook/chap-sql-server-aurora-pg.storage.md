# Indexed view functionality

This topic provides reference information comparing the feature compatibility between Microsoft SQL Server 2019 and Amazon Aurora PostgreSQL, specifically focusing on indexed views and materialized views. You can understand the differences in implementation and limitations between these two database systems when it comes to creating and managing views with indexes. The topic highlights that while SQL Server supports indexed views with specific requirements, PostgreSQL offers similar functionality through materialized views.

| Feature compatibility          | AWS SCT / AWS DMS automation level | AWS SCT action code index | Key differences                                                       |
| ------------------------------ | ---------------------------------- | ------------------------- | --------------------------------------------------------------------- |
| Two star feature compatibility | No automation                      | N/A                       | Different paradigm and syntax will require rewriting the application. |

## SQL Server Usage

The first index created on a view must be a clustered index. Subsequent indexes can be non-clustered indexes. For more information, see [Clustered and nonclustered indexes described](https://docs.microsoft.com/en-us/sql/relational-databases/indexes/clustered-and-nonclustered-indexes-described?view=sql-server-2017 "https://docs.microsoft.com/en-us/sql/relational-databases/indexes/clustered-and-nonclustered-indexes-described?view=sql-server-2017") in the _SQL Server documentation_.

Before creating an index on a view, the following requirements must be met:

- The `WITH SCHEMABINDING` option must be used when creating the view.
- Verify the `SET` options are correct for all existing tables referenced in the view and for the session. Find the link at the end of this section for required values.
- Ensure that a clustered index on the view is exists.

###### Note

You can’t use indexed views with temporal queries (`FOR SYSTEM_TIME`).

### Examples

Set the required `SET` options, create a view with the `WITH SCHEMABINDING` option, and create an index on this view.

```
SET NUMERIC_ROUNDABORT OFF;
SET ANSI_PADDING, ANSI_WARNINGS, CONCAT_NULL_YIELDS_NULL, ARITHABORT,
  QUOTED_IDENTIFIER, ANSI_NULLS ON;
GO

CREATE VIEW Sales.Ord_view
WITH SCHEMABINDING
AS
  SELECT SUM(Price*Qty*(1.00-Discount)) AS Revenue,
    OrdTime, ID, COUNT_BIG(*) AS COUNT
  FROM Sales.OrderDetail AS ordet, Sales.OrderHeader AS ordhead
  WHERE ordet.SalesOrderID = ordhead.SalesOrderID
  GROUP BY OrdTime, ID;
GO

CREATE UNIQUE CLUSTERED INDEX IDX_V1
  ON Sales.Ord_view (OrdTime, ID);
GO
```

For more information, see [Create Indexed Views](https://docs.microsoft.com/en-us/sql/relational-databases/views/create-indexed-views?view=sql-server-2017 "https://docs.microsoft.com/en-us/sql/relational-databases/views/create-indexed-views?view=sql-server-2017") in the _SQL Server documentation_.

## PostgreSQL Usage

PostgreSQL doesn’t support indexed views, but does provide similar functionality with materialized views. You can run queries associated with materialized views, and populate the view data with the `REFRESH` command.

The PostgreSQL implementation of materialized views has three primary limitations:

- You can refresh PostgreSQL materialized views either manually or using a job running the `REFRESH MATERIALIZED VIEW` command. To refresh materialized views automatically, create a trigger.
- PostgreSQL materialized views only support complete or full refresh.
- DML on materialized views isn’t supported.

In some cases, when the tables are big, full `REFRESH` can cause performance issues. In this case, you can use triggers to sync between one table to the new table. You can use the new table as an indexed view.

### Examples

The following example creates a materialized view named `sales_summary` using the sales table as the source.

```
CREATE MATERIALIZED VIEW sales_summary AS
SELECT seller_no,sale_date,sum(sale_amt)::numeric(10,2) as sales_amt
FROM sales
WHERE sale_date < CURRENT_DATE
GROUP BY seller_no, sale_date
ORDER BY seller_no, sale_date;
```

The following example runs a manual refresh of the materialized view:

```
REFRESH MATERIALIZED VIEW sales_summary;
```

###### Note

The materialized view data isn’t refreshed automatically if changes occur to its underlying tables. For automatic refresh of materialized view data, a trigger on the underlying tables must be created.

### Creating a Materialized View

When you create a materialized view in PostgreSQL, it uses a regular database table underneath. You can create database indexes on the materialized view directly and improve performance of queries that access the materialized view.

### Example

The following example creates an index on the `sellerno` and `sale_date` columns of the `sales_summary` materialized view.

```
CREATE UNIQUE INDEX sales_summary_seller
ON sales_summary (seller_no, sale_date);
```

## Summary

| Feature                  | Indexed views                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | Materialized view                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| ------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Create materialized view | `<br>SET NUMERIC_ROUNDABORT OFF;<br>SET ANSI_PADDING, ANSI_WARNINGS, CONCAT_NULL_YIELDS_NULL,<br>ARITHABORT, QUOTED_IDENTIFIER, ANSI_NULLS ON;<br>GO<br>CREATE VIEW Sales.Ord_view WITH SCHEMABINDING<br>AS SELECT SUM(Price*Qty*(1.00-Discount)) AS Revenue,<br>OrdTime, ID, COUNT_BIG(*) AS<br>COUNT FROM Sales.OrderDetail AS ordet,<br>Sales.OrderHeader AS ordhead<br>WHERE ordet.SalesOrderID = ordhead.SalesOrderID<br>GROUP BY OrdTime, ID;<br>GO<br>CREATE UNIQUE CLUSTERED INDEX IDX_V1 ON Sales.Ord_view (OrdTime, ID);<br>GO<br>` | `<br>CREATE MATERIALIZED VIEW mv1 AS SELECT<br>• FROM employees;<br>`                                                                                                                                                                                                                                                                                                                                                                                                          |
| Indexed refreshed        | Automatic                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | Manual. You can automate refreshes using triggers.<br>Create a trigger that initiates a refresh after every DML command on the underlying tables:<br>`<br>CREATE OR REPLACE FUNCTION<br>refresh_mv1()<br>returns trigger language plpgsql as<br>$$ begin<br>refresh materialized view mv1;<br>return null;<br>end $$;<br>`<br>Create the `refresh_mv1` trigger after insert, update, delete, or truncate on employees. For each statement, run the `refresh_mv1();` procedure. |
| DML                      | Supported                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | Not Supported                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |

For more information, see [Materialized Views](https://www.postgresql.org/docs/13/rules-materializedviews.htm "https://www.postgresql.org/docs/13/rules-materializedviews.htm") in the _PostgreSQL documentation_.
