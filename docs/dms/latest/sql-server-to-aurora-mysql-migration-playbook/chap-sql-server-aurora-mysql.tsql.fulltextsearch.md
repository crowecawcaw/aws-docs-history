

# Full-text search for T-SQL
<a name="chap-sql-server-aurora-mysql.tsql.fulltextsearch"></a>

This topic provides reference information about full-text search capabilities in Microsoft SQL Server 2019 and Amazon Aurora MySQL. It compares the two systems, highlighting their similarities and differences in implementing full-text search functionality. You can understand how full-text indexes are created and used in both platforms, including the types of columns that support full-text indexing and the basic syntax for creating and querying these indexes.


| Feature compatibility |  AWS SCT / AWS DMS automation level |  AWS SCT action code index | Key differences | 
| --- | --- | --- | --- | 
|  ![Two star feature compatibility](http://docs.aws.amazon.com/dms/latest/sql-server-to-aurora-mysql-migration-playbook/images/pb-compatibility-2.png)  |  ![No automation](http://docs.aws.amazon.com/dms/latest/sql-server-to-aurora-mysql-migration-playbook/images/pb-automation-0.png)  |  [Full-Text Search](chap-sql-server-aurora-mysql.tools.actioncode.md#chap-sql-server-aurora-mysql.tools.actioncode.fulltextsearch)  | Syntax and option differences, less comprehensive but simpler. Most common basic functionality is similar. Requires rewrite of administration logic and queries. | 

## SQL Server Usage
<a name="chap-sql-server-aurora-mysql.tsql.fulltextsearch.sqlserver"></a>

SQL Server supports an optional framework for running full-text search queries against character-based data in SQL Server tables using an integrated, in-process full-text engine, and the `fdhost.exe` filter daemon host process.

To run full-text queries, a full-text catalog must first be created, which in turn may contain one or more full-text indexes. A full-text index is comprised of one or more textual columns of a table.

Full-text queries perform smart linguistic searches against Full-Text indexes by identifying words and phrases based on specific language rules. The searches can be for simple words, complex phrases, or multiple forms of a word or a phrase. They can return ranking scores for matches also known as hits.

### Full-Text Indexes
<a name="chap-sql-server-aurora-mysql.tsql.fulltextsearch.sqlserver.indexes"></a>

A full-text index can be created on one of more columns of a table or view for any of the following data types:
+  `CHAR` — Fixed size ASCII string column data type.
+  `VARCHAR` — Variable size ASCII string column data type.
+  `NCHAR` — Fixed size UNICODE string column data type.
+  `NVARCHAR` — Variable size UNICODE string column data type.
+  `TEXT` — ASCII BLOB string column data type (deprecated).
+  `NTEXT` — UNICODE BLOB string column data type (deprecated).
+  `IMAGE` — Binary BLOB data type (deprecated).
+  `XML` — XML structured BLOB data type.
+  `VARBINARY(MAX)` — Binary BLOB data type.
+  `FILESTREAM` — File-based storage data type.
**Note**  
For more information about data types, [Data Types](chap-sql-server-aurora-mysql.sql.datatypes.md).

Full-text indexes are created using the `CREATE FULLTEXT INDEX` statement. A full-text index may contain up to 1024 columns from a single table or view. For more information, see [CREATE FULLTEXT INDEX (Transact-SQL)](https://docs.microsoft.com/en-us/sql/t-sql/statements/create-fulltext-index-transact-sql?view=sql-server-ver15) in the *SQL Server documentation*.

When creating full-text indexes on `BINARY` type columns, documents such as Microsoft Word can be stored as a binary stream and parsed correctly by the full-text engine.

### Full-Text Catalogs
<a name="chap-sql-server-aurora-mysql.tsql.fulltextsearch.sqlserver.catalogs"></a>

Full-text indexes are contained within full-text catalog objects. A full-text catalog is a logical container for one or more full-text indexes and can be used to collectively administer them as a group for tasks such as back-up, restore, refresh content, and so on.

Full-text catalogs are created using the `CREATE FULLTEXT CATALOG` statement. A full-text catalog may contain zero or more full-text indexes and is limited in scope to a single database. For more information, see [CREATE FULLTEXT CATALOG (Transact-SQL)](https://docs.microsoft.com/en-us/sql/t-sql/statements/create-fulltext-catalog-transact-sql?view=sql-server-ver15) in the *SQL Server documentation*.

### Full-Text Queries
<a name="chap-sql-server-aurora-mysql.tsql.fulltextsearch.sqlserver.queries"></a>

After a full-text catalog and index have been create and populated, users can perform full-text queries against these indexes to query for:
+ Simple term match for one or more words or phrases.
+ Prefix term match for words that begin with a set of characters.
+ Generational term match for inflectional forms of a word.
+ Proximity term match for words or phrases which are close to another word or phrase.
+ Thesaurus search for synonymous forms of a word.
+ Weighted term match for finding words or phrases with weighted proximity values.

Full-text queries are integrated into T-SQL, and use the following predicates and functions:
+  `CONTAINS` predicate.
+  `FREETEXT` predicate.
+  `CONTAINSTABLE` table valued function.
+  `FREETEXTTABLE` table valued function.
**Note**  
Don’t confuse full-text functionality with the `LIKE` predicate, which is used for pattern matching only.

### Updating Full-Text Indexes
<a name="chap-sql-server-aurora-mysql.tsql.fulltextsearch.sqlserver.updating"></a>

By default, full-text indexes are automatically updated when the underlying data is modified, similar to a normal B-tree or columnstore index. However, large changes to the underlying data may inflict a performance impact for the full-text indexes update because it is a resource intensive operation. In these cases, you can turn off the automatic update of the catalog and update it manually, or on a schedule, to keep the catalog up to date with the underlying tables.

**Note**  
You can monitor the status of full-text catalog by using the `FULLTEXTCATALOGPROPERTY (<Full-text Catalog Name>, 'Populatestatus')` function.

### Examples
<a name="chap-sql-server-aurora-mysql.tsql.fulltextsearch.sqlserver.examples"></a>

Create the `ProductReviews` table.

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
(1, 'This is a review for product 1, it is excellent and works as expected',
'20180701', 2),
(1, 'This is a review for product 1, it isn't that great and failed after two days',
'20180702', 2),
(2, 'This is a review for product 3, it has exceeded my expectations. A+++',
'20180710', 2);
```

Create a full-text catalog for product reviews.

```
CREATE FULLTEXT CATALOG ProductFTCatalog;
```

Create a full-text index for ProductReviews.

```
CREATE FULLTEXT INDEX
ON ProductReviews (ReviewText)
KEY INDEX PK_ProductReviews
ON ProductFTCatalog;
```

Query the full-text index for reviews containing the word *excellent*.

```
SELECT *
FROM ProductReviews
WHERE CONTAINS(ReviewText, 'excellent');
```

```
ReviewID  ProductID  ReviewText                                                              ReviewDate  UserID
1         1          This is a review for product 1, it is excellent and works as expected.  2018-07-01  2
```

For more information, see [Full-Text Search](https://docs.microsoft.com/en-us/previous-versions/sql/2014/relational-databases/search/full-text-search?view=sql-server-2014&viewFallbackFrom=sql-server-ver15) in the *SQL Server documentation*.

## MySQL Usage
<a name="chap-sql-server-aurora-mysql.tsql.fulltextsearch.mysql"></a>

 Amazon Aurora MySQL-Compatible Edition (Aurora MySQL) supports all the native full-text capabilities of MySQL InnoDB full-text indexes. Full-text indexes are used to speed up textual searches performed against textual data by using the full-text `MATCH …​ AGAINST` predicate.

Full-text indexes can be created on any textual column of the following types:
+  `CHAR` — Fixed length string data type.
+  `VARCHAR` — Variable length string data type.
+  `TEXT` — String BLOB data type.

Full-text indexes can be created as part of the `CREATE TABLE`, `ALTER TABLE`, and `CREATE INDEX` statements. Full-text indexes in Aurora MySQL use an inverted index design where a list of individual words is stored alongside a list of documents where the words were found. Proximity search is also supported by storing a byte offset position for each word.

Creating a full-text index in Aurora MySQL creates a set of index system tables that can be viewed using the `INFORMATION_SCHEMA.INNODB_SYS_TABLES` view. These tables include the auxiliary index tables representing the inverted index and a set of management tables that help facilitate management of the indexes such as deletes and sync with the underlying data, caching, configuration, and syncing processes.

### Full-Text Index Cache
<a name="chap-sql-server-aurora-mysql.tsql.fulltextsearch.mysql.indexcache"></a>

The index cache temporarily caches index entries for recent rows to minimize the contention associated with inserting documents. These inserts, even small ones, typically result in many singleton insertions to the auxiliary tables, which may prove to be challenging in terms of concurrency. Caching and batch flushing help minimize these frequent updates. In addition, batching also helps alleviate the overhead involved with multiple auxiliary table insertions for words and minimizes duplicate entries as insertions are merged and written to disk as a single entry.

### Full-Text Index Document ID and FTS\_DOC\_ID Column
<a name="chap-sql-server-aurora-mysql.tsql.fulltextsearch.mysql.document"></a>

 Aurora MySQL assigns a document identifier that maps words in the index to the document rows where those words are found. This warrants a schema change to the source table, namely adding an indicator column to point to the associated document. This column, known as `FTS_DOC_ID` must exist in the table where the full-text index is created. If the column is not present, Aurora MySQL adds it when the full-text index is created.

**Note**  
Adding a column to a table in Aurora MySQL triggers a full rebuild of the table. That may be resource intensive for larger tables and a warning is issued.

Running a `SHOW WARNINGS` statement after creating a full-text index on a table that doesn’t have this column generates a warning. Consider the following example.

```
CREATE TABLE TestFT
(
    KeyColumn INT AUTO_INCREMENT NOT NULL
    PRIMARY KEY,
    TextColumn TEXT(200)
);
```

```
CREATE FULLTEXT INDEX FTIndex1
ON TestFT(TextColumn);
```

```
SHOW WARNINGS;
```

```
Level    Code  Message
Warning  124   InnoDB rebuilding table to add column FTS_DOC_ID.
```

If the full-text index is created as part of the `CREATE TABLE` statement, the `FTS_DOC_ID` column is added silently and no warning is issued. It is recommended to create the `FTS_DOC_ID` column for tables where full-text indexes will be created as part of the `CREATE TABLE` statement to avoid an expensive rebuild of a table that is already loaded with large amounts of data. Creating the `FTS_DOC_ID` column as an `AUTO_INCREMENT` column may improve performance of data loading.

**Note**  
Dropping a full-text index from a table doesn’t drop the `FTS_DOC_ID` column.

### Full-Text Index Deletes
<a name="chap-sql-server-aurora-mysql.tsql.fulltextsearch.mysql.deletes"></a>

Similar to the insert issue described earlier, deleting rows from a table with a Full-Text index may also result in concurrency challenges due to multiple singleton deletions from the auxiliary tables.

To minimize the impact of this issue, Aurora MySQL logs the deletion of a document ID (`DOC_ID`) in a dedicated internal system table named `FTS_*_DELETED` instead of actually deleting it from the auxiliary tables. The existence of a `DOC_ID` in the `DELETED` table is a type of soft-delete. The engine consults it to determine if a row that had a match in the auxiliary tables should be discarded, or if it should be returned to the client. This approach makes deletes much faster at the expense of somewhat larger index size.

**Note**  
Soft deleted documents aren’t automatically managed. Make sure that you issue an `OPTIMIZE TABLE` statement and the `innodb_optimize_fulltext_only=ON` option to rebuild the full-text index.

### Transaction Control
<a name="chap-sql-server-aurora-mysql.tsql.fulltextsearch.mysql.transactioncontrol"></a>

Due to the caching and batch processing properties of the full-text indexes, `UPDATE` and `INSERT` to a full-text index are committed when a transaction commits. Full-text search can only access committed data.

### Full-Text Search Functions
<a name="chap-sql-server-aurora-mysql.tsql.fulltextsearch.mysql.searchfunctions"></a>

To query full-text indexes, use the `MATCH…​ AGAINST` predicate. The `MATCH` clause accepts a list of column names, separated by commas, that define the column names of the columns that have a full-text index defined and need to be searched. In the `AGAINST` clause, define the string you want searched. It also accepts an optional modifier that indicates the type of search to perform.

### MATCH…​ AGAINST Syntax
<a name="chap-sql-server-aurora-mysql.tsql.fulltextsearch.mysql.matchagainst"></a>

```
MATCH (<Column List>)
AGAINST (
<String Expression>
[ IN NATURAL LANGUAGE MODE
    | IN NATURAL LANGUAGE MODE WITH QUERY EXPANSION
    | IN BOOLEAN MODE
    | WITH QUERY EXPANSION]
)
```

**Note**  
The search expression must be constant for all rows searched. Therefore a table column isn’t permitted.

The three types of full-text searches are natural language, Boolean, and query expansion.

### Natural Language Search
<a name="chap-sql-server-aurora-mysql.tsql.fulltextsearch.mysql.nls"></a>

If no modifier is provided, or the `IN NATURAL LANGUAGE MODE` modifier is explicitly provided, the search string is interpreted as natural human language phrase. For this type of search, the stop-word list is considered and stop words are excluded. For each row, the search returns a relevance value, which denotes the similarity of the search string to the text, for the row, in all the columns listed in the `MATCH` column list. For more information, see [Full-Text Stopwords](https://dev.mysql.com/doc/refman/5.7/en/fulltext-stopwords.html) in the *MySQL documentation*.

### Boolean Search
<a name="chap-sql-server-aurora-mysql.tsql.fulltextsearch.mysql.boolean"></a>

The `IN BOOLEAN MODE` modifier specifies a Boolean search. When using Boolean search, some characters imply special meaning either at the beginning or the end of the words that make up the search string. The `+` and `—` operators are used to indicate that a word must be present or absent for the match to resolve to `TRUE`.

For example, the following statement returns rows for which the `ReviewText` column contains the word *Excellent*, but not the word *England*.

```
SELECT *
FROM ProductReviews
WHERE MATCH (ReviewText) AGAINST ('+Excellent -England' IN BOOLEAN MODE);
```

Additional Boolean operators include: \* The `@distance` operator tests if two or more words start within a specified distance, or the number of words between them. \* The `<` and `>` operators change a word’s contribution to the relevance value assigned for a specific row match. \* Parentheses `()` are used to group words into sub-expressions and may be nested. \* The tilde `~` is used as negative operator, resulting in the word’s contribution to be deducted from the total relevance value. Use this operator to mark noise words that are rated lower, but not excluded, as with the `-` operator. \* The asterisk `*` operator is used as a wildcard operator and is appended to the word. \* Double quotes ` are used for exact, literal phrase matching.

For more information, see [Boolean Full-Text Searches](https://dev.mysql.com/doc/refman/5.7/en/fulltext-boolean.html) in the *MySQL documentation*.

### Query Expansion
<a name="chap-sql-server-aurora-mysql.tsql.fulltextsearch.mysql.queryexpansion"></a>

The `WITH QUERY EXPANSION` or `IN NATURAL LANGUAGE MODE WITH QUERY EXPANSION` is useful when a search phrase is too short, which may indicate that the user is looking for implied knowledge that the full-text engine doesn’t have.

For example, a user that searches for *Car* may need to match specific car brands such as *Ford*, *Toyota*, *Mercedes-Benz*, and so on.

Blind query expansions, also known as automatic relevance feedback, performs the searches twice. On the first pass, the engine looks for the most relevant documents. It then performs a second pass using the original search phrase concatenated with the results of the first pass. For example, if the search was looking for *Cars* and the most relevant documents included the word *Ford*, the seconds search would find the documents that also mention *Ford*.

For more information, see [Full-Text Searches with Query Expansion](https://dev.mysql.com/doc/refman/5.7/en/fulltext-query-expansion.html) in the *MySQL documentation*.

### Migration Considerations
<a name="chap-sql-server-aurora-mysql.tsql.fulltextsearch.mysql.considerations"></a>

Migrating full-text indexes from SQL Server to Aurora MySQL requires a full rewrite of the code that deals with both creating, management, and querying of full-text searches.

Although the Aurora MySQL full-text engine is significantly less comprehensive than SQL Server, it is also much simpler to create and manage and is sufficiently powerful for most common, basic full-text requirements.

For more complex full-text workloads, Amazon Relational Database Service (Amazon RDS) offers CloudSearch, a managed service in the AWS Cloud that makes it simple and cost-effective to set up, manage, and scale an enterprise grade search solution. Amazon CloudSearch supports 34 languages and advanced search features such as highlighting, autocomplete, and geospatial search.

Currently, there is no direct tooling integration with Aurora MySQL and, therefore, you must create a custom application to synchronize the data between Amazon RDS instances and the CloudSearch Service.

For more information, see [Amazon CloudSearch](https://aws.amazon.com/cloudsearch/).

### Examples
<a name="chap-sql-server-aurora-mysql.tsql.fulltextsearch.mysql.examples"></a>

```
CREATE TABLE ProductReviews
(
    ReviewID INT
        AUTO_INCREMENT NOT NULL
        PRIMARY KEY,
    ProductID INT NOT NULL
        /*REFERENCES Products(ProductID)*/,
    ReviewText TEXT(4000) NOT NULL,
    ReviewDate DATE NOT NULL,
    UserID INT NOT NULL
    /*REFERENCES Users(UserID)*/
);
```

```
INSERT INTO ProductReviews
(ProductID, ReviewText, ReviewDate, UserID)
VALUES
(1, 'This is a review for product 1, it is excellent and works as expected',
'20180701', 2),
(1, 'This is a review for product 1, it isn't that great and failed after two days',
'20180702', 2),
(2, 'This is a review for product 3, it has exceeded my expectations. A+++',
'20180710', 2);
```

Query the full-text index for reviews containing the word *excellent*.

```
SELECT *
FROM ProductReviews
WHERE MATCH (ReviewText) AGAINST ('Excellent' IN NATURAL LANGUAGE MODE);
```

For more information, see [InnoDB Full-Text Indexes](https://dev.mysql.com/doc/refman/5.7/en/innodb-fulltext-index.html) in the *MySQL documentation*.