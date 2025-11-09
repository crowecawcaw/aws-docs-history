# Custom credentials

You can use this authentication type to provide your own credentials by using a Java
class that implements the [AwsCredentialsProvider](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/auth/credentials/AwsCredentialsProvider.html "https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/auth/credentials/AwsCredentialsProvider.html") interface.

## Credentials

provider

The credentials provider that will be used to authenticate requests to AWS. Set
the value of this parameter to the fully qualified class name of the custom class
that implements the [AwsCredentialsProvider](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/auth/credentials/AwsCredentialsProvider.html "https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/auth/credentials/AwsCredentialsProvider.html") interface. At runtime, that class must be on the
Java class path of the application that uses the JDBC driver.

| Parameter name      | Alias                                         | Parameter type | Default value | Value to use                                                                               |
| ------------------- | --------------------------------------------- | -------------- | ------------- | ------------------------------------------------------------------------------------------ |
| CredentialsProvider | _AWSCredentialsProviderClass<br>(deprecated)_ | Required       | none          | The fully qualified class name of the custom implementation of<br>`AwsCredentialsProvider` |

## Credentials provider

arguments

A comma-separated list of string arguments for the custom credentials provider
constructor.

| Parameter name               | Alias                                        | Parameter type | Default value |
| ---------------------------- | -------------------------------------------- | -------------- | ------------- |
| CredentialsProviderArguments | AwsCredentialsProviderArguments (deprecated) | Optional       | none          |
