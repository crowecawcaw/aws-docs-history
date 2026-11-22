

# AzureSubscriptionSummary

Information about an Azure subscription.

## Contents
<a name="API_AzureSubscriptionSummary_Contents"></a>

 ** SubscriptionId **   <a name="cwoa-Type-AzureSubscriptionSummary-SubscriptionId"></a>
The ID of the subscription.  
Type: String  
Length Constraints: Fixed length of 36.  
Pattern: `[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}`   
Required: Yes

 ** DisplayName **   <a name="cwoa-Type-AzureSubscriptionSummary-DisplayName"></a>
The display name of the subscription.  
Type: String  
Required: No

 ** ManagementGroupId **   <a name="cwoa-Type-AzureSubscriptionSummary-ManagementGroupId"></a>
The ID of the management group that contains the subscription.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 90.  
Pattern: `[-\w._()]+`   
Required: No

 ** State **   <a name="cwoa-Type-AzureSubscriptionSummary-State"></a>
The state of the subscription in Azure, for example `Enabled`.  
Type: String  
Required: No

## See Also
<a name="API_AzureSubscriptionSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/observabilityadmin-2018-05-10/AzureSubscriptionSummary) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/observabilityadmin-2018-05-10/AzureSubscriptionSummary) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/observabilityadmin-2018-05-10/AzureSubscriptionSummary) 