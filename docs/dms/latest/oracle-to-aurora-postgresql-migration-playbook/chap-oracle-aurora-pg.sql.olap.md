

# Oracle OLAP functions and PostgreSQL window functions
<a name="chap-oracle-aurora-pg.sql.olap"></a>

The following sections outline the steps to configure and utilize Oracle OLAP functions and PostgreSQL window functions with AWS Database Migration Service.


| Feature compatibility |  AWS SCT / AWS DMS automation level |  AWS SCT action code index | Key differences | 
| --- | --- | --- | --- | 
|  ![Four star feature compatibility](http://docs.aws.amazon.com/dms/latest/oracle-to-aurora-postgresql-migration-playbook/images/pb-compatibility-4.png)  |  ![Four star automation level](http://docs.aws.amazon.com/dms/latest/oracle-to-aurora-postgresql-migration-playbook/images/pb-automation-4.png)  |  [OLAP Functions](chap-oracle-aurora-pg.tools.actioncode.md#chap-oracle-aurora-pg.tools.actioncode.olapfunctions)  |  `GREATEST` and `LEAST` functions might get different results in PostgreSQL. `CONNECT BY` isn’t supported by PostgreSQL, workaround available. | 

## Oracle usage
<a name="chap-oracle-aurora-pg.sql.olap.ora"></a>

Oracle OLAP functions extend the functionality of standard SQL analytic functions by providing capabilities to compute aggregate values based on a group of rows. You can apply the OLAP functions to logically partitioned sets of results within the scope of a single query expression. OLAP functions are usually used in combination with Business Intelligence reports and analytics. They can help boost query performance as an alternative to achieving the same result using more complex non-OLAP SQL code.

### Common Oracle OLAP Functions
<a name="chap-oracle-aurora-pg.sql.olap.ora.common"></a>


| Function type | Related functions | 
| --- | --- | 
| Aggregate |  `average_rank`, `avg`, `count`, `dense_rank`, `max`, `min`, `rank`, `sum`  | 
| Analytic |  `average_rank`, `avg`, `count`, `dense_rank`, `lag`, `lag_variance`, `lead_variance_percent`, `max`, `min`, `rank`, `row_number`, `sum`, `percent_rank`, `cume_dist`, `ntile`, `first_value`, `last_value`  | 
| Hierarchical |  `hier_ancestor`, `hier_child_count`, `hier_depth`, `hier_level`, `hier_order`, `hier_parent`, `hier_top`  | 
| Lag |  `lag`, `lag_variance`, `lag_variance_percent`, `lead`, `lead_variance`, `lead_variance_percent`  | 
| OLAP DML |  `olap_dml_expression`  | 
| Rank |  `average_rank`, `dense_rank`, `rank`, `row_number`  | 

For more information, see [OLAP Functions](https://docs.oracle.com/en/database/oracle/oracle-database/19/sqlrf/OLAP-Functions.html#GUID-2AE523A7-630C-4907-B91B-89861C141EBD) and [Functions](https://docs.oracle.com/en/database/oracle/oracle-database/19/sqlrf/Functions.html#GUID-D079EFD3-C683-441F-977E-2C9503089982) in the *Oracle documentation*.

## PostgreSQL usage
<a name="chap-oracle-aurora-pg.sql.olap.pg"></a>

PostgreSQL refers to ANSI SQL analytical functions as “Window Functions”. They provide the same core functionality as SQL Analytical Functions and Oracle extended OLAP functions. Window functions in PostgreSQL operate on a logical “partition” or "window" of the result set and return a value for rows in that “window”.

From a database migration perspective, you should examine PostgreSQL Window Functions by type and compare them with the equivalent Oracle OLAP functions to verify compatibility of syntax and output.

**Note**  
Even if a PostgreSQL window function provides the same functionality of a specific Oracle OLAP function, the returned data type may be different and require application changes.

PostgreSQL provides support for two main types of window functions:
+ Aggregation functions.
+ Ranking functions.

### PostgreSQL window functions by type
<a name="chap-oracle-aurora-pg.sql.olap.pg.window"></a>


| Function type | Related functions | 
| --- | --- | 
| Aggregate |  `avg`, `count`, `max`, `min`, `sum`, `string_agg`  | 
| Ranking |  `row_number`, `rank`, `dense_rank`, `percent_rank`, `cume_dist`, `ntile`, `lag`, `lead`, `first_value`, `last_value`, `nth_value`  | 

 **Examples** 

The Oracle `rank()` function and the PostgreSQL `rank()` function provide the same results.

Oracle:

```
SELECT department_id, last_name, salary, commission_pct,
    RANK() OVER (PARTITION BY department_id
    ORDER BY salary DESC, commission_pct) "Rank"
    FROM employees WHERE department_id = 80;

DEPARTMENT_ID LAST_NAME SALARY COMMISSION_PCT Rank
80            Russell   14000  .4             1
80            Partners  13500  .3             2
80            Errazuriz 12000  .3             3
```

PostgreSQL:

```
hr=# SELECT department_id, last_name, salary, commission_pct,
    RANK() OVER (PARTITION BY department_id
    ORDER BY salary DESC, commission_pct) "Rank"
    FROM employees WHERE department_id = 80;

DEPARTMENT_ID LAST_NAME SALARY    COMMISSION_PCT Rank
80            Russell   14000.00  0.40           1
80            Partners  13500.00  0.30           2
80            Errazuriz 12000.00  0.30           3
```

**Note**  
The returned formatting for certain numeric data types is different.

### Oracle CONNECT BY equivalent in PostgreSQL
<a name="chap-oracle-aurora-pg.sql.olap.pg.connectby"></a>

PostgreSQL provides two workarounds as alternatives to Oracle hierarchical statements such as the `CONNECT BY` function:
+ Use PostgreSQL `generate_series` function.
+ Use PostgreSQL recursive views.

 **Example** 

PostgreSQL `generate_series` function.

```
SELECT "DATE"
  FROM generate_series(timestamp '2010-01-01',
                       timestamp '2017-01-01',
                       interval '1 day') s("DATE");

DATE
---------------------
2010-01-01 00:00:00
2010-01-02 00:00:00
2010-01-03 00:00:00
2010-01-04 00:00:00
2010-01-05 00:00:00
…
```

For more information, see [Window Functions](https://www.postgresql.org/docs/13/functions-window.html) and [Aggregate Functions](https://www.postgresql.org/docs/13/functions-aggregate.html) in the *PostgreSQL documentation*.

### Extended support for analytic queries and OLAP
<a name="chap-oracle-aurora-pg.sql.olap.pg.support"></a>

For advanced analytic purposes and use cases, consider using Amazon Redshift as a purpose-built data warehouse cloud solution. You can run complex analytic queries against petabytes of structured data using sophisticated query optimization, columnar storage on high-performance local disks, and massive parallel query run. Most results are returned in seconds.

 Amazon Redshift is specifically designed for online analytic processing (OLAP) and business intelligence (BI) applications, which require complex queries against large datasets. Because it addresses very different requirements, the specialized data storage schema and query run engine that Amazon Redshift uses is completely different from the PostgreSQL implementation. For example, Amazon Redshift stores data in columns, also known as a columnar-store database.


| Function type | Related functions | 
| --- | --- | 
| Aggregate |  `AVG`, `COUNT`, `CUME_DIST`, `FIRST_VALUE`, `LAG`, `LAST_VALUE`, `LEAD`, `MAX`, `MEDIAN`, `MIN`, `NTH_VALUE`, `PERCENTILE_CONT`, `PERCENTILE_DISC`, `RATIO_TO_REPORT`, `STDDEV_POP`, `STDDEV_SAMP` (synonym for `STDDEV`), `SUM`, `VAR_POP`, `VAR_SAMP` (synonym for `VARIANCE`) | 
| Ranking |  `DENSE_RANK`, `NTILE`, `PERCENT_RANK`, `RANK`, `ROW_NUMBER`  | 

For more information, see [Window functions](https://docs.aws.amazon.com/redshift/latest/dg/c_Window_functions.html) and [Overview example for window functions](https://docs.aws.amazon.com/redshift/latest/dg/c_Window_functions.html#r_Window_function_example) in the *Amazon documentation*.

## Summary
<a name="chap-oracle-aurora-pg.sql.olap.summary"></a>


| Oracle OLAP function | Returned data type | PostgreSQL window function | Returned data type | Compatible syntax | 
| --- | --- | --- | --- | --- | 
|  `Count`  |  `Number`  |  `Count`  |  `bigint`  | Yes | 
|  `Max`  | Number |  `Max`  |  `numeric`, `string`, `date/time`, `network` or `enum` type | Yes | 
|  `Min`  |  `Number`  |  `Min`  |  `numeric`, `string`, `date/time`, `network` or `enum` type | Yes | 
|  `Avg`  |  `Number`  |  `Avg`  |  `numeric`, `double`, otherwise same datatype as the argument | Yes | 
|  `Sum`  |  `Number`  |  `Sum`  |  `bigint`, otherwise same datatype as the argument | Yes | 
|  `rank()`  |  `Number`  |  `rank()`  |  `bigint`  | Yes | 
|  `row_number()`  |  `Number`  |  `row_number()`  |  `bigint`  | Yes | 
|  `dense_rank()`  |  `Number`  |  `dense_rank()`  |  `bigint`  | Yes | 
|  `percent_rank()`  |  `Number`  |  `percent_rank()`  |  `double`  | Yes | 
|  `cume_dist()`  |  `Number`  |  `cume_dist()`  |  `double`  | Yes | 
|  `ntile()`  |  `Number`  |  `ntile()`  |  `integer`  | Yes | 
|  `lag()`  | Same type as value |  `lag()`  | Same type as value | Yes | 
|  `lead()`  | Same type as value |  `lead()`  | Same type as value | Yes | 
|  `first_value()`  | Same type as value |  `first_value()`  | Same type as value | Yes | 
|  `last_value()`  | Same type as value |  `last_value()`  | Same type as value | Yes | 