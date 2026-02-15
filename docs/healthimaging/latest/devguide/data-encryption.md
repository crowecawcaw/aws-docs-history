# Data encryption

With AWS HealthImaging, you can add a layer of security to your data at rest in the cloud,
providing scalable and efficient encryption features. These include:

- Data at rest encryption capabilities available in most AWS services
- Flexible key management options, including AWS Key Management Service, with which you can
  choose whether to have AWS manage the encryption keys or to keep complete
  control over your own keys.
- AWS owned AWS KMS encryption keys
- Encrypted message queues for the transmission of sensitive data using
  server-side encryption (SSE) for Amazon SQS
  In addition, AWS provides APIs for you to integrate encryption and data protection
  with any of the services you develop or deploy in an AWS environment.

## Creating a customer managed key

You can create a symmetric customer managed key by using the AWS Management Console or the
AWS KMS APIs. For more information, see [Creating
symmetric encryption KMS keys](../../../kms/latest/developerguide/create-keys.md#create-symmetric-cmk "../../../kms/latest/developerguide/create-keys.md#create-symmetric-cmk") in the
_AWS Key Management Service Developer Guide_.

Key policies control access to your customer managed key. Every customer managed
key must have exactly one key policy, which contains statements that determine who
can use the key and how they can use it. When you create your customer managed key,
you can specify a key policy. For more information, see [Managing access to customer managed keys](../../../kms/latest/developerguide/control-access-overview.md#managing-access "../../../kms/latest/developerguide/control-access-overview.md#managing-access") in the
_AWS Key Management Service Developer Guide_.

To use your customer managed key with your HealthImaging resources, [kms:CreateGrant](../../../kms/latest/APIReference/API_CreateGrant.md "../../../kms/latest/APIReference/API_CreateGrant.md") operations must be permitted in the key policy. This
adds a grant to a customer managed key which controls access to a specified
KMS key, which gives a user access to the [Grant
operations](../../../kms/latest/developerguide/grants.md#terms-grant-operations "../../../kms/latest/developerguide/grants.md#terms-grant-operations") HealthImaging requires. For more information, see [Grants in
AWS KMS](../../../kms/latest/developerguide/grants.md "../../../kms/latest/developerguide/grants.md") in the _AWS Key Management Service Developer Guide_.

To use your customer managed KMS key with your HealthImaging resources, the following
API operations must be permitted in the key policy:

- `kms:DescribeKey` provides the customer managed key details
  needed to validate the key. This is required for all operations.
- `kms:GenerateDataKey` provides access to encrypt resources at
  rest for all write operations.
- `kms:Decrypt` provides access to read or search operations for
  encrypted resources.
- `kms:ReEncrypt*` provides access to reencrypt resources.

The following is a policy statement example that allows a user to create and
interact with a data store in HealthImaging which is encrypted by that key:

```
{
    "Sid": "Allow access to create data stores and perform CRUD and search in HealthImaging",
    "Effect": "Allow",
    "Principal": {
        "Service": [
            "medical-imaging.amazonaws.com"
        ]
    },
    "Action": [
        "kms:Decrypt",
        "kms:GenerateDataKey",
        "kms:GenerateDataKeyWithoutPlaintext"
    ],
    "Resource": "*",
    "Condition": {
        "StringEquals": {
            "kms:EncryptionContext:kms-arn": "arn:aws:kms:us-east-1:123456789012:key/bec71d48-3462-4cdd-9514-77a7226e001f",
            "kms:EncryptionContext:aws:medical-imaging:datastoreId": "datastoreId"
        }
    }
}

```

## Required IAM permissions for using a customer

managed KMS key

When creating a data store with AWS KMS encryption enabled using a customer managed
KMS key, there are required permissions for both the key policy and the IAM
policy for the user or role creating the HealthImaging data store.

For more information about key policies, see [Enabling IAM policies](../../../kms/latest/developerguide/key-policies.md#key-policy-default-allow-root-enable-iam "../../../kms/latest/developerguide/key-policies.md#key-policy-default-allow-root-enable-iam") in the
_AWS Key Management Service Developer Guide_.

The IAM user, IAM role, or AWS account creating your repositories must have
permissions for the policy below, plus the necessary permissions for
AWS HealthImaging.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "kms:CreateGrant",
 "kms:GenerateDataKey",
 "kms:RetireGrant",
 "kms:Decrypt",
 "kms:ReEncrypt*"
 ],
 "Resource": "arn:aws:kms:us-east-1:123456789012:key/bec71d48-3462-4cdd-9514-77a7226e001f"
 }
 ]
}`

```

### How HealthImaging uses grants in AWS KMS

HealthImaging requires a [grant](../../../kms/latest/developerguide/grants.md "../../../kms/latest/developerguide/grants.md") to use your
customer managed KMS key. When you create a data store encrypted with a customer
managed KMS key, HealthImaging creates a grant on your behalf by sending a [CreateGrant](../../../kms/latest/APIReference/API_CreateGrant.md "../../../kms/latest/APIReference/API_CreateGrant.md") request to AWS KMS. Grants in AWS KMS are used to give
HealthImaging access to a KMS key in a customer account.

The grants that HealthImaging creates on your behalf should not be revoked or retired.
If you revoke or retire the grant that gives HealthImaging permission to use the AWS KMS
keys in your account, HealthImaging cannot access this data, encrypt new imaging
resources pushed to the data store, or decrypt them when they are pulled. When
you revoke or retire a grant for HealthImaging, the change occurs immediately. To revoke
access rights, you should delete the data store rather than revoke the grant.
When a data store is deleted, HealthImaging retires the grants on your behalf.

### Monitoring your encryption keys for

HealthImaging

You can use CloudTrail to track the requests that HealthImaging sends to AWS KMS on your
behalf when using a customer managed KMS key. The log entries in the CloudTrail log
show `medical-imaging.amazonaws.com` in the `userAgent` field to
clearly distinguish requests made by HealthImaging.

The following examples are CloudTrail events for `CreateGrant`,
`GenerateDataKey`, `Decrypt`, and
`DescribeKey` to monitor AWS KMS operations called by HealthImaging to
access data encrypted by your customer managed key.

The following shows how to use `CreateGrant` to allow HealthImaging to
access a customer provided KMS key, enabling HealthImaging to use that KMS key to
encrypt all customer data at rest.

Users are not required to create their own grants. HealthImaging creates a grant on
your behalf by sending a `CreateGrant` request to AWS KMS. Grants in
AWS KMS are used to give HealthImaging access to a AWS KMS key in a customer account.

```
{
            "KeyId": "arn:aws:kms:us-east-1:147997158357:key/8e1c34df-5fd2-49fa-8986-4618c9829a8c",
            "GrantId": "44e88bc45b769499ce5ec4abd5ecb27eeb3b178a4782452aae65fe885ee5ba20",
            "Name": "MedicalImagingGrantForQIDO_ebff634a-2d16-4046-9238-e3dc4ab54d29",
            "CreationDate": "2025-04-17T20:12:49+00:00",
            "GranteePrincipal": "AWS Internal",
            "RetiringPrincipal": "medical-imaging.us-east-1.amazonaws.com",
            "IssuingAccount": "medical-imaging.us-east-1.amazonaws.com",
            "Operations": [
                "Decrypt",
                "Encrypt",
                "GenerateDataKey",
                "GenerateDataKeyWithoutPlaintext",
                "ReEncryptFrom",
                "ReEncryptTo",
                "CreateGrant",
                "RetireGrant",
                "DescribeKey"
            ]
        },
        {
            "KeyId": "arn:aws:kms:us-east-1:147997158357:key/8e1c34df-5fd2-49fa-8986-4618c9829a8c",
            "GrantId": "9e5fd5ba7812daf75be4a86efb2b1920d6c0c9c0b19781549556bf2ff98953a1",
            "Name": "2025-04-17T20:12:38",
            "CreationDate": "2025-04-17T20:12:38+00:00",
            "GranteePrincipal": "medical-imaging.us-east-1.amazonaws.com",
            "RetiringPrincipal": "medical-imaging.us-east-1.amazonaws.com",
            "IssuingAccount": "AWS Internal",
            "Operations": [
                "Decrypt",
                "Encrypt",
                "GenerateDataKey",
                "GenerateDataKeyWithoutPlaintext",
                "ReEncryptFrom",
                "ReEncryptTo",
                "CreateGrant",
                "RetireGrant",
                "DescribeKey"
            ]
        },
        {
            "KeyId": "arn:aws:kms:us-east-1:147997158357:key/8e1c34df-5fd2-49fa-8986-4618c9829a8c",
            "GrantId": "ab4a9b919f6ca8eb2bd08ee72475658ee76cfc639f721c9caaa3a148941bcd16",
            "Name": "9d060e5b5d4144a895e9b24901088ca5",
            "CreationDate": "2025-04-17T20:12:39+00:00",
            "GranteePrincipal": "AWS Internal",
            "RetiringPrincipal": "medical-imaging.us-east-1.amazonaws.com",
            "IssuingAccount": "medical-imaging.us-east-1.amazonaws.com",
            "Operations": [
                "Decrypt",
                "Encrypt",
                "GenerateDataKey",
                "GenerateDataKeyWithoutPlaintext",
                "ReEncryptFrom",
                "ReEncryptTo",
                "DescribeKey"
            ],
            "Constraints": {
                "EncryptionContextSubset": {
                    "kms-arn": "arn:aws:kms:us-east-1:147997158357:key/8e1c34df-5fd2-49fa-8986-4618c9829a8c"
                }
            }
        }

```

The following examples shows how to use `GenerateDataKey` to ensure
the user has necessary permissions to encrypt data before storing it.

```
{
    "eventVersion": "1.08",
    "userIdentity": {
        "type": "AssumedRole",
        "principalId": "EXAMPLEUSER",
        "arn": "arn:aws:sts::111122223333:assumed-role/Sampleuser01",
        "accountId": "111122223333",
        "accessKeyId": "EXAMPLEKEYID",
        "sessionContext": {
            "sessionIssuer": {
                "type": "Role",
                "principalId": "EXAMPLEROLE",
                "arn": "arn:aws:iam::111122223333:role/Sampleuser01",
                "accountId": "111122223333",
                "userName": "Sampleuser01"
            },
            "webIdFederationData": {},
            "attributes": {
                "creationDate": "2021-06-30T21:17:06Z",
                "mfaAuthenticated": "false"
            }
        },
        "invokedBy": "medical-imaging.amazonaws.com"
    },
    "eventTime": "2021-06-30T21:17:37Z",
    "eventSource": "kms.amazonaws.com",
    "eventName": "GenerateDataKey",
    "awsRegion": "us-east-1",
    "sourceIPAddress": "medical-imaging.amazonaws.com",
    "userAgent": "medical-imaging.amazonaws.com",
    "requestParameters": {
        "keySpec": "AES_256",
        "keyId": "arn:aws:kms:us-east-1:111122223333:key/EXAMPLE_KEY_ARN"
    },
    "responseElements": null,
    "requestID": "EXAMPLE_ID_01",
    "eventID": "EXAMPLE_ID_02",
    "readOnly": true,
    "resources": [
        {
            "accountId": "111122223333",
            "type": "AWS::KMS::Key",
            "ARN": "arn:aws:kms:us-east-1:111122223333:key/EXAMPLE_KEY_ARN"
        }
    ],
    "eventType": "AwsApiCall",
    "managementEvent": true,
    "recipientAccountId": "111122223333",
    "eventCategory": "Management"
}

```

The following example shows how HealthImaging calls the `Decrypt` operation
to use the stored encrypted data key to access the encrypted data.

```
{
    "eventVersion": "1.08",
    "userIdentity": {
        "type": "AssumedRole",
        "principalId": "EXAMPLEUSER",
        "arn": "arn:aws:sts::111122223333:assumed-role/Sampleuser01",
        "accountId": "111122223333",
        "accessKeyId": "EXAMPLEKEYID",
        "sessionContext": {
            "sessionIssuer": {
                "type": "Role",
                "principalId": "EXAMPLEROLE",
                "arn": "arn:aws:iam::111122223333:role/Sampleuser01",
                "accountId": "111122223333",
                "userName": "Sampleuser01"
            },
            "webIdFederationData": {},
            "attributes": {
                "creationDate": "2021-06-30T21:17:06Z",
                "mfaAuthenticated": "false"
            }
        },
        "invokedBy": "medical-imaging.amazonaws.com"
    },
    "eventTime": "2021-06-30T21:21:59Z",
    "eventSource": "kms.amazonaws.com",
    "eventName": "Decrypt",
    "awsRegion": "us-east-1",
    "sourceIPAddress": "medical-imaging.amazonaws.com",
    "userAgent": "medical-imaging.amazonaws.com",
    "requestParameters": {
        "encryptionAlgorithm": "SYMMETRIC_DEFAULT",
        "keyId": "arn:aws:kms:us-east-1:111122223333:key/EXAMPLE_KEY_ARN"
    },
    "responseElements": null,
    "requestID": "EXAMPLE_ID_01",
    "eventID": "EXAMPLE_ID_02",
    "readOnly": true,
    "resources": [
        {
            "accountId": "111122223333",
            "type": "AWS::KMS::Key",
            "ARN": "arn:aws:kms:us-east-1:111122223333:key/EXAMPLE_KEY_ARN"
        }
    ],
    "eventType": "AwsApiCall",
    "managementEvent": true,
    "recipientAccountId": "111122223333",
    "eventCategory": "Management"
}

```

The following example shows how HealthImaging uses the `DescribeKey`
operation to verify if the AWS KMS customer owned AWS KMS key is in a usable state
and to help a user troubleshoot if it is not functional.

```
{
    "eventVersion": "1.08",
    "userIdentity": {
        "type": "AssumedRole",
        "principalId": "EXAMPLEUSER",
        "arn": "arn:aws:sts::111122223333:assumed-role/Sampleuser01",
        "accountId": "111122223333",
        "accessKeyId": "EXAMPLEKEYID",
        "sessionContext": {
            "sessionIssuer": {
                "type": "Role",
                "principalId": "EXAMPLEROLE",
                "arn": "arn:aws:iam::111122223333:role/Sampleuser01",
                "accountId": "111122223333",
                "userName": "Sampleuser01"
            },
            "webIdFederationData": {},
            "attributes": {
                "creationDate": "2021-07-01T18:36:14Z",
                "mfaAuthenticated": "false"
            }
        },
        "invokedBy": "medical-imaging.amazonaws.com"
    },
    "eventTime": "2021-07-01T18:36:36Z",
    "eventSource": "kms.amazonaws.com",
    "eventName": "DescribeKey",
    "awsRegion": "us-east-1",
    "sourceIPAddress": "medical-imaging.amazonaws.com",
    "userAgent": "medical-imaging.amazonaws.com",
    "requestParameters": {
        "keyId": "arn:aws:kms:us-east-1:111122223333:key/EXAMPLE_KEY_ARN"
    },
    "responseElements": null,
    "requestID": "EXAMPLE_ID_01",
    "eventID": "EXAMPLE_ID_02",
    "readOnly": true,
    "resources": [
        {
            "accountId": "111122223333",
            "type": "AWS::KMS::Key",
            "ARN": "arn:aws:kms:us-east-1:111122223333:key/EXAMPLE_KEY_ARN"
        }
    ],
    "eventType": "AwsApiCall",
    "managementEvent": true,
    "recipientAccountId": "111122223333",
    "eventCategory": "Management"
}

```

### Learn more

The following resources provide more information about data at rest encryption
and are located in the in the _AWS Key Management Service Developer Guide_.

- [AWS KMS
  concepts](../../../kms/latest/developerguide/concepts.md "../../../kms/latest/developerguide/concepts.md")
- [Security best
  practices for AWS KMS](../../../kms/latest/developerguide/best-practices.md "../../../kms/latest/developerguide/best-practices.md")
