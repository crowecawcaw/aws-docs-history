Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# enable_case_sensitive_super_attribute

## Values (default in bold)

true, **false**

## Description

A configuration value that determines whether navigating SUPER data type structures with non-delimited attribute names is case sensitive.
When you set
`enable_case_sensitive_super_attribute` to `true`, navigating SUPER type structures with non-delimited attribute names is case sensitive. When you set
the value to `false`, navigating SUPER type structures with non-delimited attribute names is not case sensitive.

When you enclose an attribute name in double quotation marks and set `enable_case_sensitive_identifier`
to `true`, case is always preserved, regardless of the setting of the `enable_case_sensitive_super_attribute` configuration option.

`enable_case_sensitive_super_attribute` only applies to columns with the SUPER data type. For all other columns, consider using
`enable_case_sensitive_identifier` instead.

For more information on navigating uppercase and mixed-case JSON fields, see
[Accessing JSON fields with uppercase and mixed-case field
names or attributes](super-configurations.md#upper-mixed-case "super-configurations.md#upper-mixed-case").

## Examples

The following example shows the results of selecting SUPER
values with `enable_case_sensitive_super_attribute`
enabled and with it disabled.

```
--Create a table with a SUPER column.
CREATE TABLE tbl (col SUPER);

--Insert values.
INSERT INTO tbl VALUES (json_parse('{
 "A": "HELLO", "a": "123"
}'));

SET enable_case_sensitive_super_attribute TO ON;

SELECT col.A FROM tbl;
  a
-----
 "HELLO"
(1 row)

SELECT col.a FROM tbl;
  a
-----
 "123"
(1 row)

SET enable_case_sensitive_super_attribute TO OFF;

SELECT col.A FROM tbl;
  a
-----
 "123"
(1 row)

SELECT col.a FROM tbl;
  a
-----
 "123"
(1 row)
```

## Usage Notes

- Views and materialized views follow the value of `enable_case_sensitive_super_attribute`
  at the time of their creation. Late-binding views, stored procedures, and user-defined functions
  follow the value of `enable_case_sensitive_super_attribute` at the time of querying.
- If you're using autorefresh for materialized views, we
  recommend setting the `enable_case_sensitive_identifier value` in your cluster
  or workgroup's parameter group. This ensures that `enable_case_sensitive_identifier`
  stays constant when your materialized views are refreshed. For information on autorefresh
  for materialized views, see [Refreshing a materialized view](materialized-view-refresh.md "materialized-view-refresh.md").
  For information on setting configuration values in parameter groups,
  see
  [Amazon Redshift parameter groups](../mgmt/working-with-parameter-groups.md "../mgmt/working-with-parameter-groups.md") in the
  _Amazon Redshift Management Guide_.
- The column name in statement results is always downcased, regardless of the value of
  `enable_case_sensitive_super_attribute`. To make the column name
  case sensitive as well, enable `enable_case_sensitive_identifier`.
- We recommend that regular users querying tables with row-level security policies attached
  have the default `enable_case_sensitive_identifier` setting. For more information, see
  For information on row-level security, see
  [Row-level security](t_rls.md "t_rls.md").
