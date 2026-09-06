

# Instance profile
<a name="odbc-v2-driver-instance-profile"></a>

This authentication type is used on EC2 instances and is delivered through the Amazon EC2 metadata service.

## Authentication type
<a name="odbc-v2-driver-instance-profile-authentication-type"></a>



| **Connection string name** | **Parameter type** | **Default value** | **Connection string example** | 
| --- | --- | --- | --- | 
| AuthenticationType | Required | IAM Credentials | AuthenticationType=Instance Profile; | 