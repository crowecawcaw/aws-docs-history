# DescribeServiceAction

Describes a self-service action.

## Request Syntax

```
{
   "AcceptLanguage": "`string`",
   "Id": "`string`"
}
```

## Request Parameters

The request accepts the following data in JSON format.

**[AcceptLanguage](#API_DescribeServiceAction_RequestSyntax "#API_DescribeServiceAction_RequestSyntax")**

The language code.

- `jp` - Japanese
- `zh` - Chinese

Type: String

Length Constraints: Maximum length of 100.

Required: No

**[Id](#API_DescribeServiceAction_RequestSyntax "#API_DescribeServiceAction_RequestSyntax")**

The self-service action identifier.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 100.

Pattern: `^[a-zA-Z0-9_\-]*`

Required: Yes

## Response Syntax

```
{
   "ServiceActionDetail": {
      "Definition": {
         "***string***" : "***string***"
      },
      "ServiceActionSummary": {
         "DefinitionType": "***string***",
         "Description": "***string***",
         "Id": "***string***",
         "Name": "***string***"
      }
   }
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[ServiceActionDetail](#API_DescribeServiceAction_ResponseSyntax "#API_DescribeServiceAction_ResponseSyntax")**

Detailed information about the self-service action.

Type: [ServiceActionDetail](API_ServiceActionDetail.md "API_ServiceActionDetail.md") object

## Errors

**ResourceNotFoundException**

The specified resource was not found.

HTTP Status Code: 400

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/servicecatalog-2015-12-10/DescribeServiceAction.md "../../../goto/cli2/servicecatalog-2015-12-10/DescribeServiceAction.md")
- [AWS SDK for .NET V4](../../../goto/DotNetSDKV4/servicecatalog-2015-12-10/DescribeServiceAction.md "../../../goto/DotNetSDKV4/servicecatalog-2015-12-10/DescribeServiceAction.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/servicecatalog-2015-12-10/DescribeServiceAction.md "../../../goto/SdkForCpp/servicecatalog-2015-12-10/DescribeServiceAction.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/servicecatalog-2015-12-10/DescribeServiceAction.md "../../../goto/SdkForGoV2/servicecatalog-2015-12-10/DescribeServiceAction.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/servicecatalog-2015-12-10/DescribeServiceAction.md "../../../goto/SdkForJavaV2/servicecatalog-2015-12-10/DescribeServiceAction.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/servicecatalog-2015-12-10/DescribeServiceAction.md "../../../goto/SdkForJavaScriptV3/servicecatalog-2015-12-10/DescribeServiceAction.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/servicecatalog-2015-12-10/DescribeServiceAction.md "../../../goto/SdkForKotlin/servicecatalog-2015-12-10/DescribeServiceAction.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/servicecatalog-2015-12-10/DescribeServiceAction.md "../../../goto/SdkForPHPV3/servicecatalog-2015-12-10/DescribeServiceAction.md")
- [AWS SDK for Python](../../../goto/boto3/servicecatalog-2015-12-10/DescribeServiceAction.md "../../../goto/boto3/servicecatalog-2015-12-10/DescribeServiceAction.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/servicecatalog-2015-12-10/DescribeServiceAction.md "../../../goto/SdkForRubyV3/servicecatalog-2015-12-10/DescribeServiceAction.md")
