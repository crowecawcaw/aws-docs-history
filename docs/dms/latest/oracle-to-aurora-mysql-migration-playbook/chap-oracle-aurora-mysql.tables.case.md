# Case sensitivity differences for Oracle and MySQL

Object name case sensitivity is different for Oracle and MySQL. Oracle names aren’t case sensitive. Aurora MySQL names are case sensitive.

In Aurora for MySQL, the case sensitivity is determined by the value of the `lower_case_table_names` parameter. You can choose one of the three possible values for this parameter. To avoid some issues, Amazon recommends to use only two values with this parameter:

- 0 (names stored as given and comparisons are case-sensitive) is supported for all Amazon RDS for MySQL versions.
- 1 (names stored in lowercase and comparisons are not case-sensitive) is supported for Amazon RDS for MySQL version 5.6, version 5.7, and version 8.0.19 and higher 8.0 versions.
  The `lower_case_table_names` parameter should be set as part of a custom DB parameter group before creating a DB instance. You should avoid changing the `lower_case_table_names` parameter for existing database
  instances because doing so could cause inconsistencies with point-in-time recovery backups and read replica DB instances.

Read replicas should always use the same `lower_case_table_names` parameter value as the source DB instance.

By default, object names are being stored in lowercase for MySQL. In most cases, you’ll want to use AWS Database Migration Service (AWS DMS) transformations to change schema, table, and column names to lowercase.

For example, to create a table named `EMPLOYEES` (uppercase) in MySQL, you should use double quotation marks as shown in the following code example. You can use the same approach in Oracle.

```
CREATE TABLE "EMPLOYEES" (
  EMP_ID NUMERIC PRIMARY KEY,
  EMP_FULL_NAME VARCHAR(60) NOT NULL,
  AVG_SALARY NUMERIC NOT NULL);
```

The following command creates a table named `employees` in lowercase.

```
CREATE TABLE EMPLOYEES (
  EMP_ID NUMERIC PRIMARY KEY,
  EMP_FULL_NAME VARCHAR(60) NOT NULL,
  AVG_SALARY NUMERIC NOT NULL);
```

MySQL will look for objects names in with the exact case sensitivity as written in the query.

You can disable table name case sensitivity in MySQL by setting the parameter `lower_case_table_names` to 1. Column, index, stored routine, event names, and column aliases are not case sensitive on either platform.

For more information, see [Identifier Case Sensitivity](https://dev.mysql.com/doc/refman/5.7/en/identifier-case-sensitivity.html "https://dev.mysql.com/doc/refman/5.7/en/identifier-case-sensitivity.html") in the _MySQL documentation_.
