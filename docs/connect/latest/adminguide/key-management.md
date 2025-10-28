# Key management in Amazon Connect

You can specify AWS KMS keys, including bring your own keys (BYOK), to use for envelope
encryption with Amazon S3 input/output buckets.

When you associate the AWS KMS key to the S3 storage location in Amazon Connect, the API caller's
permissions (or the console user's permissions) are used to create a grant on the key
with the corresponding Amazon Connect instance service role as the grantee principal. For the
service linked role specific to that Amazon Connect instance, the grant allows the role to use
the key for encryption and decryption. For example:

- If you call the [DisassociateInstanceStorageConfig](../APIReference/API_DisassociateInstanceStorageConfig.md "../APIReference/API_DisassociateInstanceStorageConfig.md") API to dissociate the AWS KMS key
  from the S3 storage location in Amazon Connect, the grant is removed from the key.
- If you call the [AssociateInstanceStorageConfig](../APIReference/API_AssociateInstanceStorageConfig.md "../APIReference/API_AssociateInstanceStorageConfig.md") API to associate the AWS KMS key to
  the S3 storage location in Amazon Connect but you don't have the kms:CreateGrant
  permission, the association will fail.
  Use the [`list-grants`](https://awscli.amazonaws.com/v2/documentation/api/2.0.34/reference/kms/list-grants.html "https://awscli.amazonaws.com/v2/documentation/api/2.0.34/reference/kms/list-grants.html") CLI command to list all grants for the
  specified customer managed key.

For information about AWS KMS keys see [What is AWS Key Management Service?](../../../kms/latest/developerguide/overview.md "../../../kms/latest/developerguide/overview.md") in the
_AWS Key Management Service Developer Guide_.

## Amazon Q in Connect

Amazon Q in Connect stores knowledge documents that are encrypted at rest in S3 using a
BYOK or a service-owned key. The knowledge documents are encrypted at rest in
Amazon OpenSearch Service using a service-owned key. Amazon Q in Connect stores agent queries and call
transcripts using a BYOK or a service-owned key.

The knowledge documents used by Amazon Q in Connect are encrypted by an AWS KMS key.

## Amazon AppIntegrations

Amazon AppIntegrations doesn't support BYOK for encryption of configuration data. When syncing
external application data, periodically you are required to BYOK. Amazon AppIntegrations
requires a grant to use your customer managed key. When you create a data integration,
Amazon AppIntegrations sends a `CreateGrant` request to AWS KMS on your behalf. You can
revoke access to the grant, or remove the service's access to the customer managed key at any
time. If you do, Amazon AppIntegrations won't be able to access any of the data encrypted by the
customer managed key, which affects Amazon Connect services that are dependent on that data.

## Customer Profiles

For Customer Profiles, you can specify AWS KMS keys, including bring your own keys (BYOK), to use
for envelope encryption with Amazon S3 input/output buckets.

## Voice ID

For using Amazon Connect Voice ID, it is mandatory to provide a customer managed key KMS key (BYOK)
while creating a Amazon Connect Voice ID domain, which is used to encrypt all the customer
data at rest.

## Outbound campaigns

Outbound campaigns encrypts all sensitive data using an AWS owned key or a
customer managed key. As the customer managed key is created, owned, and managed by the you, you have
full control over the customer managed key (AWS KMS charges apply).
