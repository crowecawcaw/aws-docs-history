Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# GET_MOUNTED_ROLE

When invoked as part of a multi-dialect AWS Glue view, it allows returning the IAM role used to mount the Lake Formation schema or database. Multi-dialect means that the SQL is supported across
multiple query engines, such as Amazon EMR and Redshift. For more information about multi-dialect Glue views,
see [Creating views in the AWS Glue Data Catalog](data-catalog-views-overview.md "data-catalog-views-overview.md").

## Syntax

```
get_mounted_role()
```

## Return type

Returns a VARCHAR string or a null value.

## Usage notes

This function returns null for any use case outside of an
external Lake Formation view.

## Example

The following query returns the identity to mount the Lake Formation resource.

```
CREATE EXTERNAL PROTECTED VIEW external_schema.remote_view AS
SELECT mycol, get_mounted_role() FROM external_schema.remote_table;

mycol | get_mounted_role
----------------------------
1       arn:aws:iam::123456789012:role/salesrole
(1 row)
```
