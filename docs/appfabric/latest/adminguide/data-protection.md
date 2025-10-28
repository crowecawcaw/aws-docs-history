# Data protection in AWS AppFabric

The AWS [shared responsibility model](https://aws.amazon.com/compliance/shared-responsibility-model/ "https://aws.amazon.com/compliance/shared-responsibility-model/")
applies to data protection in AWS AppFabric. As described in this model, AWS is
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
  customers' email addresses, into tags or free-form text fields such as a **Name** field. This includes when you work with AppFabric or other AWS services
  using the console, API, AWS CLI, or AWS SDKs. Any data that you enter into
  tags or free-form text fields used for names may be used for billing or diagnostic logs. If you
  provide a URL to an external server, we strongly recommend that you do not include credentials
  information in the URL to validate your request to that server.

###### Note

For more information about data protection as it applies to AppFabric for security, see [Data processing in AppFabric](productivity-data-processing.md "productivity-data-processing.md").

## Encryption at rest

AWS AppFabric supports encryption at rest, a server-side encryption feature in which AppFabric
transparently encrypts all data related to your app bundles when it is persisted to disk, and
decrypts them when you access the data. By default, AppFabric encrypts your data using an
AWS owned key from AWS Key Management Service (AWS KMS). You can also choose to encrypt your data using your
own customer managed key from AWS KMS.

When you delete an app bundle, all its metadata is permanently deleted.

## Encryption in transit

When you configure an app bundle, you can choose either an AWS owned key or a
customer managed key. When collecting and normalizing the data for an audit log ingestion, AppFabric stores
data temporarily in an intermediate Amazon Simple Storage Service (Amazon S3) bucket and encrypts it using this key.
This intermediate bucket is deleted after 30 days, using a bucket lifecycle policy.

AppFabric secures all data in transit using TLS 1.2 and signs API requests for AWS services
with AWS Signature V4.

## Key management

AppFabric supports encrypting data with an AWS owned key or a customer managed key. We recommend that
you use a customer managed key because it puts you in full control over your encrypted data. When you
choose a customer managed key, AppFabric attaches a resource policy to the customer managed key that grants it access
to the customer managed key.

### Customer managed key

To create a customer managed key, follow the steps for [Creating symmetric
encryption KMS keys](../../../kms/latest/developerguide/create-keys.md#create-symmetric-cmk "../../../kms/latest/developerguide/create-keys.md#create-symmetric-cmk") in the _AWS KMS Developer Guide_.

## Key policy

Key policies control access to your customer managed keys. Every customer managed key must have exactly one
key policy, which contains statements that determine who can use the key and how they can use
it. When you create your customer managed key, you can specify a key policy. For information about
creating a key policy, see [Creating a key policy](../../../kms/latest/developerguide/key-policy-overview.md "../../../kms/latest/developerguide/key-policy-overview.md") in
the _AWS KMS Developer Guide_.

To use a customer managed key with AppFabric, the AWS Identity and Access Management (IAM) user or role creating your AppFabric
resources must have permission to use your customer managed key. We recommend that you create a key that
you use only with AppFabric and add your AppFabric users as users of the key. This approach limits the
scope of access to your data. The permissions your users require are as follows:

- `kms:DescribeKey`
- `kms:CreateGrant`
- `kms:GenerateDataKey`
- `kms:Decrypt`

The AWS KMS console guides you through creating a key with the appropriate key policy. For
more information about key policies, see [Key
policies in AWS KMS](../../../kms/latest/developerguide/key-policies.md#key-policy-default-allow-users "../../../kms/latest/developerguide/key-policies.md#key-policy-default-allow-users") in the _AWS KMS Developer Guide_.

Following is an example key policy that permits:

- The AWS account root user full control of the key.
- Users permitted to use AppFabric to use your customer managed key with AppFabric.
- A key policy for an app bundle setup in `us-east-1`.

## How AppFabric uses grants in AWS KMS

AppFabric requires a grant to use your customer managed key. For more information, see [Grants in AWS KMS](../../../kms/latest/developerguide/grants.md "../../../kms/latest/developerguide/grants.md") in
the _AWS KMS Developer Guide_.

When you create an app bundle, AppFabric creates a grant on your behalf by sending a
`CreateGrant` request to AWS KMS. Grants in AWS KMS are used to
give AppFabric access to an AWS KMS key in a customer account. AppFabric requires that the grant to use
your customer managed key for the following internal operations:

- Send `GenerateDataKey` requests to AWS KMS to generate data keys
  encrypted by your customer managed key.
- Send `Decrypt` requests to AWS KMS to decrypt the encrypted
  data keys so that they can be used to encrypt your data and to decrypt application access
  tokens in transit.
- Send `Encrypt` requests to AWS KMS to encrypt application
  access tokens in transit.

Following is an example of a grant.

```
{
  "KeyId": "arn:aws:kms:us-east-1:111122223333:key/ff000af-00eb-00ce-0e00-ea000fb0fba0SAMPLE",
  "GrantId": "0ab0ac0d0b000f00ea00cc0a0e00fc00bce000c000f0000000c0bc0a0000aaafSAMPLE",
  "Name": "ff000af-00eb-00ce-0e00-ea000fb0fba0SAMPLE",
  "CreationDate": "2022-10-11T20:35:39+00:00",
  "GranteePrincipal": "appfabric.us-east-1.amazonaws.com",
  "RetiringPrincipal": "appfabric.us-east-1.amazonaws.com",
  "IssuingAccount": "arn:aws:iam::111122223333:root",
  "Operations": [
    "Decrypt",
    "Encrypt",
    "GenerateDataKey"
  ],
  "Constraints": {
    "EncryptionContextSubset": {
      "appBundleArn": "arn:aws:fabric:us-east-1:111122223333:appbundle/ff000af-00eb-00ce-0e00-ea000fb0fba0SAMPLE"
    }
  }
},
```

When you delete an app bundle, AppFabric retires issued grants on your customer managed key.

## Monitoring your encryption keys for AppFabric

When you use AWS KMS customer managed keys with AppFabric, you can use AWS CloudTrail logs to track requests
that AppFabric sends to AWS KMS.

Following is an example of an CloudTrail event logged when AppFabric uses `CreateGrant`
for your customer managed key.

```
{
    "eventVersion": "1.08",
    "userIdentity": {
        "type": "AssumedRole",
        "principalId": "AROAIGDTESTANDEXAMPLE:SampleUser",
        "arn": "arn:aws:sts::111122223333:assumed-role/AssumedRole/SampleUser",
        "accountId": "111122223333",
        "accessKeyId": "AKIAIOSFODNN7EXAMPLE",
        "sessionContext": {
            "sessionIssuer": {
                "type": "Role",
                "principalId": "AROAIGDTESTANDEXAMPLE",
                "arn": "arn:aws:iam::111122223333:role/AssumedRole",
                "accountId": "111122223333",
                "userName": "SampleUser"
            },
            "webIdFederationData": {},
            "attributes": {
                "creationDate": "2023-04-28T14:01:33Z",
                "mfaAuthenticated": "false"
            }
        }
    },
    "eventTime": "2023-04-28T14:05:48Z",
    "eventSource": "kms.amazonaws.com",
    "eventName": "CreateGrant",
    "awsRegion": "us-east-1",
    "sourceIPAddress": "appfabric.amazonaws.com",
    "userAgent": "appfabric.amazonaws.com",
    "requestParameters": {
        "granteePrincipal": "appfabric.us-east-1.amazonaws.com",
        "constraints": {
            "encryptionContextSubset": {
                "appBundleArn": "arn:aws:appfabric:us-east-1:111122223333:appbundle/ff000af-00eb-00ce-0e00-ea000fb0fba0SAMPLE"
            }
        },
        "keyId": "arn:aws:kms:us-east-1:111122223333:key/EXAMPLEID",
        "retiringPrincipal": "appfabric.us-east-1.amazonaws.com",
        "operations": [
            "Encrypt",
            "Decrypt",
            "GenerateDataKey"
        ]
    },
    "responseElements": {
        "grantId": "ff000af-00eb-00ce-0e00-ea000fb0fba0SAMPLE",
        "keyId": "arn:aws:kms:us-east-1:111122223333:key/KEY_ID"
    },
    "additionalEventData": {
        "grantId": "0ab0ac0d0b000f00ea00cc0a0e00fc00bce000c000f0000000c0bc0a0000aaafSAMPLE"
    },
    "requestID": "ff000af-00eb-00ce-0e00-ea000fb0fba0SAMPLE",
    "eventID": "ff000af-00eb-00ce-0e00-ea000fb0fba0SAMPLE",
    "readOnly": false,
    "resources": [
        {
            "accountId": "AWS Internal",
            "type": "AWS::KMS::Key",
            "ARN": "arn:aws:kms:us-east-1:111122223333:key/key_ID"
        }
    ],
    "eventType": "AwsApiCall",
    "managementEvent": true,
    "recipientAccountId": "111122223333",
    "sharedEventID": "ff000af-00eb-00ce-0e00-ea000fb0fba0SAMPLE",
    "eventCategory": "Management",
    "tlsDetails": {
        "tlsVersion": "TLSv1.3",
        "cipherSuite": "TLS_AES_256_GCM_SHA384",
        "clientProvidedHostHeader": "kms.us-east-1.amazonaws.com"
    }
}
```
