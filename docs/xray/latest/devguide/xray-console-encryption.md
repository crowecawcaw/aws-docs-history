# Data protection in AWS X-Ray

AWS X-Ray always encrypts traces and related data at rest. When you need to audit and disable encryption keys
for compliance or internal requirements, you can configure X-Ray to use an AWS Key Management Service (AWS KMS) key to encrypt
data.

X-Ray provides an AWS managed key named `aws/xray`. Use this key when you just want to [audit key usage in AWS CloudTrail](../../../kms/latest/developerguide/logging-using-cloudtrail.md "../../../kms/latest/developerguide/logging-using-cloudtrail.md") and don't need to manage the key itself. When you need to manage access to the key or configure key rotation, you can [create a customer managed key](../../../kms/latest/developerguide/create-keys.md "../../../kms/latest/developerguide/create-keys.md").

When you change encryption settings, X-Ray spends some time generating and propagating data keys. While the new
key is being processed, X-Ray may encrypt data with a combination of the new and old settings. Existing data is not
re-encrypted when you change encryption settings.

###### Note

AWS KMS charges when X-Ray uses a KMS key to encrypt or decrypt trace data.

- **Default encryption** – Free.
- **AWS managed key** – Pay for key use.
- **customer managed key** – Pay for key storage and use.
  See [AWS Key Management Service Pricing](https://aws.amazon.com/kms/pricing/ "https://aws.amazon.com/kms/pricing/") for details.

###### Note

X-Ray insights notifications sends events to Amazon EventBridge, which does not currently support customer managed keys. For more information, see [Data Protection in Amazon EventBridge](../../../eventbridge/latest/userguide/data-protection.md "../../../eventbridge/latest/userguide/data-protection.md").

You must have user-level access to a customer managed key to configure X-Ray to use it, and to then view
encrypted traces. See [User permissions for encryption](security_iam_service-with-iam.md#xray-permissions-encryption "security_iam_service-with-iam.md#xray-permissions-encryption") for
more information.

CloudWatch console

###### To configure X-Ray to use a KMS key for encryption using the CloudWatch console

1. Sign in to the AWS Management Console and open the CloudWatch console at
   [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
2. Choose **Settings** in the left navigation pane.
3. Choose **View settings** under **Encryption** within the **X-Ray traces** section.
4. Choose **Edit** in the **Encryption configuration** section.
5. Choose **Use a KMS key**.
6. Choose a key from the dropdown menu:
   - **aws/xray** – Use the AWS managed key.
   - _key alias_ – Use a customer managed key in your account.
   - **Manually enter a key ARN** – Use a customer managed key in a different
     account. Enter the full Amazon Resource Name (ARN) of the key in the field that appears.

7. Choose **Update encryption**.

X-Ray console

###### To configure X-Ray to use a KMS key for encryption using the X-Ray console

1. Open the [X-Ray console](https://console.aws.amazon.com/xray/home# "https://console.aws.amazon.com/xray/home#").
2. Choose **Encryption**.
3. Choose **Use a KMS key**.
4. Choose a key from the dropdown menu:
   - **aws/xray** – Use the AWS managed key.
   - _key alias_ – Use a customer managed key in your account.
   - **Manually enter a key ARN** – Use a customer managed key in a different
     account. Enter the full Amazon Resource Name (ARN) of the key in the field that appears.

5. Choose **Apply**.

###### Note

X-Ray does not support asymmetric KMS keys.

If X-Ray is unable to access your encryption key, it stops storing data. This can happen if your user loses
access to the KMS key, or if you disable a key that's currently in use. When this happens, X-Ray shows a notification
in the navigation bar.

To configure encryption settings with the X-Ray API, see [Configuring sampling, groups, and encryption settings with the
AWS X-Ray API](xray-api-configuration.md "xray-api-configuration.md").
