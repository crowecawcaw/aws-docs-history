# Key management

When creating a new farm, you can choose one of the following keys to encrypt your farm
 data:


* **AWS owned KMS key** – Default encryption
 type if you don't specify a key when you create the farm. The KMS key is owned by
 AWS Deadline Cloud. You can't view, manage, or use AWS owned keys. However, you don't need to
 take any action to protect the keys that encrypt your data. For more information, see
 [AWS owned keys](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#aws-owned-cmk "https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#aws-owned-cmk") in the *AWS Key Management Service developer guide*.
* **Customer managed KMS key** – You specify a
 customer managed key when you create a farm. All of the content within the farm is
 encrypted with the KMS key. The key is stored in your account and is created, owned, and
 managed by you and AWS KMS charges apply. You have full control over the KMS key. You can
 perform such tasks as:




	+ Establishing and maintaining key polices
	+ Establishing and maintaining IAM policies and grants
	+ Enabling and disabling key policies
	+ Adding tags
	+ Creating key aliases
You can't manually rotate a customer owned key used with a Deadline Cloud farm. Automatic
 rotation of the key is supported.


For more information, see [Customer owned keys](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#customer-cmk "https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#customer-cmk")
 in the *AWS Key Management Service Developer Guide*.


To create a customer managed key, follow the steps for [Creating symmetric
 customer managed keys](https://docs.aws.amazon.com/kms/latest/developerguide/create-keys.html#create-symmetric-cmk "https://docs.aws.amazon.com/kms/latest/developerguide/create-keys.html#create-symmetric-cmk") in the *AWS Key Management Service Developer Guide*.

## How Deadline Cloud uses AWS KMS grants


Deadline Cloud requires a [grant](https://docs.aws.amazon.com/kms/latest/developerguide/grants.html "https://docs.aws.amazon.com/kms/latest/developerguide/grants.html") to use your customer managed key. When you create a farm encrypted with a
 customer managed key, Deadline Cloud creates a grant on your behalf by sending a `[CreateGrant](https://docs.aws.amazon.com/kms/latest/APIReference/API_CreateGrant.html "https://docs.aws.amazon.com/kms/latest/APIReference/API_CreateGrant.html")` request to AWS KMS to get access to the KMS key that you
 specified.


Deadline Cloud uses multiple grants. Each grant is used by a different part of Deadline Cloud that needs
 to encrypt or decrypt your data. Deadline Cloud also uses grants to allow access to other AWS
 services used to store data on your behalf, such as Amazon Simple Storage Service, Amazon Elastic Block Store, or
 OpenSearch.


Grants that enable Deadline Cloud to manage machines in a service-managed fleet include a Deadline Cloud
 account number and role in the `GranteePrincipal` instead of a service principal.
 While not typical, this is necessary to encrypt Amazon EBS volumes for workers in service-managed
 fleets using the customer managed KMS key specified for the farm.


## Customer managed key policy


Key policies control access to your customer managed key. Each key must have exactly one
 key policy that contains statements that determine who can use the key and how they can use
 it. When you create you customer managed key, you can specify a key policy. For more
 information, see [Managing
 access to customer managed keys](https://docs.aws.amazon.com/kms/latest/developerguide/control-access-overview.html#managing-access "https://docs.aws.amazon.com/kms/latest/developerguide/control-access-overview.html#managing-access") in the *AWS Key Management Service Developer
 Guide*.


### Minimal IAM policy for CreateFarm


To use your customer managed key to create farms using the console or the `[CreateFarm](../APIReference/API_CreateFarm.md "../APIReference/API_CreateFarm.md")` API operation, the following AWS KMS API operations must be
 permitted:



* `[kms:CreateGrant](https://docs.aws.amazon.com/kms/latest/APIReference/API_CreateGrant.html "https://docs.aws.amazon.com/kms/latest/APIReference/API_CreateGrant.html")`
 – Adds a grant to a customer managed key. Grants console access to a specified
 AWS KMS key. For more informations, see [Using grants](https://docs.aws.amazon.com/kms/latest/developerguide/grants.html "https://docs.aws.amazon.com/kms/latest/developerguide/grants.html") in the
 *AWS Key Management Service developer guide*.
* `[kms:Decrypt](https://docs.aws.amazon.com/kms/latest/APIReference/API_Decrypt.html "https://docs.aws.amazon.com/kms/latest/APIReference/API_Decrypt.html")` – Allows Deadline Cloud to decrypt data in the
 farm.
* `[kms:DescribeKey](https://docs.aws.amazon.com/kms/latest/APIReference/API_DescribeKey.html "https://docs.aws.amazon.com/kms/latest/APIReference/API_DescribeKey.html")`
 – Provides the customer managed key details to allow Deadline Cloud to validate the
 key.
* `[kms:GenerateDataKey](https://docs.aws.amazon.com/kms/latest/APIReference/API_GenerateDataKey.html "https://docs.aws.amazon.com/kms/latest/APIReference/API_GenerateDataKey.html")` – Allows Deadline Cloud to encrypt data using a
 unique data key.

The following policy statement grants the necessary permissions for the
 `CreateFarm` operation.



JSON





```
`{
 "Version":"2012-10-17", 
 "Statement": [
 {
 "Sid": "DeadlineCreateGrants",
 "Effect": "Allow",
 "Action": [
 "kms:Decrypt",
 "kms:GenerateDataKey",
 "kms:CreateGrant",
 "kms:DescribeKey"
 ],
 "Resource": "arn:aws:kms:us-west-2:`111122223333`:key/`1234567890abcdef0`",
 "Condition": {
 "StringEquals": {
 "kms:ViaService": "deadline.us-west-2.amazonaws.com"
 }
 }
 }
 ]
}`

```





### Minimal IAM policy for read-only operations


To use your customer managed key for read-only Deadline Cloud operations, such getting
 information about farms, queues, and fleets. The following AWS KMS API operations must be
 permitted:



* `[kms:Decrypt](https://docs.aws.amazon.com/kms/latest/APIReference/API_Decrypt.html "https://docs.aws.amazon.com/kms/latest/APIReference/API_Decrypt.html")` – Allows Deadline Cloud to decrypt data in the
 farm.
* `[kms:DescribeKey](https://docs.aws.amazon.com/kms/latest/APIReference/API_DescribeKey.html "https://docs.aws.amazon.com/kms/latest/APIReference/API_DescribeKey.html")`
 – Provides the customer managed key details to allow Deadline Cloud to validate the
 key.

The following policy statement grants the necessary permissions for read-only
 operations.



JSON





```
`{
 "Version":"2012-10-17", 
 "Statement": [
 {
 "Sid": "DeadlineReadOnly",
 "Effect": "Allow",
 "Action": [
 "kms:Decrypt",
 "kms:DescribeKey"
 ],
 "Resource": "arn:aws:kms:us-west-2:`111122223333`:key/`a1b2c3d4-5678-90ab-cdef-EXAMPLE11111`",
 "Condition": {
 "StringEquals": {
 "kms:ViaService": "deadline.us-west-2.amazonaws.com"
 }
 }
 }
 ]
}`

```





### Minimal IAM policy for read-write operations


To use your customer managed key for read-write Deadline Cloud operations, such as creating and
 updating farms, queues, and fleets. The following AWS KMS API operations must be
 permitted:



* `[kms:Decrypt](https://docs.aws.amazon.com/kms/latest/APIReference/API_Decrypt.html "https://docs.aws.amazon.com/kms/latest/APIReference/API_Decrypt.html")` – Allows Deadline Cloud to decrypt data in the
 farm.
* `[kms:DescribeKey](https://docs.aws.amazon.com/kms/latest/APIReference/API_DescribeKey.html "https://docs.aws.amazon.com/kms/latest/APIReference/API_DescribeKey.html")`
 – Provides the customer managed key details to allow Deadline Cloud to validate the
 key.
* `[kms:GenerateDataKey](https://docs.aws.amazon.com/kms/latest/APIReference/API_GenerateDataKey.html "https://docs.aws.amazon.com/kms/latest/APIReference/API_GenerateDataKey.html")` – Allows Deadline Cloud to encrypt data using a
 unique data key.

The following policy statement grants the necessary permissions for the
 `CreateFarm` operation.



JSON





```
`{
 "Version":"2012-10-17", 
 "Statement": [
 {
 "Sid": "DeadlineReadWrite",
 "Effect": "Allow",
 "Action": [
 "kms:Decrypt",
 "kms:DescribeKey",
 "kms:GenerateDataKey"
 ],
 "Resource": "arn:aws:kms:us-west-2:`111122223333`:key/`a1b2c3d4-5678-90ab-cdef-EXAMPLE11111`",
 "Condition": {
 "StringEquals": {
 "kms:ViaService": "deadline.us-west-2.amazonaws.com"
 }
 }
 }
 ]
}`

```





## Monitoring your encryption keys


When you use an AWS KMS customer managed key with your Deadline Cloud farms, you can use [AWS CloudTrail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-user-guide.html "https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-user-guide.html") or [Amazon CloudWatch Logs](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/WhatIsCloudWatchLogs.html "https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/WhatIsCloudWatchLogs.html") to track
 requests that Deadline Cloud sends to AWS KMS.


### CloudTrail event for grants


The following example CloudTrail event occurs when grants are created, typically when you
 call the `CreateFarm`, `CreateMonitor`, or `CreateFleet`
 operation.



```
{
    "eventVersion": "1.08",
    "userIdentity": {
        "type": "AssumedRole",
        "principalId": "`AROAIGDTESTANDEXAMPLE`:`SampleUser01`",
        "arn": "arn:aws::sts::`111122223333`:assumed-role/Admin/`SampleUser01`",
        "accountId": "`111122223333`",
        "accessKeyId": "`AKIAIOSFODNN7EXAMPLE3`",
        "sessionContext": {
            "sessionIssuer": {
                "type": "Role",
                "principalId": "`AROAIGDTESTANDEXAMPLE`",
                "arn": "arn:aws::iam::`111122223333`:role/Admin",
                "accountId": "`111122223333`",
                "userName": "Admin"
            },
            "webIdFederationData": {},
            "attributes": {
                "creationDate": "2024-04-23T02:05:26Z",
                "mfaAuthenticated": "false"
            }
        },
        "invokedBy": "deadline.amazonaws.com"
    },
    "eventTime": "2024-04-23T02:05:35Z",
    "eventSource": "kms.amazonaws.com",
    "eventName": "CreateGrant",
    "awsRegion": "us-west-2",
    "sourceIPAddress": "deadline.amazonaws.com",
    "userAgent": "deadline.amazonaws.com",
    "requestParameters": {
        "operations": [
            "CreateGrant",
            "Decrypt",
            "DescribeKey",
            "Encrypt",
            "GenerateDataKey"
        ],
        "constraints": {
            "encryptionContextSubset": {
                "aws:deadline:farmId": "farm-`abcdef12345678900987654321fedcba`",
                "aws:deadline:accountId": "`111122223333`"
            }
        },
        "granteePrincipal": "deadline.amazonaws.com",
        "keyId": "arn:aws::kms:us-west-2:`111122223333`:key/`a1b2c3d4-5678-90ab-cdef-EXAMPLE11111`",
        "retiringPrincipal": "deadline.amazonaws.com"
    },
    "responseElements": {
        "grantId": "`6bbe819394822a400fe5e3a75d0e9ef16c1733143fff0c1fc00dc7ac282a18a0`",
        "keyId": "arn:aws::kms:us-west-2:`111122223333`:key/`a1b2c3d4-5678-90ab-cdef-EXAMPLE11111`"
    },
    "requestID": "`a1b2c3d4-5678-90ab-cdef-EXAMPLE22222`",
    "eventID": "`a1b2c3d4-5678-90ab-cdef-EXAMPLE33333`",
    "readOnly": false,
    "resources": [
        {
            "accountId": "AWS Internal",
            "type": "AWS::KMS::Key",
            "ARN": "arn:aws::kms:us-west-2:`111122223333`:key/a1b2c3d4-5678-90ab-cdef-EXAMPLE44444"
        }
    ],
    "eventType": "AwsApiCall",
    "managementEvent": true,
    "recipientAccountId": "`111122223333`",
    "eventCategory": "Management"
}
```

### CloudTrail event for decryption


The following example CloudTrail event occurs when decrypting values using the customer
 managed KMS key.



```
{
    "eventVersion": "1.08",
    "userIdentity": {
        "type": "AssumedRole",
        "principalId": "`AROAIGDTESTANDEXAMPLE`:`SampleUser01`",
        "arn": "arn:aws::sts::111122223333:assumed-role/`SampleRole`/`SampleUser01`",
        "accountId": "111122223333",
        "accessKeyId": "`AKIAIOSFODNN7EXAMPLE`",
        "sessionContext": {
            "sessionIssuer": {
                "type": "Role",
                "principalId": "`AROAIGDTESTANDEXAMPLE`",
                "arn": "arn:aws::iam::`111122223333`:role/`SampleRole`",
                "accountId": "`111122223333`",
                "userName": "`SampleRole`"
            },
            "webIdFederationData": {},
            "attributes": {
                "creationDate": "2024-04-23T18:46:51Z",
                "mfaAuthenticated": "false"
            }
        },
        "invokedBy": "deadline.amazonaws.com"
    },
    "eventTime": "2024-04-23T18:51:44Z",
    "eventSource": "kms.amazonaws.com",
    "eventName": "Decrypt",
    "awsRegion": "us-west-2",
    "sourceIPAddress": "deadline.amazonaws.com",
    "userAgent": "deadline.amazonaws.com",
    "requestParameters": {
        "encryptionContext": {
            "aws:deadline:farmId": "farm-`abcdef12345678900987654321fedcba`",
            "aws:deadline:accountId": "`111122223333`",
            "aws-crypto-public-key": "`AotL+SAMPLEVALUEiOMEXAMPLEaaqNOTREALaGTESTONLY+p/5H+EuKd4Q==`"
        },
        "encryptionAlgorithm": "SYMMETRIC_DEFAULT",
        "keyId": "arn:aws::kms:us-west-2:`111122223333`:key/`a1b2c3d4-5678-90ab-cdef-EXAMPLE11111`"
    },
    "responseElements": null,
    "requestID": "`aaaaaaaa-bbbb-cccc-dddd-eeeeeeffffff`",
    "eventID": "`ffffffff-eeee-dddd-cccc-bbbbbbaaaaaa`",
    "readOnly": true,
    "resources": [
        {
            "accountId": "`111122223333`",
            "type": "AWS::KMS::Key",
            "ARN": "arn:aws::kms:us-west-2:`111122223333`:key/`a1b2c3d4-5678-90ab-cdef-EXAMPLE11111`"
        }
    ],
    "eventType": "AwsApiCall",
    "managementEvent": true,
    "recipientAccountId": "`111122223333`",
    "eventCategory": "Management"
}
```

### CloudTrail event for encryption


The following example CloudTrail event occurs when encrypting values using the customer
 managed KMS key.



```
{
    "eventVersion": "1.08",
    "userIdentity": {
        "type": "AssumedRole",
        "principalId": "`AROAIGDTESTANDEXAMPLE`:`SampleUser01`",
        "arn": "arn:aws::sts::`111122223333`:assumed-role/`SampleRole`/`SampleUser01`",
        "accountId": "`111122223333`",
        "accessKeyId": "`AKIAIOSFODNN7EXAMPLE`",
        "sessionContext": {
            "sessionIssuer": {
                "type": "Role",
                "principalId": "`AROAIGDTESTANDEXAMPLE`",
                "arn": "arn:aws::iam::`111122223333`:role/`SampleRole`",
                "accountId": "`111122223333`",
                "userName": "SampleRole"
            },
            "webIdFederationData": {},
            "attributes": {
                "creationDate": "2024-04-23T18:46:51Z",
                "mfaAuthenticated": "false"
            }
        },
        "invokedBy": "deadline.amazonaws.com"
    },
    "eventTime": "2024-04-23T18:52:40Z",
    "eventSource": "kms.amazonaws.com",
    "eventName": "GenerateDataKey",
    "awsRegion": "us-west-2",
    "sourceIPAddress": "deadline.amazonaws.com",
    "userAgent": "deadline.amazonaws.com",
    "requestParameters": {
        "numberOfBytes": 32,
        "encryptionContext": {
            "aws:deadline:farmId": "farm-`abcdef12345678900987654321fedcba`",
            "aws:deadline:accountId": "`111122223333`",
            "aws-crypto-public-key": "`AotL+SAMPLEVALUEiOMEXAMPLEaaqNOTREALaGTESTONLY+p/5H+EuKd4Q==`"
        },
        "keyId": "arn:aws::kms:us-west-2:`111122223333`:key/`abcdef12-3456-7890-0987-654321fedcba`"
    },
    "responseElements": null,
    "requestID": "`a1b2c3d4-5678-90ab-cdef-EXAMPLE11111`",
    "eventID": "`a1b2c3d4-5678-90ab-cdef-EXAMPLE22222`",
    "readOnly": true,
    "resources": [
        {
            "accountId": "`111122223333`",
            "type": "AWS::KMS::Key",
            "ARN": "arn:aws::kms:us-west-2:`111122223333`:key/`a1b2c3d4-5678-90ab-cdef-EXAMPLE33333`"
        }
    ],
    "eventType": "AwsApiCall",
    "managementEvent": true,
    "recipientAccountId": "`111122223333`",
    "eventCategory": "Management"
}
```

## Deleting a customer managed KMS key


Deleting a customer managed KMS key in AWS Key Management Service (AWS KMS) is destructive and
 potentially dangerous. It irreversibly deletes the key material and all metadata associated
 with the key. After a customer managed KMS key is deleted, you can no longer decrypt the
 data that was encrypted by that key. This means that the data becomes unrecoverable.


This is why AWS KMS gives customers a waiting period of up to 30 days before deleting the
 KMS key. The default waiting period is 30 days.


### About the waiting period


Because it's destructive and potentially dangerous to delete a customer managed
 KMS key, we require that you set a waiting period of 7–30 days. The default
 waiting period is 30 days.


However, the actual waiting period might be up to 24 hours longer than the period you
 scheduled. To get the actual date and time when the key will be deleted, use the [DescribeKey](https://docs.aws.amazon.com/kms/latest/APIReference/API_DescribeKey.html "https://docs.aws.amazon.com/kms/latest/APIReference/API_DescribeKey.html") operation. You can also see the scheduled deletion
 date of a key in the [AWS KMS
 console](https://docs.aws.amazon.com/kms/latest/developerguide/viewing-keys-console.html#viewing-details-navigate "https://docs.aws.amazon.com/kms/latest/developerguide/viewing-keys-console.html#viewing-details-navigate") on the key’s detail page, in the **General
 configuration** section. Notice the time zone.


During the waiting period, the customer managed key’s status and key state is
 **Pending deletion**.



* A customer managed KMS key that is pending deletion can’t be used in any [cryptographic
 operations](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#cryptographic-operations "https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#cryptographic-operations").
* AWS KMS doesn’t [rotate the
 backing keys](https://docs.aws.amazon.com/kms/latest/developerguide/rotate-keys.html#rotate-keys-how-it-works "https://docs.aws.amazon.com/kms/latest/developerguide/rotate-keys.html#rotate-keys-how-it-works") of customer managed KMS keys that are pending
 deletion.

For more information about deleting a customer managed KMS key, see [Deleting
 customer master keys](https://docs.aws.amazon.com/kms/latest/developerguide/deleting-keys.html "https://docs.aws.amazon.com/kms/latest/developerguide/deleting-keys.html") in the *AWS Key Management Service Developer Guide*.
