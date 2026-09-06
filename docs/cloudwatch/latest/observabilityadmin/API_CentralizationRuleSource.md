

# CentralizationRuleSource
<a name="API_CentralizationRuleSource"></a>

Configuration specifying the source of telemetry data to be centralized.

## Contents
<a name="API_CentralizationRuleSource_Contents"></a>

 ** Regions **   <a name="cwoa-Type-CentralizationRuleSource-Regions"></a>
The list of source regions from which telemetry data should be centralized.  
Type: Array of strings  
Array Members: Minimum number of 1 item.  
Length Constraints: Minimum length of 1.  
Required: Yes

 ** Scope **   <a name="cwoa-Type-CentralizationRuleSource-Scope"></a>
The organizational scope from which telemetry data should be centralized, specified using organization id, accounts or organizational unit ids.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2000.  
Required: No

 ** SourceLogsConfiguration **   <a name="cwoa-Type-CentralizationRuleSource-SourceLogsConfiguration"></a>
Log specific configuration for centralization source log groups.  
Type: [SourceLogsConfiguration](API_SourceLogsConfiguration.md) object  
Required: No

 ** SourceMetricsConfiguration **   <a name="cwoa-Type-CentralizationRuleSource-SourceMetricsConfiguration"></a>
Metric specific configuration for centralization source metrics.  
Type: [SourceMetricsConfiguration](API_SourceMetricsConfiguration.md) object  
Required: No

## See Also
<a name="API_CentralizationRuleSource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/observabilityadmin-2018-05-10/CentralizationRuleSource) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/observabilityadmin-2018-05-10/CentralizationRuleSource) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/observabilityadmin-2018-05-10/CentralizationRuleSource) 