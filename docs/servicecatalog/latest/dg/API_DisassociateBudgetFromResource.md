# DisassociateBudgetFromResource

Disassociates the specified budget from the specified resource.

## Request Syntax

```
{
   "BudgetName": "`string`",
   "ResourceId": "`string`"
}
```

## Request Parameters

The request accepts the following data in JSON format.

**[BudgetName](#API_DisassociateBudgetFromResource_RequestSyntax "#API_DisassociateBudgetFromResource_RequestSyntax")**

The name of the budget you want to disassociate.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 100.

Required: Yes

**[ResourceId](#API_DisassociateBudgetFromResource_RequestSyntax "#API_DisassociateBudgetFromResource_RequestSyntax")**

The resource identifier you want to disassociate from. Either a portfolio-id or a product-id.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 100.

Pattern: `^[a-zA-Z0-9_\-]*`

Required: Yes

## Response Elements

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors

**ResourceNotFoundException**

The specified resource was not found.

HTTP Status Code: 400

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/servicecatalog-2015-12-10/DisassociateBudgetFromResource.md "../../../goto/cli2/servicecatalog-2015-12-10/DisassociateBudgetFromResource.md")
- [AWS SDK for .NET V4](../../../goto/DotNetSDKV4/servicecatalog-2015-12-10/DisassociateBudgetFromResource.md "../../../goto/DotNetSDKV4/servicecatalog-2015-12-10/DisassociateBudgetFromResource.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/servicecatalog-2015-12-10/DisassociateBudgetFromResource.md "../../../goto/SdkForCpp/servicecatalog-2015-12-10/DisassociateBudgetFromResource.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/servicecatalog-2015-12-10/DisassociateBudgetFromResource.md "../../../goto/SdkForGoV2/servicecatalog-2015-12-10/DisassociateBudgetFromResource.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/servicecatalog-2015-12-10/DisassociateBudgetFromResource.md "../../../goto/SdkForJavaV2/servicecatalog-2015-12-10/DisassociateBudgetFromResource.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/servicecatalog-2015-12-10/DisassociateBudgetFromResource.md "../../../goto/SdkForJavaScriptV3/servicecatalog-2015-12-10/DisassociateBudgetFromResource.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/servicecatalog-2015-12-10/DisassociateBudgetFromResource.md "../../../goto/SdkForKotlin/servicecatalog-2015-12-10/DisassociateBudgetFromResource.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/servicecatalog-2015-12-10/DisassociateBudgetFromResource.md "../../../goto/SdkForPHPV3/servicecatalog-2015-12-10/DisassociateBudgetFromResource.md")
- [AWS SDK for Python](../../../goto/boto3/servicecatalog-2015-12-10/DisassociateBudgetFromResource.md "../../../goto/boto3/servicecatalog-2015-12-10/DisassociateBudgetFromResource.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/servicecatalog-2015-12-10/DisassociateBudgetFromResource.md "../../../goto/SdkForRubyV3/servicecatalog-2015-12-10/DisassociateBudgetFromResource.md")
