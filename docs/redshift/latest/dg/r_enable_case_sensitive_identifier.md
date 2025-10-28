Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# enable_case_sensitive_identifier

## Values (default in bold)

true, **false**

## Description

A configuration value that determines whether name identifiers of databases,
schemas, tables, and columns are case sensitive. The case of name identifiers is
preserved when you enclose identifiers within double quotation marks and set
`enable_case_sensitive_identifier` to `true`. The case of name
identifiers is not preserved, and instead converted to lowercase, when you do not
enclose identifiers within double quotation marks or when you set
`enable_case_sensitive_identifier` to `false`.

The case of a _username_ enclosed in double quotation marks is always preserved regardless of the setting of the `enable_case_sensitive_identifier` configuration option.

## Examples

The following example shows how to create and use case sensitive identifiers for a table and column name.

```
-- To create and use case sensitive identifiers
SET enable_case_sensitive_identifier TO true;

-- Create tables and columns with case sensitive identifiers
CREATE TABLE public."MixedCasedTable" ("MixedCasedColumn" int);

INSERT INTO public."MixedCasedTable" VALUES (1);
INSERT INTO public."MixedCasedTable" VALUES (2);
INSERT INTO public."MixedCasedTable" VALUES (3);
INSERT INTO public."MixedCasedTable" VALUES (4);
INSERT INTO public."MixedCasedTable" VALUES (5);

-- Now query with case sensitive identifiers
SELECT "MixedCasedColumn" FROM public."MixedCasedTable";
`MixedCasedColumn
------------------
1
2
3
4
5

(5 rows)`

SELECT * FROM public."MixedCasedTable" WHERE "MixedCasedColumn" = 1;
`mixedcasedcolumn
------------------
1

(1 row)`
```

The following example shows when the case of identifiers is not preserved.

```
-- To not use case sensitive identifiers
RESET enable_case_sensitive_identifier;

-- Mixed case identifiers are lowercased despite double quotation marks

CREATE TABLE "MixedCasedTable2" ("MixedCasedColumn" int);

CREATE TABLE MixedCasedTable2 (MixedCasedColumn int);
`ERROR: Relation "mixedcasedtable2" already exists`

SELECT "MixedCasedColumn" FROM "MixedCasedTable2";
`mixedcasedcolumn
------------------
(0 rows)`

SELECT MixedCasedColumn FROM MixedCasedTable2;
`mixedcasedcolumn
------------------
(0 rows)`
```

## Usage Notes

- If you're using autorefresh for materialized views, we
  recommend setting the `enable_case_sensitive_identifier` value in your cluster
  or workgroup's parameter group. This ensures that `enable_case_sensitive_identifier`
  stays constant when your materialized views are refreshed. For information on autorefresh
  for materialized views, see [Refreshing a materialized view](materialized-view-refresh.md "materialized-view-refresh.md").
  For information on setting configuration values in parameter groups,
  see
  [Amazon Redshift parameter groups](../mgmt/working-with-parameter-groups.md "../mgmt/working-with-parameter-groups.md") in the
  _Amazon Redshift Management Guide_.
- If you're using row-level security or dynamic data masking features, we
  recommend setting the `enable_case_sensitive_identifier` value in your cluster
  or workgroup's parameter group. This ensures that `enable_case_sensitive_identifier`
  stays constant throughout creating and attaching a policy, and then querying a relation
  that has a policy applied. For information on row-level security, see
  [Row-level security](t_rls.md "t_rls.md").
  For information on dynamic data masking, see
  [Dynamic data masking](t_ddm.md "t_ddm.md").
- When you set `enable_case_sensitive_identifier` to on and create a table,
  you can set case sensitive column names. When you set
  `enable_case_sensitive_identifier` to off and query the table, the column
  names are downcased. This can produce query results different from when `enable_case_sensitive_identifier`
  is set to on. Consider the following example:

```
SET enable_case_sensitive_identifier TO on;
--Amazon Redshift preserves case for column names and other identifiers.

--Create a table with two columns that are identical except for the case.
CREATE TABLE t ("c" int, "C" int);

INSERT INTO t VALUES (1, 2);

SELECT * FROM t;

 c | C
---+---
 1 | 2
(1 row)

SET enable_case_sensitive_identifier TO off;
--Amazon Redshift no longer preserves case for column names and other identifiers.

SELECT * FROM t;

 c | c
---+---
 1 | 1
(1 row)
```

- We recommend that regular users querying tables with dynamic data masking or row-level security policies attached
  have the default enable_case_sensitive_identifier setting. For information on row-level security, see
  [Row-level security](t_rls.md "t_rls.md").
  For information on dynamic data masking, see
  [Dynamic data masking](t_ddm.md "t_ddm.md").
- To reference identifiers with mixed case using dot notation, wrap each
  case-sensitive identifier in double quotation marks. For example,
  `public."MixedCasedTable"."MixedCasedColumn"`.
