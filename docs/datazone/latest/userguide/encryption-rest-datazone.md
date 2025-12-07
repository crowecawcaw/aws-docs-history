# Data encryption at rest for Amazon DataZone

Encryption of data at rest by default helps reduce the operational overhead and complexity
involved in protecting sensitive data. At the same time, it enables you to build secure
applications that meet strict encryption compliance and regulatory requirements.

Amazon DataZone uses default AWS-owned keys to automatically encrypt your data at rest. You
can't view, manage, or audit the use of AWS owned keys. For more information, see [AWS owned keys](../../../kms/latest/developerguide/concepts.md#aws-owned-cmk "../../../kms/latest/developerguide/concepts.md#aws-owned-cmk").

While you can't disable this layer of encryption or select an alternate encryption type,
you can choose a customer-managed key when you create your Amazon DataZone domains. Amazon DataZone
supports the use of a symmetric customer managed keys that you can create, own, and manage.
Because you have full control of encryption, you can perform the following tasks:

- Establish and maintain key policies
- Establish and maintain IAM policies and grants
- Enable and disable key policies
- Rotate key cryptographic material
- Add tags
- Create key aliases
- Schedule keys for deletion
  To use your own key, choose a customer managed key when you create your Amazon DataZone
  domain.

For more information, see [Customer managed keys](../../../kms/latest/developerguide/concepts.md#customer-cmk "../../../kms/latest/developerguide/concepts.md#customer-cmk").

###### Note

Amazon DataZone automatically enables encryption at rest using AWS owned keys to protect
customer data at no charge.

AWS KMS charges apply for using a customer managed keys. For more information about
pricing, see [AWS Key Management Service
Pricing](https://aws.amazon.com/kms/pricing/ "https://aws.amazon.com/kms/pricing/").

## How Amazon DataZone uses grants in AWS KMS

Amazon DataZone requires two [grants](../../../kms/latest/developerguide/grants.md "../../../kms/latest/developerguide/grants.md") to
use your customer managed key. When you create a Amazon DataZone domain encrypted with a customer
managed key, Amazon DataZone creates grants on your behalf by sending [CreateGrant](../../../kms/latest/APIReference/API_CreateGrant.md "../../../kms/latest/APIReference/API_CreateGrant.md") requests to AWS KMS. Grants in AWS KMS are used to give
Amazon DataZone access to a KMS key in your account. Amazon DataZone creates the following grants to
use your customer managed key for the following internal operations:

**One grant for encrypting your data at rest for the following
operations:**

- Send [DescribeKey](../../../kms/latest/APIReference/API_DescribeKey.md "../../../kms/latest/APIReference/API_DescribeKey.md") requests to AWS KMS to verify that the symmetric customer
  managed KMS key ID entered when creating a Amazon DataZone domain is valid.
- Send [GenerateDataKey](../../../kms/latest/APIReference/API_GenerateDataKey.md "../../../kms/latest/APIReference/API_GenerateDataKey.md") to AWS KMS to generate data keys encrypted by your customer
  managed key.
- Send [Decrypt](../../../kms/latest/APIReference/API_Decrypt.md "../../../kms/latest/APIReference/API_Decrypt.md") request enables Amazon DataZone to decrypt stored data.
- [RetireGrant](../../../kms/latest/APIReference/API_RetireGrant.md "../../../kms/latest/APIReference/API_RetireGrant.md") to retire the grant when domain is deleted.

**One grant for search, discovery, and [export](../../../sagemaker-unified-studio/latest/adminguide/sagemaker-unified-studio-export-asset-metadata-kms-permissions.md "../../../sagemaker-unified-studio/latest/adminguide/sagemaker-unified-studio-export-asset-metadata-kms-permissions.md") of your data:**

- [DescribeKey](../../../kms/latest/APIReference/API_DescribeKey.md "../../../kms/latest/APIReference/API_DescribeKey.md") - provides the customer managed key details that allow Amazon DataZone
  to validate the key.
- [Decrypt](../../../kms/latest/APIReference/API_Decrypt.md "../../../kms/latest/APIReference/API_Decrypt.md") - allows Amazon DataZone to decrypt stored data.

You can revoke access to the grant to the customer managed key at any time. If you do,
Amazon DataZone won't be able to access any of the data encrypted by the customer managed key,
which affects operations that are dependent on that data.

## Create a customer managed key

You can create a symmetric customer managed key by using the AWS Management Console,
or the AWS KMS APIs.

To create a symmetric customer managed key, follow the steps for [Creating symmetric customer managed key](../../../kms/latest/developerguide/create-keys.md#create-symmetric-cmk "../../../kms/latest/developerguide/create-keys.md#create-symmetric-cmk") in the AWS Key Management Service
Developer Guide.

**Key policy** - key policies control access to your
customer managed key. Every customer managed key must have exactly one key policy, which
contains statements that determine who can use the key and how they can use it. When you
create your customer managed key, you can specify a key policy. For more information, see
[Managing
access to customer managed keys](../../../kms/latest/developerguide/overview.md "../../../kms/latest/developerguide/overview.md") in the AWS Key Management Service Developer
Guide.

To use your customer managed key with your Amazon DataZone resources, the following API
operations must be permitted in the key policy:

- [kms:CreateGrant](../../../kms/latest/APIReference/API_CreateGrant.md "../../../kms/latest/APIReference/API_CreateGrant.md") – adds a grant to a customer managed key. Grants control
  access to a specified KMS key, which allows access to [grant operations](../../../kms/latest/developerguide/grants.md#terms-grant-operations "../../../kms/latest/developerguide/grants.md#terms-grant-operations") Amazon DataZone requires. For more information about [Using
  Grants](../../../kms/latest/developerguide/grants.md "../../../kms/latest/developerguide/grants.md"), see the AWS Key Management Service Developer Guide.
- [kms:DescribeKey](../../../kms/latest/APIReference/API_DescribeKey.md "../../../kms/latest/APIReference/API_DescribeKey.md") – provides the customer managed key details to allow
  Amazon DataZone to validate the key.
- [kms:GenerateDataKey](../../../kms/latest/APIReference/API_GenerateDataKey.md "../../../kms/latest/APIReference/API_GenerateDataKey.md") – returns a unique symmetric data key for use outside of
  AWS KMS.
- [kms:Decrypt](../../../kms/latest/APIReference/API_Decrypt.md "../../../kms/latest/APIReference/API_Decrypt.md") – decrypts ciphertext that was encrypted by a KMS key.

The following are policy statement examples you can add for Amazon DataZone:

```

"Statement": [
    {
      "Sid": "Enable IAM User Permissions for DescribeKey",
      "Effect": "Allow",
      "Principal": {
        "AWS": "arn:aws:iam::111122223333:root"
      },
      "Action": "kms:DescribeKey",
      "Resource": "arn:aws:kms:`region`:111122223333:key/`key_ID`"
    },
    {
      "Sid": "Allow access to principals authorized to manage Amazon DataZone",
      "Effect": "Allow",
      "Principal": {
        "AWS": "arn:aws:iam::111122223333:root"
      },
      "Action": [
        "kms:Decrypt",
        "kms:GenerateDataKey"
      ],
      "Resource": "arn:aws:kms:`region`:111122223333:key/`key_ID`",
      "Condition": {
        "ForAnyValue:StringEquals": {
          "kms:EncryptionContextKeys": "aws:datazone:domainId"
        }
      }
    },
    {
      "Sid": "Allow creating grants when creating an Amazon DataZone for all principals in the account that are authorized to manage Amazon DataZone",
      "Effect": "Allow",
      "Principal": {
        "AWS": "arn:aws:iam::111122223333:root"
      },
      "Action": "kms:CreateGrant",
      "Resource": "arn:aws:kms:`region`:111122223333:key/`key_ID`",
      "Condition": {
        "StringLike": {
          "kms:CallerAccount": "111122223333",
          "kms:ViaService": "datazone.`region`.amazonaws.com"
        },
        "Bool": {
          "kms:GrantIsForAWSResource": "true"
        },
        "ForAnyValue:StringEquals": {
          "kms:EncryptionContextKeys": "aws:datazone:domainId"
        }
      }
    }
]

```

###### Note

The Amazon DataZone data portal is granted access to your customer managed key via the
Domain Execution Role principal.

For more information about [specifying
permissions in a policy](../../../kms/latest/developerguide/overview.md "../../../kms/latest/developerguide/overview.md"), see the AWS Key Management Service Developer
Guide.

For more information about [troubleshooting key access](../../../kms/latest/developerguide/policy-evaluation.md#example-no-iam "../../../kms/latest/developerguide/policy-evaluation.md#example-no-iam"), see the AWS Key Management Service Developer
Guide.

## Specifying a customer managed key for

Amazon DataZone

You can specify a customer managed key as a second layer encryption during [domain creation](create-domain.md "create-domain.md").

## Amazon DataZone encryption context

An [encryption context](../../../kms/latest/developerguide/concepts.md#encrypt_context "../../../kms/latest/developerguide/concepts.md#encrypt_context") is an optional set of key-value pairs that contain additional
contextual information about the data.

AWS KMS uses the encryption context as [additional authenticated data](../../../crypto/latest/userguide/cryptography-concepts.md#term-aad "../../../crypto/latest/userguide/cryptography-concepts.md#term-aad") to support [authenticated encryption](../../../crypto/latest/userguide/cryptography-concepts.md#define-authenticated-encryption "../../../crypto/latest/userguide/cryptography-concepts.md#define-authenticated-encryption"). When you include an encryption context in a request to
encrypt data, AWS KMS binds the encryption context to the encrypted data. To decrypt data,
you include the same encryption context in the request.

Amazon DataZone uses following encryption context:

```

"encryptionContextSubset": {
    "aws:datazone:domainId": "{`dzd_samleid`}"
}

```

**Using encryption context for monitoring** - when you use
a symmetric customer managed key to encrypt Amazon DataZone, you can also use the encryption
context in audit records and logs to identify how the customer managed key is being used.
The encryption context also appears in logs generated by AWS CloudTrail or Amazon
CloudWatch Logs.

**Using encryption context to control access to your customer
managed key** - you can use the encryption context in key policies and IAM
policies as conditions to control access to your symmetric customer managed key. You can
also use encryption context constraints in a grant.

Amazon DataZone uses an encryption context constraint in grants to control access to the
customer managed key in your account or region. The grant constraint requires that the
operations that the grant allows use the specified encryption context.

The following are example key policy statements to grant access to a customer managed
key for a specific encryption context.

```

 {
      "Sid": "Enable DescribeKey",
      "Effect": "Allow",
      "Principal": {
        "AWS": "arn:aws:iam::111122223333:role/ExampleRole"
      },
      "Action": "kms:DescribeKey",
      "Resource": "arn:aws:kms:`region`:111122223333:key/`key_ID`"
    },
    {
      "Sid": "Allow access to principal to manage an Amazon DataZone domain with the given domain id",
      "Effect": "Allow",
      "Principal": {
        "AWS": "arn:aws:iam::111122223333:role/ExampleRole"
      },
      "Action": [
        "kms:Decrypt",
        "kms:GenerateDataKey"
      ],
      "Resource": "arn:aws:kms:`region`:111122223333:key/`key_ID`",
      "Condition": {
        "StringEquals": {
          "kms:EncryptionContext:aws:datazone:domainId": "`dzd_sampleid`"
        }
      }
    },
    {
      "Sid": "Allow creating grants when creating an Amazon DataZone domain to principal",
      "Effect": "Allow",
      "Principal": {
        "AWS": "arn:aws:iam::111122223333:role/ExampleRole"
      },
      "Action": "kms:CreateGrant",
      "Resource": "arn:aws:kms:`region`:111122223333:key/`key_ID`",
      "Condition": {
        "StringLike": {
          "kms:CallerAccount": "111122223333",
          "kms:ViaService": "datazone.`region`.amazonaws.com"
        },
        "Bool": {
          "kms:GrantIsForAWSResource": "true"
        },
        "ForAnyValue:StringEquals": {
          "kms:EncryptionContextKeys": "aws:datazone:domainId"
        }
      }
    }

```

## Monitoring your encryption keys for

Amazon DataZone

When you use an AWS KMS customer managed key with your Amazon DataZone resources, you can
use [AWS CloudTrail](../../../awscloudtrail/latest/userguide/cloudtrail-user-guide.md "../../../awscloudtrail/latest/userguide/cloudtrail-user-guide.md") to track requests that Amazon DataZone sends to AWS KMS. The
following examples are AWS CloudTrail events for `CreateGrant`,
`GenerateDataKey`, `Decrypt`, and `RetireGrant` to
monitor KMS operations called by Amazon DataZone to access data encrypted by your customer
managed key.

CreateGrant
When you use an AWS KMS customer managed key to encrypt your Amazon DataZone domain,
Amazon DataZone sends a `CreateGrant` request on your behalf to access the KMS
key in your AWS account. Grants that Amazon DataZone creates are specific to the resource
associated with the AWS KMS customer managed key. In addition, Amazon DataZone uses the
`RetireGrant` operation to remove a grant when you delete a
domain.

The following example event records the `CreateGrant` operation:

```

{
    "eventVersion": "1.11",
    "userIdentity": {
        "type": "AssumedRole",
        "principalId": "AROAIGDTESTANDEXAMPLE:Sampleuser01",
        "arn": "arn:aws:sts::111122223333:assumed-role/Example/Sampleuser01",
        "accountId": "111122223333",
        "accessKeyId": "AKIAIOSFODNN7EXAMPLE3",
        "sessionContext": {
            "sessionIssuer": {
                "type": "Role",
                "principalId": "AROAIGDTESTANDEXAMPLE",
                "arn": "arn:aws:iam::111122223333:role/Example",
                "accountId": "111122223333",
                "userName": "Example"
            },
            "attributes": {
                "creationDate": "2024-04-22T17:02:00Z",
                "mfaAuthenticated": "false"
            }
        },
        "invokedBy": "datazone.amazonaws.com"
    },
    "eventTime": "2024-04-22T17:02:00Z",
    "eventSource": "kms.amazonaws.com",
    "eventName": "CreateGrant",
    "awsRegion": "us-east-2",
    "sourceIPAddress": "datazone.amazonaws.com",
    "userAgent": "datazone.amazonaws.com",
    "requestParameters": {
        "retiringPrincipal": "datazone.us-east-2.amazonaws.com",
        "operations": [
            "GenerateDataKey",
            "RetireGrant",
            "DescribeKey",
            "Decrypt"
        ],
        "granteePrincipal": "datazone.us-east-2.amazonaws.com",
        "constraints": {
            "encryptionContextSubset": {
                "aws:datazone:domainId": "dzd_sampleid"
            }
        },
        "keyId": "arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-123456SAMPLE"
    },
    "responseElements": {
        "grantId": "0ab0ac0d0b000f00ea00cc0a0e00fc00bce000c000f0000000c0bc0a0000aaafSAMPLE",
        "keyId": "arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-123456SAMPLE"
    },
    "requestID": "ff000af-00eb-00ce-0e00-ea000fb0fba0SAMPLE",
    "eventID": "ff000af-00eb-00ce-0e00-ea000fb0fba0SAMPLE",
    "readOnly": false,
    "resources": [
        {
            "accountId": "111122223333",
            "type": "AWS::KMS::Key",
            "ARN": "arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-123456SAMPLE"
        }
    ],
    "eventType": "AwsApiCall",
    "managementEvent": true,
    "recipientAccountId": "111122223333",
    "eventCategory": "Management",
    "sessionCredentialFromConsole": "true"
}

```

```

{
    "eventVersion": "1.11",
    "userIdentity": {
        "type": "AssumedRole",
        "principalId": "AROAIGDTESTANDEXAMPLE:Sampleuser01",
        "arn": "arn:aws:sts::111122223333:assumed-role/Example/Sampleuser01",
        "accountId": "111122223333",
        "accessKeyId": "AKIAIOSFODNN7EXAMPLE3",
        "sessionContext": {
            "sessionIssuer": {
                "type": "Role",
                "principalId": "AROAIGDTESTANDEXAMPLE",
                "arn": "arn:aws:iam::111122223333:role/Example",
                "accountId": "111122223333",
                "userName": "Example"
            },
            "attributes": {
                "creationDate": "2024-04-22T17:10:00Z",
                "mfaAuthenticated": "false"
            }
        },
        "invokedBy": "datazone.amazonaws.com"
    },
    "eventTime": "2024-04-22T17:49:00Z",
    "eventSource": "kms.amazonaws.com",
    "eventName": "CreateGrant",
    "awsRegion": "us-east-2",
    "sourceIPAddress": "datazone.amazonaws.com",
    "userAgent": "datazone.amazonaws.com",
    "requestParameters": {
        "retiringPrincipal": "datazone.us-east-2.amazonaws.com",
        "operations": [
            "DescribeKey",
            "Decrypt"
        ],
        "granteePrincipal": "datazone.us-east-2.amazonaws.com",
        "constraints": {
            "encryptionContextSubset": {
                "aws:datazone:domainId": "dzd_sampleid"
            }
        },
        "keyId": "arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-123456SAMPLE"
    },
    "responseElements": {
        "grantId": "0ab0ac0d0b000f00ea00cc0a0e00fc00bce000c000f0000000c0bc0a0000aaafSAMPLE",
        "keyId": "arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-123456SAMPLE"
    },
    "requestID": "ff000af-00eb-00ce-0e00-ea000fb0fba0SAMPLE",
    "eventID": "ff000af-00eb-00ce-0e00-ea000fb0fba0SAMPLE",
    "readOnly": false,
    "resources": [
        {
            "accountId": "111122223333",
            "type": "AWS::KMS::Key",
            "ARN": "arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-123456SAMPLE"
        }
    ],
    "eventType": "AwsApiCall",
    "managementEvent": true,
    "recipientAccountId": "111122223333",
    "eventCategory": "Management",
    "sessionCredentialFromConsole": "true"
}

```

GenerateDataKey
When you enable an AWS KMS customer managed key for your Amazon DataZone domain,
Amazon DataZone generates data keys. It sends a `GenerateDataKey` request to
AWS KMS that specifies the AWS KMS customer managed key for the domain.

The following example event records the GenerateDataKey operation:

```

{
    "eventVersion": "1.11",
    "userIdentity": {
        "type": "AssumedRole",
        "principalId": "AROAIGDTESTANDEXAMPLE:AmazonSageMakerDomainExecution",
        "arn": "arn:aws:sts::111122223333:assumed-role/AmazonSageMakerDomainExecution/AmazonSageMakerDomainExecution",
        "accountId": "111122223333",
        "accessKeyId": "AKIAIOSFODNN7EXAMPLE3",
        "sessionContext": {
            "sessionIssuer": {
                "type": "Role",
                "principalId": "AROAIGDTESTANDEXAMPLE",
                "arn": "arn:aws:iam::111122223333:role/service-role/AmazonSageMakerDomainExecution",
                "accountId": "111122223333",
                "userName": "AmazonSageMakerDomainExecution"
            },
            "attributes": {
                "creationDate": "2024-04-22T19:50:39Z",
                "mfaAuthenticated": "false"
            }
        },
        "invokedBy": "datazone.amazonaws.com"
    },
    "eventTime": "2024-04-22T19:50:40Z",
    "eventSource": "kms.amazonaws.com",
    "eventName": "GenerateDataKey",
    "awsRegion": "us-east-2",
    "sourceIPAddress": "datazone.amazonaws.com",
    "userAgent": "datazone.amazonaws.com",
    "requestParameters": {
        "keySpec": "AES_256",
        "encryptionContext": {
            "aws:datazone:domainId": "dzd_sampleid",
            "V": "2024-04-22T17:49:12.98177136Z|cacf3df7-7b99-49f6-ae14-sample",
            "version": "0",
            "N": "dzd_sampleid|arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-123456SAMPLE",
            "*aws-kms-table*": "awsdatazoneroaring-data-store-datakeys-prod-us-east-2"
        },
        "keyId": "arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-123456SAMPLE"
    },
    "responseElements": null,
    "requestID": "ff000af-00eb-00ce-0e00-ea000fb0fba0SAMPLE",
    "eventID": "ff000af-00eb-00ce-0e00-ea000fb0fba0SAMPLE",
    "readOnly": true,
    "resources": [
        {
            "accountId": "111122223333",
            "type": "AWS::KMS::Key",
            "ARN": "arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-123456SAMPLE"
        }
    ],
    "eventType": "AwsApiCall",
    "managementEvent": true,
    "recipientAccountId": "111122223333",
    "eventCategory": "Management"
}

```

```

{
    "eventVersion": "1.11",
    "userIdentity": {
        "type": "AWSService",
        "invokedBy": "AWS Internal"
    },
    "eventTime": "2024-04-22T19:50:40Z",
    "eventSource": "kms.amazonaws.com",
    "eventName": "GenerateDataKey",
    "awsRegion": "us-east-2",
    "sourceIPAddress": "AWS Internal",
    "userAgent": "AWS Internal",
    "requestParameters": {
        "encryptionContext": {
            "aws:datazone:domainId": "dzd_sampleid",
            "aws:s3:arn": "arn:aws:s3:::amazon-datazone-us-east-2-422ceee9465430bdb354d1c9efsample"
        },
        "keyId": "arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-123456SAMPLE",
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
            "ARN": "arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-123456SAMPLE"
        }
    ],
    "eventType": "AwsApiCall",
    "managementEvent": true,
    "recipientAccountId": "111122223333",
    "sharedEventID": "ff000af-00eb-00ce-0e00-ea000fb0fba0SAMPLE",
    "eventCategory": "Management"
}

```

Decrypt
When you access an encrypted Amazon DataZone domain, Amazon DataZone calls the
`Decrypt` operation to use the stored encrypted data key to access the
encrypted data.

The following example event records the `Decrypt` operation:

```

{
    "eventVersion": "1.11",
    "userIdentity": {
        "type": "AssumedRole",
        "principalId": "AROAIGDTESTANDEXAMPLE:AmazonSageMakerDomainExecution",
        "arn": "arn:aws:sts::111122223333:assumed-role/AmazonSageMakerDomainExecution/AmazonSageMakerDomainExecution",
        "accountId": "111122223333",
        "accessKeyId": "AKIAIOSFODNN7EXAMPLE3",
        "sessionContext": {
            "sessionIssuer": {
                "type": "Role",
                "principalId": "AROAIGDTESTANDEXAMPLE",
                "arn": "arn:aws:iam::111122223333:role/service-role/AmazonSageMakerDomainExecution",
                "accountId": "111122223333",
                "userName": "AmazonSageMakerDomainExecution"
            },
            "attributes": {
                "creationDate": "2024-04-22T19:50:39Z",
                "mfaAuthenticated": "false"
            }
        },
        "invokedBy": "datazone.amazonaws.com"
    },
    "eventTime": "2024-04-22T19:51:54Z",
    "eventSource": "kms.amazonaws.com",
    "eventName": "Decrypt",
    "awsRegion": "us-east-2",
    "sourceIPAddress": "datazone.amazonaws.com",
    "userAgent": "datazone.amazonaws.com",
    "requestParameters": {
        "encryptionAlgorithm": "SYMMETRIC_DEFAULT",
        "encryptionContext": {
            "aws:datazone:domainId": "dzd_sampleid",
            "V": "2024-04-22T17:49:12.98177136Z|cacf3df7-7b99-49f6-ae14-sample",
            "version": "0",
            "N": "dzd_sampleid|arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-123456SAMPLE",
            "*aws-kms-table*": "awsdatazoneroaring-data-store-datakeys-prod-us-east-2"
        }
    },
    "responseElements": null,
    "requestID": "ff000af-00eb-00ce-0e00-ea000fb0fba0SAMPLE",
    "eventID": "ff000af-00eb-00ce-0e00-ea000fb0fba0SAMPLE",
    "readOnly": true,
    "resources": [
        {
            "accountId": "111122223333",
            "type": "AWS::KMS::Key",
            "ARN": "arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-123456SAMPLE"
        }
    ],
    "eventType": "AwsApiCall",
    "managementEvent": true,
    "recipientAccountId": "111122223333",
    "eventCategory": "Management"
}

```

```

{
    "eventVersion": "1.11",
    "userIdentity": {
        "type": "AWSService",
        "invokedBy": "datazone.amazonaws.com"
    },
    "eventTime": "2024-04-22T19:51:54Z",
    "eventSource": "kms.amazonaws.com",
    "eventName": "Decrypt",
    "awsRegion": "us-east-2",
    "sourceIPAddress": "datazone.amazonaws.com",
    "userAgent": "datazone.amazonaws.com",
    "requestParameters": {
        "encryptionContext": {
            "aws:datazone:domainId": "dzd_sampleid",
            "V": "2024-04-22T17:49:12.98177136Z|cacf3df7-7b99-49f6-ae14-sample",
            "version": "0",
            "N": "dzd_sampleid|arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-123456SAMPLE",
            "*aws-kms-table*": "awsdatazoneroaring-data-store-datakeys-prod-us-east-2"
        },
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
            "ARN": "arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-123456SAMPLE"
        }
    ],
    "eventType": "AwsApiCall",
    "managementEvent": true,
    "recipientAccountId": "111122223333",
    "sharedEventID": "ff000af-00eb-00ce-0e00-ea000fb0fba0SAMPLE",
    "eventCategory": "Management"
}

```

```

{
    "eventVersion": "1.11",
    "userIdentity": {
        "type": "AWSService",
        "invokedBy": "AWS Internal"
    },
    "eventTime": "2024-04-22T19:51:54Z",
    "eventSource": "kms.amazonaws.com",
    "eventName": "Decrypt",
    "awsRegion": "us-east-2",
    "sourceIPAddress": "AWS Internal",
    "userAgent": "AWS Internal",
    "requestParameters": {
        "encryptionAlgorithm": "SYMMETRIC_DEFAULT",
        "encryptionContext": {
            "aws:datazone:domainId": "dzd_sampleid",
            "aws:s3:arn": "arn:aws:s3:::amazon-datazone-us-east-2-422ceee9465430bdb354d1c9efsample"
        }
    },
    "responseElements": null,
    "requestID": "ff000af-00eb-00ce-0e00-ea000fb0fba0SAMPLE",
    "eventID": "ff000af-00eb-00ce-0e00-ea000fb0fba0SAMPLE",
    "readOnly": true,
    "resources": [
        {
            "accountId": "111122223333",
            "type": "AWS::KMS::Key",
            "ARN": "arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-123456SAMPLE"
        }
    ],
    "eventType": "AwsApiCall",
    "managementEvent": true,
    "recipientAccountId": "111122223333",
    "sharedEventID": "ff000af-00eb-00ce-0e00-ea000fb0fba0SAMPLE",
    "eventCategory": "Management"
}

```

RetireGrant
The following example event records the `RetireGrant` operation:

```

{
    "eventVersion": "1.11",
    "userIdentity": {
        "type": "AWSService",
        "invokedBy": "datazone.amazonaws.com"
    },
    "eventTime": "2025-04-29T22:18:50Z",
    "eventSource": "kms.amazonaws.com",
    "eventName": "RetireGrant",
    "awsRegion": "us-east-2",
    "sourceIPAddress": "datazone.amazonaws.com",
    "userAgent": "datazone.amazonaws.com",
    "requestParameters": null,
    "responseElements": {
        "keyId": "arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-123456SAMPLE"
    },
    "additionalEventData": {
        "grantId": "0ab0ac0d0b000f00ea00cc0a0e00fc00bce000c000f0000000c0bc0a0000aaafSAMPLE"
    },
    "requestID": "294308c0-7617-4727-b5c9-34eaf75aa8e3",
    "eventID": "273708f7-5fbb-3a90-b04d-2b3138bf0ec9",
    "readOnly": false,
    "resources": [
        {
            "accountId": "111122223333",
            "type": "AWS::KMS::Key",
            "ARN": "arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-123456SAMPLE"
        }
    ],
    "eventType": "AwsApiCall",
    "managementEvent": true,
    "recipientAccountId": "111122223333",
    "sharedEventID": "b46377d7-b3c3-4bfd-a257-722bd3f3411d",
    "eventCategory": "Management"
}

```

## Creating Data Lake environments that involve

encrypted AWS Glue catalogs

In advanced use cases, when you are working with an AWS Glue catalog that is
encrypted, you must grant access to the Amazon DataZone service to use your customer-managed KMS
key. You can do this by updating your custom KMS policy and adding a tag to the key. To
grant access to the Amazon DataZone service to work with data in an encrypted AWS Glue catalog,
complete the following:

- Add the following policy to your custom KMS key. For more information, see [Changing a key policy](../../../kms/latest/developerguide/key-policy-modifying.md "../../../kms/latest/developerguide/key-policy-modifying.md").

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "Allow datazone environment roles to decrypt using the key",
 "Effect": "Allow",
 "Principal": {
 "AWS": "*"
 },
 "Action": [
 "kms:Decrypt"
 ],
 "Resource": "*",
 "Condition": {
 "StringEquals": {
 "kms:EncryptionContext:glue_catalog_id": "<GLUE_CATALOG_ID>"
 },
 "ArnLike": {
 "aws:PrincipalArn": [
 "arn:aws:iam::111122223333:role/*datazone_usr*",
 "arn:aws:iam::444455556666:role/*datazone_usr*"
 ]
 }
 }
 },
 {
 "Sid": "Allow datazone environment roles to describe the key",
 "Effect": "Allow",
 "Principal": {
 "AWS": "*"
 },
 "Action": [
 "kms:DescribeKey"
 ],
 "Resource": "*",
 "Condition": {
 "ArnLike": {
 "aws:PrincipalArn": [
 "arn:aws:iam::111122223333:role/*datazone_usr*",
 "arn:aws:iam::444455556666:role/*datazone_usr*"
 ]
 }
 }
 }
 ]
}`

```

###### Important

    + You must modify the `"aws:PrincipalArn"` ARNs in the policy using
     the account IDs in which you want to create the environments. Each account in
     which you want to create an environment, must be listed in the policy as the
     `"aws:PrincipalArn"`.
    + You must also replace <GLUE\_CATALOG\_ID> with the valid AWS account ID
     in which your AWS Glue catalog is located.
    + Note that this policy grants access to use the key to all Amazon DataZone
     environment user roles in the specified account(s). If you want to only allow
     specific environment user roles to use the key, you must specify the entire
     environment user role name (for example,
     `arn:aws:iam::<ENVIRONMENT_ACCOUNT_ID>:role/datazone_usr_<ENVIRONMENT_ID>`
     (where <ENVIRONMENT\_ID> is the ID of the environment) rather than the
     wildcard format.

- Add the following tag to your custom KMS key. For more information, see [Using tags to control access to KMS keys](../../../kms/latest/developerguide/tag-authorization.md "../../../kms/latest/developerguide/tag-authorization.md").

```

key: AmazonDataZoneEnvironment
value: all

```
