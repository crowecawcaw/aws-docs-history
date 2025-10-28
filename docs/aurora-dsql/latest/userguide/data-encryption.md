# Data encryption for Amazon Aurora DSQL

Amazon Aurora DSQL encrypts all user data at rest. For enhanced security, this encryption uses
AWS Key Management Service (AWS KMS). This functionality helps reduce the operational burden and complexity
involved in protecting sensitive data. Encryption at rest helps you:

- Reduce the operational burden of protecting sensitive data
- Build security-sensitive applications that meet strict encryption compliance and
  regulatory requirements
- Add an extra layer of data protection by always securing your data in an encrypted
  cluster
- Comply with organizational policies, industry or government regulations, and compliance
  requirements
  With Aurora DSQL, you can build security-sensitive applications that meet strict
  encryption compliance and regulatory requirements. The following sections explain how to
  configure encryption for new and existing Aurora DSQL databases and manage your encryption
  keys.

###### Topics

- [KMS key types for Aurora DSQL](#kms-key-types "#kms-key-types")
- [Encryption at rest in Aurora DSQL](#encryption-at-rest "#encryption-at-rest")
- [Using AWS KMS and data keys with Aurora DSQL](#using-kms-and-data-keys "#using-kms-and-data-keys")
- [Authorizing use of your AWS KMS key for
  Aurora DSQL](#authorizing-kms-key-use "#authorizing-kms-key-use")
- [Aurora DSQL encryption context](#dsql-encryption-context "#dsql-encryption-context")
- [Monitoring Aurora DSQL interaction with
  AWS KMS](#monitoring-dsql-kms-interaction "#monitoring-dsql-kms-interaction")
- [Creating an encrypted Aurora DSQL cluster](#creating-encrypted-cluster "#creating-encrypted-cluster")
- [Removing or updating a key for your Aurora DSQL cluster](#updating-encryption-key "#updating-encryption-key")
- [Considerations for encryption with
  Aurora DSQL](#considerations-with-encryption "#considerations-with-encryption")

## KMS key types for Aurora DSQL

Aurora DSQL integrates with AWS KMS to manage the encryption keys for your clusters. To learn
more about key types and states, see [AWS Key Management Service concepts](../../../kms/latest/developerguide/concepts-intro.md "../../../kms/latest/developerguide/concepts-intro.md") in the
_AWS Key Management Service Developer Guide_. When you create a new cluster, you can
choose from the following KMS key types to encrypt your cluster:

**AWS owned key**

Default encryption type. Aurora DSQL owns the key at no additional charge to you. Amazon
Aurora DSQL transparently decrypts cluster data when you access an encrypted cluster.
You don't need to change your code or applications to use or manage encrypted clusters,
and all Aurora DSQL queries work with your encrypted data.

**Customer managed key**

You create, own, and manage the key in your AWS account. You have full control
over the KMS key. AWS KMS charges apply.

Encryption at rest using the AWS owned key is available at no additional charge.
However, AWS KMS charges apply for customer managed keys. For more information, see the [AWS KMS Pricing](https://aws.amazon.com/kms/pricing/ "https://aws.amazon.com/kms/pricing/") page.

You can switch between these key types at any time. For more information about key types,
see [Customer managed keys](../../../kms/latest/developerguide/concepts.md#customer-cmk "../../../kms/latest/developerguide/concepts.md#customer-cmk") and [AWS owned keys](../../../kms/latest/developerguide/concepts.md#aws-owned-cmk "../../../kms/latest/developerguide/concepts.md#aws-owned-cmk") in the
_AWS Key Management Service Developer Guide_.

###### Note

Aurora DSQL encryption at rest is available in all AWS Regions where Aurora DSQL is
available.

## Encryption at rest in Aurora DSQL

Amazon Aurora DSQL uses 256-bit Advanced Encryption Standard (AES-256) to encrypt your data at
rest. This encryption helps protect your data from unauthorized access to the underlying
storage. AWS KMS manages the encryption keys for your clusters. You can use the default [AWS owned keys](#aws-owned-keys "#aws-owned-keys"), or choose to use your own AWS KMS
[Customer managed keys](#customer-managed-keys "#customer-managed-keys"). To learn more
about specifying and managing keys for your Aurora DSQL clusters, see [Creating an encrypted Aurora DSQL cluster](#creating-encrypted-cluster "#creating-encrypted-cluster") and [Removing or updating a key for your Aurora DSQL cluster](#updating-encryption-key "#updating-encryption-key").

###### Topics

- [AWS owned keys](#aws-owned-keys "#aws-owned-keys")
- [Customer managed keys](#customer-managed-keys "#customer-managed-keys")

### AWS owned keys

Aurora DSQL encrypts all clusters by default with AWS owned keys. These keys are free to
use and rotate annually to protect your account resources. You don't need to view, manage,
use, or audit these keys, so there's no action required for data protection. For more
information about AWS owned keys, see [AWS owned keys](../../../kms/latest/developerguide/concepts.md#aws-owned-cmk "../../../kms/latest/developerguide/concepts.md#aws-owned-cmk") in
the _AWS Key Management Service Developer Guide_.

### Customer managed keys

You create, own, and manage customer managed keys in your AWS account. You have full
control over these KMS keys, including their policies, encryption material, tags, and
aliases. For more information about managing permissions, see [Customer managed keys](../../../kms/latest/developerguide/concepts.md#customer-cmk "../../../kms/latest/developerguide/concepts.md#customer-cmk")
in the _AWS Key Management Service Developer Guide_.

When you specify a customer managed key for cluster-level encryption, Aurora DSQL encrypts
the cluster and all its regional data with that key. To prevent data loss and maintain
cluster access, Aurora DSQL needs access to your encryption key. If you disable your customer
managed key, schedule your key for deletion, or have a policy that restricts your service
access, the encryption status for your cluster changes to `KMS_KEY_INACCESSIBLE`.
When Aurora DSQL can't access the key, users can't connect to the cluster, the encryption status
for the cluster changes to `KMS_KEY_INACCESSIBLE`, and the service loses access
to the cluster data.

For multi-Region clusters, customers can configure each region's AWS KMS encryption key
separately, and each regional cluster uses its own cluster-level encryption key. If Aurora DSQL
can't access the encryption key for a peer in a multi-Region cluster, the status for that
peer becomes `KMS_KEY_INACCESSIBLE` and it becomes unavailable for read and write
operations. Other peers continue normal operations.

###### Note

If Aurora DSQL can't access your customer managed key, your cluster encryption status
changes to `KMS_KEY_INACCESSIBLE`. After you restore key access, service will
automatically detect the restoration within 15 minutes. For more information, see Cluster
idling.

For multi-Region clusters, if key access is lost for an extended time, the cluster
restoration time depends on how much data was written while the key was
inaccessible.

## Using AWS KMS and data keys with Aurora DSQL

The Aurora DSQL encryption at rest feature uses an AWS KMS key and a hierarchy of data keys
to protect your cluster data.

We recommend that you plan your encryption strategy before implementing your cluster in
Aurora DSQL. If you store sensitive or confidential data in Aurora DSQL, consider including client-side
encryption in your plan. This way you can encrypt data as close as possible to its origin, and
ensure its protection throughout its lifecycle.

###### Topics

- [Using AWS KMS keys with Aurora DSQL](#aws-kms-key "#aws-kms-key")
- [Using cluster keys with Aurora DSQL](#cluster-keys "#cluster-keys")
- [Cluster key caching](#cluster-key-caching "#cluster-key-caching")

### Using AWS KMS keys with Aurora DSQL

Encryption at rest protects your Aurora DSQL cluster under an AWS KMS key. By default,
Aurora DSQL uses an AWS owned key, a multi-tenant encryption key that is created and managed in
a Aurora DSQL service account. But you can encrypt your Aurora DSQL clusters under a customer managed
key in your AWS account. You can select a different KMS key for each cluster, even if it
participates in a multi-Region setup.

You select the KMS key for a cluster when you create or update the cluster. You can
change the KMS key for a cluster at any time, either in the Aurora DSQL console or by using the
`UpdateCluster` operation. The process of switching keys doesn't require
downtime or degrade service.

###### Important

Aurora DSQL supports only symmetric KMS keys. You can't use an asymmetric KMS key to
encrypt your Aurora DSQL clusters.

A customer managed key provides the following benefits.

- You create and manage the KMS key, including setting the key policies and IAM
  policies to control access to the KMS key. You can enable and disable the KMS key,
  enable and disable automatic key rotation, and delete the KMS key when it is no longer
  in use.
- You can use a customer managed key with imported key material or a customer managed
  key in a custom key store that you own and manage.
- You can audit the encryption and decryption of your Aurora DSQL cluster by examining the
  Aurora DSQL API calls to AWS KMS in AWS CloudTrail logs.

However, the AWS owned key is free of charge and its use doesn't count against AWS KMS
resource or request quotas. Customer managed keys incur a charge for each API call and AWS KMS
quotas apply to these keys.

### Using cluster keys with Aurora DSQL

Aurora DSQL uses the AWS KMS key for the cluster to generate and encrypt a unique data key
for the cluster, known as the **cluster key**.

The cluster key is used as a key encryption key. Aurora DSQL uses this cluster key to protect
data encryption keys that are used to encrypt the cluster data. Aurora DSQL generates a unique
data encryption key for each underlying structure in a cluster, but multiple cluster items
might be protected by the same data encryption key.

To decrypt the cluster key, Aurora DSQL sends a request to AWS KMS when you first access an
encrypted cluster. To keep the cluster available, Aurora DSQL periodically verifies decrypt
access to the KMS key, even when you're not actively accessing the cluster.

Aurora DSQL stores and uses the cluster key and data encryption keys outside of AWS KMS. It
protects all keys with Advanced Encryption Standard (AES) encryption and 256-bit encryption
keys. Then, it stores the encrypted keys with the encrypted data so they are available to
decrypt the cluster data on demand.

If you change the KMS key for your cluster, Aurora DSQL re-encrypts the existing cluster
key with the new KMS key.

### Cluster key caching

To avoid calling AWS KMS for every Aurora DSQL operation, Aurora DSQL caches the plaintext cluster
keys for each caller in memory. If Aurora DSQL gets a request for the cached cluster key after 15
minutes of inactivity, it sends a new request to AWS KMS to decrypt the cluster key. This call
will capture any changes made to the access policies of the AWS KMS key in AWS KMS or
AWS Identity and Access Management (IAM) after the last request to decrypt the cluster key.

## Authorizing use of your AWS KMS key for

Aurora DSQL

If you use a customer managed key in your account to protect your Aurora DSQL cluster, the
policies on that key must give Aurora DSQL permission to use it on your behalf.

You have full control over the policies on a customer managed key. Aurora DSQL does not need
additional authorization to use the default AWS owned key to protect the Aurora DSQL clusters in
your AWS account.

### Key policy for a customer managed

key

When you select a customer managed key to protect a Aurora DSQL cluster, Aurora DSQL needs
permission to use the AWS KMS key on behalf of the principal who makes the selection.
That principal, a user or role, must have the permissions on the AWS KMS key that Aurora DSQL
requires. You can provide these permissions in a key policy, or an IAM policy.

At a minimum, Aurora DSQL requires the following permissions on a customer managed
key:

- `kms:Encrypt`
- `kms:Decrypt`
- `kms:ReEncrypt*` (for kms:ReEncryptFrom and kms:ReEncryptTo)
- `kms:GenerateDataKey`
- `kms:DescribeKey`

For example, the following example key policy provides only the required permissions.
The policy has the following effects:

- Allows Aurora DSQL to use the AWS KMS key in cryptographic operations, but only when
  it is acting on behalf of principals in the account who have permission to use Aurora DSQL.
  If the principals specified in the policy statement don't have permission to use Aurora DSQL,
  the call fails, even when it comes from the Aurora DSQL service.
- The `kms:ViaService` condition key allows the permissions only when the
  request comes from Aurora DSQL on behalf of the principals listed in the policy statement.
  These principals can't call these operations directly.
- Gives the AWS KMS key administrators (users who can assume the
  `db-team` role) read-only access to the AWS KMS key

Before using an example key policy, replace the example principals with actual
principals from your AWS account.

```
{
  "Sid": "Enable dsql IAM User Permissions",
  "Effect": "Allow",
  "Principal": {
    "Service": "dsql.amazonaws.com"
  },
  "Action": [
    "kms:Decrypt",
    "kms:GenerateDataKey",
    "kms:Encrypt",
    "kms:ReEncryptFrom",
    "kms:ReEncryptTo"
  ],
  "Resource": "*",
  "Condition": {
    "StringLike": {
      "kms:EncryptionContext:aws:dsql:ClusterId": "w4abucpbwuxx",
      "aws:SourceArn": "arn:aws:dsql:us-east-2:111122223333:cluster/w4abucpbwuxx"
    }
  }
},
{
  "Sid": "Enable dsql IAM User Describe Permissions",
  "Effect": "Allow",
  "Principal": {
    "Service": "dsql.amazonaws.com"
  },
  "Action": "kms:DescribeKey",
  "Resource": "*",
  "Condition": {
    "StringLike": {
      "aws:SourceArn": "arn:aws:dsql:us-east-2:111122223333:cluster/w4abucpbwuxx"
    }
  }
}

```

## Aurora DSQL encryption context

An encryption context is a set of key–value pairs that contain arbitrary nonsecret data.
When you include an encryption context in a request to encrypt data, AWS KMS cryptographically
binds the encryption context to the encrypted data. To decrypt the data, you must pass in the
same encryption context.

Aurora DSQL uses the same encryption context in all AWS KMS cryptographic operations. If you use
a customer managed key to protect your Aurora DSQL cluster, you can use the encryption context to
identify use of the AWS KMS key in audit records and logs. It also appears in plaintext in
logs such as those in AWS CloudTrail.

The encryption context can also be used as a condition for authorhorization in
policies.

In its requests to AWS KMS, Aurora DSQL uses an encryption context with a key-value pair:

```

"encryptionContext": {
  "aws:dsql:ClusterId": "w4abucpbwuxx"
},

```

The key–value pair identifies the cluster that Aurora DSQL is encrypting. The key is
`aws:dsql:ClusterId`. The value is the identifier of the cluster.

## Monitoring Aurora DSQL interaction with

AWS KMS

If you use a customer managed key to protect your Aurora DSQL clusters, you can use AWS CloudTrail
logs to track the requests that Aurora DSQL sends to AWS KMS on your behalf.

Expand the following sections to learn how Aurora DSQL uses the AWS KMS operations
`GenerateDataKey` and `Decrypt`.

When you enable encryption at rest on a cluster, Aurora DSQL creates a unique cluster key.
It sends a `GenerateDataKey` request to AWS KMS that specifies the AWS KMS key
for the cluster.

The event that records the `GenerateDataKey` operation is similar to the
following example event. The user is the Aurora DSQL service account. The parameters include
the Amazon Resource Name (ARN) of the AWS KMS key, a key specifier that requires a
256-bit key, and the encryption context that identifies the cluster.

```
{
    "eventVersion": "1.11",
    "userIdentity": {
        "type": "AWSService",
        "invokedBy": "dsql.amazonaws.com"
    },
    "eventTime": "2025-05-16T18:41:24Z",
    "eventSource": "kms.amazonaws.com",
    "eventName": "GenerateDataKey",
    "awsRegion": "us-east-1",
    "sourceIPAddress": "dsql.amazonaws.com",
    "userAgent": "dsql.amazonaws.com",
    "requestParameters": {
        "encryptionContext": {
            "aws:dsql:ClusterId": "w4abucpbwuxx"
        },
        "keySpec": "AES_256",
        "keyId": "arn:aws:kms:us-east-1:982127530226:key/8b60dd9f-2ff8-4b1f-8a9c-bf570cbfdb5e"
    },
    "responseElements": null,
    "requestID": "2da2dc32-d3f4-4d6c-8a41-aff27cd9a733",
    "eventID": "426df0a6-ba56-3244-9337-438411f826f4",
    "readOnly": true,
    "resources": [
        {
            "accountId": "AWS Internal",
            "type": "AWS::KMS::Key",
            "ARN": "arn:aws:kms:us-east-1:982127530226:key/8b60dd9f-2ff8-4b1f-8a9c-bf570cbfdb5e"
        }
    ],
    "eventType": "AwsApiCall",
    "managementEvent": true,
    "recipientAccountId": "111122223333",
    "sharedEventID": "f88e0dd8-6057-4ce0-b77d-800448426d4e",
    "vpcEndpointId": "AWS Internal",
    "vpcEndpointAccountId": "vpce-1a2b3c4d5e6f1a2b3",
    "eventCategory": "Management"
}

```

When you access an encrypted Aurora DSQL cluster, Aurora DSQL needs to decrypt the cluster key
so that it can decrypt the keys below it in the hierarchy. It then decrypts the data in
the cluster. To decrypt the cluster key, Aurora DSQL sends a `Decrypt` request to
AWS KMS that specifies the AWS KMS key for the cluster.

The event that records the `Decrypt` operation is similar to the following
example event. The user is the principal in your AWS account who is accessing the
cluster. The parameters include the encrypted cluster key (as a ciphertext blob) and the
encryption context that identifies the cluster. AWS KMS derives the ID of the AWS KMS key
from the ciphertext.

```
{
  "eventVersion": "1.05",
  "userIdentity": {
    "type": "AWSService",
    "invokedBy": "dsql.amazonaws.com"
  },
  "eventTime": "2018-02-14T16:42:39Z",
  "eventSource": "kms.amazonaws.com",
  "eventName": "Decrypt",
  "awsRegion": "us-east-1",
  "sourceIPAddress": "dsql.amazonaws.com",
  "userAgent": "dsql.amazonaws.com",
  "requestParameters": {
    "keyId": "arn:aws:kms:us-east-1:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab",
    "encryptionContext": {
      "aws:dsql:ClusterId": "w4abucpbwuxx"
    },
    "encryptionAlgorithm": "SYMMETRIC_DEFAULT"
  },
  "responseElements": null,
  "requestID": "11cab293-11a6-11e8-8386-13160d3e5db5",
  "eventID": "b7d16574-e887-4b5b-a064-bf92f8ec9ad3",
  "readOnly": true,
  "resources": [
    {
      "ARN": "arn:aws:kms:us-east-1:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab",
      "accountId": "AWS Internal",
      "type": "AWS::KMS::Key"
    }
  ],
  "eventType": "AwsApiCall",
  "managementEvent": true,
  "recipientAccountId": "111122223333",
  "sharedEventID": "d99f2dc5-b576-45b6-aa1d-3a3822edbeeb",
  "vpcEndpointId": "AWS Internal",
  "vpcEndpointAccountId": "vpce-1a2b3c4d5e6f1a2b3",
  "eventCategory": "Management"
}

```

## Creating an encrypted Aurora DSQL cluster

All Aurora DSQL clusters are encrypted at rest. By default, clusters use an AWS owned key at
no cost, or you can specify a custom AWS KMS key. Follow these steps to create your encrypted
cluster from either the AWS Management Console or the AWS CLI.

Console

###### To create an encrypted cluster in the AWS Management Console

1. Sign in to the AWS Management Console and open the Aurora DSQL console at [https://console.aws.amazon.com/dsql/](https://console.aws.amazon.com/dsql/ "https://console.aws.amazon.com/dsql/").
2. In the navigation pane on the left side of the console, choose
   **Clusters**.
3. Choose **Create Cluster** on the top right and select
   **Single-Region**.
4. In the **Cluster encryption settings**, choose one of the
   following options.
   - Accept the default settings to encrypt with an AWS owned key at no
     additional cost.
   - Select **Customize encryption settings (advanced)** to
     specify a custom KMS key. Then, search for or enter the ID or alias of your
     KMS key. Alternatively, choose **Create an AWS KMS key** to
     create a new key in the AWS KMS Console.

5. Choose **Create cluster**.

To confirm the encryption type for your cluster, navigate to the
**Clusters** page and select the ID of the cluster to view the
cluster details. Review the **Cluster settings** tab the
**Cluster KMS key** setting shows **Aurora DSQL default
key** for clusters that use AWS owned keys or the key ID for other
encryption types.

###### Note

If you select to own and manage your own key, make sure you set the KMS key
policy appropriately. For examples and more information, see [Key policy for a customer managed
key](#key-policy-customer-managed-key "#key-policy-customer-managed-key").

CLI

###### To create a cluster that's encrypted with the default AWS owned key

- Use the following command to create an Aurora DSQL cluster.

```
aws dsql create-cluster
```

As shown in the following encryption details, the encryption status for the cluster
is enabled by default, and the default encryption type is AWS owned key. The cluster is
now encrypted with the default AWS owned key in the Aurora DSQL service account.

```
"encryptionDetails": {
  "encryptionType" : "AWS_OWNED_KMS_KEY",
  "encryptionStatus" : "ENABLED"
}
```

###### To create a cluster that's encrypted with your customer managed key

- Use the following command to create an Aurora DSQL cluster, replacing the key ID in
  red text with the ID of your customer managed key.

```
aws dsql create-cluster \
--kms-encryption-key `d41d8cd98f00b204e9800998ecf8427e`
```

As shown in the following encryption details, the encryption status for the cluster
is enabled by default, and the encryption type is customer managed KMS key. The
cluster is now encrypted with your key.

```
"encryptionDetails": {
  "encryptionType" : "CUSTOMER_MANAGED_KMS_KEY",
  "kmsKeyArn" : "arn:aws:kms:us-east-1:111122223333:key/d41d8cd98f00b204e9800998ecf8427e",
  "encryptionStatus" : "ENABLED"
}
```

## Removing or updating a key for your Aurora DSQL cluster

You can use the AWS Management Console or the AWS CLI to update or remove the encryption keys on existing
clusters in Amazon Aurora DSQL. If you remove a key without replacing it, Aurora DSQL uses the default
AWS owned key. Follow these steps to update the encryption keys of an existing cluster from
the Aurora DSQL console or the AWS CLI.

Console

###### To update or remove an encryption key in the AWS Management Console

1. Sign in to the AWS Management Console and open the Aurora DSQL console at [https://console.aws.amazon.com/dsql/](https://console.aws.amazon.com/dsql/ "https://console.aws.amazon.com/dsql/").
2. In the navigation pane on the left side of the console, choose
   **Clusters**.
3. From the list view, find and select row of the cluster that you want to
   update.
4. Select the **Actions** menu and then choose
   **Modify**.
5. In the **Cluster encryption settings**, choose one of the
   following options to modify your encryption settings.
   - If you want to switch from a custom key to an AWS owned key, de-select the
     **Customize encryption settings (advanced)** option. The
     default settings will apply and encrypt your cluster with an AWS owned key at
     no cost.
   - If you want to switch from one custom KMS key to another or from an
     AWS owned key to a KMS key, select the **Customize encryption
     settings (advanced)** option if it's not already selected. Then,
     search for and select the ID or alias of the key you want to use. Alternatively,
     choose **Create an AWS KMS key** to create a new key in the AWS KMS
     Console.

6. Choose **Save**.

CLI
The following examples show how to use the AWS CLI to update an encrypted
cluster.

To update an encrypted cluster with the default AWS owned key

```

aws dsql update-cluster \
--identifier aiabtx6icfp6d53snkhseduiqq \
--kms-encryption-key "AWS_OWNED_KMS_KEY"

```

The `EncryptionStatus` of the cluster description is set to
`ENABLED` and the `EncryptionType` is
`AWS_OWNED_KMS_KEY`.

```

"encryptionDetails": {
  "encryptionType" : "AWS_OWNED_KMS_KEY",
  "encryptionStatus" : "ENABLED"
}

```

This cluster is now encrypted using the default AWS owned key in the Aurora DSQL
service account.

To update an encrypted cluster with a customer managed key for Aurora DSQL

Update the encrypted cluster, as in the following example:

```

aws dsql update-cluster \
--identifier aiabtx6icfp6d53snkhseduiqq \
--kms-encryption-key arn:aws:kms:us-east-1:123456789012:key/abcd1234-abcd-1234-a123-ab1234a1b234

```

The `EncryptionStatus` of the cluster description transitions to
`UPDATING` and the `EncryptionType` is
`CUSTOMER_MANAGED_KMS_KEY`. After Aurora DSQL finishes propagating the new key
through the platform, the encryption status will be transitioned to
`ENABLED`

```
"encryptionDetails": {
  "encryptionType" : "CUSTOMER_MANAGED_KMS_KEY",
  "kmsKeyArn" : "arn:aws:us-east-1:kms:key/abcd1234-abcd-1234-a123-ab1234a1b234",
  "encryptionStatus" : "ENABLED"
}

```

###### Note

If you select to own and manage your own key, make sure you set the KMS key policy
appropriately. For examples and more information, see [Key policy for a customer managed
key](#key-policy-customer-managed-key "#key-policy-customer-managed-key").

## Considerations for encryption with

Aurora DSQL

- Aurora DSQL encrypts all cluster data at rest. You can't disable this encryption or encrypt
  only some items in a cluster.
- AWS Backup encrypts your backups and any clusters restored from these backups. You can
  encrypt your backup data in AWS Backup using either the AWS owned key or a customer managed
  key.
- The following data protection states are enabled for Aurora DSQL:
  - Data at rest - Aurora DSQL encrypts all static data on
    persistent storage media
  - Data in transit - Aurora DSQL encrypts all
    communications using Transport Layer Security (TLS) by default

- When you transition to a different key, we recommend that you keep the original key
  enabled until the transition is complete. AWS needs the original key to decrypt data
  before it encrypts your data with the new key. The process is complete when the cluster's
  `encryptionStatus` is `ENABLED` and you see the
  `kmsKeyArn` of the new customer managed key.
- When you disable your Customer Managed Key or revoke access for Aurora DSQL to use your
  key, your cluster will go into `IDLE` state.
- The AWS Management Console and Amazon Aurora DSQL API use different terms for encryption types:
  - AWS Console – In the console, you'll see `KMS` when using a
    Customer managed key and `DEFAULT` when using an AWS owned key.
  - API – The Amazon Aurora DSQL API uses `CUSTOMER_MANAGED_KMS_KEY` for
    customer managed keys, and `AWS_OWNED_KMS_KEY` for AWS owned keys.

- If you don't specify an encryption key during cluster creation, Aurora DSQL automatically
  encrypts your data using the AWS owned key.
- You can switch between an AWS owned key and a Customer managed key at any time. Make
  this change using the AWS Management Console, AWS CLI, or the Amazon Aurora DSQL API.
