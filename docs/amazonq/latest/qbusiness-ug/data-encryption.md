# Data encryption for Amazon Q Business

Amazon Q Business supports encryption at rest using a customer supplied symmetric
AWS KMS key when provided, or uses an AWS-owned AWS KMS key if no customer managed key is
provided. Amazon Q Business also uses HTTPS protocol for data in transit.

###### Important

Amazon Q does not support asymmetric KMS keys. For more information, see [Using Symmetric and Asymmetric Keys](../../../kms/latest/developerguide/symmetric-asymmetric.md "../../../kms/latest/developerguide/symmetric-asymmetric.md")
in the _AWS Key Management Service Developer Guide_.

###### Topics

- [Encryption at rest](#encryption-rest "#encryption-rest")
- [Encryption in transit](#encryption-transit "#encryption-transit")

## Encryption at rest

Amazon Q Business provides encryption by default to protect sensitive customer
data at rest using AWS owned encryption keys. Sensitive customer data includes both
questions and answers in the Amazon Q Business web experience and the documents
uploaded to Amazon Q Business index.

The Amazon Q Business uses the questions and answers to know the conversation
context and to provide you with the best answer. The conversation data is automatically
removed once the conversation is deleted or is inactive. For more information, see [Conversation management](using-web-experience.md#conversation-mgmt "using-web-experience.md#conversation-mgmt"). The uploaded documents
are used by Amazon Q Business to retrieve them at runtime to answer your
questions.

- **AWS owned keys** – Amazon Q Business
  uses these keys by default to automatically encrypt sensitive customer data. You can't
  view, manage, or use AWS owned keys, or audit their use. However, you don't have to
  take any action or change any programs to protect the keys that encrypt your data. For
  more information, see [AWS owned keys](../../../kms/latest/developerguide/concepts.md#aws-owned-cmk "../../../kms/latest/developerguide/concepts.md#aws-owned-cmk")
  in the _AWS Key Management Service Developer Guide_.

Encryption of data at rest by default helps reduce the operational overhead and
complexity involved in protecting sensitive data. At the same time, it enables you to
build secure applications that meet strict encryption compliance and regulatory
requirements.

While you can't disable this layer of encryption or select an alternate encryption
type, you can add a second layer of encryption over the existing AWS owned encryption
keys by choosing a customer managed key when you create your resources:

- **AWS KMS key (KMS)** – Amazon Q
  supports the use of symmetric customer managed keys that you create, own, and manage to
  add a second layer of encryption over the existing AWS owned encryption.

In Amazon Q Business, you configure KMS keys when you create an Amazon Q Business application environment. The same KMS key is used to encrypt data for the
application environment you create and any child resources under the application environment (for example,
an Amazon Q Business index). However, KMS keys are not supported for the Amazon Q Business Starter index. So, if you use a KMS key with your application environment, you
won't be able to use an Amazon Q Business Starter index for it. To use KMS keys,
you must choose either an Amazon Q Business Enterprise index or an Amazon Kendra retriever
for your application environment.

###### Important

Amazon Q does not support asymmetric KMS keys. For more information, see [Using Symmetric and Asymmetric Keys](../../../kms/latest/developerguide/symmetric-asymmetric.md "../../../kms/latest/developerguide/symmetric-asymmetric.md")
in the _AWS Key Management Service Developer Guide_.

Because you have full control of this layer of encryption, you can perform such tasks
as:

- Establishing and maintaining key policies
- Establishing and maintaining IAM policies and grants
- Enabling and disabling key policies
- Rotating key cryptographic material
- Adding tags
- Creating key aliases
- Scheduling keys for deletion

For more information, see [customer managed key](../../../kms/latest/developerguide/concepts.md#customer-cmk "../../../kms/latest/developerguide/concepts.md#customer-cmk")
in the _AWS Key Management Service Developer Guide_.

###### Note

If you have created your Amazon Q Business application environment using AWS KMS and then
you want to migrate to using customer managed key (CMK), you will have to re-create your
application environment.

###### Topics

- [How Amazon Q Business uses grants in
  AWS KMS](#using-grants-kms "#using-grants-kms")
- [Create a customer managed key](#create-cmk "#create-cmk")
- [Specifying customer managed key for Amazon Q Business](#specify-cmk "#specify-cmk")
- [Monitoring your encryption keys for Amazon Q](#monitoring-cmk-key "#monitoring-cmk-key")

### How Amazon Q Business uses grants in

AWS KMS

Amazon Q Business requires a [grant](../../../kms/latest/developerguide/grants.md "../../../kms/latest/developerguide/grants.md") to use your customer managed key. When
you create a Amazon Q Business application environment resource encrypted with a customer managed key,
Amazon Q creates a grant on your behalf by sending a [CreateGrant](../../../kms/latest/APIReference/API_CreateGrant.md "../../../kms/latest/APIReference/API_CreateGrant.md") request to AWS KMS. Grants in AWS KMS are used to give Amazon Q Business access to a KMS key in a customer account.

Amazon Q Business requires the grant to use your customer managed key for the following
internal operations:

- Send [DescribeKey](../../../kms/latest/APIReference/API_DescribeKey.md "../../../kms/latest/APIReference/API_DescribeKey.md") requests to
  AWS KMS to verify that the symmetric customer managed key ID entered when creating application environment
  is valid.
- Send [GenerateDataKeyWithoutPlainText](../../../kms/latest/APIReference/API_GenerateDataKeyWithoutPlaintext.md "../../../kms/latest/APIReference/API_GenerateDataKeyWithoutPlaintext.md") requests to AWS KMS to generate data keys
  encrypted by your customer managed key.
- Send [Decrypt](../../../kms/latest/APIReference/API_Decrypt.md "../../../kms/latest/APIReference/API_Decrypt.md") requests to AWS KMS to decrypt the encrypted data keys so that they
  can be used to encrypt your data.

You can revoke access to the grant, or remove the service's access to the customer managed key
at any time. If you do, Amazon Q Business won't be able to access any of the data
encrypted by the customer managed key, which affects operations that are dependent on that
data.

### Create a customer managed key

You can create a symmetric customer managed key by using the AWS Management Console, or the AWS KMS
APIs.

###### Important

Amazon Q does not support asymmetric KMS keys. For more information, see [Using Symmetric and Asymmetric
Keys](../../../kms/latest/developerguide/symmetric-asymmetric.md "../../../kms/latest/developerguide/symmetric-asymmetric.md") in the _AWS Key Management Service Developer
Guide_.

**To create a symmetric customer managed key**

Follow the steps for [Creating
symmetric customer managed key](../../../kms/latest/developerguide/create-keys.md#create-symmetric-cmk "../../../kms/latest/developerguide/create-keys.md#create-symmetric-cmk") in the _AWS Key Management Service Developer
Guide_.

**Key policy**

Key policies control access to your customer managed key. Every customer managed key must have exactly one
key policy, which contains statements that determine who can use the key and how they can
use it. When you create your customer managed key, you can specify a key policy. For more
information, see [Managing
access to customer managed keys](../../../kms/latest/developerguide/control-access-overview.md#managing-access "../../../kms/latest/developerguide/control-access-overview.md#managing-access") in the _AWS Key Management Service
Developer Guide_.

To use your customer managed key with your Amazon Q Business resources, the following API
operations must be permitted in the key policy:

- [kms:CreateGrant](../../../kms/latest/APIReference/API_CreateGrant.md "../../../kms/latest/APIReference/API_CreateGrant.md") – Adds a grant to a customer managed key. Grants control
  access to a specified KMS key,which allows access to [grant
  operation](../../../kms/latest/developerguide/grants.md#terms-grant-operations "../../../kms/latest/developerguide/grants.md#terms-grant-operations")
  Amazon Q Business requires. For more information about [Using
  Grants](../../../kms/latest/developerguide/grants.md "../../../kms/latest/developerguide/grants.md"), see the _AWS Key Management Service Developer
  Guide_.

This allows Amazon Q Business to do the following:

    + Call `GenerateDataKeyWithoutPlainText` to generate an encrypted
     data key and store it, because the data key isn't immediately used to
     encrypt.
    + Call `Decrypt` to use the stored encrypted data key to access
     encrypted data.
    + Set up a retiring principal to allow the service to
     `RetireGrant`.

- [kms:DescribeKey](../../../kms/latest/APIReference/API_DescribeKey.md "../../../kms/latest/APIReference/API_DescribeKey.md") – Provides the customer managed key details to allow Amazon Q to validate the key.

The following are policy statement examples you can add for Amazon Q Business

```
 "Statement": [{
         "Sid": "Allow access to principals authorized to use Amazon Q",
         "Effect": "Allow",
         "Principal": {
             "AWS": "arn:aws:iam::111122223333:role/Admin"
         },
         "Action": [
             "kms:DescribeKey",
             "kms:CreateGrant"
         ],
         "Resource": "*",
         "Condition": {
             "StringEquals": {
                 "kms:ViaService": "qbusiness.region.amazonaws.com",
                 "kms:CallerAccount": "111122223333"
             }
           }
         },
         {
             "Sid": "Allow access for key administrators",
             "Effect": "Allow",
             "Principal": {
                 "AWS": "arn:aws:iam::111122223333:root"
             },
             "Action": [
                 "kms:*"
             ],
             "Resource": "arn:aws:kms:region:111122223333:key/key_ID"
         },
         {
             "Sid": "Allow read-only access to key metadata to the account",
             "Effect": "Allow",
             "Principal": {
                 "AWS": "arn:aws:iam::111122223333:root"
             },
             "Action": [
                 "kms:Describe*",
                 "kms:Get*",
                 "kms:List*",
                 "kms:RevokeGrant"
             ],
             "Resource": "*"
         }
     ]
```

[Show moreShow less](# "#")
For more information about [specifying permissions in a policy](../../../kms/latest/developerguide/control-access-overview.md#overview-policy-elements "../../../kms/latest/developerguide/control-access-overview.md#overview-policy-elements") and [troubleshooting
key access](../../../kms/latest/developerguide/policy-evaluation.md#example-no-iam "../../../kms/latest/developerguide/policy-evaluation.md#example-no-iam"), see the _AWS Key Management Service Developer
Guide_

### Specifying customer managed key for Amazon Q Business

You can specify a customer managed key as a second layer encryption for your Amazon Q Business application environment resource.

When you create your application environment, you can specify the data key by entering a
**KMS ID**, which Amazon Q Business uses to encrypt
the identifiable personal data stored by the application environment.

**KMS ID** – A [key identifier](../../../kms/latest/developerguide/concepts.md#key-id "../../../kms/latest/developerguide/concepts.md#key-id") for an
AWS KMS customer managed key. Enter a key ID, key ARN, alias name, or alias ARN.

Any resources you create under your Amazon Q Business application environment will be
encrypted with the same key.

### Monitoring your encryption keys for Amazon Q

When you use an AWS KMS customer managed key with your Amazon Q Business resources, you can
use [AWS CloudTrail](../../../awscloudtrail/latest/userguide/cloudtrail-user-guide.md "../../../awscloudtrail/latest/userguide/cloudtrail-user-guide.md") or
[Amazon CloudWatch Logs](../../../AmazonCloudWatch/latest/logs/WhatIsCloudWatchLogs.md "../../../AmazonCloudWatch/latest/logs/WhatIsCloudWatchLogs.md") to track
requests that Amazon Q Business sends to AWS KMS.

The following examples are AWS CloudTrail events for `CreateGrant`,
`GenerateDataKey`, `Decrypt`, and `DescribeKey` to
monitor KMS operations called by Amazon Q Business to access data encrypted by your
customer managed key.

CreateGrant
When you use an AWS KMS customer managed key to encrypt your application environment, Amazon Q sends a `CreateGrant` request on your behalf to access the
KMS key in your AWS account. The grant that Amazon Q Business creates are
specific to the resource associated with the AWS KMS customer managed key. In addition , Amazon Q Business uses the `RetireGrant` operation to remove a grant when
you delete a resource.

The following example event records the `CreateGrant`
operation:

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
            "invokedBy": "qbusiness.amazonaws.com"
        },
        "eventTime": "2021-04-22T17:07:02Z",
        "eventSource": "kms.amazonaws.com",
        "eventName": "CreateGrant",
        "awsRegion": "us-west-2",
        "sourceIPAddress": "172.12.34.56",
        "userAgent": "ExampleDesktop/1.0 (V1; OS)",
        "requestParameters": {
            "retiringPrincipal": "qbusiness.region.amazonaws.com",
            "operations": [
                "CreateGrant",
                "RetireGrant",
                "GenerateDataKey",
                "GenerateDataKeyWithoutPlaintext",
                "Encrypt",
                "ReEncryptTo",
                "ReEncryptFrom",
                "Decrypt",
                "DescribeKey"
            ],
            "keyId": "arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-123456SAMPLE",
            "granteePrincipal": "qbusiness.region.amazonaws.com"
        },
        "responseElements": {
            "grantId": "0ab0ac0d0b000f00ea00cc0a0e00fc00bce000c000f0000000c0bc0a0000aaafSAMPLE"
        },
        "requestID": "ff000af-00eb-00ce-0e00-ea000fb0fba0SAMPLE",
        "eventID": "ff000af-00eb-00ce-0e00-ea000fb0fba0SAMPLE",
        "readOnly": false,
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

GenerateDataKey
When you use an AWS KMS customer managed key for your application environment, Amazon Q Business
creates a unique table key. It sends a `GenerateDataKey` request to AWS KMS
that specifies the AWS KMS customer managed key for the application environment.

The following example event records the `GenerateDataKey`
operation:

```
{
        "eventVersion": "1.08",
        "userIdentity": {
            "type": "AWSService",
            "invokedBy": "qbusiness.amazonaws.com"
        },
        "eventTime": "2023-11-24T01:50:25Z",
        "eventSource": "kms.amazonaws.com",
        "eventName": "GenerateDataKey",
        "awsRegion": "us-west-2",
        "sourceIPAddress": "172.12.34.56",
        "userAgent": "ExampleDesktop/1.0 (V1; OS)",
        "requestParameters": {
            "keyId": "arn:aws:kms:us-west-2:398547360552:key/ba6c9092-ad4d-41c3-937a-f02177ae147e",
            "keySpec": "AES_256"
        },
        "responseElements": null,
        "requestID": "4bd8e018-90d0-4b93-bc8d-32338578a158",
        "eventID": "aca6cb5b-44bb-3ed6-afdd-736432323356",
        "readOnly": true,
        "resources": [
            {
                "accountId": "111122223333",
                "type": "AWS::KMS::Key",
                "ARN": "arn:aws:kms:us-west-2:398547360552:key/ba6c9092-ad4d-41c3-937a-f02177ae147e"
            }
        ],
        "eventType": "AwsApiCall",
        "managementEvent": true,
        "recipientAccountId": "398547360552",
        "sharedEventID": "57393866-c398-4fd6-a259-d6cb001c7cf9",
        "eventCategory": "Management"
    }

```

Decrypt
When you access an encrypted application environment, Amazon Q Business calls the
`Decrypt` operation to use the stored encrypted data key to access the
encrypted data.

The following example event records the `Decrypt` operation.

```
{
        "eventVersion": "1.08",
        "userIdentity": {
            "type": "AWSService",
            "invokedBy": "qbusiness.amazonaws.com"
        },
        "eventTime": "2021-04-22T17:10:51Z",
        "eventSource": "kms.amazonaws.com",
        "eventName": "Decrypt",
        "awsRegion": "us-west-2",
        "sourceIPAddress": "172.12.34.56",
        "userAgent": "ExampleDesktop/1.0 (V1; OS)",
        "requestParameters": {
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
Amazon Q Business uses the `DescribeKey` operation to verify if
the AWS KMS customer managed key associated with your application environment exists in the account and
region.

The following example event records `DescribeKey` operation:

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
            "invokedBy": "qbusiness.amazonaws.com"
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

## Encryption in transit

Amazon Q Business uses the HTTPS protocol to communicate with your client application environment.
It uses HTTPS and AWS Signature Version 4 (SigV4) to communicate with other services on
your application environment's behalf.
