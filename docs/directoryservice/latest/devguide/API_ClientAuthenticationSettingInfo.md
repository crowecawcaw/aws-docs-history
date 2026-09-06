

# ClientAuthenticationSettingInfo
<a name="API_ClientAuthenticationSettingInfo"></a>

Contains information about a client authentication method for a directory.

## Contents
<a name="API_ClientAuthenticationSettingInfo_Contents"></a>

 ** LastUpdatedDateTime **   <a name="DirectoryService-Type-ClientAuthenticationSettingInfo-LastUpdatedDateTime"></a>
The date and time when the status of the client authentication type was last updated.  
Type: Timestamp  
Required: No

 ** Status **   <a name="DirectoryService-Type-ClientAuthenticationSettingInfo-Status"></a>
Whether the client authentication type is enabled or disabled for the specified directory.  
Type: String  
Valid Values: `Enabled | Disabled`   
Required: No

 ** Type **   <a name="DirectoryService-Type-ClientAuthenticationSettingInfo-Type"></a>
The type of client authentication for the specified directory. If no type is specified, a list of all client authentication types that are supported for the directory is retrieved.   
Type: String  
Valid Values: `SmartCard | SmartCardOrPassword`   
Required: No

## See Also
<a name="API_ClientAuthenticationSettingInfo_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ds-2015-04-16/ClientAuthenticationSettingInfo) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ds-2015-04-16/ClientAuthenticationSettingInfo) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ds-2015-04-16/ClientAuthenticationSettingInfo) 