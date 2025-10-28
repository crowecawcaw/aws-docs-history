# CentralizationRuleSummary

A summary of a centralization rule's key properties and status.

## Contents

**CreatedRegion**

The AWS region where the organization centralization rule was created.

Type: String

Length Constraints: Minimum length of 1.

Required: No

**CreatedTimeStamp**

The timestamp when the organization centralization rule was created.

Type: Long

Required: No

**CreatorAccountId**

The AWS Account that created the organization centralization rule.

Type: String

Required: No

**DestinationAccountId**

The primary destination account of the organization centralization rule.

Type: String

Required: No

**DestinationRegion**

The primary destination region of the organization centralization rule.

Type: String

Length Constraints: Minimum length of 1.

Required: No

**FailureReason**

The reason why an organization centralization rule is marked UNHEALTHY.

Type: String

Valid Values: `TRUSTED_ACCESS_NOT_ENABLED | DESTINATION_ACCOUNT_NOT_IN_ORGANIZATION | INTERNAL_SERVER_ERROR`

Required: No

**LastUpdateTimeStamp**

The timestamp when the organization centralization rule was last updated.

Type: Long

Required: No

**RuleArn**

The Amazon Resource Name (ARN) of the organization centralization rule.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 1011.

Pattern: `arn:aws([a-z0-9\-]+)?:([a-zA-Z0-9\-]+):([a-z0-9\-]+)?:([0-9]{12})?:(.+)`

Required: No

**RuleHealth**

The health status of the organization centralization rule.

Type: String

Valid Values: `Healthy | Unhealthy | Provisioning`

Required: No

**RuleName**

The name of the organization centralization rule.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 100.

Pattern: `[0-9A-Za-z-_.#/]+`

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/observabilityadmin-2018-05-10/CentralizationRuleSummary.md "../../../goto/SdkForCpp/observabilityadmin-2018-05-10/CentralizationRuleSummary.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/observabilityadmin-2018-05-10/CentralizationRuleSummary.md "../../../goto/SdkForJavaV2/observabilityadmin-2018-05-10/CentralizationRuleSummary.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/observabilityadmin-2018-05-10/CentralizationRuleSummary.md "../../../goto/SdkForRubyV3/observabilityadmin-2018-05-10/CentralizationRuleSummary.md")
