# DeleteFilter

Deletes a filter.

## Request Syntax

```
{
   "filterArn": "`string`"
}
```

## Request Parameters

The request accepts the following data in JSON format.

**[filterArn](#API_DeleteFilter_RequestSyntax "#API_DeleteFilter_RequestSyntax")**

The ARN of the filter to delete.

Type: String

Length Constraints: Maximum length of 256.

Pattern: `arn:([a-z\d-]+):personalize:.*:.*:.+`

Required: Yes

## Response Elements

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors

**InvalidInputException**

Provide a valid value for the field or parameter.

HTTP Status Code: 400

**ResourceInUseException**

The specified resource is in use.

HTTP Status Code: 400

**ResourceNotFoundException**

Could not find the specified resource.

HTTP Status Code: 400

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/personalize-2018-05-22/DeleteFilter.md "../../../goto/cli2/personalize-2018-05-22/DeleteFilter.md")
- [AWS SDK for .NET](../../../goto/DotNetSDKV3/personalize-2018-05-22/DeleteFilter.md "../../../goto/DotNetSDKV3/personalize-2018-05-22/DeleteFilter.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/personalize-2018-05-22/DeleteFilter.md "../../../goto/SdkForCpp/personalize-2018-05-22/DeleteFilter.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/personalize-2018-05-22/DeleteFilter.md "../../../goto/SdkForGoV2/personalize-2018-05-22/DeleteFilter.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/personalize-2018-05-22/DeleteFilter.md "../../../goto/SdkForJavaV2/personalize-2018-05-22/DeleteFilter.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/personalize-2018-05-22/DeleteFilter.md "../../../goto/SdkForJavaScriptV3/personalize-2018-05-22/DeleteFilter.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/personalize-2018-05-22/DeleteFilter.md "../../../goto/SdkForKotlin/personalize-2018-05-22/DeleteFilter.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/personalize-2018-05-22/DeleteFilter.md "../../../goto/SdkForPHPV3/personalize-2018-05-22/DeleteFilter.md")
- [AWS SDK for Python](../../../goto/boto3/personalize-2018-05-22/DeleteFilter.md "../../../goto/boto3/personalize-2018-05-22/DeleteFilter.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/personalize-2018-05-22/DeleteFilter.md "../../../goto/SdkForRubyV3/personalize-2018-05-22/DeleteFilter.md")
