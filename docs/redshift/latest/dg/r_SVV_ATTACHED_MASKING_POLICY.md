Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# SVV_ATTACHED_MASKING_POLICY

Use SVV_ATTACHED_MASKING_POLICY to view all the relations and roles/users with policies attached on the currently connected database.

Only superusers and users with the [`sys:secadmin`](r_roles-default.md "r_roles-default.md") role can view SVV_ATTACHED_MASKING_POLICY. Regular users will see 0 rows.

## Table columns

| Column name             | Data type | Description                                                                         |
| ----------------------- | --------- | ----------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| policy_name             | text      | The name of the masking policy attached to the table.                               |
| schema_name             | text      | The schema of the table to which the policy is attached.                            |
| table_name              | text      | The name of the table to which the policy is attached.                              |
| table_type              | text      | The type of the table to which the policy is attached.                              |
| grantor                 | text      | The name of the user that attached the policy.                                      |
| grantee                 | text      | The name of the user/role to whom the policy is attached.                           |
| grantee_type            | text      | The type of grantee. This can be _role_, _user_, or _public_.                       |
| priority                | int       | The priority of the attached policy.                                                |
| input_columns           | text      | The input column attributes of the attached policy.                                 |
| output_columns          | text      | The output column attributes of the attached policy.                                |
| is_masking_datashare_on | boolean   | Whether the table to which the policy is attached is DDM-protected over datashares. | ## Internal functions SVV_ATTACHED_MASKING_POLICY supports the following internal functions: ### mask_get_policy_for_role_on_column Get the highest priority policy that applies to a given column/role pair. #### Syntax `mask_get_policy_for_role_on_column (relschema, relname, colname, rolename);` #### Parameters _relschema_ The name of the schema the policy is in. _relname_ The name of the table the policy is in. _colname_ The name of the column the policy is attached to. _rolename_ The name of the role the policy is attached to. ### mask_get_policy_for_user_on_column Get the highest priority policy that applies to a given column/user pair. #### Syntax `mask_get_policy_for_user_on_column (relschema, relname, colname, username);` #### Parameters _relschema_ The name of the schema the policy is in. _relname_ The name of the table the policy is in. _colname_ The name of the column the policy is attached to. _rolename_ The name of the user the policy is attached to. |
