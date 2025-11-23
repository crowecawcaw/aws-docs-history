# Oracle user-defined types

With AWS DMS, you can migrate Oracle user-defined types (UDTs) to compatible AWS database services. Oracle UDTs are custom data types that extend the built-in scalar data types, allowing you to store complex data structures, such as objects and collections.

| Feature compatibility | AWS SCT / AWS DMS automation level | AWS SCT action code index                                                                                                                                                               | Key differences                                  |
| --------------------- | ---------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------ |
| No compatibility      | No automation                      | [User-Defined Types](chap-oracle-aurora-mysql.tools.md#chap-oracle-aurora-mysql.tools.actioncode.udt "chap-oracle-aurora-mysql.tools.md#chap-oracle-aurora-mysql.tools.actioncode.udt") | Aurora MySQL doesn’t support user-defined types. |

## Oracle usage

Oracle refers to user-defined types (UDTs) as `OBJECT TYPES`. These types are managed using PL/SQL. User-defined types enable the creation of application-dedicated, complex data types that are based on, and extend, the built-in Oracle data types.

The `CREATE TYPE` statement supports creation of the following types:

- Objects types
- Varying array or `varray` types
- Nested table types
- Incomplete types
- Additional types such as an SQLJ object type, which is a Java class mapped to SQL user-defined type

## Examples

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

## MySQL usage

Currently, Amazon Aurora MySQL doesn’t provide a directly comparable alternative for user-defined types.
