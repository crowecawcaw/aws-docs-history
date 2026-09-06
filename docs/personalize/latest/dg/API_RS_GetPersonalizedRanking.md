

# GetPersonalizedRanking
<a name="API_RS_GetPersonalizedRanking"></a>

Re-ranks a list of recommended items for the given user. The first item in the list is deemed the most likely item to be of interest to the user.

**Note**  
The solution backing the campaign must have been created using a recipe of type PERSONALIZED\_RANKING.

## Request Syntax
<a name="API_RS_GetPersonalizedRanking_RequestSyntax"></a>

```
POST /personalize-ranking HTTP/1.1
Content-type: application/json

{
   "campaignArn": "{{string}}",
   "context": { 
      "{{string}}" : "{{string}}" 
   },
   "filterArn": "{{string}}",
   "filterValues": { 
      "{{string}}" : "{{string}}" 
   },
   "inputList": [ "{{string}}" ],
   "metadataColumns": { 
      "{{string}}" : [ "{{string}}" ]
   },
   "userId": "{{string}}"
}
```

## URI Request Parameters
<a name="API_RS_GetPersonalizedRanking_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_RS_GetPersonalizedRanking_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [campaignArn](#API_RS_GetPersonalizedRanking_RequestSyntax) **   <a name="personalize-RS_GetPersonalizedRanking-request-campaignArn"></a>
The Amazon Resource Name (ARN) of the campaign to use for generating the personalized ranking.  
Type: String  
Length Constraints: Maximum length of 256.  
Pattern: `arn:([a-z\d-]+):personalize:.*:.*:.+`   
Required: Yes

 ** [context](#API_RS_GetPersonalizedRanking_RequestSyntax) **   <a name="personalize-RS_GetPersonalizedRanking-request-context"></a>
The contextual metadata to use when getting recommendations. Contextual metadata includes any interaction information that might be relevant when getting a user's recommendations, such as the user's current location or device type.  
Type: String to string map  
Map Entries: Maximum number of 150 items.  
Key Length Constraints: Maximum length of 150.  
Key Pattern: `[A-Za-z\d_]+`   
Value Length Constraints: Maximum length of 1000.  
Required: No

 ** [filterArn](#API_RS_GetPersonalizedRanking_RequestSyntax) **   <a name="personalize-RS_GetPersonalizedRanking-request-filterArn"></a>
The Amazon Resource Name (ARN) of a filter you created to include items or exclude items from recommendations for a given user. For more information, see [Filtering Recommendations](https://docs.aws.amazon.com/personalize/latest/dg/filter.html).  
Type: String  
Length Constraints: Maximum length of 256.  
Pattern: `arn:([a-z\d-]+):personalize:.*:.*:.+`   
Required: No

 ** [filterValues](#API_RS_GetPersonalizedRanking_RequestSyntax) **   <a name="personalize-RS_GetPersonalizedRanking-request-filterValues"></a>
The values to use when filtering recommendations. For each placeholder parameter in your filter expression, provide the parameter name (in matching case) as a key and the filter value(s) as the corresponding value. Separate multiple values for one parameter with a comma.   
For filter expressions that use an `INCLUDE` element to include items, you must provide values for all parameters that are defined in the expression. For filters with expressions that use an `EXCLUDE` element to exclude items, you can omit the `filter-values`.In this case, Amazon Personalize doesn't use that portion of the expression to filter recommendations.  
For more information, see [Filtering Recommendations](https://docs.aws.amazon.com/personalize/latest/dg/filter.html).  
Type: String to string map  
Map Entries: Maximum number of 25 items.  
Key Length Constraints: Maximum length of 50.  
Key Pattern: `[A-Za-z0-9_]+`   
Value Length Constraints: Maximum length of 1000.  
Required: No

 ** [inputList](#API_RS_GetPersonalizedRanking_RequestSyntax) **   <a name="personalize-RS_GetPersonalizedRanking-request-inputList"></a>
A list of items (by `itemId`) to rank. If an item was not included in the training dataset, the item is appended to the end of the reranked list. If you are including metadata in recommendations, the maximum is 50. Otherwise, the maximum is 500.  
Type: Array of strings  
Length Constraints: Maximum length of 256.  
Required: Yes

 ** [metadataColumns](#API_RS_GetPersonalizedRanking_RequestSyntax) **   <a name="personalize-RS_GetPersonalizedRanking-request-metadataColumns"></a>
If you enabled metadata in recommendations when you created or updated the campaign, specify metadata columns from your Items dataset to include in the personalized ranking. The map key is `ITEMS` and the value is a list of column names from your Items dataset. The maximum number of columns you can provide is 10.  
 For information about enabling metadata for a campaign, see [Enabling metadata in recommendations for a campaign](https://docs.aws.amazon.com/personalize/latest/dg/campaigns.html#create-campaign-return-metadata).   
Type: String to array of strings map  
Map Entries: Maximum number of 1 item.  
Key Length Constraints: Maximum length of 256.  
Array Members: Maximum number of 99 items.  
Length Constraints: Maximum length of 150.  
Required: No

 ** [userId](#API_RS_GetPersonalizedRanking_RequestSyntax) **   <a name="personalize-RS_GetPersonalizedRanking-request-userId"></a>
The user for which you want the campaign to provide a personalized ranking.  
Type: String  
Length Constraints: Maximum length of 256.  
Required: Yes

## Response Syntax
<a name="API_RS_GetPersonalizedRanking_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "personalizedRanking": [ 
      { 
         "itemId": "string",
         "metadata": { 
            "string" : "string" 
         },
         "promotionName": "string",
         "reason": [ "string" ],
         "score": number
      }
   ],
   "recommendationId": "string"
}
```

## Response Elements
<a name="API_RS_GetPersonalizedRanking_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [personalizedRanking](#API_RS_GetPersonalizedRanking_ResponseSyntax) **   <a name="personalize-RS_GetPersonalizedRanking-response-personalizedRanking"></a>
A list of items in order of most likely interest to the user. The maximum is 500.  
Type: Array of [PredictedItem](API_RS_PredictedItem.md) objects

 ** [recommendationId](#API_RS_GetPersonalizedRanking_ResponseSyntax) **   <a name="personalize-RS_GetPersonalizedRanking-response-recommendationId"></a>
The ID of the recommendation.  
Type: String

## Errors
<a name="API_RS_GetPersonalizedRanking_Errors"></a>

 ** InvalidInputException **   
Provide a valid value for the field or parameter.  
HTTP Status Code: 400

 ** ResourceNotFoundException **   
The specified resource does not exist.  
HTTP Status Code: 404

## See Also
<a name="API_RS_GetPersonalizedRanking_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/personalize-runtime-2018-05-22/GetPersonalizedRanking) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/personalize-runtime-2018-05-22/GetPersonalizedRanking) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/personalize-runtime-2018-05-22/GetPersonalizedRanking) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/personalize-runtime-2018-05-22/GetPersonalizedRanking) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/personalize-runtime-2018-05-22/GetPersonalizedRanking) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/personalize-runtime-2018-05-22/GetPersonalizedRanking) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/personalize-runtime-2018-05-22/GetPersonalizedRanking) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/personalize-runtime-2018-05-22/GetPersonalizedRanking) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/personalize-runtime-2018-05-22/GetPersonalizedRanking) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/personalize-runtime-2018-05-22/GetPersonalizedRanking) 