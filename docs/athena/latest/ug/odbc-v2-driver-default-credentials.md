# Default credentials

You can use the default credentials that you configure on your client system to
connect to Amazon Athena. For information about using default credentials, see [Using the
Default Credential Provider Chain](../../../sdk-for-java/v1/developer-guide/credentials.md#credentials-default "../../../sdk-for-java/v1/developer-guide/credentials.md#credentials-default") in the _AWS SDK for Java Developer Guide_.

## Authentication type

| **Connection string name** | **Parameter type** | **Default value** | **Connection string example**             |
| -------------------------- | ------------------ | ----------------- | ----------------------------------------- |
| AuthenticationType         | Required           | `IAM Credentials` | `AuthenticationType=Default Credentials;` |
