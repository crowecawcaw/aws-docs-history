Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026.
We will start enforcing it in phases. For more information on the details of Python end of life
and migration options, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") that was published on June 30, 2025.

# SVV\_MASKING\_POLICY

Use SVV\_MASKING\_POLICY to view all masking policies created on the cluster.

Only superusers and users with the [`sys:secadmin`](r_roles-default.md "r_roles-default.md") role can view SVV\_MASKING\_POLICY. Regular users will see 0 rows.

## Table columns

| Column name            | Data type | Description                                                            |
| ---------------------- | --------- | ---------------------------------------------------------------------- |
| policy\_database       | text      | The name of the database in which the masking policy was created.      |
| policy\_name           | text      | The name of the masking policy.                                        |
| input\_columns         | text      | The attributes provided in the WITH clause of CREATE POLICY statement. |
| policy\_expression     | text      | The masking expression used in the policy.                             |
| policy\_modified\_by   | text      | The name of the user who last modified the policy.                     |
| policy\_modified\_time | timestamp | The timestamp of when the policy was created or last modified.         |
