Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# SVV_ROLE_GRANTS

Use SVV_ROLE_GRANTS to view a list of roles that are explicitly granted roles in the cluster.

SVV_ROLE_GRANTS is visible to the following users:

- Superusers
- Users with the ACCESS SYSTEM TABLE permission
  Other users can
  only see identities they have access to or own.

## Table columns

| Column name       | Data type | Description                    |
| ----------------- | --------- | ------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------- | ----------- | ------------------ |
| role_id           | integer   | The ID of the role.            |
| role_name         | text      | The name of the role.          |
| granted_role_id   | integer   | The ID for the granted role.   |
| granted_role_name | text      | The name for the granted role. | ## Sample query The following example returns the output of SVV_ROLE_GRANTS. ``` GRANT ROLE role1 TO ROLE role2; GRANT ROLE role2 TO ROLE role3; SELECT role_name, granted_role_name FROM svv_role_grants; role_name | granted_role_name -----------+-------------------- role2 | role1 role3 | role2 (2 rows) ``` |
