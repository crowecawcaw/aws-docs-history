# TelemetryPipeline

Represents a complete telemetry pipeline resource with configuration, status, and metadata
for data processing and transformation.

## Contents

**Arn**

The Amazon Resource Name (ARN) of the telemetry pipeline.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 1011.

Pattern: `arn:aws([a-z0-9\-]+)?:([a-zA-Z0-9\-]+):([a-z0-9\-]+)?:([0-9]{12})?:(.+)`

Required: No

**Configuration**

The configuration that defines how the telemetry pipeline processes data.

Type: [TelemetryPipelineConfiguration](API_TelemetryPipelineConfiguration.md "API_TelemetryPipelineConfiguration.md") object

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

**StatusReason**

Additional information about the pipeline status, including reasons for failure
states.

Type: [TelemetryPipelineStatusReason](API_TelemetryPipelineStatusReason.md "API_TelemetryPipelineStatusReason.md") object

Required: No

**Tags**

The key-value pairs associated with the telemetry pipeline resource.

Type: String to string map

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/observabilityadmin-2018-05-10/TelemetryPipeline.md "../../../goto/SdkForCpp/observabilityadmin-2018-05-10/TelemetryPipeline.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/observabilityadmin-2018-05-10/TelemetryPipeline.md "../../../goto/SdkForJavaV2/observabilityadmin-2018-05-10/TelemetryPipeline.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/observabilityadmin-2018-05-10/TelemetryPipeline.md "../../../goto/SdkForRubyV3/observabilityadmin-2018-05-10/TelemetryPipeline.md")
