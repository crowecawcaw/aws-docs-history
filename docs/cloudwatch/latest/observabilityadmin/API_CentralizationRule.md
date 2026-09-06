

# CentralizationRule
<a name="API_CentralizationRule"></a>

Defines how telemetry data should be centralized across an AWS Organization, including source and destination configurations.

## Contents
<a name="API_CentralizationRule_Contents"></a>

 ** Destination **   <a name="cwoa-Type-CentralizationRule-Destination"></a>
Configuration determining where the telemetry data should be centralized, backed up, as well as encryption configuration for the primary and backup destinations.  
Type: [CentralizationRuleDestination](API_CentralizationRuleDestination.md) object  
Required: Yes

 ** Source **   <a name="cwoa-Type-CentralizationRule-Source"></a>
Configuration determining the source of the telemetry data to be centralized.  
Type: [CentralizationRuleSource](API_CentralizationRuleSource.md) object  
Required: Yes

## See Also
<a name="API_CentralizationRule_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/observabilityadmin-2018-05-10/CentralizationRule) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/observabilityadmin-2018-05-10/CentralizationRule) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/observabilityadmin-2018-05-10/CentralizationRule) 