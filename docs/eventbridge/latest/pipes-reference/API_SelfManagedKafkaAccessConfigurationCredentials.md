# SelfManagedKafkaAccessConfigurationCredentials

The AWS Secrets Manager secret that stores your stream credentials.

## Contents

###### Important

This data type is a UNION, so only one of the following members can be specified when used or returned.

**BasicAuth**

The ARN of the Secrets Manager secret.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 1600.

Pattern: `(^arn:aws([a-z]|\-)*:secretsmanager:([a-z]{2,4}((-gov)|(-de)|(-iso([a-z]?)))?-[a-z]+(-\d{1})?):(\d{12}):secret:.+)`

Required: No

**ClientCertificateTlsAuth**

The ARN of the Secrets Manager secret.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 1600.

Pattern: `(^arn:aws([a-z]|\-)*:secretsmanager:([a-z]{2,4}((-gov)|(-de)|(-iso([a-z]?)))?-[a-z]+(-\d{1})?):(\d{12}):secret:.+)`

Required: No

**SaslScram256Auth**

The ARN of the Secrets Manager secret.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 1600.

Pattern: `(^arn:aws([a-z]|\-)*:secretsmanager:([a-z]{2,4}((-gov)|(-de)|(-iso([a-z]?)))?-[a-z]+(-\d{1})?):(\d{12}):secret:.+)`

Required: No

**SaslScram512Auth**

The ARN of the Secrets Manager secret.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 1600.

Pattern: `(^arn:aws([a-z]|\-)*:secretsmanager:([a-z]{2,4}((-gov)|(-de)|(-iso([a-z]?)))?-[a-z]+(-\d{1})?):(\d{12}):secret:.+)`

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/pipes-2015-10-07/SelfManagedKafkaAccessConfigurationCredentials.md "../../../goto/SdkForCpp/pipes-2015-10-07/SelfManagedKafkaAccessConfigurationCredentials.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/pipes-2015-10-07/SelfManagedKafkaAccessConfigurationCredentials.md "../../../goto/SdkForJavaV2/pipes-2015-10-07/SelfManagedKafkaAccessConfigurationCredentials.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/pipes-2015-10-07/SelfManagedKafkaAccessConfigurationCredentials.md "../../../goto/SdkForRubyV3/pipes-2015-10-07/SelfManagedKafkaAccessConfigurationCredentials.md")
