Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# CREATE MASKING POLICY

Creates a new dynamic data masking policy to obfuscate data of a given format. For more
information on dynamic data masking, see [Dynamic data masking](t_ddm.md "t_ddm.md").

Superusers and users or roles that have the sys:secadmin role can create a masking
policy.

## Syntax

```
CREATE MASKING POLICY
   { *policy\_name* | *database\_name*.*policy\_name* } [IF NOT EXISTS]
   WITH (input_columns)
   USING (masking_expression);


```

## Parameters

_policy_name_

The name of the masking policy. The masking policy can't have the same name
as another masking policy that already exists in the database.

database_name

The name of the database where the policy will be created. Policy can be created on the connected database or on Amazon Redshift Federated Permissions Catalog.

_input_columns_

A tuple of column names in the format (col1 type, col2 type ...).

Column names are used as the input for the masking expression. Column names
don't have to match the names of the columns being masked, but the input and
output data types must match.

_masking_expression_

The SQL expression used to transform the target columns. It can be written
using data manipulation functions such as String manipulation functions, or in
conjunction with user-defined functions written in SQL, Python, or with
AWS Lambda. You can include a tuple of column expressions for
masking policies that have multiple outputs. If you use a constant as your
masking expression, you must explicitly cast it to a type that matches the
input type.

You must have the USAGE permission on any user-defined functions that you
use in the masking expression.

For the usage of CREATE MASKING POLICY on Amazon Redshift Federated Permissions Catalog, see [Managing access control with Amazon Redshift federated permissions](federated-permissions-managing-access.md "federated-permissions-managing-access.md").
