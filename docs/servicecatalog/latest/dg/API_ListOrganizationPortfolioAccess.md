# ListOrganizationPortfolioAccess

Lists the organization nodes that have access to the specified portfolio. This API can
only be called by the management account in the organization or by a delegated
admin.

If a delegated admin is de-registered, they can no longer perform this operation.

## Request Syntax

```
{
   "AcceptLanguage": "`string`",
   "OrganizationNodeType": "`string`",
   "PageSize": `number`,
   "PageToken": "`string`",
   "PortfolioId": "`string`"
}
```

## Request Parameters

The request accepts the following data in JSON format.

**[AcceptLanguage](#API_ListOrganizationPortfolioAccess_RequestSyntax "#API_ListOrganizationPortfolioAccess_RequestSyntax")**

The language code.

- `jp` - Japanese
- `zh` - Chinese

Type: String

Length Constraints: Maximum length of 100.

Required: No

**[OrganizationNodeType](#API_ListOrganizationPortfolioAccess_RequestSyntax "#API_ListOrganizationPortfolioAccess_RequestSyntax")**

The organization node type that will be returned in the output.

- `ORGANIZATION` - Organization that has access to the portfolio.
- `ORGANIZATIONAL_UNIT` - Organizational unit that has access to the portfolio within your organization.
- `ACCOUNT` - Account that has access to the portfolio within your organization.

Type: String

Valid Values: `ORGANIZATION | ORGANIZATIONAL_UNIT | ACCOUNT`

Required: Yes

**[PageSize](#API_ListOrganizationPortfolioAccess_RequestSyntax "#API_ListOrganizationPortfolioAccess_RequestSyntax")**

The maximum number of items to return with this call.

Type: Integer

Valid Range: Minimum value of 0. Maximum value of 20.

Required: No

**[PageToken](#API_ListOrganizationPortfolioAccess_RequestSyntax "#API_ListOrganizationPortfolioAccess_RequestSyntax")**

The page token for the next set of results. To retrieve the first set of results, use null.

Type: String

Length Constraints: Maximum length of 2024.

Pattern: `[\u0009\u000a\u000d\u0020-\uD7FF\uE000-\uFFFD]*`

Required: No

**[PortfolioId](#API_ListOrganizationPortfolioAccess_RequestSyntax "#API_ListOrganizationPortfolioAccess_RequestSyntax")**

The portfolio identifier. For example, `port-2abcdext3y5fk`.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 100.

Pattern: `^[a-zA-Z0-9_\-]*`

Required: Yes

## Response Syntax

```
{
   "NextPageToken": "***string***",
   "OrganizationNodes": [
      {
         "Type": "***string***",
         "Value": "***string***"
      }
   ]
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[NextPageToken](#API_ListOrganizationPortfolioAccess_ResponseSyntax "#API_ListOrganizationPortfolioAccess_ResponseSyntax")**

The page token to use to retrieve the next set of results. If there are no additional results, this value is null.

Type: String

Length Constraints: Maximum length of 2024.

Pattern: `[\u0009\u000a\u000d\u0020-\uD7FF\uE000-\uFFFD]*`

**[OrganizationNodes](#API_ListOrganizationPortfolioAccess_ResponseSyntax "#API_ListOrganizationPortfolioAccess_ResponseSyntax")**

Displays information about the organization nodes.

Type: Array of [OrganizationNode](API_OrganizationNode.md "API_OrganizationNode.md") objects

## Errors

**InvalidParametersException**

One or more parameters provided to the operation are not valid.

HTTP Status Code: 400

**OperationNotSupportedException**

The operation is not supported.

HTTP Status Code: 400

**ResourceNotFoundException**

The specified resource was not found.

HTTP Status Code: 400

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/servicecatalog-2015-12-10/ListOrganizationPortfolioAccess.md "../../../goto/cli2/servicecatalog-2015-12-10/ListOrganizationPortfolioAccess.md")
- [AWS SDK for .NET V4](../../../goto/DotNetSDKV4/servicecatalog-2015-12-10/ListOrganizationPortfolioAccess.md "../../../goto/DotNetSDKV4/servicecatalog-2015-12-10/ListOrganizationPortfolioAccess.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/servicecatalog-2015-12-10/ListOrganizationPortfolioAccess.md "../../../goto/SdkForCpp/servicecatalog-2015-12-10/ListOrganizationPortfolioAccess.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/servicecatalog-2015-12-10/ListOrganizationPortfolioAccess.md "../../../goto/SdkForGoV2/servicecatalog-2015-12-10/ListOrganizationPortfolioAccess.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/servicecatalog-2015-12-10/ListOrganizationPortfolioAccess.md "../../../goto/SdkForJavaV2/servicecatalog-2015-12-10/ListOrganizationPortfolioAccess.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/servicecatalog-2015-12-10/ListOrganizationPortfolioAccess.md "../../../goto/SdkForJavaScriptV3/servicecatalog-2015-12-10/ListOrganizationPortfolioAccess.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/servicecatalog-2015-12-10/ListOrganizationPortfolioAccess.md "../../../goto/SdkForKotlin/servicecatalog-2015-12-10/ListOrganizationPortfolioAccess.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/servicecatalog-2015-12-10/ListOrganizationPortfolioAccess.md "../../../goto/SdkForPHPV3/servicecatalog-2015-12-10/ListOrganizationPortfolioAccess.md")
- [AWS SDK for Python](../../../goto/boto3/servicecatalog-2015-12-10/ListOrganizationPortfolioAccess.md "../../../goto/boto3/servicecatalog-2015-12-10/ListOrganizationPortfolioAccess.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/servicecatalog-2015-12-10/ListOrganizationPortfolioAccess.md "../../../goto/SdkForRubyV3/servicecatalog-2015-12-10/ListOrganizationPortfolioAccess.md")
