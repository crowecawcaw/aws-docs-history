

# AzureResourceIdsQuery

A query that lists Azure resources.

## Contents
<a name="API_AzureResourceIdsQuery_Contents"></a>

 ** Region **   <a name="cwoa-Type-AzureResourceIdsQuery-Region"></a>
Limits the results to one Azure Region, for example `eastus`.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 64.  
Pattern: `[a-z0-9]+`   
Required: No

 ** ResourceType **   <a name="cwoa-Type-AzureResourceIdsQuery-ResourceType"></a>
Limits the results to one Azure resource type, for example `Microsoft.Compute/virtualMachines`.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 256.  
Pattern: `[A-Za-z0-9]+\.[A-Za-z0-9]+/[A-Za-z0-9/]+`   
Required: No

 ** Scope **   <a name="cwoa-Type-AzureResourceIdsQuery-Scope"></a>
Limits the query to a management group or to specific subscriptions.  
Type: [AzureQueryScope](API_AzureQueryScope.md) object  
Required: No

 ** TagFilters **   <a name="cwoa-Type-AzureResourceIdsQuery-TagFilters"></a>
Limits the results to resources that have these tags. A resource must match the filters for all tag keys, and any of the values for each key. The service matches tag keys and values case-insensitively, as Azure does.  
Type: Array of [TagFilter](API_TagFilter.md) objects  
Array Members: Minimum number of 1 item. Maximum number of 50 items.  
Required: No

## See Also
<a name="API_AzureResourceIdsQuery_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/observabilityadmin-2018-05-10/AzureResourceIdsQuery) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/observabilityadmin-2018-05-10/AzureResourceIdsQuery) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/observabilityadmin-2018-05-10/AzureResourceIdsQuery) 