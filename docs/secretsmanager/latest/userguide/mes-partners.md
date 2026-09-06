

# Managed external secrets Partners
<a name="mes-partners"></a>

Secrets Manager natively integrates with third party applications to rotate secrets held by the partner. Each partner defines the metadata and secret value fields required to rotate the secrets. 

 The secret value contains fields that are required for connecting with your third party client and are stored during the [CreateSecret](https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_CreateSecret.html) call. The rotation metadata holds the fields that are used to update the secret during rotation and are used in the [RotateSecret](https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_RotateSecret.html) call. These fields will be defined by the integration partner to allow managed rotation flows. 

 For rotation to function properly, you must provide Secrets Manager with specific permissions to manage the secret lifecycle. For more information see [Security and Permissions](mes-security.md)

The following topics include a description of each of the metadata fields required to rotate the secret as well as a description of each of the fields required in the Secrets Manager secret to rotate.


**Topics**  

| Integration Partner | Secret type | 
| --- | --- | 
| BigID | [BigIDClientSecret](mes-partner-BigId.md) | 
| Cisco | [CiscoSecurityPlatformApiKey](mes-partner-CiscoSecurityPlatformApiKey.md) | 
| Confluent Cloud | [ConfluentCloudApiKey](mes-partner-ConfluentCloudApiKey.md) | 
| Datadog | [DatadogApiKey](mes-partner-DatadogApiKey.md) | 
| Datadog | [DatadogApplicationKey](mes-partner-DatadogApplicationKey.md) | 
| Datadog | [DatadogAdminKey](mes-partner-DatadogAdminKey.md) | 
| GitLab | [GitLabAccessToken](mes-partner-GitLabAccessToken.md) | 
| Jenkins | [JenkinsApiToken](mes-partner-JenkinsApiToken.md) | 
| MongoDB Atlas | [MongoDBAtlasServiceAccount](mes-partner-MongoDBAtlasServiceAccount.md) | 
| MongoDB Atlas | [MongoDBAtlasDatabaseUser](mes-partner-MongoDBAtlasDatabaseUser.md) | 
| Netskope | [NetskopeApiToken](mes-partner-NetskopeApiToken.md) | 
| Paddle | [PaddleApiKey](mes-partner-PaddleApiKey.md) | 
| Salesforce | [SalesforceClientSecret](mes-partner-salesforce.md) | 
| Snowflake | [SnowflakeKeyPairAuthentication](mes-partner-Snowflake.md) | 
| Snowflake | [SnowflakePat](mes-partner-SnowflakePat.md) | 
| SonarQube | [SonarQubeToken](mes-partner-SonarQubeToken.md) | 