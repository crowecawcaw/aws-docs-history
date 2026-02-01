# AssociateBudgetWithResource

Associates the specified budget with the specified resource.

## Request Syntax

```
{
   "BudgetName": "`string`",
   "ResourceId": "`string`"
}
```

## Request Parameters

The request accepts the following data in JSON format.

**[BudgetName](#API_AssociateBudgetWithResource_RequestSyntax "#API_AssociateBudgetWithResource_RequestSyntax")**

The name of the budget you want to associate.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 100.

Required: Yes

**[ResourceId](#API_AssociateBudgetWithResource_RequestSyntax "#API_AssociateBudgetWithResource_RequestSyntax")**

The resource identifier. Either a portfolio-id or a product-id.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 100.

Pattern: `^[a-zA-Z0-9_\-]*`

Required: Yes

## Response Elements

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors

**DuplicateResourceException**

The specified resource is a duplicate.

HTTP Status Code: 400

**InvalidParametersException**

One or more parameters provided to the operation are not valid.

HTTP Status Code: 400

**LimitExceededException**

The current limits of the service would have been exceeded by this operation. Decrease your
resource use or increase your service limits and retry the operation.

HTTP Status Code: 400

**ResourceNotFoundException**

The specified resource was not found.

HTTP Status Code: 400

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/servicecatalog-2015-12-10/AssociateBudgetWithResource.md "../../../goto/cli2/servicecatalog-2015-12-10/AssociateBudgetWithResource.md")
- [AWS SDK for .NET V4](../../../goto/DotNetSDKV4/servicecatalog-2015-12-10/AssociateBudgetWithResource.md "../../../goto/DotNetSDKV4/servicecatalog-2015-12-10/AssociateBudgetWithResource.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/servicecatalog-2015-12-10/AssociateBudgetWithResource.md "../../../goto/SdkForCpp/servicecatalog-2015-12-10/AssociateBudgetWithResource.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/servicecatalog-2015-12-10/AssociateBudgetWithResource.md "../../../goto/SdkForGoV2/servicecatalog-2015-12-10/AssociateBudgetWithResource.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/servicecatalog-2015-12-10/AssociateBudgetWithResource.md "../../../goto/SdkForJavaV2/servicecatalog-2015-12-10/AssociateBudgetWithResource.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/servicecatalog-2015-12-10/AssociateBudgetWithResource.md "../../../goto/SdkForJavaScriptV3/servicecatalog-2015-12-10/AssociateBudgetWithResource.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/servicecatalog-2015-12-10/AssociateBudgetWithResource.md "../../../goto/SdkForKotlin/servicecatalog-2015-12-10/AssociateBudgetWithResource.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/servicecatalog-2015-12-10/AssociateBudgetWithResource.md "../../../goto/SdkForPHPV3/servicecatalog-2015-12-10/AssociateBudgetWithResource.md")
- [AWS SDK for Python](../../../goto/boto3/servicecatalog-2015-12-10/AssociateBudgetWithResource.md "../../../goto/boto3/servicecatalog-2015-12-10/AssociateBudgetWithResource.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/servicecatalog-2015-12-10/AssociateBudgetWithResource.md "../../../goto/SdkForRubyV3/servicecatalog-2015-12-10/AssociateBudgetWithResource.md")
