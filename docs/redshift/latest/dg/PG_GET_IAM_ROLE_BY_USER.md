Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026.
We will start enforcing it in phases. For more information on the details of Python end of life
and migration options, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") that was published on June 30, 2025.

# PG\_GET\_IAM\_ROLE\_BY\_USER

Returns all IAM roles and command privileges granted to a user.

## Syntax

```
pg_get_iam_role_by_user('*name*')
```

## Arguments

_name_

The name of the user for which to return IAM roles.

## Return type

VARCHAR

## Usage notes

The PG\_GET\_IAM\_ROLE\_BY\_USER function returns one row for each set of roles and command privileges. The row contains a comma-separated list with the user name, IAM role, and command.

A value of `default` in the result indicates that the user can specify any available role to perform the displayed command.

You must be a superuser to use this function.

## Example

The following example indicates that user `reg_user1` can specify any
available IAM role to perform COPY operations. The user can also specify the
`Redshift-S3-Write` role for UNLOAD operations.

```
select pg_get_iam_role_by_user('reg_user1');
```

```
                             pg_get_iam_role_by_user
---------------------------------------------------------------------------------
 (reg_user1,default,COPY)
 (reg_user1,arn:aws:iam::123456789012:role/Redshift-S3-Write,COPY|UNLOAD)
```

The following example of the PG\_GET\_IAM\_ROLE\_BY\_USER function formats the result as a table.

```
select username, iam_role, cmd FROM pg_get_iam_role_by_user('reg_user1') res_iam_role(username text, iam_role text, cmd text);

```

```
 username  |                    iam_role                     | cmd
-----------+-------------------------------------------------+------
 reg_user1 | default                                         | None
 reg_user1 | arn:aws:iam::123456789012:role/Redshift-S3-Read | COPY
```
