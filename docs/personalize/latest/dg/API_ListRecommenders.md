# ListRecommenders

Returns a list of recommenders in a given Domain dataset group.
When a Domain dataset group is not specified, all the recommenders associated with the account are listed.
The response provides the properties for each recommender, including the Amazon Resource Name (ARN).
For more information on recommenders, see [CreateRecommender](API_CreateRecommender.md "API_CreateRecommender.md").

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

**[datasetGroupArn](#API_ListRecommenders_RequestSyntax "#API_ListRecommenders_RequestSyntax")**

The Amazon Resource Name (ARN) of the Domain dataset group to list the recommenders for. When
a Domain dataset group is not specified, all the recommenders associated with the account are listed.

Type: String

Length Constraints: Maximum length of 256.

Pattern: `arn:([a-z\d-]+):personalize:.*:.*:.+`

Required: No

**[maxResults](#API_ListRecommenders_RequestSyntax "#API_ListRecommenders_RequestSyntax")**

The maximum number of recommenders to return.

Type: Integer

Valid Range: Minimum value of 1. Maximum value of 100.

Required: No

**[nextToken](#API_ListRecommenders_RequestSyntax "#API_ListRecommenders_RequestSyntax")**

A token returned from the previous call to `ListRecommenders` for getting
the next set of recommenders (if they exist).

Type: String

Length Constraints: Maximum length of 1500.

Pattern: `\p{ASCII}{0,1500}`

Required: No

## Response Syntax

```
{
   "nextToken": "***string***",
   "recommenders": [
      {
         "creationDateTime": ***number***,
         "datasetGroupArn": "***string***",
         "lastUpdatedDateTime": ***number***,
         "name": "***string***",
         "recipeArn": "***string***",
         "recommenderArn": "***string***",
         "recommenderConfig": {
            "enableMetadataWithRecommendations": ***boolean***,
            "itemExplorationConfig": {
               "***string***" : "***string***"
            },
            "minRecommendationRequestsPerSecond": ***number***,
            "trainingDataConfig": {
               "excludedDatasetColumns": {
                  "***string***" : [ "***string***" ]
               }
            }
         },
         "status": "***string***"
      }
   ]
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[nextToken](#API_ListRecommenders_ResponseSyntax "#API_ListRecommenders_ResponseSyntax")**

A token for getting the next set of recommenders (if they exist).

Type: String

Length Constraints: Maximum length of 1500.

Pattern: `\p{ASCII}{0,1500}`

**[recommenders](#API_ListRecommenders_ResponseSyntax "#API_ListRecommenders_ResponseSyntax")**

A list of the recommenders.

Type: Array of [RecommenderSummary](API_RecommenderSummary.md "API_RecommenderSummary.md") objects

Array Members: Maximum number of 100 items.

## Errors

**InvalidInputException**

Provide a valid value for the field or parameter.

HTTP Status Code: 400

**InvalidNextTokenException**

The token is not valid.

HTTP Status Code: 400

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/personalize-2018-05-22/ListRecommenders.md "../../../goto/cli2/personalize-2018-05-22/ListRecommenders.md")
- [AWS SDK for .NET](../../../goto/DotNetSDKV3/personalize-2018-05-22/ListRecommenders.md "../../../goto/DotNetSDKV3/personalize-2018-05-22/ListRecommenders.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/personalize-2018-05-22/ListRecommenders.md "../../../goto/SdkForCpp/personalize-2018-05-22/ListRecommenders.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/personalize-2018-05-22/ListRecommenders.md "../../../goto/SdkForGoV2/personalize-2018-05-22/ListRecommenders.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/personalize-2018-05-22/ListRecommenders.md "../../../goto/SdkForJavaV2/personalize-2018-05-22/ListRecommenders.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/personalize-2018-05-22/ListRecommenders.md "../../../goto/SdkForJavaScriptV3/personalize-2018-05-22/ListRecommenders.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/personalize-2018-05-22/ListRecommenders.md "../../../goto/SdkForKotlin/personalize-2018-05-22/ListRecommenders.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/personalize-2018-05-22/ListRecommenders.md "../../../goto/SdkForPHPV3/personalize-2018-05-22/ListRecommenders.md")
- [AWS SDK for Python](../../../goto/boto3/personalize-2018-05-22/ListRecommenders.md "../../../goto/boto3/personalize-2018-05-22/ListRecommenders.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/personalize-2018-05-22/ListRecommenders.md "../../../goto/SdkForRubyV3/personalize-2018-05-22/ListRecommenders.md")
