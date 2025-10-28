Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# SVV_LANGUAGE_PRIVILEGES

Use SVV_LANGUAGE_PRIVILEGES to view the language permissions that are explicitly
granted to users, roles, and groups in the current database.

SVV_LANGUAGE_PRIVILEGES is visible to the following users:

- Superusers
- Users with the ACCESS SYSTEM TABLE permission
  Other users can
  only see identities they have access to or own.

## Table columns

| Column name    | Data type | Description                                                                                                                                         |
| -------------- | --------- | --------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------- | ------------- | ------------- | ---------------------------------------------------------------------------------------------------- | ----- | ------- | ---- | ------------ | ----- | ----- | ---- | --------------- | ----- | ------- | ---- | --------- |
| language_name  | text      | The name of the language.                                                                                                                           |
| privilege_type | text      | The type of the permission. Possible value is USAGE.                                                                                                |
| identity_id    | integer   | The ID of the identity. Possible values are user ID, role ID, or group ID.                                                                          |
| identity_name  | text      | The name of the identity.                                                                                                                           |
| identity_type  | text      | The type of the identity. Possible values are user, role, group, or public.                                                                         |
| admin_option   | boolean   | A value that indicates whether the user can grant the permission to other users and roles. It is always false for the role and group identity type. | ## Sample query The following example displays the result of the SVV_LANGUAGE_PRIVILEGES. ``` SELECT language_name,privilege_type,identity_name,identity_type,admin_option FROM svv_language_privileges WHERE identity_name IN ('role1', 'reguser'); language_name | privilege_type | identity_name | identity_type | admin_option ---------------+----------------+---------------+---------------+--------------- exfunc | USAGE | reguser | user | False exfunc | USAGE | role1 | role | False plpythonu | USAGE | reguser | user | False ``` |
