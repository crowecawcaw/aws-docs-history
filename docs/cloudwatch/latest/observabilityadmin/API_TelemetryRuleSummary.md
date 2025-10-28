# TelemetryRuleSummary

A summary of a telemetry rule's key properties.

## Contents

**CreatedTimeStamp**

The timestamp when the telemetry rule was created.

Type: Long

Required: No

**LastUpdateTimeStamp**

The timestamp when the telemetry rule was last modified.

Type: Long

Required: No

**ResourceType**

The type of AWS resource the rule applies to.

Type: String

Valid Values: `AWS::EC2::Instance | AWS::EC2::VPC | AWS::Lambda::Function`

Required: No

**RuleArn**

The Amazon Resource Name (ARN) of the telemetry rule.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 1011.

Pattern: `arn:aws([a-z0-9\-]+)?:([a-zA-Z0-9\-]+):([a-z0-9\-]+)?:([0-9]{12})?:(.+)`

Required: No

**RuleName**

The name of the telemetry rule.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 100.

Pattern: `[0-9A-Za-z-_.#/]+`

Required: No

**TelemetryType**

The type of telemetry (Logs, Metrics, or Traces) the rule configures.

Type: String

Valid Values: `Logs | Metrics | Traces`

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/observabilityadmin-2018-05-10/TelemetryRuleSummary.md "../../../goto/SdkForCpp/observabilityadmin-2018-05-10/TelemetryRuleSummary.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/observabilityadmin-2018-05-10/TelemetryRuleSummary.md "../../../goto/SdkForJavaV2/observabilityadmin-2018-05-10/TelemetryRuleSummary.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/observabilityadmin-2018-05-10/TelemetryRuleSummary.md "../../../goto/SdkForRubyV3/observabilityadmin-2018-05-10/TelemetryRuleSummary.md")
