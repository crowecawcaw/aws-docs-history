# Encryption at rest in Amazon Connect

Contact data classified as PII, or data that represents customer content being stored
by Amazon Connect, is encrypted at rest (that is, before it is put, stored, or saved to a disk)
using AWS KMS encryption keys owned by AWS. For information
about AWS KMS keys, see [What is AWS Key Management Service?](../../../kms/latest/developerguide/overview.md "../../../kms/latest/developerguide/overview.md") in the
_AWS Key Management Service Developer Guide_. Contact data in non-temporary storage is
encrypted such that data encryption keys generated from the KMS keys are not shared
across Amazon Connect instances.

Amazon S3 server-side encryption is used to encrypt conversation recordings (voice and
chat). Call recordings, screen recordings, and transcripts are stored in two
phases:

- Recordings intermediately held within Amazon Connect during and after the contact, but
  before delivery.
- Recordings delivered to your Amazon S3 bucket.
  The recordings and chat transcripts that are stored in your Amazon S3 bucket are secured
  using a KMS key that was configured when your instance was created.

For more information about key management in Amazon Connect, see [Key management in Amazon Connect](key-management.md "key-management.md").

###### Contents

- [Amazon AppIntegrations](#encryption-at-rest-appintegrations "#encryption-at-rest-appintegrations")
- [Amazon Connect Cases](#encryption-at-rest-cases "#encryption-at-rest-cases")
- [Amazon Connect Customer Profiles](#encryption-at-rest-customer-profiles "#encryption-at-rest-customer-profiles")
- [Connect AI agents](#encryption-at-rest-wisdom "#encryption-at-rest-wisdom")
- [Amazon Connect Voice ID encryption at
  rest](#encryption-at-rest-voiceid "#encryption-at-rest-voiceid")
- [Outbound campaigns encryption at rest](#encryption-at-rest-outboundcommunications "#encryption-at-rest-outboundcommunications")
- [Forecasts, capacity plans, and
  schedules](#forecasts-encryption-at-rest- "#forecasts-encryption-at-rest-")

## Amazon AppIntegrations data encryption at

rest

When you create a DataIntegration encrypted with a customer managed key, Amazon AppIntegrations creates
a grant on your behalf by sending a `CreateGrant` request to AWS KMS.
Grants in AWS KMS are used to give Amazon AppIntegrations access to a KMS key in your account.

You can revoke access to the grant, or remove the access that Amazon AppIntegrations has to
the customer managed key at any time. If you do, Amazon AppIntegrations can not access any of the data
encrypted by the customer managed key, which affects operations that are dependent on that
data.

External application data that Amazon AppIntegrations processes is encrypted at rest in an S3
bucket using the customer managed key that you provided during configuration. Integration
configuration data is encrypted at rest using a key that is time-limited and
specific to the user account.

Amazon AppIntegrations requires the grant to use the customer managed key for the following internal
operations:

- Send `GenerateDataKeyRequest` to AWS KMS to generate data keys
  encrypted by your customer managed key.
- Send `Decrypt` requests to AWS KMS to decrypt encrypted data keys
  so that they can be used to encrypt your data.

## Amazon Connect Cases encryption at rest

All customer provided data in case fields, case comments, descriptions of the
fields and templates stored by Amazon Connect Cases is encrypted at rest using encryption
keys stored in AWS Key Management Service (AWS KMS).

Amazon Connect Cases service owns, manages, monitors, and rotates the encryption keys
(that is, AWS owned keys) to meet the high security standards. Payload of the case
event streams is temporarily (typically for a few seconds) stored in Amazon EventBridge before
it is made available through the default-bus in customers account. EventBridge also
encrypts the entire payload at rest using AWS owned keys.

## Amazon Connect Customer Profiles

encryption at rest

All user data stored in Amazon Connect Customer Profiles is encrypted at rest. Amazon Connect
Customer Profiles encryption at rest provides enhanced security by encrypting all
your data at rest using encryption keys stored in AWS Key Management Service (AWS KMS). This
functionality helps reduce the operational burden and complexity involved in
protecting sensitive data. With encryption at rest, you can build security-sensitive
applications that meet strict encryption compliance and regulatory
requirements.

Organizational policies, industry or government regulations, and compliance
requirements often require the use of encryption at rest to increase the data
security of your applications. Customer Profiles integrated with AWS KMS to enable its
encryption at rest strategy. For more information, see [AWS Key Management Service Concepts](../../../kms/latest/developerguide/concepts.md "../../../kms/latest/developerguide/concepts.md") in the
AWS Key Management Service Developer Guide.

When creating a new domain, you must provide a [KMS key](../../../kms/latest/developerguide/concepts.md#kms_keys "../../../kms/latest/developerguide/concepts.md#kms_keys") that the service
will use to encrypt your data in transit and at rest. The customer managed key is created,
owned, and managed by you. You have full control over the customer managed key (AWS KMS charges
apply).

You can specify an encryption key when you create a new domain or profile object
type or switch the encryption keys on an existing resources by using the AWS
Command Line Interface (AWS CLI), or the Amazon Connect Customer Profiles Encryption API. When
you choose a customer managed key, Amazon Connect Customer Profiles creates a grant to the customer managed key
that grants it access to the customer managed key.

AWS KMS charges apply for a customer managed key. For more information about pricing, see
[AWS KMS pricing](https://aws.amazon.com/kms/pricing/ "https://aws.amazon.com/kms/pricing/").

## Connect AI agents encryption at rest

All user data stored in Connect AI agents is encrypted at rest using encryption keys
stored in AWS Key Management Service. If you optionally provide a customer managed key, Connect AI agents uses it to
encrypt knowledge content stored at rest outside of Connect AI agents search indices.
Connect AI agents uses dedicated search indices per customer and they are encrypted at rest
by using AWS owned keys stored in AWS Key Management Service. Additionally, you can use CloudTrail to
audit any data access using the Connect AI agents APIs.

AWS KMS charges apply when using a key that you provide. For more information about
pricing, see [AWS KMS
pricing](https://aws.amazon.com/kms/pricing/ "https://aws.amazon.com/kms/pricing/").

## Amazon Connect Voice ID encryption at

rest

Amazon Connect Voice ID stores customer voiceprints which cannot be reverse-engineered to
obtain the enrolled customer's speech or identify a customer. All user data stored
in Amazon Connect Voice ID is encrypted at rest. When creating a new Voice ID domain, you
must provide a customer managed key that the service uses to encrypt your data at rest. The
customer managed key is created, owned, and managed by you. You have full control over the
key.

You can update the KMS key in the Voice ID domain by using the
`update-domain` command in AWS Command Line Interface (AWS CLI),
or the [UpdateDomain](../../../voiceid/latest/APIReference/API_UpdateDomain.md "../../../voiceid/latest/APIReference/API_UpdateDomain.md")
Voice ID API.

When you change the KMS key, an asynchronous process will be triggered to
re-encrypt the old data with the new KMS key. After this process completes, all of
your domain's data will be encrypted under the new KMS key, and you may safely
retire the old key. For more information, see [UpdateDomain](../../../voiceid/latest/APIReference/API_UpdateDomain.md "../../../voiceid/latest/APIReference/API_UpdateDomain.md").

Voice ID creates a grant to the customer managed key that grants it access to the key. For
more information, see [How Amazon Connect Voice ID uses grants in
AWS KMS](#voiceid-uses-grants "#voiceid-uses-grants").

Following is a list of data that is encrypted at rest using the customer managed key:

- **Voiceprints**: The voiceprints generated
  while enrolling the speakers and registering fraudsters into the
  system.
- **Speaker and fraudster audio**: The audio
  data used for enrolling the speakers and registering the fraudsters.
- **CustomerSpeakerId**: The customer-provided
  SpeakerId while enrolling the customer into Voice ID.
- **Customer-provided metadata**: These include
  free-form strings such as `Domain`
  `Description`, `Domain Name`, `Job Name`,
  and more.

AWS KMS charges apply for a customer managed key. For more information about pricing, see
[AWS KMS pricing](https://aws.amazon.com/kms/pricing/ "https://aws.amazon.com/kms/pricing/").

### How Amazon Connect Voice ID uses grants in

AWS KMS

Amazon Connect Voice ID requires a grant to use your customer managed key. When you create a
domain, Voice ID creates a grant on your behalf by sending a see [CreateGrant](../../../kms/latest/APIReference/API_CreateGrant.md "../../../kms/latest/APIReference/API_CreateGrant.md") request to AWS KMS. The grant is required to use your
customer managed key for the following internal operations:

- Send [DescribeKey](../../../kms/latest/APIReference/API_DescribeKey.md "../../../kms/latest/APIReference/API_DescribeKey.md") requests to AWS KMS to verify that the symmetric
  customer managed key ID provided is valid.
- Send [GenerateDataKey](../../../kms/latest/APIReference/API_GenerateDataKey.md "../../../kms/latest/APIReference/API_GenerateDataKey.md") requests to KMS key to create data keys
  with which to encrypt objects.
- Send [Decrypt](../../../kms/latest/APIReference/API_Decrypt.md "../../../kms/latest/APIReference/API_Decrypt.md")
  requests to AWS KMS to decrypt the encrypted data keys so that they can be
  used to encrypt your data.
- Send [ReEncrypt](../../../kms/latest/APIReference/API_ReEncrypt.md "../../../kms/latest/APIReference/API_ReEncrypt.md")
  requests to AWS KMS when the key is updated to re-encrypt a limited set of
  data using the new key.
- Store files in S3 using the AWS KMS key to encrypt the data.

You can revoke access to the grant, or remove the service's access to the
customer managed key at any time. If you do, Voice ID won't be able to access any of the
data encrypted by the customer managed key, which affects all the operations that are
dependent on that data, leading to `AccessDeniedException` errors and
failures in the asynchronous workflows.

### Customer managed key policy for

Voice ID

Key policies control access to your customer managed key. Every customer managed key must have
exactly one key policy, which contains statements that determine who can use the
key and how they can use it. When you create your customer managed key, you can specify a
key policy. For more information, see [Managing access to KMS keys](../../../kms/latest/developerguide/control-access-overview.md#managing-access "../../../kms/latest/developerguide/control-access-overview.md#managing-access") in the
_AWS Key Management Service Developer Guide_.

Following is an example key policy which gives a user the permissions they
need to call all Voice ID APIs using the customer managed key:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "Allow key access to Amazon Connect VoiceID.",
 "Effect": "Allow",
 "Principal": {
 "AWS": "`your_user_or_role_ARN`"
 },
 "Action": [
 "kms:CreateGrant",
 "kms:Decrypt",
 "kms:DescribeKey"
 ],
 "Resource": "*",
 "Condition": {
 "StringEquals": {
 "kms:ViaService": [
 "voiceid.`us-east-1`.amazonaws.com"
 ]
 }
 }
 }
 ]
}`

```

For information about specifying permissions in a policy, see [Specifying
KMS keys in IAM policy statements](../../../kms/latest/developerguide/cmks-in-iam-policies.md "../../../kms/latest/developerguide/cmks-in-iam-policies.md") in the AWS Key Management Service Developer Guide.

For information about troubleshooting key access, see [Troubleshooting key access](../../../kms/latest/developerguide/policy-evaluation.md "../../../kms/latest/developerguide/policy-evaluation.md") in the AWS Key Management Service Developer Guide.

### Voice ID encryption

context

An [encryption
context](../../../kms/latest/developerguide/concepts.md#encrypt_context "../../../kms/latest/developerguide/concepts.md#encrypt_context") is an optional set of key-value pairs that contain
additional contextual information about the data. AWS KMS uses the encryption
context as [additional
authenticated data](../../../encryption-sdk/latest/developer-guide/concepts.md "../../../encryption-sdk/latest/developer-guide/concepts.md") to support [authenticated encryption](../../../encryption-sdk/latest/developer-guide/concepts.md#digital-sigs "../../../encryption-sdk/latest/developer-guide/concepts.md#digital-sigs").

When you include an encryption context in a request to encrypt data, AWS KMS
binds the encryption context to the encrypted data. To decrypt data, you include
the same encryption context in the request.

Voice ID uses the same encryption context in all AWS KMS cryptographic
operations, where the key is `aws:voiceid:domain:arn` and the value
is the resource Amazon Resource Name (ARN) [Amazon Resource Name
(ARN)](../../../general/latest/gr/aws-arns-and-namespaces.md "../../../general/latest/gr/aws-arns-and-namespaces.md").

```
"encryptionContext": {
   "aws:voiceid:domain:arn": "arn:aws:voiceid:us-west-2:111122223333:domain/sampleDomainId"
}
```

You can also use the encryption context in audit records and logs to identify
how the customer managed key is being used. The encryption context also appears in logs
generated by CloudTrail or Amazon CloudWatch Logs.

#### Using encryption

context to control access to your customer managed key

You can use the encryption context in key policies and IAM policies as
conditions to control access to your symmetric customer managed key. You can also use
encryption context constraints in a grant.

Amazon Connect Voice ID uses an encryption context constraint in grants to control
access to the customer managed key in your account or Region. The grant constraint
requires that the operations that the grant allows use the specified
encryption context.

The following are example key policy statements to grant access to a
customer managed key for a specific encryption context. The condition in this policy
statement requires that the grants have an encryption context constraint
that specifies the encryption context.

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
             "kms:EncryptionContext:"aws:voiceid:domain:arn": "arn:aws:voiceid:us-west-2:111122223333:domain/sampleDomainId""
          }
     }
}
```

### Monitoring your encryption keys for

Voice ID

When you use an AWS KMS customer managed key with Voice ID, you can use [AWS CloudTrail](../../../awscloudtrail/latest/userguide/cloudtrail-user-guide.md "../../../awscloudtrail/latest/userguide/cloudtrail-user-guide.md") or [Amazon CloudWatch Logs](../../../AmazonCloudWatch/latest/logs/WhatIsCloudWatchLogs.md "../../../AmazonCloudWatch/latest/logs/WhatIsCloudWatchLogs.md") to track requests that Voice ID sends to AWS KMS.

The following examples is a sample AWS CloudTrail event for `CreateGrant`
operation called by Voice ID to access data encrypted by your customer managed key:

CreateGrant

```
{
    "eventVersion": "1.08",
    "userIdentity": {
        "type": "AssumedRole",
        "principalId": "AROA5STZEFPSZEOW7NP3X:SampleUser1",
        "arn": "arn:aws:sts::111122223333:assumed-role/SampleRole/SampleUser",
        "accountId": "111122223333",
        "accessKeyId": "AAAAAAA1111111EXAMPLE",
        "sessionContext": {
            "sessionIssuer": {
                "type": "Role",
                "principalId": "AROA5STZEFPSZEOW7NP3X",
                "arn": "arn:aws:iam::111122223333:role/SampleRole",
                "accountId": "111122223333",
                "userName": "SampleUser"
            },
            "webIdFederationData": {},
            "attributes": {
                "creationDate": "2021-09-14T23:02:23Z",
                "mfaAuthenticated": "false"
            }
        },
        "invokedBy": "voiceid.amazonaws.com"
    },
    "eventTime": "2021-09-14T23:02:50Z",
    "eventSource": "kms.amazonaws.com",
    "eventName": "CreateGrant",
    "awsRegion": "us-west-2",
    "sourceIPAddress": "SampleIpAddress",
    "userAgent": "Example Desktop/1.0 (V1; OS)",
    "requestParameters": {
        "constraints": {
            "encryptionContextSubset": {
                "aws:voiceid:domain:arn": "arn:aws:voiceid:us-west-2:111122223333:domain/sampleDomainId"
            }
        },
        "retiringPrincipal": "voiceid.amazonaws.com",
        "keyId": "arn:aws:kms:us-west-2:111122223333:key/44444444-3333-2222-1111-EXAMPLE11111",
        "operations": [
            "CreateGrant",
            "Decrypt",
            "DescribeKey",
            "GenerateDataKey",
            "GenerateDataKeyPair",
            "GenerateDataKeyPairWithoutPlaintext",
            "GenerateDataKeyWithoutPlaintext",
            "ReEncryptFrom",
            "ReEncryptTo"
        ],
        "granteePrincipal": "voiceid.amazonaws.com "
    },
    "responseElements": {
        "grantId": "00000000000000000000000000000cce47be074a8c379ed39f22b155c6e86af82"
    },
    "requestID": "ed0fe4ab-305b-4388-8adf-7e8e3a4e80fe",
    "eventID": "31d0d7c6-ce5b-4caf-901f-025bf71241f6",
    "readOnly": false,
    "resources": [
        {
            "accountId": "111122223333",
            "type": "AWS::KMS::Key",
            "ARN": "arn:aws:kms:us-west-2:111122223333:key/00000000-1111-2222-3333-9999999999999"
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
      "type": "AWSService",
      "invokedBy": "voiceid.amazonaws.com"
    },
    "eventTime": "2021-10-13T15:12:39Z",
    "eventSource": "kms.amazonaws.com",
    "eventName": "DescribeKey",
    "awsRegion": "us-west-2",
    "sourceIPAddress": "voiceid.amazonaws.com",
    "userAgent": "voiceid.amazonaws.com",
    "requestParameters": {
        "keyId": "alias/sample-key-alias"
    },
    "responseElements": null,
    "requestID": "ed0fe4ab-305b-4388-8adf-7e8e3a4e80fe",
    "eventID": "31d0d7c6-ce5b-4caf-901f-025bf71241f6",
    "readOnly": true,
    "resources": [{
        "accountId": "111122223333",
        "type": "AWS::KMS::Key",
        "ARN": "arn:aws:kms:us-west-2:111122223333:key/00000000-1111-2222-3333-9999999999999"
    }],
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
        "type": "AWSService",
        "invokedBy": "voiceid.amazonaws.com"
    },
    "eventTime": "2021-10-12T23:59:34Z",
    "eventSource": "kms.amazonaws.com",
    "eventName": "Decrypt",
    "awsRegion": "us-west-2",
    "sourceIPAddress": "voiceid.amazonaws.com",
    "userAgent": "voiceid.amazonaws.com",
    "requestParameters": {
        "encryptionContext": {
            "keyId": "arn:aws:kms:us-west-2:111122223333:key/44444444-3333-2222-1111-EXAMPLE11111",
            "encryptionContext": {
                "aws:voiceid:domain:arn": "arn:aws:voiceid:us-west-2:111122223333:domain/sampleDomainId"
            },
            "encryptionAlgorithm": "SYMMETRIC_DEFAULT"
        },
        "responseElements": null,
        "requestID": "ed0fe4ab-305b-4388-8adf-7e8e3a4e80fe",
        "eventID": "31d0d7c6-ce5b-4caf-901f-025bf71241f6",
        "readOnly": true,
        "resources": [{
            "accountId": "111122223333",
            "type": "AWS::KMS::Key",
            "ARN": "arn:aws:kms:us-west-2:111122223333:key/00000000-1111-2222-3333-9999999999999"
        }],
        "eventType": "AwsApiCall",
        "managementEvent": true,
        "recipientAccountId": "111122223333",
        "sharedEventID": "35d58aa1-26b2-427a-908f-025bf71241f6",
        "eventCategory": "Management"
    }
```

GenerateDataKeyWithoutPlaintext

```
{
    "eventVersion": "1.08",
    "userIdentity": {
        "type": "AWSService",
        "invokedBy": "voiceid.amazonaws.com"
    },
    "eventTime": "2021-10-13T00:26:41Z",
    "eventSource": "kms.amazonaws.com",
    "eventName": "GenerateDataKeyWithoutPlaintext",
    "awsRegion": "us-west-2",
    "sourceIPAddress": "voiceid.amazonaws.com",
    "userAgent": "voiceid.amazonaws.com",
    "requestParameters": {
        "keyId": "arn:aws:kms:us-west-2:111122223333:key/44444444-3333-2222-1111-EXAMPLE11111",
        "encryptionContext": {
            "aws:voiceid:domain:arn": "arn:aws:voiceid:us-west-2:111122223333:domain/sampleDomainId"
        },
        "keySpec": "AES_256"
    },
    "responseElements": null,
    "requestID": "ed0fe4ab-305b-4388-8adf-7e8e3a4e80fe",
    "eventID": "31d0d7c6-ce5b-4caf-901f-025bf71241f6",
    "readOnly": true,
    "resources": [{
        "accountId": "111122223333",
        "type": "AWS::KMS::Key",
        "ARN": "arn:aws:kms:us-west-2:111122223333:key/00000000-1111-2222-3333-9999999999999"
    }],
    "eventType": "AwsApiCall",
    "managementEvent": true,
    "recipientAccountId": "111122223333",
    "sharedEventID": "35d58aa1-26b2-427a-908f-025bf71241f6",
    "eventCategory": "Management"
}
```

ReEncrypt

```
{
    "eventVersion": "1.08",
    "userIdentity": {
        "type": "AWSService",
        "invokedBy": "voiceid.amazonaws.com"
    },
    "eventTime": "2021-10-13T00:59:05Z",
    "eventSource": "kms.amazonaws.com",
    "eventName": "ReEncrypt",
    "awsRegion": "us-west-2",
    "sourceIPAddress": "voiceid.amazonaws.com",
    "userAgent": "voiceid.amazonaws.com",
    "requestParameters": {
        "destinationEncryptionContext": {
            "aws:voiceid:domain:arn": "arn:aws:voiceid:us-west-2:111122223333:domain/sampleDomainId"
        },
        "destinationKeyId": "arn:aws:kms:us-west-2:111122223333:key/44444444-3333-2222-1111-EXAMPLE11111",
        "sourceEncryptionAlgorithm": "SYMMETRIC_DEFAULT",
        "sourceAAD": "SampleSourceAAAD+JXBmH+ZJNM73BfHE/dwQALXp7Sf44VwvoJOrLj",
        "destinationAAD": "SampleDestinationAAAD+JXBmH+ZJNM73BfHE/dwQALXp7Sf44VwvoJOrLj",
        "sourceEncryptionContext": {
            "aws:voiceid:domain:arn": "arn:aws:voiceid:us-west-2:111122223333:domain/sampleDomainId"
        },
        "destinationEncryptionAlgorithm": "SYMMETRIC_DEFAULT",
        "sourceKeyId": "arn:aws:kms:us-west-2:111122223333:key/55555555-3333-2222-1111-EXAMPLE22222"
    },
    "responseElements": null,
    "requestID": "ed0fe4ab-305b-4388-8adf-7e8e3a4e80fe",
    "eventID": "31d0d7c6-ce5b-4caf-901f-025bf71241f6",
    "readOnly": true,
    "resources": [{
            "accountId": "111122223333",
            "type": "AWS::KMS::Key",
            "ARN": "arn:aws:kms:us-west-2:111122223333:key/00000000-1111-2222-3333-9999999999999"
        },
        {
            "accountId": "111122223333",
            "type": "AWS::KMS::Key",
            "ARN": "arn:aws:kms:us-west-2:111122223333:key/00000000-1111-2222-3333-7777777777777"
        }
    ],
    "eventType": "AwsApiCall",
    "managementEvent": true,
    "recipientAccountId": "111122223333",
    "sharedEventID": "35d58aa1-26b2-427a-908f-025bf71241f6",
    "eventCategory": "Management"
}
```

## Outbound

campaigns encryption at rest

Outbound campaigns stores customer phone numbers and relevant attributes. This
information is always encrypted at rest, using either a customer managed key or an
AWS owned key. The data is separated by the Amazon Connect instance ID and is
encrypted by instance specific keys.

You can provide your own customer managed key when onboarding to
Outbound campaigns.

The service uses your customer-managed key to encrypt sensitive data at rest.
This key is created, owned, and fully managed by you, giving you complete control
over its usage and security.

If you do not provide your own customer managed key, then Outbound campaigns encrypts
sensitive data at rest using an AWS owned key specific to your Amazon Connect
instance. You can't view, manage, use, or audit AWS owned keys. However, you don't
have to take any action or change any programs to protect the keys that encrypt your
data. For more information, see [AWS owned
keys](../../../kms/latest/developerguide/concepts.md#aws-owned-cmk "../../../kms/latest/developerguide/concepts.md#aws-owned-cmk") in the _AWS Key Management Service Developer Guide_.

AWS KMS charges apply for a customer managed key. For more information about
pricing, see [AWS KMS pricing](https://aws.amazon.com/kms/pricing/ "https://aws.amazon.com/kms/pricing/").

### How outbound

campaigns uses grants in AWS KMS

Outbound campaigns requires a grant to use your customer managed key. When
you onboard to outbound campaigns using the AWS console or the
`StartInstanceOnboardingJob` API, Outbound campaigns creates a grant
on your behalf by sending a `CreateGrant` request to AWS KMS. Grants in
AWS KMS are used to give the Amazon Connect Outbound campaigns service-linked role
access to a KMS key in your account.

Outbound campaigns requires the grant to use the customer managed key for the
following internal operations:

- Send [DescribeKey](../../../kms/latest/APIReference/API_DescribeKey.md "../../../kms/latest/APIReference/API_DescribeKey.md") requests to AWS KMS to verify that the symmetric
  customer managed key ID provided is valid.
- Send a `GenerateDataKeyWithoutPlainText` request to AWS KMS
  to generate data keys encrypted by your customer managed key.
- Send `Decrypt` requests to AWS KMS to decrypt encrypted data
  keys so that they can be used to encrypt your data.

You can revoke access to the grant, or remove the access that outbound
campaigns has to the customer managed key at any time. If you do, outbound
campaigns can not access any of the data encrypted by the customer managed key,
which affects operations that are dependent on that data.

### Customer

managed key policy for outbound campaigns

Key policies control access to your customer managed key. Every customer
managed key must have exactly one key policy, which contains statements that
determine who can use the key and how they can use it. When you create your
customer managed key, you can specify a key policy. For more information, see
[Managing access to KMS keys](../../../kms/latest/developerguide/control-access-overview.md#managing-access "../../../kms/latest/developerguide/control-access-overview.md#managing-access") in the _AWS Key Management Service Developer
Guide_.

Following is an example key policy which gives a user the permissions they
need to call outbound campaigns [StartInstanceOnboardingJob](../APIReference/API_connect-outbound-campaigns_StartInstanceOnboardingJob.md "../APIReference/API_connect-outbound-campaigns_StartInstanceOnboardingJob.md"), [PutDialRequestBatch](../APIReference/API_connect-outbound-campaigns_PutDialRequestBatch.md "../APIReference/API_connect-outbound-campaigns_PutDialRequestBatch.md") and [PutOutboundRequestBatch](../APIReference/API_connect-outbound-campaigns_PutOutboundRequestBatch.md "../APIReference/API_connect-outbound-campaigns_PutOutboundRequestBatch.md") API using the customer managed key:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "Allow key access to Amazon Connect outbound campaigns.",
 "Effect": "Allow",
 "Principal": {
 "AWS": "`your_user_or_role_ARN`"
 },
 "Action": [
 "kms:Decrypt",
 "kms:CreateGrant"
 ],
 "Resource": "*",
 "Condition": {
 "StringEquals": {
 "kms:ViaService": "connect-campaigns.`us-east-1`.amazonaws.com",
 "kms:EncryptionContext:aws:accountId": "`111122223333`",
 "kms:EncryptionContext:aws:connect:instanceId": "`InstanceID`"
 }
 }
 },
 {
 "Sid": "Allow direct access to key metadata to the account",
 "Effect": "Allow",
 "Principal": {
 "AWS": "arn:aws:iam::`111122223333`:root"
 },
 "Action": [
 "kms:Describe*"
 ],
 "Resource": "*"
 }
 ]
}`

```

For information about specifying permissions in a policy, see [Specifying KMS
keys in IAM policy statements](../../../kms/latest/developerguide/cmks-in-iam-policies.md "../../../kms/latest/developerguide/cmks-in-iam-policies.md") in the AWS Key Management Service Developer Guide.

For information about troubleshooting key access, see [Troubleshooting key access](../../../kms/latest/developerguide/policy-evaluation.md "../../../kms/latest/developerguide/policy-evaluation.md") in the AWS Key Management Service Developer Guide.

### Outbound campaigns

encryption context

An [encryption
context](../../../kms/latest/developerguide/concepts.md#encrypt_context "../../../kms/latest/developerguide/concepts.md#encrypt_context") is an optional set of key-value pairs that contain
additional contextual information about the data. AWS KMS uses the encryption
context as [additional
authenticated data](../../../encryption-sdk/latest/developer-guide/concepts.md "../../../encryption-sdk/latest/developer-guide/concepts.md") to support [authenticated encryption](../../../encryption-sdk/latest/developer-guide/concepts.md#digital-sigs "../../../encryption-sdk/latest/developer-guide/concepts.md#digital-sigs").

When you include an encryption context in a request to encrypt data, AWS KMS
binds the encryption context to the encrypted data. To decrypt data, you include
the same encryption context in the request.

Outbound campaigns uses the same encryption context in all AWS KMS
cryptographic operations, where the key are aws:accountId and
aws:connect:instanceId and the value is the aws account id and Connect instance
id.

```
"encryptionContext": {
   "aws:accountId": "111122223333",
   "aws:connect:instanceId": "sample instance id"
}
```

You can also use the encryption context in audit records and logs to identify
how the customer managed key is being used. The encryption context also appears
in logs generated by CloudTrail or Amazon CloudWatch Logs.

#### Using encryption context to control access to your customer managed

key

You can use the encryption context in key policies and IAM policies as
conditions to control access to your symmetric customer managed key. You can
also use encryption context constraints in a grant.

Outbound campaigns uses an encryption context constraint in grants to
control access to the customer managed key in your account or region. The
grant constraint requires that the operations that the grant allows use the
specified encryption context.

The following are example key policy statements to grant access to a
customer managed key for a specific encryption context. The condition in
this policy statement requires that the grants have an encryption context
constraint that specifies the encryption context.

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
             "kms:EncryptionContext:aws:accountId": "111122223333",
             "kms:EncryptionContext:aws:connect:instanceId": "sample instance id"
          }
     }
}
```

### Monitoring your encryption keys for Outbound campaigns

When you use an AWS KMS customer managed key with your outbound campaigns
resources, you can use [AWS CloudTrail](../../../awscloudtrail/latest/userguide/cloudtrail-user-guide.md "../../../awscloudtrail/latest/userguide/cloudtrail-user-guide.md") or [Amazon CloudWatch Logs](../../../AmazonCloudWatch/latest/logs/WhatIsCloudWatchLogs.md "../../../AmazonCloudWatch/latest/logs/WhatIsCloudWatchLogs.md") to track
requests that Amazon Location sends to AWS KMS.

The following examples are AWS CloudTrail events for CreateGrant,
GenerateDataKeyWithoutPlainText, DescribeKey, and Decrypt to monitor KMS
operations called by Amazon Location to access data encrypted by your customer
managed key:

CreateGrant

```
{
  "eventVersion": "1.09",
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
        "arn": "arn:aws:iam::111122223333:role/Admin/Sampleuser01",
        "accountId": "111122223333",
        "userName": "Admin"
      },
      "attributes": {
        "creationDate": "2024-08-27T18:40:57Z",
        "mfaAuthenticated": "false"
      }
    },
    "invokedBy": "connect-campaigns.amazonaws.com"
  },
  "eventTime": "2024-08-27T18:46:29Z",
  "eventSource": "kms.amazonaws.com",
  "eventName": "CreateGrant",
  "awsRegion": "us-west-2",
  "sourceIPAddress": "connect-campaigns.amazonaws.com",
  "userAgent": "connect-campaigns.amazonaws.com",
  "requestParameters": {
    "constraints": {
      "encryptionContextSubset": {
        "aws:connect:instanceId": "1234abcd-12ab-34cd-56ef-123456SAMPLE",
        "aws:accountId": "111122223333"
      }
    },
    "granteePrincipal": "arn:aws:iam::111122223333:role/aws-service-role/connect-campaigns.amazonaws.com/AWSServiceRoleForConnectCampaigns_EXAMPLE",
    "retiringPrincipal": "arn:aws:iam::111122223333:role/aws-service-role/connect-campaigns.amazonaws.com/AWSServiceRoleForConnectCampaigns_EXAMPLE",
    "keyId": "arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-123456SAMPLE",
    "operations": [
      "Decrypt",
      "Encrypt",
      "DescribeKey",
      "GenerateDataKey",
      "GenerateDataKeyWithoutPlaintext",
      "ReEncryptFrom",
      "ReEncryptTo"
    ]
  },
  "responseElements": {
    "grantId": "0ab0ac0d0b000f00ea00cc0a0e00fc00bce000c000f0000000c0bc0a0000aaafSAMPLE",
    "keyId": "arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-123456SAMPLE"
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
  "recipientAccountId": "111122223333",
  "eventCategory": "Management",
  "sessionCredentialFromConsole": "true"
}

```

GenerateDataKeyWithoutPlainText

```
{
  "eventVersion": "1.09",
  "userIdentity": {
    "type": "AssumedRole",
    "principalId": "AROAIGDTESTANDEXAMPLE:connect-campaigns-session",
    "arn": "arn:aws:sts::111122223333:assumed-role/AWSServiceRoleForConnectCampaigns_EXAMPLE/connect-campaigns-session",
    "accountId": "111122223333",
    "accessKeyId": "AROAIGDTESTANDEXAMPLE",
    "sessionContext": {
      "sessionIssuer": {
        "type": "Role",
        "principalId": "AROAIGDTESTANDEXAMPLE",
        "arn": "arn:aws:iam::111122223333:role/aws-service-role/connect-campaigns.amazonaws.com/AWSServiceRoleForConnectCampaigns_EXAMPLE",
        "accountId": "111122223333",
        "userName": "AWSServiceRoleForConnectCampaigns_EXAMPLE"
      },
      "attributes": {
        "creationDate": "2024-08-27T18:46:29Z",
        "mfaAuthenticated": "false"
      }
    },
    "invokedBy": "connect-campaigns.amazonaws.com"
  },
  "eventTime": "2024-08-27T18:46:29Z",
  "eventSource": "kms.amazonaws.com",
  "eventName": "GenerateDataKeyWithoutPlaintext",
  "awsRegion": "us-west-2",
  "sourceIPAddress": "connect-campaigns.amazonaws.com",
  "userAgent": "connect-campaigns.amazonaws.com",
  "requestParameters": {
    "encryptionContext": {
      "aws:connect:instanceId": "1234abcd-12ab-34cd-56ef-123456SAMPLE",
      "aws:accountId": "111122223333"
    },
    "keyId": "arn:aws:kms:us-west-2:586277393662:key/1234abcd-12ab-34cd-56ef-123456SAMPLE",
    "keySpec": "AES_256"
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
  "recipientAccountId": "111122223333",
  "eventCategory": "Management"
}


```

DescribeKey

```
{
  "eventVersion": "1.09",
  "userIdentity": {
    "type": "AssumedRole",
    "principalId": "AROAIGDTESTANDEXAMPLE:connect-campaigns-session",
    "arn": "arn:aws:sts::111122223333:assumed-role/AWSServiceRoleForConnectCampaigns_EXAMPLE/connect-campaigns-session",
    "accountId": "111122223333",
    "accessKeyId": "AROAIGDTESTANDEXAMPLE",
    "sessionContext": {
      "sessionIssuer": {
        "type": "Role",
        "principalId": "AROAIGDTESTANDEXAMPLE",
        "arn": "arn:aws:iam::111122223333:role/aws-service-role/connect-campaigns.amazonaws.com/AWSServiceRoleForConnectCampaigns_EXAMPLE",
        "accountId": "111122223333",
        "userName": "AWSServiceRoleForConnectCampaigns_EXAMPLE"
      },
      "attributes": {
        "creationDate": "2024-08-27T18:46:29Z",
        "mfaAuthenticated": "false"
      }
    },
    "invokedBy": "connect-campaigns.amazonaws.com"
  },
  "eventTime": "2024-08-27T18:46:29Z",
  "eventSource": "kms.amazonaws.com",
  "eventName": "DescribeKey",
  "awsRegion": "us-west-2",
  "sourceIPAddress": "connect-campaigns.amazonaws.com",
  "userAgent": "connect-campaigns.amazonaws.com",
  "requestParameters": {
    "keyId": "arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-123456SAMPLE",
    "grantTokens": [
      "EL7BPAGG-KDm8661M1pl55WcQD_9ZgFwYXN-SAMPLE"
    ]
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
  "recipientAccountId": "111122223333",
  "eventCategory": "Management"
}


```

Decrypt

```
{
  "eventVersion": "1.09",
  "userIdentity": {
    "type": "AssumedRole",
    "principalId": "AROAIGDTESTANDEXAMPLE:Sampleuser01",
    "arn": "arn:aws:sts::111122223333:assumed-role/Admin/Sampleuser01",
    "accountId": "111122223333",
    "accessKeyId": "AKIAIOSFODNN7EXAMPLE3",
    "sessionContext": {
      "sessionIssuer": {
        "type": "Role",
        "principalId": "AKIAIOSFODNN7EXAMPLE3",
        "arn": "arn:aws:iam::111122223333:role/Admin/Sampleuser01",
        "accountId": "111122223333",
        "userName": "Admin"
      },
      "attributes": {
        "creationDate": "2024-08-27T18:40:57Z",
        "mfaAuthenticated": "false"
      }
    },
    "invokedBy": "connect-campaigns.amazonaws.com"
  },
  "eventTime": "2024-08-27T19:09:02Z",
  "eventSource": "kms.amazonaws.com",
  "eventName": "Decrypt",
  "awsRegion": "us-west-2",
  "sourceIPAddress": "connect-campaigns.amazonaws.com",
  "userAgent": "connect-campaigns.amazonaws.com",
  "requestParameters": {
    "encryptionContext": {
      "aws:connect:instanceId": "1234abcd-12ab-34cd-56ef-123456SAMPLE",
      "aws:accountId": "111122223333"
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
  "recipientAccountId": "111122223333",
  "eventCategory": "Management",
  "sessionCredentialFromConsole": "true"
}


```

## Forecasts, capacity plans, and

schedules

When you create forecasts, capacity plans, and schedules, all data are encrypted
at rest using AWS owned key encryption keys stored in AWS Key Management Service.
