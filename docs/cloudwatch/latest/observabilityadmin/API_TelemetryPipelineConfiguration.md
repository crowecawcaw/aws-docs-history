# TelemetryPipelineConfiguration

Defines the configuration for a pipeline, including how data flows from sources through
processors to destinations. The configuration is specified in YAML format and must include a
valid pipeline definition with required source and sink components. This pipeline enables
end-to-end telemetry data collection, transformation, and delivery while supporting optional
processing steps and extensions for enhanced functionality.

The primary pipeline configuration section are:

- **Source:** Defines where log data originates from (S3
  buckets, CloudWatch Logs, third-party APIs). Each pipeline must have exactly one
  source.
- **Processors (optional):** Transform, parse, and enrich
  log data as it flows through the pipeline. Processors are applied sequentially in the
  order they are defined.
- **Sink:** Defines the destination where processed log
  data is sent. Each pipeline must have exactly one sink.
- **Extensions (optional):** Provide additional
  functionality such as AWS Secrets Manager integration for credential management.
  For more details on each configuration section see [CloudWatch pipelines User
  Guide](../../../AmazonCloudWatch/latest/monitoring/cloudwatch-pipelines.md "../../../AmazonCloudWatch/latest/monitoring/cloudwatch-pipelines.md"). Additional comprehensive configuration examples can be found in the [CreateTelemetryPipeline API docs](API_CreateTelemetryPipeline.md#API_CreateTelemetryPipeline_Examples "API_CreateTelemetryPipeline.md#API_CreateTelemetryPipeline_Examples").

## Contents

**Body**

The pipeline configuration body that defines the data processing rules and
transformations.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 24000.

Required: Yes

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/observabilityadmin-2018-05-10/TelemetryPipelineConfiguration.md "../../../goto/SdkForCpp/observabilityadmin-2018-05-10/TelemetryPipelineConfiguration.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/observabilityadmin-2018-05-10/TelemetryPipelineConfiguration.md "../../../goto/SdkForJavaV2/observabilityadmin-2018-05-10/TelemetryPipelineConfiguration.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/observabilityadmin-2018-05-10/TelemetryPipelineConfiguration.md "../../../goto/SdkForRubyV3/observabilityadmin-2018-05-10/TelemetryPipelineConfiguration.md")
