# Key management for Amazon S3 data access

This page is specific to the Amazon S3 data access type where the provider is sharing objects
encrypted using SSE-KMS. The subscriber must have a grant on the keys used for
access.

If your Amazon S3 bucket contains data encrypted using AWS KMS customer managed keys, you must share these
AWS KMS keys with AWS Data Exchange to configure your Amazon S3 data access data set. For more
information, see [Step 2: Configure Amazon S3 data
access](publish-s3-data-access-product.md#configure-s3-data-access-product "publish-s3-data-access-product.md#configure-s3-data-access-product").

###### Topics

- [Creating AWS KMS grants](#create-kms-grants "#create-kms-grants")
- [Encryption context and grant
  constraints](#encryption-context-grant-constraint "#encryption-context-grant-constraint")
- [Monitoring your AWS KMS keys in
  AWS Data Exchange](#monitoring-your-kms-keys "#monitoring-your-kms-keys")

## Creating AWS KMS grants

When you provide AWS KMS keys as part of your Amazon S3 data access data set, AWS Data Exchange
creates an AWS KMS grant on each AWS KMS key shared. This grant, known as the _parent grant_, is used to give AWS Data Exchange permission to create
additional AWS KMS grants for subscribers. These additional grants are known as _child grants_. Each subscriber is permitted one AWS KMS grant.
Subscribers get permission to decrypt the AWS KMS key. Then, they can decrypt and use
the encrypted Amazon S3 objects shared with them. For more information, see [Grants in
AWS KMS](../../../kms/latest/developerguide/grants.md "../../../kms/latest/developerguide/grants.md") in the _AWS Key Management Service Developer
Guide_.

AWS Data Exchange also uses the AWS KMS parent grant to manage the lifecycle of the AWS KMS grant that
it creates. When a subscription ends, AWS Data Exchange retires the AWS KMS child grant created for
the corresponding subscriber. If the revision is revoked, or the data set is deleted,
AWS Data Exchange retires the AWS KMS parent grant. For more information about AWS KMS actions, see the
[AWS KMS
API reference](../../../kms/latest/APIReference/API_Operations.md "../../../kms/latest/APIReference/API_Operations.md").

## Encryption context and grant

constraints

AWS Data Exchange uses grant constraints to permit the decrypt operation only when the request
includes the specified encryption context. You can use the Amazon S3 Bucket Key feature to
encrypt your Amazon S3 objects and share it with AWS Data Exchange. The bucket Amazon Resource Name (ARN)
is implicitly used by Amazon S3 as the encryption context. The following example shows that
AWS Data Exchange uses the bucket ARN as the grant constraint for all AWS KMS grants that it
creates.

```
"Constraints": {
   "EncryptionContextSubset":  "aws:s3:arn": “arn:aws:s3:::<Bucket ARN>"
   }
}

```

## Monitoring your AWS KMS keys in

AWS Data Exchange

When you share AWS KMS customer managed keys with AWS Data Exchange, you can use [AWS CloudTrail](../../../awscloudtrail/latest/userguide/cloudtrail-user-guide.md "../../../awscloudtrail/latest/userguide/cloudtrail-user-guide.md") to
track requests that AWS Data Exchange or data subscribers send to AWS KMS. The following are examples
of what your CloudTrail logs will look like for the `CreateGrant` and
`Decrypt` calls to AWS KMS.

CreateGrant for parent
`CreateGrant` is for parent grants created by AWS Data Exchange for
itself.

```
{
    "eventVersion": "1.08",
    "userIdentity": {
        "type": "AssumedRole",
        "principalId": "AROAIGDTESTANDEXAMPLE:Provider01",
        "arn": "arn:aws:sts::<your-account-id>:assumed-role/Admin/Provider01",
        "accountId": "<your-account-id>",
        "accessKeyId": "AKIAIOSFODNN7EXAMPLE",
        "sessionContext": {
            "sessionIssuer": {
                "type": "Role",
                "principalId": "AROAIGDTESTANDEXAMPLE",
                "arn": "arn:aws:iam::<your-account-id>:role/Admin/Provider01”,
                "accountId": "<your-account-id>",
                "userName": "Admin"
            },
            "webIdFederationData": {},
            "attributes": {
                "creationDate": "2023-02-16T17:29:23Z",
                "mfaAuthenticated": "false"
            }
        },
        "invokedBy": "datax.amazonaws.com"
    },
    "eventTime": "2023-02-16T17:32:47Z",
    "eventSource": "kms.amazonaws.com",
    "eventName": "CreateGrant",
    "awsRegion": "us-east-2",
    "sourceIPAddress": "datax.amazonaws.com",
    "userAgent": "datax.amazonaws.com",
    "requestParameters": {
        "keyId": "<Key ARN of the Key you shared with AWS Data Exchange>",
        "operations": [
            "CreateGrant",
            "Decrypt",
            "RetireGrant"
        ],
        "granteePrincipal": "dataexchange.us-east-2.amazonaws.com",
        "retiringPrincipal": "dataexchange.us-east-2.amazonaws.com",
        "constraints": {
            "encryptionContextSubset": {
                AWS:s3:arn": "arn:aws:s3:::<Your Bucket ARN>"
            }
        }
    },
    "responseElements": {
        "grantId": "<KMS Grant ID of the created Grant>",
        "keyId": "<Key ARN of the Key you shared with AWS Data Exchange>"
    },
    "requestID": "ff000af-00eb-00ce-0e00-ea000fb0fba0SAMPLE",
    "eventID": "ff000af-00eb-00ce-0e00-ea000fb0fba0SAMPLE",
    "readOnly": false,
    "resources": [
        {
            "accountId": "<Your Account Id>",
            "type": "AWS::KMS::Key",
            "ARN": "<Key ARN of the Key you shared with AWS Data Exchange>"
        }
    ],
    "eventType": "AwsApiCall",
    "managementEvent": true,
    "recipientAccountId": "<Your Account Id>",
    "eventCategory": "Management"
}

```

CreateGrant for child
`CreateGrant` is for child grants created by AWS Data Exchange for
subscribers.

```
{
      "eventVersion": "1.08",
      "userIdentity": {
         "type": "AWSService",
         "invokedBy": "datax.amazonaws.com"
     },
     "eventTime": "2023-02-15T23:15:49Z",
     "eventSource": "kms.amazonaws.com",
     "eventName": "CreateGrant",
     "awsRegion": "us-east-2",
     "sourceIPAddress": "datax.amazonaws.com",
     "userAgent": "datax.amazonaws.com",
     "requestParameters": {
         "keyId": "<Key ARN of the Key you shared with AWS Data Exchange>",
         "operations": [
             "Decrypt"
         ],
         "granteePrincipal": “<Subscriber’s account Id>”,
         "retiringPrincipal": "dataexchange.us-east-2.amazonaws.com",
         "constraints": {
             "encryptionContextSubset": {
                 "aws:s3:arn": "arn:aws:s3:::<Your Bucket ARN>"
             }
         }
     },
     "responseElements": {
         "grantId": "<KMS Grant ID of the created Grant>",
         "keyId": "<Key ARN of the Key you shared with AWS Data Exchange>"
     },
     "requestID": "ff000af-00eb-00ce-0e00-ea000fb0fba0SAMPLE",
     "eventID": "ff000af-00eb-00ce-0e00-ea000fb0fba0SAMPLE",
     "readOnly": false,
     "resources": [
         {
             "accountId": "<Your Account Id>",
             "type": "AWS::KMS::Key",
             "ARN": "<Key ARN of the Key you shared with AWS Data Exchange>"
         }
     ],
     "eventType": "AwsApiCall",
     "managementEvent": true,
     "recipientAccountId": "<Your Account Id>",
     "sharedEventID": "ff000af-00eb-00ce-0e00-ea000fb0fba0SAMPLE ",
     "eventCategory": "Management"
}

```

Decrypt
`Decrypt` is called by subscribers when they attempt to read
the encrypted data in which they're subscribed.

```
{
    "eventVersion": "1.08",
    "userIdentity": {
        "type": "AWSAccount",
        "principalId": "AROAIGDTESTANDEXAMPLE:Subscriber01",
        "accountId": "<subscriber-account-id>",
        "invokedBy": "<subscriber’s IAM identity>"
    },
    "eventTime": "2023-02-15T23:28:30Z",
    "eventSource": "kms.amazonaws.com",
    "eventName": "Decrypt",
    "awsRegion": "us-east-2",
    "sourceIPAddress": "<subscriber’s IP address>",
    "userAgent": "<subscriber’s user agent>",
    "requestParameters": {
        "encryptionContext": {
            "aws:s3:arn": "arn:aws:s3:::<Your Bucket ARN>"
        },
        "encryptionAlgorithm": "SYMMETRIC_DEFAULT"
    },
    "responseElements": null,
    "requestID": ""ff000af-00eb-00ce-0e00-ea000fb0fba0SAMPLE",
    "eventID": ""ff000af-00eb-00ce-0e00-ea000fb0fba0SAMPLE”,
    "readOnly": true,
    "resources": [
        {
            "accountId": "<Your Account Id>",
            "type": "AWS::KMS::Key",
            "ARN": "<Key ARN of the Key you shared with AWS Data Exchange>"
        }
    ],
    "eventType": "AwsApiCall",
    "managementEvent": true,
    "recipientAccountId": "602466227860",
    "sharedEventID": "bcf4d02a-31ea-4497-9c98-4c3549f20a7b",
    "eventCategory": "Management"
}

```
