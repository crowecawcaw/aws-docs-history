# Data protection in Amazon VPC Lattice

The AWS [shared responsibility model](https://aws.amazon.com/compliance/shared-responsibility-model/ "https://aws.amazon.com/compliance/shared-responsibility-model/")
applies to data protection in Amazon VPC Lattice. As described in this model, AWS is
responsible for protecting the global infrastructure that runs all of the AWS Cloud. You are
responsible for maintaining control over your content that is hosted on this infrastructure.
This content includes the security configuration and management tasks for the AWS services
that you use. For more information about data privacy, see the [Data Privacy FAQ](https://aws.amazon.com/compliance/data-privacy-faq/ "https://aws.amazon.com/compliance/data-privacy-faq/"). For information about data protection in Europe, see the [AWS Shared
Responsibility Model and GDPR](https://aws.amazon.com/blogs/security/the-aws-shared-responsibility-model-and-gdpr/ "https://aws.amazon.com/blogs/security/the-aws-shared-responsibility-model-and-gdpr/") blog post on the _AWS Security
Blog_.

## Encryption in transit

VPC Lattice is a fully managed service that consists of a control plane and a data plane.
Each plane serves a distinct purpose in the service. The control plane provides the
administrative APIs used to create, read/describe, update, delete, and list (CRUDL) resources
(for example, `CreateService` and `UpdateService`). Communications to
the VPC Lattice control plane are protected in-transit by TLS. The data plane is the VPC Lattice
Invoke API, which provides the interconnection between services. TLS encrypts communications
to the VPC Lattice data plane when you use HTTPS or TLS. The cipher suite and protocol version
use defaults provided by VPC Lattice and are not configurable. For more information, see [HTTPS listeners for VPC Lattice services](https-listeners.md "https-listeners.md").

## Encryption at rest

By default, encryption of data at rest helps reduce the operational overhead and
complexity involved in protecting sensitive data. At the same time, it enables you to build
secure applications that meet strict encryption compliance and regulatory requirements.

###### Contents

- [Server-side encryption with Amazon S3 managed keys (SSE-S3)](#s3-managed-keys "#s3-managed-keys")
- [Server-side encryption with AWS KMS keys stored in AWS KMS (SSE-KMS)](#kms-managed-keys "#kms-managed-keys")

### Server-side encryption with Amazon S3 managed keys (SSE-S3)

When you use server-side encryption with Amazon S3 managed keys (SSE-S3), each object is
encrypted with a unique key. As an additional safeguard, we encrypt the key itself with a
root key that we regularly rotates. Amazon S3 server-side encryption uses one of the strongest
block ciphers available, 256-bit Advanced Encryption Standard (AES-256) GCM, to encrypt your
data. For objects encrypted prior to AES-GCM, AES-CBC is still supported to decrypt those
objects. For more information, see [Using server-side
encryption with Amazon S3-managed encryption keys (SSE-S3)](../../../AmazonS3/latest/userguide/UsingServerSideEncryption.md "../../../AmazonS3/latest/userguide/UsingServerSideEncryption.md").

If you enable server-side encryption with Amazon S3-managed encryption keys (SSE-S3) for your
S3 bucket for VPC Lattice access logs, we automatically encrypt each access log file before it
is stored in your S3 bucket. For more information, see [Logs sent to Amazon S3](../../../AmazonCloudWatch/latest/logs/AWS-logs-and-resource-policy.md#AWS-logs-infrastructure-S3 "../../../AmazonCloudWatch/latest/logs/AWS-logs-and-resource-policy.md#AWS-logs-infrastructure-S3") in the _Amazon CloudWatch User Guide_.

### Server-side encryption with AWS KMS keys stored in AWS KMS (SSE-KMS)

Server-side encryption with AWS KMS keys (SSE-KMS) is similar to SSE-S3, but with
additional benefits and charges for using this service. There are separate permissions for
the AWS KMS key that provides added protection against unauthorized access of your objects in
Amazon S3. SSE-KMS also provides you with an audit trail that shows when your AWS KMS key was used
and by whom. For more information, see [Using server-side encryption with
AWS Key Management Service (SSE-KMS)](../../../AmazonS3/latest/userguide/UsingKMSEncryption.md "../../../AmazonS3/latest/userguide/UsingKMSEncryption.md").

###### Contents

- [Encryption and decryption of your certificate’s private key](#private-key "#private-key")
- [Encryption context for VPC Lattice](#encryption-context "#encryption-context")
- [Monitoring your encryption keys for VPC Lattice](#monitoring-encryption-keys "#monitoring-encryption-keys")

#### Encryption and decryption of your certificate’s private key

Your ACM certificate and private key are encrypted using an AWS managed KMS key
that has the alias **aws/acm**. You can view the key ID with
this alias in the AWS KMS console under **AWS managed keys**.

VPC Lattice does not directly access your ACM resources. It uses AWS TLS Connection
Manager to secure and access the private keys for your certificate. When you use your
ACM certificate to create a VPC Lattice service, VPC Lattice associates your certificate with
AWS TLS Connection Manager. This is done by creating a grant in AWS KMS against your AWS
Managed Key with the prefix **aws/acm**. A grant is a policy
instrument that allows TLS Connection Manager to use KMS keys in cryptographic operations.
The grant allows the grantee principal (TLS Connection Manager) to call the specified
grant operations on the KMS key to decrypt your certificate's private key. TLS Connection
Manager then uses the certificate and the decrypted (plaintext) private key to establish a
secure connection (SSL/TLS session) with clients of VPC Lattice services. When the
certificate is disassociated from a VPC Lattice service, the grant is retired.

If you want to remove access to the KMS key, we recommend that you replace or delete
the certificate from the service using the AWS Management Console or the `update-service`
command in the AWS CLI.

#### Encryption context for VPC Lattice

An [encryption context](../../../kms/latest/developerguide/encrypt_context.md "../../../kms/latest/developerguide/encrypt_context.md")
is an optional set of key-value pairs that contain contextual
information about what your private key might be used for. AWS KMS binds the encryption
context to the encrypted data and uses it as additional authenticated data to support
authenticated encryption.

When your TLS keys are used with VPC Lattice and TLS Connection manager, the name of your
VPC Lattice service is included in the encryption context used to encrypt your key at rest.
You can verify which VPC Lattice service your certificate and private key are being used for
by viewing the encryption context in your CloudTrail logs as shown in the next section, or by
looking at the **Associated Resources** tab in the ACM console.

To decrypt data, the same encryption context is included in the request. VPC Lattice uses
the same encryption context in all AWS KMS cryptographic operations, where the key is
`aws:vpc-lattice:arn` and the value is the Amazon Resource Name (ARN) of the
VPC Lattice service.

The following example shows the encryption context in the output of an operation such
as `CreateGrant`.

```
"encryptionContextEquals": {
    "aws:acm:arn": "arn:aws:acm:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab",
    "aws:vpc-lattice:arn": "arn:aws:vpc-lattice:us-west-2:111122223333:service/svc-0b23c1234567890ab"
}
```

#### Monitoring your encryption keys for VPC Lattice

When you use an AWS managed key with your VPC Lattice service, you can use [AWS CloudTrail](../../../awscloudtrail/latest/userguide.md "../../../awscloudtrail/latest/userguide.md") to
track requests that VPC Lattice sends to AWS KMS.

###### CreateGrant

When you add your ACM certificate to a VPC Lattice service, a `CreateGrant`
request is sent on your behalf for TLS Connection Manager to be able to decrypt the
private key associated with your ACM certificate

You can view the `CreateGrant` operation as an event in **CloudTrail**,
**Event history**, **CreateGrant**.

The following is an example event record in the CloudTrail event history for the
`CreateGrant` operation.

```
{
    "eventVersion": "1.08",
    "userIdentity": {
        "type": "IAMUser",
        "principalId": "EX_PRINCIPAL_ID",
        "arn": "arn:aws:iam::111122223333:user/Alice",
        "accountId": "111122223333",
        "accessKeyId": "EXAMPLE_KEY_ID",
        "sessionContext": {
            "sessionIssuer": {
                "type": "IAMUser",
                "principalId": "EX_PRINCIPAL_ID",
                "arn": "arn:aws:iam::111122223333:user/Alice",
                "accountId": "111122223333",
                "userName": "Alice"
            },
            "webIdFederationData": {},
            "attributes": {
                "creationDate": "2023-02-06T23:30:50Z",
                "mfaAuthenticated": "false"
            }
        },
        "invokedBy": "acm.amazonaws.com"
    },
    "eventTime": "2023-02-07T00:07:18Z",
    "eventSource": "kms.amazonaws.com",
    "eventName": "CreateGrant",
    "awsRegion": "us-west-2",
    "sourceIPAddress": "acm.amazonaws.com",
    "userAgent": "acm.amazonaws.com",
    "requestParameters": {
        "granteePrincipal": "tlsconnectionmanager.amazonaws.com",
        "keyId": "1234abcd-12ab-34cd-56ef-1234567890ab",
        "operations": [
            "Decrypt"
        ],
        "constraints": {
            "encryptionContextEquals": {
                "aws:acm:arn": "arn:aws:acm:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab",
                "aws:vpc-lattice:arn": "arn:aws:vpc-lattice:us-west-2:111122223333:service/svc-0b23c1234567890ab"
            }
        },
        "retiringPrincipal": "acm.us-west-2.amazonaws.com"
    },
    "responseElements": {
        "grantId": "f020fe75197b93991dc8491d6f19dd3cebb24ee62277a05914386724f3d48758",
        "keyId": "arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"
    },
    "requestID": "ba178361-8ab6-4bdd-9aa2-0d1a44b2974a",
    "eventID": "8d449963-1120-4d0c-9479-f76de11ce609",
    "readOnly": false,
    "resources": [
        {
            "accountId": "111122223333",
            "type": "AWS::KMS::Key",
            "ARN": "arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"
        }
    ],
    "eventType": "AwsApiCall",
    "managementEvent": true,
    "recipientAccountId": "111122223333",
    "eventCategory": "Management"
}
```

In the above `CreateGrant` example, the grantee principal is TLS Connection
Manager, and the encryption context has the VPC Lattice service ARN.

###### ListGrants

You can use your KMS key ID and your account ID to call the `ListGrants`
API. This gets you a list of all grants for the specified KMS key. For more information,
see [ListGrants](../../../kms/latest/APIReference/API_ListGrants.md "../../../kms/latest/APIReference/API_ListGrants.md").

Use the following `ListGrants` command in the AWS CLI to see the details of
all the grants.

```
aws kms list-grants —key-id `your-kms-key-id`
```

The following is example output.

```
{
    "Grants": [
        {
            "Operations": [
                "Decrypt"
            ],
            "KeyId": "arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab",
            "Name": "IssuedThroughACM",
            "RetiringPrincipal": "acm.us-west-2.amazonaws.com",
            "GranteePrincipal": "tlsconnectionmanager.amazonaws.com",
            "GrantId": "f020fe75197b93991dc8491d6f19dd3cebb24ee62277a05914386724f3d48758",
            "IssuingAccount": "arn:aws:iam::111122223333:root",
            "CreationDate": "2023-02-06T23:30:50Z",
            "Constraints": {
                "encryptionContextEquals": {
                  "aws:acm:arn": "arn:aws:acm:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab",
                  "aws:vpc-lattice:arn": "arn:aws:vpc-lattice:us-west-2:111122223333:service/svc-0b23c1234567890ab"
                }
            }
        }
    ]
}
```

In the above `ListGrants` example, the grantee principal is TLS Connection
Manager and the encryption context has the VPC Lattice service ARN.

###### Decrypt

VPC Lattice uses TLS Connection Manager to call the `Decrypt` operation to
decrypt your private key in order to serve TLS connections in your VPC Lattice service. You
can view the `Decrypt` operation as an event in **CloudTrail**
**Event history**, **Decrypt**.

The following is an example event record in the CloudTrail event history for the
`Decrypt` operation.

```
{
    "eventVersion": "1.08",
    "userIdentity": {
        "type": "AWSService",
        "invokedBy": "tlsconnectionmanager.amazonaws.com"
    },
    "eventTime": "2023-02-07T00:07:23Z",
    "eventSource": "kms.amazonaws.com",
    "eventName": "Decrypt",
    "awsRegion": "us-west-2",
    "sourceIPAddress": "tlsconnectionmanager.amazonaws.com",
    "userAgent": "tlsconnectionmanager.amazonaws.com",
    "requestParameters": {
        "encryptionContext": {
            "aws:acm:arn": "arn:aws:acm:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab",
            "aws:vpc-lattice:arn": "arn:aws:vpc-lattice:us-west-2:111122223333:service/svc-0b23c1234567890ab"
        },
        "encryptionAlgorithm": "SYMMETRIC_DEFAULT"
    },
    "responseElements": null,
    "requestID": "12345126-30d5-4b28-98b9-9153da559963",
    "eventID": "abcde202-ba1a-467c-b4ba-f729d45ae521",
    "readOnly": true,
    "resources": [
        {
            "accountId": "111122223333",
            "type": "AWS::KMS::Key",
            "ARN": "arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"
        }
    ],
    "eventType": "AwsApiCall",
    "managementEvent": true,
    "recipientAccountId": "111122223333",
    "sharedEventID": "abcde202-ba1a-467c-b4ba-f729d45ae521",
    "eventCategory": "Management"
}
```
