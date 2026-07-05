Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026.
We will start enforcing it in phases. For more information on the details of Python end of life
and migration options, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") that was published on June 30, 2025.

# SVV\_IAM\_PRIVILEGES

Use SVV\_IAM\_PRIVILEGES to view explicitly granted IAM privileges on users, roles and groups.

SVV\_IAM\_PRIVILEGES is visible to the following users:

- Superusers
- Users with the ACCESS SYSTEM TABLE permission
  Other users can
  only see entries they have access to.

## Table columns

| Column name    | Data type | Description                                                                            |
| -------------- | --------- | -------------------------------------------------------------------------------------- |
| iam\_arn       | text      | Name of the namespace.                                                                 |
| command\_type  | text      | Privilege types. Possible values are COPY, UNLOAD, CREATE MODEL, or EXTERNAL FUNCTION. |
| identity\_id   | integer   | Identity ID. Possible values are user ID, role ID, or group ID.                        |
| identity\_name | text      | Identity name.                                                                         |
| identity\_type | text      | Identity type. Possible values are user, role, group, or public.                       |

## Sample queries

The following example shows the results of SVV\_IAM\_PRIVILEGES.

```

SELECT * from SVV_IAM_PRIVILEGES ORDER BY IDENTITY_ID;
       iam_arn        | command_type | identity_id | identity_name | identity_type
----------------------+--------------+-------------+---------------+---------------
 default-aws-iam-role | COPY         |           0 | public        | public
 default-aws-iam-role | UNLOAD       |           0 | public        | public
 default-aws-iam-role | CREATE MODEL |           0 | public        | public
 default-aws-iam-role | EXFUNC       |           0 | public        | public
 default-aws-iam-role | COPY         |         106 | u1            | user
 default-aws-iam-role | UNLOAD       |         106 | u1            | user
 default-aws-iam-role | CREATE MODEL |         106 | u1            | user
 default-aws-iam-role | EXFUNC       |         106 | u1            | user
 default-aws-iam-role | COPY         |      118413 | r1            | role
 default-aws-iam-role | UNLOAD       |      118413 | r1            | role
 default-aws-iam-role | CREATE MODEL |      118413 | r1            | role
 default-aws-iam-role | EXFUNC       |      118413 | r1            | role
(12 rows)
```
