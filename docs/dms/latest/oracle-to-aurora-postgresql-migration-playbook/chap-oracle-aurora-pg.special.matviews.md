

# Oracle and PostgreSQL materialized views
<a name="chap-oracle-aurora-pg.special.matviews"></a>

With AWS DMS, you can create and manage materialized views in Oracle and PostgreSQL databases to improve query performance and enable efficient data access. A materialized view is a database object that stores a pre-computed result set from a query, providing fast access to summarized or frequently accessed data.


| Feature compatibility |  AWS SCT / AWS DMS automation level |  AWS SCT action code index | Key differences | 
| --- | --- | --- | --- | 
|  ![Three star feature compatibility](http://docs.aws.amazon.com/dms/latest/oracle-to-aurora-postgresql-migration-playbook/images/pb-compatibility-3.png)  |  ![Three star automation level](http://docs.aws.amazon.com/dms/latest/oracle-to-aurora-postgresql-migration-playbook/images/pb-automation-3.png)  |  [Materialized Views](chap-oracle-aurora-pg.tools.actioncode.md#chap-oracle-aurora-pg.tools.actioncode.materializedviews)  | PostgreSQL doesn’t support automatic or incremental REFRESH. | 

## Oracle usage
<a name="chap-oracle-aurora-pg.special.matviews.ora"></a>

Oracle materialized views (also known as MViews) are table segments where the contents are periodically refreshed based on the results of a stored query. Oracle materialized views are defined with specific queries and can be manually or automatically refreshed based on specific configurations. A materialized view runs its associated query and stores the results as a table segment.

Oracle materialized views are especially useful for:
+ Replication of data across multiple databases.
+ Data warehouse use cases.
+ Increasing performance by persistently storing the results of complex queries as database tables.

Such as ordinary views, you can create materialized views with a `SELECT` query. The `FROM` clause of an MView query can reference tables, views, and other materialized views. The source objects that an Mview uses as data sources are also called master tables (replication terminology) or detail tables (data warehouse terminology).

 **Immediate or deferred refresh** 

When you create materialized views, use the `BUILD IMMEDIATE` option to instruct Oracle to immediately update the contents of the materialized view by running the underlying query. This is different from a deferred update where the materialized view is populated only on the first requested refresh.

 **Fast and complete refresh** 

You can use one of the two following options to refresh data in your materialized view.
+  `REFRESH FAST` — Incremental data refresh. Only updates rows that have changed since the last refresh of the Materialized View instead of performing a complete refresh. This type of refresh fails if materialized view logs have not been created.
+  `COMPLETE` — The table segment used by the materialized view is truncated (data is cleared) and repopulated by running the associated query.

 **Materialized view logs** 

When you create materialized views, use a materialized view log to instruct Oracle to store any changes performed by DML commands on the master tables that are used to refresh the materialized view, which provides faster materialized view refreshes.

Without materialized view logs, Oracle must re-run the query associated with the materialized view each time. This process is also known as a complete refresh. This process is slower compared to using materialized view logs.

 **Materialized view refresh strategy** 

You can use one of the two following strategies to refresh data in your materialized view.
+  `ON COMMIT` — Refreshes the materialized view upon any commit made on the underlying associated tables.
+  `ON DEMAND` — The refresh is initiated by a scheduled task or manually by the user.

 **Examples** 

Create a simple Materialized View named mv1 that runs a simple `SELECT` statement on the employees table.

```
CREATE MATERIALIZED VIEW mv1 AS SELECT * FROM hr.employees;
```

Create a more complex materialized view using a database link (remote) to obtain data from a table located in a remote database. This materialized view also contains a subquery. The `FOR UPDATE` clause allows the materialized view to be updated.

```
CREATE MATERIALIZED VIEW foreign_customers FOR
UPDATE AS SELECT * FROM sh.customers@remote cu WHERE EXISTS
(SELECT * FROM sh.countries@remote co WHERE co.country_id = cu.country_id);
```

Create a materialized view on two source tables: `times` and `products`. This approach enables `FAST` refresh of the materialized view instead of the slower `COMPLETE` refresh. Also, create a new materialized view named sales\_mv which is refreshed incrementally `REFRESH FAST` each time changes in data are detected (`ON COMMIT`) on one or more of the tables associated with the materialized view query.

```
CREATE MATERIALIZED VIEW LOG ON times
WITH ROWID, SEQUENCE (time_id, calendar_year)
INCLUDING NEW VALUES;

CREATE MATERIALIZED VIEW LOG ON products
WITH ROWID, SEQUENCE (prod_id)
INCLUDING NEW VALUES;

CREATE MATERIALIZED VIEW sales_mv
BUILD IMMEDIATE
REFRESH FAST ON COMMIT
AS SELECT t.calendar_year, p.prod_id,
SUM(s.amount_sold) AS sum_sales
FROM times t, products p, sales s
WHERE t.time_id = s.time_id AND p.prod_id = s.prod_id
GROUP BY t.calendar_year, p.prod_id;
```

For more information, see [Basic Materialized Views](https://docs.oracle.com/en/database/oracle/oracle-database/19/dwhsg/basic-materialized-views.html#GUID-A7AE8E5D-68A5-4519-81EB-252EAAF0ADFF) in the *Oracle documentation*.

## PostgreSQL usage
<a name="chap-oracle-aurora-pg.special.matviews.pg"></a>

PostgreSQL supports materialized views with associated queries similar to the Oracle implementation. The query associated with the materialized view is used to populate the materialized view at the time the `REFRESH` command is issued. The PostgreSQL implementation of materialized views has three primary limitations when compared to Oracle materialized views:
+ PostgreSQL materialized views may be refreshed either manually or using a job running the `REFRESH MATERIALIZED VIEW` command. Automatic refresh of materialized views require the creation of a trigger.
+ PostgreSQL materialized views only support complete (full) refresh.
+ DML on materialized views is not supported.

**Note**  
In PostgreSQL 10, the statistics collector is being updated properly after a `REFRESH MATERIALIZED VIEW` run.

 **Examples** 

Create a materialized view named sales\_summary using the sales table as the source for the materialized view.

```
CREATE MATERIALIZED VIEW sales_summary AS
SELECT seller_no,sale_date,sum(sale_amt)::numeric(10,2) as sales_amt
FROM sales
WHERE sale_date < CURRENT_DATE
GROUP BY seller_no, sale_date
ORDER BY seller_no, sale_date;
```

Execute a manual refresh of the materialized view.

```
REFRESH MATERIALIZED VIEW sales_summary;
```

**Note**  
The materialized view data will not be refreshed automatically if changes occur to its underlying tables. For automatic refresh of materialized view data, a trigger on the underlying tables must be created.

 **Creating a materialized view** 

When you create a materialized view in PostgreSQL, it uses a regular database table underneath. You can create database indexes on the materialized view directly and improve performance of queries that access the materialized view.

 **Example** 

Create an index on the `sellerno` and `sale_date` columns of the `sales_summary` materialized view.

```
CREATE UNIQUE INDEX sales_summary_seller
ON sales_summary (seller_no, sale_date);
```

## Summary
<a name="chap-oracle-aurora-pg.special.matviews.summary"></a>


| Option | Oracle | PostgreSQL | 
| --- | --- | --- | 
| Create materialized view |  <pre>CREATE MATERIALIZED VIEW<br />mv1 AS SELECT * FROM employees;</pre>  |  <pre>CREATE MATERIALIZED VIEW mv1 AS<br />SELECT * FROM employees;</pre>  | 
| Manual refresh of a materialized view | <pre>DBMS_MVIEW.REFRESH('mv1', 'cf');</pre>The `cf` parameter configures the refresh method: `c` is complete and `f` is fast. |  <pre>REFRESH MATERIALIZED VIEW mv1;</pre>  | 
| Online refresh of a materialized view |  <pre>CREATE MATERIALIZED VIEW<br />mv1 REFRESH FAST ON COMMIT<br />AS SELECT * FROM employees;</pre>  | Create a trigger that will initiate a refresh after every DML command on the underlying tables:<pre>CREATE OR REPLACE FUNCTION<br />refresh_mv1()<br />returns trigger language plpgsql as<br />$$ begin<br />refresh materialized view mv1;<br />return null;<br />end $$;<br /><br />create trigger refresh_ mv1 after insert or update<br />or delete or truncate on employees for each statement<br />execute procedure refresh_mv1();</pre> | 
| Automatic incremental refresh of a materialized view |  <pre>CREATE MATERIALIZED VIEW LOG<br />ON employees…<br />INCLUDING NEW VALUES;<br /><br />CREATE MATERIALIZED VIEW<br />mv1 REFRESH FAST AS SELECT<br />* FROM employees;</pre>  | Not Supported | 
| DML on materialized view data | Supported | Not Supported | 

For more information, see [Materialized Views](https://www.postgresql.org/docs/13/rules-materializedviews.htm) in the *PostgreSQL documentation*.