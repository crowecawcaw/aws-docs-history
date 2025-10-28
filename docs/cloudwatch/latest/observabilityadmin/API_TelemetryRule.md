# TelemetryRule

Defines how telemetry should be configured for specific AWS resources.

## Contents

**TelemetryType**

The type of telemetry to collect (Logs, Metrics, or Traces).

Type: String

Valid Values: `Logs | Metrics | Traces`

Required: Yes

**DestinationConfiguration**

Configuration specifying where and how the telemetry data should be delivered.

Type: [TelemetryDestinationConfiguration](API_TelemetryDestinationConfiguration.md "API_TelemetryDestinationConfiguration.md") object

Required: No

**ResourceType**

The type of AWS resource to configure telemetry for (e.g., "AWS::EC2::VPC").

Type: String

Valid Values: `AWS::EC2::Instance | AWS::EC2::VPC | AWS::Lambda::Function`

Required: No

**Scope**

The organizational scope to which the rule applies, specified using accounts or
organizational units.

Type: String

Required: No

**SelectionCriteria**

Criteria for selecting which resources the rule applies to, such as resource tags.

Type: String

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/observabilityadmin-2018-05-10/TelemetryRule.md "../../../goto/SdkForCpp/observabilityadmin-2018-05-10/TelemetryRule.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/observabilityadmin-2018-05-10/TelemetryRule.md "../../../goto/SdkForJavaV2/observabilityadmin-2018-05-10/TelemetryRule.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/observabilityadmin-2018-05-10/TelemetryRule.md "../../../goto/SdkForRubyV3/observabilityadmin-2018-05-10/TelemetryRule.md")
