# Merge for T-SQL

This topic contains reference information comparing the MERGE statement in SQL Server with equivalent functionality in PostgreSQL. You can understand the differences in feature compatibility between these database systems when migrating from Microsoft SQL Server 2019 to Amazon Aurora PostgreSQL.

| Feature compatibility            | AWS SCT / AWS DMS automation level | AWS SCT action code index                                                                                                                                                          | Key differences                        |
| -------------------------------- | ---------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------- |
| Three star feature compatibility | No automation                      | [MERGE](chap-sql-server-aurora-pg.tools.md#chap-sql-server-aurora-pg.tools.actioncode.merge "chap-sql-server-aurora-pg.tools.md#chap-sql-server-aurora-pg.tools.actioncode.merge") | Rewrite to use `INSERT…​ ON CONFLICT`. |

## SQL Server Usage

`MERGE` is a complex , hybrid DML/DQL statement for performing `INSERT`, `UPDATE`, or `DELETE` operations on a target table based on the results of a logical join of the target table and a source data set.

`MERGE` can also return row sets similar to SELECT using the OUTPUT clause, which gives the calling scope access to the actual data modifications of the `MERGE` statement.

The `MERGE` statement is most efficient for non-trivial conditional DML. For example, inserting data if a row key value doesn’t exist and updating the existing row if the key value already exists.

You can easily manage additional logic such as deleting rows from the target that don’t appear in the source. For simple, straightforward updates of data in one table based on data in another, it is typically more efficient to use simple `INSERT`, `DELETE`, and `UPDATE` statements. You can replace all `MERGE` functionality with `INSERT`, `DELETE`, and `UPDATE` statements, but not necessarily less efficiently.

The SQL Server `MERGE` statement provides a wide range of functionality and flexibility and is compatible with ANSI standard SQL:2008. SQL Server has many extensions to `MERGE` that provide efficient T-SQL solutions for synchronizing data.

### Syntax

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

The following example performs a simple one-way synchronization of two tables.

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

For the preceding examples, the result looks as shown following.

```
Col1  Col2
1     Target1
2     Source2
3     Source3
4     Source4
```

Perform a conditional two-way synchronization using `NULL` for no change and `DELETE` from the target when the data isn’t found in the source.

```
TRUNCATE TABLE SourceTable;
INSERT INTO SourceTable (Col1, Col2) VALUES (3, NULL), (4, 'NewSource4'), (5,'Source5');
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

For the preceding examples, the result looks as shown following.

```
Col1  Col2
3     Source3
4     NewSource4
5     Source5
```

For more information, see [MERGE (Transact-SQL)](https://docs.microsoft.com/en-us/sql/t-sql/statements/merge-transact-sql?view=sql-server-ver15 "https://docs.microsoft.com/en-us/sql/t-sql/statements/merge-transact-sql?view=sql-server-ver15") in the _SQL Server documentation_.

## PostgreSQL Usage

Currently, PostgreSQL version 10 doesn’t support the use of the `MERGE` command. As an alternative, consider using the `INSERT…​ ON CONFLICT` clause, which can handle cases where insert clauses might cause a conflict, and then redirect the operation as an update.

### Examples

The following example uses the `ON ONFLICT` clause.

```
CREATE TABLE EMP_BONUS (
EMPLOYEE_ID NUMERIC,
BONUS_YEAR VARCHAR(4),
SALARY NUMERIC,
BONUS NUMERIC,
PRIMARY KEY (EMPLOYEE_ID, BONUS_YEAR));

INSERT INTO EMP_BONUS (EMPLOYEE_ID, BONUS_YEAR, SALARY)
  SELECT EMPLOYEE_ID, EXTRACT(YEAR FROM NOW()), SALARY
  FROM EMPLOYEES
  WHERE SALARY < 10000
  ON CONFLICT (EMPLOYEE_ID, BONUS_YEAR)
  DO UPDATE SET BONUS = EMP_BONUS.SALARY * 0.5;
  SELECT * FROM EMP_BONUS;

employee_id  bonus_year  salary   bonus
103          2017        9000.00  4500.000
104          2017        6000.00  3000.000
105          2017        4800.00  2400.000
106          2017        4800.00  2400.000
107          2017        4200.00  2100.000
109          2017        9000.00  4500.000
110          2017        8200.00  4100.000
111          2017        7700.00  3850.000
112          2017        7800.00  3900.000
113          2017        6900.00  3450.000
115          2017        3100.00  1550.000
116          2017        2900.00  1450.000
117          2017        2800.00  1400.000
118          2017        2600.00  1300.000
```

Running the same operation multiple times using the `ON CONFLICT` clause doesn’t generate an error because the existing records are redirected to the update clause.

For more information, see [INSERT](https://www.postgresql.org/docs/13/sql-insert.html "https://www.postgresql.org/docs/13/sql-insert.html") and [Unsupported Features](https://www.postgresql.org/docs/13/unsupported-features-sql-standard.htm "https://www.postgresql.org/docs/13/unsupported-features-sql-standard.htm") in the _PostgreSQL documentation_.
