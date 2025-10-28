# ListDatasetGroups

Returns a list of dataset groups. The response provides the properties
for each dataset group, including the Amazon Resource Name (ARN). For more
information on dataset groups, see [CreateDatasetGroup](API_CreateDatasetGroup.md "API_CreateDatasetGroup.md").

## Request Syntax

```
{
   "maxResults": `number`,
   "nextToken": "`string`"
}
```

## Request Parameters

The request accepts the following data in JSON format.

**[maxResults](#API_ListDatasetGroups_RequestSyntax "#API_ListDatasetGroups_RequestSyntax")**

The maximum number of dataset groups to return.

Type: Integer

Valid Range: Minimum value of 1. Maximum value of 100.

Required: No

**[nextToken](#API_ListDatasetGroups_RequestSyntax "#API_ListDatasetGroups_RequestSyntax")**

A token returned from the previous call to
`ListDatasetGroups` for getting the next set of dataset
groups (if they exist).

Type: String

Length Constraints: Maximum length of 1500.

Pattern: `\p{ASCII}{0,1500}`

Required: No

## Response Syntax

```
{
   "datasetGroups": [
      {
         "creationDateTime": ***number***,
         "datasetGroupArn": "***string***",
         "domain": "***string***",
         "failureReason": "***string***",
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

**[datasetGroups](#API_ListDatasetGroups_ResponseSyntax "#API_ListDatasetGroups_ResponseSyntax")**

The list of your dataset groups.

Type: Array of [DatasetGroupSummary](API_DatasetGroupSummary.md "API_DatasetGroupSummary.md") objects

Array Members: Maximum number of 100 items.

**[nextToken](#API_ListDatasetGroups_ResponseSyntax "#API_ListDatasetGroups_ResponseSyntax")**

A token for getting the next set of dataset groups (if they
exist).

Type: String

Length Constraints: Maximum length of 1500.

Pattern: `\p{ASCII}{0,1500}`

## Errors

**InvalidNextTokenException**

The token is not valid.

HTTP Status Code: 400

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/personalize-2018-05-22/ListDatasetGroups.md "../../../goto/cli2/personalize-2018-05-22/ListDatasetGroups.md")
- [AWS SDK for .NET](../../../goto/DotNetSDKV3/personalize-2018-05-22/ListDatasetGroups.md "../../../goto/DotNetSDKV3/personalize-2018-05-22/ListDatasetGroups.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/personalize-2018-05-22/ListDatasetGroups.md "../../../goto/SdkForCpp/personalize-2018-05-22/ListDatasetGroups.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/personalize-2018-05-22/ListDatasetGroups.md "../../../goto/SdkForGoV2/personalize-2018-05-22/ListDatasetGroups.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/personalize-2018-05-22/ListDatasetGroups.md "../../../goto/SdkForJavaV2/personalize-2018-05-22/ListDatasetGroups.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/personalize-2018-05-22/ListDatasetGroups.md "../../../goto/SdkForJavaScriptV3/personalize-2018-05-22/ListDatasetGroups.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/personalize-2018-05-22/ListDatasetGroups.md "../../../goto/SdkForKotlin/personalize-2018-05-22/ListDatasetGroups.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/personalize-2018-05-22/ListDatasetGroups.md "../../../goto/SdkForPHPV3/personalize-2018-05-22/ListDatasetGroups.md")
- [AWS SDK for Python](../../../goto/boto3/personalize-2018-05-22/ListDatasetGroups.md "../../../goto/boto3/personalize-2018-05-22/ListDatasetGroups.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/personalize-2018-05-22/ListDatasetGroups.md "../../../goto/SdkForRubyV3/personalize-2018-05-22/ListDatasetGroups.md")
