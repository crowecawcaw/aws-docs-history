# Oracle and PostgreSQL user-defined types

With AWS DMS, you can migrate user-defined types (UDTs) from Oracle and PostgreSQL databases to compatible target databases. UDTs extend the database’s built-in data types by providing a way to store complex data structures like objects or custom data types.

| Feature compatibility           | AWS SCT / AWS DMS automation level | AWS SCT action code index                                                                                                                                                   | Key differences                                                                                                                     |
| ------------------------------- | ---------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- |
| Four star feature compatibility | Four star automation level         | [User-Defined Types](chap-oracle-aurora-pg.tools.md#chap-oracle-aurora-pg.tools.actioncode.udt "chap-oracle-aurora-pg.tools.md#chap-oracle-aurora-pg.tools.actioncode.udt") | PostgreSQL doesn’t support `FORALL` statement and `DEFAULT` option. PostgreSQL doesn’t support constructors of the collection type. |

## Oracle usage

Oracle refers to user-defined types (UDTs) as `OBJECT TYPES`. These types are managed using PL/SQL. User-defined types enable the creation of application-dedicated, complex data types that are based on, and extend, the built-in Oracle data types.

The `CREATE TYPE` statement supports creating of the following types:app-name:

- Objects types
- Varying array (varray) types
- Nested table types
- Incomplete types
- Additional types such as an SQLJ object type (a Java class mapped to SLQ user defined type)

**Examples**

Create an Oracle Object Type to store an employee phone number.

```
CREATE OR REPLACE TYPE EMP_PHONE_NUM AS OBJECT (
  PHONE_NUM VARCHAR2(11));

CREATE TABLE EMPLOYEES (
  EMP_ID NUMBER PRIMARY KEY,
  EMP_PHONE EMP_PHONE_NUM NOT NULL);

INSERT INTO EMPLOYEES VALUES(1, EMP_PHONE_NUM('111-222-333'));
SELECT a.EMP_ID, a.EMP_PHONE.PHONE_NUM FROM EMPLOYEES a;

EMP_ID  EMP_PHONE.P
1       111-222-333
```

Create an Oracle object type as a collection of attributes for the employees table.

```
CREATE OR REPLACE TYPE EMP_ADDRESS AS OBJECT (
  STATE VARCHAR2(2),
  CITY VARCHAR2(20),
  STREET VARCHAR2(20),
  ZIP_CODE NUMBER);

CREATE TABLE EMPLOYEES (
  EMP_ID NUMBER PRIMARY KEY,
  EMP_NAME VARCHAR2(10) NOT NULL,
  EMP_ADDRESS EMP_ADDRESS NOT NULL);

INSERT INTO EMPLOYEES VALUES(1, 'John Smith',
  EMP_ADDRESS('AL', 'Gulf Shores', '3033 Joyce Street', '36542'));

SELECT a.EMP_ID, a.EMP_NAME, a.EMP_ADDRESS.STATE,
  a.EMP_ADDRESS.CITY, a.EMP_ADDRESS.STREET, a.EMP_ADDRESS.ZIP_CODE
  FROM EMPLOYEES a;

EMP_ID  EMP_NAME    STATE  CITY         STREET             ZIP_CODE
1       John Smith  AL     Gulf Shores  3033 Joyce Street  36542
```

For more information, see [CREATE TYPE](https://docs.oracle.com/en/database/oracle/oracle-database/19/sqlrf/CREATE-TYPE.html#GUID-E72E3EE6-DE95-4F58-8941-E2F76D0EAE80 "https://docs.oracle.com/en/database/oracle/oracle-database/19/sqlrf/CREATE-TYPE.html#GUID-E72E3EE6-DE95-4F58-8941-E2F76D0EAE80") and [CREATE TYPE BODY](https://docs.oracle.com/en/database/oracle/oracle-database/19/sqlrf/CREATE-TYPE-BODY.html#GUID-C4F1591A-6F62-4897-9039-2C3F066F1E9D "https://docs.oracle.com/en/database/oracle/oracle-database/19/sqlrf/CREATE-TYPE-BODY.html#GUID-C4F1591A-6F62-4897-9039-2C3F066F1E9D") in the _Oracle documentation_.

## PostgreSQL usage

Similar to Oracle, PostgreSQL enables creation of user-defined types using the `CREATE TYPE` statement. A user-defined type is owned by the user who creates it. If a schema name is specified, the type is created under the specified schema.

PostgreSQL supports the creation of several different user-defined types.

- **Composite** — Stores a single named attribute that is attached to a data type or multiple attributes as an attribute collection. In PostgreSQL, you can also use the `CREATE TYPE` statement standalone with an association to a table.
- **Enumerated (enum)** — Stores a static ordered set of values. For example, product categories.

```
CREATE TYPE PRODUCT_CATEGORT AS ENUM ('Hardware', 'Software', 'Document');
```

- **Range** — Stores a range of values, for example, a range of timestamps used to represent the ranges of time of when a course is scheduled.

```
CREATE TYPE float8_range AS RANGE (subtype = float8, subtype_diff = float8mi);
```

For more information, see [Range Types](https://www.postgresql.org/docs/10/rangetypes.html "https://www.postgresql.org/docs/10/rangetypes.html") in the _PostgreSQL documentation_.

- **Base** — These types are the system core types (abstract types) and are implemented in a low-level language such as C.
- **Array** — Support definition of columns as multidimensional arrays. An array column can be created with a built-in type or a user-defined base type, enum type, or composite.

```
CREATE TABLE COURSE_SCHEDULE (
  COURSE_ID NUMERIC PRIMARY KEY,
  COURSE_NAME VARCHAR(60),
  COURSE_SCHEDULES text[]);
```

For more information, see [Arrays](https://www.postgresql.org/docs/13/arrays.html "https://www.postgresql.org/docs/13/arrays.html") in the _PostgreSQL documentation_.

## PostgreSQL CREATE TYPE synopsis

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

PostgreSQL syntax differences from Oracle `CREATE TYPE` statement.

- PostgreSQL doesn’t support `CREATE OR REPLACE TYPE`.
- PostgreSQL doesn’t accept `AS OBJECT`.

**Examples**

Create a user-defined type as a dedicated type for storing an employee phone number.

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

Create a PostgreSQL object type as a collection of Attributes for the employees table.

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
