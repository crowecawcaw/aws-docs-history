

# Oracle function-based indexes and MySQL indexing on generated columns
<a name="chap-oracle-aurora-mysql.tables.expression"></a>

With AWS DMS, you can improve query performance by creating indexes on computed values or expressions in your databases. Oracle function-based indexes and MySQL indexes on generated columns let you index data derived from an expression or function, rather than just indexing on a column’s stored values. This can significantly speed up queries that filter or sort on calculated values.


| Feature compatibility |  AWS SCT / AWS DMS automation level |  AWS SCT action code index | Key differences | 
| --- | --- | --- | --- | 
|  ![Two star feature compatibility](http://docs.aws.amazon.com/dms/latest/oracle-to-aurora-mysql-migration-playbook/images/pb-compatibility-2.png)  |  ![No automation](http://docs.aws.amazon.com/dms/latest/oracle-to-aurora-mysql-migration-playbook/images/pb-automation-0.png)  |  [Indexes](chap-oracle-aurora-mysql.tools.actioncode.md#chap-oracle-aurora-mysql.tools.actioncode.indexes)  | MySQL doesn’t support functional indexes, a workaround is available. | 

## Oracle usage
<a name="chap-oracle-aurora-mysql.tables.expression.oracle"></a>

Function-based indexes allow functions to be used in the `WHERE` clause of queries on indexed columns. Function-based indexes store the output of a function applied on the values of a table column. The Oracle query optimizer only uses a function-based index when the function is used as part of a query.

Oracle updates the index for each DML to ensure that the value that returns from the function is correct.

### Example
<a name="chap-oracle-aurora-mysql.tables.expression.oracle.example"></a>

Create a function-based index.

```
CREATE TABLE SYSTEM_EVENTS(
  EVENT_ID NUMERIC PRIMARY KEY,
  EVENT_CODE VARCHAR2(10) NOT NULL,
  EVENT_DESCIPTION VARCHAR2(200),
  EVENT_TIME TIMESTAMPNOT NULL);

CREATE INDEX EVNT_BY_DAY ON SYSTEM_EVENTS(
  EXTRACT(DAY FROM EVENT_TIME));
```

For more information, see [Indexes and Index-Organized Tables](https://docs.oracle.com/en/database/oracle/oracle-database/19/cncpt/indexes-and-index-organized-tables.html#GUID-797E49E6-2DCE-4FD4-8E4A-6E761F1383D1) and [CREATE INDEX](https://docs.oracle.com/en/database/oracle/oracle-database/19/sqlrf/CREATE-INDEX.html#GUID-1F89BBC0-825F-4215-AF71-7588E31D8BFE) in the *Oracle documentation*.

## MySQL usage
<a name="chap-oracle-aurora-mysql.tables.expression.mysql"></a>

MySQL does not directly support a feature equivalent to Oracle function-based indexes. However, workarounds exist that can offer similar functionality. Specifically, you can create secondary indexes on MySQL generated columns. Implementing this workaround may require modification of existing SQL queries.

A generated column derives its values from the result of an expression. Creating an index on a generated column allows the generated column to be used in a WHERE clause of a query while accessing data with the index. Unlike Oracle function-based indexes, this workaround requires specifying the function in the table column specification.

You can create generated columns as `STORED` or `VIRTUAL`. For our purposes, we need to create generated columns as `STORED`. Otherwise, we won’t be able to index those columns.

MySQL can’t use stored routines or functions with generated columns.

Generated columns support NOT NULL restrictions.

A generated expression cannot exceed 64 KB for the entire table. For example, you can create a single field with a generated expression length of 64 KB or 12 fields with a length of 5 KB each.

A generated column can’t refer to itself or to other generated columns defined later, but it can refer to any previously defined generated columns.

The generation expression can only call native deterministic functions.

You can mix `VIRTUAL` and `STORED` columns within a table.

When you insert data to the table, make sure that you don’t reference the generated columns in your insert statement.

### Examples
<a name="chap-oracle-aurora-mysql.tables.expression.mysql.examples"></a>

Create a generated column that calculates the yearly salary based on the monthly salary, and create a secondary index on that column.

```
CREATE TABLE EMPS (ID INT, MONTH_SALARY INT,
  YEAR_SALARY INT GENERATED ALWAYS AS (MONTH_SALARY*12),
  INDEX FBI_YEAR_IDX (YEAR_SALARY));

INSERT INTO EMPS (ID, MONTH_SALARY) VALUES (1,10000);
INSERT INTO EMPS (ID, MONTH_SALARY) VALUES (2,8764);
INSERT INTO EMPS (ID, MONTH_SALARY) VALUES (3,4355);
INSERT INTO EMPS (ID, MONTH_SALARY) VALUES (4,6554);

SELECT * FROM EMPS;

ID  MONTH_SALARY  YEAR_SALARY
1   10000         120000
2   8764          105168
```

Queries can reference the `YEAR_SALARY` column as part of the `WHERE` clause and access data using the `FBI_YEAR_IDX` index.

```
SELECT * FROM EMPS WHERE YEAR_SALARY>80000;
SELECT * FROM EMPS WHERE MONTH_SALARY*12>80000;
```

Consider another example.

Create two generated columns using string manipulation functions as part of the table specification with secondary indexes on each.

```
CREATE TABLE EMPS (ID INT, FULL_NAME CHAR(40),
FIRST_NAME CHAR(20) GENERATED ALWAYS AS
  (SUBSTRING(FULL_NAME, 1,INSTR(FULL_NAME,' '))),
LAST_NAME CHAR(20) GENERATED ALWAYS AS
  (SUBSTRING(FULL_NAME, INSTR(FULL_NAME,' '))),
INDEX FBI_FNAME_IDX (FIRST_NAME),
INDEX FBI_LNAME_IDX (LAST_NAME));

INSERT INTO EMPS (ID, FULL_NAME) VALUES (1,'James Kirk');
INSERT INTO EMPS (ID, FULL_NAME) VALUES (2,'Benjamin Sisko');
INSERT INTO EMPS (ID, FULL_NAME) VALUES (3,'Karthryn Janeway');
INSERT INTO EMPS (ID, FULL_NAME) VALUES (4,'Jean- Luc Picard');
```

Queries can now use the `FBI_FNAME_IDX` index.

```
SELECT ID FROM EMPS WHERE
  SUBSTRING(FULL_NAME, 1,INSTR(FULL_NAME,' '))='Jacob';

SELECT ID FROM EMPS WHERE FIRST_NAME='Jacob';
```

**Note**  
For the preceding example, generated columns were not necessary. However, the generated columns were provided as an example. Instead, you can use a B-tree index created on the column prefix to achieve the same results.

```
CREATE TABLE EMPS (ID INT, FULL_NAME CHAR(40));
CREATE INDEX FBI_NAME_PREF_IDX ON EMPS (FULL_NAME(20));
```

For more information, see [CREATE TABLE and Generated Columns](https://dev.mysql.com/doc/refman/5.7/en/create-table-generated-columns.html) in the *MySQL documentation*.