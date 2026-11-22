

# AzureTelemetrySourceConfigurationInput

The Microsoft Azure source configuration for a third-party telemetry enrichment.

## Contents
<a name="API_AzureTelemetrySourceConfigurationInput_Contents"></a>

 ** AwsConfigConnectorArn **   <a name="cwoa-Type-AzureTelemetrySourceConfigurationInput-AwsConfigConnectorArn"></a>
The Amazon Resource Name (ARN) of the AWS Config connector for the Microsoft Azure tenant to collect resource metadata from.  
Type: String  
Length Constraints: Minimum length of 20. Maximum length of 2048.  
Pattern: `arn:aws(-[a-z]+)*:config:[a-z0-9\-]+:[0-9]{12}:connector/[^\r\n]+`   
Required: Yes

## See Also
<a name="API_AzureTelemetrySourceConfigurationInput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/observabilityadmin-2018-05-10/AzureTelemetrySourceConfigurationInput) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/observabilityadmin-2018-05-10/AzureTelemetrySourceConfigurationInput) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/observabilityadmin-2018-05-10/AzureTelemetrySourceConfigurationInput) 