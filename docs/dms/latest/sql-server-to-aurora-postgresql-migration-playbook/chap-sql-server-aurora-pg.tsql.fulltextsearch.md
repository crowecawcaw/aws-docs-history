

# Full-text search for T-SQL
<a name="chap-sql-server-aurora-pg.tsql.fulltextsearch"></a>

This topic provides reference information about full-text search capabilities in Microsoft SQL Server and PostgreSQL, which is relevant to migrating from SQL Server 2019 to Amazon Aurora PostgreSQL. It explains the differences in how these database systems implement full-text search functionality, including index creation, query syntax, and performance optimization techniques.


| Feature compatibility |  AWS SCT / AWS DMS automation level |  AWS SCT action code index | Key differences | 
| --- | --- | --- | --- | 
|  ![Two star feature compatibility](http://docs.aws.amazon.com/dms/latest/sql-server-to-aurora-postgresql-migration-playbook/images/pb-compatibility-2.png)  |  ![No automation](http://docs.aws.amazon.com/dms/latest/sql-server-to-aurora-postgresql-migration-playbook/images/pb-automation-0.png)  |  [Full-Text Search](chap-sql-server-aurora-pg.tools.actioncode.md#chap-sql-server-aurora-pg.tools.actioncode.fulltextsearch)  | Different paradigm and syntax require rewriting the application. | 

## SQL Server Usage
<a name="chap-sql-server-aurora-pg.tsql.fulltextsearch.sqlserver"></a>

SQL Server supports an optional framework for running full-text search queries against character-based data in SQL Server tables using an integrated, in-process full-text engine and a `fdhost.exe` filter daemon host process.

To run full-text queries, create a full-text catalog. This catalog in turn may contain one or more full-text indexes. A full-text index is comprised of one or more textual columns of a table.

Full-text queries perform smart linguistic searches against full-text indexes by identifying words and phrases based on specific language rules. The searches can be for simple words, complex phrases, or multiple forms of a word or a phrase. They can return ranking scores for matches or hits.

### Full-Text Indexes
<a name="chap-sql-server-aurora-pg.tsql.fulltextsearch.sqlserver.indexes"></a>

You can create a full-text index on one of more columns of a table or view for any of the following data types:
+  `CHAR` — Fixed size ASCII string column data type.
+  `VARCHAR` — Variable size ASCII string column data type.
+  `NCHAR` — Fixed size UNICODE string column data type.
+  `NVARCHAR` — Variable size UNICODE string column data type.
+  `TEXT` — ASCII BLOB string column data type. This data type is deprecated.
+  `NTEXT` — UNICODE BLOB string column data type. This data type is deprecated.
+  `IMAGE` — Binary BLOB data type. This data type is deprecated.
+  `XML` — XML structured BLOB data type.
+  `VARBINARY(MAX)` — Binary BLOB data type.
+  `FILESTREAM` — File-based storage data type.

For more information, see [Data Types](chap-sql-server-aurora-pg.sql.datatypes.md).

You can use the `CREATE FULLTEXT INDEX` statement to create full-text indexes. A full-text index may contain up to 1024 columns from a single table or view.

When you create full-text indexes on `BINARY` type columns, you can store documents such as Microsoft Word as a binary stream and parse them correctly by the full-text engine.

### Full-Text Catalogs
<a name="chap-sql-server-aurora-pg.tsql.fulltextsearch.sqlserver.catalogs"></a>

Full-text indexes are contained within full-text catalog objects. A full-text catalog is a logical container for one or more full-text indexes, You can use a full-text catalog to collectively administer them as a group for tasks such as back-up, restore, refresh content, and so on.

You can use the `CREATE FULLTEXT CATALOG` statement to create full-text catalogs. A full-text catalog may contain zero or more full-text indexes and is limited in scope to a single database.

### Full-Text Queries
<a name="chap-sql-server-aurora-pg.tsql.fulltextsearch.sqlserver.queries"></a>

After you create and populate a full-text catalog and index, you can run full-text queries against these indexes to query for:
+ Simple term match for one or more words or phrases.
+ Prefix term match for words that begin with a set of characters.
+ Generational term match for inflectional forms of a word.
+ Proximity term match for words or phrases that are close to another word or phrase.
+ Thesaurus search for synonymous forms of a word.
+ Weighted term match for finding words or phrases with weighted proximity values.

Full-text queries are integrated into T-SQL and use the following predicates and functions:
+  `CONTAINS` predicate.
+  `FREETEXT` predicate.
+  `CONTAINSTABLE` table-valued function.
+  `FREETEXTTABLE` table-valued function.

**Note**  
Don’t confuse full-text functionality with the `LIKE` predicate, which is used for pattern matching only.

### Updating Full-Text Indexes
<a name="chap-sql-server-aurora-pg.tsql.fulltextsearch.sqlserver.updating"></a>

By default, full-text indexes are automatically updated when the underlying data is modified, similar to a normal B-tree or columnstore index. However, large changes to the underlying data may inflict a performance impact for the full-text indexes update because it is a resource intensive operation. In these cases, you can disable the automatic update of the catalog and update it manually, or on a schedule, to keep the catalog up to date with the underlying tables.

**Note**  
You can monitor the status of the full-text catalog by using the `FULLTEXTCATALOGPROPERTY (<Full-text Catalog Name>, 'Populatestatus')` function.

### Examples
<a name="chap-sql-server-aurora-pg.tsql.fulltextsearch.sqlserver.examples"></a>

The following example creates a product review table.

```
CREATE TABLE ProductReviews
(
  ReviewID INT NOT NULL
  IDENTITY(1,1),
  CONSTRAINT PK_ProductReviews PRIMARY KEY(ReviewID),
  ProductID INT NOT NULL
  /*REFERENCES Products(ProductID)*/,
  ReviewText VARCHAR(4000) NOT NULL,
  ReviewDate DATE NOT NULL,
  UserID INT NOT NULL
  /*REFERENCES Users(UserID)*/
);
```

```
INSERT INTO ProductReviews
( ProductID, ReviewText, ReviewDate, UserID)
VALUES
(1, 'This is a review for product 1, it is excellent and works as expected','20180701', 2),
(1, 'This is a review for product 1, it isn't that great and failed after two days','20180702', 2),
(2, 'This is a review for product 3, it has exceeded my expectations. A+++','20180710', 2);
```

The following example creates a full-text catalog for product reviews.

```
CREATE FULLTEXT CATALOG ProductFTCatalog;
```

The following example creates a full-text index for product reviews.

```
CREATE FULLTEXT INDEX
ON ProductReviews (ReviewText)
KEY INDEX PK_ProductReviews
ON ProductFTCatalog;
```

The following example queries the full-text index for reviews containing the word `excellent`.

```
SELECT *
FROM ProductReviews
WHERE CONTAINS(ReviewText, 'excellent');
```

```
ReviewID  ProductID  ReviewText                                                             ReviewDate  UserID
1         1          This is a review for product 1, it is excellent and works as expected  2018-07-01  2
```

For more information, see [Full-Text Search](https://docs.microsoft.com/en-us/previous-versions/sql/2014/relational-databases/search/full-text-search?view=sql-server-2014&viewFallbackFrom=sql-server-ver15) in the *SQL Server documentation*.

## PostgreSQL Usage
<a name="chap-sql-server-aurora-pg.tsql.fulltextsearch.pg"></a>

You can use full-text indexes to speed up textual searches performed against textual data by using the full-text `@@` predicate.

You can create full-text indexes on almost any column data type. It depends on the operator class used when the index is created. You can query all classes from the `pg_opclass` table. Also, you can define the default values.

The default class uses index `tsvector` data types. The most common use is to create one column with text or other data type, and use triggers to convert it to a `tsvector`.

There are two index types for full-text searches: `GIN` and `GiST`.

 `GIN` is slower when building the index because it is complete and doesn’t have false positive results, but it’s faster when querying.

You can improve the `GIN` performance on creation by increasing the `maintenance_work_mem` parameter.

When you create `GIN` indexes, you can combine them with these parameters:
+  `fastupdate` puts updates on the index on a waiting list so they will occur in `VACUUM` or related scenarios. The default value is `ON`.
+  `gin_pending_list_limit`: the maximum size of a waiting list in KB. The default value is 4MB.

You can’t use `GIN` as composite index (multi columns) unless you add the `btree_gin` extension (which is supported in Amazon Aurora).

```
CREATE EXTENSION btree_gin;
CREATE INDEX reviews_idx ON reviews USING GIN (title, body);
```

### Full-Text Search Functions
<a name="chap-sql-server-aurora-pg.tsql.fulltextsearch.pg.functions"></a>

 **Boolean search** 

You can use `to_tsquery()`, which accepts a list of words is checked against the normalized vector created with `to_tsvector()`. To do this, use the `@@` operator to check if `tsquery` matches `tsvector`. For example, the following statement returns `t` because the column contains the word **boy**. This search also returns `t` for **boys** but not for **boyser**.

```
SELECT to_tsvector('The quick young boy jumped over the fence')
@@ to_tsquery('boy');
```

 **Operators search** 

The following example shows how to use the `AND (&)`, `OR (|)`, and `NOT (!)` operators.

```
SELECT to_tsvector('The quick young boy jumped over the fence')
@@ to_tsquery('young & (boy | guy) & !girl');
```

 **Phase search** 

When using `to_tsquery`, you can also search for a similar term if you replace boy with boys and add the langauge to be used.

```
SELECT to_tsvector('The quick young boy jumped over the fence')
@@ to_tsquery('english', 'young & (boys | guy) & !girl');
```

Search words within a specific distance. In the following example, `-` is equal to 1. These examples return true.

```
SELECT to_tsvector('The quick young boy jumped over the fence') @@
  to_tsquery('young <-> boy'),
  to_tsvector('The quick young boy jumped over the fence') @@
  to_tsquery('quick <3> jumped');
```

### Migration Considerations
<a name="chap-sql-server-aurora-pg.tsql.fulltextsearch.pg.considerations"></a>

Migrating full-text indexes from SQL Server to Aurora PostgreSQL requires a full rewrite of the code that addresses creating, managing, and querying of full-text searches.

Although the Aurora PostgreSQL full-text engine is significantly less comprehensive than SQL Server, it is also much simpler to create and manage, and it is sufficiently powerful for most common, basic full-text requirements.

You can create a text search dictionary. For more information, see [CREATE TEXT SEARCH DICTIONARY](https://www.postgresql.org/docs/13/sql-createtsdictionary.html).

For more complex full-text workloads, use Amazon CloudSearch, a managed service that makes it simple and cost-effective to set up, manage, and scale an enterprise grade search solution. Amazon CloudSearch supports 34 languages and advanced search features such as highlighting, autocomplete, and geospatial search.

Currently, there is no direct tooling integration with Aurora PostgreSQL. Therefore, create a custom application to synchronize the data between Amazon RDS instances and the CloudSearch service.

For more information, see [Amazon CloudSearch](https://aws.amazon.com/cloudsearch/).

### Examples
<a name="chap-sql-server-aurora-pg.tsql.fulltextsearch.pg.examples"></a>

```
CREATE TABLE ProductReviews
(
  ReviewID SERIAL PRIMARY KEY,
  ProductID INT NOT NULL
  ReviewText TEXT NOT NULL,
  ReviewDate DATE NOT NULL,
  UserID INT NOT NULL
);
```

```
INSERT INTO ProductReviews
(ProductID, ReviewText, ReviewDate, UserID)
VALUES
(1, 'This is a review for product 1, it is excellent and works as expected', '20180701', 2),
(1, 'This is a review for product 1, it isn't that great and failed after two days', '20180702', 2),
(2, 'This is a review for product 3, it has exceeded my expectations. A+++', '20180710', 2);
```

The following example creates a full-text search index.

```
CREATE INDEX gin_idx ON ProductReviews USING gin (ReviewText gin_trgm_ops);
```

You can use `gin_trgm_ops` to index a `TEXT` data type.

The following example queries the full-text index for reviews containing the word excellent.

```
SELECT * FROM ProductReviews where ReviewText @@ to_tsquery('excellent');
```

For more information, see [Full Text Search](https://www.postgresql.org/docs/13/textsearch.html) and [Additional Features](https://www.postgresql.org/docs/13/textsearch-features.html) in the *PostgreSQL documentation*.