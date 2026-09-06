

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# SVV\_ML\_MODEL\_PRIVILEGES
<a name="r_SVV_ML_MODEL_PRIVILEGES"></a>

Use SVV\_ML\_MODEL\_PRIVILEGES to view the machine learning model permissions that are explicitly granted to users, roles, and groups in the cluster.

SVV\_ML\_MODEL\_PRIVILEGES is visible to the following users:
+ Superusers
+ Users with the ACCESS SYSTEM TABLE permission

Other users can only see identities they have access to or own.

## Table columns
<a name="r_SVV_ML_MODEL_PRIVILEGES-table-columns"></a>


| Column name  | Data type  | Description | 
| --- | --- | --- | 
| namespace\_name | text | The name of the namespace where a specified machine learning model exists. | 
| model\_name | text | The name of the machine learning model. | 
| model\_version | integer | The version number of the model. | 
| privilege\_type | text | The type of the permission. Possible value is EXECUTE. | 
| identity\_id | integer | The ID of the identity. Possible values are user ID, role ID, or group ID. | 
| identity\_name | text | The name of the identity. | 
| identity\_type | text | The type of the identity. Possible values are user, role, group, or public. | 
| admin\_option | boolean | A value that indicates whether the user can grant the permission to other users and roles. It is always false for the role and group identity type. | 

## Sample query
<a name="r_SVV_ML_MODEL_PRIVILEGES-sample-query"></a>

The following example displays the result of the SVV\_ML\_MODEL\_PRIVILEGES.

```
SELECT namespace_name,model_name,model_version,privilege_type,identity_name,identity_type,admin_option FROM svv_ml_model_privileges
WHERE model_name = 'test_model';

 namespace_name | model_name | model_version | privilege_type |  identity_name | identity_type | admin_option
----------------+------------+---------------+----------------+----------------+---------------+--------------
      public    | test_model |       1       |    EXECUTE     |     reguser    |     user      |    False
      public    | test_model |       1       |    EXECUTE     |     role1      |     role      |    False
```