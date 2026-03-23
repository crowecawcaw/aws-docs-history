# Overall Oracle and PostgreSQL indexes summary

With AWS DMS, you can assess the indexing strategies of your Oracle and PostgreSQL databases before migrating them to a new environment. Overall Oracle and PostgreSQL indexes summary provides a comprehensive analysis of the indexes in your source databases, including their types, usage statistics, and potential redundancies.

## Usage

PostgreSQL supports multiple types of Indexes using different indexing algorithms that can provide performance benefits for different types of queries. The built-in PostgreSQL Index types include:

- **B-Tree** — Default indexes that you can use for equality and range for the majority of queries. These indexes can operate against all datatypes. You can use B-Tree indexes to retrieve NULL values. B-Tree index values are sorted in ascending order by default.
- **Hash** — Hash Indexes are practical for equality operators. These types of indexes are rarely used because they aren’t transaction-safe. They need to be rebuilt manually in case of failures.
- **GIN** (Generalized Inverted Indexes) — GIN indexes are useful when an index needs to map a large amount of values to one row, while B-Tree indexes are optimized for cases when a row has a single key value. GIN indexes work well for indexing fulltext search and for indexing array values.
- **GiST** (Generalized Search Tree) — GiST indexes aren’t viewed as a single type of index but rather as an index infrastructure; a base to create different indexing strategies. GiST indexes enable building general B-Tree structures that you can use for operations more complex than equality and range comparisons. They are mainly used to create indexes for geometric data types and they support full-text search indexing.
- **BRIN** (Block Range Indexes) — BRIN Indexes store summary data for values stored in sequential physical table block ranges. A BRIN index contains only the minimum and maximum values contained in a group of database pages. Its main advantage is that it can rule out the presence of certain records and therefore reduce query run time.

Additional PostgreSQL indexes (such as SP-GiST) exist but are currently not supported because they require a loadable extension not currently available in Amazon Aurora PostgreSQL.

Starting with PostgreSQL 12 it is now possible to monitor progress of `CREATE INDEX` and `REINDEX` operartions by querying system view `pg_stat_progress_create_index`.

## CREATE INDEX synopsis

```
CREATE [ UNIQUE ] INDEX [ CONCURRENTLY ] [ [ IF NOT EXISTS ] name ]
ON table_name [ USING method ]
( { column_name | ( expression ) } [ COLLATE collation ] [ opclass ] [ ASC | DESC
] [ NULLS { FIRST | LAST } ] [, ...] )
[ WITH ( storage_parameter = value [, ... ] ) ]
[ TABLESPACE tablespace_name ]
[ WHERE predicate ]
```

By default, the `CREATE INDEX` statement creates a B-Tree index.

**Examples**

Oracle `CREATE/DROP` Index.

```
CREATE UNIQUE INDEX IDX_EMP_ID ON EMPLOYEES (EMPLOYEE_ID DESC);
DROP INDEX IDX_EMP_ID;
```

PostgreSQL `CREATE/DROP` Index.

```
demo=> CREATE UNIQUE INDEX IDX_EMP_ID ON EMPLOYEES (EMPLOYEE_ID DESC);
demo=> DROP INDEX IDX_EMP_ID;
```

Oracle `ALTER INDEX …​ RENAME`.

```
ALTER INDEX IDX_EMP_ID RENAME TO IDX_EMP_ID_OLD;
```

PostgreSQL `ALTER INDEX …​ RENAME`.

```
demo=> ALTER INDEX IDX_EMP_ID RENAME TO IDX_EMP_ID_OLD;
```

Oracle `ALTER INDEX …​ TABLESPACE`.

```
ALTER INDEX IDX_EMP_ID REBUILD TABLESPACE USER_IDX;
```

PostgreSQL `ALTER INDEX …​ TABLESPACE`.

```
demo=> CREATE TABLESPACE PGIDX LOCATION '/data/indexes';
demo=> ALTER INDEX IDX_EMP_ID SET TABLESPACE PGIDX;
```

Oracle `REBUILD INDEX`.

```
ALTER INDEX IDX_EMP_ID REBUILD;
```

PostgreSQL `REINDEX (REBUILD) INDEX`.

```
demo=> REINDEX INDEX IDX_EMP_ID;
```

Oracle `REBUILD INDEX ONLINE`.

```
ALTER INDEX IDX_EMP_ID REBUILD ONLINE;
```

PostgreSQL `REINDEX (REBUILD) INDEX ONLINE`.

```
demo=> CREATE INDEX CONCURRENTLY IDX_EMP_ID1 ON EMPLOYEES(EMPLOYEE_ID);
demo=> DROP INDEX CONCURRENTLY IDX_EMP_ID;
```

For more information, see [Building Indexes Concurrently](https://www.postgresql.org/docs/13/sql-createindex.html#SQL-CREATEINDEX-CONCURRENTLY "https://www.postgresql.org/docs/13/sql-createindex.html#SQL-CREATEINDEX-CONCURRENTLY"), [ALTER INDEX](https://www.postgresql.org/docs/13/sql-alterindex.html "https://www.postgresql.org/docs/13/sql-alterindex.html"), and [REINDEX](https://www.postgresql.org/docs/13/sql-reindex.html "https://www.postgresql.org/docs/13/sql-reindex.html") in the _PostgreSQL documentation_.

## Summary

| Oracle indexes types and features                   | PostgreSQL compatibility                                                           | PostgreSQL equivalent                      |
| --------------------------------------------------- | ---------------------------------------------------------------------------------- | ------------------------------------------ |
| B-Tree Index                                        | Supported                                                                          | B-Tree Index                               |
| Index-Organized Tables                              | Supported                                                                          | PostgreSQL CLUSTER                         |
| Reverse key indexes                                 | Not supported                                                                      | N/A                                        |
| Descending indexes                                  | Supported                                                                          | ASC (default) / DESC                       |
| B-tree cluster indexes                              | Not supported                                                                      | N/A                                        |
| Unique / non-unique indexes                         | Supported                                                                          | Syntax is identical                        |
| Function-based indexes                              | Supported                                                                          | PostgreSQL expression indexes              |
| Application domain indexes                          | Not supported                                                                      | N/A                                        |
| BITMAP index / Bitmap join indexes                  | Not supported                                                                      | Consider BRIN index                        |
| Composite indexes                                   | Supported                                                                          | Multicolumn indexes                        |
| Invisible indexes                                   | Not supported                                                                      | Extension hypopg isn’t currently supported |
| Local and global indexes                            | Not supported                                                                      | N/A                                        |
| Partial Indexes for Partitioned Tables (Oracle 12c) | Not supported                                                                      | N/A                                        |
| CREATE INDEX… / DROP INDEX…                         | Supported                                                                          | High percentage of syntax similarity       |
| ALTER INDEX… (General Definitions)                  | Supported                                                                          | N/A                                        |
| ALTER INDEX… REBUILD                                | Supported                                                                          | REINDEX                                    |
| ALTER INDEX… REBUILD ONLINE                         | Limited support                                                                    | CONCURRENTLY                               |
| Index metadata                                      | PG_INDEXES (Oracle USER_INDEXES)                                                   | N/A                                        |
| Index tablespace allocation                         | Supported                                                                          | SET TABLESPACE                             |
| Index Parallel Operations                           | Not supported                                                                      | N/A                                        |
| Index compression                                   | No direct equivalent to Oracle index key compression or advanced index compression | N/A                                        |
