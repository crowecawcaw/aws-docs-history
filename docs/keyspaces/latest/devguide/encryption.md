# Encryption at rest: How to use customer managed

keys to encrypt tables in Amazon Keyspaces

You can use the console or CQL statements to specify the AWS KMS key for new tables and
update the encryption keys of existing tables in Amazon Keyspaces. The following topic outlines how to
implement customer managed keys for new and existing tables.

###### Topics

- [Prerequisites: Create a customer managed key
  using AWS KMS and grant permissions to Amazon Keyspaces](#encryption.createCMKMS "#encryption.createCMKMS")
- [Step 3: Specify a customer managed key for
  a new table](#encryption.tutorial-creating "#encryption.tutorial-creating")
- [Step 4: Update the encryption key of an
  existing table](#encryption.tutorial-update "#encryption.tutorial-update")
- [Step 5: Use the Amazon Keyspaces encryption context in logs](#encryption-context "#encryption-context")
- [Step 6: Configure monitoring with AWS CloudTrail](#encryption-cmk-trail "#encryption-cmk-trail")

## Prerequisites: Create a customer managed key

using AWS KMS and grant permissions to Amazon Keyspaces

Before you can protect an Amazon Keyspaces table with a [customer managed key](encryption.md#customer-managed "encryption.md#customer-managed"), you must first create the key in AWS Key Management Service (AWS KMS) and then authorize
Amazon Keyspaces to use that key.

### Step 1: Create a customer managed key using

AWS KMS

To create a customer managed key to be used to protect an Amazon Keyspaces table, you can follow the steps in [Creating symmetric encryption KMS keys](../../../kms/latest/developerguide/create-keys.md#create-symmetric-cmk "../../../kms/latest/developerguide/create-keys.md#create-symmetric-cmk")
using the console or the AWS API.

### Step 2: Authorize the use of your customer managed

key

Before you can choose a [customer managed key](encryption.md#customer-managed "encryption.md#customer-managed") to protect an Amazon Keyspaces table, the policies on that
customer managed key must give Amazon Keyspaces permission to use it on your behalf. You have full control over the
policies and grants on the customer managed key. You can provide these permissions in a [key policy](../../../kms/latest/developerguide/key-policies.md "../../../kms/latest/developerguide/key-policies.md"), an [IAM
policy](../../../kms/latest/developerguide/iam-policies.md "../../../kms/latest/developerguide/iam-policies.md"), or a [grant](../../../kms/latest/developerguide/grants.md "../../../kms/latest/developerguide/grants.md").

Amazon Keyspaces doesn't need additional authorization to use the default [AWS owned key](encryption.md#keyspaces-owned "encryption.md#keyspaces-owned") to protect the Amazon Keyspaces tables in your AWS
account.

The following topics show how to configure the required permissions using IAM
policies and grants that allow Amazon Keyspaces tables to use a customer managed key.

###### Topics

- [Key policy for customer managed keys](#encryption-customer-managed-policy "#encryption-customer-managed-policy")
- [Example key policy](#encryption-customer-managed-policy-sample "#encryption-customer-managed-policy-sample")
- [Using grants to authorize Amazon Keyspaces](#encryption-grants "#encryption-grants")

#### Key policy for customer managed keys

When you select a [customer managed key](encryption.md#customer-managed "encryption.md#customer-managed") to
protect an Amazon Keyspaces table, Amazon Keyspaces gets permission to use the customer managed key on behalf of the
principal who makes the selection. That principal, a user or role, must have the permissions
on the customer managed key that Amazon Keyspaces requires.

At a minimum, Amazon Keyspaces requires the following permissions on a customer managed key:

- [kms:Encrypt](../../../kms/latest/APIReference/API_Encrypt.md "../../../kms/latest/APIReference/API_Encrypt.md")
- [kms:Decrypt](../../../kms/latest/APIReference/API_Decrypt.md "../../../kms/latest/APIReference/API_Decrypt.md")
- [kms:ReEncrypt](../../../kms/latest/APIReference/API_ReEncrypt.md "../../../kms/latest/APIReference/API_ReEncrypt.md")\* (for kms:ReEncryptFrom and
  kms:ReEncryptTo)
- kms:GenerateDataKey\* (for [kms:GenerateDataKey](../../../kms/latest/APIReference/API_GenerateDataKey.md "../../../kms/latest/APIReference/API_GenerateDataKey.md") and [kms:GenerateDataKeyWithoutPlaintext](../../../kms/latest/APIReference/API_GenerateDataKeyWithoutPlaintext.md "../../../kms/latest/APIReference/API_GenerateDataKeyWithoutPlaintext.md"))
- [kms:DescribeKey](../../../kms/latest/APIReference/API_DescribeKey.md "../../../kms/latest/APIReference/API_DescribeKey.md")
- [kms:CreateGrant](../../../kms/latest/APIReference/API_CreateGrant.md "../../../kms/latest/APIReference/API_CreateGrant.md")

#### Example key policy

For example, the following example key policy provides only the required permissions.
The policy has the following effects:

- Allows Amazon Keyspaces to use the customer managed key in cryptographic operations and create
  grants—but only when it's acting on behalf of principals in the account who have
  permission to use Amazon Keyspaces. If the principals specified in the policy statement don't have
  permission to use Amazon Keyspaces, the call fails, even when it comes from the Amazon Keyspaces service.
- The [kms:ViaService](../../../kms/latest/developerguide/policy-conditions.md#conditions-kms-via-service "../../../kms/latest/developerguide/policy-conditions.md#conditions-kms-via-service") condition key
  allows the permissions only when the request comes from Amazon Keyspaces on behalf of the principals
  listed in the policy statement. These principals can't call these operations directly.
  Note that the `kms:ViaService` value, `cassandra.**\***.amazonaws.com`, has an asterisk (\*) in the Region position. Amazon Keyspaces
  requires the permission to be independent of any particular AWS Region.
- Gives the customer managed key administrators (users who can assume the `db-team` role)
  read-only access to the customer managed key and permission to revoke grants, including the [grants that Amazon Keyspaces requires](#encryption-grants "#encryption-grants") to protect the table.
- Gives Amazon Keyspaces read-only access to the customer managed key. In this case, Amazon Keyspaces can call these
  operations directly. It doesn't have to act on behalf of an account principal.

Before using an example key policy, replace the example principals with actual principals
from your AWS account.

```
{
  "Id": "key-policy-cassandra",
  "Version":"2012-10-17",
  "Statement": [
    {
      "Sid" : "Allow access through Amazon Keyspaces for all principals in the account that are authorized to use Amazon Keyspaces",
      "Effect": "Allow",
      "Principal": {"AWS": "`arn:aws:iam::`111122223333`:user/db-lead`"},
      "Action": [
        "kms:Encrypt",
        "kms:Decrypt",
        "kms:ReEncrypt*",
        "kms:GenerateDataKey*",
        "kms:DescribeKey",
        "kms:CreateGrant"
      ],
      "Resource": "*",
      "Condition": {
         "StringLike": {
           "kms:ViaService" : "cassandra.*.amazonaws.com"
         }
      }
    },
    {
      "Sid":  "Allow administrators to view the customer managed key and revoke grants",
      "Effect": "Allow",
      "Principal": {
        "AWS": "`arn:aws:iam::`111122223333`:role/db-team`"
       },
      "Action": [
        "kms:Describe*",
        "kms:Get*",
        "kms:List*",
        "kms:RevokeGrant"
      ],
      "Resource": "*"
    }
  ]
}
```

#### Using grants to authorize Amazon Keyspaces

In addition to key policies, Amazon Keyspaces uses grants to set permissions on a customer managed key.
To view the grants on a customer managed key in your account, use the [ListGrants](../../../kms/latest/APIReference/API_ListGrants.md "../../../kms/latest/APIReference/API_ListGrants.md") operation. Amazon Keyspaces doesn't need
grants, or any additional permissions, to use the [AWS owned key](encryption.md#keyspaces-owned "encryption.md#keyspaces-owned") to protect your table.

Amazon Keyspaces uses the grant permissions when it performs background system maintenance and
continuous data protection tasks. It also uses grants to generate table keys.

Each grant is specific to a table. If the account includes multiple tables encrypted
under the same customer managed key, there is a grant of each type for each table. The grant is
constrained by the [Amazon Keyspaces encryption
context](../../../kms/latest/developerguide/encryption-context.md "../../../kms/latest/developerguide/encryption-context.md"), which includes the table name and the AWS account ID. The grant
includes permission to [retire the
grant](../../../kms/latest/APIReference/API_RetireGrant.md "../../../kms/latest/APIReference/API_RetireGrant.md") if it's no longer needed.

To create the grants, Amazon Keyspaces must have permission to call `CreateGrant` on
behalf of the user who created the encrypted table.

The key policy can also allow the account to [revoke the grant](../../../kms/latest/APIReference/API_RevokeGrant.md "../../../kms/latest/APIReference/API_RevokeGrant.md") on the customer managed key. However, if
you revoke the grant on an active encrypted table, Amazon Keyspaces will not be able to protect and
maintain the table.

## Step 3: Specify a customer managed key for

a new table

Follow these steps to specify the customer managed key on a new table using the Amazon Keyspaces console or CQL.

### Create an encrypted table using a

customer managed key (console)

1. Sign in to the AWS Management Console, and open the Amazon Keyspaces console at [https://console.aws.amazon.com/keyspaces/home](https://console.aws.amazon.com/keyspaces/home "https://console.aws.amazon.com/keyspaces/home").
2. In the navigation pane, choose **Tables**, and then choose
   **Create table**.
3. On the **Create table** page in the **Table
   details** section, select a keyspace and provide a name for the new
   table.
4. In the **Schema** section, create the schema for your
   table.
5. In the **Table settings** section, choose **Customize
   settings**.
6. Continue to **Encryption settings**.

In this step, you select the encryption settings for the table.

In the **Encryption at rest** section under
**Choose an AWS KMS key**, choose the option **Choose a
different KMS key (advanced)**, and in the search field, choose an
AWS KMS key or enter an Amazon Resource Name (ARN).

###### Note

If the key you selected is not accessible or is missing the required permissions, see [Troubleshooting key
access](../../../kms/latest/developerguide/policy-evaluation.md "../../../kms/latest/developerguide/policy-evaluation.md") in the AWS Key Management Service Developer Guide. 7. Choose **Create** to create the encrypted table.

### Create a new table using a customer managed

key for encryption at rest (CQL)

To create a new table that uses a customer managed key for encryption at rest, you can use the
`CREATE TABLE` statement as shown in the following example. Make sure to
replace the key ARN with an ARN for a valid key with permissions granted to Amazon Keyspaces.

```
CREATE TABLE `my_keyspace.my_table`(id bigint, name text, place text STATIC, PRIMARY KEY(id, name)) WITH CUSTOM_PROPERTIES = {
        'encryption_specification':{
                'encryption_type': 'CUSTOMER_MANAGED_KMS_KEY',
                'kms_key_identifier':'`arn:aws:kms:eu-west-1:5555555555555:key/11111111-1111-111-1111-111111111111`'
            }
    };
```

If you receive an `Invalid Request Exception`, you need to confirm that the customer managed key is valid
and Amazon Keyspaces has the required permissions. To confirm that the key has been configured correctly, see [Troubleshooting key access](../../../kms/latest/developerguide/policy-evaluation.md "../../../kms/latest/developerguide/policy-evaluation.md") in the AWS Key Management Service Developer Guide.

## Step 4: Update the encryption key of an

existing table

You can also use the Amazon Keyspaces console or CQL to change the encryption keys of an
existing table between an AWS owned key and a customer managed KMS key at any
time.

### Update an existing table with

the new customer managed key (console)

1. Sign in to the AWS Management Console, and open the Amazon Keyspaces console at [https://console.aws.amazon.com/keyspaces/home](https://console.aws.amazon.com/keyspaces/home "https://console.aws.amazon.com/keyspaces/home").
2. In the navigation pane, choose
   **Tables**.
3. Choose the table that you want to update, and then choose the
   **Additional settings** tab.
4. In the **Encryption at rest** section, choose **Manage Encryption** to edit the encryption settings for the table.

Under **Choose an AWS KMS key**, choose the option **Choose a
different KMS key (advanced)**, and in the search field, choose an
AWS KMS key or enter an Amazon Resource Name (ARN).

###### Note

If the key you selected is not valid, see [Troubleshooting key access](../../../kms/latest/developerguide/policy-evaluation.md "../../../kms/latest/developerguide/policy-evaluation.md") in the AWS Key Management Service Developer Guide.

Alternatively, you can choose an AWS owned key for a table that is encrypted with a customer managed key. 5. Choose **Save changes** to save your changes to the table.

### Update the encryption key used

for an existing table

To change the encryption key of an existing table, you use the `ALTER
 TABLE` statement to specify a customer managed key for encryption at rest. Make sure to
replace the key ARN with an ARN for a valid key with permissions granted to Amazon Keyspaces.

```
ALTER TABLE `my_keyspace.my_table` WITH CUSTOM_PROPERTIES = {
              'encryption_specification':{
                      'encryption_type': 'CUSTOMER_MANAGED_KMS_KEY',
                      'kms_key_identifier':'`arn:aws:kms:eu-west-1:5555555555555:key/11111111-1111-111-1111-111111111111`'
                  }
         };
```

If you receive an `Invalid Request Exception`, you need to confirm that the customer managed key is valid
and Amazon Keyspaces has the required permissions. To confirm that the key has been configured correctly, see [Troubleshooting key access](../../../kms/latest/developerguide/policy-evaluation.md "../../../kms/latest/developerguide/policy-evaluation.md") in the AWS Key Management Service Developer Guide.

To change the encryption key back to the default encryption at rest option with AWS owned keys, you can use the
`ALTER TABLE` statement as shown in the following example.

```
ALTER TABLE `my_keyspace.my_table` WITH CUSTOM_PROPERTIES = {
                'encryption_specification':{
                      'encryption_type' : 'AWS_OWNED_KMS_KEY'
                    }
         };
```

## Step 5: Use the Amazon Keyspaces encryption context in logs

An [encryption context](../../../kms/latest/developerguide/encrypt_context.md "../../../kms/latest/developerguide/encrypt_context.md") is a set of key–value pairs
that contain arbitrary nonsecret data. When you include an encryption context in a request to
encrypt data, AWS KMS cryptographically binds the encryption context to the encrypted data. To
decrypt the data, you must pass in the same encryption context.

Amazon Keyspaces uses the same encryption context in all AWS KMS cryptographic operations. If you use a
[customer managed key](encryption.md#customer-managed "encryption.md#customer-managed") to protect your Amazon Keyspaces table, you can use
the encryption context to identify the use of the customer managed key in audit records and logs. It
also appears in plaintext in logs, such as in logs for [AWS CloudTrail](../../../awscloudtrail/latest/userguide/cloudtrail-user-guide.md "../../../awscloudtrail/latest/userguide/cloudtrail-user-guide.md") and [Amazon CloudWatch Logs](../../../AmazonCloudWatch/latest/logs/WhatIsCloudWatchLogs.md "../../../AmazonCloudWatch/latest/logs/WhatIsCloudWatchLogs.md").

In its requests to AWS KMS, Amazon Keyspaces uses an encryption context with three key–value
pairs.

```
"encryptionContextSubset": {
    "aws:cassandra:keyspaceName": "my_keyspace",
    "aws:cassandra:tableName": "mytable"
    "aws:cassandra:subscriberId": "`111122223333`"
}
```

- **Keyspace** – The first key–value pair
  identifies the keyspace that includes the table that Amazon Keyspaces is encrypting. The key is
  `aws:cassandra:keyspaceName`. The value is the name of the keyspace.

```
"aws:cassandra:keyspaceName": "`<keyspace-name>`"
```

For example:

```
"aws:cassandra:keyspaceName": "`my_keyspace`"
```

- **Table** – The second key–value pair
  identifies the table that Amazon Keyspaces is encrypting. The key is
  `aws:cassandra:tableName`. The value is the name of the table.

```
"aws:cassandra:tableName": "`<table-name>`"
```

For example:

```
"aws:cassandra:tableName": "`my_table`"
```

- **Account** – The third key–value pair
  identifies the AWS account. The key is `aws:cassandra:subscriberId`. The value
  is the account ID.

```
"aws:cassandra:subscriberId": "`<account-id>`"
```

For example:

```
"aws:cassandra:subscriberId": "`111122223333`"
```

## Step 6: Configure monitoring with AWS CloudTrail

If you use a [customer managed key](encryption.md#customer-managed "encryption.md#customer-managed") to protect your Amazon Keyspaces
tables, you can use AWS CloudTrail logs to track the requests that Amazon Keyspaces sends to AWS KMS on your
behalf.

The `GenerateDataKey`, `DescribeKey`, `Decrypt`, and
`CreateGrant` requests are discussed in this section. In addition, Amazon Keyspaces uses a
[RetireGrant](../../../kms/latest/APIReference/API_RetireGrant.md "../../../kms/latest/APIReference/API_RetireGrant.md") operation to remove a
grant when you delete a table.

###### Note

When you work with Amazon Keyspaces, some operations may generate CloudTrail events with an `invokedBy`
field of `dynamodb.amazonaws.com`.
This is expected and occurs because Amazon Keyspaces integrates with Amazon DynamoDB to provide its service.

**GenerateDataKey**

Amazon Keyspaces creates a unique table key to encrypt data at rest. It
sends a [GenerateDataKey](../../../kms/latest/APIReference/API_GenerateDataKey.md "../../../kms/latest/APIReference/API_GenerateDataKey.md") request to AWS KMS that specifies the KMS key
for the table.

The event that records the `GenerateDataKey` operation is similar to the
following example event. The user is the Amazon Keyspaces service account. The parameters include
the Amazon Resource Name (ARN) of the customer managed key, a key specifier that requires a
256-bit key, and the [encryption context](#encryption-context "#encryption-context") that
identifies the keyspace, the table, and the AWS account.

```
{
    "eventVersion": "1.08",
    "userIdentity": {
        "type": "AWSService",
        "invokedBy": "AWS Internal"
    },
    "eventTime": "2021-04-16T04:56:05Z",
    "eventSource": "kms.amazonaws.com",
    "eventName": "GenerateDataKey",
    "awsRegion": "us-east-1",
    "sourceIPAddress": "AWS Internal",
    "userAgent": "AWS Internal",
    "requestParameters": {
        "keySpec": "AES_256",
        "encryptionContext": {
            "aws:cassandra:keyspaceName": "my_keyspace",
            "aws:cassandra:tableName": "my_table",
            "aws:cassandra:subscriberId": "123SAMPLE012"
        },
        "keyId": "arn:aws:kms:eu-west-1:5555555555555:key/11111111-1111-111-1111-111111111111"
    },
    "responseElements": null,
    "requestID": "5e8e9cb5-9194-4334-aacc-9dd7d50fe246",
    "eventID": "49fccab9-2448-4b97-a89d-7d5c39318d6f",
    "readOnly": true,
    "resources": [
        {
            "accountId": "123SAMPLE012",
            "type": "AWS::KMS::Key",
            "ARN": "arn:aws:kms:eu-west-1:5555555555555:key/11111111-1111-111-1111-111111111111"
        }
    ],
    "eventType": "AwsApiCall",
    "managementEvent": true,
    "eventCategory": "Management",
    "recipientAccountId": "123SAMPLE012",
    "sharedEventID": "84fbaaf0-9641-4e32-9147-57d2cb08792e"
}
```

**DescribeKey**

Amazon Keyspaces uses a [DescribeKey](../../../kms/latest/APIReference/API_DescribeKey.md "../../../kms/latest/APIReference/API_DescribeKey.md")
operation to determine whether the KMS key you selected exists in the account and
Region.

The event that records the `DescribeKey` operation is similar to the
following example event. The user is the Amazon Keyspaces service account. The parameters include
the ARN of the customer managed key and a key specifier that requires a 256-bit key.

```
{
    "eventVersion": "1.08",
    "userIdentity": {
        "type": "IAMUser",
        "principalId": "AIDAZ3FNIIVIZZ6H7CFQG",
        "arn": "arn:aws:iam::123SAMPLE012:user/admin",
        "accountId": "123SAMPLE012",
        "accessKeyId": "AKIAIOSFODNN7EXAMPLE",
        "userName": "admin",
        "sessionContext": {
            "sessionIssuer": {},
            "webIdFederationData": {},
            "attributes": {
                "mfaAuthenticated": "false",
                "creationDate": "2021-04-16T04:55:42Z"
            }
        },
        "invokedBy": "AWS Internal"
    },
    "eventTime": "2021-04-16T04:55:58Z",
    "eventSource": "kms.amazonaws.com",
    "eventName": "DescribeKey",
    "awsRegion": "us-east-1",
    "sourceIPAddress": "AWS Internal",
    "userAgent": "AWS Internal",
    "requestParameters": {
        "keyId": "arn:aws:kms:eu-west-1:5555555555555:key/11111111-1111-111-1111-111111111111"
    },
    "responseElements": null,
    "requestID": "c25a8105-050b-4f52-8358-6e872fb03a6c",
    "eventID": "0d96420e-707e-41b9-9118-56585a669658",
    "readOnly": true,
    "resources": [
        {
            "accountId": "123SAMPLE012",
            "type": "AWS::KMS::Key",
            "ARN": "arn:aws:kms:eu-west-1:5555555555555:key/11111111-1111-111-1111-111111111111"
        }
    ],
    "eventType": "AwsApiCall",
    "managementEvent": true,
    "eventCategory": "Management",
    "recipientAccountId": "123SAMPLE012"
}
```

**Decrypt**

When you access an Amazon Keyspaces table, Amazon Keyspaces needs to decrypt the table key so
that it can decrypt the keys below it in the hierarchy. It then decrypts the data in the
table. To decrypt the table key, Amazon Keyspaces sends a [Decrypt](../../../kms/latest/APIReference/API_Decrypt.md "../../../kms/latest/APIReference/API_Decrypt.md") request to AWS KMS that specifies
the KMS key for the table.

The event that records the `Decrypt` operation is similar to the
following example event. The user is the principal in your AWS account who is
accessing the table. The parameters include the encrypted table key (as a ciphertext
blob) and the [encryption context](#encryption-context "#encryption-context") that
identifies the table and the AWS account. AWS KMS derives the ID of the customer managed key from
the ciphertext.

```
{
    "eventVersion": "1.08",
    "userIdentity": {
        "type": "AWSService",
        "invokedBy": "AWS Internal"
    },
    "eventTime": "2021-04-16T05:29:44Z",
    "eventSource": "kms.amazonaws.com",
    "eventName": "Decrypt",
    "awsRegion": "us-east-1",
    "sourceIPAddress": "AWS Internal",
    "userAgent": "AWS Internal",
    "requestParameters": {
        "encryptionContext": {
            "aws:cassandra:keyspaceName": "my_keyspace",
            "aws:cassandra:tableName": "my_table",
            "aws:cassandra:subscriberId": "123SAMPLE012"
        },
        "encryptionAlgorithm": "SYMMETRIC_DEFAULT"
    },
    "responseElements": null,
    "requestID": "50e80373-83c9-4034-8226-5439e1c9b259",
    "eventID": "8db9788f-04a5-4ae2-90c9-15c79c411b6b",
    "readOnly": true,
    "resources": [
        {
            "accountId": "123SAMPLE012",
            "type": "AWS::KMS::Key",
            "ARN": "arn:aws:kms:eu-west-1:5555555555555:key/11111111-1111-111-1111-111111111111"
        }
    ],
    "eventType": "AwsApiCall",
    "managementEvent": true,
    "eventCategory": "Management",
    "recipientAccountId": "123SAMPLE012",
    "sharedEventID": "7ed99e2d-910a-4708-a4e3-0180d8dbb68e"
}
```

**CreateGrant**

When you use a [customer managed key](encryption.md#customer-managed "encryption.md#customer-managed") to protect your
Amazon Keyspaces table, Amazon Keyspaces uses [grants](#encryption-grants "#encryption-grants") to allow the
service to perform continuous data protection and maintenance and durability tasks.
These grants aren't required on [AWS owned keys](encryption.md#keyspaces-owned "encryption.md#keyspaces-owned").

The grants that Amazon Keyspaces creates are specific to a table. The principal in the [CreateGrant](../../../kms/latest/APIReference/API_CreateGrant.md "../../../kms/latest/APIReference/API_CreateGrant.md") request is the user who
created the table.

The event that records the `CreateGrant` operation is similar to the
following example event. The parameters include the ARN of the customer managed key for the table,
the grantee principal and retiring principal (the Amazon Keyspaces service), and the operations
that the grant covers. It also includes a constraint that requires all encryption
operations use the specified [encryption
context](#encryption-context "#encryption-context").

```
{
    "eventVersion": "1.08",
    "userIdentity": {
        "type": "IAMUser",
        "principalId": "AIDAZ3FNIIVIZZ6H7CFQG",
        "arn": "arn:aws:iam::arn:aws:kms:eu-west-1:5555555555555:key/11111111-1111-111-1111-111111111111:user/admin",
        "accountId": "arn:aws:kms:eu-west-1:5555555555555:key/11111111-1111-111-1111-111111111111",
        "accessKeyId": "AKIAI44QH8DHBEXAMPLE",
        "userName": "admin",
        "sessionContext": {
            "sessionIssuer": {},
            "webIdFederationData": {},
            "attributes": {
                "mfaAuthenticated": "false",
                "creationDate": "2021-04-16T04:55:42Z"
            }
        },
        "invokedBy": "AWS Internal"
    },
    "eventTime": "2021-04-16T05:11:10Z",
    "eventSource": "kms.amazonaws.com",
    "eventName": "CreateGrant",
    "awsRegion": "us-east-1",
    "sourceIPAddress": "AWS Internal",
    "userAgent": "AWS Internal",
    "requestParameters": {
        "keyId": "a7d328af-215e-4661-9a69-88c858909f20",
        "operations": [
            "DescribeKey",
            "GenerateDataKey",
            "Decrypt",
            "Encrypt",
            "ReEncryptFrom",
            "ReEncryptTo",
            "RetireGrant"
        ],
        "constraints": {
            "encryptionContextSubset": {
                "aws:cassandra:keyspaceName": "my_keyspace",
                "aws:cassandra:tableName": "my_table",
                "aws:cassandra:subscriberId": "123SAMPLE012"
            }
        },
        "retiringPrincipal": "cassandratest.us-east-1.amazonaws.com",
        "granteePrincipal": "cassandratest.us-east-1.amazonaws.com"
    },
    "responseElements": {
        "grantId": "18e4235f1b07f289762a31a1886cb5efd225f069280d4f76cd83b9b9b5501013"
    },
    "requestID": "b379a767-1f9b-48c3-b731-fb23e865e7f7",
    "eventID": "29ee1fd4-28f2-416f-a419-551910d20291",
    "readOnly": false,
    "resources": [
        {
            "accountId": "123SAMPLE012",
            "type": "AWS::KMS::Key",
            "ARN": "arn:aws:kms:eu-west-1:5555555555555:key/11111111-1111-111-1111-111111111111"
        }
    ],
    "eventType": "AwsApiCall",
    "managementEvent": true,
    "eventCategory": "Management",
    "recipientAccountId": "123SAMPLE012"
}
```
