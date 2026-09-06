

# Data encryption at rest for Amazon Location Service
<a name="encryption-at-rest"></a>

Amazon Location Service provides encryption by default to protect sensitive customer data at rest using AWS owned encryption keys.
+ **AWS owned keys** — Amazon Location uses these keys by default to automatically encrypt personally identifiable data. You can't view, manage, or use AWS owned keys, or audit their use. However, you don't have to take any action or change any programs to protect the keys that encrypt your data. For more information, see [AWS owned keys](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#aws-owned-cmk) in the *AWS Key Management Service Developer Guide*. 

Encryption of data at rest by default helps reduce the operational overhead and complexity involved in protecting sensitive data. At the same time, it enables you to build secure applications that meet strict encryption compliance and regulatory requirements. 

While you can't disable this layer of encryption or select an alternate encryption type, you can add a second layer of encryption over the existing AWS owned encryption keys by choosing a customer managed key when you create your tracker and geofence collection resources:
+ **Customer managed keys** — Amazon Location supports the use of a symmetric customer managed key that you create, own, and manage to add a second layer of encryption over the existing AWS owned encryption. Because you have full control of this layer of encryption, you can perform such tasks as: 
  + Establishing and maintaining key policies
  + Establishing and maintaining IAM policies and grants
  + Enabling and disabling key policies
  + Rotating key cryptographic material
  + Adding tags
  + Creating key aliases
  + Scheduling keys for deletion

  For more information, see [customer managed key](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#customer-cmk) in the *AWS Key Management Service Developer Guide*. 

The following table summarizes how Amazon Location encrypts personally identifiable data.


| Data type | AWS owned key encryption | Customer managed key encryption (Optional) | 
| --- | --- | --- | 
| PositionA point geometry containing [the device position details](https://docs.aws.amazon.com/location/latest/APIReference/API_WaypointTracking_DevicePosition.html). | Enabled | Enabled | 
| PositionPropertiesA set of key-value pairs [associated with the position update](https://docs.aws.amazon.com/location/latest/APIReference/API_WaypointTracking_DevicePosition.html). | Enabled | Enabled | 
| GeofenceGeometryA polygon [geofence geometry](https://docs.aws.amazon.com/location/latest/APIReference/API_WaypointGeofencing_GeofenceGeometry.html) representing the geofenced area. | Enabled | Enabled | 
| DeviceIdThe device identifier specified when [uploading a device position update](https://docs.aws.amazon.com/location/latest/APIReference/API_WaypointTracking_DevicePositionUpdate.html) to a tracker resource. | Enabled | Not supported | 
| GeofenceIdAn identifier specified when [storing a geofence geometry](https://docs.aws.amazon.com/location/latest/APIReference/API_WaypointGeofencing_PutGeofence.html), or a [batch of geofences](https://docs.aws.amazon.com/location/latest/APIReference/API_WaypointGeofencing_BatchPutGeofence.html) in a given geofence collection.  | Enabled | Not supported | 

**Note**  
Amazon Location automatically enables encryption at rest using AWS owned keys to protect personally identifiable data at no charge.   
However, AWS KMS charges apply for using a customer managed key. For more information about pricing, see the [AWS Key Management Service pricing](https://aws.amazon.com/kms/pricing/).

For more information on AWS KMS, see [What is AWS Key Management Service?](https://docs.aws.amazon.com/kms/latest/developerguide/overview.html) 

## How Amazon Location Service uses grants in AWS KMS
<a name="encryption-grant"></a>

Amazon Location requires a [grant](https://docs.aws.amazon.com/kms/latest/developerguide/grants.html) to use your customer managed key.

When you create a [tracker resource](https://docs.aws.amazon.com/location/latest/developerguide/trackers.html) or [geofence collection](https://docs.aws.amazon.com/location/latest/developerguide/geofences.html) encrypted with a customer managed key, Amazon Location creates a grant on your behalf by sending a [CreateGrant](https://docs.aws.amazon.com/kms/latest/APIReference/API_CreateGrant.html) request to AWS KMS. Grants in AWS KMS are used to give Amazon Location access to a KMS key in a customer account.

Amazon Location requires the grant to use your customer managed key for the following internal operations:
+ Send [DescribeKey](https://docs.aws.amazon.com/kms/latest/APIReference/API_DescribeKey.html) requests to AWS KMS to verify that the symmetric customer managed KMS key ID entered when creating a tracker or geofence collection is valid.
+ Send [GenerateDataKeyWithoutPlaintext](https://docs.aws.amazon.com/kms/latest/APIReference/API_GenerateDataKeyWithoutPlaintext.html) requests to AWS KMS to generate data keys encrypted by your customer managed key.
+ Send [Decrypt](https://docs.aws.amazon.com/kms/latest/APIReference/API_Decrypt.html) requests to AWS KMS to decrypt the encrypted data keys so that they can be used to encrypt your data.

You can revoke access to the grant, or remove the service's access to the customer managed key at any time. If you do, Amazon Location won't be able to access any of the data encrypted by the customer managed key, which affects operations that are dependent on that data. For example, if you attempt to [get device positions](https://docs.aws.amazon.com/location/latest/APIReference/API_WaypointTracking_GetDevicePosition.html) from an encrypted tracker that Amazon Location can't access, then the operation would return an `AccessDeniedException` error.

## Create a customer managed key
<a name="create-key"></a>

 You can create a symmetric customer managed key by using the AWS Management Console, or the AWS KMS APIs.

**To create a symmetric customer managed key**

Follow the steps for [Creating symmetric customer managed key](https://docs.aws.amazon.com/kms/latest/developerguide/create-keys.html#create-symmetric-cmk) in the *AWS Key Management Service Developer Guide*.

**Key policy**

Key policies control access to your customer managed key. Every customer managed key must have exactly one key policy, which contains statements that determine who can use the key and how they can use it. When you create your customer managed key, you can specify a key policy. For more information, see [Managing access to customer managed keys](https://docs.aws.amazon.com/kms/latest/developerguide/key-policies.html) in the *AWS Key Management Service Developer Guide*.

To use your customer managed key with your Amazon Location resources, the following API operations must be permitted in the key policy:
+ `[kms:CreateGrant](https://docs.aws.amazon.com/kms/latest/APIReference/API_CreateGrant.html)` – Adds a grant to a customer managed key. Grants control access to a specified KMS key, which allows access to [grant operations](https://docs.aws.amazon.com/kms/latest/developerguide/grants.html#terms-grant-operations) Amazon Location requires. For more information about [Using Grants](https://docs.aws.amazon.com/kms/latest/developerguide/grants.html), see the *AWS Key Management Service Developer Guide*.

  This allows Amazon Location to do the following:
  + Call `GenerateDataKeyWithoutPlainText` to generate an encrypted data key and store it, because the data key isn't immediately used to encrypt.
  + Call `Decrypt` to use the stored encrypted data key to access encrypted data.
  + Set up a retiring principal to allow the service to `RetireGrant`.
+ `[kms:DescribeKey](https://docs.aws.amazon.com/kms/latest/APIReference/API_DescribeKey.html)` – Provides the customer managed key details to allow Amazon Location to validate the key.

The following are policy statement examples you can add for Amazon Location:

```
  "Statement" : [ 
    {
      "Sid" : "Allow access to principals authorized to use Amazon Location",
      "Effect" : "Allow",
      "Principal" : {
        "AWS" : "*"
      },
      "Action" : [ 
        "kms:DescribeKey", 
        "kms:CreateGrant"
      ],
      "Resource" : "*",
      "Condition" : {
        "StringEquals" : {
          "kms:ViaService" : "geo.region.amazonaws.com",
          "kms:CallerAccount" : "111122223333"
        }
    },
    {
      "Sid": "Allow access for key administrators",
      "Effect": "Allow",
      "Principal": {
        "AWS": "arn:aws:iam::111122223333:root"
       },
      "Action" : [ 
        "kms:*"
       ],
      "Resource": "arn:aws:kms:{{region}}:111122223333:key/{{key_ID}}"
    },
    {
      "Sid" : "Allow read-only access to key metadata to the account",
      "Effect" : "Allow",
      "Principal" : {
        "AWS" : "arn:aws:iam::111122223333:root"
      },
      "Action" : [ 
        "kms:Describe*",
        "kms:Get*",
        "kms:List*",
        "kms:RevokeGrant"
      ],
      "Resource" : "*"
    }
  ]
```

For more information about [specifying permissions in a policy](https://docs.aws.amazon.com/kms/latest/developerguide/key-policies.html), see the *AWS Key Management Service Developer Guide*.

For more information about [troubleshooting key access](https://docs.aws.amazon.com/kms/latest/developerguide/policy-evaluation.html#example-no-iam), see the *AWS Key Management Service Developer Guide*.

## Specifying a customer managed key for Amazon Location
<a name="enable-custom-encryption"></a>

You can specify a customer managed key as a second layer encryption for the following resources:
+ [Create a tracker](start-create-tracker.md)
+ [Get started with Amazon Location Service Geofences](geofence-gs.md)

When you create a resource, you can specify the data key by entering a **KMS ID**, which Amazon Location uses to encrypt the identifiable personal data stored by the resource.
+ **KMS ID** — A [key identifier](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#key-id) for an AWS KMS customer managed key. Enter a key ID, key ARN, alias name, or alias ARN.

## Amazon Location Service encryption context
<a name="location-encryption-context"></a>

An [encryption context](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#encrypt_context) is an optional set of key-value pairs that contain additional contextual information about the data.

AWS KMS uses the encryption context as [additional authenticated data](https://docs.aws.amazon.com/kms/latest/cryptographic-details/crypto-primitives.html) to support [authenticated encryption](https://docs.aws.amazon.com/kms/latest/cryptographic-details/crypto-primitives.html). When you include an encryption context in a request to encrypt data, AWS KMS binds the encryption context to the encrypted data. To decrypt data, you include the same encryption context in the request.

**Amazon Location Service encryption context**

Amazon Location uses the same encryption context in all AWS KMS cryptographic operations, where the key is `aws:geo:arn` and the value is the resource [Amazon Resource Name](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference-arns.html) (ARN).

**Example**  

```
"encryptionContext": {
    "aws:geo:arn": "arn:aws:geo:us-west-2:111122223333:geofence-collection/SAMPLE-GeofenceCollection"
}
```

**Using encryption context for monitoring**

When you use a symmetric customer managed key to encrypt your tracker or geofence collection, you can also use the encryption context in audit records and logs to identify how the customer managed key is being used. The encryption context also appears in [logs generated by AWS CloudTrail or Amazon CloudWatch Logs](#example-custom-encryption).

**Using encryption context to control access to your customer managed key**

You can use the encryption context in key policies and IAM policies as `conditions` to control access to your symmetric customer managed key. You can also use encryption context constraints in a grant.

Amazon Location uses an encryption context constraint in grants to control access to the customer managed key in your account or region. The grant constraint requires that the operations that the grant allows use the specified encryption context.

**Example**  
The following are example key policy statements to grant access to a customer managed key for a specific encryption context. The condition in this policy statement requires that the grants have an encryption context constraint that specifies the encryption context.  

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
             "kms:EncryptionContext:aws:geo:arn": "arn:aws:geo:us-west-2:111122223333:tracker/SAMPLE-Tracker"
          }
     }
}
```

## Monitoring your encryption keys for Amazon Location Service
<a name="example-custom-encryption"></a>

When you use an AWS KMS customer managed key with your Amazon Location Service resources, you can use [AWS CloudTrail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-user-guide.html) or [Amazon CloudWatch Logs](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/WhatIsCloudWatchLogs.html) to track requests that Amazon Location sends to AWS KMS.

The following examples are AWS CloudTrail events for `CreateGrant`, `GenerateDataKeyWithoutPlainText`, `Decrypt`, and `DescribeKey` to monitor KMS operations called by Amazon Location to access data encrypted by your customer managed key:

------
#### [ CreateGrant ]

When you use an AWS KMS customer managed key to encrypt your tracker or geofence collection resources, Amazon Location sends a `CreateGrant` request on your behalf to access the KMS key in your AWS account. The grant that Amazon Location creates are specific to the resource associated with the AWS KMS customer managed key. In addition, Amazon Location uses the `RetireGrant` operation to remove a grant when you delete a resource.

The following example event records the `CreateGrant` operation:

```
{
    "eventVersion": "1.08",
    "userIdentity": {
        "type": "AssumedRole",
        "principalId": "AROAIGDTESTANDEXAMPLE:Sampleuser01",
        "arn": "arn:aws:sts::111122223333:assumed-role/Admin/Sampleuser01",
        "accountId": "111122223333",
        "accessKeyId": "AKIAIOSFODNN7EXAMPLE3",
        "sessionContext": {
            "sessionIssuer": {
                "type": "Role",
                "principalId": "AROAIGDTESTANDEXAMPLE:Sampleuser01",
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
        "invokedBy": "geo.amazonaws.com"
    },
    "eventTime": "2021-04-22T17:07:02Z",
    "eventSource": "kms.amazonaws.com",
    "eventName": "CreateGrant",
    "awsRegion": "us-west-2",
    "sourceIPAddress": "172.12.34.56",
    "userAgent": "ExampleDesktop/1.0 (V1; OS)",
    "requestParameters": {
        "retiringPrincipal": "geo.region.amazonaws.com",
        "operations": [
            "GenerateDataKeyWithoutPlaintext",
            "Decrypt",
            "DescribeKey"
        ],
        "keyId": "arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-123456SAMPLE",
        "granteePrincipal": "geo.region.amazonaws.com"
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

------
#### [ GenerateDataKeyWithoutPlainText ]

When you enable an AWS KMS customer managed key for your tracker or geofence collection resource, Amazon Location creates a unique table key. It sends a `GenerateDataKeyWithoutPlainText` request to AWS KMS that specifies the AWS KMS customer managed key for the resource.

The following example event records the `GenerateDataKeyWithoutPlainText` operation:

```
{
    "eventVersion": "1.08",
    "userIdentity": {
        "type": "AWSService",
        "invokedBy": "geo.amazonaws.com"
    },
    "eventTime": "2021-04-22T17:07:02Z",
    "eventSource": "kms.amazonaws.com",
    "eventName": "GenerateDataKeyWithoutPlaintext",
    "awsRegion": "us-west-2",
    "sourceIPAddress": "172.12.34.56",
    "userAgent": "ExampleDesktop/1.0 (V1; OS)",
    "requestParameters": {
        "encryptionContext": {
            "aws:geo:arn": "arn:aws:geo:us-west-2:111122223333:geofence-collection/SAMPLE-GeofenceCollection"
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

------
#### [ Decrypt ]

When you access an encrypted tracker or geofence collection,Amazon Location calls the `Decrypt` operation to use the stored encrypted data key to access the encrypted data. 

The following example event records the `Decrypt` operation:

```
{
    "eventVersion": "1.08",
    "userIdentity": {
        "type": "AWSService",
        "invokedBy": "geo.amazonaws.com"
    },
    "eventTime": "2021-04-22T17:10:51Z",
    "eventSource": "kms.amazonaws.com",
    "eventName": "Decrypt",
    "awsRegion": "us-west-2",
    "sourceIPAddress": "172.12.34.56",
    "userAgent": "ExampleDesktop/1.0 (V1; OS)",
    "requestParameters": {
        "encryptionContext": {
            "aws:geo:arn": "arn:aws:geo:us-west-2:111122223333:geofence-collection/SAMPLE-GeofenceCollection"
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

------
#### [ DescribeKey ]

Amazon Location uses the `DescribeKey` operation to verify if the AWS KMS customer managed key associated with your tracker or geofence collection exists in the account and region.

The following example event records the `DescribeKey` operation:

```
{
    "eventVersion": "1.08",
    "userIdentity": {
        "type": "AssumedRole",
        "principalId": "AROAIGDTESTANDEXAMPLE:Sampleuser01",
        "arn": "arn:aws:sts::111122223333:assumed-role/Admin/Sampleuser01",
        "accountId": "111122223333",
        "accessKeyId": "AKIAIOSFODNN7EXAMPLE3",
        "sessionContext": {
            "sessionIssuer": {
                "type": "Role",
                "principalId": "AROAIGDTESTANDEXAMPLE:Sampleuser01",
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
        "invokedBy": "geo.amazonaws.com"
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

------

## Learn more
<a name="Learn-more-data-at-rest-encryption"></a>

The following resources provide more information about data encryption at rest.
+ For more information about [AWS Key Management Service basic concepts](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html), see the *AWS Key Management Service Developer Guide*.
+ For more information about [Security best practices for AWS Key Management Service](https://docs.aws.amazon.com/kms/latest/developerguide/kms-security.html), see the *AWS Key Management Service Developer Guide*.