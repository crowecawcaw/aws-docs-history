# DeleteAdapterVersion

Deletes an Amazon Textract adapter version. Requires that you specify both an AdapterId and a
AdapterVersion. Deletes the adapter version specified by the AdapterId and the AdapterVersion.

## Request Syntax

```
{
   "AdapterId": "`string`",
   "AdapterVersion": "`string`"
}
```

## Request Parameters

The request accepts the following data in JSON format.

**[AdapterId](#API_DeleteAdapterVersion_RequestSyntax "#API_DeleteAdapterVersion_RequestSyntax")**

A string containing a unique ID for the adapter version that will be deleted.

Type: String

Length Constraints: Minimum length of 12. Maximum length of 1011.

Required: Yes

**[AdapterVersion](#API_DeleteAdapterVersion_RequestSyntax "#API_DeleteAdapterVersion_RequestSyntax")**

Specifies the adapter version to be deleted.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 128.

Required: Yes

## Response Elements

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors

**AccessDeniedException**

You aren't authorized to perform the action. Use the Amazon Resource Name (ARN)
of an authorized user or IAM role to perform the operation.

HTTP Status Code: 400

**ConflictException**

Updating or deleting a resource can cause an inconsistent state.

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

- [AWS Command Line Interface V2](../../../goto/cli2/textract-2018-06-27/DeleteAdapterVersion.md "../../../goto/cli2/textract-2018-06-27/DeleteAdapterVersion.md")
- [AWS SDK for .NET](../../../goto/DotNetSDKV3/textract-2018-06-27/DeleteAdapterVersion.md "../../../goto/DotNetSDKV3/textract-2018-06-27/DeleteAdapterVersion.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/textract-2018-06-27/DeleteAdapterVersion.md "../../../goto/SdkForCpp/textract-2018-06-27/DeleteAdapterVersion.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/textract-2018-06-27/DeleteAdapterVersion.md "../../../goto/SdkForGoV2/textract-2018-06-27/DeleteAdapterVersion.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/textract-2018-06-27/DeleteAdapterVersion.md "../../../goto/SdkForJavaV2/textract-2018-06-27/DeleteAdapterVersion.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/textract-2018-06-27/DeleteAdapterVersion.md "../../../goto/SdkForJavaScriptV3/textract-2018-06-27/DeleteAdapterVersion.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/textract-2018-06-27/DeleteAdapterVersion.md "../../../goto/SdkForKotlin/textract-2018-06-27/DeleteAdapterVersion.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/textract-2018-06-27/DeleteAdapterVersion.md "../../../goto/SdkForPHPV3/textract-2018-06-27/DeleteAdapterVersion.md")
- [AWS SDK for Python](../../../goto/boto3/textract-2018-06-27/DeleteAdapterVersion.md "../../../goto/boto3/textract-2018-06-27/DeleteAdapterVersion.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/textract-2018-06-27/DeleteAdapterVersion.md "../../../goto/SdkForRubyV3/textract-2018-06-27/DeleteAdapterVersion.md")
