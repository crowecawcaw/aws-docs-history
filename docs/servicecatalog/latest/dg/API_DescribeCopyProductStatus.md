# DescribeCopyProductStatus

Gets the status of the specified copy product operation.

## Request Syntax

```
{
   "AcceptLanguage": "`string`",
   "CopyProductToken": "`string`"
}
```

## Request Parameters

The request accepts the following data in JSON format.

**[AcceptLanguage](#API_DescribeCopyProductStatus_RequestSyntax "#API_DescribeCopyProductStatus_RequestSyntax")**

The language code.

- `jp` - Japanese
- `zh` - Chinese

Type: String

Length Constraints: Maximum length of 100.

Required: No

**[CopyProductToken](#API_DescribeCopyProductStatus_RequestSyntax "#API_DescribeCopyProductStatus_RequestSyntax")**

The token for the copy product operation. This token is returned by [CopyProduct](API_CopyProduct.md "API_CopyProduct.md").

Type: String

Length Constraints: Minimum length of 1. Maximum length of 100.

Pattern: `^[a-zA-Z0-9_\-]*`

Required: Yes

## Response Syntax

```
{
   "CopyProductStatus": "***string***",
   "StatusDetail": "***string***",
   "TargetProductId": "***string***"
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[CopyProductStatus](#API_DescribeCopyProductStatus_ResponseSyntax "#API_DescribeCopyProductStatus_ResponseSyntax")**

The status of the copy product operation.

Type: String

Valid Values: `SUCCEEDED | IN_PROGRESS | FAILED`

**[StatusDetail](#API_DescribeCopyProductStatus_ResponseSyntax "#API_DescribeCopyProductStatus_ResponseSyntax")**

The status message.

Type: String

**[TargetProductId](#API_DescribeCopyProductStatus_ResponseSyntax "#API_DescribeCopyProductStatus_ResponseSyntax")**

The identifier of the copied product.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 100.

Pattern: `^[a-zA-Z0-9_\-]*`

## Errors

**ResourceNotFoundException**

The specified resource was not found.

HTTP Status Code: 400

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/servicecatalog-2015-12-10/DescribeCopyProductStatus.md "../../../goto/cli2/servicecatalog-2015-12-10/DescribeCopyProductStatus.md")
- [AWS SDK for .NET V4](../../../goto/DotNetSDKV4/servicecatalog-2015-12-10/DescribeCopyProductStatus.md "../../../goto/DotNetSDKV4/servicecatalog-2015-12-10/DescribeCopyProductStatus.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/servicecatalog-2015-12-10/DescribeCopyProductStatus.md "../../../goto/SdkForCpp/servicecatalog-2015-12-10/DescribeCopyProductStatus.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/servicecatalog-2015-12-10/DescribeCopyProductStatus.md "../../../goto/SdkForGoV2/servicecatalog-2015-12-10/DescribeCopyProductStatus.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/servicecatalog-2015-12-10/DescribeCopyProductStatus.md "../../../goto/SdkForJavaV2/servicecatalog-2015-12-10/DescribeCopyProductStatus.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/servicecatalog-2015-12-10/DescribeCopyProductStatus.md "../../../goto/SdkForJavaScriptV3/servicecatalog-2015-12-10/DescribeCopyProductStatus.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/servicecatalog-2015-12-10/DescribeCopyProductStatus.md "../../../goto/SdkForKotlin/servicecatalog-2015-12-10/DescribeCopyProductStatus.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/servicecatalog-2015-12-10/DescribeCopyProductStatus.md "../../../goto/SdkForPHPV3/servicecatalog-2015-12-10/DescribeCopyProductStatus.md")
- [AWS SDK for Python](../../../goto/boto3/servicecatalog-2015-12-10/DescribeCopyProductStatus.md "../../../goto/boto3/servicecatalog-2015-12-10/DescribeCopyProductStatus.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/servicecatalog-2015-12-10/DescribeCopyProductStatus.md "../../../goto/SdkForRubyV3/servicecatalog-2015-12-10/DescribeCopyProductStatus.md")
