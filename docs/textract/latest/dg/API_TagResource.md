# TagResource

Adds one or more tags to the specified resource.

## Request Syntax

```
{
   "ResourceARN": "`string`",
   "Tags": {
      "`string`" : "`string`"
   }
}
```

## Request Parameters

The request accepts the following data in JSON format.

**[ResourceARN](#API_TagResource_RequestSyntax "#API_TagResource_RequestSyntax")**

The Amazon Resource Name (ARN) that specifies the resource to be tagged.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 1011.

Required: Yes

**[Tags](#API_TagResource_RequestSyntax "#API_TagResource_RequestSyntax")**

A set of tags (key-value pairs) that you want to assign to the resource.

Type: String to string map

Map Entries: Minimum number of 0 items. Maximum number of 200 items.

Key Length Constraints: Minimum length of 1. Maximum length of 128.

Key Pattern: `^(?!aws:)[\p{L}\p{Z}\p{N}_.:/=+\-@]*$`

Value Length Constraints: Minimum length of 0. Maximum length of 256.

Value Pattern: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`

Required: Yes

## Response Elements

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

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

**ServiceQuotaExceededException**

Returned when a request cannot be completed as it would exceed a maximum service quota.

HTTP Status Code: 400

**ThrottlingException**

Amazon Textract is temporarily unable to process the request. Try your call again.

HTTP Status Code: 500

**ValidationException**

Indicates that a request was not valid. Check request for proper formatting.

HTTP Status Code: 400

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/textract-2018-06-27/TagResource.md "../../../goto/cli2/textract-2018-06-27/TagResource.md")
- [AWS SDK for .NET V4](../../../goto/DotNetSDKV4/textract-2018-06-27/TagResource.md "../../../goto/DotNetSDKV4/textract-2018-06-27/TagResource.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/textract-2018-06-27/TagResource.md "../../../goto/SdkForCpp/textract-2018-06-27/TagResource.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/textract-2018-06-27/TagResource.md "../../../goto/SdkForGoV2/textract-2018-06-27/TagResource.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/textract-2018-06-27/TagResource.md "../../../goto/SdkForJavaV2/textract-2018-06-27/TagResource.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/textract-2018-06-27/TagResource.md "../../../goto/SdkForJavaScriptV3/textract-2018-06-27/TagResource.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/textract-2018-06-27/TagResource.md "../../../goto/SdkForKotlin/textract-2018-06-27/TagResource.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/textract-2018-06-27/TagResource.md "../../../goto/SdkForPHPV3/textract-2018-06-27/TagResource.md")
- [AWS SDK for Python](../../../goto/boto3/textract-2018-06-27/TagResource.md "../../../goto/boto3/textract-2018-06-27/TagResource.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/textract-2018-06-27/TagResource.md "../../../goto/SdkForRubyV3/textract-2018-06-27/TagResource.md")
