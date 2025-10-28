# Default credentials

You can use the default credentials that you configure on your client system to
connect to Amazon Athena by setting the following connection parameters. For information
about using default credentials, see [Using the
Default Credential Provider Chain](../../../sdk-for-java/v1/developer-guide/credentials.md#credentials-default "../../../sdk-for-java/v1/developer-guide/credentials.md#credentials-default") in the
_AWS SDK for Java Developer Guide_.

## Credentials provider

The credentials provider that will be used to authenticate requests to AWS. Set
the value of this parameter to `DefaultChain`.

| Parameter name      | Alias                                      | Parameter type | Default value | Value to use   |
| ------------------- | ------------------------------------------ | -------------- | ------------- | -------------- |
| CredentialsProvider | _AWSCredentialsProviderClass (deprecated)_ | Required       | none          | `DefaultChain` |
