

# IAM credentials
<a name="jdbc-v3-driver-iam-credentials"></a>

You can use your IAM credentials with the JDBC driver to connect to Amazon Athena by setting the following connection parameters.

## User
<a name="jdbc-v3-driver-user"></a>

Your AWS access key ID. For information about access keys, see [AWS security credentials](https://docs.aws.amazon.com/IAM/latest/UserGuide/security-creds.html) in the *IAM User Guide*.



| Parameter name | Alias | Parameter type | Default value | 
| --- | --- | --- | --- | 
| User | AccessKeyId | Required | none | 

## Password
<a name="jdbc-v3-driver-password"></a>

Your AWS secret key ID. For information about access keys, see [AWS security credentials](https://docs.aws.amazon.com/IAM/latest/UserGuide/security-creds.html) in the *IAM User Guide*.



| Parameter name | Alias | Parameter type | Default value | 
| --- | --- | --- | --- | 
| Password | SecretAccessKey | Optional | none | 

## Session token
<a name="jdbc-v3-driver-session-token"></a>

If you use temporary AWS credentials, you must specify a session token. For information about temporary credentials, see [Temporary security credentials in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp.html) in the *IAM User Guide*.



| Parameter name | Alias | Parameter type | Default value | 
| --- | --- | --- | --- | 
| SessionToken | none | Optional | none | 