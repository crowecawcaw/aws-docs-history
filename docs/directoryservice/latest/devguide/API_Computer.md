

# Computer
<a name="API_Computer"></a>

Contains information about a computer account in a directory.

## Contents
<a name="API_Computer_Contents"></a>

 ** ComputerAttributes **   <a name="DirectoryService-Type-Computer-ComputerAttributes"></a>
An array of [Attribute](API_Attribute.md) objects containing the LDAP attributes that belong to the computer account.  
Type: Array of [Attribute](API_Attribute.md) objects  
Required: No

 ** ComputerId **   <a name="DirectoryService-Type-Computer-ComputerId"></a>
The identifier of the computer.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 256.  
Pattern: `[&\w+-.@]+`   
Required: No

 ** ComputerName **   <a name="DirectoryService-Type-Computer-ComputerName"></a>
The computer name.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 15.  
Required: No

## See Also
<a name="API_Computer_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ds-2015-04-16/Computer) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ds-2015-04-16/Computer) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ds-2015-04-16/Computer) 