# Encryption at rest for azimuth elevation ephemeris

## Key policy requirements for azimuth elevation ephemeris

To use a customer managed key with azimuth elevation ephemeris data, your key policy must grant the following permissions
to the AWS Ground Station service. Unlike TLE and OEM ephemeris data which uses grants, azimuth elevation ephemeris uses direct key policy
permissions for encryption operations. This is a simpler method to manage the permissions of, and use your keys.

- [`kms:GenerateDataKey`](../../../kms/latest/APIReference/API_GenerateDataKey.md "../../../kms/latest/APIReference/API_GenerateDataKey.md")

* Generates data keys for encrypting your azimuth elevation ephemeris data.

- [`kms:Decrypt`](../../../kms/latest/APIReference/API_Decrypt.md "../../../kms/latest/APIReference/API_Decrypt.md")

* Decrypts the encrypted data keys when accessing your azimuth elevation ephemeris data.

### Example key policy granting AWS Ground Station access to a customer managed key

###### Note

With azimuth elevation ephemeris, you must configure these permissions directly in the key policy. The regional AWS Ground Station
service principal (e.g., `groundstation.`region`.amazonaws.com`) must be granted these
permissions in your key policy statements. Without these statements added to the key policy AWS Ground Station will be unable to store or access your
custom azimuth elevation ephemeris.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "Allow AWS Ground Station to Describe key",
 "Effect": "Allow",
 "Principal": {
 "Service": "groundstation.`us-east-1`.amazonaws.com"
 },
 "Action": "kms:DescribeKey",
 "Resource": "*"
 },
 {
 "Sid": "Allow AWS Ground Station to Encrypt and Decrypt with key",
 "Effect": "Allow",
 "Principal": {
 "Service": "groundstation.`us-east-1`.amazonaws.com"
 },
 "Action": [
 "kms:GenerateDataKey",
 "kms:Decrypt"
 ],
 "Resource": "*"
 }
 ]
}`

```

## IAM user permissions for creating azimuth elevation ephemeris with customer managed keys

When AWS Ground Station uses a customer managed key in cryptographic operations, it acts on behalf of the user who is creating
the azimuth elevation ephemeris resource.

To create an azimuth elevation ephemeris resource using a customer managed key, a user must have permissions to call the following
operations on the customer managed key:

- [`kms:GenerateDataKey`](../../../kms/latest/APIReference/API_GenerateDataKey.md "../../../kms/latest/APIReference/API_GenerateDataKey.md")

* Allows the user to generate data keys for encrypting the azimuth elevation ephemeris data.

- [`kms:Decrypt`](../../../kms/latest/APIReference/API_Decrypt.md "../../../kms/latest/APIReference/API_Decrypt.md")

* Allows the user to decrypt data keys when accessing the azimuth elevation ephemeris data.

- [`kms:DescribeKey`](../../../kms/latest/APIReference/API_DescribeKey.md "../../../kms/latest/APIReference/API_DescribeKey.md")

* Allows the user to view the customer managed key details to validate the key.

You can specify these required permissions in a key policy, or in an IAM policy if the key policy allows it.
These permissions ensure that users can authorize AWS Ground Station to use the customer managed key for encryption
operations on their behalf.

## How AWS Ground Station uses key policies for azimuth elevation ephemeris

When you provide azimuth elevation ephemeris data with a customer managed key, AWS Ground Station uses key policies to access
your encryption key. The permissions are granted directly to AWS Ground Station through key policy statements rather than through
grants as with TLE or OEM ephemeris data.

If you remove AWS Ground Station's access to the customer managed key, AWS Ground Station won't be able to access any of the data
encrypted by that key, which affects operations that are dependent on that data. For example, if you remove
key policy permissions for azimuth elevation ephemeris currently in use for a contact, AWS Ground Station will be unable to use the
provided azimuth elevation data for commanding the antenna during the contact. This will cause the contact to end
in a FAILED state.

## Azimuth elevation ephemeris encryption context

When AWS Ground Station uses your AWS KMS key to encrypt azimuth elevation ephemeris data, the service specifies an
[encryption context](../../../kms/latest/developerguide/encrypt_context.md "../../../kms/latest/developerguide/encrypt_context.md").
The encryption context is additional authenticated data (AAD) that AWS KMS uses to ensure data integrity. When an encryption context
is specified for an encryption operation, the service must specify the same encryption context for the decryption
operation. Otherwise, decryption fails. The encryption context is also written to your CloudTrail logs to
help you understand why a given AWS KMS key was used. Your CloudTrail logs might contain many entries describing
the use of a AWS KMS key, but the encryption context in each log entry can help you determine the reason for
that particular use.

AWS Ground Station specifies the following encryption context when it performs cryptographic operations with your
customer managed key on an azimuth elevation ephemeris:

```
{
    "encryptionContext": {
        "aws:groundstation:ground-station-id": "Ohio 1",
        "aws:groundstation:arn": "arn:aws:groundstation:us-east-2:111122223333:ephemeris/00a770b0-082d-45a4-80ed-SAMPLE",
        "aws:s3:arn": "arn:aws:s3:::customerephemerisbucket/00a770b0-082d-45a4-80ed-SAMPLE/raw"
    }
}
```

The encryption context contains:

`aws:groundstation:ground-station-id`

The name of the ground station associated with the azimuth elevation ephemeris.

aws:groundstation:arn

The ARN of the ephemeris resource.

aws:s3:arn

The ARN of the ephemeris stored in Amazon S3.

## Using encryption context to control access to your customer managed key

You can use IAM condition statements to control AWS Ground Station access to your customer managed key. Adding a condition statement on the
`kms:GenerateDataKey` and `kms:Decrypt` actions restricts which ground stations a AWS KMS can be used for.

The following are example key policy statements to grant AWS Ground Station access to your customer managed key in a specific region for a specific ground station.
The condition in this policy statement requires that all encrypt and decrypt access to the key that specify an encryption context that matches the condition in the key policy.

### Example key policy granting AWS Ground Station access to a customer managed key for a specific ground station

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "Allow AWS Ground Station to Describe key",
 "Effect": "Allow",
 "Principal": {
 "Service": "groundstation.`us-east-1`.amazonaws.com"
 },
 "Action": "kms:DescribeKey",
 "Resource": "*"
 },
 {
 "Sid": "Allow AWS Ground Station to Encrypt and Decrypt with key",
 "Effect": "Allow",
 "Principal": {
 "Service": "groundstation.`us-east-1`.amazonaws.com"
 },
 "Action": [
 "kms:GenerateDataKey",
 "kms:Decrypt"
 ],
 "Resource": "*",
 "Condition": {
 "StringEquals": {
 "kms:EncryptionContext:aws:groundstation:ground-station-id": "`specific-ground-station-name`"
 }
 }
 }
 ]
}`

```

### Example key policy granting AWS Ground Station access to a customer managed key for multiple ground stations

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "Allow AWS Ground Station to Describe key",
 "Effect": "Allow",
 "Principal": {
 "Service": "groundstation.`us-east-1`.amazonaws.com"
 },
 "Action": "kms:DescribeKey",
 "Resource": "*"
 },
 {
 "Sid": "Allow AWS Ground Station to Encrypt and Decrypt with key",
 "Effect": "Allow",
 "Principal": {
 "Service": "groundstation.`us-east-1`.amazonaws.com"
 },
 "Action": [
 "kms:GenerateDataKey",
 "kms:Decrypt"
 ],
 "Resource": "*",
 "Condition": {
 "StringLike": {
 "kms:EncryptionContext:aws:groundstation:ground-station-id": [
 "`specific-ground-station-name-1`",
 "`specific-ground-station-name-2`"
 ]
 }
 }
 }
 ]
}`

```

## Monitoring your encryption keys for azimuth elevation ephemeris

When you use an AWS KMS customer managed key with your azimuth elevation ephemeris resources, you can use
[CloudTrail](../../../awscloudtrail/latest/userguide/cloudtrail-user-guide.md "../../../awscloudtrail/latest/userguide/cloudtrail-user-guide.md") or
[CloudWatch logs](../../../AmazonCloudWatch/latest/logs/WhatIsCloudWatchLogs.md "../../../AmazonCloudWatch/latest/logs/WhatIsCloudWatchLogs.md") to track requests that AWS Ground Station sends to AWS KMS. The following examples are CloudTrail
events for [GenerateDataKey](../../../kms/latest/APIReference/API_GenerateDataKey.md "../../../kms/latest/APIReference/API_GenerateDataKey.md")
and [Decrypt](../../../kms/latest/APIReference/API_Decrypt.md "../../../kms/latest/APIReference/API_Decrypt.md") to monitor AWS KMS
operations called by AWS Ground Station to access data encrypted by your customer managed key.

GenerateDataKey

When you use an AWS KMS customer managed key to encrypt your azimuth elevation ephemeris resources, AWS Ground Station sends a
[GenerateDataKey](../../../kms/latest/APIReference/API_GenerateDataKey.md "../../../kms/latest/APIReference/API_GenerateDataKey.md") request
to AWS KMS in order to generate a data key with which to encrypt your data.

The following example event records the [GenerateDataKey](../../../kms/latest/APIReference/API_GenerateDataKey.md "../../../kms/latest/APIReference/API_GenerateDataKey.md")
operation for azimuth elevation ephemeris:

```
{
    "eventVersion": "1.11",
    "userIdentity": {
        "type": "AssumedRole",
        "principalId": "ASIAIOSFODNN7EXAMPLE",
        "arn": "arn:aws:sts::111122223333:assumed-role/Admin/SampleUser01",
        "accountId": "111122223333",
        "accessKeyId": "ASIAIOSFODNN7EXAMPLE",
        "sessionContext": {
            "sessionIssuer": {
                "type": "Role",
                "principalId": "ASIAIOSFODNN7EXAMPLE",
                "arn": "arn:aws:iam::111122223333:role/Admin",
                "accountId": "111122223333",
                "userName": "Admin"
            },
            "attributes": {
                "creationDate": "2025-08-25T14:45:48Z",
                "mfaAuthenticated": "false"
            }
        },
        "invokedBy": "AWS Internal"
    },
    "eventTime": "2025-08-25T14:52:02Z",
    "eventSource": "kms.amazonaws.com",
    "eventName": "GenerateDataKey",
    "awsRegion": "us-west-2",
    "sourceIPAddress": "AWS Internal",
    "userAgent": "AWS Internal",
    "requestParameters": {
        "keySpec": "AES_256",
        "encryptionContext": {
            "aws:groundstation:arn": "arn:aws:groundstation:us-west-2:111122223333:ephemeris/bb650670-7a4b-4152-bd60-SAMPLE",
            "aws:groundstation:ground-station-id": "Ohio 1",
            "aws:s3:arn": "arn:aws:s3:::customerephemerisbucket/bb650670-7a4b-4152-bd60-SAMPLE/raw"
        },
        "keyId": "arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-123456SAMPLE"
    },
    "responseElements": null,
    "requestID": "ef6f9a8f-8ef6-46a1-bdcb-123456SAMPLE",
    "eventID": "952842d4-1389-3232-b885-123456SAMPLE",
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
    "sharedEventID": "8424f6b6-2280-4d1d-b9fd-0348b1546cba",
    "eventCategory": "Management"
}
```

Decrypt

When you use an AWS KMS customer managed key to encrypt your azimuth elevation ephemeris resources, AWS Ground Station uses the
[Decrypt](../../../kms/latest/APIReference/API_Decrypt.md "../../../kms/latest/APIReference/API_Decrypt.md") operation to decrypt
the azimuth elevation ephemeris data provided if they are already encrypted with the same customer managed key.

The following example event records the [Decrypt](../../../kms/latest/APIReference/API_Decrypt.md "../../../kms/latest/APIReference/API_Decrypt.md")
operation for azimuth elevation ephemeris:

```
{
    "eventVersion": "1.11",
    "userIdentity": {
        "type": "AssumedRole",
        "principalId": "ASIAIOSFODNN7EXAMPLE",
        "arn": "arn:aws:sts::111122223333:assumed-role/Admin/SampleUser01",
        "accountId": "111122223333",
        "accessKeyId": "ASIAIOSFODNN7EXAMPLE",
        "sessionContext": {
            "sessionIssuer": {
                "type": "Role",
                "principalId": "ASIAIOSFODNN7EXAMPLE",
                "arn": "arn:aws:iam::111122223333:role/Admin",
                "accountId": "111122223333",
                "userName": "Admin"
            }
        },
        "attributes": {
            "creationDate": "2025-08-25T14:45:48Z",
            "mfaAuthenticated": "false"
        }
    },
    "invokedBy": "AWS Internal",
    "eventTime": "2025-08-25T14:54:01Z",
    "eventSource": "kms.amazonaws.com",
    "eventName": "Decrypt",
    "awsRegion": "us-west-2",
    "sourceIPAddress": "AWS Internal",
    "userAgent": "AWS Internal",
    "requestParameters": {
        "encryptionContext": {
            "aws:groundstation:arn": "arn:aws:groundstation:us-west-2:111122223333:ephemeris/bb650670-7a4b-4152-bd60-SAMPLE",
            "aws:groundstation:ground-station-id": "Ohio 1",
            "aws:s3:arn": "arn:aws:s3:::customerephemerisbucket/bb650670-7a4b-4152-bd60-SAMPLE/raw"
        },
        "encryptionAlgorithm": "SYMMETRIC_DEFAULT"
    },
    "responseElements": null,
    "requestID": "a2f46066-49fb-461a-93cb-123456SAMPLE",
    "eventID": "e997b426-e3ad-31c7-a308-123456SAMPLE",
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
    "sharedEventID": "477b568e-7f56-4f04-905c-623ff146f30d",
    "eventCategory": "Management"
}
```
