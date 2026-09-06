

Amazon Fraud Detector is no longer open to new customers as of November 7, 2025. For capabilities similar to Amazon Fraud Detector, explore Amazon SageMaker, AutoGluon, and AWS WAF.

# Key management
<a name="key-management"></a>

Amazon Fraud Detector encrypts your data using one of two types of keys:
+ An AWS owned [KMS key](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#master_keys). This is the default.
+ A customer managed [KMS key](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#master_keys). 

## Creating customer managed KMS key
<a name="create-customer-managed-cmk"></a>

You can create customer managed KMS key using either the AWS KMS console or the [CreateKey](https://docs.aws.amazon.com/kms/latest/APIReference/API_CreateKey.html) API. When creating the key make sure you, 
+ Select a symmetric encryption customer managed KMS key, Amazon Fraud Detector does not support asymmetric KMS keys. For more information, see [Asymmetric Keys in AWS KMS](https://docs.aws.amazon.com/kms/latest/developerguide/symmetric-asymmetric.html) in the AWS Key Management Service Developer Guide.
+ Create single region KMS key. Amazon Fraud Detector does not support multi-region KMS keys. For more information, see [Multi-region keys in AWS KMS](https://docs.aws.amazon.com/kms/latest/developerguide/multi-region-keys-overview.html) in the AWS Key Management Service Developer Guide.
+ Provide the following [key policy](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#key_permissions) to grant permissions to Amazon Fraud Detector to use the key. 

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

  For information on key policies, see [Using Key Policies in AWS KMS](https://docs.aws.amazon.com/kms/latest/developerguide/key-policies.html) in the AWS Key Management Service Developer Guide.

## Encrypting data using customer managed KMS key
<a name="encrypt-data-using-CMK"></a>

Use Amazon Fraud Detector’s [PutKMSEncryptionKey](https://docs.aws.amazon.com/frauddetector/latest/api/API_PutKMSEncryptionKey.html) API to encrypt your Amazon Fraud Detector data at rest using the customer managed KMS key. You can change the encryption configuration at any time using `PutKMSEncryptionKey` API. 

**Important notes about encrypted data**
+ Data generated after setting up the customer managed KMS key is encrypted. Data generated before setting up the customer managed KMS key will remain unencrypted.
+ If customer managed KMS key is changed, the data that was encrypted using the previous encryption configuration will not be re-encrypted.

## View data
<a name="view-encrypted-data"></a>

When you use customer managed KMS key to encrypt your Amazon Fraud Detector data, the data encrypted using this method is not searchable using filters in the ** Search Past Predictions** area of the Amazon Fraud Detector console. To ensure complete search results, use one or more of the following properties to filter results:
+ Event ID
+ Evaluation timestamp
+ Detector status
+ Detector version
+ Model version
+ Model type
+ Rule evaluation status
+ Rule execution mode
+ Rule match status
+ Rule version
+ Variable data source

If customer managed KMS key was either deleted or is scheduled for deletion, your data might not be available. For more information, see [Deleting KMS key](https://docs.aws.amazon.com/kms/latest/developerguide/deleting-keys.html). 