# ListTagOptions

Lists the specified TagOptions or all TagOptions.

## Request Syntax

```
{
   "Filters": {
      "Active": `boolean`,
      "Key": "`string`",
      "Value": "`string`"
   },
   "PageSize": `number`,
   "PageToken": "`string`"
}
```

## Request Parameters

The request accepts the following data in JSON format.

**[Filters](#API_ListTagOptions_RequestSyntax "#API_ListTagOptions_RequestSyntax")**

The search filters. If no search filters are specified, the output includes all TagOptions.

Type: [ListTagOptionsFilters](API_ListTagOptionsFilters.md "API_ListTagOptionsFilters.md") object

Required: No

**[PageSize](#API_ListTagOptions_RequestSyntax "#API_ListTagOptions_RequestSyntax")**

The maximum number of items to return with this call.

Type: Integer

Valid Range: Minimum value of 0. Maximum value of 20.

Required: No

**[PageToken](#API_ListTagOptions_RequestSyntax "#API_ListTagOptions_RequestSyntax")**

The page token for the next set of results. To retrieve the first set of results, use null.

Type: String

Length Constraints: Maximum length of 2024.

Pattern: `[\u0009\u000a\u000d\u0020-\uD7FF\uE000-\uFFFD]*`

Required: No

## Response Syntax

```
{
   "PageToken": "***string***",
   "TagOptionDetails": [
      {
         "Active": ***boolean***,
         "Id": "***string***",
         "Key": "***string***",
         "Owner": "***string***",
         "Value": "***string***"
      }
   ]
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[PageToken](#API_ListTagOptions_ResponseSyntax "#API_ListTagOptions_ResponseSyntax")**

The page token for the next set of results. To retrieve the first set of results, use null.

Type: String

Length Constraints: Maximum length of 2024.

Pattern: `[\u0009\u000a\u000d\u0020-\uD7FF\uE000-\uFFFD]*`

**[TagOptionDetails](#API_ListTagOptions_ResponseSyntax "#API_ListTagOptions_ResponseSyntax")**

Information about the TagOptions.

Type: Array of [TagOptionDetail](API_TagOptionDetail.md "API_TagOptionDetail.md") objects

## Errors

**InvalidParametersException**

One or more parameters provided to the operation are not valid.

HTTP Status Code: 400

**TagOptionNotMigratedException**

An operation requiring TagOptions failed because the TagOptions migration process has
not been performed for this account. Use the AWS Management Console to perform the migration
process before retrying the operation.

HTTP Status Code: 400

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/servicecatalog-2015-12-10/ListTagOptions.md "../../../goto/cli2/servicecatalog-2015-12-10/ListTagOptions.md")
- [AWS SDK for .NET](../../../goto/DotNetSDKV3/servicecatalog-2015-12-10/ListTagOptions.md "../../../goto/DotNetSDKV3/servicecatalog-2015-12-10/ListTagOptions.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/servicecatalog-2015-12-10/ListTagOptions.md "../../../goto/SdkForCpp/servicecatalog-2015-12-10/ListTagOptions.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/servicecatalog-2015-12-10/ListTagOptions.md "../../../goto/SdkForGoV2/servicecatalog-2015-12-10/ListTagOptions.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/servicecatalog-2015-12-10/ListTagOptions.md "../../../goto/SdkForJavaV2/servicecatalog-2015-12-10/ListTagOptions.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/servicecatalog-2015-12-10/ListTagOptions.md "../../../goto/SdkForJavaScriptV3/servicecatalog-2015-12-10/ListTagOptions.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/servicecatalog-2015-12-10/ListTagOptions.md "../../../goto/SdkForKotlin/servicecatalog-2015-12-10/ListTagOptions.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/servicecatalog-2015-12-10/ListTagOptions.md "../../../goto/SdkForPHPV3/servicecatalog-2015-12-10/ListTagOptions.md")
- [AWS SDK for Python](../../../goto/boto3/servicecatalog-2015-12-10/ListTagOptions.md "../../../goto/boto3/servicecatalog-2015-12-10/ListTagOptions.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/servicecatalog-2015-12-10/ListTagOptions.md "../../../goto/SdkForRubyV3/servicecatalog-2015-12-10/ListTagOptions.md")
