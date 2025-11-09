# Data protection in AWS Entity Resolution

The AWS [shared responsibility model](https://aws.amazon.com/compliance/shared-responsibility-model/ "https://aws.amazon.com/compliance/shared-responsibility-model/")
applies to data protection in AWS Entity Resolution. As described in this model, AWS is
responsible for protecting the global infrastructure that runs all of the AWS Cloud. You are
responsible for maintaining control over your content that is hosted on this infrastructure.
You are also responsible for the security configuration and management tasks for the AWS services
that you use. For more information about data privacy, see the [Data Privacy FAQ](https://aws.amazon.com/compliance/data-privacy-faq/ "https://aws.amazon.com/compliance/data-privacy-faq/"). For information about data protection in Europe, see the [AWS Shared
Responsibility Model and GDPR](https://aws.amazon.com/blogs/security/the-aws-shared-responsibility-model-and-gdpr/ "https://aws.amazon.com/blogs/security/the-aws-shared-responsibility-model-and-gdpr/") blog post on the _AWS Security
Blog_.

For data protection purposes, we recommend that you protect AWS account
credentials and set up individual users with AWS IAM Identity Center or AWS Identity and Access Management (IAM). That way, each user is given only the permissions necessary to fulfill their job duties. We also recommend that you secure your data in the following ways:

- Use multi-factor authentication (MFA) with each account.
- Use SSL/TLS to communicate with AWS resources. We require TLS 1.2 and recommend TLS 1.3.
- Set up API and user activity logging with AWS CloudTrail. For information about using CloudTrail trails to capture AWS activities, see [Working with CloudTrail trails](../../../awscloudtrail/latest/userguide/cloudtrail-trails.md "../../../awscloudtrail/latest/userguide/cloudtrail-trails.md") in the _AWS CloudTrail User Guide_.
- Use AWS encryption solutions, along with all default security controls within AWS services.
- Use advanced managed security services such as Amazon Macie, which assists in discovering
  and securing sensitive data that is stored in Amazon S3.
- If you require FIPS 140-3 validated cryptographic modules when accessing AWS through
  a command line interface or an API, use a FIPS endpoint. For more information about the
  available FIPS endpoints, see [Federal
  Information Processing Standard (FIPS) 140-3](https://aws.amazon.com/compliance/fips/ "https://aws.amazon.com/compliance/fips/").
  We strongly recommend that you never put confidential or sensitive information, such as your
  customers' email addresses, into tags or free-form text fields such as a **Name** field. This includes when you work with AWS Entity Resolution or other AWS services
  using the console, API, AWS CLI, or AWS SDKs. Any data that you enter into
  tags or free-form text fields used for names may be used for billing or diagnostic logs. If you
  provide a URL to an external server, we strongly recommend that you do not include credentials
  information in the URL to validate your request to that server.

## Data encryption at rest for AWS Entity Resolution

AWS Entity Resolution provides encryption by default to protect sensitive customer data at rest using
AWS owned encryption keys.

**AWS owned keys** – AWS Entity Resolution uses these keys by
default to automatically encrypt personally identifiable data. You can't view, manage, or use
AWS owned keys, or audit their use. However, you don't have to take any action to protect
the keys that encrypt your data. For more information, see [AWS
owned keys](../../../kms/latest/developerguide/concepts.md#aws-owned-cmk "../../../kms/latest/developerguide/concepts.md#aws-owned-cmk") in the _AWS Key Management Service Developer
Guide_.

Encryption of data at rest by default helps reduce the operational overhead and complexity
involved in protecting sensitive data. At the same time, you can use it to build secure
applications that meet strict encryption compliance and regulatory requirements.

Alternatively, you can also provide a customer managed KMS key for encryption when you
create your matching workflow resource.

**Customer managed keys** – AWS Entity Resolution supports the use
of a symmetric customer managed KMS key that you create, own, and manage to allow encryption
of your sensitive data. Because you have full control of this layer of encryption, you can
perform such tasks as:

- Establishing and maintaining key policies
- Establishing and maintaining IAM policies and grants
- Enabling and disabling key policies
- Rotating key cryptographic material
- Adding tags
- Creating key aliases
- Scheduling keys for deletion

For more information, see [customer managed key](../../../kms/latest/developerguide/concepts.md#customer-cmk "../../../kms/latest/developerguide/concepts.md#customer-cmk") in the _AWS Key Management Service Developer
Guide_.

For more information about AWS KMS, see [What is AWS Key
Management Service?](../../../kms/latest/developerguide/overview.md "../../../kms/latest/developerguide/overview.md")

## Key management

### How AWS Entity Resolution uses grants in AWS KMS

AWS Entity Resolution requires a [grant](../../../kms/latest/developerguide/grants.md "../../../kms/latest/developerguide/grants.md") to
use your customer managed key. When you create a matching workflow encrypted with a customer
managed key, AWS Entity Resolution creates a grant on your behalf by sending a [CreateGrant](../../../kms/latest/APIReference/API_CreateGrant.md "../../../kms/latest/APIReference/API_CreateGrant.md") request to AWS KMS. Grants in AWS KMS are used to give AWS Entity Resolution access
to a KMS key in a customer account. AWS Entity Resolution requires the grant to use your customer
managed key for the following internal operations:

- Send [GenerateDataKey](../../../kms/latest/APIReference/API_GenerateDataKeyWithoutPlaintext.md "../../../kms/latest/APIReference/API_GenerateDataKeyWithoutPlaintext.md") requests to AWS KMS to generate data keys encrypted by your
  customer managed key.
- Send [Decrypt](../../../kms/latest/APIReference/API_Decrypt.md "../../../kms/latest/APIReference/API_Decrypt.md") requests to AWS KMS to decrypt the encrypted data keys so that they
  can be used to encrypt your data.

You can revoke access to the grant, or remove the service's access to the customer
managed key at any time. If you do, AWS Entity Resolution won't be able to access any of the data
encrypted by the customer managed key, which affects operations that are dependent on that
data. For example, if you remove the service access to your key through the grant and
attempt to start a job for a matching workflow encrypted with a customer key, then the
operation would return an `AccessDeniedException` error.

### Creating a customer managed key

You can create a symmetric customer managed key by using the AWS Management Console, or the AWS KMS
APIs.

**To create a symmetric customer managed key**

AWS Entity Resolution supports encryption using [Symmetric encryption KMS keys](../../../kms/latest/developerguide/concepts.md#symmetric-cmks "../../../kms/latest/developerguide/concepts.md#symmetric-cmks"). Follow the steps for [Creating symmetric customer managed key](../../../kms/latest/developerguide/create-keys.md#create-symmetric-cmk "../../../kms/latest/developerguide/create-keys.md#create-symmetric-cmk") in the _AWS Key Management Service
Developer Guide_.

**Key policy statement**

Key policies control access to your customer managed key. Every customer managed key
must have exactly one key policy, which contains statements that determine who can use the
key and how they can use it. When you create your customer managed key, you can specify a
key policy. For more information, see [Managing access to customer managed keys](../../../kms/latest/developerguide/control-access-overview.md#managing-access "../../../kms/latest/developerguide/control-access-overview.md#managing-access") in the _AWS Key Management Service Developer Guide_.

To use your customer managed key with your AWS Entity Resolution resources, the following API
operations must be permitted in the key policy:

- [`kms:DescribeKey`](../../../kms/latest/APIReference/API_DescribeKey.md "../../../kms/latest/APIReference/API_DescribeKey.md") – Provides information such as the key
  ARN, creation date (and deletion date, if applicable), the key state, and the origin and
  expiration date (if any) of the key material. It includes fields, like
  `KeySpec`, that help you distinguish different types of KMS keys. It also
  displays the key usage (encryption, signing, or generating and verifying MACs) and the
  algorithms that the KMS key supports. AWS Entity Resolution validates that the
  `KeySpec` is `SYMMETRIC_DEFAULT` and `KeyUsage` is
  `ENCRYPT_DECRYPT`.
- [`kms:CreateGrant`](../../../kms/latest/APIReference/API_CreateGrant.md "../../../kms/latest/APIReference/API_CreateGrant.md") – Adds a grant to a customer managed
  key. Grants control access to a specified KMS key, which allows access to [grant operations](../../../kms/latest/developerguide/grants.md#terms-grant-operations "../../../kms/latest/developerguide/grants.md#terms-grant-operations") AWS Entity Resolution requires. For more information about [Using
  Grants](../../../kms/latest/developerguide/grants.md "../../../kms/latest/developerguide/grants.md"), see the _AWS Key Management Service Developer
  Guide_.

This allows AWS Entity Resolution to do the following:

- Call `GenerateDataKey` to generate an encrypted data key and store it,
  because the data key isn't immediately used to encrypt.
- Call `Decrypt` to use the stored encrypted data key to access encrypted
  data.
- Set up a retiring principal to allow the service to `RetireGrant`.

The following are policy statement examples you can add for AWS Entity Resolution:

```
{
      "Sid" : "Allow access to principals authorized to use AWS Entity Resolution",
      "Effect" : "Allow",
      "Principal" : {
        "AWS" : "*"
      },
      "Action" : ["kms:DescribeKey","kms:CreateGrant"],
      "Resource" : "*",
      "Condition" : {
        "StringEquals" : {
          "kms:ViaService" : "entityresolution.region.amazonaws.com",
          "kms:CallerAccount" : "111122223333"
        }
      }
}
```

**Permissions for users**

When you configure a KMS key as the default key for encryption, the default KMS key
policy allows any user with access to the required KMS actions to use this KMS key to
encrypt or decrypt resources. You must grant users permission to call the following actions
in order to use customer managed KMS key encryption:

- `kms:CreateGrant`
- `kms:Decrypt`
- `kms:DescribeKey`
- `kms:GenerateDataKey`

During a [`CreateMatchingWorkflow` request](../apireference/API_CreateMatchingWorkflow.md "../apireference/API_CreateMatchingWorkflow.md"), AWS Entity Resolution will send a [DescribeKey](../../../kms/latest/APIReference/API_DescribeKey.md "../../../kms/latest/APIReference/API_DescribeKey.md")and a [CreateGrant](../../../kms/latest/APIReference/API_CreateGrant.md "../../../kms/latest/APIReference/API_CreateGrant.md") request to AWS KMS on your behalf. This will require the IAM entity
making the `CreateMatchingWorkflow` request with a customer managed KMS key to
have the `kms:DescribeKey` permissions on the KMS key policy.

During a [`CreateIdMappingWorkflow`](../apireference/API_CreateIdMappingWorkflow.md "../apireference/API_CreateIdMappingWorkflow.md") and [`StartIdMappingJob`](../apireference/API_StartIdMappingJob.md "../apireference/API_StartIdMappingJob.md") request, AWS Entity Resolution will send a [DescribeKey](../../../kms/latest/APIReference/API_DescribeKey.md "../../../kms/latest/APIReference/API_DescribeKey.md") and a [CreateGrant](../../../kms/latest/APIReference/API_CreateGrant.md "../../../kms/latest/APIReference/API_CreateGrant.md") request to AWS KMS on your behalf. This will require the IAM entity
making the `CreateIdMappingWorkflow` and `StartIdMappingJob` request
with a customer managed KMS key to have the `kms:DescribeKey` permissions on
the KMS key policy. Providers will be able to access the customer managed key to decrypt the data in
the AWS Entity Resolution Amazon S3 bucket.

The following are policy statement examples you can add for providers to decrypt the
data in the AWS Entity Resolution Amazon S3 bucket:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [{
 "Effect": "Allow",
 "Principal": {
 "AWS": "arn:aws:iam::715724997226:root"
 },
 "Action": [
 "kms:Decrypt"
 ],
 "Resource": "arn:aws:kms:us-east-1:`111122223333`:key/key-id",
 "Condition": {
 "StringEquals": {
 "kms:ViaService": "s3.us-east-1.amazonaws.com"
 }
 }
 }]
}`

```

Replace each `<user input placeholder>` with your own
information.

|               |                               |
| ------------- | ----------------------------- |
| `<KMSKeyARN>` | AWS KMS Amazon Resource Name. |

Similarly, the IAM entity invoking the [`StartMatchingJob` API](../apireference/API_StartMatchingJob.md "../apireference/API_StartMatchingJob.md") must have `kms:Decrypt` and
`kms:GenerateDataKey` permissions on the customer managed KMS key provided in
the matching workflow.

For more information about [specifying permissions in a policy](../../../kms/latest/developerguide/control-access-overview.md#overview-policy-elements "../../../kms/latest/developerguide/control-access-overview.md#overview-policy-elements"), see the _AWS Key Management Service
Developer Guide_.

For more information about [troubleshooting key access](../../../kms/latest/developerguide/policy-evaluation.md#example-no-iam "../../../kms/latest/developerguide/policy-evaluation.md#example-no-iam"), see the _AWS Key Management Service Developer
Guide_.

### Specifying a customer managed key for AWS Entity Resolution

You can specify a customer managed key as a second layer encryption for the following
resources:

[Matching
workflow](../apireference/API_CreateMatchingWorkflow.md "../apireference/API_CreateMatchingWorkflow.md") – When you create a matching workflow resource, you can specify
the data key by entering a **KMSArn**, which AWS Entity Resolution uses to
encrypt the identifiable personal data stored by the resource.

**KMSArn** – Enter a key ARN, which is a [key
identifier](../../../kms/latest/developerguide/concepts.md#key-id "../../../kms/latest/developerguide/concepts.md#key-id") for an AWS KMS customer managed key.

You can specify a customer managed key as a second layer encryption for the following
resources if you are creating or running an ID mapping workflow across two
AWS accounts:

[ID mapping
workflow](../apireference/API_CreateIdMappingWorkflow.md "../apireference/API_CreateIdMappingWorkflow.md") or [Start ID mapping
workflow](../apireference/API_StartIdMappingJob.md "../apireference/API_StartIdMappingJob.md") – When you create a ID mapping workflow resource or start an ID
mapping workflow job, you can specify the data key by entering a **KMSArn**, which AWS Entity Resolution uses to encrypt the identifiable personal data stored
by the resource.

**KMSArn** – Enter a key ARN, which is a [key
identifier](../../../kms/latest/developerguide/concepts.md#key-id "../../../kms/latest/developerguide/concepts.md#key-id") for an AWS KMS customer managed key.

### Monitoring your encryption keys for AWS Entity Resolution

Service

When you use an AWS KMS customer managed key with your AWS Entity Resolution Service resources, you
can use [AWS CloudTrail](../../../awscloudtrail/latest/userguide/cloudtrail-user-guide.md "../../../awscloudtrail/latest/userguide/cloudtrail-user-guide.md") or [Amazon CloudWatch Logs](../../../AmazonCloudWatch/latest/logs/WhatIsCloudWatchLogs.md "../../../AmazonCloudWatch/latest/logs/WhatIsCloudWatchLogs.md") to track requests that AWS Entity Resolution sends to AWS KMS.

The following examples are AWS CloudTrail events for `CreateGrant`,
`GenerateDataKey`, `Decrypt`, and `DescribeKey` to
monitor AWS KMS operations called by AWS Entity Resolution to access data encrypted by your customer
managed key:

###### Topics

- [CreateGrant](#create-grant "#create-grant")
- [DescribeKey](#kms-creategrant "#kms-creategrant")
- [GenerateDataKey](#kms-generatedatakey "#kms-generatedatakey")
- [Decrypt](#kms-decrypt "#kms-decrypt")

#### CreateGrant

When you use an AWS KMS customer managed key to encrypt your matching workflow resource,
AWS Entity Resolution sends a `CreateGrant` request on your behalf to access the KMS key
in your AWS account. The grant that AWS Entity Resolution creates are specific to the resource
associated with the AWS KMS customer managed key. In addition, AWS Entity Resolution uses the
`RetireGrant` operation to remove a grant when you delete a resource.

The following example event records the `CreateGrant` operation:

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
        "invokedBy": "entityresolution.amazonaws.com"
    },
    "eventTime": "2021-04-22T17:07:02Z",
    "eventSource": "kms.amazonaws.com",
    "eventName": "CreateGrant",
    "awsRegion": "us-west-2",
    "sourceIPAddress": "172.12.34.56",
    "userAgent": "ExampleDesktop/1.0 (V1; OS)",
    "requestParameters": {
        "retiringPrincipal": "entityresolution.region.amazonaws.com",
        "operations": [
            "GenerateDataKey",
            "Decrypt",
        ],
        "keyId": "arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-123456SAMPLE",
        "granteePrincipal": "entityresolution.region.amazonaws.com"
    },
    "responseElements": {
        "grantId": "0ab0ac0d0b000f00ea00cc0a0e00fc00bce000c000f0000000c0bc0a0000aaafSAMPLE",
        "keyId": "arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-123456SAMPLE",
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

#### DescribeKey

AWS Entity Resolution uses the `DescribeKey` operation to verify if the AWS KMS customer
managed key associated with your matching resource exists in the account and
Region.

The following example event records the `DescribeKey` operation.

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
        "invokedBy": "entityresolution.amazonaws.com"
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

#### GenerateDataKey

When you enable an AWS KMS customer managed key for your matching workflow resource,
AWS Entity Resolution sends a `GenerateDataKey` request through Amazon Simple Storage Service (Amazon S3) to AWS KMS
that specifies the AWS KMS customer managed key for the resource.

The following example event records the `GenerateDataKey` operation.

```
{
    "eventVersion": "1.08",
    "userIdentity": {
        "type": "AWSService",
        "invokedBy": "s3.amazonaws.com"
    },
    "eventTime": "2021-04-22T17:07:02Z",
    "eventSource": "kms.amazonaws.com",
    "eventName": "GenerateDataKey",
    "awsRegion": "us-west-2",
    "sourceIPAddress": "172.12.34.56",
    "userAgent": "ExampleDesktop/1.0 (V1; OS)",
    "requestParameters": {
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

#### Decrypt

When you enable an AWS KMS customer managed key for your matching workflow resource,
AWS Entity Resolution sends a `Decrypt` request through Amazon Simple Storage Service (Amazon S3) to AWS KMS that
specifies the AWS KMS customer managed key for the resource.

The following example event records the `Decrypt` operation.

```
{
    "eventVersion": "1.08",
    "userIdentity": {
        "type": "AWSService",
        "invokedBy": "s3.amazonaws.com"
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

### Considerations

AWS Entity Resolution doesn't support updating a matching workflow with a new customer managed
KMS key. In such cases, you can create a new workflow with the customer managed
KMS key.

### Learn more

The following resources provide more information about data encryption at rest.

For more information about [AWS Key
Management Service basic concepts](../../../kms/latest/developerguide/concepts.md "../../../kms/latest/developerguide/concepts.md"), see the _AWS Key Management Service
Developer Guide_.

For more information about [Security
best practices for AWS Key Management Service](../../../kms/latest/developerguide/best-practices.md "../../../kms/latest/developerguide/best-practices.md"), see the _AWS Key Management Service Developer Guide_.
