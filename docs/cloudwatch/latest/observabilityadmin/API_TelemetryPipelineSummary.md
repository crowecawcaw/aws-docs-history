

# TelemetryPipelineSummary
<a name="API_TelemetryPipelineSummary"></a>

Contains summary information about a telemetry pipeline for listing operations.

## Contents
<a name="API_TelemetryPipelineSummary_Contents"></a>

 ** Arn **   <a name="cwoa-Type-TelemetryPipelineSummary-Arn"></a>
The Amazon Resource Name (ARN) of the telemetry pipeline.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 1011.  
Pattern: `arn:aws([a-z0-9\-]+)?:([a-zA-Z0-9\-]+):([a-z0-9\-]+)?:([0-9]{12})?:(.+)`   
Required: No

 ** ConfigurationSummary **   <a name="cwoa-Type-TelemetryPipelineSummary-ConfigurationSummary"></a>
A summary of the pipeline configuration components.  
Type: [ConfigurationSummary](API_ConfigurationSummary.md) object  
Required: No

 ** CreatedTimeStamp **   <a name="cwoa-Type-TelemetryPipelineSummary-CreatedTimeStamp"></a>
The timestamp when the telemetry pipeline was created.  
Type: Long  
Required: No

 ** LastUpdateTimeStamp **   <a name="cwoa-Type-TelemetryPipelineSummary-LastUpdateTimeStamp"></a>
The timestamp when the telemetry pipeline was last updated.  
Type: Long  
Required: No

 ** Name **   <a name="cwoa-Type-TelemetryPipelineSummary-Name"></a>
The name of the telemetry pipeline.  
Type: String  
Length Constraints: Minimum length of 3. Maximum length of 28.  
Pattern: `.*[a-z][a-z0-9\-]+.*`   
Required: No

 ** Status **   <a name="cwoa-Type-TelemetryPipelineSummary-Status"></a>
The current status of the telemetry pipeline.  
Type: String  
Valid Values: `CREATING | ACTIVE | UPDATING | DELETING | CREATE_FAILED | UPDATE_FAILED`   
Required: No

 ** Tags **   <a name="cwoa-Type-TelemetryPipelineSummary-Tags"></a>
The key-value pairs associated with the telemetry pipeline resource.  
Type: String to string map  
Required: No

## See Also
<a name="API_TelemetryPipelineSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/observabilityadmin-2018-05-10/TelemetryPipelineSummary) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/observabilityadmin-2018-05-10/TelemetryPipelineSummary) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/observabilityadmin-2018-05-10/TelemetryPipelineSummary) 