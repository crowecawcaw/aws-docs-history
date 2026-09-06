

# IAM credentials
<a name="odbc-v2-driver-iam-credentials"></a>

You can use your IAM credentials to connect to Amazon Athena with the ODBC driver using the connection string parameters described in this section.

## Authentication type
<a name="odbc-v2-driver-iam-credentials-authentication-type"></a>



| **Connection string name** | **Parameter type** | **Default value** | **Connection string example** | 
| --- | --- | --- | --- | 
| AuthenticationType | Required | IAM Credentials | AuthenticationType=IAM Credentials; | 

## User ID
<a name="odbc-v2-driver-iam-credentials-user-id"></a>

Your AWS Access Key ID. For more information about access keys, see [AWS security credentials](https://docs.aws.amazon.com/IAM/latest/UserGuide/security-creds.html)in the *IAM User Guide*.



| **Connection string name** | **Parameter type** | **Default value** | **Connection string example** | 
| --- | --- | --- | --- | 
| UID | Required | none | UID=AKIAIOSFODNN7EXAMPLE; | 

## Password
<a name="odbc-v2-driver-iam-credentials-password"></a>

Your AWS secret key id. For more information about access keys, see [AWS security credentials](https://docs.aws.amazon.com/IAM/latest/UserGuide/security-creds.html)in the *IAM User Guide*.



| **Connection string name** | **Parameter type** | **Default value** | **Connection string example** | 
| --- | --- | --- | --- | 
| PWD | Required | none | PWD=wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKE; | 

## Session token
<a name="odbc-v2-driver-iam-credentials-session-token"></a>

If you use temporary AWS credentials, you must specify a session token. For information about temporary credentials, see [Temporary security credentials in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp.html) in the *IAM User Guide*.



| **Connection string name** | **Parameter type** | **Default value** | **Connection string example** | 
| --- | --- | --- | --- | 
| SessionToken | Optional | none | SessionToken=AQoDYXdzEJr...<remainder of session token>; | 