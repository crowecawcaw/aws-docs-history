Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# ALTER MASKING POLICY

Alters an existing dynamic data masking policy. For more information on dynamic data
masking, see [Dynamic data masking](t_ddm.md "t_ddm.md").

Superusers and users or roles that have the sys:secadmin role can alter a masking
policy.

## Syntax

```
ALTER MASKING POLICY *policy\_name*
   USING (*masking\_expression*);
```

## Parameters

_policy_name_

The name of the masking policy. This must be the name of a masking policy
that already exists in the database.

_masking_expression_

The SQL expression used to transform the target columns. It can be written
using data manipulation functions such as String manipulation functions, or in
conjunction with user-defined functions written in SQL, Python, or with
AWS Lambda.

The expression must match the original expression's input columns and data
types. For example, if the original masking policy's input columns were
`sample_1 FLOAT` and `sample_2 VARCHAR(10)`, you
wouldn't be able to alter the masking policy to take a third column, or make
the policy take a FLOAT and a BOOLEAN. If you use a constant as your masking
expression, you must explicitly cast it to a type that matches the input
type.

You must have the USAGE permission on any user-defined functions that you
use in the masking expression.
