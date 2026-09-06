

# CentralizationRuleDestination
<a name="API_CentralizationRuleDestination"></a>

Configuration specifying the primary destination for centralized telemetry data.

## Contents
<a name="API_CentralizationRuleDestination_Contents"></a>

 ** Region **   <a name="cwoa-Type-CentralizationRuleDestination-Region"></a>
The primary destination region to which telemetry data should be centralized.  
Type: String  
Length Constraints: Minimum length of 1.  
Required: Yes

 ** Account **   <a name="cwoa-Type-CentralizationRuleDestination-Account"></a>
The destination account (within the organization) to which the telemetry data should be centralized.  
Type: String  
Length Constraints: Fixed length of 12.  
Pattern: `[0-9]{12}`   
Required: No

 ** DestinationLogsConfiguration **   <a name="cwoa-Type-CentralizationRuleDestination-DestinationLogsConfiguration"></a>
Log specific configuration for centralization destination log groups.  
Type: [DestinationLogsConfiguration](API_DestinationLogsConfiguration.md) object  
Required: No

 ** DestinationMetricsConfiguration **   <a name="cwoa-Type-CentralizationRuleDestination-DestinationMetricsConfiguration"></a>
Metric specific configuration for centralization destination metrics.  
Type: [DestinationMetricsConfiguration](API_DestinationMetricsConfiguration.md) object  
Required: No

## See Also
<a name="API_CentralizationRuleDestination_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/observabilityadmin-2018-05-10/CentralizationRuleDestination) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/observabilityadmin-2018-05-10/CentralizationRuleDestination) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/observabilityadmin-2018-05-10/CentralizationRuleDestination) 