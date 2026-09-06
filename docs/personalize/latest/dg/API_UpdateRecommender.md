

# UpdateRecommender
<a name="API_UpdateRecommender"></a>

Updates the recommender to modify the recommender configuration. If you update the recommender to modify the columns used in training, Amazon Personalize automatically starts a full retraining of the models backing your recommender. While the update completes, you can still get recommendations from the recommender. The recommender uses the previous configuration until the update completes. To track the status of this update, use the `latestRecommenderUpdate` returned in the [DescribeRecommender](https://docs.aws.amazon.com/personalize/latest/dg/API_DescribeRecommender.html) operation. 

## Request Syntax
<a name="API_UpdateRecommender_RequestSyntax"></a>

```
{
   "recommenderArn": "{{string}}",
   "recommenderConfig": { 
      "enableMetadataWithRecommendations": {{boolean}},
      "itemExplorationConfig": { 
         "{{string}}" : "{{string}}" 
      },
      "minRecommendationRequestsPerSecond": {{number}},
      "trainingDataConfig": { 
         "excludedDatasetColumns": { 
            "{{string}}" : [ "{{string}}" ]
         },
         "includedDatasetColumns": { 
            "{{string}}" : [ "{{string}}" ]
         }
      }
   }
}
```

## Request Parameters
<a name="API_UpdateRecommender_RequestParameters"></a>

The request accepts the following data in JSON format.

 ** [recommenderArn](#API_UpdateRecommender_RequestSyntax) **   <a name="personalize-UpdateRecommender-request-recommenderArn"></a>
The Amazon Resource Name (ARN) of the recommender to modify.  
Type: String  
Length Constraints: Maximum length of 256.  
Pattern: `arn:([a-z\d-]+):personalize:.*:.*:.+`   
Required: Yes

 ** [recommenderConfig](#API_UpdateRecommender_RequestSyntax) **   <a name="personalize-UpdateRecommender-request-recommenderConfig"></a>
The configuration details of the recommender.  
Type: [RecommenderConfig](API_RecommenderConfig.md) object  
Required: Yes

## Response Syntax
<a name="API_UpdateRecommender_ResponseSyntax"></a>

```
{
   "recommenderArn": "string"
}
```

## Response Elements
<a name="API_UpdateRecommender_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [recommenderArn](#API_UpdateRecommender_ResponseSyntax) **   <a name="personalize-UpdateRecommender-response-recommenderArn"></a>
The same recommender Amazon Resource Name (ARN) as given in the request.  
Type: String  
Length Constraints: Maximum length of 256.  
Pattern: `arn:([a-z\d-]+):personalize:.*:.*:.+` 

## Errors
<a name="API_UpdateRecommender_Errors"></a>

 ** InvalidInputException **   
Provide a valid value for the field or parameter.  
HTTP Status Code: 400

 ** ResourceInUseException **   
The specified resource is in use.  
HTTP Status Code: 400

 ** ResourceNotFoundException **   
Could not find the specified resource.  
HTTP Status Code: 400

## See Also
<a name="API_UpdateRecommender_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/personalize-2018-05-22/UpdateRecommender) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/personalize-2018-05-22/UpdateRecommender) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/personalize-2018-05-22/UpdateRecommender) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/personalize-2018-05-22/UpdateRecommender) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/personalize-2018-05-22/UpdateRecommender) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/personalize-2018-05-22/UpdateRecommender) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/personalize-2018-05-22/UpdateRecommender) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/personalize-2018-05-22/UpdateRecommender) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/personalize-2018-05-22/UpdateRecommender) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/personalize-2018-05-22/UpdateRecommender) 