

# MongoDB Atlas Service Account Credentials
<a name="mes-partner-MongoDBAtlasServiceAccount"></a>

## Secret Value Fields
<a name="w2aac27c11c31b3"></a>

The following are the fields that must be contained in the Secrets Manager secret:

```
{
  "clientId": "{{service account OAuth client ID}}",
  "clientSecret": "{{service account OAuth client secret}}",
  "orgId": "{{Atlas Organization ID}}"
}
```

clientId  
The MongoDB Atlas service account OAuth client ID. This must start with `mdb_sa_id_` followed by a 24-character hexadecimal string.

clientSecret  
The MongoDB Atlas service account OAuth client secret used for authentication.

orgId  
The 24-character hexadecimal Atlas Organization ID. You can find this in your Atlas Organization Settings.

## Secret Metadata Fields
<a name="w2aac27c11c31b5"></a>

The following are the metadata fields for MongoDB Atlas Service Account:

```
{
  "adminSecretArn": "arn:aws:secretsmanager:us-east-1:111122223333:secret:{{MongoDBAtlasServiceAccount}}",
  "apiVersion": "{{2025-03-12}}"
}
```

adminSecretArn  
(Optional) The Amazon Resource Name (ARN) for the secret that contains the administrative service account OAuth credentials used to rotate this service account secret. The admin secret should contain a `clientId` and `clientSecret` value within the secret structure. If omitted, the service account will use its own credentials for self-rotation.

apiVersion  
(Optional) The Atlas Admin API version date in `yyyy-mm-dd` format. This value is used in the `Accept` header as `application/vnd.atlas.{apiVersion}+json`. Defaults to `2025-03-12` if not specified.

## Usage Flow
<a name="w2aac27c11c31b7"></a>

The rotation supports two authentication modes. In self-rotation mode (default), the service account uses its own credentials to create and delete its secrets. This requires the service account to have permissions to manage its own secrets. In admin-assisted rotation mode, a separate admin service account credential stored in another secret is used. This is required when the service account lacks self-management permissions.

You can create your secret using the [CreateSecret](https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_CreateSecret.html) call with the secret value containing the fields mentioned above and secret type as MongoDBAtlasServiceAccount. The rotation configurations can be set using a [RotateSecret](https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_RotateSecret.html) call. If you opt for self-rotation, you can omit the optional `adminSecretArn` field. You must provide a role ARN in the [RotateSecret](https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_RotateSecret.html) call which grants the service the required permissions to rotate the secret. For an example of a permissions policy, see [Security and Permissions](mes-security.md).

For customers opting to rotate their secrets using a separate set of credentials (stored in an Admin Secret), create the Admin Secret in AWS Secrets Manager containing the admin service account's `clientId` and `clientSecret`. You must provide the ARN of this Admin Secret in the rotation metadata in a [RotateSecret](https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_RotateSecret.html) call for your service account secret.

During rotation, the driver creates a new secret for the service account via the Atlas Admin API, verifies the new secret by generating an OAuth token, updates the secret with new credentials, and deletes the old secret.