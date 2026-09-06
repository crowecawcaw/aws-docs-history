

# Oracle materialized views and MySQL summary tables or views
<a name="chap-oracle-aurora-mysql.special.matviews"></a>

With AWS DMS, you can create Oracle materialized views and MySQL summary tables or views to improve query performance and data availability. Materialized views and summary tables are database objects that store pre-computed results of queries, reducing the need for complex calculations at runtime.


| Feature compatibility |  AWS SCT / AWS DMS automation level |  AWS SCT action code index | Key differences | 
| --- | --- | --- | --- | 
|  ![One star feature compatibility](http://docs.aws.amazon.com/dms/latest/oracle-to-aurora-mysql-migration-playbook/images/pb-compatibility-1.png)  |  ![No automation](http://docs.aws.amazon.com/dms/latest/oracle-to-aurora-mysql-migration-playbook/images/pb-automation-0.png)  |  [Materialized Views](chap-oracle-aurora-mysql.tools.actioncode.md#chap-oracle-aurora-mysql.tools.actioncode.mview)  | MySQL doesn’t support materialized views. | 

## Oracle usage
<a name="chap-oracle-aurora-mysql.special.matviews.oracle"></a>

Oracle materialized views are table segments where the contents are periodically refreshed based on the results of a stored query. Oracle materialized views are defined with specific queries and can be manually or automatically refreshed based on specific configurations. A materialized view runs its associated query and stores the results as a table segment.

Oracle materialized views are especially useful for:
+ Replication of data across multiple databases.
+ Data warehouse use cases.
+ Increasing performance by persistently storing the results of complex queries as database tables.

Such as ordinary views, you can create materialized views with a `SELECT` query. The `FROM` clause of a materialized view query can reference tables, views, and other materialized views. The source objects that a materialized view uses as data sources are also called master tables (replication terminology) or detail tables (data warehouse terminology).

### Immediate or deferred refresh
<a name="chap-oracle-aurora-mysql.special.matviews.oracle.immediate"></a>

When you create materialized views, use the `BUILD IMMEDIATE` option can to instruct Oracle to immediately update the contents of the materialized view by running the underlying query. This is different from a deferred update where the materialized view is populated only on the first requested refresh.

### Fast and complete refresh
<a name="chap-oracle-aurora-mysql.special.matviews.oracle.fastrefresh"></a>

You can use one of the two following options to refresh data in your materialized view.
+  `REFRESH FAST` — Incremental data refresh. Only updates rows that have changed since the last refresh of the Materialized View instead of performing a complete refresh. This type of refresh fails if materialized view logs have not been created.
+  `COMPLETE` — The table segment used by the materialized view is truncated (data is cleared) and repopulated by running the associated query.

### Materialized view logs
<a name="chap-oracle-aurora-mysql.special.matviews.oracle.logs"></a>

When you create materialized views, use a materialized view log to instruct Oracle to store any changes performed by DML commands on the master tables that are used to refresh the materialized view, which provides faster materialized view refreshes.

Without materialized view logs, Oracle must re-run the query associated with the materialized view each time. This process is also known as a complete refresh. This process is slower compared to using materialized view logs.

### Materialized view refresh strategy
<a name="chap-oracle-aurora-mysql.special.matviews.oracle.strategy"></a>

You can use one of the two following strategies to refresh data in your materialized view.
+  `ON COMMIT` — Refreshes the materialized view upon any commit made on the underlying associated tables.
+  `ON DEMAND` — The refresh is initiated by a scheduled task or manually by the user.

### Examples
<a name="chap-oracle-aurora-mysql.special.matviews.oracle.examples"></a>

The following example creates a simple Materialized View named `mv1` that runs a simple `SELECT` statement on the `employees` table.

```
CREATE MATERIALIZED VIEW mv1 AS SELECT * FROM hr.employees;
```

The following example creates a more complex materialized view using a database link (remote) to obtain data from a table located in a remote database. This materialized view also contains a subquery. The `FOR UPDATE` clause allows the materialized view to be updated.

```
CREATE MATERIALIZED VIEW foreign_customers FOR
UPDATE AS SELECT * FROM sh.customers@remote cu WHERE EXISTS
(SELECT * FROM sh.countries@remote co WHERE co.country_id = cu.country_id);
```

The following example creates a materialized view on two source tables: `times` and `products`. This approach enables `FAST` refresh of the materialized view instead of the slower `COMPLETE` refresh. Also, create a new materialized view named `sales_mv` which is refreshed incrementally `REFRESH FAST` each time changes in data are detected (`ON COMMIT`) on one or more of the tables associated with the materialized view query.

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

## MySQL usage
<a name="chap-oracle-aurora-mysql.special.matviews.mysql"></a>

Oracle materialized views have no equivalent feature in MySQL, but other features can be used separately or combined to achieve similar functionality.

Make sure that you evaluate each case on its own merits, but options include:
+  **Summary tables** — If your materialized view has many calculations and data manipulations, you can keep the results in tables and query the data without running all calculations on-the-fly. The data for these tables can be copied using triggers or events objects.
+  **Views** — Aurora MySQL has a new Parallel Query mechanism that offloads some of the query operations to the storage level. This approach can greatly improve performance. In some cases, regular views can be used and may decrease some administration tasks. To evaluate this option, measure the performance and execution time of your SQL.

For more information, see [CREATE TABLE Statement](https://dev.mysql.com/doc/refman/5.7/en/create-table.html), [Trigger Syntax and Examples](https://dev.mysql.com/doc/refman/5.7/en/trigger-syntax.html), and [CREATE VIEW Statement](https://dev.mysql.com/doc/refman/5.7/en/create-view.html) in the *MySQL documentation*.