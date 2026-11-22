

# TagFilter

A tag filter. A resource matches only if it has the tag. Filters for different tag keys must all match; for one tag key, any of the values can match.

## Contents
<a name="API_TagFilter_Contents"></a>

 ** Key **   <a name="cwoa-Type-TagFilter-Key"></a>
The tag key. Up to 512 characters. The characters < > % & \\ ? / $ { } ' " ` and control characters aren't allowed.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 512.  
Pattern: `[^<>%&\\?/${}'"`\u0000-\u001F\u007F]+`   
Required: Yes

 ** Values **   <a name="cwoa-Type-TagFilter-Values"></a>
The tag values to match. A resource matches if it has any of these values for the tag key.  
Type: Array of strings  
Array Members: Minimum number of 1 item. Maximum number of 50 items.  
Length Constraints: Minimum length of 0. Maximum length of 256.  
Pattern: `[^${}'"`\\<>\u0000-\u001F\u007F]*`   
Required: Yes

## See Also
<a name="API_TagFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/observabilityadmin-2018-05-10/TagFilter) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/observabilityadmin-2018-05-10/TagFilter) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/observabilityadmin-2018-05-10/TagFilter) 