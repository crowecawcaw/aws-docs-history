# CreateRecommender

Creates a recommender with the recipe (a Domain dataset group use case) you specify.
You create recommenders for a Domain dataset group and specify the recommender's Amazon Resource Name (ARN) when you make a
[GetRecommendations](API_RS_GetRecommendations.md "API_RS_GetRecommendations.md")
request.

**Minimum recommendation requests per second**

###### Important

A high `minRecommendationRequestsPerSecond` will increase your bill. We recommend starting with 1 for `minRecommendationRequestsPerSecond` (the default). Track
your usage using Amazon CloudWatch metrics, and increase the `minRecommendationRequestsPerSecond`
as necessary.

When you create a recommender, you can configure the recommender's minimum recommendation requests per second. The minimum recommendation requests per second
(`minRecommendationRequestsPerSecond`) specifies the baseline recommendation request throughput provisioned by
Amazon Personalize. The default minRecommendationRequestsPerSecond is `1`. A recommendation request is a single `GetRecommendations` operation.
Request throughput is measured in requests per second and Amazon Personalize uses your requests per second to derive
your requests per hour and the price of your recommender usage.

If your requests per second increases beyond
`minRecommendationRequestsPerSecond`, Amazon Personalize auto-scales the provisioned capacity up and down,
but never below `minRecommendationRequestsPerSecond`.
There's a short time delay while the capacity is increased that might cause loss of
requests.

Your bill is the greater of either the minimum requests per hour (based on minRecommendationRequestsPerSecond)
or the actual number of requests. The actual request throughput used is calculated as the average requests/second within a one-hour window.

We recommend starting with the default `minRecommendationRequestsPerSecond`, track
your usage using Amazon CloudWatch metrics, and then increase the `minRecommendationRequestsPerSecond`
as necessary.

**Status**

A recommender can be in one of the following states:

- CREATE PENDING > CREATE IN_PROGRESS > ACTIVE -or- CREATE FAILED
- STOP PENDING > STOP IN_PROGRESS > INACTIVE > START PENDING > START IN_PROGRESS > ACTIVE
- DELETE PENDING > DELETE IN_PROGRESS
  To get the recommender status, call [DescribeRecommender](API_DescribeRecommender.md "API_DescribeRecommender.md").

###### Note

Wait until the `status` of the recommender
is `ACTIVE` before asking the recommender for recommendations.

###### Related APIs

- [ListRecommenders](API_ListRecommenders.md "API_ListRecommenders.md")
- [DescribeRecommender](API_DescribeRecommender.md "API_DescribeRecommender.md")
- [UpdateRecommender](API_UpdateRecommender.md "API_UpdateRecommender.md")
- [DeleteRecommender](API_DeleteRecommender.md "API_DeleteRecommender.md")

## Request Syntax

```
{
   "datasetGroupArn": "`string`",
   "name": "`string`",
   "recipeArn": "`string`",
   "recommenderConfig": {
      "enableMetadataWithRecommendations": `boolean`,
      "itemExplorationConfig": {
         "`string`" : "`string`"
      },
      "minRecommendationRequestsPerSecond": `number`,
      "trainingDataConfig": {
         "excludedDatasetColumns": {
            "`string`" : [ "`string`" ]
         },
         "includedDatasetColumns": {
            "`string`" : [ "`string`" ]
         }
      }
   },
   "tags": [
      {
         "tagKey": "`string`",
         "tagValue": "`string`"
      }
   ]
}
```

## Request Parameters

The request accepts the following data in JSON format.

**[datasetGroupArn](#API_CreateRecommender_RequestSyntax "#API_CreateRecommender_RequestSyntax")**

The Amazon Resource Name (ARN) of the destination domain dataset group for the recommender.

Type: String

Length Constraints: Maximum length of 256.

Pattern: `arn:([a-z\d-]+):personalize:.*:.*:.+`

Required: Yes

**[name](#API_CreateRecommender_RequestSyntax "#API_CreateRecommender_RequestSyntax")**

The name of the recommender.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 63.

Pattern: `^[a-zA-Z0-9][a-zA-Z0-9\-_]*`

Required: Yes

**[recipeArn](#API_CreateRecommender_RequestSyntax "#API_CreateRecommender_RequestSyntax")**

The Amazon Resource Name (ARN) of the recipe that the recommender will use. For a recommender, a recipe is a Domain dataset group
use case. Only Domain dataset group use cases can be used to create a recommender. For information about use cases see [Choosing recommender use cases](domain-use-cases.md "domain-use-cases.md").

Type: String

Length Constraints: Maximum length of 256.

Pattern: `arn:([a-z\d-]+):personalize:.*:.*:.+`

Required: Yes

**[recommenderConfig](#API_CreateRecommender_RequestSyntax "#API_CreateRecommender_RequestSyntax")**

The configuration details of the recommender.

Type: [RecommenderConfig](API_RecommenderConfig.md "API_RecommenderConfig.md") object

Required: No

**[tags](#API_CreateRecommender_RequestSyntax "#API_CreateRecommender_RequestSyntax")**

A list of [tags](tagging-resources.md "tagging-resources.md") to apply to the recommender.

Type: Array of [Tag](API_Tag.md "API_Tag.md") objects

Array Members: Minimum number of 0 items. Maximum number of 200 items.

Required: No

## Response Syntax

```
{
   "recommenderArn": "***string***"
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[recommenderArn](#API_CreateRecommender_ResponseSyntax "#API_CreateRecommender_ResponseSyntax")**

The Amazon Resource Name (ARN) of the recommender.

Type: String

Length Constraints: Maximum length of 256.

Pattern: `arn:([a-z\d-]+):personalize:.*:.*:.+`

## Errors

**InvalidInputException**

Provide a valid value for the field or parameter.

HTTP Status Code: 400

**LimitExceededException**

The limit on the number of requests per second has been exceeded.

HTTP Status Code: 400

**ResourceAlreadyExistsException**

The specified resource already exists.

HTTP Status Code: 400

**ResourceInUseException**

The specified resource is in use.

HTTP Status Code: 400

**ResourceNotFoundException**

Could not find the specified resource.

HTTP Status Code: 400

**TooManyTagsException**

You have exceeded the maximum number of tags you can apply to this resource.

HTTP Status Code: 400

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/personalize-2018-05-22/CreateRecommender.md "../../../goto/cli2/personalize-2018-05-22/CreateRecommender.md")
- [AWS SDK for .NET](../../../goto/DotNetSDKV3/personalize-2018-05-22/CreateRecommender.md "../../../goto/DotNetSDKV3/personalize-2018-05-22/CreateRecommender.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/personalize-2018-05-22/CreateRecommender.md "../../../goto/SdkForCpp/personalize-2018-05-22/CreateRecommender.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/personalize-2018-05-22/CreateRecommender.md "../../../goto/SdkForGoV2/personalize-2018-05-22/CreateRecommender.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/personalize-2018-05-22/CreateRecommender.md "../../../goto/SdkForJavaV2/personalize-2018-05-22/CreateRecommender.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/personalize-2018-05-22/CreateRecommender.md "../../../goto/SdkForJavaScriptV3/personalize-2018-05-22/CreateRecommender.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/personalize-2018-05-22/CreateRecommender.md "../../../goto/SdkForKotlin/personalize-2018-05-22/CreateRecommender.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/personalize-2018-05-22/CreateRecommender.md "../../../goto/SdkForPHPV3/personalize-2018-05-22/CreateRecommender.md")
- [AWS SDK for Python](../../../goto/boto3/personalize-2018-05-22/CreateRecommender.md "../../../goto/boto3/personalize-2018-05-22/CreateRecommender.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/personalize-2018-05-22/CreateRecommender.md "../../../goto/SdkForRubyV3/personalize-2018-05-22/CreateRecommender.md")
