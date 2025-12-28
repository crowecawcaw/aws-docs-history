# Oracle MERGE statement and MySQL equivalent

With AWS DMS, you can perform Oracle `MERGE` statements and the MySQL equivalent to conditionally insert, update, or delete rows in a target table based on the results of a join with a source table.

| Feature compatibility            | AWS SCT / AWS DMS automation level | AWS SCT action code index                                                                                                                                                      | Key differences                                                                |
| -------------------------------- | ---------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| Three star feature compatibility | No automation                      | [Merge](chap-oracle-aurora-mysql.tools.md#chap-oracle-aurora-mysql.tools.actioncode.merge "chap-oracle-aurora-mysql.tools.md#chap-oracle-aurora-mysql.tools.actioncode.merge") | Aurora MySQL doesn’t support the `MERGE` statement. A workaround is available. |

## Oracle usage

The `MERGE` statement provides a means to specify single SQL statements that conditionally perform `INSERT`, `UPDATE`, or `DELETE` operations on a target table—a task that would otherwise require multiple logical statements.

The `MERGE` statement selects record(s) from the source table and then, by specifying a logical structure, automatically performs multiple DML operations on the target table. Its main advantage is to help avoid the use of multiple inserts, updates or deletes. It is important to note that `MERGE` is a deterministic statement. That is, once a row has been processed by the MERGE statement, it can’t be processed again using the same `MERGE` statement. `MERGE` is also sometimes known as `UPSERT`.

### Examples

Use `MERGE` to insert or update employees who are entitled to a bonus (by year).

```
CREATE TABLE EMP_BONUS(EMPLOYEE_ID NUMERIC,BONUS_YEAR VARCHAR2(4),
SALARY NUMERIC,BONUS NUMERIC, PRIMARY KEY (EMPLOYEE_ID, BONUS_YEAR));

MERGE INTO EMP_BONUS E1
USING (SELECT EMPLOYEE_ID, FIRST_NAME, SALARY, DEPARTMENT_ID
FROM EMPLOYEES) E2 ON (E1.EMPLOYEE_ID = E2.EMPLOYEE_ID) WHEN MATCHED THEN
UPDATE SET E1.BONUS = E2.SALARY * 0.5
DELETE WHERE (E1.SALARY >= 10000)
WHEN NOT MATCHED THEN
INSERT (E1.EMPLOYEE_ID, E1.BONUS_YEAR, E1.SALARY , E1.BONUS)
VALUES (E2.EMPLOYEE_ID, EXTRACT(YEAR FROM SYSDATE), E2.SALARY,
E2.SALARY * 0.5)
WHERE (E2.SALARY < 10000);

SELECT * FROM EMP_BONUS;

EMPLOYEE_ID BONUS_YEAR SALARY BONUS
103         2017       9000   4500
104         2017       6000   3000
105         2017       4800   2400
106         2017       4800   2400
107         2017       4200   2100
111         2017       7700   3850
112         2017       7800   3900
113         2017       6900   3450
115         2017       3100   1550
```

For more information, see [MERGE](https://docs.oracle.com/en/database/oracle/oracle-database/19/sqlrf/MERGE.html#GUID-5692CCB7-24D9-4C0E-81A7-A22436DC968F "https://docs.oracle.com/en/database/oracle/oracle-database/19/sqlrf/MERGE.html#GUID-5692CCB7-24D9-4C0E-81A7-A22436DC968F") in the _Oracle documentation_.

## MySQL usage

Aurora MySQL doesn’t support the `MERGE` statement. However, it provides two other statements for merging data: `REPLACE`, and `INSERT…​ ON DUPLICATE KEY UPDATE`.

`REPLACE` deletes a row and inserts a new row if a duplicate key conflict occurs. `INSERT…​ ON DUPLICATE KEY UPDATE` performs an in-place update. Both `REPLACE` and `ON DUPLICATE KEY UPDATE` rely on an existing primary key and unique constraints. It is not possible to define custom `MATCH` conditions as with the `MERGE` statement in Oracle.

`REPLACE` provides a function similar to `INSERT`. The difference is that `REPLACE` first deletes an existing row if a duplicate key violation for a `PRIMARY KEY` or `UNIQUE` constraint occurs.

`REPLACE` is a MySQL extension that is not ANSI compliant. It either performs only an `INSERT` when no duplicate key violations occur, or it performs a `DELETE` and then an `INSERT` if violations occur.

### Syntax

```
REPLACE [INTO] <Table Name> (<Column List>) VALUES v(<Values List>)
```

```
REPLACE [INTO] <Table Name> SET <Assignment List: ColumnName = VALUE...>
```

```
REPLACE [INTO] <Table Name> (<Column List>) SELECT ...
```

### INSERT …​ ON DUPLICATE KEY UPDATE

The `ON DUPLICATE KEY UPDATE` clause of the `INSERT` statement acts as a dual DML hybrid. Similar to `REPLACE`, it executes the assignments in the `SET` clause instead of raising a duplicate key error. `ON DUPLICATE KEY UPDATE` is a MySQL extension that in not ANSI compliant.

```
INSERT [INTO] <Table Name> [<Column List>] VALUES (<Value List>
ON DUPLICATE KEY <Assignment List: ColumnName = Value...>
```

```
INSERT [INTO] <Table Name> SET <Assignment List: ColumnName = Value...>
ON DUPLICATE KEY UPDATE <Assignment List: ColumnName = Value...>
```

```
INSERT [INTO] <Table Name> [<Column List>] SELECT ... ON DUPLICATE KEY
UPDATE <Assignment List: ColumnName = Value...>
```

### Migration considerations

Neither `REPLACE` nor `INSERT …​ ON DUPLICATE KEY UPDATE` provide a full functional replacement for the `MERGE` statement in Oracle. The key differences are:

- Key violation conditions are mandated by the primary key or unique constraints that exist on the target table. They can’t be defined using an explicit predicate.
- There is no alternative for the `WHEN NOT MATCHED BY SOURCE` clause.
- There is no alternative for the `OUTPUT` clause.

The key difference between `REPLACE` and `INSERT ON DUPLICATE KEY UPDATE` is that with `REPLACE`, the violating row is deleted or attempted to be deleted. If foreign keys are in place, the `DELETE` operation may fail, which may fail the entire transaction.

For `INSERT …​ ON DUPLICATE KEY UPDATE`, the update is performed on the existing row in place without attempting to delete it.

It should be straightforward to replace most `MERGE` statements with either `REPLACE` or `INSERT…​ ON DUPLICATE KEY UPDATE`. Alternatively, break down the operations into their constituent `INSERT`, `UPDATE`, and `DELETE` statements.

### Examples

Use `REPLACE` to create a simple one-way, two-table sync.

```
CREATE TABLE SourceTable (Col1 INT NOT NULL PRIMARY KEY,
  Col2 VARCHAR(20) NOT NULL);
CREATE TABLE TargetTable (Col1 INT NOT NULL PRIMARY KEY,
  Col2 VARCHAR(20) NOT NULL);
```

```
INSERT INTO SourceTable (Col1, Col2)
  VALUES (2, 'Source2'), (3, 'Source3'), (4, 'Source4');
INSERT INTO TargetTable (Col1, Col2)
  VALUES (1, 'Target1'), (2, 'Target2'), (3, 'Target3');
```

```
REPLACE INTO TargetTable(Col1, Col2)
  SELECT Col1, Col2 FROM SourceTable;
```

```
SELECT * FROM TargetTable;
```

For the preceding example, the result looks as shown following.

```
Col1  Col2
1     Target1
2     Source2
3     Source3
4     Source4
```

The following example creates a conditional two-way sync using NULL for no change and `DELETE` from target when not found in source.

```
TRUNCATE TABLE SourceTable;
```

```
INSERT INTO SourceTable(Col1, Col2)
  VALUES (3, NULL), (4, 'NewSource4'), (5, 'Source5');
DELETE FROM TargetTable
  WHERE Col1 NOT IN (SELECT Col1 FROM SourceTable);
```

```
INSERT INTO TargetTable (Col1, Col2)
SELECT Col1, Col2
FROM SourceTable AS SRC
WHERE SRC.Col1 NOT IN (SELECT Col1 FROM TargetTable);
```

```
UPDATE TargetTable AS TGT
SET Col2 = (SELECT COALESCE(SRC.Col2, TGT.Col2)
FROM SourceTable AS SRC WHERE SRC.Col1 = TGT.Col1)
WHERE TGT.Col1 IN (SELECT Col1 FROM SourceTable);
```

```
SELECT * FROM TargetTable;
```

For the preceding example, the result looks as shown following.

```
Col1  Col2
3     Source3
4     NewSource4
5     Source5
```

## Summary

The following table describes similarities, differences, and key migration considerations.

| Oracle MERGE feature                                           | Migrate to Aurora MySQL                                                                 | Comments                                                                                                                                                                                                                                                                                                                     |
| -------------------------------------------------------------- | --------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Define source set in `USING` clause.                           | Define source set in a `SELECT` query or in a table.                                    |                                                                                                                                                                                                                                                                                                                              |
| Define logical duplicate key condition with an `ON` predicate. | Duplicate key condition mandated by primary key and unique constraints on target table. |                                                                                                                                                                                                                                                                                                                              |
| `WHEN MATCHED THEN UPDATE`                                     | `REPLACE` or `INSERT…​ ON DUPLICATE KEY UPDATE`                                         | When using `REPLACE`, the violating row is deleted, or attempted to be deleted. If there are foreign keys in place, the `DELETE` operation may fail, which may fail the entire transaction. With `INSERT …​ ON DUPLICATE KEY UPDATE`, the update is performed on the existing row in place, without attempting to delete it. |
| `WHEN MATCHED THEN DELETE`                                     | `DELETE FROM Target WHERE Key IN (SELECT Key FROM Source)`                              |                                                                                                                                                                                                                                                                                                                              |
| `WHEN NOT MATCHED THEN INSERT`                                 | `REPLACE` or `INSERT…​ ON DUPLICATE KEY UPDATE`                                         | When using REPLACE, the violating row is deleted, or attempted to be deleted. If there are foreign keys in place, the `DELETE` operation may fail, which may fail the entire transaction. With `INSERT …​ ON DUPLICATE KEY UPDATE`, the update is performed on the existing row in place, without attempting to delete it.   |

For more information, see [REPLACE Statement](https://dev.mysql.com/doc/refman/5.7/en/replace.html "https://dev.mysql.com/doc/refman/5.7/en/replace.html") and [INSERT …​ ON DUPLICATE KEY UPDATE Statement](https://dev.mysql.com/doc/refman/5.7/en/insert-on-duplicate.html "https://dev.mysql.com/doc/refman/5.7/en/insert-on-duplicate.html") in the _MySQL documentation_.
