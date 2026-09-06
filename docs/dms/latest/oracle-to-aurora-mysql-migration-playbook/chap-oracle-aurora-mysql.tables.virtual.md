

# Oracle virtual columns and MySQL generated columns
<a name="chap-oracle-aurora-mysql.tables.virtual"></a>

With AWS DMS, you can seamlessly migrate databases that utilize virtual columns (Oracle) or generated columns (MySQL) to compatible target databases. Virtual columns and generated columns define values derived from other columns or expressions, providing a means to store computed data without modifying the base tables. This functionality is beneficial for applications relying on calculated fields, auditing requirements, or data denormalization strategies.


| Feature compatibility |  AWS SCT / AWS DMS automation level |  AWS SCT action code index | Key differences | 
| --- | --- | --- | --- | 
|  ![Four star feature compatibility](http://docs.aws.amazon.com/dms/latest/oracle-to-aurora-mysql-migration-playbook/images/pb-compatibility-4.png)  |  ![Three star automation level](http://docs.aws.amazon.com/dms/latest/oracle-to-aurora-mysql-migration-playbook/images/pb-automation-3.png)  |  [Creating Table](chap-oracle-aurora-mysql.tools.actioncode.md#chap-oracle-aurora-mysql.tools.actioncode.tables)  | Different paradigm and syntax. | 

## Oracle usage
<a name="chap-oracle-aurora-mysql.tables.virtual.oracle"></a>

Oracle virtual columns appear as normal columns, but their values are calculated instead of being stored in the database. You can’t create virtual columns based on other virtual columns and can only reference columns from the same table. When you create a virtual column, you can either explicitly specify the data type or let the database select the data type based on the expression.

You can use virtual columns with constraints, indexes, table partitioning, and foreign keys.

Functions in expressions must be deterministic at the time of table creation.

Virtual columns can’t be manipulated by DML operations.

You can use virtual columns in a `WHERE` clause and as part of DML commands.

When you create an index on a virtual column, Oracle creates a function-based index.

Virtual columns don’t support index-organized tables, external, objects, clusters, or temporary tables.

The output of a virtual column expression must be a scalar value.

The virtual column keywords `GENERATED ALWAYS AS` and `VIRTUAL` aren’t mandatory and are provided for clarity only.

```
COLUMN_NAME [data type] [GENERATED ALWAYS] AS (expression) [VIRTUAL]
```

The keyword `AS` after the column name indicates the column is created as a virtual column.

A virtual column doesn’t need to be specified in an `INSERT` statement.

### Examples
<a name="chap-oracle-aurora-mysql.tables.virtual.oracle.examples"></a>

Create a table that includes two virtual columns.

```
CREATE TABLE EMPLOYEES (
  EMPLOYEE_ID NUMBER,
  FIRST_NAME VARCHAR2(20),
  LAST_NAME VARCHAR2(25),
  USER_NAME VARCHAR2(25),
  EMAIL AS (LOWER(USER_NAME) || '@aws.com'),
  HIRE_DATE DATE,
  BASE_SALARY NUMBER,
  SALES_COUNT NUMBER,
  FINAL_SALARY NUMBER GENERATED ALWAYS AS
    (CASE WHEN SALES_COUNT >= 10 THEN BASE_SALARY +
    (BASE_SALARY * (SALES_COUNT * 0.05))
    END)
  VIRTUAL);
```

Insert a new record into the table without specifying values for the virtual column.

```
INSERT INTO EMPLOYEES
  (EMPLOYEE_ID, FIRST_NAME, LAST_NAME,
    USER_NAME, HIRE_DATE,BASE_SALARY, SALES_COUNT)
  VALUES(1, 'John', 'Smith', 'jsmith',
    '17-JUN-2003', 5000, 21);
```

Select the email Virtual Column from the table.

```
SELECT email FROM EMPLOYEES;

EMAIL           FINAL_SALARY
jsmith@aws.com  10250
```

For more information, see [CREATE TABLE](https://docs.oracle.com/en/database/oracle/oracle-database/19/sqlrf/CREATE-TABLE.html#GUID-F9CE0CC3-13AE-4744-A43C-EAC7A71AAAB6) in the *Oracle documentation*.

## MySQL usage
<a name="chap-oracle-aurora-mysql.tables.virtual.mysql"></a>

The syntax and functionality of generated columns are similar to virtual columns. They appear as normal columns, but their values are calculated. Generated columns cannot be created based on other Generated Columns and can only reference columns from the same table. When you create generated columns, make sure that you explicitly specify the data type of the column.
+ Unlike Oracle, you can create generated columns based on other generated columns preceding them in the field list.
+ You can use generated columns with constraints, indexes, table partitioning.
+ Functions in expressions must be deterministic at the time of table creation.
+ Generated columns can’t be manipulated by DML operations.
+ Generated columns can be used in a `WHERE` clause and as part of DML commands.
+ When you create an index on a generated column, the generated values are stored in the index.
+ The output of a generated column expression must be a scalar value.

### Examples
<a name="chap-oracle-aurora-mysql.tables.virtual.mysql.examples"></a>

Create a table that includes two generated columns.

```
CREATE TABLE EMPLOYEES (
  EMPLOYEE_ID INT,
  FIRST_NAME VARCHAR(20),
  LAST_NAME VARCHAR(25),
  USER_NAME VARCHAR(25),
  EMAIL VARCHAR(25) AS
    (CONCAT(LOWER(USER_ NAME),'@aws.com')),
  HIRE_DATE DATE,
  BASE_SALARY INT,
  SALES_COUNT INT,
  FINAL_SALARY INT GENERATED ALWAYS AS
    (CASE WHEN SALES_COUNT >= 10 THEN BASE_SALARY + (
    BASE_SALARY * (SALES_COUNT * 0.05)) END) VIRTUAL);
```

Insert a new record into the table without specifying values for the generated column.

```
INSERT INTO EMPLOYEES
  (EMPLOYEE_ID, FIRST_NAME, LAST_NAME, USER_NAME, HIRE_DATE,
  BASE_SALARY, SALES_COUNT)
  VALUES(1, 'John', 'Smith', 'jsmith', now(), 5000, 21);
```

Select the email and the generated column from the table.

```
SELECT EMAIL, FINAL_SALARY FROM EMPLOYEES;
```

For the preceding example, the result looks as shown following.

```
email           FINAL_SALARY
jsmith@aws.com  10250
```

For more information, see [CREATE TABLE and Generated Columns](https://dev.mysql.com/doc/refman/5.7/en/create-table-generated-columns.html) and [Secondary Indexes and Generated Columns](https://dev.mysql.com/doc/refman/5.7/en/create-table-secondary-indexes.html) in the *MySQL documentation*.