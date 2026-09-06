

# GetActionRecommendations
<a name="API_RS_GetActionRecommendations"></a>

Returns a list of recommended actions in sorted in descending order by prediction score. Use the `GetActionRecommendations` API if you have a custom campaign that deploys a solution version trained with a PERSONALIZED\_ACTIONS recipe. 

For more information about PERSONALIZED\_ACTIONS recipes, see [PERSONALIZED\_ACTIONS recipes](https://docs.aws.amazon.com/personalize/latest/dg/nexts-best-action-recipes.html). For more information about getting action recommendations, see [Getting action recommendations](https://docs.aws.amazon.com/personalize/latest/dg/get-action-recommendations.html).

## Request Syntax
<a name="API_RS_GetActionRecommendations_RequestSyntax"></a>

```
POST /action-recommendations HTTP/1.1
Content-type: application/json

{
   "campaignArn": "{{string}}",
   "filterArn": "{{string}}",
   "filterValues": { 
      "{{string}}" : "{{string}}" 
   },
   "numResults": {{number}},
   "userId": "{{string}}"
}
```

## URI Request Parameters
<a name="API_RS_GetActionRecommendations_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_RS_GetActionRecommendations_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [campaignArn](#API_RS_GetActionRecommendations_RequestSyntax) **   <a name="personalize-RS_GetActionRecommendations-request-campaignArn"></a>
The Amazon Resource Name (ARN) of the campaign to use for getting action recommendations. This campaign must deploy a solution version trained with a PERSONALIZED\_ACTIONS recipe.  
Type: String  
Length Constraints: Maximum length of 256.  
Pattern: `arn:([a-z\d-]+):personalize:.*:.*:.+`   
Required: No

 ** [filterArn](#API_RS_GetActionRecommendations_RequestSyntax) **   <a name="personalize-RS_GetActionRecommendations-request-filterArn"></a>
The ARN of the filter to apply to the returned recommendations. For more information, see [Filtering Recommendations](https://docs.aws.amazon.com/personalize/latest/dg/filter.html).  
When using this parameter, be sure the filter resource is `ACTIVE`.  
Type: String  
Length Constraints: Maximum length of 256.  
Pattern: `arn:([a-z\d-]+):personalize:.*:.*:.+`   
Required: No

 ** [filterValues](#API_RS_GetActionRecommendations_RequestSyntax) **   <a name="personalize-RS_GetActionRecommendations-request-filterValues"></a>
The values to use when filtering recommendations. For each placeholder parameter in your filter expression, provide the parameter name (in matching case) as a key and the filter value(s) as the corresponding value. Separate multiple values for one parameter with a comma.   
For filter expressions that use an `INCLUDE` element to include actions, you must provide values for all parameters that are defined in the expression. For filters with expressions that use an `EXCLUDE` element to exclude actions, you can omit the `filter-values`. In this case, Amazon Personalize doesn't use that portion of the expression to filter recommendations.  
For more information, see [Filtering recommendations and user segments](https://docs.aws.amazon.com/personalize/latest/dg/filter.html).  
Type: String to string map  
Map Entries: Maximum number of 25 items.  
Key Length Constraints: Maximum length of 50.  
Key Pattern: `[A-Za-z0-9_]+`   
Value Length Constraints: Maximum length of 1000.  
Required: No

 ** [numResults](#API_RS_GetActionRecommendations_RequestSyntax) **   <a name="personalize-RS_GetActionRecommendations-request-numResults"></a>
The number of results to return. The default is 5. The maximum is 100.  
Type: Integer  
Valid Range: Minimum value of 0.  
Required: No

 ** [userId](#API_RS_GetActionRecommendations_RequestSyntax) **   <a name="personalize-RS_GetActionRecommendations-request-userId"></a>
The user ID of the user to provide action recommendations for.  
Type: String  
Length Constraints: Maximum length of 256.  
Required: No

## Response Syntax
<a name="API_RS_GetActionRecommendations_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "actionList": [ 
      { 
         "actionId": "string",
         "score": number
      }
   ],
   "recommendationId": "string"
}
```

## Response Elements
<a name="API_RS_GetActionRecommendations_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [actionList](#API_RS_GetActionRecommendations_ResponseSyntax) **   <a name="personalize-RS_GetActionRecommendations-response-actionList"></a>
A list of action recommendations sorted in descending order by prediction score. There can be a maximum of 100 actions in the list. For information about action scores, see [How action recommendation scoring works](https://docs.aws.amazon.com/personalize/latest/dg/how-action-recommendation-scoring-works.html).  
Type: Array of [PredictedAction](API_RS_PredictedAction.md) objects

 ** [recommendationId](#API_RS_GetActionRecommendations_ResponseSyntax) **   <a name="personalize-RS_GetActionRecommendations-response-recommendationId"></a>
The ID of the recommendation.  
Type: String

## Errors
<a name="API_RS_GetActionRecommendations_Errors"></a>

 ** InvalidInputException **   
Provide a valid value for the field or parameter.  
HTTP Status Code: 400

 ** ResourceNotFoundException **   
The specified resource does not exist.  
HTTP Status Code: 404

## See Also
<a name="API_RS_GetActionRecommendations_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/personalize-runtime-2018-05-22/GetActionRecommendations) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/personalize-runtime-2018-05-22/GetActionRecommendations) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/personalize-runtime-2018-05-22/GetActionRecommendations) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/personalize-runtime-2018-05-22/GetActionRecommendations) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/personalize-runtime-2018-05-22/GetActionRecommendations) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/personalize-runtime-2018-05-22/GetActionRecommendations) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/personalize-runtime-2018-05-22/GetActionRecommendations) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/personalize-runtime-2018-05-22/GetActionRecommendations) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/personalize-runtime-2018-05-22/GetActionRecommendations) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/personalize-runtime-2018-05-22/GetActionRecommendations) 