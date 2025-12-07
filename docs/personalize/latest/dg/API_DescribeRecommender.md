# DescribeRecommender

Describes the given recommender, including its status.

A recommender can be in one of the following states:

- CREATE PENDING > CREATE IN_PROGRESS > ACTIVE -or- CREATE FAILED
- STOP PENDING > STOP IN_PROGRESS > INACTIVE > START PENDING > START IN_PROGRESS > ACTIVE
- DELETE PENDING > DELETE IN_PROGRESS
  When the `status` is `CREATE FAILED`, the response includes the
  `failureReason` key, which describes why.

The `modelMetrics` key is null when
the recommender is being created or deleted.

For more information on recommenders, see [CreateRecommender](API_CreateRecommender.md "API_CreateRecommender.md").

## Request Syntax

```
{
   "recommenderArn": "`string`"
}
```

## Request Parameters

The request accepts the following data in JSON format.

**[recommenderArn](#API_DescribeRecommender_RequestSyntax "#API_DescribeRecommender_RequestSyntax")**

The Amazon Resource Name (ARN) of the recommender to describe.

Type: String

Length Constraints: Maximum length of 256.

Pattern: `arn:([a-z\d-]+):personalize:.*:.*:.+`

Required: Yes

## Response Syntax

```
{
   "recommender": {
      "creationDateTime": ***number***,
      "datasetGroupArn": "***string***",
      "failureReason": "***string***",
      "lastUpdatedDateTime": ***number***,
      "latestRecommenderUpdate": {
         "creationDateTime": ***number***,
         "failureReason": "***string***",
         "lastUpdatedDateTime": ***number***,
         "recommenderConfig": {
            "enableMetadataWithRecommendations": ***boolean***,
            "itemExplorationConfig": {
               "***string***" : "***string***"
            },
            "minRecommendationRequestsPerSecond": ***number***,
            "trainingDataConfig": {
               "excludedDatasetColumns": {
                  "***string***" : [ "***string***" ]
               },
               "includedDatasetColumns": {
                  "***string***" : [ "***string***" ]
               }
            }
         },
         "status": "***string***"
      },
      "modelMetrics": {
         "***string***" : ***number***
      },
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
            },
            "includedDatasetColumns": {
               "***string***" : [ "***string***" ]
            }
         }
      },
      "status": "***string***"
   }
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[recommender](#API_DescribeRecommender_ResponseSyntax "#API_DescribeRecommender_ResponseSyntax")**

The properties of the recommender.

Type: [Recommender](API_Recommender.md "API_Recommender.md") object

## Errors

**InvalidInputException**

Provide a valid value for the field or parameter.

HTTP Status Code: 400

**ResourceNotFoundException**

Could not find the specified resource.

HTTP Status Code: 400

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/personalize-2018-05-22/DescribeRecommender.md "../../../goto/cli2/personalize-2018-05-22/DescribeRecommender.md")
- [AWS SDK for .NET](../../../goto/DotNetSDKV3/personalize-2018-05-22/DescribeRecommender.md "../../../goto/DotNetSDKV3/personalize-2018-05-22/DescribeRecommender.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/personalize-2018-05-22/DescribeRecommender.md "../../../goto/SdkForCpp/personalize-2018-05-22/DescribeRecommender.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/personalize-2018-05-22/DescribeRecommender.md "../../../goto/SdkForGoV2/personalize-2018-05-22/DescribeRecommender.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/personalize-2018-05-22/DescribeRecommender.md "../../../goto/SdkForJavaV2/personalize-2018-05-22/DescribeRecommender.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/personalize-2018-05-22/DescribeRecommender.md "../../../goto/SdkForJavaScriptV3/personalize-2018-05-22/DescribeRecommender.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/personalize-2018-05-22/DescribeRecommender.md "../../../goto/SdkForKotlin/personalize-2018-05-22/DescribeRecommender.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/personalize-2018-05-22/DescribeRecommender.md "../../../goto/SdkForPHPV3/personalize-2018-05-22/DescribeRecommender.md")
- [AWS SDK for Python](../../../goto/boto3/personalize-2018-05-22/DescribeRecommender.md "../../../goto/boto3/personalize-2018-05-22/DescribeRecommender.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/personalize-2018-05-22/DescribeRecommender.md "../../../goto/SdkForRubyV3/personalize-2018-05-22/DescribeRecommender.md")
