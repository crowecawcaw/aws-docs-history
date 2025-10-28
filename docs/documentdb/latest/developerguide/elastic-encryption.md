# Data encryption at rest for Amazon DocumentDB elastic clusters

The following topics help you learn about, create, and monitor AWS Key Management Service encryption keys for Amazon DocumentDB elastic clusters:

###### Topics

- [How Amazon DocumentDB elastic clusters use grants in AWS KMS](#ec-encrypt-grants "#ec-encrypt-grants")
- [Create a customer managed key](#ec-encrypt-create "#ec-encrypt-create")
- [Monitoring your encryption keys for Amazon DocumentDB elastic clusters](#ec-encrypt-monitor "#ec-encrypt-monitor")
- [Learn more](#ec-encrypt-learn "#ec-encrypt-learn")
  Amazon DocumentDB elastic clusters automatically integrate with AWS Key Management Service (AWS KMS) for key management and uses a method known as envelope encryption to protect your data.
  For more information about envelope encryption, see [Envelope encryption](../../../kms/latest/developerguide/concepts.md#enveloping "../../../kms/latest/developerguide/concepts.md#enveloping") in the _AWS Key Management Service Developer Guide_.

An AWS KMS key is a logical representation of a key.
The KMS key includes metadata, such as the key ID, creation date, description, and key state.
The KMS key also contains the key material used to encrypt and decrypt data.
For more information about KMS keys, see [AWS KMS keys](../../../kms/latest/developerguide/concepts.md#kms_keys "../../../kms/latest/developerguide/concepts.md#kms_keys") in the _AWS Key Management Service Developer Guide_.

Amazon DocumentDB elastic clusters support encryption with two types of keys:

- **AWS owned keys —** Amazon DocumentDB elastic clusters use these keys by default to automatically encrypt personally identifiable data.
  You can't view, manage, or use AWS-owned keys, or audit their use.
  However, you don't have to take any action or change any programs to protect the keys that encrypt your data.
  For more information, see [AWS owned keys](../../../kms/latest/developerguide/concepts.md#aws-owned-cmk "../../../kms/latest/developerguide/concepts.md#aws-owned-cmk") in the _AWS Key Management Service Developer Guide_.
- **Customer-managed keys —** Symmetric AWS KMS keys that you create, own, and manage.
  Because you have full control of this layer of encryption, you can perform such tasks as:

      + Establishing and maintaining key policies
      + Establishing and maintaining IAM policies and grants
      + Enabling and disabling key policies
      + Rotating key cryptographic material
      + Adding tags
      + Creating key aliases
      + Scheduling keys for deletion

  For more information, see [Customer managed keys](../../../kms/latest/developerguide/concepts.md#customer-cmk "../../../kms/latest/developerguide/concepts.md#customer-cmk") in the _AWS Key Management Service Developer Guide_.

###### Important

You must use a symmetric encryption KMS key to encrypt your cluster as Amazon DocumentDB supports only symmetric encryption KMS keys.
Do not use an asymmetric KMS key to attempt to encrypt the data in your Amazon DocumentDB elastic clusters.
For more information, see [Asymmetric keys in AWS KMS](../../../kms/latest/developerguide/symmetric-asymmetric.md "../../../kms/latest/developerguide/symmetric-asymmetric.md") in the _AWS Key Management Service Developer Guide_.

If Amazon DocumentDB can no longer gain access to the encryption key for a cluster — for example, when access to a key is revoked — the encrypted cluster goes into a terminal state.
In this case, you can only restore the cluster from a backup. For Amazon DocumentDB, backups are always enabled for 1 day.
In addition, if you disable the key for an encrypted Amazon DocumentDB cluster, you will eventually lose read and write access to that cluster.
When Amazon DocumentDB encounters a cluster that is encrypted by a key that it doesn't have access to, it puts the cluster into a terminal state.
In this state, the cluster is no longer available, and the current state of the database can't be recovered.
To restore the cluster, you must re-enable access to the encryption key for Amazon DocumentDB, and then restore the cluster from a backup.

###### Important

You cannot change the KMS key for an encrypted cluster after you have already created it.
Be sure to determine your encryption key requirements before you create your encrypted elastic cluster.

## How Amazon DocumentDB elastic clusters use grants in AWS KMS

Amazon DocumentDB elastic clusters require a [grant](../../../kms/latest/developerguide/grants.md "../../../kms/latest/developerguide/grants.md") to use your customer managed key.

When you create a cluster encrypted with a customer managed key, Amazon DocumentDB elastic clusters create a grant on your behalf by sending a `CreateGrant` request to AWS KMS.
Grants in AWS KMS are used to give Amazon DocumentDB elastic clusters access to a KMS key in a customer account.

Amazon DocumentDB elastic clusters require the grant to use your customer managed key for the following internal operations:

- Send `DescribeKey` requests to AWS KMS to verify that the symmetric customer managed KMS key ID, entered when creating a tracker or geofence collection, is valid.
- Send `GenerateDataKey` requests to AWS KMS to generate data keys encrypted by your customer managed key.
- Send `Decrypt` requests to AWS KMS to decrypt the encrypted data keys so that they can be used to encrypt your data.
- You can revoke access to the grant, or remove the service's access to the customer managed key at any time.
  If you do, Amazon DocumentDB elastic clusters won't be able to access any of the data encrypted by the customer managed key, which affects operations that are dependent on that data.

## Create a customer managed key

You can create a symmetric customer managed key by using the AWS Management Console or the AWS KMS API.

**Symmetric customer managed key creation**

Follow the steps for [Creating symmetric customer managed key](../../../kms/latest/developerguide/create-keys.md "../../../kms/latest/developerguide/create-keys.md") in the _AWS Key Management Service Developer Guide_.

**Key policy**

Key policies control access to your customer managed key.
Every customer managed key must have exactly one key policy, which contains statements that determine who can use the key and how they can use it.
When you create your customer managed key, you can specify a key policy.
For more information, see the KMS key access information located in the [AWS Key Management Service overview](../../../kms/latest/developerguide/overview.md "../../../kms/latest/developerguide/overview.md") of the _AWS Key Management Service Developer Guide_.

To use your customer managed key with Amazon DocumentDB elastic cluster resources, the following API operations must be permitted in the key policy:

- [`kms:CreateGrant`](../../../kms/latest/APIReference/API_CreateGrant.md "../../../kms/latest/APIReference/API_CreateGrant.md") – Adds a grant to a customer managed key.
  Grants control access to a specified KMS key, which allows access to grant operations Amazon Location Service requires.
  For more information about using grants, see [Grants in AWS KMS](../../../kms/latest/developerguide/grants.md "../../../kms/latest/developerguide/grants.md") in the _AWS Key Management Service Developer Guide_.
- [`kms:DescribeKey`](../../../kms/latest/APIReference/API_DescribeKey.md "../../../kms/latest/APIReference/API_DescribeKey.md") – Provides the customer managed key details to allow Docdb Elastic to validate the key.
- [`kms:Decrypt`](../../../kms/latest/APIReference/API_Decrypt.md "../../../kms/latest/APIReference/API_Decrypt.md") – Allows Docdb Elastic to use the stored encrypted data key to access encrypted data.
- [`kms:GenerateDataKey`](../../../kms/latest/APIReference/API_GenerateDataKey.md "../../../kms/latest/APIReference/API_GenerateDataKey.md") – Allows Docdb Elastic to generate an encrypted data key and store it because the data key isn't immediately used to encrypt.

For more information, see [Permissions for AWS services in key policies](../../../kms/latest/developerguide/key-policy-services.md "../../../kms/latest/developerguide/key-policy-services.md") and [Troubleshooting key access](../../../kms/latest/developerguide/policy-evaluation.md "../../../kms/latest/developerguide/policy-evaluation.md") in the _AWS Key Management Service Developer Guide_.

**Restricting customer managed key access via IAM policies**

In addition to KMS key policies, you can also restrict KMS key permissions in an IAM policy.

You can make the IAM policy stricter in various ways.
For example, to allow the customer managed key to be used only for requests that originate in Amazon DocumentDB elastic clusters, you can use the [`kms:ViaService` condition key](../../../kms/latest/developerguide/policy-conditions.md#conditions-kms-via-service "../../../kms/latest/developerguide/policy-conditions.md#conditions-kms-via-service") with the `docdb-elastic.<region-name>.amazonaws.com` value.

For more information, see [Allowing users in other accounts to use a KMS key](../../../kms/latest/developerguide/key-policy-modifying-external-accounts.md "../../../kms/latest/developerguide/key-policy-modifying-external-accounts.md") in the _AWS Key Management Service Developer Guide_.

## Monitoring your encryption keys for Amazon DocumentDB elastic clusters

When you use an AWS KMS key customer managed key with your Docdb Elastic resources, you can use AWS CloudTrail or Amazon CloudWatch Logs to track requests that Docdb Elastic sends to AWS KMS.

The following examples are AWS CloudTrail events for `CreateGrant`, `GenerateDataKeyWithoutPlainText`, `Decrypt`, and `DescribeKey` to monitor AWS KMS key operations called by Amazon DocumentDB elastic clusters to access data encrypted by your customer managed key:

CreateGrant

```
{
    "eventVersion": "1.08",
    "userIdentity": {
        "type": "AssumedRole",
        "principalId": "AROAIGDTESTANDEXAMPLE:Sampleuser01",
        "arn": "arn:aws:sts::111122223333:assumed-role/Admin/Sampleuser01",
        "accountId": "111122223333",
        "accessKeyId": "AKIAIOSFODNN7EXAMPLE3",
        "sessionContext": {
            "sessionIssuer": {
                "type": "Role",
                "principalId": "AROAIGDTESTANDEXAMPLE",
                "arn": "arn:aws:iam::111122223333:assumed-role/Admin/Sampleuser01",
                "accountId": "111122223333",
                "userName": "Sampleuser01"
            },
            "webIdFederationData": {},
            "attributes": {
                "creationDate": "2023-05-09T23:04:20Z",
                "mfaAuthenticated": "false"
            }
        },
        "invokedBy": "docdb-elastic.amazonaws.com"
    },
    "eventTime": "2023-05-09T23:55:48Z",
    "eventSource": "kms.amazonaws.com",
    "eventName": "CreateGrant",
    "awsRegion": "us-east-1",
    "sourceIPAddress": "docdb-elastic.amazonaws.com",
    "userAgent": "docdb-elastic.amazonaws.com",
    "requestParameters": {
        "retiringPrincipal": "docdb-elastic.us-east-1.amazonaws.com",
        "granteePrincipal": "docdb-elastic.us-east-1.amazonaws.com",
        "operations": [
            "Decrypt",
            "Encrypt",
            "GenerateDataKey",
            "GenerateDataKeyWithoutPlaintext",
            "ReEncryptFrom",
            "ReEncryptTo",
            "CreateGrant",
            "RetireGrant",
            "DescribeKey"
        ],
        "keyId": "arn:aws:kms:us-east-1:111122223333:key/1234abcd-12ab-34cd-56ef-123456SAMPLE"
    },
    "responseElements": {
        "grantId": "0ab0ac0d0b000f00ea00cc0a0e00fc00bce000c000f0000000c0bc0a0000aaafSAMPLE",
        "keyId": "arn:aws:kms:us-east-1:111122223333:key/1234abcd-12ab-34cd-56ef-123456SAMPLE"
    },
    "requestID": "ff000af-00eb-00ce-0e00-ea000fb0fba0SAMPLE",
    "eventID": "ff000af-00eb-00ce-0e00-ea000fb0fba0SAMPLE",
    "readOnly": false,
    "resources": [
        {
            "accountId": "AWS Internal",
            "type": "AWS::KMS::Key",
            "ARN": "arn:aws:kms:us-east-1:111122223333:key/1234abcd-12ab-34cd-56ef-123456SAMPLE"
        }
    ],
    "eventType": "AwsApiCall",
    "managementEvent": true,
    "recipientAccountId": "111122223333",
    "eventCategory": "Management"
}
```

GenerateDataKey

```
{
    "eventVersion": "1.08",
    "userIdentity": {
        "type": "AssumedRole",
        "principalId": "AROAIGDTESTANDEXAMPLE:Sampleuser01",
        "arn": "arn:aws:sts::111122223333:assumed-role/Admin/Sampleuser01",
        "accountId": "111122223333",
        "accessKeyId": "AKIAIOSFODNN7EXAMPLE3",
        "sessionContext": {
            "sessionIssuer": {
                "type": "Role",
                "principalId": "AROAIGDTESTANDEXAMPLE",
                "arn": "arn:aws:iam::111122223333:assumed-role/Admin/Sampleuser01",
                "accountId": "111122223333",
                "userName": "Sampleuser01"
            },
            "webIdFederationData": {},
            "attributes": {
                "creationDate": "2023-05-10T18:02:59Z",
                "mfaAuthenticated": "false"
            }
        },
        "invokedBy": "docdb-elastic.amazonaws.com"
    },
    "eventTime": "2023-05-10T18:03:25Z",
    "eventSource": "kms.amazonaws.com",
    "eventName": "GenerateDataKey",
    "awsRegion": "us-east-1",
    "sourceIPAddress": "docdb-elastic.amazonaws.com",
    "userAgent": "docdb-elastic.amazonaws.com",
    "requestParameters": {
        "keySpec": "AES_256",
        "keyId": "arn:aws:kms:us-east-1:111122223333:key/1234abcd-12ab-34cd-56ef-123456SAMPLE"
    },
    "responseElements": null,
    "requestID": "ff000af-00eb-00ce-0e00-ea000fb0fba0SAMPLE",
    "eventID": "ff000af-00eb-00ce-0e00-ea000fb0fba0SAMPLE",
    "readOnly": true,
    "resources": [
        {
            "accountId": "AWS Internal",
            "type": "AWS::KMS::Key",
            "ARN": "arn:aws:kms:us-east-1:111122223333:key/1234abcd-12ab-34cd-56ef-123456SAMPLE"
        }
    ],
    "eventType": "AwsApiCall",
    "managementEvent": true,
    "recipientAccountId": "111122223333",
    "eventCategory": "Management"
}
```

Decrypt

```
{
    "eventVersion": "1.08",
    "userIdentity": {
        "type": "AssumedRole",
        "principalId": "AROAIGDTESTANDEXAMPLE:Sampleuser01",
        "arn": "arn:aws:sts::111122223333:assumed-role/Admin/Sampleuser01",
        "accountId": "111122223333",
        "accessKeyId": "AKIAIOSFODNN7EXAMPLE3",
        "sessionContext": {
            "sessionIssuer": {
                "type": "Role",
                "principalId": "AROAIGDTESTANDEXAMPLE",
                "arn": "arn:aws:iam::111122223333:assumed-role/Admin/Sampleuser01",
                "accountId": "111122223333",
                "userName": "Sampleuser01"
            },
            "webIdFederationData": {},
            "attributes": {
                "creationDate": "2023-05-10T18:05:49Z",
                "mfaAuthenticated": "false"
            }
        },
        "invokedBy": "docdb-elastic.amazonaws.com"
    },
    "eventTime": "2023-05-10T18:06:19Z",
    "eventSource": "kms.amazonaws.com",
    "eventName": "Decrypt",
    "awsRegion": "us-east-1",
    "sourceIPAddress": "docdb-elastic.amazonaws.com",
    "userAgent": "docdb-elastic.amazonaws.com",
    "requestParameters": {
        "encryptionAlgorithm": "SYMMETRIC_DEFAULT"
    },
    "responseElements": null,
    "requestID": "ff000af-00eb-00ce-0e00-ea000fb0fba0SAMPLE",
    "eventID": "ff000af-00eb-00ce-0e00-ea000fb0fba0SAMPLE",
    "readOnly": true,
    "resources": [
        {
            "accountId": "AWS Internal",
            "type": "AWS::KMS::Key",
            "ARN": "arn:aws:kms:us-east-1:111122223333:key/1234abcd-12ab-34cd-56ef-123456SAMPLE"
        }
    ],
    "eventType": "AwsApiCall",
    "managementEvent": true,
    "recipientAccountId": "111122223333",
    "eventCategory": "Management"
}
```

DescribeKey

```
{
    "eventVersion": "1.08",
    "userIdentity": {
        "type": "AssumedRole",
        "principalId": "AROAIGDTESTANDEXAMPLE:Sampleuser01",
        "arn": "arn:aws:sts::111122223333:assumed-role/Admin/Sampleuser01",
        "accountId": "111122223333",
        "accessKeyId": "AKIAIOSFODNN7EXAMPLE3",
        "sessionContext": {
            "sessionIssuer": {
                "type": "Role",
                "principalId": "AROAIGDTESTANDEXAMPLE",
                "arn": "arn:aws:iam::111122223333:assumed-role/Admin/Sampleuser01",
                "accountId": "111122223333",
                "userName": "Sampleuser01"
            },
            "webIdFederationData": {},
            "attributes": {
                "creationDate": "2023-05-09T23:04:20Z",
                "mfaAuthenticated": "false"
            }
        },
        "invokedBy": "docdb-elastic.amazonaws.com"
    },
    "eventTime": "2023-05-09T23:55:48Z",
    "eventSource": "kms.amazonaws.com",
    "eventName": "DescribeKey",
    "awsRegion": "us-east-1",
    "sourceIPAddress": "docdb-elastic.amazonaws.com",
    "userAgent": "docdb-elastic.amazonaws.com",
    "requestParameters": {
        "keyId": "alias/SampleKmsKey"
    },
    "responseElements": null,
    "requestID": "ff000af-00eb-00ce-0e00-ea000fb0fba0SAMPLE",
    "eventID": "ff000af-00eb-00ce-0e00-ea000fb0fba0SAMPLE",
    "readOnly": true,
    "resources": [
        {
            "accountId": "AWS Internal",
            "type": "AWS::KMS::Key",
            "ARN": "arn:aws:kms:us-east-1:111122223333:key/1234abcd-12ab-34cd-56ef-123456SAMPLE"
        }
    ],
    "eventType": "AwsApiCall",
    "managementEvent": true,
    "recipientAccountId": "111122223333",
    "eventCategory": "Management"
}
```

## Learn more

The following resources provide more information about data encryption at rest:

- For more information about AWS KMS concepts, see [AWS Key Management Service basic concepts](../../../kms/latest/developerguide/concepts.md "../../../kms/latest/developerguide/concepts.md") in the _AWS Key Management Service Developer Guide_.
- For more information about AWS KMS security, see [Security best practices for AWS Key Management Service](../../../kms/latest/developerguide/best-practices.md "../../../kms/latest/developerguide/best-practices.md") in the _AWS Key Management Service Developer Guide_.
