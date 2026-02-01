# GetAdapter

Gets configuration information for an adapter specified by an AdapterId, returning information on AdapterName, Description,
CreationTime, AutoUpdate status, and FeatureTypes.

## Request Syntax

```
{
   "AdapterId": "`string`"
}
```

## Request Parameters

The request accepts the following data in JSON format.

**[AdapterId](#API_GetAdapter_RequestSyntax "#API_GetAdapter_RequestSyntax")**

A string containing a unique ID for the adapter.

Type: String

Length Constraints: Minimum length of 12. Maximum length of 1011.

Required: Yes

## Response Syntax

```
{
   "AdapterId": "***string***",
   "AdapterName": "***string***",
   "AutoUpdate": "***string***",
   "CreationTime": ***number***,
   "Description": "***string***",
   "FeatureTypes": [ "***string***" ],
   "Tags": {
      "***string***" : "***string***"
   }
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[AdapterId](#API_GetAdapter_ResponseSyntax "#API_GetAdapter_ResponseSyntax")**

A string identifying the adapter that information has been retrieved for.

Type: String

Length Constraints: Minimum length of 12. Maximum length of 1011.

**[AdapterName](#API_GetAdapter_ResponseSyntax "#API_GetAdapter_ResponseSyntax")**

The name of the requested adapter.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 128.

Pattern: `[a-zA-Z0-9-_]+`

**[AutoUpdate](#API_GetAdapter_ResponseSyntax "#API_GetAdapter_ResponseSyntax")**

Binary value indicating if the adapter is being automatically updated or not.

Type: String

Valid Values: `ENABLED | DISABLED`

**[CreationTime](#API_GetAdapter_ResponseSyntax "#API_GetAdapter_ResponseSyntax")**

The date and time the requested adapter was created at.

Type: Timestamp

**[Description](#API_GetAdapter_ResponseSyntax "#API_GetAdapter_ResponseSyntax")**

The description for the requested adapter.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 256.

Pattern: `^[a-zA-Z0-9\s!"\#\$%'&\(\)\*\+\,\-\./:;=\?@\[\\\]\^_`\{\|\}~><]+$`

**[FeatureTypes](#API_GetAdapter_ResponseSyntax "#API_GetAdapter_ResponseSyntax")**

List of the targeted feature types for the requested adapter.

Type: Array of strings

Valid Values: `TABLES | FORMS | QUERIES | SIGNATURES | LAYOUT`

**[Tags](#API_GetAdapter_ResponseSyntax "#API_GetAdapter_ResponseSyntax")**

A set of tags (key-value pairs) associated with the adapter that has been retrieved.

Type: String to string map

Map Entries: Minimum number of 0 items. Maximum number of 200 items.

Key Length Constraints: Minimum length of 1. Maximum length of 128.

Key Pattern: `^(?!aws:)[\p{L}\p{Z}\p{N}_.:/=+\-@]*$`

Value Length Constraints: Minimum length of 0. Maximum length of 256.

Value Pattern: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`

## Errors

**AccessDeniedException**

You aren't authorized to perform the action. Use the Amazon Resource Name (ARN)
of an authorized user or IAM role to perform the operation.

HTTP Status Code: 400

**InternalServerError**

Amazon Textract experienced a service issue. Try your call again.

HTTP Status Code: 500

**InvalidParameterException**

An input parameter violated a constraint. For example, in synchronous operations,
an `InvalidParameterException` exception occurs
when neither of the `S3Object` or `Bytes` values are supplied in the `Document`
request parameter.
Validate your parameter before calling the API operation again.

HTTP Status Code: 400

**ProvisionedThroughputExceededException**

The number of requests exceeded your throughput limit. If you want to increase this limit,
contact Amazon Textract.

HTTP Status Code: 400

**ResourceNotFoundException**

Returned when an operation tried to access a nonexistent resource.

HTTP Status Code: 400

**ThrottlingException**

Amazon Textract is temporarily unable to process the request. Try your call again.

HTTP Status Code: 500

**ValidationException**

Indicates that a request was not valid. Check request for proper formatting.

HTTP Status Code: 400

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/textract-2018-06-27/GetAdapter.md "../../../goto/cli2/textract-2018-06-27/GetAdapter.md")
- [AWS SDK for .NET V4](../../../goto/DotNetSDKV4/textract-2018-06-27/GetAdapter.md "../../../goto/DotNetSDKV4/textract-2018-06-27/GetAdapter.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/textract-2018-06-27/GetAdapter.md "../../../goto/SdkForCpp/textract-2018-06-27/GetAdapter.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/textract-2018-06-27/GetAdapter.md "../../../goto/SdkForGoV2/textract-2018-06-27/GetAdapter.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/textract-2018-06-27/GetAdapter.md "../../../goto/SdkForJavaV2/textract-2018-06-27/GetAdapter.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/textract-2018-06-27/GetAdapter.md "../../../goto/SdkForJavaScriptV3/textract-2018-06-27/GetAdapter.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/textract-2018-06-27/GetAdapter.md "../../../goto/SdkForKotlin/textract-2018-06-27/GetAdapter.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/textract-2018-06-27/GetAdapter.md "../../../goto/SdkForPHPV3/textract-2018-06-27/GetAdapter.md")
- [AWS SDK for Python](../../../goto/boto3/textract-2018-06-27/GetAdapter.md "../../../goto/boto3/textract-2018-06-27/GetAdapter.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/textract-2018-06-27/GetAdapter.md "../../../goto/SdkForRubyV3/textract-2018-06-27/GetAdapter.md")
