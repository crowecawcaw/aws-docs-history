# Snowflake Key Pair

## Secret Value Fields

The following are the fields that must be contained in the Secrets Manager secret:

```
{
  "account": "`Your Account Identifier`",
  "user": "`Your user name`",
  "privateKey": "`Your private Key`",
  "publicKey": "`Your public Key`",
  "passphrase": "`Your Passphrase`"
}
```

user

The Snowflake username associated with this key-pair authentication. This user must be configured in Snowflake to accept key-pair authentication, and the public key must be assigned to this user's profile.

account

Your Snowflake account identifier used to establish the connection. This can be extracted from your Snowflake URL (the portion before .snowflakecomputing.com)

privateKey

The RSA private key in PEM format used for authentication. The BEGIN/END markers are optional.

publicKey

The public key counterpart in PEM format corresponding to the private key. The BEGIN/END markers are optional.

passphrase

(Optional) This field refers to the passphrase used to decrypt the encrypted private key.

## Secret Metadata Fields

The following are the metadata fields for Snowflake:

```
{
  "cryptographicAlgorithm": "`Your Cryptographic algorithm`",
  "encryptPrivateKey": "`True/False`"
}
```

cryptographicAlgorithm

(Optional) This refers to the algorithm used for key generation. You have a choice of 3 algorithms: `RS256|RS384|RS512` . This field is optional and the default algorithm chosen is RS256.

encryptPrivateKey

(Optional) This field can be used to choose if you want to encrypt your private key. It is false by default. The passphrase for encryption is randomly generated.

## Usage Flow

You can create your secret using the [CreateSecret](../apireference/API_CreateSecret.md "../apireference/API_CreateSecret.md")
call with the secret value containing the fields mentioned above and secret type as SnowflakeKeyPairAuthentication. The rotation configurations can be set using
a [RotateSecret](../apireference/API_RotateSecret.md "../apireference/API_RotateSecret.md") call.
You can optionally provide the secret metadata field(s) based on your requirement. You must also provide a
role ARN in the [RotateSecret](../apireference/API_RotateSecret.md "../apireference/API_RotateSecret.md") call which grants
the service the required permissions to rotate the secret. For example of a permissions policy see [Security and Permissions](mes-security.md "mes-security.md").
Note that the rotation metadata field can be left empty for this partner.
