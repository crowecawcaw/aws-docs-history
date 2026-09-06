

# TelemetryPipeline
<a name="API_TelemetryPipeline"></a>

Represents a complete telemetry pipeline resource with configuration, status, and metadata for data processing and transformation.

## Contents
<a name="API_TelemetryPipeline_Contents"></a>

 ** Arn **   <a name="cwoa-Type-TelemetryPipeline-Arn"></a>
The Amazon Resource Name (ARN) of the telemetry pipeline.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 1011.  
Pattern: `arn:aws([a-z0-9\-]+)?:([a-zA-Z0-9\-]+):([a-z0-9\-]+)?:([0-9]{12})?:(.+)`   
Required: No

 ** Configuration **   <a name="cwoa-Type-TelemetryPipeline-Configuration"></a>
The configuration that defines how the telemetry pipeline processes data.  
Type: [TelemetryPipelineConfiguration](API_TelemetryPipelineConfiguration.md) object  
Required: No

 ** CreatedTimeStamp **   <a name="cwoa-Type-TelemetryPipeline-CreatedTimeStamp"></a>
The timestamp when the telemetry pipeline was created.  
Type: Long  
Required: No

 ** LastUpdateTimeStamp **   <a name="cwoa-Type-TelemetryPipeline-LastUpdateTimeStamp"></a>
The timestamp when the telemetry pipeline was last updated.  
Type: Long  
Required: No

 ** Name **   <a name="cwoa-Type-TelemetryPipeline-Name"></a>
The name of the telemetry pipeline.  
Type: String  
Length Constraints: Minimum length of 3. Maximum length of 28.  
Pattern: `.*[a-z][a-z0-9\-]+.*`   
Required: No

 ** Status **   <a name="cwoa-Type-TelemetryPipeline-Status"></a>
The current status of the telemetry pipeline.  
Type: String  
Valid Values: `CREATING | ACTIVE | UPDATING | DELETING | CREATE_FAILED | UPDATE_FAILED`   
Required: No

 ** StatusReason **   <a name="cwoa-Type-TelemetryPipeline-StatusReason"></a>
Additional information about the pipeline status, including reasons for failure states.  
Type: [TelemetryPipelineStatusReason](API_TelemetryPipelineStatusReason.md) object  
Required: No

 ** Tags **   <a name="cwoa-Type-TelemetryPipeline-Tags"></a>
The key-value pairs associated with the telemetry pipeline resource.  
Type: String to string map  
Required: No

## See Also
<a name="API_TelemetryPipeline_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/observabilityadmin-2018-05-10/TelemetryPipeline) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/observabilityadmin-2018-05-10/TelemetryPipeline) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/observabilityadmin-2018-05-10/TelemetryPipeline) 