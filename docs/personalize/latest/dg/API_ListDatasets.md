# ListDatasets

Returns the list of datasets contained in the given dataset group. The
response provides the properties for each dataset, including the Amazon
Resource Name (ARN). For more information on datasets, see [CreateDataset](API_CreateDataset.md "API_CreateDataset.md").

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

**[datasetGroupArn](#API_ListDatasets_RequestSyntax "#API_ListDatasets_RequestSyntax")**

The Amazon Resource Name (ARN) of the dataset group that contains the
datasets to list.

Type: String

Length Constraints: Maximum length of 256.

Pattern: `arn:([a-z\d-]+):personalize:.*:.*:.+`

Required: No

**[maxResults](#API_ListDatasets_RequestSyntax "#API_ListDatasets_RequestSyntax")**

The maximum number of datasets to return.

Type: Integer

Valid Range: Minimum value of 1. Maximum value of 100.

Required: No

**[nextToken](#API_ListDatasets_RequestSyntax "#API_ListDatasets_RequestSyntax")**

A token returned from the previous call to
`ListDatasets` for getting the next set of dataset
import jobs (if they exist).

Type: String

Length Constraints: Maximum length of 1500.

Pattern: `\p{ASCII}{0,1500}`

Required: No

## Response Syntax

```
{
   "datasets": [
      {
         "creationDateTime": ***number***,
         "datasetArn": "***string***",
         "datasetType": "***string***",
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

**[datasets](#API_ListDatasets_ResponseSyntax "#API_ListDatasets_ResponseSyntax")**

An array of `Dataset` objects. Each object provides
metadata information.

Type: Array of [DatasetSummary](API_DatasetSummary.md "API_DatasetSummary.md") objects

Array Members: Maximum number of 100 items.

**[nextToken](#API_ListDatasets_ResponseSyntax "#API_ListDatasets_ResponseSyntax")**

A token for getting the next set of datasets (if they exist).

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

- [AWS Command Line Interface V2](../../../goto/cli2/personalize-2018-05-22/ListDatasets.md "../../../goto/cli2/personalize-2018-05-22/ListDatasets.md")
- [AWS SDK for .NET](../../../goto/DotNetSDKV3/personalize-2018-05-22/ListDatasets.md "../../../goto/DotNetSDKV3/personalize-2018-05-22/ListDatasets.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/personalize-2018-05-22/ListDatasets.md "../../../goto/SdkForCpp/personalize-2018-05-22/ListDatasets.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/personalize-2018-05-22/ListDatasets.md "../../../goto/SdkForGoV2/personalize-2018-05-22/ListDatasets.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/personalize-2018-05-22/ListDatasets.md "../../../goto/SdkForJavaV2/personalize-2018-05-22/ListDatasets.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/personalize-2018-05-22/ListDatasets.md "../../../goto/SdkForJavaScriptV3/personalize-2018-05-22/ListDatasets.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/personalize-2018-05-22/ListDatasets.md "../../../goto/SdkForKotlin/personalize-2018-05-22/ListDatasets.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/personalize-2018-05-22/ListDatasets.md "../../../goto/SdkForPHPV3/personalize-2018-05-22/ListDatasets.md")
- [AWS SDK for Python](../../../goto/boto3/personalize-2018-05-22/ListDatasets.md "../../../goto/boto3/personalize-2018-05-22/ListDatasets.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/personalize-2018-05-22/ListDatasets.md "../../../goto/SdkForRubyV3/personalize-2018-05-22/ListDatasets.md")
