

# Encryption at rest with AWS Key Management Service
<a name="kms-encryption-at-rest"></a>

By default, AWS Network Firewall provides encryption for your data at rest using *AWS owned keys* to protect sensitive customer data. Or, you can use symmetric *customer managed keys* that you create, own, and manage to encrypt your data at rest.
+ **AWS owned keys** — Network Firewall uses these keys to automatically encrypt personally identifiable data. You can't view, manage, or use AWS owned keys, or audit their use. However, you don't have to take any action or change any programs to protect the keys that encrypt your data. Encryption of data at rest by default helps reduce the operational overhead and complexity involved in protecting sensitive data. At the same time, it enables you to build secure applications that meet strict encryption compliance and regulatory requirements. For more information about using AWS owned keys, see [AWS owned keys](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#aws-owned-cmk) in the *AWS Key Management Service Developer Guide*. 
+ **Customer managed keys** — Network Firewall supports the use of a symmetric customer managed key that you create, own, and manage. You can specify a customer managed key when you create your firewall, firewall policy, and rule group resources. Because you have full control over this type of encryption, you can perform such tasks as:
  + Establishing and maintaining key policies
  + Establishing and maintaining IAM policies and grants
  + Enabling and disabling key policies
  + Rotating key cryptographic material
  + Adding tags
  + Creating key aliases
  + Scheduling keys for deletion

  For more information, see [Customer managed keys](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#customer-cmk) in the *AWS Key Management Service Developer Guide*. 

**Note**  
Network Firewall automatically enables encryption at rest using AWS owned keys to protect personally identifiable data at no charge. Standard AWS KMS charges apply when using customer managed keys. For more information about pricing, see the [AWS Key Management Service pricing](https://aws.amazon.com/kms/pricing/). 

For general information on AWS KMS, see [What is AWS Key Management Service?](https://docs.aws.amazon.com/kms/latest/developerguide/overview.html) in the *AWS Key Management Service Developer Guide*. 

## Using customer managed keys with Network Firewall
<a name="Using-cust-keys"></a>

The following section provides information about using customer managed keys with Network Firewall.

**Topics**
+ [How AWS Network Firewall uses grants in AWS KMS](#encryption-grant)
+ [Creating a customer managed key](#create-key)
+ [Specifying a customer managed key for Network Firewall](#enable-custom-encryption)
+ [AWS Network Firewall encryption context](#location-encryption-context)
+ [Monitoring customer managed keys](#example-custom-encryption)

### How AWS Network Firewall uses grants in AWS KMS
<a name="encryption-grant"></a>

Network Firewall requires a [grant](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#grant) to use your customer managed key.

When you create a firewall, firewall policy, or rule group encrypted with a customer managed key, Network Firewall creates a grant on your behalf by sending a [CreateGrant](https://docs.aws.amazon.com/kms/latest/APIReference/API_CreateGrant.html) request to AWS KMS. Grants in AWS KMS are used to give Network Firewall access to a KMS key in a customer account.

Network Firewall requires the grant to use your customer managed key for the following internal operations:
+ Send [DescribeKey](https://docs.aws.amazon.com/kms/latest/APIReference/API_DescribeKey.html) requests to AWS KMS to verify that the symmetric customer managed key ID entered when creating a firewall, firewall policy, or rule group is valid.
+ Send [GenerateDataKey](https://docs.aws.amazon.com/kms/latest/APIReference/API_GenerateDataKey.html) requests to AWS KMS to generate data keys encrypted by your customer managed key.
+ Send [Decrypt](https://docs.aws.amazon.com/kms/latest/APIReference/API_Decrypt.html) requests to AWS KMS to decrypt the encrypted data keys so that they can be used to encrypt your data.

**Important**  
You can revoke access to the grant or delete the customer managed key at any time. However if you do, the Network Firewall resources that are dependent on the customer managed key won't function. The firewall endpoints encrypted with the customer managed key will drop all packets. To continue to use the resource types that are associated with the customer managed key, you must delete the dependent resources, and then recreate your resources with a key containing adequate permissions.

### Creating a customer managed key
<a name="create-key"></a>

 You can create a symmetric customer managed key by using the AWS Management Console, or the AWS KMS APIs.

**To create a symmetric customer managed key**

Follow the steps for [Creating symmetric customer managed key](https://docs.aws.amazon.com/kms/latest/developerguide/create-keys.html#create-symmetric-cmk) in the *AWS Key Management Service Developer Guide*.

**Key policy**

Key policies control access to your customer managed key. Every customer managed key must have exactly one key policy, which contains statements that determine who can use the key and how they can use it. When you create your customer managed key, you can specify a key policy. For more information, see [Managing access to customer managed keys](https://docs.aws.amazon.com/kms/latest/developerguide/control-access-overview.html#managing-access) in the *AWS Key Management Service Developer Guide*.

To use your customer managed key with your Network Firewall resources, the following API operations must be permitted in the key policy:
+ `[kms:CreateGrant](https://docs.aws.amazon.com/kms/latest/APIReference/API_CreateGrant.html)` – Adds a grant to a customer managed key. Grants control access to a specified KMS key, which allows access to [grant operations](https://docs.aws.amazon.com/kms/latest/developerguide/grants.html#terms-grant-operations) Network Firewall requires. For more information, see [Using Grants](https://docs.aws.amazon.com/kms/latest/developerguide/grants.html) in the*AWS Key Management Service Developer Guide*.

  This allows Network Firewall to do the following:
  + Call `GenerateDataKey` to generate an encrypted data key and store it, because the data key isn't immediately used to encrypt.
  + Call `Decrypt` to use the stored encrypted data key to access encrypted data.
  + Set up a retiring principal to allow the service to `RetireGrant`.

The following are policy statement examples you can add for Network Firewall:

------
#### [ JSON ]

****  

```
          {
    "Id": "key-consolepolicy-3",
    "Version":"2012-10-17",		 	 	 
    "Statement": [
        {
            "Sid": "Enable IAM User Permissions",
            "Effect": "Allow",
            "Principal": {
                "AWS": "arn:aws:iam::{{111122223333}}:root"
            },
            "Action": "kms:*",
            "Resource": "*"
        },
        {
            "Sid": "Allow access for Key Administrators",
            "Effect": "Allow",
            "Principal": {
                "AWS": "arn:aws:iam::{{111122223333}}:role/Admin"
            },
            "Action": [
                "kms:Create*",
                "kms:Describe*",
                "kms:Enable*",
                "kms:List*",
                "kms:Put*",
                "kms:Update*",
                "kms:Revoke*",
                "kms:Disable*",
                "kms:Get*",
                "kms:Delete*",
                "kms:TagResource",
                "kms:UntagResource",
                "kms:ScheduleKeyDeletion",
                "kms:CancelKeyDeletion"
            ],
            "Resource": "*"
        },
        {
            "Sid": "Allow use of the key",
            "Effect": "Allow",
            "Principal": {
                "AWS": "arn:aws:iam::{{111122223333}}:root"
            },
            "Action": [
                "kms:Encrypt",
                "kms:Decrypt",
                "kms:ReEncrypt*",
                "kms:GenerateDataKey*",
                "kms:DescribeKey"
            ],
            "Resource": "*"
        },
        {
            "Sid": "Allow attachment of persistent resources",
            "Effect": "Allow",
            "Principal": {
                "AWS": "arn:aws:iam::{{111122223333}}:root"
            },
            "Action": [
                "kms:CreateGrant",
                "kms:ListGrants",
                "kms:RevokeGrant"
            ],
            "Resource": "*",
            "Condition": {
                "Bool": {
                    "kms:GrantIsForAWSResource": "true"
                }
            }
        }
    ]
}
```

------

For information about [specifying permissions in a policy](https://docs.aws.amazon.com/kms/latest/developerguide/control-access-overview.html#overview-policy-elements), see the *AWS Key Management Service Developer Guide*. For more information about [troubleshooting key access](https://docs.aws.amazon.com/kms/latest/developerguide/policy-evaluation.html#example-no-iam), see the *AWS Key Management Service Developer Guide*.

### Specifying a customer managed key for Network Firewall
<a name="enable-custom-encryption"></a>

You can specify a customer managed key for the following resources:
+ Firewalls
+ Firewall policies
+ Rule groups
+ TLS inspection configurations

When you create a resource, you can specify the data key by entering an *AWS KMS ID*, which Network Firewall uses to encrypt the identifiable personal data stored by the resource. An AWS KMS ID is a [key identifier](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#key-id) for an AWS KMS customer managed key. You can specify a key ID, key ARN, alias name, or alias ARN.

### AWS Network Firewall encryption context
<a name="location-encryption-context"></a>

An [encryption context](https://docs.aws.amazon.com/kms/latest/developerguide/encrypt_context.html) is an optional set of key-value pairs that contain additional contextual information about the data. AWS KMS uses the encryption context as additional authenticated data to support authenticated encryption. When you include an encryption context in a request to encrypt data, AWS KMS binds the encryption context to the encrypted data. To decrypt data, you include the same encryption context in the request.

**AWS Network Firewall encryption context**

Network Firewall uses the same encryption context in all AWS KMS cryptographic operations, where the key is `aws:network-firewall:resource-id` and the value is the resource [Amazon Resource Name](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) (ARN).

**Example**  

```
"encryptionContext": {
    "aws:network-firewall:resource-id": "abcdef-b795-4280-8560-3c2b5e723c41"
}
```

**Using encryption context for monitoring**

When you use a symmetric customer managed key to encrypt your Network Firewall resources, you can also use the encryption context in audit records and logs to identify how the customer managed key is being used. The encryption context also appears in [logs generated by AWS CloudTrail or Amazon CloudWatch Logs](#example-custom-encryption).

**Using encryption context to control access to your customer managed key**

You can use the encryption context in key policies and IAM policies as `conditions` to control access to your symmetric customer managed key. You can also use encryption context constraints in a grant.

Network Firewall uses an encryption context constraint in grants to control access to the customer managed key in your account or Region. The grant constraint requires that the operations that the grant allows use the specified encryption context.

**Example**  
The following are example key policy statements to grant access to a customer managed key for a specific encryption context. The condition in this policy statement requires that the grants have an encryption context constraint that specifies the encryption context.  

```
{
    "KeyId": "arn:aws:kms:{{region}}:111122223333:key/1234abcd-12ab-34cd-56ef-123456SAMPLE",
    "GrantId": "{{grant_ID}}",
    "Name": "11223344-abcd-1111-2222-111222333444",
    "CreationDate": "2022-03-16T14:42:42-04:00",
    "GranteePrincipal": "network-firewall.{{region}}.amazonaws.com",
    "RetiringPrincipal": "network-firewall.{{region}}.amazonaws.com",
    "IssuingAccount": "111122223333",
    "Operations": [
        "Decrypt",
        "GenerateDataKey",
        "RetireGrant"
    ],
    "Constraints": {
        "EncryptionContextSubset": {
            "aws:network-firewall:resource-id": "11223344-aabb-1122-3344-111222333444"
        }
    }
}
```

### Monitoring customer managed keys
<a name="example-custom-encryption"></a>

When you use an AWS KMS customer managed key with your AWS Network Firewall resources, you can use [AWS CloudTrail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-user-guide.html) or [Amazon CloudWatch Logs](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/WhatIsCloudWatchLogs.html) to track requests that Network Firewall sends to AWS KMS.

The following example is an AWS CloudTrail event for `CreateGrant` to monitor KMS operations called by Network Firewall to access data encrypted by your customer managed key:

When you use an AWS KMS customer managed key to encrypt your Network Firewall resources, Network Firewall sends a `CreateGrant` request on your behalf to access the KMS key in your AWS account. The grant that Network Firewall creates are specific to the resource associated with the AWS KMS customer managed key. In addition, Network Firewall uses the `RetireGrant` operation to remove a grant when you delete a resource.

The following example event records the `CreateGrant` operation:

------
#### [ CreateGrant ]

When you use an AWS KMS customer managed key to encrypt your Network Firewall resources, Network Firewall sends a `CreateGrant` request on your behalf to access the customer managed key in your AWS account. The grant that Network Firewall creates are specific to the resource associated with the AWS KMS customer managed key. In addition, Network Firewall uses the `RetireGrant` operation to remove a grant when you delete a resource.

The following example event records the `CreateGrant` operation:

```
{
    "eventVersion": "1.08",
    "userIdentity": {
        "type": "AssumedRole",
        "principalId": "AROAIGDTESTANDEXAMPLE:Sampleuser01",
        "arn": "arn:aws:sts::555555555555:assumed-role/Admin/example_Account",
        "accountId": "555555555555",
        "accessKeyId": "AKIAIOSFODNN7EXAMPLE3",
        "sessionContext": {
            "sessionIssuer": {
                "type": "Role",
                "principalId": "AROAIGDTESTANDEXAMPLE:Sampleuser01",
                "arn": "arn:aws:iam::555555555555:role/Admin",
                "accountId": "555555555555",
                "userName": "Admin"
            },
            "webIdFederationData": {},
            "attributes": {
                "creationDate": "2022-03-16T18:41:09Z",
                "mfaAuthenticated": "false"
            }
        },
        "invokedBy": "555555555555"
    },
    "eventTime": "2022-03-16T18:42:42Z",
    "eventSource": "kms.amazonaws.com",
    "eventName": "CreateGrant",
    "awsRegion": "{{region}}",
    "sourceIPAddress": "192.0.2.0/24",
    "userAgent": "111122223333",
    "requestParameters": {
        "keyId": "arn:aws:kms:{{region}}:111122223333:key/1234abcd-12ab-34cd-56ef-123456SAMPLE",
        "retiringPrincipal": "network-firewall.{{region}}.amazonaws.com",
        "operations": [
            "Decrypt",
            "GenerateDataKey",
            "RetireGrant"
        ],
        "granteePrincipal": "network-firewall.{{region}}.amazonaws.com",
        "constraints": {
            "encryptionContextSubset": {
                "aws:network-firewall:resource-id": "1234abcd-12ab-34cd-56ef-123456SAMPLE"
            }
        }
    },
    "responseElements": {
        "grantId": "0ab0ac0d0b000f00ea00cc0a0e00fc00bce000c000f0000000c0bc0a0000aaafSAMPLE"
    },
    "requestID": "ff000af-00eb-00ce-0e00-ea000fb0fba0SAMPLE",
    "eventID": "ff000af-00eb-00ce-0e00-ea000fb0fba0SAMPLE",
    "readOnly": false,
    "resources": [
        {
            "accountId": "093688922507",
            "type": "AWS::KMS::Key",
            "ARN": "arn:aws:kms:{{region}}:111122223333:key/1234abcd-12ab-34cd-56ef-123456SAMPLE"
        }
    ],
    "eventType": "AwsApiCall",
    "managementEvent": true,
    "recipientAccountId": "555555555555",
    "sharedEventID": "ff000af-00eb-00ce-0e00-ea000fb0fba0SAMPLE",
    "eventCategory": "Management"
}
```

------
#### [ GenerateDataKey ]

When you enable an AWS KMS customer managed key for your Network Firewall resource, Network Firewall creates a unique table key. It sends a `GenerateDataKey` request to AWS KMS that specifies the AWS KMS customer managed key for the resource.

The following example event records the `GenerateDataKey` operation:

```
{
    "eventVersion": "1.08",
    "userIdentity": {
        "type": "AWSService",
        "invokedBy": "444455556666"
    },
    "eventTime": "2022-03-10T17:16:28Z",
    "eventSource": "kms.amazonaws.com",
    "eventName": "GenerateDataKey",
    "awsRegion": "{{region}}",
    "sourceIPAddress": "198.51.100.0/24",
    "userAgent": "ExampleDesktop/1.0 (V1; OS)",
    "requestParameters": {
        "keySpec": "AES_256",
        "keyId": "arn:aws:kms:{{region}}:444455556666:key/1234abcd-12ab-34cd-56ef-123456SAMPLE",
        "encryptionContext": {
            "aws:network-firewall:resource-id": "1234abcd-12ab-34cd-56ef-123456SAMPLE",
            "aws:s3:arn": "arn:aws:s3:::service-bucket/stateless-rulegroup/9876abcd-12ab-23cd-56ef-123456SAMPLE/1/1234abcd-12ab-34cd-56ef-123456SAMPLE"
        }
    },
    "responseElements": null,
    "requestID": "aa000af-00eb-00ce-0e00-ea000gh0fba0SAMPLE",
    "eventID": "ff000af-00eb-00ce-0e00-ea000fb0fba0SAMPLE",
    "readOnly": true,
    "resources": [
        {
            "accountId": "444455556666",
            "type": "AWS::KMS::Key",
            "ARN": "arn:aws:kms:{{region}}:444455556666:key/1234abcd-12ab-34cd-56ef-123456SAMPLE"
        }
    ],
    "eventType": "AwsApiCall",
    "managementEvent": true,
    "recipientAccountId": "444455556666",
    "sharedEventID": "ff000af-00eb-00ce-0e00-ea000fb0fba0SAMPLE",
    "eventCategory": "Management"
}
```

------
#### [ Decrypt ]

When you access an encrypted resource, Network Firewall calls the `Decrypt` operation to use the stored encrypted data key to access the encrypted data. 

The following example event records the `Decrypt` operation:

```
{
    "eventVersion": "1.08",
    "userIdentity": {
        "type": "AWSService",
        "invokedBy": "444455556666"
    },
    "eventTime": "2022-03-10T17:16:33Z",
    "eventSource": "kms.amazonaws.com",
    "eventName": "Decrypt",
    "awsRegion": "{{region}}",
    "sourceIPAddress": "198.51.100.0/24",
    "userAgent": "ExampleDesktop/1.0 (V1; OS)",
    "requestParameters": {
        "encryptionContext": {
            "aws:network-firewall:resource-id": "1234abcd-12ab-34cd-56ef-123456SAMPLE",
            "aws:s3:arn": "arn:aws:s3:::service-bucket/stateless-rulegroup/9876abcd-12ab-23cd-56ef-123456SAMPLE/1/1234abcd-12ab-34cd-56ef-123456SAMPLE"
        },
        "encryptionAlgorithm": "SYMMETRIC_DEFAULT"
    },
    "responseElements": null,
    "requestID": "ff000af-00eb-00ce-0e00-ea000fb0fba0SAMPLE",
    "eventID": "ff000af-00eb-00ce-0e00-ea000fb0fba0SAMPLE",
    "readOnly": true,
    "resources": [
        {
            "accountId": "444455556666",
            "type": "AWS::KMS::Key",
            "ARN": "arn:aws:kms:{{region}}:444455556666:key/1234abcd-12ab-34cd-56ef-123456SAMPLE"
        }
    ],
    "eventType": "AwsApiCall",
    "managementEvent": true,
    "recipientAccountId": "444455556666",
    "sharedEventID": "ff000af-00eb-00ce-0e00-ea000fb0fba0SAMPLE",
    "eventCategory": "Management"
}
```

------

## Learn more
<a name="Learn-more-data-at-rest-encryption"></a>

The following resources provide more information about data encryption at rest.
+ For more information about [AWS Key Management Service basic concepts](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html), see the *AWS Key Management Service Developer Guide*.
+ For more information about [Security best practices for AWS Key Management Service](https://docs.aws.amazon.com/kms/latest/developerguide/best-practices.html), see the *AWS Key Management Service Developer Guide*.