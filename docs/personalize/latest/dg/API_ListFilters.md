# ListFilters

Lists all filters that belong to a given dataset group.

## Request Syntax

```
{
   "datasetGroupArn": "`string`",
   "maxResults": `number`,
   "nextToken": "`string`"
}
```

## Request Parameters

The request accepts the following data in JSON format.

**[datasetGroupArn](#API_ListFilters_RequestSyntax "#API_ListFilters_RequestSyntax")**

The ARN of the dataset group that contains the filters.

Type: String

Length Constraints: Maximum length of 256.

Pattern: `arn:([a-z\d-]+):personalize:.*:.*:.+`

Required: No

**[maxResults](#API_ListFilters_RequestSyntax "#API_ListFilters_RequestSyntax")**

The maximum number of filters to return.

Type: Integer

Valid Range: Minimum value of 1. Maximum value of 100.

Required: No

**[nextToken](#API_ListFilters_RequestSyntax "#API_ListFilters_RequestSyntax")**

A token returned from the previous call to `ListFilters` for getting the
next set of filters (if they exist).

Type: String

Length Constraints: Maximum length of 1500.

Pattern: `\p{ASCII}{0,1500}`

Required: No

## Response Syntax

```
{
   "Filters": [
      {
         "creationDateTime": ***number***,
         "datasetGroupArn": "***string***",
         "failureReason": "***string***",
         "filterArn": "***string***",
         "lastUpdatedDateTime": ***number***,
         "name": "***string***",
         "status": "***string***"
      }
   ],
   "nextToken": "***string***"
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[Filters](#API_ListFilters_ResponseSyntax "#API_ListFilters_ResponseSyntax")**

A list of returned filters.

Type: Array of [FilterSummary](API_FilterSummary.md "API_FilterSummary.md") objects

Array Members: Maximum number of 100 items.

**[nextToken](#API_ListFilters_ResponseSyntax "#API_ListFilters_ResponseSyntax")**

A token for getting the next set of filters (if they exist).

Type: String

Length Constraints: Maximum length of 1500.

Pattern: `\p{ASCII}{0,1500}`

## Errors

**InvalidInputException**

Provide a valid value for the field or parameter.

HTTP Status Code: 400

**InvalidNextTokenException**

The token is not valid.

HTTP Status Code: 400

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/personalize-2018-05-22/ListFilters.md "../../../goto/cli2/personalize-2018-05-22/ListFilters.md")
- [AWS SDK for .NET](../../../goto/DotNetSDKV3/personalize-2018-05-22/ListFilters.md "../../../goto/DotNetSDKV3/personalize-2018-05-22/ListFilters.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/personalize-2018-05-22/ListFilters.md "../../../goto/SdkForCpp/personalize-2018-05-22/ListFilters.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/personalize-2018-05-22/ListFilters.md "../../../goto/SdkForGoV2/personalize-2018-05-22/ListFilters.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/personalize-2018-05-22/ListFilters.md "../../../goto/SdkForJavaV2/personalize-2018-05-22/ListFilters.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/personalize-2018-05-22/ListFilters.md "../../../goto/SdkForJavaScriptV3/personalize-2018-05-22/ListFilters.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/personalize-2018-05-22/ListFilters.md "../../../goto/SdkForKotlin/personalize-2018-05-22/ListFilters.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/personalize-2018-05-22/ListFilters.md "../../../goto/SdkForPHPV3/personalize-2018-05-22/ListFilters.md")
- [AWS SDK for Python](../../../goto/boto3/personalize-2018-05-22/ListFilters.md "../../../goto/boto3/personalize-2018-05-22/ListFilters.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/personalize-2018-05-22/ListFilters.md "../../../goto/SdkForRubyV3/personalize-2018-05-22/ListFilters.md")
