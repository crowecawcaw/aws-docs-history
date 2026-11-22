

# AzureQueryScope

Limits a query to a management group or to specific subscriptions.

## Contents
<a name="API_AzureQueryScope_Contents"></a>

 ** ManagementGroupId **   <a name="cwoa-Type-AzureQueryScope-ManagementGroupId"></a>
Limits the query to resources under this management group.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 90.  
Pattern: `[-\w._()]+`   
Required: No

 ** SubscriptionIds **   <a name="cwoa-Type-AzureQueryScope-SubscriptionIds"></a>
Limits the query to these subscriptions. You can specify 1–1000 subscriptions.  
Type: Array of strings  
Array Members: Minimum number of 1 item. Maximum number of 1000 items.  
Length Constraints: Fixed length of 36.  
Pattern: `[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}`   
Required: No

## See Also
<a name="API_AzureQueryScope_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/observabilityadmin-2018-05-10/AzureQueryScope) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/observabilityadmin-2018-05-10/AzureQueryScope) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/observabilityadmin-2018-05-10/AzureQueryScope) 