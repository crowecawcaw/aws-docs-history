For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified
data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](timestream-for-influxdb.md "timestream-for-influxdb.md").

# How Amazon Timestream for InfluxDB uses secrets

Timestream for InfluxDB supports username and password authentication through the user interface, and token credentials for least privilege client and application connections. Timestream for InfluxDB users have `allAccess` permissions within their organization while tokens can have any set of permissions. Following best practices for secure API token management, users should be created to manage tokens for fine-grain access within an organization. Additional information on admin best practices with Timestream for InfluxDB can be found in the [Influxdata documentation](https://docs.influxdata.com/influxdb/v2/admin/tokens/create-token/ "https://docs.influxdata.com/influxdb/v2/admin/tokens/create-token/").

AWS Secrets Manager is a secret storage service that you can use to protect database credentials, API keys, and other secret information. Then in your code, you can replace hardcoded credentials with an API call to Secrets Manager. This helps ensure that the secret can't be compromised by someone examining your code, because the secret isn't there. For an overview of Secrets Manager, see [What is AWS Secrets Manager](../../../secretsmanager/latest/userguide/intro.md "../../../secretsmanager/latest/userguide/intro.md").

When you create a database instance, Timestream for InfluxDB automatically creates an admin secret for you to use with the multi-user rotation AWS Lambda function. In order to rotate Timestream for InfluxDB users and tokens, you must create a new secret by hand for each user or token you wish to rotate. Each secret can be configured to rotate on a schedule with the use of a Lambda function. The process to setup a new rotating secret consists of uploading the Lambda function code, configuring the Lambda role, defining the new secret, and configuring the secret rotation schedule.

## What's in the secret

When you store Timestream for InfluxDB user credentials in the secret, use the following format.

Single-user:

```
{
  "engine": "<required: must be set to 'timestream-influxdb'>",
  "username": "<required: username>",
  "password": "<required: password>",
  "dbIdentifier": "<required: DB identifier>"
}
```

When you create a Timestream for InfluxDB instance, an admin secret is automatically stored in Secrets Manager with credentials to be used with the multi-user Lambda function. Set the `adminSecretArn` to the `Authentication Properties Secret Manager ARN` value found on the DB instance summary page or to the ARN of an admin secret. To create a new admin secret you must already have the associated credentials and the credentials must have admin privileges.

When you store Timestream for InfluxDB token credentials in the secret, use the following format.

Multi-user:

```
{
  "engine": "<required: must be set to 'timestream-influxdb'>",
  "org": "<required: organization to associate token with>",
  "adminSecretArn": "<required: ARN of the admin secret>",
  "type": "<required: allAccess or operator or custom>",
  "dbIdentifier": "<required: DB identifier>",
  "token": "<required unless generating a new token: token being rotated>",
  "writeBuckets": "<optional: list of bucketIDs for custom type token, must be input within plaintext panel, for example ['id1','id2']>",
  "readBuckets": "<optional: list of bucketIDs for custom type token, must be input within plaintext panel, for example ['id1','id2']>",
  "permissions": "<optional: list of permissions for custom type token, must be input within plaintext panel, for example ['write-tasks','read-tasks']>"
}
```

When you store Timestream for InfluxDB admin credentials in the secret, use the following format:

Admin secret:

```
{
  "engine": "<required: must be set to 'timestream-influxdb'>",
  "username": "<required: username>",
  "password": "<required: password>",
  "dbIdentifier": "<required: DB identifier>",
  "organization": "<optional: initial organization>",
  "bucket": "<optional: initial bucket>"
}
```

To turn on automatic rotation for the secret, the secret must be in the correct JSON structure. See [Rotating the secret](#timestream-for-influx-security-db-secrets-rotation "#timestream-for-influx-security-db-secrets-rotation") for how to rotate Timestream for InfluxDB secrets.

## Modifying the secret

The credentials generated during the Timestream for InfluxDB instance creation process are stored in a Secrets Manager secret in your account. The [GetDbInstance](../../../ts-influxdb/latest/ts-influxdb-api/API_GetDbInstance.md "../../../ts-influxdb/latest/ts-influxdb-api/API_GetDbInstance.md") response object contains an `influxAuthParametersSecretArn` which holds the Amazon Resource Name (ARN) to such secret. The secret will only be populated after your Timestream for InfluxDB instance is available. This is a READONLY copy as any updates/modifications/deletions to this secret doesn't impact the created DB instance. If you delete this secret, the [API response](../../../ts-influxdb/latest/ts-influxdb-api/API_GetDbInstance.md#API_GetDbInstance_ResponseSyntax "../../../ts-influxdb/latest/ts-influxdb-api/API_GetDbInstance.md#API_GetDbInstance_ResponseSyntax") will still refer to the deleted secret ARN.

To create a new token in the Timestream for InfluxDB instance rather than store existing token credentials, you can create non-operator tokens by leaving the `token` value blank in the secret and using the multi-user rotation function with the `AUTHENTICATION_CREATION_ENABLED` Lambda environment variable set to `true`. If you create a new token, the permissions defined in the secret are assigned to the token and cannot be altered after the first successful rotation. For more information on rotating secrets, see [Rotating AWS Secrets Manager Secrets](../../../secretsmanager/latest/userguide/rotating-secrets.md "../../../secretsmanager/latest/userguide/rotating-secrets.md").

If a secret is deleted, the associated user or token in the Timestream for InfluxDB instance will not be deleted.

## Rotating the secret

You use the Timestream for InfluxDB single- and multi-user rotation Lambda functions to rotate Timestream for InfluxDB user and token credentials. Use the single-user Lambda function to rotate user credentials for your Timestream for InfluxDB instance, and use the multi-user Lambda function to rotate token credentials for your Timestream for InfluxDB instance.

Rotating users and tokens with the single- and multi-user Lambda functions is optional. Timestream for InfluxDB credentials never expire and any exposed credentials pose a risk for malicious actions against your DB instance. The advantage of rotating Timestream for InfluxDB credentials with Secrets Manager is an added security layer which limits the attack vector of exposed credentials to the window of time until the next rotation cycle. If no rotation mechanism is in place for your DB instance, any exposed credentials will be valid until they are manually deleted.

You can configure Secrets Manager to automatically rotate secrets for you according to a schedule that you specify. This enables you to replace long-term secrets with short-term ones, which helps to significantly reduce the risk of compromise. For more information on rotating secrets with Secrets Manager, see [Rotate AWS Secrets Manager Secrets](../../../secretsmanager/latest/userguide/rotating-secrets.md "../../../secretsmanager/latest/userguide/rotating-secrets.md").

### Rotating users

When you rotate users with the single-user Lambda function, a new random password will be assigned to the user after each rotation. For more information on how to enable automatic rotation, see [Set up automatic rotation for non-database AWS Secrets Manager secrets](../../../secretsmanager/latest/userguide/rotate-secrets_turn-on-for-other.md "../../../secretsmanager/latest/userguide/rotate-secrets_turn-on-for-other.md").

#### Rotating admin secrets

To rotate an admin secret you use the single-user rotation function. You need to add the `engine` and `dbIdentifier` values to the secret since those values are not automatically populated on DB initialization. See [What's in the secret](#timestream-for-influx-security-db-secrets-definition "#timestream-for-influx-security-db-secrets-definition") for the complete secret template.

To locate an admin secret for a Timestream for InfluxDB instance you use the admin secret ARN from the Timestream for InfluxDB instance summary page. It is recommended that you rotate all Timestream for InfluxDB admin secrets since admin users have elevated permissions for the Timestream for InfluxDB instance.

#### Lambda rotation function

You can rotate a Timestream for InfluxDB user with the single-user rotation function by using the [What's in the secret](#timestream-for-influx-security-db-secrets-definition "#timestream-for-influx-security-db-secrets-definition") with a new secret and adding the required fields for your Timestream for InfluxDB user. For more information on secret rotation Lambda functions, see [Rotation by Lambda function](../../../secretsmanager/latest/userguide/rotate-secrets_lambda.md "../../../secretsmanager/latest/userguide/rotate-secrets_lambda.md").

You can rotate a Timestream for InfluxDB user with the single-user rotation function by using the [What's in the secret](#timestream-for-influx-security-db-secrets-definition "#timestream-for-influx-security-db-secrets-definition") with a new secret and adding the required fields for your Timestream for InfluxDB user. For more information on secret rotation Lambda functions, see [Rotation by Lambda function](../../../secretsmanager/latest/userguide/rotate-secrets_lambda.md "../../../secretsmanager/latest/userguide/rotate-secrets_lambda.md").

The single user rotation function authenticates with the Timestream for InfluxDB DB instance using the credentials defined in the secret, then generates a new random password and sets the new password for the user. For more information on secret rotation Lambda functions, see [Rotation by Lambda function](../../../secretsmanager/latest/userguide/rotate-secrets_lambda.md "../../../secretsmanager/latest/userguide/rotate-secrets_lambda.md").

#### Lambda function execution role permissions

Use the following IAM policy as the role for the single-user Lambda function. The policy gives the Lambda function the required permissions to perform a secret rotation for Timestream for InfluxDB users.

Replace all items listed below in the IAM policy with values from your AWS account:

- **{rotating_secret_arn}** — The ARN for the secret being rotated can be found in the Secrets Manager secret details.
- **{db_instance_arn}** — The Timestream for InfluxDB instance ARN can be found on the Timestream for InfluxDB instance summary page.

### Rotating tokens

You can rotate a Timestream for InfluxDB token with the multi-user rotation function by using the [What's in the secret](#timestream-for-influx-security-db-secrets-definition "#timestream-for-influx-security-db-secrets-definition") with a new secret and adding the required fields for your Timestream for InfluxDB token. For more information on secret rotation Lambda functions, see [Rotation by Lambda function](../../../secretsmanager/latest/userguide/rotate-secrets_lambda.md "../../../secretsmanager/latest/userguide/rotate-secrets_lambda.md").

You can rotate a Timestream for InfluxDB token by using the Timestream for InfluxDB multi-user Lambda function. Set the `AUTHENTICATION_CREATION_ENABLED` environment variable to `true` in the Lambda configuration to enable token creation. To create a new token, use the [What's in the secret](#timestream-for-influx-security-db-secrets-definition "#timestream-for-influx-security-db-secrets-definition") for your secret value. Omit the `token` key-value pair in the new secret and set the `type` to `allAccess`, or define the specific permissions and set the type to `custom`. The rotation function will create a new token during the first rotation cycle. You can't change the token permissions by editing the secret after rotation and any subsequent rotations will use the permissions that are set in the DB instance.

#### Lambda rotation function

The multi-user rotation function rotates token credentials by creating a new permission identical token using the admin credentials in the admin secret. The Lambda function validates the token value in the secret before creating the replacement token, storing the new token value in the secret, and deleting the old token. If the Lambda function is creating a new token it will first validate that the `AUTHENTICATION_CREATION_ENABLED` environment variable is set to `true`, that there is no token value in the secret, and that the token type is not type operator.

#### Lambda function execution role permissions

Use the following IAM policy as the role for the multi-user Lambda function. The policy gives the Lambda function the required permissions to perform a secret rotation for Timestream for InfluxDB tokens.

Replace all items listed below in the IAM policy with values from your AWS account:

- **{rotating_secret_arn}** — The ARN for the secret being rotated can be found in the Secrets Manager secret details.
- **{authentication_properties_admin_secret_arn}** — The Timestream for InfluxDB admin secret ARN can be found on the Timestream for InfluxDB instance summary page.
- **{db_instance_arn}** — The Timestream for InfluxDB instance ARN can be found on the Timestream for InfluxDB instance summary page.
