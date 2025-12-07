Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Using AWS KMS with the Amazon Redshift Data API

When you encrypt your Amazon Redshift cluster or Redshift Serverless workgroup with a customer managed key, the
Amazon Redshift Data API uses that same customer managed key to store and encrypt your queries and
results.

The Data API encrypts your data by default to protect sensitive information, such
as query text and query results. It uses AWS KMS encryption keys owned by AWS for this
protection.

Default encryption for data at rest reduces operational overhead and complexity when
you protect sensitive data. This approach helps you build secure applications that meet
strict encryption compliance and regulatory requirements.

## Using grants in AWS KMS

The Data API requires a grant to use your customer managed key.

When you call `ExecuteStatement` or `BatchExecuteStatement`
against a cluster encrypted with a customer managed key, Amazon Redshift creates a grant on
your behalf by sending a [`CreateGrant`](../../../kms/latest/APIReference/API_CreateGrant.md "../../../kms/latest/APIReference/API_CreateGrant.md") request to AWS KMS. AWS KMS uses grants to give
the Data API access to a KMS key in your account.

The Data API requires the grant to use your customer managed key for the following
operations:

- Send [`Encrypt`](../../../kms/latest/APIReference/API_Encrypt.md "../../../kms/latest/APIReference/API_Encrypt.md") requests to AWS KMS to encrypt query
  metadata with your customer managed key.
- Send [`GenerateDataKey`](../../../kms/latest/APIReference/API_GenerateDataKey.md "../../../kms/latest/APIReference/API_GenerateDataKey.md") requests to AWS KMS to generate
  data keys encrypted by your customer managed key.
- Send [`Decrypt`](../../../kms/latest/APIReference/API_Decrypt.md "../../../kms/latest/APIReference/API_Decrypt.md") requests to AWS KMS to decrypt the encrypted
  data keys so they can encrypt your data.

You can revoke access to the grant or remove Amazon Redshift access to your customer managed key at any
time. If you do, the Data API can no longer access data encrypted by your
customer managed key, which affects operations that depend on that data. For example, if you
try to retrieve query results or track query status after revoking the grant, the
Data API returns an `AccessDeniedException`.

## Key policies for your customer managed key

Key policies control access to your customer managed key. Every customer managed key must have exactly
one key policy, which contains statements that determine who can use the key and how
they can use it. When you create your customer managed key, you can specify a key policy. For
more information, see [Customer managed keys](../../../kms/latest/developerguide/concepts.md#customer-mgn-key "../../../kms/latest/developerguide/concepts.md#customer-mgn-key") in the _AWS Key Management Service Developer
Guide_.

To use your customer managed keys with the Data API, you must first allow access to
Amazon Redshift. The following API operations must be permitted in the key policy:

- `kms:CreateGrant` – Adds a grant to a customer managed
  key. Grants control access to a specified AWS KMS key, which allows access to
  grant operations that Amazon Redshift requires. For more information, see [Using
  grants in AWS KMS](../../../kms/latest/developerguide/grants.md#terms-grant-operations "../../../kms/latest/developerguide/grants.md#terms-grant-operations").

The following is an example key policy:

```
"Statement":[
   {
      "Sid":"Allow access to principals authorized to use Amazon Redshift",
      "Effect":"Allow",
      "Principal":{
         "AWS":"*"
      },
      "Action":[
         "kms:DescribeKey",
         "kms:CreateGrant"
      ],
      "Resource":"*",
      "Condition":{
         "StringEquals":{
            "kms:ViaService":"redshift.amazonaws.com",
            "kms:CallerAccount":"111122223333"
         }
      }
   },
   {
      "Sid":"AllowKeyAdministratorsAccess",
      "Effect":"Allow",
      "Principal":{
         "AWS":"arn:aws:iam::111122223333:role/ExampleAdminRole"
      },
      "Action":"kms:*",
      "Resource":"*"
   },
   {
      "Sid":"AllowKeyUseForExampleRole",
      "Effect":"Allow",
      "Principal":{
         "AWS":"arn:aws:iam::111122223333:role/ExampleUserRole"
      },
      "Action":[
         "kms:Encrypt",
         "kms:Decrypt",
         "kms:ReEncrypt*",
         "kms:GenerateDataKey*",
         "kms:DescribeKey"
      ],
      "Resource":"*"
   }
]
```

## Data API encryption context

An encryption context is an optional set of key-value pairs that contains
additional contextual information about the data. AWS KMS uses the encryption context
as additional authenticated data to support authenticated encryption. When you
include an encryption context in a request to encrypt data, AWS KMS binds the
encryption context to the encrypted data. To decrypt the data, you must include the
same encryption context in the request.

The Data API uses the same three encryption context key-value pairs in all
AWS KMS cryptographic operations for provisioned clusters:

- `aws:redshift:arn` – The cluster's Amazon Resource Name
  (ARN)
- `aws:redshift:createtime` – The timestamp when you requested
  cluster creation
- `serviceName` – `RedshiftDataAPI`

```
"EncryptionContextSubset": {
    "aws:redshift:arn": "arn:aws:redshift:us-east-1:123456789012:cluster:redshift-cluster",
    "aws:redshift:createtime": "20250815T0000Z",
    "serviceName": "RedshiftDataAPI",
}
```

The Data API uses two encryption context key-value pairs in all AWS KMS
cryptographic operations for serverless workgroups:

- `aws:redshift-serverless:arn` – The namespace's Amazon Resource
  Name (ARN)
- `serviceName` – RedshiftDataAPI

```
"EncryptionContextSubset": {
    "aws:redshift-serverless:arn": "arn:aws:redshift-serverless:us-east-1:123456789012:namespace:12345678-1234-1234-1234-123456789012",
    "serviceName": "RedshiftDataAPI"
}
```

For more information about encryption, see [Introduction to the
cryptographic details of AWS KMS](../../../kms/latest/cryptographic-details/intro.md "../../../kms/latest/cryptographic-details/intro.md"). For more information about the Amazon Redshift and
AWS KMS integration, see [How Amazon Redshift uses
AWS KMS](../../../kms/latest/developerguide/services-redshift.md "../../../kms/latest/developerguide/services-redshift.md").
