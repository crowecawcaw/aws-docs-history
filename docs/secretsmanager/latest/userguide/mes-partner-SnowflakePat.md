

# Snowflake Programmatic Access Token
<a name="mes-partner-SnowflakePat"></a>

## Secret Value Fields
<a name="w2aac27c11c41b3"></a>

The following are the fields that must be contained in the Secrets Manager secret:

```
{
  "account": "{{Snowflake account identifier}}",
  "user": "{{Snowflake username}}",
  "privateKey": "{{PEM-encoded private key}}",
  "passphrase": "{{private key passphrase (optional)}}",
  "patTokenName": "{{PAT name}}",
  "patTokenValue": "{{PAT secret value}}"
}
```

account  
Your Snowflake account identifier (for example, `myorg-myaccount`). This is the portion before `.snowflakecomputing.com` in your Snowflake URL.

user  
The Snowflake username who owns the PAT. This user must have key-pair authentication configured.

privateKey  
PEM-encoded private key for key-pair authentication. This key is not rotated — it is used to authenticate the ROTATE PAT command (a PAT cannot rotate itself).

passphrase  
(Optional) Passphrase for an encrypted private key. Leave empty if the private key is unencrypted.

patTokenName  
The name of the programmatic access token to rotate. Must match the token name in Snowflake.

patTokenValue  
The programmatic access token secret value. This is the field that gets rotated.

## Secret Metadata Fields
<a name="w2aac27c11c41b5"></a>

The following are the metadata fields for Snowflake Programmatic Access Token:

```
{
  "daysToExpiry": "{{15}}",
  "expireOldTokenAfterHours": "{{24}}"
}
```

daysToExpiry  
(Optional) The PAT's DAYS\_TO\_EXPIRY value set at creation time (1–365). Default: 15. Must match the Snowflake setting. Used to validate that the rotation schedule is shorter than the token's TTL.

expireOldTokenAfterHours  
(Optional) Hours before the previous token expires after rotation (0–720). Default: 24. Set to 0 for immediate expiry of the old token.

## Usage Flow
<a name="w2aac27c11c41b7"></a>

This rotation uses a single-secret architecture. The secret contains both the key-pair credentials (for authenticating the rotation command) and the PAT value (the rotated credential).

You can create your secret using the [CreateSecret](https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_CreateSecret.html) call with the secret value containing the fields mentioned above and secret type as SnowflakePat. The rotation configurations can be set using a [RotateSecret](https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_RotateSecret.html) call. The rotation metadata field can be left empty to use default values. You must provide a role ARN in the [RotateSecret](https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_RotateSecret.html) call which grants the service the required permissions to rotate the secret. For an example of a permissions policy, see [Security and Permissions](mes-security.md).

During rotation, the driver connects to Snowflake via key-pair authentication and executes the `ALTER USER ... ROTATE PAT` command, which atomically generates a new token and expires the old one with the configured grace period. The new token is then verified by connecting with it as a password.