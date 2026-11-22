

# AzureResourceIdentifierSummary

Information about an Azure resource.

## Contents
<a name="API_AzureResourceIdentifierSummary_Contents"></a>

 ** ResourceId **   <a name="cwoa-Type-AzureResourceIdentifierSummary-ResourceId"></a>
The Azure Resource Manager ID of the resource.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 1024.  
Required: Yes

 ** Region **   <a name="cwoa-Type-AzureResourceIdentifierSummary-Region"></a>
The Azure Region of the resource, for example `eastus`.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 64.  
Pattern: `[a-z0-9]+`   
Required: No

 ** ResourceType **   <a name="cwoa-Type-AzureResourceIdentifierSummary-ResourceType"></a>
The Azure resource type, for example `Microsoft.Compute/virtualMachines`.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 256.  
Pattern: `[A-Za-z0-9]+\.[A-Za-z0-9]+/[A-Za-z0-9/]+`   
Required: No

 ** SubscriptionId **   <a name="cwoa-Type-AzureResourceIdentifierSummary-SubscriptionId"></a>
The Azure subscription that contains the resource.  
Type: String  
Length Constraints: Fixed length of 36.  
Pattern: `[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}`   
Required: No

 ** Tags **   <a name="cwoa-Type-AzureResourceIdentifierSummary-Tags"></a>
The tags on the resource. Absent if the resource has no tags.  
Type: String to string map  
Map Entries: Minimum number of 0 items. Maximum number of 50 items.  
Key Length Constraints: Minimum length of 1. Maximum length of 512.  
Value Length Constraints: Minimum length of 0. Maximum length of 256.  
Required: No

## See Also
<a name="API_AzureResourceIdentifierSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/observabilityadmin-2018-05-10/AzureResourceIdentifierSummary) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/observabilityadmin-2018-05-10/AzureResourceIdentifierSummary) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/observabilityadmin-2018-05-10/AzureResourceIdentifierSummary) 