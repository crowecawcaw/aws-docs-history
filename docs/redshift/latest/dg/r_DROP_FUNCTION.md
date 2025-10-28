Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# DROP FUNCTION

Removes a user-defined function (UDF) from the database. The function's signature,
or list of argument data types, must be specified because multiple functions can exist with
the same name but different signatures. You can't drop an Amazon Redshift built-in
function.

This command isn't reversible.

## Required privileges

Following are required privileges for DROP FUNCTION:

- Superuser
- Users with the DROP FUNCTION privilege
- Function owner

## Syntax

```
DROP FUNCTION *name*
( [*arg\_name*] *arg\_type*   [, ...] )
[ CASCADE | RESTRICT ]
```

## Parameters

_name_

The name of the function to be removed.

_arg_name_

The name of an input argument. DROP FUNCTION ignores argument names, because
only the argument data types are needed to determine the function's
identity.

_arg_type_

The data type of the input argument. You can supply a comma-separated list
with a maximum of 32 data types.

CASCADE

Keyword specifying to automatically drop objects that depend on the
function, such as views.

To create a view that isn't dependent on a function, include the WITH
NO SCHEMA BINDING clause in the view definition. For more information, see
[CREATE VIEW](r_CREATE_VIEW.md "r_CREATE_VIEW.md").

RESTRICT

Keyword specifying that if any objects depend on the function, do not drop
the function and return a message. This action is the default.

## Examples

The following example drops the function named `f_sqrt`:

```
drop function f_sqrt(int);
```

To remove a function that has dependencies, use the CASCADE option, as shown in the
following example:

```
drop function f_sqrt(int)cascade;
```
