

# Confluent Cloud API Key
<a name="mes-partner-ConfluentCloudApiKey"></a>

## Secret Value Fields
<a name="w2aac27c11c17b3"></a>

The following are the fields that must be contained in the Secrets Manager secret:

```
{
  "apiKey": "{{API Key ID}}",
  "apiSecret": "{{API Secret}}",
  "serviceAccountId": "{{Service Account ID}}",
  "resourceId": "{{Resource ID}}",
  "environmentId": "{{Environment ID}}"
}
```

apiKey  
The Confluent Cloud API Key ID used for authentication.

apiSecret  
The Confluent Cloud API Secret used for authentication.

serviceAccountId  
The ID of the Service Account principal that this API key represents, for example `sa-abc123`. The rotation logic uses this to create new keys for the correct principal.

resourceId  
(Optional) The resource ID for scoping the API key. This can be a Kafka cluster (`lkc-xxxxx`), ksqlDB cluster (`lksqlc-xxxxx`), Schema Registry (`lsrc-xxxxx`), Flink region (`aws.us-west-2`, `azure.centralus`, `gcp.us-central1`), or `Tableflow`. Omit this field for cloud resource management API keys.

environmentId  
(Optional) The Confluent Cloud Environment ID, for example `env-abcde`. Used when creating cluster-scoped keys.

## Secret Metadata Fields
<a name="w2aac27c11c17b5"></a>

The following are the metadata fields for Confluent Cloud API Key:

```
{
  "adminSecretArn": "arn:aws:secretsmanager:us-east-1:111122223333:secret:{{ConfluentCloudApiKey}}"
}
```

adminSecretArn  
(Optional) The Amazon Resource Name (ARN) for the secret that contains the administrative Confluent Cloud API Key credentials used to rotate this secret. The admin API key must have CloudClusterAdmin or OrganizationAdmin role to create and delete API keys for Service Accounts. If omitted, the user secret's own credentials are used for self-rotation.

## Usage Flow
<a name="w2aac27c11c17b7"></a>

The rotation supports two modes. In self-rotation mode (default), the user secret's own `apiKey`/`apiSecret` are used to authenticate Confluent API calls for key creation and deletion. The user secret's API key must have sufficient permissions to manage its own Service Account's keys. In admin-secret mode, a separate admin secret containing `apiKey`/`apiSecret` with admin permissions is used instead.

You can create your secret using the [CreateSecret](https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_CreateSecret.html) call with the secret value containing the fields mentioned above and secret type as ConfluentCloudApiKey. The rotation configurations can be set using a [RotateSecret](https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_RotateSecret.html) call. If you opt for self-rotation, you can omit the optional `adminSecretArn` field. You must provide a role ARN in the [RotateSecret](https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_RotateSecret.html) call which grants the service the required permissions to rotate the secret. For an example of a permissions policy, see [Security and Permissions](mes-security.md).

For customers opting to rotate their secrets using a separate set of admin credentials, create the Admin Secret in AWS Secrets Manager containing the admin `apiKey` and `apiSecret`. You must provide the ARN of this Admin Secret in the rotation metadata in a [RotateSecret](https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_RotateSecret.html) call for your API key secret.

During rotation, the driver creates a new API key for the target Service Account via the Confluent Cloud API, verifies the new key, updates the secret with new credentials, and deletes the old API key.