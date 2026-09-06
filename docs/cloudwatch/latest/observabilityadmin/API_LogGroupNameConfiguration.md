

# LogGroupNameConfiguration
<a name="API_LogGroupNameConfiguration"></a>

Configuration that specifies a naming pattern for destination log groups created during centralization. The pattern supports static text and dynamic variables that are replaced with source attributes when log groups are created.

## Contents
<a name="API_LogGroupNameConfiguration_Contents"></a>

 ** LogGroupNamePattern **   <a name="cwoa-Type-LogGroupNameConfiguration-LogGroupNamePattern"></a>
The pattern used to generate destination log group names during centralization. The pattern can contain static text and dynamic variables that are replaced with source attributes. If a variable cannot be resolved, it inherits the value from its parent variable in the hierarchy. The pattern must be between 1 and 512 characters.  
Supported variables:  
+  **${source.logGroup}** — The original log group name from the source account.
+  **${source.accountId}** — The AWS account ID where the log originated.
+  **${source.region}** — The AWS Region where the log originated.
+  **${source.org.id}** — The AWS Organization ID of the source account.
+  **${source.org.ouId}** — The organizational unit ID of the source account.
+  **${source.org.rootId}** — The organization Root ID.
+  **${source.org.path}** — The organizational path from account to root.
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 512.  
Pattern: `(?:[\._\-/#A-Za-z0-9]+|\$\{[A-Za-z]+(?:\.[A-Za-z]+){1,2}\})+`   
Required: Yes

## See Also
<a name="API_LogGroupNameConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/observabilityadmin-2018-05-10/LogGroupNameConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/observabilityadmin-2018-05-10/LogGroupNameConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/observabilityadmin-2018-05-10/LogGroupNameConfiguration) 