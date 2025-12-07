# FieldToMatch

Specifies a field in the request to redact from WAF logs, such as headers, query
parameters, or body content.

## Contents

**Method**

Redacts the HTTP method from WAF logs.

Type: String

Required: No

**QueryString**

Redacts the entire query string from WAF logs.

Type: String

Required: No

**SingleHeader**

Redacts a specific header field by name from WAF logs.

Type: [SingleHeader](API_SingleHeader.md "API_SingleHeader.md") object

Required: No

**UriPath**

Redacts the URI path from WAF logs.

Type: String

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/observabilityadmin-2018-05-10/FieldToMatch.md "../../../goto/SdkForCpp/observabilityadmin-2018-05-10/FieldToMatch.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/observabilityadmin-2018-05-10/FieldToMatch.md "../../../goto/SdkForJavaV2/observabilityadmin-2018-05-10/FieldToMatch.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/observabilityadmin-2018-05-10/FieldToMatch.md "../../../goto/SdkForRubyV3/observabilityadmin-2018-05-10/FieldToMatch.md")
