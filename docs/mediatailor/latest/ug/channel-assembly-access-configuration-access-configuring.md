# Configuring AWS Secrets Manager access token authentication

When you want to use AWS Secrets Manager access token authentication, you perform the
following steps:

1. You [create an AWS Key Management Service
   customer managed key](../../../kms/latest/developerguide/create-keys.md "../../../kms/latest/developerguide/create-keys.md").
2. You [create a
   AWS Secrets Manager secret](../../../secretsmanager/latest/userguide/managing-secrets.md "../../../secretsmanager/latest/userguide/managing-secrets.md"). The secret contains your access token,
   which is stored in Secrets Manager as an encrypted secret value. MediaTailor uses
   the AWS KMS customer managed key to decrypt the secret value.
3. You configure an AWS Elemental MediaTailor source location to use Secrets Manager access
   token authentication.
   The following section provides step-by-step guidance on how to configure
   AWS Secrets Manager access token authentication.

###### Topics

- [Step 1: Create an AWS KMS symmetric customer managed key](#channel-assembly-access-configuration-access-token-how-to-create-kms "#channel-assembly-access-configuration-access-token-how-to-create-kms")
- [Step 2: Create an AWS Secrets Manager secret](#channel-assembly-access-configuration-access-token-how-to-create-secret "#channel-assembly-access-configuration-access-token-how-to-create-secret")
- [Step 3: Configure a MediaTailor source location with access token
  authentication](#channel-assembly-access-configuration-access-token-how-to-enable-access-token-auth "#channel-assembly-access-configuration-access-token-how-to-enable-access-token-auth")

## Step 1: Create an AWS KMS symmetric customer managed key

You use AWS Secrets Manager to store your access token in the form of a
`SecretString` stored in a secret. The
`SecretString` is encrypted through the use of an _AWS KMS symmetric customer managed key_ that you create,
own, and manage. MediaTailor uses the symmetric customer managed key to facilitate access to
the secret with a grant, and to encrypt and decrypt the secret value.

Customer managed keys let you perform tasks such as the following:

- Establishing and maintaining key policies
- Establishing and maintaining IAM policies and grants
- Enabling and disabling key policies
- Rotating cryptographic key material
- Adding tags

For information about how Secrets Manager uses AWS KMS to protect secrets, see
the topic [How AWS Secrets Manager uses AWS KMS](../../../kms/latest/developerguide/services-secrets-manager.md "../../../kms/latest/developerguide/services-secrets-manager.md") in the _AWS Key Management Service Developer Guide_.

For more information about customer managed keys, see [Customer managed keys](../../../kms/latest/developerguide/concepts.md#customer-cmk "../../../kms/latest/developerguide/concepts.md#customer-cmk") in the _AWS Key Management Service Developer Guide_.

###### Note

AWS KMS charges apply for using a customer managed key For more information about
pricing, see the [AWS Key Management Service Pricing](https://aws.amazon.com/kms/pricing/ "https://aws.amazon.com/kms/pricing/") page.

You can create an AWS KMS symmetric customer managed key using the AWS Management Console or
programmatically with the AWS KMS APIs.

### To create a symmetric customer managed key

Follow the steps for [Creating a symmetric customer managed key](../../../kms/latest/developerguide/create-keys.md#create-symmetric-cmk "../../../kms/latest/developerguide/create-keys.md#create-symmetric-cmk") in the _AWS Key Management Service Developer Guide._

Make a note of the key Amazon Resource Name (ARN); you'll need it in
[Step 2: Create an AWS Secrets Manager secret](#channel-assembly-access-configuration-access-token-how-to-create-secret "#channel-assembly-access-configuration-access-token-how-to-create-secret").

### Encryption context

An _encryption context_ is an
optional set of key-value pairs that contain additional contextual
information about the data.

Secrets Manager includes an [encryption context](../../../kms/latest/developerguide/services-secrets-manager.md#asm-encryption-context "../../../kms/latest/developerguide/services-secrets-manager.md#asm-encryption-context") when encrypting and decrypting the
`SecretString`. The encryption context includes the
secret ARN, which limits the encryption to that specific secret. As an
added measure of security, MediaTailor creates an AWS KMS grant on your behalf.
MediaTailor applies a [GrantConstraints](../../../kms/latest/APIReference/API_GrantConstraints.md "../../../kms/latest/APIReference/API_GrantConstraints.md") operation that only allows us to _decrypt_ the `SecretString`
associated with the secret ARN contained in the Secrets Manager encryption
context.

For information about how Secrets Manager uses encryption context, see the
[Encryption context](../../../kms/latest/developerguide/concepts.md#encrypt_context "../../../kms/latest/developerguide/concepts.md#encrypt_context") topic in the _AWS Key Management Service Developer Guide_.

### Setting the key policy

Key policies control access to your customer managed key. Every customer managed key must
have exactly one key policy, which contains statements that determine
who can use the key and how they can use it. When you create your
customer managed key you can use the default key policy. For more information, see
[Authentication
and access control for AWS KMS](../../../kms/latest/developerguide/control-access.md "../../../kms/latest/developerguide/control-access.md") in the _AWS Key Management Service Developer Guide_.

To use your customer managed key with your MediaTailor source location resources, you
must give permission to the IAM principal that calls [CreateSourceLocation](../apireference/API_CreateSourceLocation.md "../apireference/API_CreateSourceLocation.md") or [UpdateSourceLocation](../apireference/API_UpdateSourceLocation.md "../apireference/API_UpdateSourceLocation.md") to use the following API
operations:

- `kms:CreateGrant` – Adds a grant to a customer managed key.
  MediaTailor creates a grant on your customer managed key that lets it
  use the key to create or update a source location configured
  with access token authentication. For more information about
  using [Grants in
  AWS KMS](../../../kms/latest/developerguide/grants.md "../../../kms/latest/developerguide/grants.md"), see the _AWS Key Management Service Developer Guide._

This allows MediaTailor to do the following:

    + Call `Decrypt` so that it can successfully
     retrieve your Secrets Manager secret when calling [GetSecretValue](../../../secretsmanager/latest/apireference/API_GetSecretValue.md "../../../secretsmanager/latest/apireference/API_GetSecretValue.md").
    + Call `RetireGrant` to retire the grant when
     the source location is deleted, or when access to the
     secret has been revoked.

The following is an example policy statement that you can add for
MediaTailor:

```
{
        "Sid": "Enable MediaTailor Channel Assembly access token usage for the MediaTailorManagement IAM role",
        "Effect": "Allow",
        "Principal": {
        "AWS": "arn:aws:iam::`account number`:role/MediaTailorManagement"
    },
     "Action": "kms:CreateGrant",
     "Resource": "*",
     "Condition": {
         "StringEquals": {
             "kms:ViaService": "mediatailor.`region`.amazonaws.com"
        }
    }
}
```

For more information about specifying permissions in a policy and
troubleshooting key access, see [Grants in AWS KMS](../../../kms/latest/developerguide/grants.md "../../../kms/latest/developerguide/grants.md") in the _AWS Key Management Service Developer Guide_.

## Step 2: Create an AWS Secrets Manager secret

Use Secrets Manager to store your access token in the form of a
`SecretString` that's encrypted by an AWS KMS customer managed key. MediaTailor
uses the key to decrypt the `SecretString`. For information about
how Secrets Manager uses AWS KMS to protect secrets, see the topic [How
AWS Secrets Manager uses AWS KMS](../../../kms/latest/developerguide/services-secrets-manager.md "../../../kms/latest/developerguide/services-secrets-manager.md") in the _AWS Key Management Service Developer Guide_.

If you use AWS Elemental MediaPackage as your source location origin, and would like to use
MediaTailor Secrets Manager access token authentication follow the procedure [Integrating with MediaPackage endpoints that use CDN authorization](channel-assembly-access-configuration-access-token-integrating-emp-cdn-auth.md "channel-assembly-access-configuration-access-token-integrating-emp-cdn-auth.md").

You can create a Secrets Manager secret using the AWS Management Console or programmatically with
the Secrets Manager APIs.

### To create a secret

Follow the steps for [Create
and manage secrets with AWS Secrets Manager](../../../secretsmanager/latest/userguide/managing-secrets.md "../../../secretsmanager/latest/userguide/managing-secrets.md") in the
_AWS Secrets Manager User Guide_.

Keep in mind the following considerations when creating your
secret:

- The [KmsKeyId](../../../secretsmanager/latest/apireference/API_ReplicaRegionType.md#SecretsManager-Type-ReplicaRegionType-KmsKeyId "../../../secretsmanager/latest/apireference/API_ReplicaRegionType.md#SecretsManager-Type-ReplicaRegionType-KmsKeyId") must be the [key
  ARN](../../../kms/latest/developerguide/find-cmk-id-arn.md "../../../kms/latest/developerguide/find-cmk-id-arn.md") of the customer managed key you created in Step 1.
- You must supply a [SecretString](../../../secretsmanager/latest/apireference/API_CreateSecret.md#SecretsManager-CreateSecret-request-SecretString "../../../secretsmanager/latest/apireference/API_CreateSecret.md#SecretsManager-CreateSecret-request-SecretString"). The `SecretString` should
  be a valid JSON object that includes a key and value containing
  the access token. For example,
  {"MyAccessTokenIdentifier":"112233445566"}. The value must
  between 8-128 characters long.

When you configure your source location with access token
authentication, you specify the `SecretString` key.
MediaTailor uses the key to look up and retrieve the access token
stored in the `SecretString`.

Make a note of the secret ARN and the
`SecretString` key. You'll use them when you
configure your source location to use access token
authentication.

### Attaching a resource-based secret policy

To let MediaTailor access the secret value, you must attach a resource-based
policy to the secret. For more information, see [Attach a permissions policy to an Secrets Manager
Secret](../../../secretsmanager/latest/userguide/auth-and-access_resource-policies.md "../../../secretsmanager/latest/userguide/auth-and-access_resource-policies.md") in the _AWS Secrets Manager User Guide_.

The following is a policy statement example that you can add for
MediaTailor:

JSON

```
`{

 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Principal": {
 "Service": "mediatailor.amazonaws.com"
 },
 "Action": "secretsmanager:GetSecretValue",
 "Resource": "arn:aws:secretsmanager:`us-east-1`:`111122223333`:secret:`secret-name`"
 }
 ]

}`

```

## Step 3: Configure a MediaTailor source location with access token

authentication

You can configure Secrets Manager access token authentication using the AWS Management Console or
programmatically with the MediaTailor APIs.

**To configure a source location with Secrets Manager access
token authentication**

Follow the steps for [Access configuration](channel-assembly-creating-source-locations.md#access-configuration-console "channel-assembly-creating-source-locations.md#access-configuration-console") in the
_AWS Elemental MediaTailor User Guide_.
