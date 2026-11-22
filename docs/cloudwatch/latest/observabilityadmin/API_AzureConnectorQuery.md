

# AzureConnectorQuery

The type of Azure resource to list. Specify one type.

## Contents
<a name="API_AzureConnectorQuery_Contents"></a>

**Important**  
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** EventHubs **   <a name="cwoa-Type-AzureConnectorQuery-EventHubs"></a>
Lists Azure Event Hubs.  
Type: [AzureEventHubsQuery](API_AzureEventHubsQuery.md) object  
Required: No

 ** ManagementGroups **   <a name="cwoa-Type-AzureConnectorQuery-ManagementGroups"></a>
Lists Azure management groups.  
Type: [AzureManagementGroupsQuery](API_AzureManagementGroupsQuery.md) object  
Required: No

 ** Regions **   <a name="cwoa-Type-AzureConnectorQuery-Regions"></a>
Lists the Azure Regions that have resources in scope.  
Type: [AzureRegionsQuery](API_AzureRegionsQuery.md) object  
Required: No

 ** ResourceIds **   <a name="cwoa-Type-AzureConnectorQuery-ResourceIds"></a>
Lists Azure resources.  
Type: [AzureResourceIdsQuery](API_AzureResourceIdsQuery.md) object  
Required: No

 ** ResourceTypes **   <a name="cwoa-Type-AzureConnectorQuery-ResourceTypes"></a>
Lists the Azure resource types that have resources in scope.  
Type: [AzureResourceTypesQuery](API_AzureResourceTypesQuery.md) object  
Required: No

 ** Subscriptions **   <a name="cwoa-Type-AzureConnectorQuery-Subscriptions"></a>
Lists Azure subscriptions.  
Type: [AzureSubscriptionsQuery](API_AzureSubscriptionsQuery.md) object  
Required: No

## See Also
<a name="API_AzureConnectorQuery_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/observabilityadmin-2018-05-10/AzureConnectorQuery) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/observabilityadmin-2018-05-10/AzureConnectorQuery) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/observabilityadmin-2018-05-10/AzureConnectorQuery) 