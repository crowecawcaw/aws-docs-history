Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# SVV_ML_MODEL_PRIVILEGES

Use SVV_ML_MODEL_PRIVILEGES to view the machine learning model permissions that are
explicitly granted to users, roles, and groups in the cluster.

SVV_ML_MODEL_PRIVILEGES is visible to the following users:

- Superusers
- Users with the ACCESS SYSTEM TABLE permission
  Other users can
  only see identities they have access to or own.

## Table columns

| Column name    | Data type | Description                                                                                                                                         |
| -------------- | --------- | --------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------- | ------------- | -------------- | ------------- | ------------- | ---------------------------------------------------------------------------------------------------------------------------------- | ---------- | --- | ------- | ------- | ---- | ------------ | ---------- | --- | ------- | ----- | ---- | --------- |
| namespace_name | text      | The name of the namespace where a specified machine learning model exists.                                                                          |
| model_name     | text      | The name of the machine learning model.                                                                                                             |
| model_version  | integer   | The version number of the model.                                                                                                                    |
| privilege_type | text      | The type of the permission. Possible value is EXECUTE.                                                                                              |
| identity_id    | integer   | The ID of the identity. Possible values are user ID, role ID, or group ID.                                                                          |
| identity_name  | text      | The name of the identity.                                                                                                                           |
| identity_type  | text      | The type of the identity. Possible values are user, role, group, or public.                                                                         |
| admin_option   | boolean   | A value that indicates whether the user can grant the permission to other users and roles. It is always false for the role and group identity type. | ## Sample query The following example displays the result of the SVV_ML_MODEL_PRIVILEGES. ``` SELECT namespace_name,model_name,model_version,privilege_type,identity_name,identity_type,admin_option FROM svv_ml_model_privileges WHERE model_name = 'test_model'; namespace_name | model_name | model_version | privilege_type | identity_name | identity_type | admin_option ----------------+------------+---------------+----------------+----------------+---------------+-------------- public | test_model | 1   | EXECUTE | reguser | user | False public | test_model | 1   | EXECUTE | role1 | role | False ``` |
