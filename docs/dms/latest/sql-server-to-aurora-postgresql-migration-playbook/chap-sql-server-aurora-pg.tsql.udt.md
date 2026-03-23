# User-defined types for T-SQL

This topic provides reference information about user-defined types in SQL Server and PostgreSQL, which is valuable for database administrators and developers migrating from Microsoft SQL Server 2019 to Amazon Aurora PostgreSQL. You can gain insight into how both database systems implement custom data types, including their similarities and differences.

| Feature compatibility           | AWS SCT / AWS DMS automation level | AWS SCT action code index | Key differences                |
| ------------------------------- | ---------------------------------- | ------------------------- | ------------------------------ |
| Four star feature compatibility | Four star automation level         | N/A                       | Syntax and option differences. |

## SQL Server Usage

SQL Server user-defined types provide a mechanism for encapsulating custom data types and for adding NULL constraints.

SQL Server also supports table-valued user-defined types, which you can use to pass a set of values to a stored procedure.

User-defined types can also be associated to CLR code assemblies. Beginning with SQL Server 2014, memory optimized types support memory optimized tables and code.

###### Note

If your code uses custom rules bound to data types, Microsoft recommends discontinuing the use of this deprecated feature.

All user-defined types are based on an existing system data types. They allow developers to reuse the definition, making the code and schema more readable.

### Syntax

The simplified syntax for the `CREATE TYPE` statement is shown following.

```
CREATE TYPE <type name> {
FROM <base type> [ NULL | NOT NULL ] | AS TABLE (<Table Definition>)}
```

### User-Defined Types Examples

The following example creates a `ZipCode` scalar user-defined type.

```
CREATE TYPE ZipCode
FROM CHAR(5)
NOT NULL
```

The following example uses this `ZipCode` type in a table.

```
CREATE TABLE UserLocations
(UserID INT NOT NULL PRIMARY KEY, ZipCode ZipCode);

INSERT INTO [UserLocations] ([UserID],[ZipCode]) VALUES (1, '94324');
INSERT INTO [UserLocations] ([UserID],[ZipCode]) VALUES (2, NULL);
```

The code in the preceding example displays the following error message indicating that NULL values for `ZipCode` aren’t allowed.

```
Msg 515, Level 16, State 2, Line 78
Can't insert the value NULL into column 'ZipCode', table 'tempdb.dbo.UserLocations';
column does not allow nulls. INSERT fails.
The statement has been terminated.
```

### Table-Valued Types Examples

The following example demonstrates how to create and use a table-valued types to pass a set of values to a stored procedure.

Create the `OrderItems` table.

```
CREATE TABLE OrderItems
(
  OrderID INT NOT NULL,
  Item VARCHAR(20) NOT NULL,
  Quantity SMALLINT NOT NULL,
  PRIMARY KEY(OrderID, Item)
);
```

Create a table-valued type for the `OrderItems` table.

```
CREATE TYPE OrderItems
AS TABLE
(
  OrderID INT NOT NULL,
  Item VARCHAR(20) NOT NULL,
  Quantity SMALLINT NOT NULL,
  PRIMARY KEY(OrderID, Item)
);
```

Create the InsertOrderItems procedure. Note that the entire set of rows from the table-valued parameter is handled with one statement.

```
CREATE PROCEDURE InsertOrderItems
@OrderItems AS OrderItems READONLY
AS
BEGIN
  INSERT INTO OrderItems(OrderID, Item, Quantity)
  SELECT OrderID,
    Item,
    Quantity
  FROM @OrderItems;
END
```

Instantiate the OrderItems type, insert the values, and pass it to a stored procedure.

```
DECLARE @OrderItems AS OrderItems;

INSERT INTO @OrderItems ([OrderID], [Item], [Quantity])
VALUES
(1, 'M8 Bolt', 100),
(1, 'M8 Nut', 100),
(1, M8 Washer, 200);

EXECUTE [InsertOrderItems] @OrderItems = @OrderItems;

(3 rows affected)
```

Select all rows from the OrderItems table.

```
SELECT * FROM OrderItems;

OrderID  Item       Quantity
1        M8 Bolt    100
1        M8 Nut     100
1        M8 Washer  200
```

For more information, see [CREATE TYPE (Transact-SQL)](https://docs.microsoft.com/en-us/sql/t-sql/statements/create-type-transact-sql?view=sql-server-ver15 "https://docs.microsoft.com/en-us/sql/t-sql/statements/create-type-transact-sql?view=sql-server-ver15") in the _SQL Server documentation_.

## PostgreSQL Usage

Similar to SQL Server, PostgreSQL enables the creation of user-defined types using the `CREATE TYPE` statement.

A user-defined type is owned by the user who creates it. If a schema name is specified, the type is created under that schema.

PostgreSQL supports the creation of several different user-defined types: \* Composite types store a single named attribute attached to a data type or multiple attributes as an attribute collection. In PostgreSQL, you can also use the CREATE TYPE statement standalone with an association to a table. \* Enumerated types (enum) store a static ordered set of values. For example, product categories.

-

```
CREATE TYPE PRODUCT_CATEGORT AS ENUM
  ('Hardware', 'Software', 'Document');
```

- Range Types store a range of values, for example, a range of timestamps used to represent the ranges of time of when a course is scheduled.

```
CREATE TYPE float8_range AS RANGE
  (subtype = float8, subtype_diff = float8mi);
```

For more information, see [Range Types](https://www.postgresql.org/docs/13/rangetypes.html "https://www.postgresql.org/docs/13/rangetypes.html") in the _PostgreSQL documentation_.

- Base types are the system core types (abstract types) and are implemented in a low-level language such as C.
- Array types support definition of columns as multidimensional arrays. You can create an array column with a built-in type or a user-defined base type, enum type, or composite.

```
CREATE TABLE COURSE_SCHEDULE (
  COURSE_ID NUMERIC PRIMARY KEY,
  COURSE_NAME VARCHAR(60),
  COURSE_SCHEDULES text[]);
```

For more information, see [Arrays](https://www.postgresql.org/docs/13/arrays.html "https://www.postgresql.org/docs/13/arrays.html") in the _PostgreSQL documentation_.

### Syntax

```
CREATE TYPE name AS RANGE (
  SUBTYPE = subtype
  [ , SUBTYPE_OPCLASS = subtype_operator_class ]
  [ , COLLATION = collation ]
  [ , CANONICAL = canonical_function ]
  [ , SUBTYPE_DIFF = subtype_diff_function ]
)
CREATE TYPE name (
  INPUT = input_function,
  OUTPUT = output_function
  [ , RECEIVE = receive_function ]
  [ , SEND = send_function ]
  [ , TYPMOD_IN = type_modifier_input_function ]
  [ , TYPMOD_OUT = type_modifier_output_function ]
  [ , ANALYZE = analyze_function ]
  [ , INTERNALLENGTH = { internallength | VARIABLE } ]
  [ , PASSEDBYVALUE ]
  [ , ALIGNMENT = alignment ]
  [ , STORAGE = storage ]
  [ , LIKE = like_type ]
  [ , CATEGORY = category ]
  [ , PREFERRED = preferred ]
  [ , DEFAULT = default ]
  [ , ELEMENT = element ]
  [ , DELIMITER = delimiter ]
  [ , COLLATABLE = collatable ]
)
```

### Examples

The following example creates a user-defined type for storing an employee phone numbers.

```
CREATE TYPE EMP_PHONE_NUM AS (
  PHONE_NUM VARCHAR(11));

CREATE TABLE EMPLOYEES (
  EMP_ID NUMERIC PRIMARY KEY,
  EMP_PHONE EMP_PHONE_NUM NOT NULL);

INSERT INTO EMPLOYEES VALUES(1, ROW('111-222-333'));

SELECT a.EMP_ID, (a.EMP_PHONE).PHONE_NUM FROM EMPLOYEES a;

emp_id  phone_num
1       111-222-333
(1 row)
```

The following example creates a PostgreSQL Object Type as a collection of Attributes for the employees table.

```
CREATE OR REPLACE TYPE EMP_ADDRESS AS OBJECT (
  STATE VARCHAR(2),
  CITY VARCHAR(20),
  STREET VARCHAR(20),
  ZIP_CODE NUMERIC);

CREATE TABLE EMPLOYEES (
  EMP_ID NUMERIC PRIMARY KEY,
  EMP_NAME VARCHAR(10) NOT NULL,
  EMP_ADDRESS EMP_ADDRESS NOT NULL);

INSERT INTO EMPLOYEES
  VALUES(1, 'John Smith',
  ('AL', 'Gulf Shores', '3033 Joyce Street', '36542'));

SELECT a.EMP_NAME,
  (a.EMP_ADDRESS).STATE,
  (a.EMP_ADDRESS).CITY,
  (a.EMP_ADDRESS).STREET,
  (a.EMP_ADDRESS).ZIP_CODE
FROM EMPLOYEES a;

emp_name    state  city         street             zip_code
John Smith  AL     Gulf Shores  3033 Joyce Street  36542
```

For more information, see [CREATE TYPE](https://www.postgresql.org/docs/13/sql-createtype.html "https://www.postgresql.org/docs/13/sql-createtype.html") and [Composite Types](https://www.postgresql.org/docs/13/rowtypes.htm "https://www.postgresql.org/docs/13/rowtypes.htm") in the _PostgreSQL documentation_.
