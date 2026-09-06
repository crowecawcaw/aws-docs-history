

# FieldToMatch
<a name="API_FieldToMatch"></a>

 Specifies a field in the request to redact from WAF logs, such as headers, query parameters, or body content. 

## Contents
<a name="API_FieldToMatch_Contents"></a>

 ** Method **   <a name="cwoa-Type-FieldToMatch-Method"></a>
 Redacts the HTTP method from WAF logs.   
Type: String  
Required: No

 ** QueryString **   <a name="cwoa-Type-FieldToMatch-QueryString"></a>
 Redacts the entire query string from WAF logs.   
Type: String  
Required: No

 ** SingleHeader **   <a name="cwoa-Type-FieldToMatch-SingleHeader"></a>
 Redacts a specific header field by name from WAF logs.   
Type: [SingleHeader](API_SingleHeader.md) object  
Required: No

 ** UriPath **   <a name="cwoa-Type-FieldToMatch-UriPath"></a>
 Redacts the URI path from WAF logs.   
Type: String  
Required: No

## See Also
<a name="API_FieldToMatch_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/observabilityadmin-2018-05-10/FieldToMatch) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/observabilityadmin-2018-05-10/FieldToMatch) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/observabilityadmin-2018-05-10/FieldToMatch) 