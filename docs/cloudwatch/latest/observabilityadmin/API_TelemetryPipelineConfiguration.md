

# TelemetryPipelineConfiguration
<a name="API_TelemetryPipelineConfiguration"></a>

Defines the configuration for a pipeline, including how data flows from sources through processors to destinations. The configuration is specified in YAML format and must include a valid pipeline definition with required source and sink components. This pipeline enables end-to-end telemetry data collection, transformation, and delivery while supporting optional processing steps and extensions for enhanced functionality.

The primary pipeline configuration section are:
+  **Source:** Defines where log data originates from (S3 buckets, CloudWatch Logs, third-party APIs). Each pipeline must have exactly one source.
+  **Processors (optional):** Transform, parse, and enrich log data as it flows through the pipeline. Processors are applied sequentially in the order they are defined.
+  **Sink:** Defines the destination where processed log data is sent. Each pipeline must have exactly one sink.
+  **Extensions (optional):** Provide additional functionality such as AWS Secrets Manager integration for credential management.

For more details on each configuration section see [CloudWatch pipelines User Guide](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/cloudwatch-pipelines.html). Additional comprehensive configuration examples can be found in the [CreateTelemetryPipeline API docs](https://docs.aws.amazon.com/cloudwatch/latest/observabilityadmin/API_CreateTelemetryPipeline.html#API_CreateTelemetryPipeline_Examples).

## Contents
<a name="API_TelemetryPipelineConfiguration_Contents"></a>

 ** Body **   <a name="cwoa-Type-TelemetryPipelineConfiguration-Body"></a>
The pipeline configuration body that defines the data processing rules and transformations.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 24000.  
Required: Yes

## See Also
<a name="API_TelemetryPipelineConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/observabilityadmin-2018-05-10/TelemetryPipelineConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/observabilityadmin-2018-05-10/TelemetryPipelineConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/observabilityadmin-2018-05-10/TelemetryPipelineConfiguration) 