

# Default credentials
<a name="odbc-v2-driver-default-credentials"></a>

You can use the default credentials that you configure on your client system to connect to Amazon Athena. For information about using default credentials, see [Using the Default Credential Provider Chain](https://docs.aws.amazon.com/sdk-for-java/v1/developer-guide/credentials.html#credentials-default) in the *AWS SDK for Java Developer Guide*.

## Authentication type
<a name="odbc-v2-driver-default-credentials-authentication"></a>



| **Connection string name** | **Parameter type** | **Default value** | **Connection string example** | 
| --- | --- | --- | --- | 
| AuthenticationType | Required | IAM Credentials | AuthenticationType=Default Credentials; | 