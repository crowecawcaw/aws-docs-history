This guide documents the new AWS Wickr administration console, released on
March 13, 2025. For documentation on the classic version of the AWS Wickr administration console, see [Classic
Administration Guide](../adminguide-classic/what-is-wickr.md "../adminguide-classic/what-is-wickr.md").

# Encryption at rest

AWS Wickr Data Retention Service transparently encrypts all retained messages and file
attachments at rest by default. You do not need to perform any additional configuration to
ensure your data is encrypted at rest. The Data Retention Service applies encryption on the
server-side for all customer data stored in Amazon S3.

The Data Retention Service encrypts customer data at rest using a customer managed KMS key
(CMK). When you deploy the Data Retention Service through AWS Service Catalog, a symmetric CMK is
automatically created in your account and configured as the default encryption key for all
retained data. You retain full control over this key, including the ability to audit usage,
rotate the key, and revoke access.

## Encrypting data at rest using customer managed KMS keys for data retention

### How the Data Retention Service uses a customer managed KMS key

When the Data Retention Service is deployed, a symmetric customer managed KMS key
(RetentionKey) is created in your AWS account. This key is used to
encrypt the following resources:

- **Retained messages** — All Wickr
  messages (text, reactions, and others) captured by the data retention bot
  are encrypted with the CMK before being stored in your S3 bucket.
  Messages are encrypted inside a Nitro Enclave using the AWS Encryption
  SDK, then uploaded to Amazon S3 with SSE-KMS using the same CMK.
- **Retained file attachments** — File
  attachments associated with messages are decrypted from Wickr's end-to-end
  encryption inside the Nitro Enclave, re-encrypted with the CMK, and stored
  in Amazon S3 with SSE-KMS.
- **Encrypted account state** — The data
  retention bot's cryptographic private keys and account state are encrypted
  with the CMK and stored in DynamoDB. Decryption of this state requires Nitro
  Enclave attestation.
- **S3 bucket default encryption** — The
  retention S3 bucket is configured with SSE-KMS using the CMK as the default
  encryption key. A bucket policy enforces that all objects must be uploaded
  with `aws:kms` server-side encryption.
- **Decrypted output bucket** — When
  customers trigger on-demand decryption (via Step Functions state machine), the
  decrypted output is also stored in a separate S3 bucket encrypted with the
  same CMK.

###### Cross-account role architecture

The Data Retention Service operates in a Wickr-managed AWS account and
accesses customer resources via a cross-account IAM role
(`DRSCustomerCrossAccountRole-{networkId}-{region}`). The Wickr
DRS Enclave Role assumes this customer-side role using AWS STS with an external ID
(`wickr-drs-{networkId}`) to perform KMS and S3
operations.

###### Nitro Enclave attestation

Direct `kms:Decrypt` calls (outside of S3 SSE-KMS) require Nitro
Enclave attestation. The KMS key policy enforces that the
`kms:RecipientAttestation:PCR0`,
`kms:RecipientAttestation:PCR1`, and
`kms:RecipientAttestation:PCR2` conditions must be present,
ensuring that decryption of sensitive data (account state, message content) can
only occur inside the verified enclave. This prevents any
operator—including Wickr—from decrypting customer data outside the
enclave.

AWS Nitro Enclaves process messages using your KMS key to
decrypt the data retention module's private keys, decrypt the Wickr-encrypted
message content, and re-encrypt it with a unique data key per message before storing
it in your S3 bucket.

### Configuring customer managed KMS keys in Data Retention Service

The Data Retention Service supports symmetric KMS keys with key usage
`ENCRYPT_DECRYPT` and key spec `SYMMETRIC_DEFAULT`.
Automatic key rotation is enabled by default when the key is created via Service
Catalog.

Additionally, a second asymmetric KMS key (ECC\_NIST\_P384, KEY\_AGREEMENT) is
created for the password recovery workflow. This key is used for ECDH key agreement
and cannot be used for general encryption/decryption. This key is optionally used
for customers migrating from a Data Retention Bot docker-based architecture.

###### Note

Multi-region keys are not currently supported. The KMS key must be in the same
region as the S3 bucket and the Data Retention Service deployment.

#### Configuring permissions to use a customer managed KMS key

The following key policy is automatically configured when deploying via
Service Catalog. If you need to manually configure a key, use the following
least-privilege policy:

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "YourExistingStatements",
      "Effect": "...",
      "...": "..."
    },
    {
      "Sid": "EnclaveGenerateDataKey",
      "Effect": "Allow",
      "Principal": {
        "AWS": "arn:aws:iam::`{customer-account-id}`:role/DRSCustomerCrossAccountRole-`{networkId}`-`{region}`"
      },
      "Action": "kms:GenerateDataKey",
      "Resource": "*",
      "Condition": {
        "StringLike": {
          "kms:RecipientAttestation:PCR0": "*",
          "kms:RecipientAttestation:PCR1": "*",
          "kms:RecipientAttestation:PCR2": "*"
        },
        "ForAnyValue:StringEquals": {
          "kms:EncryptionContextKeys": [
            "aws:wickr:network:id",
            "aws:wickr:app:id"
          ]
        }
      }
    },
    {
      "Sid": "EnclaveDescribeKey",
      "Effect": "Allow",
      "Principal": {
        "AWS": "arn:aws:iam::`{customer-account-id}`:role/DRSCustomerCrossAccountRole-`{networkId}`-`{region}`"
      },
      "Action": "kms:DescribeKey",
      "Resource": "*"
    },
    {
      "Sid": "EnclaveDecryptWithAttestation",
      "Effect": "Allow",
      "Principal": {
        "AWS": "arn:aws:iam::`{customer-account-id}`:role/DRSCustomerCrossAccountRole-`{networkId}`-`{region}`"
      },
      "Action": "kms:Decrypt",
      "Resource": "*",
      "Condition": {
        "StringLike": {
          "kms:RecipientAttestation:PCR0": "*",
          "kms:RecipientAttestation:PCR1": "*",
          "kms:RecipientAttestation:PCR2": "*"
        },
        "ForAnyValue:StringEquals": {
          "kms:EncryptionContextKeys": "aws:wickr:app:id"
        }
      }
  },
    {
      "Sid": "DRSDecryptionLambda",
      "Effect": "Allow",
      "Principal": {
        "AWS": "arn:aws:iam::`{customer-account-id}`:role/{DecryptionLambdaRoleName}"
      },
      "Action": "kms:Decrypt",
      "Resource": "*",
      "Condition": {
        "ForAnyValue:StringEquals": {
          "kms:EncryptionContextKeys": "aws:wickr:network:id"
        }
      }
    }
  ]
}
```

Purpose of each statement:

EnableIAMPolicies

Allows your account root to manage the key. This is the
standard key administrator statement.

EnclaveGenerateDataKey

`kms:GenerateDataKey` — Invoked by the Nitro
Enclave to to generate data encryption keys for encrypting message
content and account state before storing in S3. Only permitted when
the enclave provides a valid Nitro Enclave attestation document (PCR0/1/2
conditions) and an encryption context key of aws:wickr:network:id or
aws:wickr:app:id is present.

EnclaveDescribeKey

`kms:DescribeKey` — Allows the enclave to
retrieve key metadata (key spec, usage, status) for validation
during initialization.

EnclaveDecryptWithAttestation

`kms:Decrypt` — Invoked by the Nitro Enclave to
decrypt account state (private keys) needed for Wickr message
decryption. This is only permitted when the enclave provides a valid Nitro Enclave
attestation document (PCR0/1/2 conditions), and the
encryption context key aws:wickr:app:id is present, ensuring
decryption cannot occur outside the enclave.

DRSDecryptionLambda

`kms:Decrypt` — Invoked by the on-demand
decryption Lambda to decrypt retained messages when you
trigger the decryption state machine. This role is not accessible
by the Wickr service and exists solely for you to decrypt
your own messages from the encrypted S3 bucket.

If migration is required from previous data retention installation, you must
provide your Docker-bot module password to the service before serverless data
retention can be enabled. For more information see, [Password recovery instruction](password-recovery-instruction.md "password-recovery-instruction.md"). For details on the policy
required for your password recover key, see [Custom KMS key setup for data retention service](custom-kms-key.md "custom-kms-key.md").

If you need to manually configure KMS key, see [Custom KMS key setup for data retention service](custom-kms-key.md "custom-kms-key.md") for least permissive policy for your
key.

#### Creating a new Data Retention deployment with a customer managed KMS key

The Data Retention Service is deployed through AWS Service Catalog. When you launch the
`WickrDataRetentionProduct` product, the CloudFormation template
automatically:

1. Creates a symmetric CMK with alias
   `wickr-drs-`{networkId}`-`{region}`-`{suffix}`-key`
2. Creates an asymmetric CMK (ECC P-384) for password recovery with alias
   `wickr-drs-`{networkId}`-`{region}`-`{suffix}`-password-recovery-key`
3. Creates an S3 bucket with SSE-KMS default encryption using the
   symmetric CMK
4. Creates the `DRSCustomerCrossAccountRole` with appropriate
   KMS permissions
5. Registers the KMS key ARN and S3 bucket with the Wickr Admin API via
   a Custom Resource Lambda

The KMS key ARN is also registered via the Wickr Admin SDK endpoint:

```
PUT /networks/`{networkId}`/serverless-resources
{
  "s3BucketName": "wickr-drs-`{networkId}`-`{region}`-`{suffix}`",
  "kmsKeyArn": "arn:aws:kms:`{region}`:`{accountId}`:key/`{keyId}`",
  "passwordRecoveryKmsKeyArn": "arn:aws:kms:`{region}`:`{accountId}`:key/`{keyId}`"
}
```

The `kmsKeyArn` parameter must be a valid KMS key ARN. The API
validates the ARN format before storing it.

#### Changing encryption configuration on an existing deployment

The Data Retention Service does not currently support changing the CMK after
deployment. The KMS key is tightly coupled to:

- The S3 bucket's default encryption configuration
- The encrypted account state stored in DynamoDB
- The key policy with Nitro Enclave attestation conditions

To change the encryption key, you must:

1. Deploy a new Data Retention Service instance with a new KMS
   key.
2. Previously retained messages encrypted with the old key remain
   accessible only with the original key.

###### Important

Do not disable or delete the original KMS key while encrypted messages
exist in the retention bucket. Doing so will make those messages permanently
unrecoverable.

#### Scoping down access to the customer managed KMS key

###### Nitro Enclave attestation (primary access control)

The primary mechanism for scoping access to the CMK is Nitro Enclave
attestation. The key policy requires
`kms:RecipientAttestation:PCR0`, `PCR1`, and
`PCR2` conditions for direct `kms:Decrypt` calls.
This ensures:

- Only the verified Wickr DRS enclave binary can decrypt sensitive
  data.
- Even the cross-account role cannot decrypt data outside the
  enclave.
- CloudTrail logs include the actual PCR values for auditing.

###### Confused deputy protection

The cross-account role uses an external ID
(`wickr-drs-{networkId}`) in the STS `AssumeRole`
call. This prevents confused deputy attacks where another service might
attempt to use the Wickr DRS enclave role to access your resources.

###### kms:ViaService condition

S3 SSE-KMS decrypt operations are scoped using the
`kms:ViaService` condition. This ensures that S3-mediated
decryption is only permitted when the request comes through the S3
service.

###### Encryption context

S3 SSE-KMS automatically includes the S3 object ARN as encryption context.
The key policy uses this encryption context to scope S3 decrypt permissions
to specific prefixes (for example, the password tool prefix).

## Monitoring Data Retention Service interaction with AWS KMS

You can monitor all KMS API calls made by the Data Retention Service using CloudTrail. To
search CloudTrail log entries, use the CloudTrail console or the CloudTrail `LookupEvents`
operation.

The following CloudTrail event fields can be used to audit KMS usage by the Data Retention
Service:

| Field                                               | Expected value                                                                                                                                                  |
| --------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `eventName`                                         | `Encrypt`, `Decrypt`,<br>`GenerateDataKey`                                                                                                                      |
| `userIdentity.arn`                                  | `arn:aws:sts::`{customerAccountId}`:assumed-role/DRSCustomerCrossAccountRole-`{networkId}`-`{region}``<br>or `drs-create-account` or<br>`drs-password-recovery` |
| `requestParameters.keyId`                           | Your CMK ARN (for example,<br>`arn:aws:kms:`{region}`:`{accountId}`:key/`{keyId}``)                                                                             |
| `additionalEventData.recipient.attestationDocument` | Present for enclave-attested Decrypt calls (contains PCR<br>values)                                                                                             |
| `requestParameters.encryptionContext`               | For S3 SSE-KMS: `{"aws:s3:arn":<br>"arn:aws:s3:::`{bucketName}`/`{objectKey}`"}`                                                                                |

Key events to monitor:

- **Encrypt** — Occurs when the enclave
  encrypts message content or account state before storing in S3/DynamoDB.
- **GenerateDataKey** — Occurs when S3
  generates a data key for SSE-KMS envelope encryption during object
  upload.
- **Decrypt** — Occurs when the enclave
  decrypts account state (with attestation) or when S3 auto-decrypts objects on
  read.
- **DeriveSharedSecret** — Occurs on the
  password recovery key when the enclave performs ECDH key agreement during the
  password recovery flow.
- **GetPublicKey** — Occurs on the password
  recovery key when your `collect.py` script retrieves the
  public key for local ECDH encryption.

Additionally, the Service Catalog product creates a CloudWatch dashboard
(`WickrDataRetentionService-`{networkId}``)
that includes widgets for KMS key success metrics (Encrypt, GenerateDataKey, Decrypt
operations) and a decryption error alarm that triggers when decryption failures are
detected.
