# MongoDB Atlas Database User

## Secret Value Fields

The following are the fields that must be contained in the Secrets Manager secret:

```
{
  "username": "`database username`",
  "password": "`database password`",
  "clusterUrl": "`cluster hostname`",
  "databaseName": "`authentication database`",
  "groupId": "`Atlas Project ID`"
}
```

username

The MongoDB database username (SCRAM-authenticated). This user must be configured in
MongoDB Atlas to accept SCRAM authentication.

password

The current password for the MongoDB Atlas database user.

clusterUrl

The MongoDB Atlas cluster hostname, for example `cluster0.abc123.mongodb.net`.
Do not include the `mongodb+srv://` prefix. This is used for verifying the new password during rotation.

databaseName

The authentication database where the user's credentials are stored. Typically
`admin` for SCRAM users or `$external` for X.509/LDAP.

groupId

The 24-character hexadecimal Atlas Project ID (also known as Group ID).
You can find this in your Atlas Project Settings.

## Secret Metadata Fields

The following are the metadata fields for MongoDB Atlas Database User:

```
{
  "adminSecretArn": "arn:aws:secretsmanager:us-east-1:111122223333:secret:`MongoDBAtlasServiceAccount`",
  "apiVersion": "`2025-03-12`"
}
```

adminSecretArn

The Amazon Resource Name (ARN) for the secret that contains the Atlas service account
OAuth credentials (type: MongoDBAtlasServiceAccount) with Project Database Access Admin permissions.
This admin secret is used to authenticate to the Atlas Admin API for password updates.

apiVersion

(Optional) The Atlas Admin API version date in `yyyy-mm-dd` format. This value is used
in the `Accept` header as `application/vnd.atlas.{apiVersion}+json`.
Defaults to `2025-03-12` if not specified.

## Usage Flow

This rotation type uses a two-secret architecture. An admin secret containing Atlas service account
OAuth credentials (`clientId`, `clientSecret`, `serviceAccountId`) is required
to authenticate to the Atlas Admin API. The admin secret should be of type MongoDBAtlasServiceAccount.

You can create your secret using the [CreateSecret](../apireference/API_CreateSecret.md "../apireference/API_CreateSecret.md") call with the secret
value containing the fields mentioned above and secret type as MongoDBAtlasDatabaseUser. The rotation configurations can be set using a
[RotateSecret](../apireference/API_RotateSecret.md "../apireference/API_RotateSecret.md") call.
You must provide the `adminSecretArn` in the rotation metadata. You must also provide a role ARN in the
[RotateSecret](../apireference/API_RotateSecret.md "../apireference/API_RotateSecret.md") call which grants the service the required permissions to
rotate the secret. For an example of a permissions policy, see [Security and Permissions](mes-security.md "mes-security.md").

Because the admin secret is of a different type (MongoDBAtlasServiceAccount) than the user secret
(MongoDBAtlasDatabaseUser), the default rotation role policy scoped by `secretsmanager:resource/Type`
will not grant access to the admin secret. You must explicitly provide the rotation role access to the admin
secret by adding a statement scoped to the MongoDBAtlasServiceAccount type or by specifying the admin secret ARN
directly in the role policy.

During rotation, the driver generates a new password, calls the Atlas Admin API to update the database
user's password, and verifies the new password by opening a real MongoDB connection to the cluster.
Note that there is a propagation delay of 5-10 seconds after the password update before the new password
is accepted by the cluster's authentication layer.
