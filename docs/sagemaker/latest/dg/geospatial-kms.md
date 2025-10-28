# Use AWS KMS Permissions for Amazon SageMaker geospatial capabilities

You can protect your data at rest using encryption for SageMaker geospatial capabilities. By default, it uses server-side encryption with an Amazon SageMaker geospatial owned key.
SageMaker geospatial capabilities also supports an option for server-side encryption with a customer managed KMS key.

## Server-Side Encryption with Amazon SageMaker geospatial managed key (Default)

SageMaker geospatial capabilities encrypts all your data, including computational results from your Earth Observation jobs (EOJ)
and Vector Enrichment jobs (VEJ) along with all your service metadata. There is no data that is stored within SageMaker geospatial capabilities
unencrypted. It uses a default AWS owned key to encrypt all your data.

## Server-Side Encryption with customer managed KMS key (Optional)

SageMaker geospatial capabilities supports the use of a symmetric customer managed key that you create,
own, and manage to add a second layer of encryption over the existing AWS owned encryption. Because you
have full control of this layer of encryption, you can perform such tasks as:

- Establishing and maintaining key policies
- Establishing and maintaining IAM policies and grants
- Enabling and disabling key policies
- Rotating key cryptographic material
- Adding tags
- Creating key aliases
- Scheduling keys for deletion

For more information, see [Customer managed keys](../../../kms/latest/developerguide/concepts.md#customer-cmk "../../../kms/latest/developerguide/concepts.md#customer-cmk") in the _AWS Key Management Service Developer Guide_.

## How SageMaker geospatial capabilities uses grants in AWS KMS

SageMaker geospatial capabilities requires a grant to use your customer managed key.
When you create an EOJ or an VEJ encrypted with a customer managed key, SageMaker geospatial capabilities creates
a grant on your behalf by sending a `CreateGrant` request to AWS KMS. Grants in AWS KMS are used to
give SageMaker geospatial capabilities access to a KMS key in a customer account. You can revoke access to the grant,
or remove the service's access to the customer managed key at any time. If you do, SageMaker geospatial capabilities
won't be able to access any of the data encrypted by the customer managed key,
which affects operations that are dependent on that data.

## Create a customer managed key

You can create a symmetric customer managed key by using the AWS Management Console, or the AWS KMS APIs.

**To create a symmetric customer managed key**

Follow the steps for [Creating symmetric encryption KMS keys](../../../kms/latest/developerguide/create-keys.md#create-symmetric-cmk "../../../kms/latest/developerguide/create-keys.md#create-symmetric-cmk") in the AWS Key Management Service Developer Guide.

**Key policy**

Key policies control access to your customer managed key. Every customer managed key must have exactly
one key policy, which contains statements that determine who can use the key and how they can use it.
When you create your customer managed key, you can specify a key policy. For more information,
see [Determining access to AWS KMS keys](../../../kms/latest/developerguide/determining-access.md "../../../kms/latest/developerguide/determining-access.md") in the _AWS Key Management Service Developer Guide_.

To use your customer managed key with your SageMaker geospatial capabilities resources, the following API operations
must be permitted in the key policy. The principal for these operations should be the Execution Role
you provide in the SageMaker geospatial capabilities request. SageMaker geospatial capabilities assumes the provided Execution Role in
the request to perform these KMS operations.

- `kms:CreateGrant`
- `kms:GenerateDataKey`
- `kms:Decrypt`
- `kms:GenerateDataKeyWithoutPlaintext`

The following are policy statement examples you can add for SageMaker geospatial capabilities:

**CreateGrant**

```
"Statement" : [
    {
      "Sid" : "Allow access to Amazon SageMaker geospatial capabilities",
      "Effect" : "Allow",
      "Principal" : {
        "AWS" : "<Customer provided Execution Role ARN>"
      },
      "Action" : [
          "kms:CreateGrant",
           "kms:Decrypt",
           "kms:GenerateDataKey",
           "kms:GenerateDataKeyWithoutPlaintext"
      ],
      "Resource" : "*",
    },
 ]
```

For more information about specifying permissions in a policy, see [AWS KMS permissions](../../../kms/latest/developerguide/kms-api-permissions-reference.md "../../../kms/latest/developerguide/kms-api-permissions-reference.md") in the _AWS Key Management Service Developer Guide_.
For more information about troubleshooting, see [Troubleshooting key access](../../../kms/latest/developerguide/policy-evaluation.md "../../../kms/latest/developerguide/policy-evaluation.md") in the _AWS Key Management Service Developer Guide_.

If your key policy does not have your account root as key administrator,
you need to add the same KMS permissions on your execution role ARN. Here is a sample policy you can add
to the execution role:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Action": [
 "kms:CreateGrant",
 "kms:Decrypt",
 "kms:GenerateDataKey",
 "kms:GenerateDataKeyWithoutPlaintext"
 ],
 "Resource": [
 "arn:aws:kms:`us-east-1`:`111122223333`:key/`key-id`"
 ],
 "Effect": "Allow"
 }
 ]
}`

```

## Monitoring your encryption keys for SageMaker geospatial capabilities

When you use an AWS KMS customer managed key with your SageMaker geospatial capabilities resources,
you can use AWS CloudTrail or Amazon CloudWatch Logs to track requests that SageMaker geospatial sends to AWS KMS.

Select a tab in the following table to see examples of AWS CloudTrail events to monitor KMS operations called by SageMaker geospatial capabilities
to access data encrypted by your customer managed key.

CreateGrant

```
{
    "eventVersion": "1.08",
    "userIdentity": {
        "type": "AssumedRole",
        "principalId": "AROAIGDTESTANDEXAMPLE:SageMaker-Geospatial-StartEOJ-KMSAccess",
        "arn": "arn:aws:sts::111122223333:assumed-role/SageMakerGeospatialCustomerRole/SageMaker-Geospatial-StartEOJ-KMSAccess",
        "accountId": "111122223333",
        "accessKeyId": "AKIAIOSFODNN7EXAMPLE3",
        "sessionContext": {
            "sessionIssuer": {
                "type": "Role",
                "principalId": "AKIAIOSFODNN7EXAMPLE3",
                "arn": "arn:aws:sts::111122223333:assumed-role/SageMakerGeospatialCustomerRole",
                "accountId": "111122223333",
                "userName": "SageMakerGeospatialCustomerRole"
            },
            "webIdFederationData": {},
            "attributes": {
                "creationDate": "2023-03-17T18:02:06Z",
                "mfaAuthenticated": "false"
            }
        },
        "invokedBy": "arn:aws:iam::111122223333:root"
    },
    "eventTime": "2023-03-17T18:02:06Z",
    "eventSource": "kms.amazonaws.com",
    "eventName": "CreateGrant",
    "awsRegion": "us-west-2",
    "sourceIPAddress": "172.12.34.56",
    "userAgent": "ExampleDesktop/1.0 (V1; OS)",
    "requestParameters": {
        "retiringPrincipal": "sagemaker-geospatial.us-west-2.amazonaws.com",
        "keyId": "arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-123456SAMPLE",
        "operations": [
            "Decrypt"
        ],
        "granteePrincipal": "sagemaker-geospatial.us-west-2.amazonaws.com"
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
    "eventCategory": "Management"
}
```

GenerateDataKey

```
{
    "eventVersion": "1.08",
    "userIdentity": {
        "type": "AWSService",
        "invokedBy": "sagemaker-geospatial.amazonaws.com"
    },
    "eventTime": "2023-03-24T00:29:45Z",
    "eventSource": "kms.amazonaws.com",
    "eventName": "GenerateDataKey",
    "awsRegion": "us-west-2",
    "sourceIPAddress": "sagemaker-geospatial.amazonaws.com",
    "userAgent": "sagemaker-geospatial.amazonaws.com",
    "requestParameters": {
        "encryptionContext": {
            "aws:s3:arn": "arn:aws:s3:::axis-earth-observation-job-378778860802/111122223333/napy9eintp64/output/consolidated/32PPR/2022-01-04T09:58:03Z/S2B_32PPR_20220104_0_L2A_msavi.tif"
        },
        "keyId": "arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-123456SAMPLE",
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

Decrypt

```
{
    "eventVersion": "1.08",
    "userIdentity": {
        "type": "AWSService",
        "invokedBy": "sagemaker-geospatial.amazonaws.com"
    },
    "eventTime": "2023-03-28T22:04:24Z",
    "eventSource": "kms.amazonaws.com",
    "eventName": "Decrypt",
    "awsRegion": "us-west-2",
    "sourceIPAddress": "sagemaker-geospatial.amazonaws.com",
    "userAgent": "sagemaker-geospatial.amazonaws.com",
    "requestParameters": {
        "encryptionAlgorithm": "SYMMETRIC_DEFAULT",
        "encryptionContext": {
            "aws:s3:arn": "arn:aws:s3:::axis-earth-observation-job-378778860802/111122223333/napy9eintp64/output/consolidated/32PPR/2022-01-04T09:58:03Z/S2B_32PPR_20220104_0_L2A_msavi.tif"
        },
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

GenerateDataKeyWithoutPlainText

```
{
    "eventVersion": "1.08",
    "userIdentity": {
        "type": "AssumedRole",
        "principalId": "AROAIGDTESTANDEXAMPLE:SageMaker-Geospatial-StartEOJ-KMSAccess",
        "arn": "arn:aws:sts::111122223333:assumed-role/SageMakerGeospatialCustomerRole/SageMaker-Geospatial-StartEOJ-KMSAccess",
        "accountId": "111122223333",
        "accessKeyId": "AKIAIOSFODNN7EXAMPLE3",
        "sessionContext": {
            "sessionIssuer": {
                "type": "Role",
                "principalId": "AKIAIOSFODNN7EXAMPLE3",
                "arn": "arn:aws:sts::111122223333:assumed-role/SageMakerGeospatialCustomerRole",
                "accountId": "111122223333",
                "userName": "SageMakerGeospatialCustomerRole"
            },
            "webIdFederationData": {},
            "attributes": {
                "creationDate": "2023-03-17T18:02:06Z",
                "mfaAuthenticated": "false"
            }
        },
        "invokedBy": "arn:aws:iam::111122223333:root"
    },
    "eventTime": "2023-03-28T22:09:16Z",
    "eventSource": "kms.amazonaws.com",
    "eventName": "GenerateDataKeyWithoutPlaintext",
    "awsRegion": "us-west-2",
    "sourceIPAddress": "172.12.34.56",
    "userAgent": "ExampleDesktop/1.0 (V1; OS)",
    "requestParameters": {
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
    "recipientAccountId": "111122223333",
    "eventCategory": "Management"
}
```
