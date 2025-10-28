# Monitoring your encryption keys for the Amazon Bedrock service

When you use an AWS KMS customer managed key with your Amazon Bedrock resources, you can use [AWS CloudTrail](../../../awscloudtrail/latest/userguide/cloudtrail-user-guide.md "../../../awscloudtrail/latest/userguide/cloudtrail-user-guide.md") or
[Amazon CloudWatch Logs](../../../AmazonCloudWatch/latest/logs/WhatIsCloudWatchLogs.md "../../../AmazonCloudWatch/latest/logs/WhatIsCloudWatchLogs.md") to track requests that Amazon Bedrock sends to AWS KMS.

The following is an example AWS CloudTrail event for [CreateGrant](../../../kms/latest/APIReference/API_CreateGrant.md "../../../kms/latest/APIReference/API_CreateGrant.md") to monitor AWS KMS operations called by Amazon Bedrock to create a primary grant:

```
{
"eventVersion": "1.09",
    "userIdentity": {
"type": "AssumedRole",
        "principalId": "AROAIGDTESTANDEXAMPLE:SampleUser01",
        "arn": "arn:aws:sts::111122223333:assumed-role/RoleForModelImport/SampleUser01",
        "accountId": "111122223333",
        "accessKeyId": "EXAMPLE",
        "sessionContext": {
"sessionIssuer": {
"type": "Role",
                "principalId": "AROAIGDTESTANDEXAMPLE",
                "arn": "arn:aws:iam::111122223333:role/RoleForModelImport",
                "accountId": "111122223333",
                "userName": "RoleForModelImport"
            },
            "attributes": {
"creationDate": "2024-05-07T21:46:28Z",
                "mfaAuthenticated": "false"
            }
        },
        "invokedBy": "bedrock.amazonaws.com"
    },
    "eventTime": "2024-05-07T21:49:44Z",
    "eventSource": "kms.amazonaws.com",
    "eventName": "CreateGrant",
    "awsRegion": "us-east-1",
    "sourceIPAddress": "bedrock.amazonaws.com",
    "userAgent": "bedrock.amazonaws.com",
    "requestParameters": {
"granteePrincipal": "bedrock.amazonaws.com",
        "retiringPrincipal": "bedrock.amazonaws.com",
        "keyId": "arn:aws:kms:us-east-1:111122223333:key/1234abcd-12ab-34cd-56ef-123456SAMPLE",
        "operations": [
            "Decrypt",
            "CreateGrant",
            "GenerateDataKey",
            "DescribeKey"
        ]
    },
    "responseElements": {
"grantId": "0ab0ac0d0b000f00ea00cc0a0e00fc00bce000c000f0000000c0bc0a0000aaafSAMPLE",
        "keyId": "arn:aws:kms:us-east-1:111122223333:key/1234abcd-12ab-34cd-56ef-123456SAMPLE"
    },
    "requestID": "ff000af-00eb-00ce-0e00-ea000fb0fba0SAMPLE",
    "eventID": "ff000af-00eb-00ce-0e00-ea000fb0fba0SAMPLE",
    "readOnly": false,
    "resources": [
        {
"accountId": "111122223333",
            "type": "AWS::KMS::Key",
            "ARN": "arn:aws:kms:us-east-1:111122223333:key/1234abcd-12ab-34cd-56ef-123456SAMPLE"
        }
    ],
    "eventType": "AwsApiCall",
    "managementEvent": true,
    "recipientAccountId": "111122223333",
    "eventCategory": "Management"
}



```

Attach the following resource-based policy to the KMS key by following the steps at [Creating a policy](../../../kms/latest/developerguide/key-policy-overview.md "../../../kms/latest/developerguide/key-policy-overview.md"). The policy contains two statements.

1. Permissions for a role to encrypt model customization artifacts. Add ARNs of the imported custom model builder roles to the `Principal` field.
2. Permissions for a role to use the imported custom model in inference. Add ARNs of imported custom model user roles to the `Principal` field.

JSON

```
`{
 "Version":"2012-10-17",
 "Id": "KMS Key Policy",
 "Statement": [
 {
 "Sid": "Permissions for imported model builders",
 "Effect": "Allow",
 "Principal": {
 "AWS": "arn:aws:iam::`123456789012`:user/role"
 },
 "Action": [
 "kms:Decrypt",
 "kms:GenerateDataKey",
 "kms:DescribeKey",
 "kms:CreateGrant"
 ],
 "Resource": "*"
 },
 {
 "Sid": "Permissions for imported model users",
 "Effect": "Allow",
 "Principal": {
 "AWS": "arn:aws:iam::`123456789012`:user/role"
 },
 "Action": "kms:Decrypt",
 "Resource": "*"
 }
 ]
}`

```
