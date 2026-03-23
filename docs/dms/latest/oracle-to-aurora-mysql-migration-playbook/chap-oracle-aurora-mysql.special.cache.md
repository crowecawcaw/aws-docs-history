# Oracle SQL Result Cache and MySQL Query Cache

With AWS DMS, you can leverage performance optimization features such as Oracle SQL Result Cache and MySQL Query Cache to improve query execution times. The Oracle SQL Result Cache stores data from previous queries, allowing faster retrieval for identical subsequent queries. MySQL Query Cache temporarily stores the text of a `SELECT` query and its corresponding result set, facilitating quicker responses to repeated queries on the same data.

| Feature compatibility            | AWS SCT / AWS DMS automation level | AWS SCT action code index | Key differences                                                                                                   |
| -------------------------------- | ---------------------------------- | ------------------------- | ----------------------------------------------------------------------------------------------------------------- |
| Three star feature compatibility | No automation                      | N/A                       | Syntax and option differences, similar functionality. This is off the MySQL roadmap and suggested not to be used. |

## Oracle usage

The Oracle SQL Result Cache feature is related to the following caching categories:

- Global temporary tables.
- Materialized views.
- PL/SQL collection.
- The `WHEN` clause.

The Result Cache reduces I/O operations by skipping the fetch step of execution plans and retrieving rows from the buffer cache. This feature is most useful for data warehouse scenarios where many rows must be scanned, but the result sets contain few rows. The rows are stored in the System Global Area (SGA) and are reused when the same SQL statements are executed in the current session or other sessions.

The `RESULT_CACHE_MODE` parameter controls caching and accepts the following values:

- `MANUAL` — SQL results are not cached for SQL statements unless they use a hint to perform caching.
- `FORCE` — All results are cached for SQL statements unless they use a hint to prevent caching.

In Oracle Real Application Cluster (RAC) environments, each instance has its own private result cache and can’t be used by other instances.

The query result cache is not compatible with scalar subquery caching.

### Examples

Cache a query when `RESULT_CACHE_MODE` is set to `MANUAL`.

```
SELECT /*+ RESULT_CACHE */ count(*) FROM bigdata_smallres_tbl;
```

Turn off caching when `RESULT_CACHE_MODE` is set to `FORCE` and a result cache isn’t needed.

```
SELECT /*+ NO_RESULT_CACHE */ count(*) FROM bigdata_smallres_tbl;
```

For more information, see [Configuring the Client Result Cache](https://docs.oracle.com/en/database/oracle/oracle-database/19/tgdba/tuning-result-cache.html#GUID-21CAA1E7-9E46-4442-9F3E-CE09EEF60D92 "https://docs.oracle.com/en/database/oracle/oracle-database/19/tgdba/tuning-result-cache.html#GUID-21CAA1E7-9E46-4442-9F3E-CE09EEF60D92") in the _Oracle documentation_.

## MySQL usage

According to the MySQL roadmap, it is recommended not to use the Query Cache.

Like the Oracle Result Cache, the MySQL Query Cache reduces I/O operations by skipping the fetch step of run plans and retrieving rows from the buffer cache. It can be shared across multiple sessions.

The Query Cache is deprecated as of MySQL 5.7.20 and will be removed in MySQL 8.0. For more information, see [Retiring Support for the Query Cache](https://dev.mysql.com/blog-archive/mysql-8-0-retiring-support-for-the-query-cache/ "https://dev.mysql.com/blog-archive/mysql-8-0-retiring-support-for-the-query-cache/") in the _MySQL Blog_.

### Examples

The following example runs a `select` statement using the Query Cache.

```
SELECT SQL_CACHE count(*) FROM bigdata_smallres_tbl;
```

The following example runs a `select` statement without using the Query Cache.

```
SELECT SQL_NO_CACHE count(*) FROM bigdata_smallres_tbl;
```

For more information, see [The MySQL Query Cache](https://dev.mysql.com/doc/refman/5.7/en/query-cache.html "https://dev.mysql.com/doc/refman/5.7/en/query-cache.html") in the _MySQL documentation_.
