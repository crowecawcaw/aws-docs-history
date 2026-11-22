

# AzureFlowLogStorageAccountScope

The Azure Storage Accounts in one Azure Region that store Flow Logs.

## Contents
<a name="API_AzureFlowLogStorageAccountScope_Contents"></a>

 ** Region **   <a name="cwoa-Type-AzureFlowLogStorageAccountScope-Region"></a>
The Azure Region of the Storage Accounts, for example `eastus`.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 64.  
Pattern: `[a-z0-9]+`   
Required: Yes

 ** StorageAccountIds **   <a name="cwoa-Type-AzureFlowLogStorageAccountScope-StorageAccountIds"></a>
The Azure Resource Manager IDs of the Storage Accounts.  
Type: Array of strings  
Array Members: Minimum number of 1 item. Maximum number of 100 items.  
Length Constraints: Minimum length of 1. Maximum length of 1024.  
Pattern: `/[sS][uU][bB][sS][cC][rR][iI][pP][tT][iI][oO][nN][sS]/[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}/[rR][eE][sS][oO][uU][rR][cC][eE][gG][rR][oO][uU][pP][sS]/[^/${}'"`\\<>%&?#\s\u0000-\u001F\u007F]+/[pP][rR][oO][vV][iI][dD][eE][rR][sS]/[mM][iI][cC][rR][oO][sS][oO][fF][tT]\.[sS][tT][oO][rR][aA][gG][eE]/[sS][tT][oO][rR][aA][gG][eE][aA][cC][cC][oO][uU][nN][tT][sS]/[a-z0-9]{3,24}`   
Required: Yes

## See Also
<a name="API_AzureFlowLogStorageAccountScope_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/observabilityadmin-2018-05-10/AzureFlowLogStorageAccountScope) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/observabilityadmin-2018-05-10/AzureFlowLogStorageAccountScope) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/observabilityadmin-2018-05-10/AzureFlowLogStorageAccountScope) 