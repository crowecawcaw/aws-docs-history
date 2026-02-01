# ListLaunchPaths

Lists the paths
to the specified product.
A path describes
how the user
gets access
to a specified product
and is necessary
when provisioning a product.
A path also determines the constraints
that are put on a product.
A path is dependent
on a specific product, porfolio, and principal.

###### Note

When provisioning a product
that's been added
to a portfolio,
you must grant your user, group, or role access
to the portfolio.
For more information,
see [Granting users access](../adminguide/catalogs_portfolios_users.md "../adminguide/catalogs_portfolios_users.md")
in the _Service Catalog User Guide_.

## Request Syntax

```
{
   "AcceptLanguage": "`string`",
   "PageSize": `number`,
   "PageToken": "`string`",
   "ProductId": "`string`"
}
```

## Request Parameters

The request accepts the following data in JSON format.

**[AcceptLanguage](#API_ListLaunchPaths_RequestSyntax "#API_ListLaunchPaths_RequestSyntax")**

The language code.

- `jp` - Japanese
- `zh` - Chinese

Type: String

Length Constraints: Maximum length of 100.

Required: No

**[PageSize](#API_ListLaunchPaths_RequestSyntax "#API_ListLaunchPaths_RequestSyntax")**

The maximum number of items to return with this call.

Type: Integer

Valid Range: Minimum value of 0. Maximum value of 20.

Required: No

**[PageToken](#API_ListLaunchPaths_RequestSyntax "#API_ListLaunchPaths_RequestSyntax")**

The page token for the next set of results. To retrieve the first set of results, use null.

Type: String

Length Constraints: Maximum length of 2024.

Pattern: `[\u0009\u000a\u000d\u0020-\uD7FF\uE000-\uFFFD]*`

Required: No

**[ProductId](#API_ListLaunchPaths_RequestSyntax "#API_ListLaunchPaths_RequestSyntax")**

The product identifier.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 100.

Pattern: `^[a-zA-Z0-9_\-]*`

Required: Yes

## Response Syntax

```
{
   "LaunchPathSummaries": [
      {
         "ConstraintSummaries": [
            {
               "Description": "***string***",
               "Type": "***string***"
            }
         ],
         "Id": "***string***",
         "Name": "***string***",
         "Tags": [
            {
               "Key": "***string***",
               "Value": "***string***"
            }
         ]
      }
   ],
   "NextPageToken": "***string***"
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[LaunchPathSummaries](#API_ListLaunchPaths_ResponseSyntax "#API_ListLaunchPaths_ResponseSyntax")**

Information about the launch path.

Type: Array of [LaunchPathSummary](API_LaunchPathSummary.md "API_LaunchPathSummary.md") objects

**[NextPageToken](#API_ListLaunchPaths_ResponseSyntax "#API_ListLaunchPaths_ResponseSyntax")**

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

- [AWS Command Line Interface V2](../../../goto/cli2/servicecatalog-2015-12-10/ListLaunchPaths.md "../../../goto/cli2/servicecatalog-2015-12-10/ListLaunchPaths.md")
- [AWS SDK for .NET V4](../../../goto/DotNetSDKV4/servicecatalog-2015-12-10/ListLaunchPaths.md "../../../goto/DotNetSDKV4/servicecatalog-2015-12-10/ListLaunchPaths.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/servicecatalog-2015-12-10/ListLaunchPaths.md "../../../goto/SdkForCpp/servicecatalog-2015-12-10/ListLaunchPaths.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/servicecatalog-2015-12-10/ListLaunchPaths.md "../../../goto/SdkForGoV2/servicecatalog-2015-12-10/ListLaunchPaths.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/servicecatalog-2015-12-10/ListLaunchPaths.md "../../../goto/SdkForJavaV2/servicecatalog-2015-12-10/ListLaunchPaths.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/servicecatalog-2015-12-10/ListLaunchPaths.md "../../../goto/SdkForJavaScriptV3/servicecatalog-2015-12-10/ListLaunchPaths.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/servicecatalog-2015-12-10/ListLaunchPaths.md "../../../goto/SdkForKotlin/servicecatalog-2015-12-10/ListLaunchPaths.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/servicecatalog-2015-12-10/ListLaunchPaths.md "../../../goto/SdkForPHPV3/servicecatalog-2015-12-10/ListLaunchPaths.md")
- [AWS SDK for Python](../../../goto/boto3/servicecatalog-2015-12-10/ListLaunchPaths.md "../../../goto/boto3/servicecatalog-2015-12-10/ListLaunchPaths.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/servicecatalog-2015-12-10/ListLaunchPaths.md "../../../goto/SdkForRubyV3/servicecatalog-2015-12-10/ListLaunchPaths.md")
