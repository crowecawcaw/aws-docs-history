

# AzureConnectorQueryResults

The results of an Azure discovery query. The populated member matches the member of the query.

## Contents
<a name="API_AzureConnectorQueryResults_Contents"></a>

**Important**  
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** EventHubs **   <a name="cwoa-Type-AzureConnectorQueryResults-EventHubs"></a>
The Azure Event Hubs.  
Type: Array of [AzureEventHubSummary](API_AzureEventHubSummary.md) objects  
Required: No

 ** ManagementGroups **   <a name="cwoa-Type-AzureConnectorQueryResults-ManagementGroups"></a>
The Azure management groups.  
Type: Array of [AzureManagementGroupSummary](API_AzureManagementGroupSummary.md) objects  
Required: No

 ** Regions **   <a name="cwoa-Type-AzureConnectorQueryResults-Regions"></a>
The Azure Regions.  
Type: Array of strings  
Length Constraints: Minimum length of 1. Maximum length of 64.  
Pattern: `[a-z0-9]+`   
Required: No

 ** ResourceIds **   <a name="cwoa-Type-AzureConnectorQueryResults-ResourceIds"></a>
The Azure resources.  
Type: Array of [AzureResourceIdentifierSummary](API_AzureResourceIdentifierSummary.md) objects  
Required: No

 ** ResourceTypes **   <a name="cwoa-Type-AzureConnectorQueryResults-ResourceTypes"></a>
The Azure resource types.  
Type: Array of strings  
Length Constraints: Minimum length of 1. Maximum length of 256.  
Pattern: `[A-Za-z0-9]+\.[A-Za-z0-9]+/[A-Za-z0-9/]+`   
Required: No

 ** Subscriptions **   <a name="cwoa-Type-AzureConnectorQueryResults-Subscriptions"></a>
The Azure subscriptions.  
Type: Array of [AzureSubscriptionSummary](API_AzureSubscriptionSummary.md) objects  
Required: No

## See Also
<a name="API_AzureConnectorQueryResults_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/observabilityadmin-2018-05-10/AzureConnectorQueryResults) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/observabilityadmin-2018-05-10/AzureConnectorQueryResults) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/observabilityadmin-2018-05-10/AzureConnectorQueryResults) 