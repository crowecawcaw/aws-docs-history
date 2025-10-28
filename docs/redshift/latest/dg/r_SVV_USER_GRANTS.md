Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# SVV_USER_GRANTS

Use SVV_USER_GRANTS to view the list of users that are explicitly granted roles in the cluster.

SVV_USER_GRANTS is visible to the following users:

- Superusers
- Users with the ACCESS SYSTEM TABLE permission
  Other users can
  only see roles that are explicitly granted to them.

## Table columns

| Column name  | Data type | Description                                                                          |
| ------------ | --------- | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | --------- | ------------------------------------------------------------- | ----- | ------------- | ----- | --------------- | ----- | ------------- | ----- | --------- |
| user_id      | integer   | The user ID for the user.                                                            |
| user_name    | text      | The name of the user.                                                                |
| role_id      | integer   | The role ID for the granted role.                                                    |
| role_name    | text      | The role name for the granted role.                                                  |
| admin_option | boolean   | A value that indicates whether the user can grant the role to other users and roles. | ## Sample queries The following queries grant roles to users and show the list of users that are explicitly granted roles. ``` GRANT ROLE role1 TO reguser; GRANT ROLE role2 TO reguser; GRANT ROLE role1 TO superuser; GRANT ROLE role2 TO superuser; SELECT user_name,role_name,admin_option FROM svv_user_grants; user_name | role_name | admin_option -----------+-----------+-------------- superuser | role1 | False reguser | role1 | False superuser | role2 | False reguser | role2 | False ``` |
