

# Setting
<a name="API_Setting"></a>

Contains information about the configurable settings for a directory.

## Contents
<a name="API_Setting_Contents"></a>

 ** Name **   <a name="DirectoryService-Type-Setting-Name"></a>
The name of the directory setting. For example:  
 `TLS_1_0`   
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 255.  
Pattern: `^[a-zA-Z0-9-/. _]*$`   
Required: Yes

 ** Value **   <a name="DirectoryService-Type-Setting-Value"></a>
The value of the directory setting for which to retrieve information. For example, for `TLS_1_0`, the valid values are: `Enable` and `Disable`.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 255.  
Pattern: `^[a-zA-Z0-9_]*$`   
Required: Yes

## See Also
<a name="API_Setting_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ds-2015-04-16/Setting) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ds-2015-04-16/Setting) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ds-2015-04-16/Setting) 