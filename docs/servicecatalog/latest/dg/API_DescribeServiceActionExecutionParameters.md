# DescribeServiceActionExecutionParameters

Finds the default parameters for a specific self-service action on a specific provisioned product and returns a map of the results to the user.

## Request Syntax

```
{
   "AcceptLanguage": "`string`",
   "ProvisionedProductId": "`string`",
   "ServiceActionId": "`string`"
}
```

## Request Parameters

The request accepts the following data in JSON format.

**[AcceptLanguage](#API_DescribeServiceActionExecutionParameters_RequestSyntax "#API_DescribeServiceActionExecutionParameters_RequestSyntax")**

The language code.

- `jp` - Japanese
- `zh` - Chinese

Type: String

Length Constraints: Maximum length of 100.

Required: No

**[ProvisionedProductId](#API_DescribeServiceActionExecutionParameters_RequestSyntax "#API_DescribeServiceActionExecutionParameters_RequestSyntax")**

The identifier of the provisioned product.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 100.

Pattern: `^[a-zA-Z0-9_\-]*`

Required: Yes

**[ServiceActionId](#API_DescribeServiceActionExecutionParameters_RequestSyntax "#API_DescribeServiceActionExecutionParameters_RequestSyntax")**

The self-service action identifier.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 100.

Pattern: `^[a-zA-Z0-9_\-]*`

Required: Yes

## Response Syntax

```
{
   "ServiceActionParameters": [
      {
         "DefaultValues": [ "***string***" ],
         "Name": "***string***",
         "Type": "***string***"
      }
   ]
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[ServiceActionParameters](#API_DescribeServiceActionExecutionParameters_ResponseSyntax "#API_DescribeServiceActionExecutionParameters_ResponseSyntax")**

The parameters of the self-service action.

Type: Array of [ExecutionParameter](API_ExecutionParameter.md "API_ExecutionParameter.md") objects

## Errors

**InvalidParametersException**

One or more parameters provided to the operation are not valid.

HTTP Status Code: 400

**ResourceNotFoundException**

The specified resource was not found.

HTTP Status Code: 400

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/servicecatalog-2015-12-10/DescribeServiceActionExecutionParameters.md "../../../goto/cli2/servicecatalog-2015-12-10/DescribeServiceActionExecutionParameters.md")
- [AWS SDK for .NET V4](../../../goto/DotNetSDKV4/servicecatalog-2015-12-10/DescribeServiceActionExecutionParameters.md "../../../goto/DotNetSDKV4/servicecatalog-2015-12-10/DescribeServiceActionExecutionParameters.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/servicecatalog-2015-12-10/DescribeServiceActionExecutionParameters.md "../../../goto/SdkForCpp/servicecatalog-2015-12-10/DescribeServiceActionExecutionParameters.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/servicecatalog-2015-12-10/DescribeServiceActionExecutionParameters.md "../../../goto/SdkForGoV2/servicecatalog-2015-12-10/DescribeServiceActionExecutionParameters.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/servicecatalog-2015-12-10/DescribeServiceActionExecutionParameters.md "../../../goto/SdkForJavaV2/servicecatalog-2015-12-10/DescribeServiceActionExecutionParameters.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/servicecatalog-2015-12-10/DescribeServiceActionExecutionParameters.md "../../../goto/SdkForJavaScriptV3/servicecatalog-2015-12-10/DescribeServiceActionExecutionParameters.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/servicecatalog-2015-12-10/DescribeServiceActionExecutionParameters.md "../../../goto/SdkForKotlin/servicecatalog-2015-12-10/DescribeServiceActionExecutionParameters.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/servicecatalog-2015-12-10/DescribeServiceActionExecutionParameters.md "../../../goto/SdkForPHPV3/servicecatalog-2015-12-10/DescribeServiceActionExecutionParameters.md")
- [AWS SDK for Python](../../../goto/boto3/servicecatalog-2015-12-10/DescribeServiceActionExecutionParameters.md "../../../goto/boto3/servicecatalog-2015-12-10/DescribeServiceActionExecutionParameters.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/servicecatalog-2015-12-10/DescribeServiceActionExecutionParameters.md "../../../goto/SdkForRubyV3/servicecatalog-2015-12-10/DescribeServiceActionExecutionParameters.md")
