# GetRecommendations

Returns a list of recommended items. For campaigns, the campaign's Amazon Resource Name (ARN) is required and the required user and item input depends on the recipe type used to
create the solution backing the campaign as follows:

- USER_PERSONALIZATION - `userId` required, `itemId` not used
- RELATED_ITEMS - `itemId` required, `userId` not used

###### Note

Campaigns that are backed by a solution created using a recipe of type
PERSONALIZED_RANKING use the [GetPersonalizedRanking](API_RS_GetPersonalizedRanking.md "API_RS_GetPersonalizedRanking.md") API.

For recommenders, the recommender's ARN is required and the required item and user input depends on the use case (domain-based recipe) backing the recommender.
For information on use case requirements see [Choosing recommender use cases](domain-use-cases.md "domain-use-cases.md").

## Request Syntax

```
POST /recommendations HTTP/1.1
Content-type: application/json

{
   "campaignArn": "`string`",
   "context": {
      "`string`" : "`string`"
   },
   "filterArn": "`string`",
   "filterValues": {
      "`string`" : "`string`"
   },
   "itemId": "`string`",
   "metadataColumns": {
      "`string`" : [ "`string`" ]
   },
   "numResults": `number`,
   "promotions": [
      {
         "filterArn": "`string`",
         "filterValues": {
            "`string`" : "`string`"
         },
         "name": "`string`",
         "percentPromotedItems": `number`
      }
   ],
   "recommenderArn": "`string`",
   "userId": "`string`"
}
```

## URI Request Parameters

The request does not use any URI parameters.

## Request Body

The request accepts the following data in JSON format.

**[campaignArn](#API_RS_GetRecommendations_RequestSyntax "#API_RS_GetRecommendations_RequestSyntax")**

The Amazon Resource Name (ARN) of the campaign to use for getting recommendations.

Type: String

Length Constraints: Maximum length of 256.

Pattern: `arn:([a-z\d-]+):personalize:.*:.*:.+`

Required: No

**[context](#API_RS_GetRecommendations_RequestSyntax "#API_RS_GetRecommendations_RequestSyntax")**

The contextual metadata to use when getting recommendations. Contextual metadata includes
any interaction information that might be relevant when getting a user's recommendations, such
as the user's current location or device type.

Type: String to string map

Map Entries: Maximum number of 150 items.

Key Length Constraints: Maximum length of 150.

Key Pattern: `[A-Za-z\d_]+`

Value Length Constraints: Maximum length of 1000.

Required: No

**[filterArn](#API_RS_GetRecommendations_RequestSyntax "#API_RS_GetRecommendations_RequestSyntax")**

The ARN of the filter to apply to the returned recommendations. For more information, see
[Filtering Recommendations](filter.md "filter.md").

When using this parameter, be sure the filter resource is `ACTIVE`.

Type: String

Length Constraints: Maximum length of 256.

Pattern: `arn:([a-z\d-]+):personalize:.*:.*:.+`

Required: No

**[filterValues](#API_RS_GetRecommendations_RequestSyntax "#API_RS_GetRecommendations_RequestSyntax")**

The values to use when filtering recommendations. For each placeholder parameter in your filter expression, provide the parameter name (in matching case)
as a key and the filter value(s) as the corresponding value. Separate multiple values for one parameter with a comma.

For filter expressions that use an `INCLUDE` element to include items,
you must provide values for all parameters that are defined in the expression. For
filters with expressions that use an `EXCLUDE` element to exclude items, you
can omit the `filter-values`.In this case, Amazon Personalize doesn't use that portion of
the expression to filter recommendations.

For more information, see
[Filtering recommendations and user segments](filter.md "filter.md").

Type: String to string map

Map Entries: Maximum number of 25 items.

Key Length Constraints: Maximum length of 50.

Key Pattern: `[A-Za-z0-9_]+`

Value Length Constraints: Maximum length of 1000.

Required: No

**[itemId](#API_RS_GetRecommendations_RequestSyntax "#API_RS_GetRecommendations_RequestSyntax")**

The item ID to provide recommendations for.

Required for `RELATED_ITEMS` recipe type.

Type: String

Length Constraints: Maximum length of 256.

Required: No

**[metadataColumns](#API_RS_GetRecommendations_RequestSyntax "#API_RS_GetRecommendations_RequestSyntax")**

If you enabled metadata in recommendations when you created or updated the campaign or recommender, specify the metadata columns from your Items dataset to include in item recommendations.
The map key is `ITEMS` and the value is a list of column names from your Items dataset.
The maximum number of columns you can provide is 10.

For information about enabling metadata for a campaign, see [Enabling metadata in recommendations for a campaign](campaigns.md#create-campaign-return-metadata "campaigns.md#create-campaign-return-metadata").
For information about enabling metadata for a recommender, see [Enabling metadata in recommendations for a recommender](creating-recommenders.md#create-recommender-return-metadata "creating-recommenders.md#create-recommender-return-metadata").

Type: String to array of strings map

Map Entries: Maximum number of 1 item.

Key Length Constraints: Maximum length of 256.

Array Members: Maximum number of 99 items.

Length Constraints: Maximum length of 150.

Required: No

**[numResults](#API_RS_GetRecommendations_RequestSyntax "#API_RS_GetRecommendations_RequestSyntax")**

The number of results to return. The default is 25. If you are including
metadata in recommendations, the maximum is 50. Otherwise, the maximum is 500.

Type: Integer

Valid Range: Minimum value of 0.

Required: No

**[promotions](#API_RS_GetRecommendations_RequestSyntax "#API_RS_GetRecommendations_RequestSyntax")**

The promotions to apply to the recommendation request.
A promotion defines additional business rules that apply to a configurable subset of recommended items.

Type: Array of [Promotion](API_RS_Promotion.md "API_RS_Promotion.md") objects

Array Members: Maximum number of 1 item.

Required: No

**[recommenderArn](#API_RS_GetRecommendations_RequestSyntax "#API_RS_GetRecommendations_RequestSyntax")**

The Amazon Resource Name (ARN) of the recommender to use to get recommendations. Provide a recommender ARN if you
created a Domain dataset group with a recommender for a domain use case.

Type: String

Length Constraints: Maximum length of 256.

Pattern: `arn:([a-z\d-]+):personalize:.*:.*:.+`

Required: No

**[userId](#API_RS_GetRecommendations_RequestSyntax "#API_RS_GetRecommendations_RequestSyntax")**

The user ID to provide recommendations for.

Required for `USER_PERSONALIZATION` recipe type.

Type: String

Length Constraints: Maximum length of 256.

Required: No

## Response Syntax

```
HTTP/1.1 200
Content-type: application/json

{
   "itemList": [
      {
         "itemId": "***string***",
         "metadata": {
            "***string***" : "***string***"
         },
         "promotionName": "***string***",
         "reason": [ "***string***" ],
         "score": ***number***
      }
   ],
   "recommendationId": "***string***"
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[itemList](#API_RS_GetRecommendations_ResponseSyntax "#API_RS_GetRecommendations_ResponseSyntax")**

A list of recommendations sorted in descending order by prediction score. There can be a
maximum of 500 items in the list.

Type: Array of [PredictedItem](API_RS_PredictedItem.md "API_RS_PredictedItem.md") objects

**[recommendationId](#API_RS_GetRecommendations_ResponseSyntax "#API_RS_GetRecommendations_ResponseSyntax")**

The ID of the recommendation.

Type: String

## Errors

**InvalidInputException**

Provide a valid value for the field or parameter.

HTTP Status Code: 400

**ResourceNotFoundException**

The specified resource does not exist.

HTTP Status Code: 404

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/personalize-runtime-2018-05-22/GetRecommendations.md "../../../goto/cli2/personalize-runtime-2018-05-22/GetRecommendations.md")
- [AWS SDK for .NET V4](../../../goto/DotNetSDKV4/personalize-runtime-2018-05-22/GetRecommendations.md "../../../goto/DotNetSDKV4/personalize-runtime-2018-05-22/GetRecommendations.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/personalize-runtime-2018-05-22/GetRecommendations.md "../../../goto/SdkForCpp/personalize-runtime-2018-05-22/GetRecommendations.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/personalize-runtime-2018-05-22/GetRecommendations.md "../../../goto/SdkForGoV2/personalize-runtime-2018-05-22/GetRecommendations.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/personalize-runtime-2018-05-22/GetRecommendations.md "../../../goto/SdkForJavaV2/personalize-runtime-2018-05-22/GetRecommendations.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/personalize-runtime-2018-05-22/GetRecommendations.md "../../../goto/SdkForJavaScriptV3/personalize-runtime-2018-05-22/GetRecommendations.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/personalize-runtime-2018-05-22/GetRecommendations.md "../../../goto/SdkForKotlin/personalize-runtime-2018-05-22/GetRecommendations.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/personalize-runtime-2018-05-22/GetRecommendations.md "../../../goto/SdkForPHPV3/personalize-runtime-2018-05-22/GetRecommendations.md")
- [AWS SDK for Python](../../../goto/boto3/personalize-runtime-2018-05-22/GetRecommendations.md "../../../goto/boto3/personalize-runtime-2018-05-22/GetRecommendations.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/personalize-runtime-2018-05-22/GetRecommendations.md "../../../goto/SdkForRubyV3/personalize-runtime-2018-05-22/GetRecommendations.md")
