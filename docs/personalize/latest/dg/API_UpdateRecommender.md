# UpdateRecommender

Updates the recommender to modify the recommender configuration.
If you update the recommender to modify the columns used in training, Amazon Personalize automatically starts a full retraining of
the models backing your recommender. While the update completes, you can still get recommendations from the recommender. The recommender
uses the previous configuration until the update completes.
To track the status of this update,
use the `latestRecommenderUpdate` returned in the [DescribeRecommender](API_DescribeRecommender.md "API_DescribeRecommender.md")
operation.

## Request Syntax

```
{
   "recommenderArn": "`string`",
   "recommenderConfig": {
      "enableMetadataWithRecommendations": `boolean`,
      "itemExplorationConfig": {
         "`string`" : "`string`"
      },
      "minRecommendationRequestsPerSecond": `number`,
      "trainingDataConfig": {
         "excludedDatasetColumns": {
            "`string`" : [ "`string`" ]
         }
      }
   }
}
```

## Request Parameters

The request accepts the following data in JSON format.

**[recommenderArn](#API_UpdateRecommender_RequestSyntax "#API_UpdateRecommender_RequestSyntax")**

The Amazon Resource Name (ARN) of the recommender to modify.

Type: String

Length Constraints: Maximum length of 256.

Pattern: `arn:([a-z\d-]+):personalize:.*:.*:.+`

Required: Yes

**[recommenderConfig](#API_UpdateRecommender_RequestSyntax "#API_UpdateRecommender_RequestSyntax")**

The configuration details of the recommender.

Type: [RecommenderConfig](API_RecommenderConfig.md "API_RecommenderConfig.md") object

Required: Yes

## Response Syntax

```
{
   "recommenderArn": "***string***"
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[recommenderArn](#API_UpdateRecommender_ResponseSyntax "#API_UpdateRecommender_ResponseSyntax")**

The same recommender Amazon Resource Name (ARN) as given in the request.

Type: String

Length Constraints: Maximum length of 256.

Pattern: `arn:([a-z\d-]+):personalize:.*:.*:.+`

## Errors

**InvalidInputException**

Provide a valid value for the field or parameter.

HTTP Status Code: 400

**ResourceInUseException**

The specified resource is in use.

HTTP Status Code: 400

**ResourceNotFoundException**

Could not find the specified resource.

HTTP Status Code: 400

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/personalize-2018-05-22/UpdateRecommender.md "../../../goto/cli2/personalize-2018-05-22/UpdateRecommender.md")
- [AWS SDK for .NET](../../../goto/DotNetSDKV3/personalize-2018-05-22/UpdateRecommender.md "../../../goto/DotNetSDKV3/personalize-2018-05-22/UpdateRecommender.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/personalize-2018-05-22/UpdateRecommender.md "../../../goto/SdkForCpp/personalize-2018-05-22/UpdateRecommender.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/personalize-2018-05-22/UpdateRecommender.md "../../../goto/SdkForGoV2/personalize-2018-05-22/UpdateRecommender.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/personalize-2018-05-22/UpdateRecommender.md "../../../goto/SdkForJavaV2/personalize-2018-05-22/UpdateRecommender.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/personalize-2018-05-22/UpdateRecommender.md "../../../goto/SdkForJavaScriptV3/personalize-2018-05-22/UpdateRecommender.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/personalize-2018-05-22/UpdateRecommender.md "../../../goto/SdkForKotlin/personalize-2018-05-22/UpdateRecommender.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/personalize-2018-05-22/UpdateRecommender.md "../../../goto/SdkForPHPV3/personalize-2018-05-22/UpdateRecommender.md")
- [AWS SDK for Python](../../../goto/boto3/personalize-2018-05-22/UpdateRecommender.md "../../../goto/boto3/personalize-2018-05-22/UpdateRecommender.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/personalize-2018-05-22/UpdateRecommender.md "../../../goto/SdkForRubyV3/personalize-2018-05-22/UpdateRecommender.md")
