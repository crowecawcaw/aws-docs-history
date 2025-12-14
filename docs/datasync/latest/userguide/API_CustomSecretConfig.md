# CustomSecretConfig

Specifies configuration information for a customer-managed Secrets Manager secret where
a storage location credentials is stored in Secrets Manager as plain text (for authentication
token, secret key, or password) or as binary (for Kerberos keytab). This configuration includes
the secret ARN, and the ARN for an IAM role that provides access to the secret.

###### Note

You can use either `CmkSecretConfig` or `CustomSecretConfig` to
provide credentials for a `CreateLocation` request. Do not provide both
parameters for the same request.

## Contents

**SecretAccessRoleArn**

Specifies the ARN for the AWS Identity and Access Management role that DataSync uses to
access the secret specified for `SecretArn`.

Type: String

Length Constraints: Maximum length of 2048.

Pattern: `^(arn:(aws|aws-cn|aws-us-gov|aws-eusc|aws-iso|aws-iso-b):iam::[0-9]{12}:role/[a-zA-Z0-9+=,.@_-]+|)$`

Required: No

**SecretArn**

Specifies the ARN for an AWS Secrets Manager secret.

Type: String

Length Constraints: Maximum length of 2048.

Pattern: `^(arn:(aws|aws-cn|aws-us-gov|aws-eusc|aws-iso|aws-iso-b):secretsmanager:[a-z\-0-9]+:[0-9]{12}:secret:.*|)$`

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/datasync-2018-11-09/CustomSecretConfig.md "../../../goto/SdkForCpp/datasync-2018-11-09/CustomSecretConfig.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/datasync-2018-11-09/CustomSecretConfig.md "../../../goto/SdkForJavaV2/datasync-2018-11-09/CustomSecretConfig.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/datasync-2018-11-09/CustomSecretConfig.md "../../../goto/SdkForRubyV3/datasync-2018-11-09/CustomSecretConfig.md")
