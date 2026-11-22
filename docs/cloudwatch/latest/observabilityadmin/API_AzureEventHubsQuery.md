

# AzureEventHubsQuery

A query that lists Azure Event Hubs.

## Contents
<a name="API_AzureEventHubsQuery_Contents"></a>

 ** NamespaceName **   <a name="cwoa-Type-AzureEventHubsQuery-NamespaceName"></a>
Limits the results to Event Hubs in this namespace.  
Type: String  
Length Constraints: Minimum length of 6. Maximum length of 50.  
Pattern: `[A-Za-z][A-Za-z0-9-]{4,48}[A-Za-z0-9]`   
Required: No

 ** Region **   <a name="cwoa-Type-AzureEventHubsQuery-Region"></a>
Limits the results to one Azure Region, for example `eastus`.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 64.  
Pattern: `[a-z0-9]+`   
Required: No

 ** Scope **   <a name="cwoa-Type-AzureEventHubsQuery-Scope"></a>
Limits the query to a management group or to specific subscriptions.  
Type: [AzureQueryScope](API_AzureQueryScope.md) object  
Required: No

## See Also
<a name="API_AzureEventHubsQuery_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/observabilityadmin-2018-05-10/AzureEventHubsQuery) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/observabilityadmin-2018-05-10/AzureEventHubsQuery) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/observabilityadmin-2018-05-10/AzureEventHubsQuery) 