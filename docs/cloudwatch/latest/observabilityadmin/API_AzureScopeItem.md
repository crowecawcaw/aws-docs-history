

# AzureScopeItem

The telemetry types to collect from a set of Azure resources.

## Contents
<a name="API_AzureScopeItem_Contents"></a>

 ** Scope **   <a name="cwoa-Type-AzureScopeItem-Scope"></a>
The Azure resources to collect telemetry from.  
Type: [AzureScope](API_AzureScope.md) object  
Required: Yes

 ** TelemetryTypes **   <a name="cwoa-Type-AzureScopeItem-TelemetryTypes"></a>
The telemetry types to collect.  
Type: Array of strings  
Array Members: Minimum number of 1 item. Maximum number of 3 items.  
Valid Values: `ResourceLogs | Metrics | FlowLogs`   
Required: Yes

## See Also
<a name="API_AzureScopeItem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/observabilityadmin-2018-05-10/AzureScopeItem) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/observabilityadmin-2018-05-10/AzureScopeItem) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/observabilityadmin-2018-05-10/AzureScopeItem) 