Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# SVV_MASKING_POLICY

Use SVV_MASKING_POLICY to view all masking policies created on the cluster.

Only superusers and users with the [`sys:secadmin`](r_roles-default.md "r_roles-default.md") role can view SVV_MASKING_POLICY. Regular users will see 0 rows.

## Table columns

| Column name          | Data type | Description                                                            |
| -------------------- | --------- | ---------------------------------------------------------------------- |
| policy_database      | text      | The name of the database in which the masking policy was created.      |
| policy_name          | text      | The name of the masking policy.                                        |
| input_columns        | text      | The attributes provided in the WITH clause of CREATE POLICY statement. |
| policy_expression    | text      | The masking expression used in the policy.                             |
| policy_modified_by   | text      | The name of the user who last modified the policy.                     |
| policy_modified_time | timestamp | The timestamp of when the policy was created or last modified.         |
