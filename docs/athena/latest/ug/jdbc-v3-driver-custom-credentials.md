

# Custom credentials
<a name="jdbc-v3-driver-custom-credentials"></a>

You can use this authentication type to provide your own credentials by using a Java class that implements the [AwsCredentialsProvider](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/auth/credentials/AwsCredentialsProvider.html) interface.

## Credentials provider
<a name="jdbc-v3-driver-custom-credentials-credentials-provider"></a>

The credentials provider that will be used to authenticate requests to AWS. Set the value of this parameter to the fully qualified class name of the custom class that implements the [AwsCredentialsProvider](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/auth/credentials/AwsCredentialsProvider.html) interface. At runtime, that class must be on the Java class path of the application that uses the JDBC driver.



| Parameter name | Alias | Parameter type | Default value | Value to use | 
| --- | --- | --- | --- | --- | 
| CredentialsProvider | AWSCredentialsProviderClass (deprecated) | Required | none | The fully qualified class name of the custom implementation of AwsCredentialsProvider | 

## Credentials provider arguments
<a name="jdbc-v3-driver-credentials-provider-arguments"></a>

A comma-separated list of string arguments for the custom credentials provider constructor.



| Parameter name | Alias | Parameter type | Default value | 
| --- | --- | --- | --- | 
| CredentialsProviderArguments | AwsCredentialsProviderArguments (deprecated) | Optional | none | 