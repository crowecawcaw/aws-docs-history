Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# downcase_delimited_identifier

## Values (default in bold)

**on**, off

## Description

This configuration is being retired. Instead use `enable_case_sensitive_identifier`.

Enables the super parser to read JSON fields that are in uppercase or mixed-case.
Also enables federated query support to supported PostgreSQL databases with mixed-case names of database, schema, table, and column.
To use case-sensitive identifiers, set this parameter to off.

## Usage Notes

- If you're using row-level security or dynamic data masking features, we
  recommend setting the `downcase_delimited_identifier` value in your cluster
  or workgroup's parameter group. This ensures that `downcase_delimited_identifier`
  stays constant throughout creating and attaching a policy, and then querying a relation
  that has a policy applied. For information on row-level security, see
  [Row-level security](t_rls.md "t_rls.md").
  For information on dynamic data masking, see
  [Dynamic data masking](t_ddm.md "t_ddm.md").
- When you set `downcase_delimited_identifier` to off and create a table,
  you can set case sensitive column names. When you set
  `downcase_delimited_identifier` to on and query the table, the column
  names are downcased. This can produce query results different from when
  `downcase_delimited_identifier` is set to off. Consider the following example:

```
SET downcase_delimited_identifier TO off;
--Amazon Redshift preserves case for column names and other identifiers.

--Create a table with two columns that are identical except for the case.
CREATE TABLE t ("c" int, "C" int);

INSERT INTO t VALUES (1, 2);

SELECT * FROM t;

 c | C
---+---
 1 | 2
(1 row)

SET enable_downcase_delimited_identifier TO on;
--Amazon Redshift no longer preserves case for column names and other identifiers.

SELECT * FROM t;

 c | c
---+---
 1 | 1
(1 row)
```

- We recommend that regular users querying tables with dynamic data masking or row-level security policies attached
  have the default downcase_delimited_identifier setting. For more information, see
  For information on row-level security, see
  [Row-level security](t_rls.md "t_rls.md").
  For information on dynamic data masking, see
  [Dynamic data masking](t_ddm.md "t_ddm.md").
