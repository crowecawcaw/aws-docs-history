

# AzureSubscriptionScope

The subscriptions to find resources in: all subscriptions that the connector can read, or a list of subscriptions. Specify one.

## Contents
<a name="API_AzureSubscriptionScope_Contents"></a>

**Important**  
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** All **   <a name="cwoa-Type-AzureSubscriptionScope-All"></a>
All subscriptions that Azure role-based access control (Azure RBAC) allows the connector to read. Subscriptions that the connector can read later are included automatically.  
Type: [AllSubscriptions](API_AllSubscriptions.md) object  
Required: No

 ** Ids **   <a name="cwoa-Type-AzureSubscriptionScope-Ids"></a>
A list of 1–1000 subscription IDs.  
Type: Array of strings  
Array Members: Minimum number of 1 item. Maximum number of 1000 items.  
Length Constraints: Fixed length of 36.  
Pattern: `[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}`   
Required: No

## See Also
<a name="API_AzureSubscriptionScope_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/observabilityadmin-2018-05-10/AzureSubscriptionScope) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/observabilityadmin-2018-05-10/AzureSubscriptionScope) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/observabilityadmin-2018-05-10/AzureSubscriptionScope) 