# LogsEncryptionConfiguration

Configuration for encrypting centralized log groups. This configuration is only applied to
destination log groups for which the corresponding source log groups are encrypted using
Customer Managed KMS Keys.

## Contents

**EncryptionStrategy**

Configuration that determines the encryption strategy of the destination log groups.
CUSTOMER_MANAGED uses the configured KmsKeyArn to encrypt newly created destination log
groups.

Type: String

Valid Values: `CUSTOMER_MANAGED | AWS_OWNED`

Required: Yes

**EncryptionConflictResolutionStrategy**

Conflict resolution strategy for centralization if the encryption strategy is set to
CUSTOMER_MANAGED and the destination log group is encrypted with an AWS_OWNED KMS Key. ALLOW
lets centralization go through while SKIP prevents centralization into the destination log
group.

Type: String

Valid Values: `ALLOW | SKIP`

Required: No

**KmsKeyArn**

KMS Key ARN belonging to the primary destination account and region, to encrypt newly
created central log groups in the primary destination.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 1011.

Pattern: `arn:aws([a-z0-9\-]+)?:([a-zA-Z0-9\-]+):([a-z0-9\-]+)?:([0-9]{12})?:(.+)`

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/observabilityadmin-2018-05-10/LogsEncryptionConfiguration.md "../../../goto/SdkForCpp/observabilityadmin-2018-05-10/LogsEncryptionConfiguration.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/observabilityadmin-2018-05-10/LogsEncryptionConfiguration.md "../../../goto/SdkForJavaV2/observabilityadmin-2018-05-10/LogsEncryptionConfiguration.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/observabilityadmin-2018-05-10/LogsEncryptionConfiguration.md "../../../goto/SdkForRubyV3/observabilityadmin-2018-05-10/LogsEncryptionConfiguration.md")
