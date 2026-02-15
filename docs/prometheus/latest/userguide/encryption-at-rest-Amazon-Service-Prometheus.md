# Encryption at

rest

By default, Amazon Managed Service for Prometheus automatically provides you with encryption at rest and does this
using AWS owned encryption keys.

- **AWS owned keys** – Amazon Managed Service for Prometheus uses these
  keys to automatically encrypt data uploaded to your workspace. You can't view,
  manage or use AWS owned keys, or audit their use. However, you don't have to
  take any action or change any programs to protect the keys that encrypt your
  data. For more information, see [AWS owned
  keys](../../../kms/latest/developerguide/concepts.md#aws-owned-cmk "../../../kms/latest/developerguide/concepts.md#aws-owned-cmk") in the _AWS Key Management Service Developer Guide_.
  Encryption of data at rest helps reduce the operational overhead and complexity that goes into
  protecting sensitive customer data, such as personally identifiable information. It
  allows you to build secure applications that meet strict encryption compliance and
  regulatory requirements.

You can alternatively choose to use a customer managed key when you create your
workspace:

- **Customer managed keys** – Amazon Managed Service for Prometheus
  supports the use of a symmetric customer managed key that you create, own, and
  manage to encrypt the data in your workspace. Because you have
  full control of this encryption, you can perform such tasks
  as:

      + Establishing and maintaining key policies
      + Establishing and maintaining IAM policies and grants
      + Enabling and disabling key policies
      + Rotating key cryptographic material
      + Adding tags
      + Creating key aliases
      + Scheduling keys for deletion

  For more information, see [customer
  managed keys](../../../kms/latest/developerguide/concepts.md#customer-cmk "../../../kms/latest/developerguide/concepts.md#customer-cmk") in the _AWS Key Management Service Developer
  Guide._
  Choose whether to use customer managed keys or AWS owned keys
  carefully. Workspaces created with customer managed keys can't be
  converted to use AWS owned keys later (and vice versa).

###### Note

Amazon Managed Service for Prometheus automatically enables encryption at rest using AWS owned keys to
protect your data at no charge.

However, AWS KMS charges apply for using a customer managed key. For more
information about pricing, see [AWS Key Management Service pricing](https://aws.amazon.com/kms/pricing/ "https://aws.amazon.com/kms/pricing/").

For more information on AWS KMS, see [What is AWS Key Management Service?](../../../kms/latest/developerguide/overview.md "../../../kms/latest/developerguide/overview.md")

###### Note

Workspaces created with customer managed keys cannot use [AWS managed collectors](AMP-collector.md "AMP-collector.md") for
ingestion.

## How Amazon Managed Service for Prometheus uses grants in AWS KMS

Amazon Managed Service for Prometheus requires three [grants](../../../kms/latest/developerguide/grants.md "../../../kms/latest/developerguide/grants.md") to use your customer
managed key.

When you create an Amazon Managed Service for Prometheus workspace encrypted with a customer managed key,
Amazon Managed Service for Prometheus creates the three grants on your behalf by sending [CreateGrant](../../../kms/latest/APIReference/API_CreateGrant.md "../../../kms/latest/APIReference/API_CreateGrant.md") requests to AWS KMS. Grants in AWS KMS are used to give
Amazon Managed Service for Prometheus access to the KMS key in your account, even when not called directly on
your behalf (for example, when storing metrics data that has been scraped from an
Amazon EKS cluster.

Amazon Managed Service for Prometheus requires the grants to use your customer managed key for the following
internal operations:

- Send [DescribeKey](../../../kms/latest/APIReference/API_DescribeKey.md "../../../kms/latest/APIReference/API_DescribeKey.md")
  requests to AWS KMS to verify that the symmetric customer managed KMS key
  given when creating a workspace is valid.
- Send [GenerateDataKey](../../../kms/latest/APIReference/API_GenerateDataKey.md "../../../kms/latest/APIReference/API_GenerateDataKey.md") requests to AWS KMS to generate
  data keys encrypted by your customer managed key.
- Send [Decrypt](../../../kms/latest/APIReference/API_Decrypt.md "../../../kms/latest/APIReference/API_Decrypt.md") requests
  to AWS KMS to decrypt the encrypted data keys so that they can be used to
  encrypt your data.

Amazon Managed Service for Prometheus creates three grants to the AWS KMS key that allow Amazon Managed Service for Prometheus to use the
key on your behalf. You can remove access to the key by changing the key policy, by
disabling the key, or by revoking the grant. You should understand the
consequences of these actions before performing them. This can cause data loss in
your workspace.

If you remove access to any of the grants in any way, Amazon Managed Service for Prometheus won't be able to
access any of the data encrypted by the customer managed key, nor store new data
sent to the workspace, which affects operations that are dependent on that data.
New data sent to the workspace will not be accessible and may be permanently lost.

###### Warning

- If you disable the key, or remove Amazon Managed Service for Prometheus access in the key policy,
  the workspace data is no longer accessible. New data being sent to the
  workspace will not be accessible and may be permanently lost.

You can get access to the workspace data and start receiving new data
again by restoring Amazon Managed Service for Prometheus access to the key.

- If you _revoke_ a
  grant, it can't be recreated, and the data in the workspace is lost
  permanently.

## Step 1: Create a customer managed key

You can create a symmetric customer managed key by using the AWS Management Console, or the AWS KMS
APIs. The key does not need to be in the same account as the Amazon Managed Service for Prometheus workspace,
as long as you provide the correct access through policy, as described below.

**To create a symmetric customer managed key**

Follow the steps for [Creating
symmetric customer managed key](../../../kms/latest/developerguide/create-keys.md#create-symmetric-cmk "../../../kms/latest/developerguide/create-keys.md#create-symmetric-cmk") in the _AWS Key Management Service Developer
Guide_.

**Key policy**

Key policies control access to your customer managed key. Every customer managed key must have exactly
one key policy, which contains statements that determine who can use the key and how
they can use it. When you create your customer managed key, you can specify a key policy. For
more information, see [Managing access to customer managed keys](../../../kms/latest/developerguide/control-access-overview.md#managing-access "../../../kms/latest/developerguide/control-access-overview.md#managing-access") in the _AWS Key Management Service
Developer Guide_.

To use your customer managed key with your Amazon Managed Service for Prometheus workspaces, the following API
operations must be permitted in the key policy:

- `kms:CreateGrant` – Adds a grant to a customer managed key.
  Grants control access to a specified KMS key, which allows access to [grant
  operations](../../../kms/latest/developerguide/grants.md#terms-grant-operations "../../../kms/latest/developerguide/grants.md#terms-grant-operations") Amazon Managed Service for Prometheus requires. For more information, see [Using
  Grants](../../../kms/latest/developerguide/grants.md "../../../kms/latest/developerguide/grants.md") in the _AWS Key Management Service Developer
  Guide_.

This allows Amazon Managed Service for Prometheus to do the following:

    + Call `GenerateDataKey` to generate an
     encrypted data key and store it, because the data key isn't
     immediately used to encrypt.
    + Call `Decrypt` to use the stored encrypted data key to
     access encrypted data.

- `kms:DescribeKey` – Provides the customer managed key details to
  allow Amazon Managed Service for Prometheus to validate the key.

The following are policy statement examples you can add for Amazon Managed Service for Prometheus:

```
  "Statement" : [
    {
      "Sid" : "Allow access to Amazon Managed Service for Prometheus principal within your account",
      "Effect" : "Allow",
      "Principal" : {
        "AWS" : "*"
      },
      "Action" : [
        "kms:DescribeKey",
        "kms:CreateGrant",
        "kms:GenerateDataKey",
        "kms:Decrypt"
      ],
      "Resource" : "*",
      "Condition" : {
        "StringEquals" : {
          "kms:ViaService" : "aps.`region`.amazonaws.com",
          "kms:CallerAccount" : "111122223333"
        }
    },
    {
      "Sid": "Allow access for key administrators - not required for Amazon Managed Service for Prometheus",
      "Effect": "Allow",
      "Principal": {
        "AWS": "arn:aws:iam::111122223333:root"
       },
      "Action" : [
        "kms:*"
       ],
      "Resource": "arn:aws:kms:`region`:111122223333:key/`key_ID`"
    },
    `<other statements needed for other non-Amazon Managed Service for Prometheus scenarios>`
  ]
```

- For more information about [specifying permissions in a policy](../../../kms/latest/developerguide/control-access-overview.md#overview-policy-elements "../../../kms/latest/developerguide/control-access-overview.md#overview-policy-elements"), see the _AWS Key Management Service Developer Guide_.
- For more information about [troubleshooting key access](../../../kms/latest/developerguide/policy-evaluation.md#example-no-iam "../../../kms/latest/developerguide/policy-evaluation.md#example-no-iam"), see the _AWS Key Management Service Developer Guide_.

## Step 2: Specifying a customer managed key for

Amazon Managed Service for Prometheus

When you create a workspace, you can specify the customer managed key by entering
a **KMS Key ARN**, which Amazon Managed Service for Prometheus uses to encrypt the data
stored by the workspace.

## Step 3: Accessing data from other services, such as

Amazon Managed Grafana

_This step is optional — it is only required if you need to access
your Amazon Managed Service for Prometheus data from another service._

Your encrypted data is not accessible from other services, unless they also have
access to use the AWS KMS key. For example, if you want to use Amazon Managed Grafana to create a
dashboard or alert on your data, you must give Amazon Managed Grafana access to the key.

###### To give Amazon Managed Grafana access to your customer managed key

1. In your [Amazon Managed Grafana
   workspaces list](https://console.aws.amazon.com/grafana/home?#/workspaces "https://console.aws.amazon.com/grafana/home?#/workspaces"), select the name for the workspace that you want to
   have access to Amazon Managed Service for Prometheus. This shows you summary information about your
   Amazon Managed Grafana workspace.
2. Note the name of the IAM role used by your workspace. The name is in
   the format `AmazonGrafanaServiceRole-<unique-id>`. The console
   shows you the full ARN for the role. You will specify this name in the AWS KMS
   console in a later step.
3. In your [AWS KMS Customer
   managed keys list](https://console.aws.amazon.com/kms/home?#/kme/keys "https://console.aws.amazon.com/kms/home?#/kme/keys"), choose the customer managed key you used during
   creation of your Amazon Managed Service for Prometheus workspace. This
   opens the key configuration details page.
4. Next to **Key users**, select the **Add**
   button.
5. From the list of names, choose the Amazon Managed Grafana IAM role that you noted
   above. To make it easier to find, you can search by the name, as well.
6. Choose **Add** to add the IAM role to the list of Key
   users.

Your Amazon Managed Grafana workspace can now access the data in your Amazon Managed Service for Prometheus workspace. You
can add other users or roles to the key users to enable other services to access
your workspace.

## Amazon Managed Service for Prometheus encryption context

An [encryption
context](../../../kms/latest/developerguide/concepts.md#encrypt_context "../../../kms/latest/developerguide/concepts.md#encrypt_context") is an optional set of key-value pairs that contain additional
contextual information about the data.

AWS KMS uses the encryption context as additional authenticated data to support
authenticated encryption. When you include an encryption context in a
request to encrypt data, AWS KMS binds the encryption context to the encrypted data.
To decrypt data, you include the same encryption context in the request.

**Amazon Managed Service for Prometheus encryption context**

Amazon Managed Service for Prometheus uses the same encryption context in all AWS KMS cryptographic
operations, where the key is `aws:amp:arn` and the value is the
[Amazon Resource
Name](../../../general/latest/gr/aws-arns-and-namespaces.md "../../../general/latest/gr/aws-arns-and-namespaces.md") (ARN) of the workspace.

###### Example

```
"encryptionContext": {
    "aws:aps:arn": "arn:aws:aps:us-west-2:111122223333:workspace/ws-sample-1234-abcd-56ef-7890abcd12ef"
}
```

**Using encryption context for monitoring**

When you use a symmetric customer managed key to encrypt your workspace data,
you can also use the encryption context in audit records and logs to identify how
the customer managed key is being used. The encryption context also appears in [logs generated by AWS CloudTrail or
Amazon CloudWatch Logs](#example-custom-encryption "#example-custom-encryption").

**Using encryption context to control access to your
customer managed key**

You can use the encryption context in key policies and IAM policies as
`conditions` to control access to your symmetric customer managed key. You can
also use encryption context constraints in a grant.

Amazon Managed Service for Prometheus uses an encryption context constraint in grants to control access to the
customer managed key in your account or region. The grant constraint requires that the
operations that the grant allows use the specified encryption context.

###### Example

The following are example key policy statements to give access to a customer
managed key for a specific encryption context. The condition in this policy
statement requires that the grants have an encryption context constraint that
specifies the encryption context.

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
             "kms:EncryptionContext:aws:aps:arn": "arn:aws:aps:us-west-2:111122223333:workspace/ws-sample-1234-abcd-56ef-7890abcd12ef"
          }
     }
}
```

## Monitoring your encryption keys for

Amazon Managed Service for Prometheus

When you use an AWS KMS customer managed key with your Amazon Managed Service for Prometheus workspaces, you can
use [AWS CloudTrail](../../../awscloudtrail/latest/userguide/cloudtrail-user-guide.md "../../../awscloudtrail/latest/userguide/cloudtrail-user-guide.md")
or [Amazon CloudWatch Logs](../../../AmazonCloudWatch/latest/logs/WhatIsCloudWatchLogs.md "../../../AmazonCloudWatch/latest/logs/WhatIsCloudWatchLogs.md")
to track requests that Amazon Managed Service for Prometheus sends to AWS KMS.

The following examples are AWS CloudTrail events for `CreateGrant`,
`GenerateDataKey`, `Decrypt`, and
`DescribeKey` to monitor KMS operations called by Amazon Managed Service for Prometheus to access
data encrypted by your customer managed key:

CreateGrant
When you use an AWS KMS customer managed key to encrypt your workspace,
Amazon Managed Service for Prometheus sends three `CreateGrant` requests
on your behalf to access the KMS key you specified. The grants
that Amazon Managed Service for Prometheus creates are specific to the resource associated with the
AWS KMS customer managed key.

The following example event records a `CreateGrant`
operation:

```
{
    "eventVersion": "1.08",
    "userIdentity": {
        "type": "AssumedRole",
        "principalId": "TESTANDEXAMPLE:Sampleuser01",
        "arn": "arn:aws:sts::111122223333:assumed-role/Admin/Sampleuser01",
        "accountId": "111122223333",
        "accessKeyId": "EXAMPLE-KEY-ID1",
        "sessionContext": {
            "sessionIssuer": {
                "type": "Role",
                "principalId": "TESTANDEXAMPLE:Sampleuser01",
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
        "invokedBy": "aps.amazonaws.com"
    },
    "eventTime": "2021-04-22T17:07:02Z",
    "eventSource": "kms.amazonaws.com",
    "eventName": "CreateGrant",
    "awsRegion": "us-west-2",
    "sourceIPAddress": "172.12.34.56",
    "userAgent": "ExampleDesktop/1.0 (V1; OS)",
    "requestParameters": {
        "retiringPrincipal": "aps.region.amazonaws.com",
        "operations": [
            "GenerateDataKey",
            "Decrypt",
            "DescribeKey"
        ],
        "keyId": "arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-123456SAMPLE",
        "granteePrincipal": "aps.region.amazonaws.com"
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
When you enable an AWS KMS customer managed key for your workspace,
Amazon Managed Service for Prometheus creates a unique key. It sends a
`GenerateDataKey` request to AWS KMS that
specifies the AWS KMScustomer managed key for the resource.

The following example event records the
`GenerateDataKey` operation:

```
{
    "eventVersion": "1.08",
    "userIdentity": {
        "type": "AWSService",
        "invokedBy": "aps.amazonaws.com"
    },
    "eventTime": "2021-04-22T17:07:02Z",
    "eventSource": "kms.amazonaws.com",
    "eventName": "GenerateDataKey",
    "awsRegion": "us-west-2",
    "sourceIPAddress": "172.12.34.56",
    "userAgent": "ExampleDesktop/1.0 (V1; OS)",
    "requestParameters": {
        "encryptionContext": {
            "aws:aps:arn": "arn:aws:aps:us-west-2:111122223333:workspace/ws-sample-1234-abcd-56ef-7890abcd12ef"
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
When a query is generated on an encrypted workspace, Amazon Managed Service for Prometheus
calls the `Decrypt` operation to use the stored encrypted
data key to access the encrypted data.

The following example event records the `Decrypt`
operation:

```
{
    "eventVersion": "1.08",
    "userIdentity": {
        "type": "AWSService",
        "invokedBy": "aps.amazonaws.com"
    },
    "eventTime": "2021-04-22T17:10:51Z",
    "eventSource": "kms.amazonaws.com",
    "eventName": "Decrypt",
    "awsRegion": "us-west-2",
    "sourceIPAddress": "172.12.34.56",
    "userAgent": "ExampleDesktop/1.0 (V1; OS)",
    "requestParameters": {
        "encryptionContext": {
            "aws:aps:arn": "arn:aws:aps:us-west-2:111122223333:workspace/ws-sample-1234-abcd-56ef-7890abcd12ef"
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
Amazon Managed Service for Prometheus uses the `DescribeKey` operation to verify if the
AWS KMS customer managed key associated with your workspace
exists in the account and region.

The following example event records the `DescribeKey`
operation:

```
{
    "eventVersion": "1.08",
    "userIdentity": {
        "type": "AssumedRole",
        "principalId": "TESTANDEXAMPLE:Sampleuser01",
        "arn": "arn:aws:sts::111122223333:assumed-role/Admin/Sampleuser01",
        "accountId": "111122223333",
        "accessKeyId": "EXAMPLE-KEY-ID1",
        "sessionContext": {
            "sessionIssuer": {
                "type": "Role",
                "principalId": "TESTANDEXAMPLE:Sampleuser01",
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
        "invokedBy": "aps.amazonaws.com"
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

The following resources provide more information about data encryption at
rest.

- For more information about [AWS Key Management Service basic
  concepts](../../../kms/latest/developerguide/concepts.md "../../../kms/latest/developerguide/concepts.md"), see the _AWS Key Management Service Developer
  Guide_.
- For more information about [Security best
  practices for AWS Key Management Service](../../../kms/latest/developerguide/best-practices.md "../../../kms/latest/developerguide/best-practices.md"), see the _AWS Key Management Service Developer Guide_.
