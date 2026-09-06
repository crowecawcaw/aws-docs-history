

# Default credentials
<a name="jdbc-v3-driver-default-credentials"></a>

You can use the default credentials that you configure on your client system to connect to Amazon Athena by setting the following connection parameters. For information about using default credentials, see [Using the Default Credential Provider Chain](https://docs.aws.amazon.com/sdk-for-java/v1/developer-guide/credentials.html#credentials-default) in the *AWS SDK for Java Developer Guide*.

## Credentials provider
<a name="jdbc-v3-driver-credentials-provider"></a>

The credentials provider that will be used to authenticate requests to AWS. Set the value of this parameter to `DefaultChain`.



| Parameter name | Alias | Parameter type | Default value | Value to use | 
| --- | --- | --- | --- | --- | 
| CredentialsProvider | AWSCredentialsProviderClass (deprecated) | Required | none | DefaultChain | 