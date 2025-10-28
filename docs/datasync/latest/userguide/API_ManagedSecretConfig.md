# ManagedSecretConfig

Specifies configuration information for a DataSync-managed secret, such as an
authentication token or set of credentials that DataSync uses to access a specific
transfer location. DataSync uses the default AWS-managed KMS key to encrypt this secret in AWS Secrets Manager.

## Contents

**SecretArn**

Specifies the ARN for an AWS Secrets Manager secret.

Type: String

Length Constraints: Maximum length of 2048.

Pattern: `^(arn:(aws|aws-cn|aws-us-gov|aws-iso|aws-iso-b):secretsmanager:[a-z\-0-9]+:[0-9]{12}:secret:.*|)$`

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/datasync-2018-11-09/ManagedSecretConfig.md "../../../goto/SdkForCpp/datasync-2018-11-09/ManagedSecretConfig.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/datasync-2018-11-09/ManagedSecretConfig.md "../../../goto/SdkForJavaV2/datasync-2018-11-09/ManagedSecretConfig.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/datasync-2018-11-09/ManagedSecretConfig.md "../../../goto/SdkForRubyV3/datasync-2018-11-09/ManagedSecretConfig.md")
