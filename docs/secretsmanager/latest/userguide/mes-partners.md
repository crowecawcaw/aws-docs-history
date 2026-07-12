# Managed external secrets Partners

Secrets Manager natively integrates with third party applications to rotate secrets
held by the partner. Each partner defines the metadata and secret value fields required
to rotate the secrets.

The secret value contains fields that are required for connecting with your third party client and are
stored during the [CreateSecret](../apireference/API_CreateSecret.md "../apireference/API_CreateSecret.md") call.
The rotation metadata holds the fields that are used to update the
secret during rotation and are used in the [RotateSecret](../apireference/API_RotateSecret.md "../apireference/API_RotateSecret.md") call.
These fields will be defined by the integration partner to allow managed rotation flows.

For rotation to function properly, you must provide Secrets Manager with specific permissions to manage
the secret lifecycle. For more information see [Security and Permissions](mes-security.md "mes-security.md")

The following topics include a description of each of the metadata fields required to
rotate the secret as well as a description of each of the fields required in the Secrets Manager
secret to rotate.

Topics| Integration Partner | Secret type |
| --- | --- |
| BigID | [BigIDClientSecret](mes-partner-BigId.md "mes-partner-BigId.md") |
| Confluent Cloud | [ConfluentCloudApiKey](mes-partner-ConfluentCloudApiKey.md "mes-partner-ConfluentCloudApiKey.md") |
| Datadog | [DatadogApiKey](mes-partner-DatadogApiKey.md "mes-partner-DatadogApiKey.md") |
| Datadog | [DatadogApplicationKey](mes-partner-DatadogApplicationKey.md "mes-partner-DatadogApplicationKey.md") |
| Datadog | [DatadogAdminKey](mes-partner-DatadogAdminKey.md "mes-partner-DatadogAdminKey.md") |
| GitLab | [GitLabAccessToken](mes-partner-GitLabAccessToken.md "mes-partner-GitLabAccessToken.md") |
| MongoDB Atlas | [MongoDBAtlasServiceAccount](mes-partner-MongoDBAtlasServiceAccount.md "mes-partner-MongoDBAtlasServiceAccount.md") |
| MongoDB Atlas | [MongoDBAtlasDatabaseUser](mes-partner-MongoDBAtlasDatabaseUser.md "mes-partner-MongoDBAtlasDatabaseUser.md") |
| Paddle | [PaddleApiKey](mes-partner-PaddleApiKey.md "mes-partner-PaddleApiKey.md") |
| Salesforce | [SalesforceClientSecret](mes-partner-salesforce.md "mes-partner-salesforce.md") |
| Snowflake | [SnowflakeKeyPairAuthentication](mes-partner-Snowflake.md "mes-partner-Snowflake.md") |
| Snowflake | [SnowflakePat](mes-partner-SnowflakePat.md "mes-partner-SnowflakePat.md") |
