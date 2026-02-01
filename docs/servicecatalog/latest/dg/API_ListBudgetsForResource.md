# ListBudgetsForResource

Lists all the budgets associated to the specified resource.

## Request Syntax

```
{
   "AcceptLanguage": "`string`",
   "PageSize": `number`,
   "PageToken": "`string`",
   "ResourceId": "`string`"
}
```

## Request Parameters

The request accepts the following data in JSON format.

**[AcceptLanguage](#API_ListBudgetsForResource_RequestSyntax "#API_ListBudgetsForResource_RequestSyntax")**

The language code.

- `jp` - Japanese
- `zh` - Chinese

Type: String

Length Constraints: Maximum length of 100.

Required: No

**[PageSize](#API_ListBudgetsForResource_RequestSyntax "#API_ListBudgetsForResource_RequestSyntax")**

The maximum number of items to return with this call.

Type: Integer

Valid Range: Minimum value of 0. Maximum value of 20.

Required: No

**[PageToken](#API_ListBudgetsForResource_RequestSyntax "#API_ListBudgetsForResource_RequestSyntax")**

The page token for the next set of results. To retrieve the first set of results, use null.

Type: String

Length Constraints: Maximum length of 2024.

Pattern: `[\u0009\u000a\u000d\u0020-\uD7FF\uE000-\uFFFD]*`

Required: No

**[ResourceId](#API_ListBudgetsForResource_RequestSyntax "#API_ListBudgetsForResource_RequestSyntax")**

The resource identifier.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 100.

Pattern: `^[a-zA-Z0-9_\-]*`

Required: Yes

## Response Syntax

```
{
   "Budgets": [
      {
         "BudgetName": "***string***"
      }
   ],
   "NextPageToken": "***string***"
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[Budgets](#API_ListBudgetsForResource_ResponseSyntax "#API_ListBudgetsForResource_ResponseSyntax")**

Information about the associated budgets.

Type: Array of [BudgetDetail](API_BudgetDetail.md "API_BudgetDetail.md") objects

**[NextPageToken](#API_ListBudgetsForResource_ResponseSyntax "#API_ListBudgetsForResource_ResponseSyntax")**

The page token to use to retrieve the next set of results. If there are no additional results, this value is null.

Type: String

Length Constraints: Maximum length of 2024.

Pattern: `[\u0009\u000a\u000d\u0020-\uD7FF\uE000-\uFFFD]*`

## Errors

**InvalidParametersException**

One or more parameters provided to the operation are not valid.

HTTP Status Code: 400

**ResourceNotFoundException**

The specified resource was not found.

HTTP Status Code: 400

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/servicecatalog-2015-12-10/ListBudgetsForResource.md "../../../goto/cli2/servicecatalog-2015-12-10/ListBudgetsForResource.md")
- [AWS SDK for .NET V4](../../../goto/DotNetSDKV4/servicecatalog-2015-12-10/ListBudgetsForResource.md "../../../goto/DotNetSDKV4/servicecatalog-2015-12-10/ListBudgetsForResource.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/servicecatalog-2015-12-10/ListBudgetsForResource.md "../../../goto/SdkForCpp/servicecatalog-2015-12-10/ListBudgetsForResource.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/servicecatalog-2015-12-10/ListBudgetsForResource.md "../../../goto/SdkForGoV2/servicecatalog-2015-12-10/ListBudgetsForResource.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/servicecatalog-2015-12-10/ListBudgetsForResource.md "../../../goto/SdkForJavaV2/servicecatalog-2015-12-10/ListBudgetsForResource.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/servicecatalog-2015-12-10/ListBudgetsForResource.md "../../../goto/SdkForJavaScriptV3/servicecatalog-2015-12-10/ListBudgetsForResource.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/servicecatalog-2015-12-10/ListBudgetsForResource.md "../../../goto/SdkForKotlin/servicecatalog-2015-12-10/ListBudgetsForResource.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/servicecatalog-2015-12-10/ListBudgetsForResource.md "../../../goto/SdkForPHPV3/servicecatalog-2015-12-10/ListBudgetsForResource.md")
- [AWS SDK for Python](../../../goto/boto3/servicecatalog-2015-12-10/ListBudgetsForResource.md "../../../goto/boto3/servicecatalog-2015-12-10/ListBudgetsForResource.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/servicecatalog-2015-12-10/ListBudgetsForResource.md "../../../goto/SdkForRubyV3/servicecatalog-2015-12-10/ListBudgetsForResource.md")
