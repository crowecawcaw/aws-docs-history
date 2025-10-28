Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# PG_GET_GRANTEE_BY_IAM_ROLE

Returns all users and groups granted a specified IAM role.

## Syntax

```
pg_get_grantee_by_iam_role('*iam\_role\_arn*')
```

## Arguments

_iam_role_arn_

The IAM role for which to return the users and groups that have been granted this role.

## Return type

VARCHAR

## Usage notes

The PG_GET_GRANTEE_BY_IAM_ROLE function returns one row for each user or group.
Each row contains the grantee name, grantee type, and granted privilege. The possible
values for the grantee type are `p` for public, `u` for user,
and `g` for group.

You must be a superuser to use this function.

## Example

The following example indicates that the IAM role `Redshift-S3-Write`
is granted to `group1` and `reg_user1`. Users in
`group_1` can specify the role only for COPY operations, and user
`reg_user1` can specify the role only to perform UNLOAD
operations.

```
select pg_get_grantee_by_iam_role('arn:aws:iam::123456789012:role/Redshift-S3-Write');

```

```
  pg_get_grantee_by_iam_role
-----------------------------
 (group_1,g,COPY)
 (reg_user1,u,UNLOAD)
```

The following example of the PG_GET_GRANTEE_BY_IAM_ROLE function formats the result as a table.

```
select grantee, grantee_type, cmd_type FROM pg_get_grantee_by_iam_role('arn:aws:iam::123456789012:role/Redshift-S3-Write') res_grantee(grantee text, grantee_type text, cmd_type text) ORDER BY 1,2,3;

```

```
  grantee  | grantee_type | cmd_type
-----------+--------------+----------
 group_1   | g            | COPY
 reg_user1 | u            | UNLOAD
```
