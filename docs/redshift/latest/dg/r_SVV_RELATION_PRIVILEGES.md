Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# SVV_RELATION_PRIVILEGES

Use SVV_RELATION_PRIVILEGES to view the relation (tables and views) permissions that
are explicitly granted to users, roles, and groups in the current database.

SVV_RELATION_PRIVILEGES is visible to the following users:

- Superusers
- Users with the SYSLOG ACCESS UNRESTRICTED permission
  Other users can only see identities they have access to or own. For more information about data visibility,
  see [Visibility of data in system tables and
  views](cm_chap_system-tables.md#c_visibility-of-data "cm_chap_system-tables.md#c_visibility-of-data").

## Table columns

| Column name    | Data type | Description                                                                                                                                         |
| -------------- | --------- | --------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------- | -------------- | ------------- | ------------- | --------------------------------------------------------------------------------------------------------------------- | ------ | ------ | ------- | ---- | ------------ | ------ | ------ | ----- | ---- | --------- |
| namespace_name | text      | The name of the namespace where a specified relation exists.                                                                                        |
| relation_name  | text      | The name of the relation.                                                                                                                           |
| privilege_type | text      | The type of the permission. Possible values are INSERT, SELECT, UPDATE, DELETE, REFERENCES, or DROP.                                                |
| identity_id    | integer   | The ID of the identity. Possible values are user ID, role ID, or group ID.                                                                          |
| identity_name  | text      | The name of the identity.                                                                                                                           |
| identity_type  | text      | The type of the identity. Possible values are user, role, group, or public.                                                                         |
| admin_option   | boolean   | A value that indicates whether the user can grant the permission to other users and roles. It is always false for the role and group identity type. | ## Sample query The following example displays the result of the SVV_RELATION_PRIVILEGES. ``` SELECT namespace_name,relation_name,privilege_type,identity_name,identity_type,admin_option FROM svv_relation_privileges WHERE relation_name = 'orders' AND privilege_type = 'SELECT'; namespace_name | relation_name | privilege_type | identity_name | identity_type | admin_option ----------------+---------------+----------------+----------------+---------------+-------------- public | orders | SELECT | reguser | user | False public | orders | SELECT | role1 | role | False ``` |
