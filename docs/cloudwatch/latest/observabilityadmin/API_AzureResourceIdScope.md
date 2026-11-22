

# AzureResourceIdScope

Azure resources in one Azure Region.

## Contents
<a name="API_AzureResourceIdScope_Contents"></a>

 ** Region **   <a name="cwoa-Type-AzureResourceIdScope-Region"></a>
The Azure Region of the resources, for example `eastus`. Required because an Azure resource ID doesn't include the Region.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 64.  
Pattern: `[a-z0-9]+`   
Required: Yes

 ** ResourceIds **   <a name="cwoa-Type-AzureResourceIdScope-ResourceIds"></a>
The Azure Resource Manager IDs of the resources.  
Type: Array of strings  
Array Members: Minimum number of 1 item. Maximum number of 1000 items.  
Length Constraints: Minimum length of 1. Maximum length of 1024.  
Pattern: `/[sS][uU][bB][sS][cC][rR][iI][pP][tT][iI][oO][nN][sS]/[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}(/[rR][eE][sS][oO][uU][rR][cC][eE][gG][rR][oO][uU][pP][sS]/[^/${}'"`\\<>%&?#\s\u0000-\u001F\u007F]+)?/[pP][rR][oO][vV][iI][dD][eE][rR][sS]/[A-Za-z0-9.]+/[^/${}'"`\\<>%&?#\s\u0000-\u001F\u007F]+(/[^/${}'"`\\<>%&?#\s\u0000-\u001F\u007F]+)*`   
Required: Yes

## See Also
<a name="API_AzureResourceIdScope_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/observabilityadmin-2018-05-10/AzureResourceIdScope) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/observabilityadmin-2018-05-10/AzureResourceIdScope) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/observabilityadmin-2018-05-10/AzureResourceIdScope) 