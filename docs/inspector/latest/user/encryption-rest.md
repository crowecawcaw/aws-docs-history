# Encryption at rest

By default, Amazon Inspector stores data at rest using AWS encryption solutions.
Amazon Inspector encrypts data, such as the following:

- Resource inventory collected with AWS Systems Manager.
- Resource inventory parsed from Amazon Elastic Container Registry images
- Generated security findings using AWS owned encryption keys from AWS Key Management Service

You cannot manage, use, or view AWS owned keys.
However, you don't need to take action or change programs to protect keys that encrypt your data.
For more information, see [AWS owned keys](../../../kms/latest/developerguide/concepts.md#kms_keys "../../../kms/latest/developerguide/concepts.md#kms_keys").

If you disable Amazon Inspector, it permanently deletes all resources it stores or maintains for you, such as collected inventory and security findings.

## Encryption at rest for code in your findings

For Amazon Inspector Lambda code scanning, Amazon Inspector partners with Amazon Q to scan your code for vulnerabilities.
When a vulnerability is detected, Amazon Q extracts a snippet of your code containing the vulnerability and stores that code until Amazon Inspector requests access.
By default, Amazon Q uses an AWS owned key to encrypt the extracted code.
However, you can configure Amazon Inspector to use your own customer-managed AWS KMS key for encryption.

The following workflow explains how Amazon Inspector uses the key you configure to encrypt your code:

1. You supply an AWS KMS key to Amazon Inspector using the Amazon Inspector [UpdateEncryptionKey](../../v2/APIReference/API_UpdateEncryptionKey.md "../../v2/APIReference/API_UpdateEncryptionKey.md") API.
2. Amazon Inspector forwards the information about your AWS KMS key to Amazon Q, and Amazon Q stores the information for future use.
3. Amazon Q uses the KMS key you configured in Amazon Inspector through the key policy.
4. Amazon Q creates an encrypted data key from your AWS KMS key and stores it.
   This data key is used to encrypt your code data stored by Amazon Q.
5. When Amazon Inspector requests data from code scans, Amazon Q uses the KMS key to decrypt the data key.
   When you disable Lambda Code Scanning, Amazon Q deletes the associated data key.

## Permissions for code encryption with a customer managed key

For encryption, you must create a KMS key with [a policy](../../../kms/latest/developerguide/key-policy-overview.md "../../../kms/latest/developerguide/key-policy-overview.md") that includes a statement allowing Amazon Inspector and Amazon Q to perform the following actions.

- `kms:Decrypt`
- `kms:DescribeKey`
- `kms:Encrypt`
- `kms:GenerateDataKey`
- `kms:GenerateDataKeyWithoutPlainText`

###### Policy statement

You can use the following policy statement when creating the KMS key.

###### Note

Replace `account-id` with your 12-digit AWS account ID.
Replace `Region` with the AWS Region where you enabled Amazon Inspector and Lambda code scanning.
Replace `role-ARN` with the Amazon Resource Name for your IAM role.

```

{
  "Effect": "Allow",
  "Principal": {
    "Service": "q.amazonaws.com"
  },
  "Action": [
    "kms:Encrypt",
    "kms:Decrypt",
    "kms:GenerateDataKeyWithoutPlaintext",
    "kms:GenerateDataKey"
  ],
  "Resource": "*",
  "Condition": {
    "StringLike": {
      "kms:EncryptionContext:aws:qdeveloper:lambda-codescan-scope": "`account-id`"
    },
    "StringEquals": {
      "aws:SourceAccount": "`account-id`"
    },
    "ArnLike": {
      "aws:SourceArn": "arn:aws:qdeveloper:`Region`:`account-id`:scans/*"
    }
  }
},
{
  "Effect": "Allow",
  "Principal": {
    "Service": "q.amazonaws.com"
  },
  "Action": "kms:DescribeKey",
  "Resource": "*",
  "Condition": {
    "StringEquals": {
      "aws:SourceAccount": "`account-id`"
    },
    "ArnLike": {
      "aws:SourceArn": "arn:aws:qdeveloper:`Region`:`account-id`:scans/*"
    }
  }
},
{
  "Effect": "Allow",
  "Action": [
    "kms:Encrypt",
    "kms:Decrypt",
    "kms:GenerateDataKeyWithoutPlaintext",
    "kms:GenerateDataKey"
  ],
  "Principal": {
    "AWS": "`role-ARN`"
  },
  "Resource": "*",
  "Condition": {
    "StringEquals": {
      "kms:ViaService": "inspector2.`Region`.amazonaws.com"
    },
    "StringLike": {
      "kms:EncryptionContext:aws:qdeveloper:lambda-codescan-scope": "`account-id`"
    }
  }
},
{
  "Effect": "Allow",
  "Action": [
    "kms:DescribeKey"
  ],
  "Principal": {
    "AWS": "`role-ARN`"
  },
  "Resource": "*",
  "Condition": {
    "StringEquals": {
      "kms:ViaService": "inspector2.`Region`.amazonaws.com"
    }
  }
}
```

The policy statement is formatted in JSON.
After you include the statement, review the policy to make sure the syntax is valid.
If the statement is the last statement in the policy, place a comma after the closing brace for the previous statement.
If the statement is the first statement or between two existing statements in the policy, place a comma after the closing brace for the statement.

###### Note

Amazon Inspector no longer supports [grants](../../../kms/latest/developerguide/grants.md "../../../kms/latest/developerguide/grants.md") to encrypt code snippets extracted from packages.
If you are using a grant-based policy, you can still access your findings.
However, if you ever update or reset your KMS key or disable Lambda Code Scanning, you will need to use the KMS key policy described in this section.

If you set, update, or reset the encryption key for your account, you must use an Amazon Inspector administrator policy, such as the AWS managed policy `AmazonInspector2FullAccess`.

## Configuring encryption with a customer managed key

To configure encryption for your account using a customer managed key you must be an Amazon Inspector
administrator with the permissions outlined in [Permissions for code encryption with a customer managed key](#cmk-permissions "#cmk-permissions"). Additionally you will need a AWS KMS key in the same
AWS Region as your findings, or a [multi-region key](../../../kms/latest/developerguide/multi-region-keys-overview.md "../../../kms/latest/developerguide/multi-region-keys-overview.md"). You can use an existing symmetric key in your account or create
a symmetric customer managed key by using the AWS Management Console, or the AWS KMS
APIs. For more information see [Creating symmetric
encryption AWS KMS keys](../../../kms/latest/developerguide/create-keys.md#create-symmetric-cmk "../../../kms/latest/developerguide/create-keys.md#create-symmetric-cmk") in the AWS KMS user guide.

###### Note

Effective June 13th, 2025, the service principal in AWS KMS requests logged in CloudTrail during code snippet encryption/decryption is changing from "codeguru-reviewer" to "q".

### Using the Amazon Inspector API to configure encryption

To set a key for encryption the [UpdateEncryptionKey](../../v2/APIReference/API_UpdateEncryptionKey.md "../../v2/APIReference/API_UpdateEncryptionKey.md") operation of the Amazon Inspector API while signed in as an Amazon Inspector administrator. In the API request, use the `kmsKeyId` field to specify the ARN of the AWS KMS key you want to use. For `scanType` enter `CODE` and for `resourceType` enter `AWS_LAMBDA_FUNCTION`.

You can use [UpdateEncryptionKey](../../v2/APIReference/API_GetEncryptionKey.md "../../v2/APIReference/API_GetEncryptionKey.md") API to check view which AWS KMS key Amazon Inspector is using for encryption.

###### Note

If you attempt to use `GetEncryptionKey` when you haven't set a customer managed key the operation returns a `ResourceNotFoundException` error which means that an AWS owned key is being used for encryption.

If you delete the key or change it's policy to deny access to Amazon Inspector or Amazon Q you will be unable to access your code vulnerability findings and Lambda code scanning will fail for your account.

You can use `ResetEncryptionKey` to resume using an AWS owned key to encrypt code extracted as part of your Amazon Inspector findings.
