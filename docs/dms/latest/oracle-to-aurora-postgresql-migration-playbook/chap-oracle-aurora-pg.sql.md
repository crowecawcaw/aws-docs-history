# MERGE statement

With AWS DMS, you can perform Oracle `MERGE` statements and the PostgreSQL equivalent to conditionally insert, update, or delete rows in a target table based on the results of a join with a source table.

| Feature compatibility            | AWS SCT / AWS DMS automation level | AWS SCT action code index                                                                                                                                          | Key differences                                            |
| -------------------------------- | ---------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------- |
| Three star feature compatibility | No automation                      | [Merge](chap-oracle-aurora-pg.tools.md#chap-oracle-aurora-pg.tools.actioncode.merge "chap-oracle-aurora-pg.tools.md#chap-oracle-aurora-pg.tools.actioncode.merge") | MERGE isn’t supported by PostgreSQL, workaround available. |

## Oracle usage

The `MERGE` statement provides a means to specify single SQL statements that conditionally perform `INSERT`, `UPDATE`, or `DELETE` operations on a target table—a task that would otherwise require multiple logical statements.

The `MERGE` statement selects record(s) from the source table and then, by specifying a logical structure, automatically performs multiple DML operations on the target table. Its main advantage is to help avoid the use of multiple inserts, updates or deletes. It is important to note that `MERGE` is a deterministic statement. That is, once a row has been processed by the MERGE statement, it can’t be processed again using the same `MERGE` statement. `MERGE` is also sometimes known as `UPSERT`.

**Examples**

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
109         2017       9000   4500
110         2017       8200   4100
111         2017       7700   3850
112         2017       7800   3900
113         2017       6900   3450
115         2017       3100   1550
```

For more information, see [MERGE](https://docs.oracle.com/en/database/oracle/oracle-database/19/sqlrf/MERGE.html#GUID-5692CCB7-24D9-4C0E-81A7-A22436DC968F "https://docs.oracle.com/en/database/oracle/oracle-database/19/sqlrf/MERGE.html#GUID-5692CCB7-24D9-4C0E-81A7-A22436DC968F") in the _Oracle documentation_.

## PostgreSQL usage

PostgreSQL doesn’t support the use of the `MERGE` SQL command. As an alternative, consider using the `INSERT… ON CONFLICT` clause, which can handle cases where insert clauses might cause a conflict, and then redirect the operation as an update.

**Examples**

Using the `ON CONFLICT` clause to handle a similar scenario as shown for the Oracle `MERGE` command.

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
