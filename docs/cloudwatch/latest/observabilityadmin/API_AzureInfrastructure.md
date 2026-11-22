

# AzureInfrastructure

The choices for the Azure infrastructure that the setup creates.

## Contents
<a name="API_AzureInfrastructure_Contents"></a>

 ** EventHubs **   <a name="cwoa-Type-AzureInfrastructure-EventHubs"></a>
The Event Hubs configuration. Specify exactly one entry, which applies to the Event Hubs in every Azure Region. This value applies only if an `AzureScopeItem` collects `ResourceLogs`. If you omit it, the setup uses default settings.  
Type: Array of [AzureEventHubConfiguration](API_AzureEventHubConfiguration.md) objects  
Array Members: Fixed number of 1 item.  
Required: No

 ** FlowLogs **   <a name="cwoa-Type-AzureInfrastructure-FlowLogs"></a>
The location of your Flow Logs. You must specify this value if an `AzureScopeItem` collects `FlowLogs`, and you can specify it only in that case.  
Type: [AzureFlowLogsInfrastructure](API_AzureFlowLogsInfrastructure.md) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.  
Required: No

 ** SubscriptionId **   <a name="cwoa-Type-AzureInfrastructure-SubscriptionId"></a>
The Azure subscription in which the setup creates the Event Hubs namespaces and, for `AwsManaged` Flow Logs, the Storage Accounts. You must specify this value if an `AzureScopeItem` collects `ResourceLogs`, or if you specify `EventHubs` or `AwsManaged` Flow Logs.  
Type: String  
Length Constraints: Fixed length of 36.  
Pattern: `[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}`   
Required: No

## See Also
<a name="API_AzureInfrastructure_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/observabilityadmin-2018-05-10/AzureInfrastructure) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/observabilityadmin-2018-05-10/AzureInfrastructure) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/observabilityadmin-2018-05-10/AzureInfrastructure) 