# TelemetryPipelineSummary

Contains summary information about a telemetry pipeline for listing operations.

## Contents

**Arn**

The Amazon Resource Name (ARN) of the telemetry pipeline.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 1011.

Pattern: `arn:aws([a-z0-9\-]+)?:([a-zA-Z0-9\-]+):([a-z0-9\-]+)?:([0-9]{12})?:(.+)`

Required: No

**ConfigurationSummary**

A summary of the pipeline configuration components.

Type: [ConfigurationSummary](API_ConfigurationSummary.md "API_ConfigurationSummary.md") object

Required: No

**CreatedTimeStamp**

The timestamp when the telemetry pipeline was created.

Type: Long

Required: No

**LastUpdateTimeStamp**

The timestamp when the telemetry pipeline was last updated.

Type: Long

Required: No

**Name**

The name of the telemetry pipeline.

Type: String

Length Constraints: Minimum length of 3. Maximum length of 28.

Pattern: `.*[a-z][a-z0-9\-]+.*`

Required: No

**Status**

The current status of the telemetry pipeline.

Type: String

Valid Values: `CREATING | ACTIVE | UPDATING | DELETING | CREATE_FAILED | UPDATE_FAILED`

Required: No

**Tags**

The key-value pairs associated with the telemetry pipeline resource.

Type: String to string map

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/observabilityadmin-2018-05-10/TelemetryPipelineSummary.md "../../../goto/SdkForCpp/observabilityadmin-2018-05-10/TelemetryPipelineSummary.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/observabilityadmin-2018-05-10/TelemetryPipelineSummary.md "../../../goto/SdkForJavaV2/observabilityadmin-2018-05-10/TelemetryPipelineSummary.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/observabilityadmin-2018-05-10/TelemetryPipelineSummary.md "../../../goto/SdkForRubyV3/observabilityadmin-2018-05-10/TelemetryPipelineSummary.md")
