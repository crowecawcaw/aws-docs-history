

# AzureScope

The Azure resources to collect telemetry from. These are the resources found by `Subscriptions`, `Regions`, and `ResourceTypes`, optionally narrowed by `TagFilters`, plus any resources listed in `Resources`. You can specify:
+  `Subscriptions`, `Regions`, and `ResourceTypes` together
+  `Resources` 
+ Both

## Contents
<a name="API_AzureScope_Contents"></a>

 ** Regions **   <a name="cwoa-Type-AzureScope-Regions"></a>
The Azure Regions to find resources in. Required when you use `Subscriptions` and `ResourceTypes`.  
Type: Array of strings  
Array Members: Minimum number of 1 item. Maximum number of 100 items.  
Length Constraints: Minimum length of 1. Maximum length of 64.  
Pattern: `[a-z0-9]+`   
Required: No

 ** Resources **   <a name="cwoa-Type-AzureScope-Resources"></a>
Specific Azure resources, listed by Azure Region.  
Type: Array of [AzureResourceIdScope](API_AzureResourceIdScope.md) objects  
Array Members: Minimum number of 1 item. Maximum number of 100 items.  
Required: No

 ** ResourceTypes **   <a name="cwoa-Type-AzureScope-ResourceTypes"></a>
The Azure resource types to find. Required when you use `Subscriptions` and `Regions`.  
Type: Array of strings  
Array Members: Minimum number of 1 item. Maximum number of 100 items.  
Length Constraints: Minimum length of 1. Maximum length of 256.  
Pattern: `[A-Za-z0-9]+\.[A-Za-z0-9]+/[A-Za-z0-9/]+`   
Required: No

 ** Subscriptions **   <a name="cwoa-Type-AzureScope-Subscriptions"></a>
The subscriptions to find resources in: all subscriptions that the connector can read, or a list of subscriptions. Required when you use `Regions` and `ResourceTypes`.  
Type: [AzureSubscriptionScope](API_AzureSubscriptionScope.md) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.  
Required: No

 ** TagFilters **   <a name="cwoa-Type-AzureScope-TagFilters"></a>
Limits the resources found by `Subscriptions`, `Regions`, and `ResourceTypes` to those that have these tags. You can specify up to 50 filters.  
Type: Array of [TagFilter](API_TagFilter.md) objects  
Array Members: Minimum number of 1 item. Maximum number of 50 items.  
Required: No

## See Also
<a name="API_AzureScope_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/observabilityadmin-2018-05-10/AzureScope) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/observabilityadmin-2018-05-10/AzureScope) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/observabilityadmin-2018-05-10/AzureScope) 