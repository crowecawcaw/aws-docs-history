# GetPersonalizedRanking

Re-ranks a list of recommended items for the given user. The first item in the list is
deemed the most likely item to be of interest to the user.

###### Note

The solution backing the campaign must have been created using a recipe of type
PERSONALIZED_RANKING.

## Request Syntax

```
POST /personalize-ranking HTTP/1.1
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
   "inputList": [ "`string`" ],
   "metadataColumns": {
      "`string`" : [ "`string`" ]
   },
   "userId": "`string`"
}
```

## URI Request Parameters

The request does not use any URI parameters.

## Request Body

The request accepts the following data in JSON format.

**[campaignArn](#API_RS_GetPersonalizedRanking_RequestSyntax "#API_RS_GetPersonalizedRanking_RequestSyntax")**

The Amazon Resource Name (ARN) of the campaign to use for generating the personalized
ranking.

Type: String

Length Constraints: Maximum length of 256.

Pattern: `arn:([a-z\d-]+):personalize:.*:.*:.+`

Required: Yes

**[context](#API_RS_GetPersonalizedRanking_RequestSyntax "#API_RS_GetPersonalizedRanking_RequestSyntax")**

The contextual metadata to use when getting recommendations. Contextual metadata includes
any interaction information that might be relevant when getting a user's recommendations, such
as the user's current location or device type.

Type: String to string map

Map Entries: Maximum number of 150 items.

Key Length Constraints: Maximum length of 150.

Key Pattern: `[A-Za-z\d_]+`

Value Length Constraints: Maximum length of 1000.

Required: No

**[filterArn](#API_RS_GetPersonalizedRanking_RequestSyntax "#API_RS_GetPersonalizedRanking_RequestSyntax")**

The Amazon Resource Name (ARN) of a filter you created to include items or exclude items from recommendations for a given user.
For more information, see
[Filtering Recommendations](filter.md "filter.md").

Type: String

Length Constraints: Maximum length of 256.

Pattern: `arn:([a-z\d-]+):personalize:.*:.*:.+`

Required: No

**[filterValues](#API_RS_GetPersonalizedRanking_RequestSyntax "#API_RS_GetPersonalizedRanking_RequestSyntax")**

The values to use when filtering recommendations. For each placeholder parameter in your filter expression, provide the parameter name (in matching case)
as a key and the filter value(s) as the corresponding value. Separate multiple values for one parameter with a comma.

For filter expressions that use an `INCLUDE` element to include items,
you must provide values for all parameters that are defined in the expression. For
filters with expressions that use an `EXCLUDE` element to exclude items, you
can omit the `filter-values`.In this case, Amazon Personalize doesn't use that portion of
the expression to filter recommendations.

For more information, see
[Filtering Recommendations](filter.md "filter.md").

Type: String to string map

Map Entries: Maximum number of 25 items.

Key Length Constraints: Maximum length of 50.

Key Pattern: `[A-Za-z0-9_]+`

Value Length Constraints: Maximum length of 1000.

Required: No

**[inputList](#API_RS_GetPersonalizedRanking_RequestSyntax "#API_RS_GetPersonalizedRanking_RequestSyntax")**

A list of items (by `itemId`) to rank. If an item was not included in the training dataset,
the item is appended to the end of the reranked list. If you are including
metadata in recommendations, the maximum is 50. Otherwise, the maximum is 500.

Type: Array of strings

Length Constraints: Maximum length of 256.

Required: Yes

**[metadataColumns](#API_RS_GetPersonalizedRanking_RequestSyntax "#API_RS_GetPersonalizedRanking_RequestSyntax")**

If you enabled metadata in recommendations when you created or updated the campaign, specify metadata columns from your Items dataset to include
in the personalized ranking.
The map key is `ITEMS` and the value is a list of column names from your Items dataset.
The maximum number of columns you can provide is 10.

For information about enabling metadata for a campaign, see [Enabling metadata in recommendations for a campaign](campaigns.md#create-campaign-return-metadata "campaigns.md#create-campaign-return-metadata").

Type: String to array of strings map

Map Entries: Maximum number of 1 item.

Key Length Constraints: Maximum length of 256.

Array Members: Maximum number of 99 items.

Length Constraints: Maximum length of 150.

Required: No

**[userId](#API_RS_GetPersonalizedRanking_RequestSyntax "#API_RS_GetPersonalizedRanking_RequestSyntax")**

The user for which you want the campaign to provide a personalized ranking.

Type: String

Length Constraints: Maximum length of 256.

Required: Yes

## Response Syntax

```
HTTP/1.1 200
Content-type: application/json

{
   "personalizedRanking": [
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

**[personalizedRanking](#API_RS_GetPersonalizedRanking_ResponseSyntax "#API_RS_GetPersonalizedRanking_ResponseSyntax")**

A list of items in order of most likely interest to the user. The maximum is 500.

Type: Array of [PredictedItem](API_RS_PredictedItem.md "API_RS_PredictedItem.md") objects

**[recommendationId](#API_RS_GetPersonalizedRanking_ResponseSyntax "#API_RS_GetPersonalizedRanking_ResponseSyntax")**

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

- [AWS Command Line Interface V2](../../../goto/cli2/personalize-runtime-2018-05-22/GetPersonalizedRanking.md "../../../goto/cli2/personalize-runtime-2018-05-22/GetPersonalizedRanking.md")
- [AWS SDK for .NET V4](../../../goto/DotNetSDKV4/personalize-runtime-2018-05-22/GetPersonalizedRanking.md "../../../goto/DotNetSDKV4/personalize-runtime-2018-05-22/GetPersonalizedRanking.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/personalize-runtime-2018-05-22/GetPersonalizedRanking.md "../../../goto/SdkForCpp/personalize-runtime-2018-05-22/GetPersonalizedRanking.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/personalize-runtime-2018-05-22/GetPersonalizedRanking.md "../../../goto/SdkForGoV2/personalize-runtime-2018-05-22/GetPersonalizedRanking.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/personalize-runtime-2018-05-22/GetPersonalizedRanking.md "../../../goto/SdkForJavaV2/personalize-runtime-2018-05-22/GetPersonalizedRanking.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/personalize-runtime-2018-05-22/GetPersonalizedRanking.md "../../../goto/SdkForJavaScriptV3/personalize-runtime-2018-05-22/GetPersonalizedRanking.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/personalize-runtime-2018-05-22/GetPersonalizedRanking.md "../../../goto/SdkForKotlin/personalize-runtime-2018-05-22/GetPersonalizedRanking.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/personalize-runtime-2018-05-22/GetPersonalizedRanking.md "../../../goto/SdkForPHPV3/personalize-runtime-2018-05-22/GetPersonalizedRanking.md")
- [AWS SDK for Python](../../../goto/boto3/personalize-runtime-2018-05-22/GetPersonalizedRanking.md "../../../goto/boto3/personalize-runtime-2018-05-22/GetPersonalizedRanking.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/personalize-runtime-2018-05-22/GetPersonalizedRanking.md "../../../goto/SdkForRubyV3/personalize-runtime-2018-05-22/GetPersonalizedRanking.md")
