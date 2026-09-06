

# MERGE for T-SQL
<a name="chap-sql-server-aurora-mysql.tsql.merge"></a>

This topic provides reference information about migrating from Microsoft SQL Server 2019’s MERGE statement to equivalent functionality in Amazon Aurora MySQL. You can understand the key differences and similarities between SQL Server’s MERGE capabilities and alternatives such as REPLACE and INSERT…​ON DUPLICATE KEY UPDATE statements.


| Feature compatibility |  AWS SCT / AWS DMS automation level |  AWS SCT action code index | Key differences | 
| --- | --- | --- | --- | 
|  ![Three star feature compatibility](http://docs.aws.amazon.com/dms/latest/sql-server-to-aurora-mysql-migration-playbook/images/pb-compatibility-3.png)  |  ![No automation](http://docs.aws.amazon.com/dms/latest/sql-server-to-aurora-mysql-migration-playbook/images/pb-automation-0.png)  |  [MERGE](chap-sql-server-aurora-mysql.tools.actioncode.md#chap-sql-server-aurora-mysql.tools.actioncode.merge)  | Rewrite to use `REPLACE` and `ON DUPLICATE KEY`, or individual constituent DML statements. | 

## SQL Server Usage
<a name="chap-sql-server-aurora-mysql.tsql.merge.sqlserver"></a>

 `MERGE` is a complex , hybrid DML/DQL statement for performing `INSERT`, `UPDATE`, or `DELETE` operations on a target table based on the results of a logical join of the target table and a source data set.

 `MERGE` can also return row sets similar to `SELECT` using the `OUTPUT` clause, which gives the calling scope access to the actual data modifications of the `MERGE` statement.

The `MERGE` statement is most efficient for non-trivial conditional DML. For example, inserting data if a row key value doesn’t exist and updating the existing row if the key value already exists.

You can manage additional logic such as deleting rows from the target that don’t appear in the source. For simple, straightforward updates of data in one table based on data in another, it is typically more efficient to use simple `INSERT`, `DELETE`, and `UPDATE` statements. You can replicate all `MERGE` functionality using `INSERT`, `DELETE`, and `UPDATE` statements, but not necessarily less efficiently.

The SQL Server MERGE statement offers a wide range of functionality and flexibility and is compatible with ANSI standard SQL:2008. SQL Server has many extensions to MERGE that provide efficient T-SQL solutions for synchronizing data.

### Syntax
<a name="chap-sql-server-aurora-mysql.tsql.merge.sqlserver.syntax"></a>

```
MERGE [INTO] <Target Table> [AS] <Table Alias>]
USING <Source Table>
ON <Merge Predicate>
[WHEN MATCHED [AND <Predicate>]
THEN UPDATE SET <Column Assignments...> | DELETE]
[WHEN NOT MATCHED [BY TARGET] [AND <Predicate>]
THEN INSERT [(<Column List>)]
VALUES (<Values List>) | DEFAULT VALUES]
[WHEN NOT MATCHED BY SOURCE [AND <Predicate>]
THEN UPDATE SET <Column Assignments...> | DELETE]
OUTPUT [<Output Clause>]
```

### Examples
<a name="chap-sql-server-aurora-mysql.tsql.merge.sqlserver.examples"></a>

Perform a simple one-way synchronization of two tables.

```
CREATE TABLE SourceTable
(
    Col1 INT NOT NULL PRIMARY KEY,
    Col2 VARCHAR(20) NOT NULL
);
```

```
CREATE TABLE TargetTable
(
    Col1 INT NOT NULL PRIMARY KEY,
    Col2 VARCHAR(20) NOT NULL
);
```

```
INSERT INTO SourceTable (Col1, Col2)
VALUES
(2, 'Source2'),
(3, 'Source3'),
(4, 'Source4');
```

```
INSERT INTO TargetTable (Col1, Col2)
VALUES
(1, 'Target1'),
(2, 'Target2'),
(3, 'Target3');
```

```
MERGE INTO TargetTable AS TGT
USING SourceTable AS SRC ON TGT.Col1 = SRC.Col1
WHEN MATCHED
    THEN UPDATE SET TGT.Col2 = SRC.Col2
WHEN NOT MATCHED
    THEN INSERT (Col1, Col2)
    VALUES (SRC.Col1, SRC.Col2);
```

```
SELECT * FROM TargetTable;
```

```
Col1  Col2
1     Target1
2     Source2
3     Source3
4     Source4
```

Perform a conditional two-way synchronization using NULL for no change and `DELETE` from the target when the data isn’t found in the source.

```
TRUNCATE TABLE SourceTable;
INSERT INTO SourceTable (Col1, Col2) VALUES (3, NULL), (4, 'NewSource4'), (5, 'Source5');
```

```
MERGE INTO TargetTable AS TGT
USING SourceTable AS SRC ON TGT.Col1 = SRC.Col1
WHEN MATCHED AND SRC.Col2 IS NOT NULL
    THEN UPDATE SET TGT.Col2 = SRC.Col2
WHEN NOT MATCHED
    THEN INSERT (Col1, Col2)
    VALUES (SRC.Col1, SRC.Col2)
WHEN NOT MATCHED BY SOURCE
    THEN DELETE;
```

```
SELECT *
FROM TargetTable;
```

```
Col1  Col2
3     Source3
4     NewSource4
5     Source5
```

For more information, see [MERGE (Transact-SQL)](https://docs.microsoft.com/en-us/sql/t-sql/statements/merge-transact-sql?view=sql-server-ver15) in the *SQL Server documentation*.

## MySQL Usage
<a name="chap-sql-server-aurora-mysql.tsql.merge.mysql"></a>

 Amazon Aurora MySQL-Compatible Edition (Aurora MySQL) doesn’t support the `MERGE` statement. However, it provides two other statements for merging data: `REPLACE`, and `INSERT…​ ON DUPLICATE KEY UPDATE`.

 `REPLACE` deletes a row and inserts a new row if a duplicate key conflict occurs. `INSERT…​ ON DUPLICATE KEY UPDATE` performs an in-place update. Both `REPLACE` and `ON DUPLICATE KEY UPDATE` rely on an existing primary key and unique constraints. It isn’t possible to define custom `MATCH` conditions as with SQL Server `MERGE` statement.

### REPLACE
<a name="chap-sql-server-aurora-mysql.tsql.merge.mysql.replace"></a>

 `REPLACE` provides a function similar to `INSERT`. The difference is that `REPLACE` first deletes an existing row if a duplicate key violation for a `PRIMARY KEY` or `UNIQUE` constraint occurs.

 `REPLACE` is a MySQL extension that isn’t ANSI compliant. It either performs only an INSERT when no duplicate key violations occur, or it performs a `DELETE` and then an `INSERT` if violations occur.

 **Syntax** 

```
REPLACE [INTO] <Table Name> (<Column List>)
VALUES (<Values List>)
```

```
REPLACE [INTO] <Table Name>
SET <Assignment List: ColumnName = VALUE...>
```

```
REPLACE [INTO] <Table Name> (<Column List>)
SELECT ...
```

### INSERT …​ ON DUPLICATE KEY UPDATE
<a name="chap-sql-server-aurora-mysql.tsql.merge.mysql.insert"></a>

The `ON DUPLICATE KEY UPDATE` clause of the `INSERT` statement acts as a dual DML hybrid. Similar to `REPLACE`, it runs the assignments in the `SET` clause instead of raising a duplicate key error. `ON DUPLICATE KEY UPDATE` is a MySQL extension that in not ANSI compliant.

 **Syntax** 

```
INSERT [INTO] <Table Name> [<Column List>]
VALUES (<Value List>
ON DUPLICATE KEY <Assignment List: ColumnName = Value...>
```

```
INSERT [INTO] <Table Name>
SET <Assignment List: ColumnName = Value...>
ON DUPLICATE KEY
    UPDATE <Assignment List: ColumnName = Value...>
```

```
INSERT [INTO] <Table Name> [<Column List>]
SELECT ...
ON DUPLICATE KEY
    UPDATE <Assignment List: ColumnName = Value...>
```

### Migration Considerations
<a name="chap-sql-server-aurora-mysql.tsql.merge.mysql.considerations"></a>

 `REPLACE` and `INSERT …​ ON DUPLICATE KEY UPDATE` don’t provide a full functional replacement for `MERGE` in SQL Server. The key differences are:
+ Key violation conditions are mandated by the primary key or unique constraints that exist on the target table. They can’t be defined using an explicit predicate.
+ There is no alternative for the WHEN NOT MATCHED BY SOURCE clause.
+ There is no alternative for the OUTPUT clause.

The key difference between `REPLACE` and `INSERT ON DUPLICATE KEY UPDATE` is that with `REPLACE`, the violating row is deleted or attempted to be deleted. If foreign keys are in place, the `DELETE` operation may fail, which may fail the entire transaction.

For `INSERT …​ ON DUPLICATE KEY UPDATE`, the update is performed on the existing row in place without attempting to delete it.

It should be straightforward to replace most `MERGE` statements with either `REPLACE` or `INSERT…​ ON DUPLICATE KEY UPDATE`.

Alternatively, break down the operations into their constituent `INSERT`, `UPDATE`, and `DELETE` statements.

### Examples
<a name="chap-sql-server-aurora-mysql.tsql.merge.mysql.examples"></a>

Use `REPLACE` to create a simple one-way, two-table sync.

```
CREATE TABLE SourceTable
(
    Col1 INT NOT NULL PRIMARY KEY,
    Col2 VARCHAR(20) NOT NULL
);
```

```
CREATE TABLE TargetTable
(
    Col1 INT NOT NULL PRIMARY KEY,
    Col2 VARCHAR(20) NOT NULL
);
```

```
INSERT INTO SourceTable (Col1, Col2)
VALUES
(2, 'Source2'),
(3, 'Source3'),
(4, 'Source4');
```

```
INSERT INTO TargetTable (Col1, Col2)
VALUES
(1, 'Target1'),
(2, 'Target2'),
(3, 'Target3');
```

```
REPLACE INTO TargetTable(Col1, Col2)
SELECT Col1,
    Col2
FROM SourceTable;
```

```
SELECT *
FROM TargetTable;
```

```
Col1  Col2
1     Target1
2     Source2
3     Source3
4     Source4
```

Create a conditional two-way sync using NULL for no change and `DELETE` from target when not found in source.

```
TRUNCATE TABLE SourceTable;
```

```
INSERT INTO SourceTable(Col1, Col2)
VALUES
(3, NULL),
(4, 'NewSource4'),
(5, 'Source5');
```

```
DELETE FROM TargetTable
WHERE Col1 NOT IN (SELECT Col1 FROM SourceTable);
```

```
INSERT INTO TargetTable (Col1, Col2)
SELECT Col1,
    Col2
FROM SourceTable AS SRC
WHERE SRC.Col1 NOT IN (
    SELECT Col1
    FROM TargetTable
);
```

```
UPDATE TargetTable AS TGT
SET Col2 = (
    SELECT COALESCE(SRC.Col2, TGT.Col2)
    FROM SourceTable AS SRC
    WHERE SRC.Col1 = TGT.Col1
    )
WHERE TGT.Col1 IN (
    SELECT Col1
    FROM SourceTable
);
```

```
SELECT *
FROM TargetTable;
```

```
Col1  Col2
3     Source3
4     NewSource4
5     Source5
```

## Summary
<a name="chap-sql-server-aurora-mysql.tsql.merge.summary"></a>

The following table describes similarities, differences, and key migration considerations.


| SQL Server MERGE feature | Migrate to Aurora MySQL  | Comments | 
| --- | --- | --- | 
| Define source set in `USING` clause. | Define source set in a `SELECT` query or in a table. |  | 
| Define logical duplicate key condition with an `ON` predicate. | Duplicate key condition mandated by primary key and unique constraints on target table. |  | 
|  `WHEN MATCHED THEN UPDATE`  |  `REPLACE` or `INSERT…​ ON DUPLICATE KEY UPDATE`  | When using `REPLACE`, the violating row will be deleted, or attempted to be deleted. If there are foreign keys in place, the `DELETE` operation may fail, which may fail the entire transaction.<br />With `INSERT …​ ON DUPLICATE KEY UPDATE`, the updated is performed on the existing row in place, without attempting to delete it. | 
|  `WHEN MATCHED THEN DELETE`  |  `DELETE FROM Target WHERE Key IN (SELECT Key FROM Source)`  |  | 
|  `WHEN NOT MATCHED THEN INSERT`  |  `REPLACE` or `INSERT…​ ON DUPLICATE KEY UPDATE`  | See the preceding comment. | 
|  `WHEN NOT MATCHED BY SOURCE UPDATE`  |  `UPDATE Target SET <assignments> WHERE Key NOT IN (SELECT Key FROM Source)`  |  | 
|  `WHEN NOT MATCHED BY SOURCE DELETE`  |  `DELETE FROM Target WHERE KEY NOT IN (SELECT Key FROM Source)`  |  | 
|  `OUTPUT` clause | N/A |  | 

For more information, see [REPLACE Statement](https://dev.mysql.com/doc/refman/5.7/en/replace.html) and [INSERT …​ ON DUPLICATE KEY UPDATE Statement](https://dev.mysql.com/doc/refman/5.7/en/insert-on-duplicate.html) in the *MySQL documentation*.