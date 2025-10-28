# TelemetryConfiguration

A model representing the state of a resource within an account according to telemetry
config.

## Contents

**AccountIdentifier**

The account ID which contains the resource managed in telemetry configuration. An example
of a valid account ID is `012345678901`.

Type: String

Length Constraints: Fixed length of 12.

Pattern: `[0-9]{12}`

Required: No

**LastUpdateTimeStamp**

The timestamp of the last change to the telemetry configuration for the resource. For
example, `1728679196318`.

Type: Long

Required: No

**ResourceIdentifier**

The identifier of the resource, for example `i-0b22a22eec53b9321`.

Type: String

Required: No

**ResourceTags**

Tags associated with the resource, for example `{ Name: "ExampleInstance",
 Environment: "Development" }`.

Type: String to string map

Required: No

**ResourceType**

The type of resource, for example `AWS::EC2::Instance`.

Type: String

Valid Values: `AWS::EC2::Instance | AWS::EC2::VPC | AWS::Lambda::Function`

Required: No

**TelemetryConfigurationState**

The configuration state for the resource, for example `{ Logs: NotApplicable;
 Metrics: Enabled; Traces: NotApplicable; }`.

Type: String to string map

Valid Keys: `Logs | Metrics | Traces`

Valid Values: `Enabled | Disabled | NotApplicable`

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/observabilityadmin-2018-05-10/TelemetryConfiguration.md "../../../goto/SdkForCpp/observabilityadmin-2018-05-10/TelemetryConfiguration.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/observabilityadmin-2018-05-10/TelemetryConfiguration.md "../../../goto/SdkForJavaV2/observabilityadmin-2018-05-10/TelemetryConfiguration.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/observabilityadmin-2018-05-10/TelemetryConfiguration.md "../../../goto/SdkForRubyV3/observabilityadmin-2018-05-10/TelemetryConfiguration.md")
