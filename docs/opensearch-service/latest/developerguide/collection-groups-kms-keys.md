# Encryption and KMS keys in collection

groups

Each OpenSearch Serverless collection you create is protected with encryption of data at rest using
AWS KMS to store and manage your encryption keys. When working with collection groups, you
have flexibility in how you specify the KMS key for your collections.

You can provide the KMS key associated with a collection in two ways:

- **In the CreateCollection request** – Specify the
  KMS key directly when you create the collection using the
  `encryption-config` parameter.
- **In security policies** – Define the KMS key
  association in an encryption security policy.
  When you specify a KMS key in both locations, the KMS key provided in the
  CreateCollection request takes precedence over the security policy configuration.

This flexibility simplifies managing collections at scale, particularly when you need
to create multiple collections with unique KMS keys. Instead of creating and managing
thousands of encryption policies, you can specify the KMS key directly during collection
creation.

## Sharing OCUs across different KMS

keys

Collection groups enable compute resource sharing across collections with
different KMS keys. Collections in the same collection group share OCU memory space,
regardless of their encryption keys. This shared compute model reduces costs by
eliminating the need for separate OCUs for each KMS key.

Collection groups provide isolation for security and performance requirements. You
can group collections with the same KMS key into a single collection group for
security isolation, or combine collections with different KMS keys in the same group
for cost optimization. This flexibility lets you balance security requirements with
resource efficiency.

The system maintains security by encrypting each collection's data with its
designated KMS key. Access controls continue to apply at the collection level, and
the shared compute resources access multiple KMS keys as needed to serve the
collections in the group.

## Required KMS permissions

When you specify a KMS key in the CreateCollection request, you need the following
additional permissions:

- `kms:DescribeKey` – Allows OpenSearch Serverless to retrieve information about
  the KMS key.
- `kms:CreateGrant` – Allows OpenSearch Serverless to create a grant for the KMS
  key to enable encryption operations.

These permissions are not required when using AWS owned keys.
