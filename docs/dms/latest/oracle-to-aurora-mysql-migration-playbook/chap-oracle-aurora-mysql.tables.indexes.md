# MySQL overall indexes summary

MySQL supports multiple types of indexes using different indexing algorithms that can provide performance benefits for different types of queries.

## Usage

The built-in MySQL index types include:

- **B-tree** — Default indexes that you can use for equality and range for the majority of queries. These indexes can operate against all data types. You can use B-tree indexes to retrieve NULL values. B-tree index values are sorted in ascending order by default.
- **Hash** — Hash Indexes are practical for equality operators. These types of indexes are rarely used because they aren’t transaction-safe. This type of index is supported by `MEMORY` and `NDB` storage engines.
- **Full-text** — Full-text indexes are useful when the application needs to query large amount of text, using more complicated morphology attributes.
- **Spatial** — This index supports objects such as `POINT` and `GEOMETRY` to run geographic-related queries.

###### Note

Amazon Relational Database Service (Amazon RDS) for MySQL version supports descending indexes: `DESC` in an index definition is no longer ignored but causes storage of key values in descending order. Previously indexes could be scanned in reverse order but at a performance penalty. A descending index can be scanned in forward order which is more efficient. Descending indexes also make it possible for the optimizer to use multiple-column indexes when the most efficient scan order mixes ascending order for some columns and descending order for others. For more information, see [Descending Indexes](https://dev.mysql.com/doc/refman/8.0/en/descending-indexes.html "https://dev.mysql.com/doc/refman/8.0/en/descending-indexes.html") in the _MySQL documentation_.

## CREATE INDEX synopsis

```
CREATE [UNIQUE | FULLTEXT | SPATIAL] INDEX index_name
  [index_type]
  ON tbl_name (key_part,...)
  [index_option]
  [algorithm_option | lock_option] ...

key_part:
  col_name [(length)] [ASC | DESC]

index_option:
  KEY_BLOCK_SIZE [=] value
  | index_type
  | WITH PARSER parser_name
  | COMMENT 'string'

index_type:
  USING {BTREE | HASH}

algorithm_option:
  ALGORITHM [=] {DEFAULT | INPLACE | COPY}

lock_option:
  LOCK [=] {DEFAULT | NONE | SHARED | EXCLUSIVE}
```

By default, the `CREATE INDEX` statement creates a B-tree index.

## Examples

Oracle `CREATE/DROP` index.

```
CREATE UNIQUE INDEX IDX_EMP_ID ON EMPLOYEES (EMPLOYEE_ID DESC);
DROP INDEX IDX_EMP_ID;
```

MySQL `CREATE/DROP` index.

```
CREATE UNIQUE INDEX IDX_EMP_ID ON EMPLOYEES (EMPLOYEE_ID DESC);
DROP INDEX IDX_EMP_ID;
```

Oracle `ALTER INDEX …​ RENAME`.

```
ALTER INDEX IDX_EMP_ID RENAME TO IDX_EMP_ID_OLD;
```

MySQL `ALTER INDEX …​ RENAME`.

```
ALTER TABLE EMPLOYEES RENAME INDEX IDX_EMP_ID TO IDX_EMP_ID_OLD;
```

Oracle `REBUILD INDEX`.

```
ALTER INDEX IDX_EMP_ID REBUILD;
```

MySQL `REINDEX (REBUILD) INDEX`.

```
ANALYZE TABLE EMPLOYEES;
```

For more information, see [CREATE INDEX Statement](https://dev.mysql.com/doc/refman/5.7/en/create-index.html "https://dev.mysql.com/doc/refman/5.7/en/create-index.html"), [ANALYZE TABLE Statement](https://dev.mysql.com/doc/refman/5.7/en/analyze-table.html "https://dev.mysql.com/doc/refman/5.7/en/analyze-table.html"), and [ALTER TABLE Statement](https://dev.mysql.com/doc/refman/5.7/en/alter-table.html "https://dev.mysql.com/doc/refman/5.7/en/alter-table.html") in the _MySQL documentation_.

## Summary

| Oracle indexes types and features                   | MySQL compatibility                                                                | MySQL equivalent                                                                                                        |
| --------------------------------------------------- | ---------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------- |
| B-tree Index                                        | Supported                                                                          | B-tree Index                                                                                                            |
| Index-organized tables                              | Supported                                                                          | Default behavior by InnoDB                                                                                              |
| Reverse key indexes                                 | Not supported                                                                      | N/A                                                                                                                     |
| Descending indexes                                  | Supported                                                                          | `ABS` (default) / `DESC`                                                                                                |
| B-tree cluster indexes                              | Not supported                                                                      | N/A                                                                                                                     |
| Unique and non-unique indexes                       | Supported                                                                          | Syntax is identical                                                                                                     |
| Function-based indexes                              | Supported                                                                          | Use generated columns                                                                                                   |
| Application domain indexes                          | Not supported                                                                      | N/A                                                                                                                     |
| BITMAP index or Bitmap join indexes                 | Not supported                                                                      | N/A                                                                                                                     |
| Composite indexes                                   | Supported                                                                          | Multicolumn indexes                                                                                                     |
| Invisible indexes                                   | Not supported                                                                      | N/A                                                                                                                     |
| Local and global indexes                            | Not supported                                                                      | N/A                                                                                                                     |
| Partial indexes for partitioned tables (Oracle 12c) | Limited compatibility                                                              | Column prefix index                                                                                                     |
| `CREATE INDEX…​` or `DROP INDEX…​`                  | Supported                                                                          | High percentage of syntax similarity                                                                                    |
| `ALTER INDEX…​` (general definitions)               | Not supported                                                                      | N/A                                                                                                                     |
| `ALTER INDEX…​ REBUILD`                             | Supported                                                                          | `ANALYZE TABLE`                                                                                                         |
| `ALTER INDEX…​ REBUILD ONLINE`                      | Not supported                                                                      | N/A                                                                                                                     |
| Index metadata                                      | `STATISTICS (Oracle USER_INDEXES)`                                                 | `<br>SELECT DISTINCT TABLE_SCHEMA,<br>TABLE_NAME, INDEX_NAME,<br>INDEX_TYPE FROM<br>INFORMATION_SCHEMA.STATISTICS;<br>` |
| Index tablespace allocation                         | Not supported                                                                      | N/A                                                                                                                     |
| Index parallel operations                           | Not supported                                                                      | N/A                                                                                                                     |
| Index compression                                   | No direct equivalent to Oracle index key compression or advanced index compression | N/A                                                                                                                     |
