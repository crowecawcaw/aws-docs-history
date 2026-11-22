

# AzureEventHubSummary

Information about an Azure Event Hub.

## Contents
<a name="API_AzureEventHubSummary_Contents"></a>

 ** EventHubName **   <a name="cwoa-Type-AzureEventHubSummary-EventHubName"></a>
The name of the Event Hub.  
Type: String  
Required: Yes

 ** FullyQualifiedNamespace **   <a name="cwoa-Type-AzureEventHubSummary-FullyQualifiedNamespace"></a>
The fully qualified host name of the Event Hubs namespace, for example `<namespace>.servicebus.windows.net`. The suffix differs in sovereign clouds.  
Type: String  
Required: Yes

 ** NamespaceName **   <a name="cwoa-Type-AzureEventHubSummary-NamespaceName"></a>
The name of the Event Hubs namespace that contains the Event Hub.  
Type: String  
Length Constraints: Minimum length of 6. Maximum length of 50.  
Pattern: `[A-Za-z][A-Za-z0-9-]{4,48}[A-Za-z0-9]`   
Required: Yes

 ** ResourceId **   <a name="cwoa-Type-AzureEventHubSummary-ResourceId"></a>
The Azure Resource Manager ID of the Event Hub.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 1024.  
Required: Yes

 ** Region **   <a name="cwoa-Type-AzureEventHubSummary-Region"></a>
The Azure Region of the Event Hub, for example `eastus`.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 64.  
Pattern: `[a-z0-9]+`   
Required: No

 ** SubscriptionId **   <a name="cwoa-Type-AzureEventHubSummary-SubscriptionId"></a>
The Azure subscription that contains the Event Hub.  
Type: String  
Length Constraints: Fixed length of 36.  
Pattern: `[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}`   
Required: No

## See Also
<a name="API_AzureEventHubSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/observabilityadmin-2018-05-10/AzureEventHubSummary) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/observabilityadmin-2018-05-10/AzureEventHubSummary) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/observabilityadmin-2018-05-10/AzureEventHubSummary) 