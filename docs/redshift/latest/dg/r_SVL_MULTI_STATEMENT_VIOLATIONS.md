Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# SVL_MULTI_STATEMENT_VIOLATIONS

Use the SVL_MULTI_STATEMENT_VIOLATIONS view to get a complete record of all of the SQL commands run on the system that violates transaction block restrictions.

Violations occur when you run any of the following SQL commands that Amazon Redshift restricts inside a transaction block or
multi-statement requests:

- [CREATE DATABASE](r_CREATE_DATABASE.md "r_CREATE_DATABASE.md")
- [DROP DATABASE](r_DROP_DATABASE.md "r_DROP_DATABASE.md")
- [ALTER TABLE APPEND](r_ALTER_TABLE_APPEND.md "r_ALTER_TABLE_APPEND.md")
- [CREATE EXTERNAL TABLE](r_CREATE_EXTERNAL_TABLE.md "r_CREATE_EXTERNAL_TABLE.md")
- DROP EXTERNAL TABLE
- RENAME EXTERNAL TABLE
- ALTER EXTERNAL TABLE
- CREATE TABLESPACE
- DROP TABLESPACE
- [CREATE LIBRARY](r_CREATE_LIBRARY.md "r_CREATE_LIBRARY.md")
- [DROP LIBRARY](r_DROP_LIBRARY.md "r_DROP_LIBRARY.md")
- REBUILDCAT
- INDEXCAT
- REINDEX DATABASE
- [VACUUM](r_VACUUM_command.md "r_VACUUM_command.md")
- [GRANT](r_GRANT.md "r_GRANT.md")
- [COPY](r_COPY.md "r_COPY.md")

###### Note

If there are any entries in this view, then change your corresponding applications and SQL scripts. We recommend changing your application code to move the use of these restricted SQL commands outside of the transaction block. If you need further assistance, contact AWS Support.

SVL_MULTI_STATEMENT_VIOLATIONS is visible to all users. Superusers can see all rows; regular users can see only their own data. For more information, see [Visibility of data in system tables and
views](cm_chap_system-tables.md#c_visibility-of-data "cm_chap_system-tables.md#c_visibility-of-data").

Some or all of the data in this table can also be found in the SYS monitoring view [SYS_QUERY_HISTORY](SYS_QUERY_HISTORY.md "SYS_QUERY_HISTORY.md"). The data in the SYS monitoring view is formatted to be easier to use and understand.
We recommend that you use the SYS monitoring view for your queries.

## Table

columns

| Column name | Data type      | Description                                                                                                                                                                                                                                                                                                                                                                                                                |
| ----------- | -------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------- | ------- | --- | --- | ----- | --------- | ------- | -------- | ---- | ------------------------------------------------------------------------------------------------------------------------------------- | --- | --------------- | ---- | ---- | ------ | ---------- | ---------- | --- | --- | ------------------------ | --- | --------------- | ---- | ---- | ------ | ---------- | ---------- | --- | ------- | -------------------- | --- | --------------- | ---- | ---- | ------ | ---------- | ---------- | --- | ------- | -------------- |
| userid      | integer        | The ID of the user who caused the violation.                                                                                                                                                                                                                                                                                                                                                                               |
| database    | character(32)  | The name of the database that the user was connected to.                                                                                                                                                                                                                                                                                                                                                                   |
| cmdname     | character(20)  | The name of the command that cannot run inside a transaction block or multi-statement request. For example, CREATE DATABASE, DROP DATABASE, ALTER TABLE APPEND, CREATE EXTERNAL TABLE, DROP EXTERNAL TABLE, RENAME EXTERNAL TABLE, ALTER EXTERNAL TABLE, CREATE LIBRARY, DROP LIBRARY, REBUILDCAT, INDEXCAT, REINDEX DATABASE, VACUUM, GRANT on external resources, CLUSTER, COPY, CREATE TABLESPACE, and DROP TABLESPACE. |
| xid         | bigint         | The transaction ID associated with the statement.                                                                                                                                                                                                                                                                                                                                                                          |
| pid         | integer        | The process ID for the statement.                                                                                                                                                                                                                                                                                                                                                                                          |
| label       | character(320) | Either the name of the file used to run the query or a label defined with a SET QUERY_GROUP command. If the query is not file-based or the QUERY_GROUP parameter is not set, this field is blank.                                                                                                                                                                                                                          |
| starttime   | timestamp      | The exact time when the statement started executing, with 6 digits of precision for fractional seconds, for example: `2009-06-12 11:29:19.131358`                                                                                                                                                                                                                                                                          |
| endtime     | timestamp      | The exact time when the statement finished executing, with 6 digits of precision for fractional seconds, for example: `2009-06-12 11:29:19.193640`                                                                                                                                                                                                                                                                         |
| sequence    | integer        | When a single statement contains more than 200 characters, additional rows are logged for that statement. Sequence 0 is the first row, 1 is the second, and so on.                                                                                                                                                                                                                                                         |
| type        | varchar(10)    | The type of SQL statement: `QUERY`, `DDL`, or `UTILITY`.                                                                                                                                                                                                                                                                                                                                                                   |
| text        | character(200) | The SQL text, in 200-character increments. This field might contain special characters such as backslash (`\\`) and newline (`\n`).                                                                                                                                                                                                                                                                                        | ## Sample query The following query returns multiple statements that have violations. ``` select \* from svl_multi_statement_violations order by starttime asc; userid | database | cmdname | xid | pid | label | starttime | endtime | sequence | type | text ============================================================================================================================== 1 | dev | CREATE DATABASE | 1034 | 5729 | label1 | ****\***** | **\*\*\*** | 0   | DDL | create table c(b int); 1 | dev | CREATE DATABASE | 1034 | 5729 | label1 | ****\***** | **\*\*\*** | 0   | UTILITY | create database b; 1 | dev | CREATE DATABASE | 1034 | 5729 | label1 | ****\***** | **\*\*\*** | 0   | UTILITY | COMMIT ... ``` |
