# Encryption

Defines the encryption configuration for S3 Table integrations, including the encryption
algorithm and KMS key settings.

## Contents

**SseAlgorithm**

The server-side encryption algorithm used for encrypting data in the S3 Table
integration.

Type: String

Valid Values: `aws:kms | AES256`

Required: Yes

**KmsKeyArn**

The Amazon Resource Name (ARN) of the KMS key used for encryption when using
customer-managed keys.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 1011.

Pattern: `arn:aws([a-z0-9\-]+)?:([a-zA-Z0-9\-]+):([a-z0-9\-]+)?:([0-9]{12})?:(.+)`

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/observabilityadmin-2018-05-10/Encryption.md "../../../goto/SdkForCpp/observabilityadmin-2018-05-10/Encryption.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/observabilityadmin-2018-05-10/Encryption.md "../../../goto/SdkForJavaV2/observabilityadmin-2018-05-10/Encryption.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/observabilityadmin-2018-05-10/Encryption.md "../../../goto/SdkForRubyV3/observabilityadmin-2018-05-10/Encryption.md")
