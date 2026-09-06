

# Tag
<a name="API_Tag"></a>

Metadata assigned to a directory consisting of a key-value pair.

## Contents
<a name="API_Tag_Contents"></a>

 ** Key **   <a name="DirectoryService-Type-Tag-Key"></a>
Required name of the tag. The string value can be Unicode characters and cannot be prefixed with "aws:". The string can contain only the set of Unicode letters, digits, white-space, '\_', '.', '/', '=', '\+', '-', ':', '@'(Java regex: "^([\\\\p{L}\\\\p{Z}\\\\p{N}\_.:/=\+\\\\-]\*)$").  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 128.  
Pattern: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`   
Required: Yes

 ** Value **   <a name="DirectoryService-Type-Tag-Value"></a>
The optional value of the tag. The string value can be Unicode characters. The string can contain only the set of Unicode letters, digits, white-space, '\_', '.', '/', '=', '\+', '-', ':', '@' (Java regex: "^([\\\\p{L}\\\\p{Z}\\\\p{N}\_.:/=\+\\\\-]\*)$").  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 256.  
Pattern: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`   
Required: Yes

## See Also
<a name="API_Tag_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ds-2015-04-16/Tag) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ds-2015-04-16/Tag) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ds-2015-04-16/Tag) 