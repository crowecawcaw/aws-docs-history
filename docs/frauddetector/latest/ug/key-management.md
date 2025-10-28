Amazon Fraud Detector will no longer be open to new customers starting November 7, 2025. If you would like to use Amazon Fraud Detector,
sign up prior to that date. For capabilities similar to Amazon Fraud Detector, explore Amazon SageMaker, AutoGluon, and AWS WAF.

# Key management

Amazon Fraud Detector encrypts your data using one of two types of keys:

- An AWS owned [KMS key](../../../kms/latest/developerguide/concepts.md#master_keys "../../../kms/latest/developerguide/concepts.md#master_keys"). This is the default.
- A customer managed [KMS key](../../../kms/latest/developerguide/concepts.md#master_keys "../../../kms/latest/developerguide/concepts.md#master_keys").

## Creating customer managed KMS key

You can create customer managed KMS key using either the AWS KMS console or the [CreateKey](../../../kms/latest/APIReference/API_CreateKey.md "../../../kms/latest/APIReference/API_CreateKey.md") API.
When creating the key make sure you,

- Select a symmetric encryption customer managed KMS key, Amazon Fraud Detector does not support asymmetric KMS keys. For more information, see [Asymmetric Keys in AWS KMS](../../../kms/latest/developerguide/symmetric-asymmetric.md "../../../kms/latest/developerguide/symmetric-asymmetric.md") in the AWS Key Management Service Developer Guide.
- Create single region KMS key. Amazon Fraud Detector does not support multi-region KMS keys. For more information, see [Multi-region keys in AWS KMS](../../../kms/latest/developerguide/multi-region-keys-overview.md "../../../kms/latest/developerguide/multi-region-keys-overview.md") in the AWS Key Management Service Developer Guide.
- Provide the following [key policy](../../../kms/latest/developerguide/concepts.md#key_permissions "../../../kms/latest/developerguide/concepts.md#key_permissions") to grant permissions to Amazon Fraud Detector to use the key.

```

        {
    "Effect": "Allow",
    "Principal": {
        "Service": "frauddetector.amazonaws.com"
    },
    "Action": [
        "kms:Encrypt",
        "kms:Decrypt",
        "kms:ReEncrypt*",
        "kms:GenerateDataKey*",
        "kms:DescribeKey",
        "kms:CreateGrant",
        "kms:RetireGrant"
    ],
    "Resource": "*"
}

```

For information on key policies, see [Using Key Policies in AWS KMS](../../../kms/latest/developerguide/key-policies.md "../../../kms/latest/developerguide/key-policies.md") in the AWS Key Management Service Developer Guide.

## Encrypting data using customer managed KMS key

Use Amazon Fraud Detector’s [PutKMSEncryptionKey](../api/API_PutKMSEncryptionKey.md "../api/API_PutKMSEncryptionKey.md") API to encrypt your Amazon Fraud Detector data at rest using the customer managed KMS key. You can change the encryption configuration at any time using `PutKMSEncryptionKey` API.

**Important notes about encrypted data**

- Data generated after setting up the customer managed KMS key is encrypted. Data generated before setting up the customer managed KMS key will remain unencrypted.
- If customer managed KMS key is changed, the data that was encrypted using the previous encryption configuration will not be re-encrypted.

## View data

When you use customer managed KMS key to encrypt your Amazon Fraud Detector data, the data encrypted using this method is not searchable using filters in the **Search Past Predictions** area of the Amazon Fraud Detector console.
To ensure complete search results, use one or more of the following properties to filter results:

- Event ID
- Evaluation timestamp
- Detector status
- Detector version
- Model version
- Model type
- Rule evaluation status
- Rule execution mode
- Rule match status
- Rule version
- Variable data source

If customer managed KMS key was either deleted or is scheduled for deletion, your data might not be available. For more information, see [Deleting KMS key](../../../kms/latest/developerguide/deleting-keys.md "../../../kms/latest/developerguide/deleting-keys.md").
