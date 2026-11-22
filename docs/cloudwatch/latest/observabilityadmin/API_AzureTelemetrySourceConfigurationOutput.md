

# AzureTelemetrySourceConfigurationOutput

The Microsoft Azure source configuration of a third-party telemetry enrichment.

## Contents
<a name="API_AzureTelemetrySourceConfigurationOutput_Contents"></a>

 ** AwsConfigConnectorArn **   <a name="cwoa-Type-AzureTelemetrySourceConfigurationOutput-AwsConfigConnectorArn"></a>
The Amazon Resource Name (ARN) of the AWS Config connector that the enrichment uses.  
Type: String  
Length Constraints: Minimum length of 20. Maximum length of 2048.  
Pattern: `arn:aws(-[a-z]+)*:config:[a-z0-9\-]+:[0-9]{12}:connector/[^\r\n]+`   
Required: No

 ** ServiceLinkedRecorderArn **   <a name="cwoa-Type-AzureTelemetrySourceConfigurationOutput-ServiceLinkedRecorderArn"></a>
The Amazon Resource Name (ARN) of the service-linked configuration recorder that CloudWatch created in your account for the enrichment.  
Type: String  
Length Constraints: Minimum length of 20. Maximum length of 2048.  
Pattern: `arn:aws(-[a-z]+)*:config:[a-z0-9\-]+:[0-9]{12}:configuration-recorder/[^\r\n]+`   
Required: No

## See Also
<a name="API_AzureTelemetrySourceConfigurationOutput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/observabilityadmin-2018-05-10/AzureTelemetrySourceConfigurationOutput) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/observabilityadmin-2018-05-10/AzureTelemetrySourceConfigurationOutput) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/observabilityadmin-2018-05-10/AzureTelemetrySourceConfigurationOutput) 