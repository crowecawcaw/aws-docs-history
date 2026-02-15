# Data encryption at rest for Amazon SES

By default, Amazon SES encrypts all data at rest. Encryption by default helps reduce the
operational overhead and complexity involved in protecting data. Encryption also enables you
to create Mail Manager archives that meet strict encryption compliance and regulatory
requirements.

SES provides the following encryption options:

- **AWS owned keys** – SES uses these by
  default. You can't view, manage, or use AWS owned keys, or audit their use. However, you
  don't have to take any action or change any programs to protect the keys that encrypt your
  data. For more information, see [AWS owned keys](../../../kms/latest/developerguide/concepts.md#aws-owned-cmk "../../../kms/latest/developerguide/concepts.md#aws-owned-cmk") in
  the _AWS Key Management Service Developer Guide_.
- **Customer managed keys** – SES supports
  the use of symmetric customer managed keys that you create, own, and manage. Because you have full
  control of the encryption, you can perform such tasks as:

      + Establishing and maintaining key policies
      + Establishing and maintaining IAM policies and grants
      + Enabling and disabling key policies
      + Rotating key cryptographic material
      + Adding tags
      + Creating key aliases
      + Scheduling keys for deletion

  To use your own key, choose a customer managed key when you create your SES
  resources.

For more information, see [Customer managed keys](../../../kms/latest/developerguide/concepts.md#customer-cmk "../../../kms/latest/developerguide/concepts.md#customer-cmk")
in the _AWS Key Management Service Developer Guide_.

###### Note

SES automatically enables encryption at rest using AWS owned keys at no charge.

However, AWS KMS charges apply for using a customer managed key. For more information about pricing,
see the [AWS Key Management Service pricing](https://aws.amazon.com/kms/pricing/ "https://aws.amazon.com/kms/pricing/").

## Create a customer managed key

You can create a symmetric customer managed key by using the AWS Management Console, or the AWS KMS APIs.

**To create a symmetric customer managed key**

Follow the steps for [Creating symmetric
encryption KMS keys](../../../kms/latest/developerguide/create-keys.md#create-symmetric-cmk "../../../kms/latest/developerguide/create-keys.md#create-symmetric-cmk") in the _AWS Key Management Service Developer
Guide_.

###### Note

For archiving, your key must meet the following requirements:

- The key must be symmetric.
- The key material origin must be `AWS_KMS`.
- The key usage must be `ENCRYPT_DECRYPT`.

**Key policy**

Key policies control access to your customer managed key. Every customer managed key must have exactly one key
policy, which contains statements that determine who can use the key and how they can use
it. When you create your customer managed key, you can specify a key policy. For more information, see
[Managing
access to customer managed keys](../../../kms/latest/developerguide/control-access-overview.md#managing-access "../../../kms/latest/developerguide/control-access-overview.md#managing-access") in the _AWS Key Management Service Developer
Guide_.

To use your customer managed key with Mail Manager archiving, your key policy must permit the following API
operations:

- [kms:DescribeKey](../../../kms/latest/APIReference/API_DescribeKey.md "../../../kms/latest/APIReference/API_DescribeKey.md") – Provides the customer managed key details that allow
  SES to validate the key.
- [kms:GenerateDataKey](../../../kms/latest/APIReference/API_GenerateDataKey.md "../../../kms/latest/APIReference/API_GenerateDataKey.md") – Allows SES to generate a data key for
  encrypting data at rest.
- [kms:Decrypt](../../../kms/latest/APIReference/API_Decrypt.md "../../../kms/latest/APIReference/API_Decrypt.md") – Allows SES to decrypt stored data before
  returning it to API clients.

The following example shows a typical key policy:

```
{
            "Sid": "Allow SES to encrypt/decrypt",
            "Effect": "Allow",
            "Principal": {
                "Service": "ses.amazonaws.com"
            },
            "Action": [
                "kms:GenerateDataKey",
                "kms:Decrypt",
                "kms:DescribeKey"
            ],
            "Resource": "*"
        },
```

For more information, see [specifying permissions in a policy](../../../kms/latest/developerguide/control-access-overview.md#overview-policy-elements "../../../kms/latest/developerguide/control-access-overview.md#overview-policy-elements"), in the _AWS Key Management Service
Developer Guide_.

For more information about troubleshooting, see [troubleshooting key access](../../../kms/latest/developerguide/policy-evaluation.md#example-no-iam "../../../kms/latest/developerguide/policy-evaluation.md#example-no-iam"), in the _AWS Key Management Service Developer
Guide_.

## Specifying a customer managed key for Mail Manager archiving

You can specify a customer managed key as an alternative to using AWS owned keys.
When you create an archive, you can specify the data key by
entering a **KMS key ARN**, which Mail Manager archiving uses to
encrypt all customer data in the archive.

- **KMS key ARN** – A [key identifier](../../../kms/latest/developerguide/concepts.md#key-id "../../../kms/latest/developerguide/concepts.md#key-id") for an
  AWS KMS customer managed key. Enter a key ID, key ARN, alias name, or alias ARN.

## Amazon SES encryption context

An [encryption context](../../../kms/latest/developerguide/concepts.md#encrypt_context "../../../kms/latest/developerguide/concepts.md#encrypt_context")
is an optional set of key-value pairs that contain additional contextual information about
the data.

AWS KMS uses the encryption context as additional authenticated data to support
authenticated encryption. When you include an
encryption context in a request to encrypt data, AWS KMS binds the encryption context to the
encrypted data. To decrypt data, you include the same encryption context in the
request.

###### Note

Amazon SES doesn't support encryption contexts for archive creation. Instead, you use an
IAM or KMS policy. For example policies, see [Archive creation policies](#archive-creation-policies "#archive-creation-policies"), later in this section.

**Amazon SES encryption context**

SES uses the same encryption context in all AWS KMS cryptographic operations,
where the key is `aws:ses:arn` and the value is the resource [Amazon
Resource Name](../../../general/latest/gr/aws-arns-and-namespaces.md "../../../general/latest/gr/aws-arns-and-namespaces.md") (ARN).

###### Example

```
"encryptionContext": {
    "aws:ses:arn": "arn:aws:ses:us-west-2:111122223333:ExampleResourceName/ExampleResourceID"
}
```

**Using encryption context for monitoring**

When you use a symmetric customer managed key to encrypt your SES resource, you can also use
the encryption context in audit records and logs to identify how the customer managed key is being
used. The encryption context also appears in [logs
generated by AWS CloudTrail or Amazon CloudWatch Logs](#example-custom-encryption "#example-custom-encryption").

**Using encryption context to control access to your
customer managed key**

You can use the encryption context in key policies and IAM policies as
`conditions` to control access to your symmetric customer managed key. You can also use
encryption context constraints in a grant.

SES uses an encryption context constraint in grants to control access to the
customer managed key in your account or region. The grant constraint requires that the operations that
the grant allows use the specified encryption context.

###### Example

The following are example key policy statements to grant access to a customer managed key for a
specific encryption context. The condition in this policy statement requires that the
grants have an encryption context constraint that specifies the encryption context.

```
{
    "Sid": "Enable DescribeKey",
    "Effect": "Allow",
    "Principal": {
        "AWS": "arn:aws:iam::111122223333:role/ExampleReadOnlyRole"
     },
     "Action": "kms:DescribeKey",
     "Resource": "*"
},
{
     "Sid": "Enable CreateGrant",
     "Effect": "Allow",
     "Principal": {
         "AWS": "arn:aws:iam::111122223333:role/ExampleReadOnlyRole"
     },
     "Action": "kms:CreateGrant",
     "Resource": "*",
     "Condition": {
         "StringEquals": {
             "kms:EncryptionContext:aws:ses:arn": "arn:aws:ses:us-west-2:111122223333:ExampleResourceName/ExampleResourceID"
          }
     }
}
```

## Archive creation policies

The following example policies show how to enable archive creation. The policies work on
all assets.

**IAM policy**

```
{
            "Sid": "VisualEditor0",
            "Effect": "Allow",
            "Action": "ses:CreateArchive",
            "Resource": [
                "*"
            ]
        },
        {
            "Effect": "Allow",
            "Action": [
                "kms:DescribeKey",
                "kms:GenerateDataKey",
                "kms:Decrypt"
            ],
            "Resource": "*",
            "Condition": {
                "StringEquals": {
                    "kms:ViaService": "ses.us-east-1.amazonaws.com",
                    "kms:CallerAccount": "012345678910"
                }
            }
        }
```

**AWS KMS policy**

```
{
            "Sid": "Allow SES to encrypt/decrypt",
            "Effect": "Allow",
            "Principal": {
                "Service": "ses.amazonaws.com"
            },
            "Action": [
                "kms:GenerateDataKey",
                "kms:Decrypt",
                "kms:DescribeKey"
            ],
            "Resource": "*"
        },
```

## Monitoring your encryption keys for

Amazon SES

When you use an AWS KMS customer managed key with your Amazon SES resources, you can use [AWS CloudTrail](../../../awscloudtrail/latest/userguide/cloudtrail-user-guide.md "../../../awscloudtrail/latest/userguide/cloudtrail-user-guide.md") or [Amazon CloudWatch Logs](../../../AmazonCloudWatch/latest/logs/WhatIsCloudWatchLogs.md "../../../AmazonCloudWatch/latest/logs/WhatIsCloudWatchLogs.md") to track
requests that SES sends to AWS KMS.

The following examples are AWS CloudTrail events for
`GenerateDataKey`, `Decrypt`, and `DescribeKey` to monitor
KMS operations called by SES to access data encrypted by your customer managed key:

GenerateDataKey
When you enable an AWS KMS customer managed key for your resource, SES creates a unique
table key. It sends a `GenerateDataKey` request to AWS KMS that specifies the
AWS KMScustomer managed key for the resource.

When you enable an AWS KMS customer managed key for your Mail Manager archive resource, it will use
`GenerateDataKey` when encrypting archive data at rest.

The following example event records the `GenerateDataKey`
operation:

```
{
    "eventVersion": "1.08",
    "userIdentity": {
        "type": "AWSService",
        "invokedBy": "ses.amazonaws.com"
    },
    "eventTime": "2021-04-22T17:07:02Z",
    "eventSource": "kms.amazonaws.com",
    "eventName": "GenerateDataKey",
    "awsRegion": "us-west-2",
    "sourceIPAddress": "172.12.34.56",
    "userAgent": "ExampleDesktop/1.0 (V1; OS)",
    "requestParameters": {
        "encryptionContext": {
            "aws:ses:arn": "arn:aws:ses:us-west-2:111122223333:ExampleResourceName/ExampleResourceID"
        },
        "keySpec": "AES_256",
        "keyId": "arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-123456SAMPLE"
    },
    "responseElements": null,
    "requestID": "ff000af-00eb-00ce-0e00-ea000fb0fba0SAMPLE",
    "eventID": "ff000af-00eb-00ce-0e00-ea000fb0fba0SAMPLE",
    "readOnly": true,
    "resources": [
        {
            "accountId": "111122223333",
            "type": "AWS::KMS::Key",
            "ARN": "arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-123456SAMPLE"
        }
    ],
    "eventType": "AwsApiCall",
    "managementEvent": true,
    "eventCategory": "Management",
    "recipientAccountId": "111122223333",
    "sharedEventID": "57f5dbee-16da-413e-979f-2c4c6663475e"
}
```

Decrypt
When you access an encrypted resource, SES calls the `Decrypt`
operation to use the stored encrypted data key to access the encrypted data.

The following example event records the `Decrypt` operation:

```
{
    "eventVersion": "1.08",
    "userIdentity": {
        "type": "AWSService",
        "invokedBy": "ses.amazonaws.com"
    },
    "eventTime": "2021-04-22T17:10:51Z",
    "eventSource": "kms.amazonaws.com",
    "eventName": "Decrypt",
    "awsRegion": "us-west-2",
    "sourceIPAddress": "172.12.34.56",
    "userAgent": "ExampleDesktop/1.0 (V1; OS)",
    "requestParameters": {
        "encryptionContext": {
            "aws:ses:arn": "arn:aws:ses:us-west-2:111122223333:ExampleResourceName/ExampleResourceID"
        },
        "keyId": "arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-123456SAMPLE",
        "encryptionAlgorithm": "SYMMETRIC_DEFAULT"
    },
    "responseElements": null,
    "requestID": "ff000af-00eb-00ce-0e00-ea000fb0fba0SAMPLE",
    "eventID": "ff000af-00eb-00ce-0e00-ea000fb0fba0SAMPLE",
    "readOnly": true,
    "resources": [
        {
            "accountId": "111122223333",
            "type": "AWS::KMS::Key",
            "ARN": "arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-123456SAMPLE"
        }
    ],
    "eventType": "AwsApiCall",
    "managementEvent": true,
    "eventCategory": "Management",
    "recipientAccountId": "111122223333",
    "sharedEventID": "dc129381-1d94-49bd-b522-f56a3482d088"
}
```

DescribeKey
SES uses the `DescribeKey` operation to verify if the AWS KMS
customer managed key associated with your resource exists in the account and region.

The following example event records the `DescribeKey` operation:

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
                "principalId": "AROAIGDTESTANDEXAMPLE:Sampleuser01",
                "arn": "arn:aws:sts::111122223333:assumed-role/Admin/Sampleuser01",
                "accountId": "111122223333",
                "userName": "Admin"
            },
            "webIdFederationData": {},
            "attributes": {
                "mfaAuthenticated": "false",
                "creationDate": "2021-04-22T17:02:00Z"
            }
        },
        "invokedBy": "ses.amazonaws.com"
    },
    "eventTime": "2021-04-22T17:07:02Z",
    "eventSource": "kms.amazonaws.com",
    "eventName": "DescribeKey",
    "awsRegion": "us-west-2",
    "sourceIPAddress": "172.12.34.56",
    "userAgent": "ExampleDesktop/1.0 (V1; OS)",
    "requestParameters": {
        "keyId": "00dd0db0-0000-0000-ac00-b0c000SAMPLE"
    },
    "responseElements": null,
    "requestID": "ff000af-00eb-00ce-0e00-ea000fb0fba0SAMPLE",
    "eventID": "ff000af-00eb-00ce-0e00-ea000fb0fba0SAMPLE",
    "readOnly": true,
    "resources": [
        {
            "accountId": "111122223333",
            "type": "AWS::KMS::Key",
            "ARN": "arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-123456SAMPLE"
        }
    ],
    "eventType": "AwsApiCall",
    "managementEvent": true,
    "eventCategory": "Management",
    "recipientAccountId": "111122223333"
}
```

## Learn more

The following resources provide more information about data encryption at rest.

- For more information about [AWS Key Management Service basic concepts](../../../kms/latest/developerguide/concepts.md "../../../kms/latest/developerguide/concepts.md"), see
  the _AWS Key Management Service Developer Guide_.
- For more information about [Security best practices for
  AWS Key Management Service](../../../kms/latest/developerguide/best-practices.md "../../../kms/latest/developerguide/best-practices.md"), see the _AWS Key Management Service Developer
  Guide_.
