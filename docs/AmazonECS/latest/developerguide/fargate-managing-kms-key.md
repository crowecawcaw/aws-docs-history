# Managing AWS KMS keys for Fargate ephemeral storage for Amazon ECS

After creating or importing your AWS KMS key to encrypt your Fargate ephemeral storage, you manage it the
same way you would any other AWS KMS key.

###### Automatic rotation of AWS KMS keys

You can enable automatic key rotation or rotate them manually. Automatic key rotation rotates the key
for you yearly by generating new cryptographic material for the key. AWS KMS also saves all previous
versions of the cryptographic material, so you'll be able to decrypt any data that used the earlier key
versions. Any rotated material won't be deleted by AWS KMS until you delete the key.

Automatic key rotation is optional and can be enabled or disabled at any time.

###### Disabling or revoking AWS KMS keys

If you disable a customer managed key in AWS KMS, it doesn't have any impact on running tasks, and they
continue to function through their lifecycle. If a new task uses the disabled or revoked key, the task
fails since it can't access the key. You should set a CloudWatch alarm or similar to make sure a disabled key
is never needed to decrypt already encrypted data.

###### Deleting AWS KMS keys

Deleting keys should always be a last resort and should only be done if you're certain the deleted
key is never needed again. New tasks that try to use the deleted key will fail because they can't
access it. AWS KMS advises disabling a key instead of deleting it. If you feel it's necessary to delete a
key, we suggest disabling it first and setting a CloudWatch alarm to make sure it isn't needed. If you do
delete a key, AWS KMS supplies at least seven days to change your mind.

###### Auditing AWS KMS key access

You can use CloudTrail logs to audit access to your AWS KMS key. You're able to check the AWS KMS operations
`CreateGrant`, `GenerateDataKeyWithoutPlaintext`, and `Decrypt`.
These operations also show the `aws:ecs:clusterAccount` and `aws:ecs:clusterName`
as part of the `EncryptionContext` logged in CloudTrail.

The following are example CloudTrail events for `GenerateDataKeyWithoutPlaintext`,
`GenerateDataKeyWithoutPlaintext (DryRun)`, `CreateGrant`, `CreateGrant
 (DryRun)`, and `RetireGrant` (replace the `red` values with
your own).

GenerateDataKeyWithoutPlaintext

```
{
    "eventVersion": "1.08",
    "userIdentity": {
        "type": "AWSService",
        "invokedBy": "ec2-frontend-api.amazonaws.com"
    },
    "eventTime": "2024-04-23T18:08:13Z",
    "eventSource": "kms.amazonaws.com",
    "eventName": "GenerateDataKeyWithoutPlaintext",
    "awsRegion": "`us-west-2`",
    "sourceIPAddress": "ec2-frontend-api.amazonaws.com",
    "userAgent": "ec2-frontend-api.amazonaws.com",
    "requestParameters": {
        "numberOfBytes": 64,
        "keyId": "arn:aws:kms:`us-west-2`:`account-id`:key/`a1b2c3d4-5678-90ab-cdef-EXAMPLE11111`",
        "encryptionContext": {
            "aws:ecs:clusterAccount": "`account-id`",
            "aws:ebs:id": "`vol-xxxxxxx`",
            "aws:ecs:clusterName": "`cluster-name`"
        }
    },
    "responseElements": null,
    "requestID": "`a1b2c3d4-5678-90ab-cdef-EXAMPLE22222`",
    "eventID": "`a1b2c3d4-5678-90ab-cdef-EXAMPLE33333`",
    "readOnly": true,
    "resources": [
        {
            "accountId": "AWS Internal",
            "type": "AWS::KMS::Key",
            "ARN": "arn:aws:kms:`us-west-2`:`account-id`:key/`a1b2c3d4-5678-90ab-cdef-EXAMPLE11111`"
        }
    ],
    "eventType": "AwsApiCall",
    "managementEvent": true,
    "recipientAccountId": "`account-id`",
    "sharedEventID": "`a1b2c3d4-5678-90ab-cdef-EXAMPLEaaaaa`",
    "eventCategory": "Management"
}
```

GenerateDataKeyWithoutPlaintext (DryRun)

```
{
    "eventVersion": "1.08",
    "userIdentity": {
        "type": "AWSService",
        "invokedBy": "fargate.amazonaws.com"
    },
    "eventTime": "2024-04-23T18:08:11Z",
    "eventSource": "kms.amazonaws.com",
    "eventName": "GenerateDataKeyWithoutPlaintext",
    "awsRegion": "`us-west-2`",
    "sourceIPAddress": "fargate.amazonaws.com",
    "userAgent": "fargate.amazonaws.com",
    "errorCode": "DryRunOperationException",
    "errorMessage": "The request would have succeeded, but the DryRun option is set.",
    "requestParameters": {
        "keyId": "arn:aws:kms:`us-west-2`:`account-id`:key/`a1b2c3d4-5678-90ab-cdef-EXAMPLE11111`",
        "dryRun": true,
        "numberOfBytes": 64,
        "encryptionContext": {
            "aws:ecs:clusterAccount": "`account-id`",
            "aws:ecs:clusterName": "`cluster-name`"
        }
    },
    "responseElements": null,
    "requestID": "`a1b2c3d4-5678-90ab-cdef-EXAMPLE22222`",
    "eventID": "`a1b2c3d4-5678-90ab-cdef-EXAMPLE33333`",
    "readOnly": true,
    "resources": [
        {
            "accountId": "AWS Internal",
            "type": "AWS::KMS::Key",
            "ARN": "arn:aws:kms:`us-west-2`:`account-id`:key/`a1b2c3d4-5678-90ab-cdef-EXAMPLE11111`"
        }
    ],
    "eventType": "AwsApiCall",
    "managementEvent": true,
    "recipientAccountId": "`account-id`",
    "sharedEventID": "`a1b2c3d4-5678-90ab-cdef-EXAMPLEaaaaa`",
    "eventCategory": "Management"
}
```

CreateGrant

```
{
    "eventVersion": "1.08",
    "userIdentity": {
        "type": "AWSService",
        "invokedBy": "ec2-frontend-api.amazonaws.com"
    },
    "eventTime": "2024-04-23T18:08:13Z",
    "eventSource": "kms.amazonaws.com",
    "eventName": "CreateGrant",
    "awsRegion": "`us-west-2`",
    "sourceIPAddress": "ec2-frontend-api.amazonaws.com",
    "userAgent": "ec2-frontend-api.amazonaws.com",
    "requestParameters": {
        "keyId": "arn:aws:kms:`us-west-2`:`account-id`:key/`a1b2c3d4-5678-90ab-cdef-EXAMPLE11111`",
        "granteePrincipal": "fargate.`us-west-2`.amazonaws.com",
        "operations": [
            "Decrypt"
        ],
        "constraints": {
            "encryptionContextSubset": {
                "aws:ecs:clusterAccount": "`account-id`",
                "aws:ebs:id": "vol-xxxx",
                "aws:ecs:clusterName": "`cluster-name`"
            }
        },
        "retiringPrincipal": "ec2.`us-west-2`.amazonaws.com"
    },
    "responseElements": {
        "grantId": "`e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`",
        "keyId": "arn:aws:kms:`us-west-2`:`account-id`:key/`a1b2c3d4-5678-90ab-cdef-EXAMPLE11111`"
    },
    "requestID": "`a1b2c3d4-5678-90ab-cdef-EXAMPLE22222`",
    "eventID": "`a1b2c3d4-5678-90ab-cdef-EXAMPLE33333`",
    "readOnly": false,
    "resources": [
        {
            "accountId": "AWS Internal",
            "type": "AWS::KMS::Key",
            "ARN": "arn:aws:kms:`us-west-2`:`account-id`:key/`a1b2c3d4-5678-90ab-cdef-EXAMPLE11111`"
        }
    ],
    "eventType": "AwsApiCall",
    "managementEvent": true,
    "recipientAccountId": "`account-id`",
    "sharedEventID": "`a1b2c3d4-5678-90ab-cdef-EXAMPLEaaaaa`",
    "eventCategory": "Management"
}
```

CreateGrant (DryRun)

```
{
    "eventVersion": "1.08",
    "userIdentity": {
        "type": "AWSService",
        "invokedBy": "fargate.amazonaws.com"
    },
    "eventTime": "2024-04-23T18:08:11Z",
    "eventSource": "kms.amazonaws.com",
    "eventName": "CreateGrant",
    "awsRegion": "`us-west-2`",
    "sourceIPAddress": "fargate.amazonaws.com",
    "userAgent": "fargate.amazonaws.com",
    "errorCode": "DryRunOperationException",
    "errorMessage": "The request would have succeeded, but the DryRun option is set.",
    "requestParameters": {
        "keyId": "arn:aws:kms:`us-west-2`:`account-id`:key/`a1b2c3d4-5678-90ab-cdef-EXAMPLE11111`",
        "granteePrincipal": "fargate.`us-west-2`.amazonaws.com",
        "dryRun": true,
        "operations": [
            "Decrypt"
        ],
        "constraints": {
            "encryptionContextSubset": {
                "aws:ecs:clusterAccount": "`account-id`",
                "aws:ecs:clusterName": "`cluster-name`"
            }
        }
    },
    "responseElements": null,
    "requestID": "`a1b2c3d4-5678-90ab-cdef-EXAMPLE22222`",
    "eventID": "`a1b2c3d4-5678-90ab-cdef-EXAMPLE33333`",
    "readOnly": false,
    "resources": [
        {
            "accountId": "AWS Internal",
            "type": "AWS::KMS::Key",
            "ARN": "arn:aws:kms:`us-west-2`:`account-id`:key/`a1b2c3d4-5678-90ab-cdef-EXAMPLE11111`"
        }
    ],
    "eventType": "AwsApiCall",
    "managementEvent": true,
    "recipientAccountId": "`account-id`",
    "sharedEventID": "`a1b2c3d4-5678-90ab-cdef-EXAMPLEaaaaa`",
    "eventCategory": "Management"
}
```

RetireGrant

```
{
    "eventVersion": "1.08",
    "userIdentity": {
        "type": "AWSService",
        "invokedBy": "AWS Internal"
    },
    "eventTime": "2024-04-20T18:37:38Z",
    "eventSource": "kms.amazonaws.com",
    "eventName": "RetireGrant",
    "awsRegion": "`us-west-2`",
    "sourceIPAddress": "AWS Internal",
    "userAgent": "AWS Internal",
    "requestParameters": null,
    "responseElements": {
        "keyId": "arn:aws:kms:`us-west-2`:`account-id`:key/`a1b2c3d4-5678-90ab-cdef-EXAMPLE11111`"
    },
    "additionalEventData": {
        "grantId": "`e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`"
    },
    "requestID": "`a1b2c3d4-5678-90ab-cdef-EXAMPLE22222`",
    "eventID": "`a1b2c3d4-5678-90ab-cdef-EXAMPLE33333`",
    "readOnly": false,
    "resources": [
        {
            "accountId": "AWS Internal",
            "type": "AWS::KMS::Key",
            "ARN": "arn:aws:kms:`us-west-2`:`account-id`:key/`a1b2c3d4-5678-90ab-cdef-EXAMPLE11111`"
        }
    ],
    "eventType": "AwsApiCall",
    "managementEvent": true,
    "recipientAccountId": "`account-id`",
    "sharedEventID": "`a1b2c3d4-5678-90ab-cdef-EXAMPLEaaaaa`",
    "eventCategory": "Management"
}
```
