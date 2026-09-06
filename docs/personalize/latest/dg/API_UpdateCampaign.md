

# UpdateCampaign
<a name="API_UpdateCampaign"></a>

 Updates a campaign to deploy a retrained solution version with an existing campaign, change your campaign's `minProvisionedTPS`, or modify your campaign's configuration. For example, you can set `enableMetadataWithRecommendations` to true for an existing campaign.

 To update a campaign to start automatically using the latest solution version, specify the following:
+ For the `SolutionVersionArn` parameter, specify the Amazon Resource Name (ARN) of your solution in `SolutionArn/$LATEST` format. 
+  In the `campaignConfig`, set `syncWithLatestSolutionVersion` to `true`. 

To update a campaign, the campaign status must be ACTIVE or CREATE FAILED. Check the campaign status using the [DescribeCampaign](https://docs.aws.amazon.com/personalize/latest/dg/API_DescribeCampaign.html) operation.

**Note**  
You can still get recommendations from a campaign while an update is in progress. The campaign will use the previous solution version and campaign configuration to generate recommendations until the latest campaign update status is `Active`. 

For more information about updating a campaign, including code samples, see [Updating a campaign](https://docs.aws.amazon.com/personalize/latest/dg/update-campaigns.html). For more information about campaigns, see [Creating a campaign](https://docs.aws.amazon.com/personalize/latest/dg/campaigns.html).

## Request Syntax
<a name="API_UpdateCampaign_RequestSyntax"></a>

```
{
   "campaignArn": "{{string}}",
   "campaignConfig": { 
      "enableMetadataWithRecommendations": {{boolean}},
      "itemExplorationConfig": { 
         "{{string}}" : "{{string}}" 
      },
      "rankingInfluence": { 
         "{{string}}" : {{number}} 
      },
      "syncWithLatestSolutionVersion": {{boolean}}
   },
   "minProvisionedTPS": {{number}},
   "solutionVersionArn": "{{string}}"
}
```

## Request Parameters
<a name="API_UpdateCampaign_RequestParameters"></a>

The request accepts the following data in JSON format.

 ** [campaignArn](#API_UpdateCampaign_RequestSyntax) **   <a name="personalize-UpdateCampaign-request-campaignArn"></a>
The Amazon Resource Name (ARN) of the campaign.  
Type: String  
Length Constraints: Maximum length of 256.  
Pattern: `arn:([a-z\d-]+):personalize:.*:.*:.+`   
Required: Yes

 ** [campaignConfig](#API_UpdateCampaign_RequestSyntax) **   <a name="personalize-UpdateCampaign-request-campaignConfig"></a>
The configuration details of a campaign.  
Type: [CampaignConfig](API_CampaignConfig.md) object  
Required: No

 ** [minProvisionedTPS](#API_UpdateCampaign_RequestSyntax) **   <a name="personalize-UpdateCampaign-request-minProvisionedTPS"></a>
Specifies the requested minimum provisioned transactions (recommendations) per second that Amazon Personalize will support. A high `minProvisionedTPS` will increase your bill. We recommend starting with 1 for `minProvisionedTPS` (the default). Track your usage using Amazon CloudWatch metrics, and increase the `minProvisionedTPS` as necessary.  
Type: Integer  
Valid Range: Minimum value of 1.  
Required: No

 ** [solutionVersionArn](#API_UpdateCampaign_RequestSyntax) **   <a name="personalize-UpdateCampaign-request-solutionVersionArn"></a>
The Amazon Resource Name (ARN) of a new model to deploy. To specify the latest solution version of your solution, specify the ARN of your *solution* in `SolutionArn/$LATEST` format. You must use this format if you set `syncWithLatestSolutionVersion` to `True` in the [CampaignConfig](https://docs.aws.amazon.com/personalize/latest/dg/API_CampaignConfig.html).   
 To deploy a model that isn't the latest solution version of your solution, specify the ARN of the solution version.   
 For more information about automatic campaign updates, see [Enabling automatic campaign updates](https://docs.aws.amazon.com/personalize/latest/dg/campaigns.html#create-campaign-automatic-latest-sv-update).   
Type: String  
Length Constraints: Maximum length of 256.  
Pattern: `arn:([a-z\d-]+):personalize:.*:.*:.+`   
Required: No

## Response Syntax
<a name="API_UpdateCampaign_ResponseSyntax"></a>

```
{
   "campaignArn": "string"
}
```

## Response Elements
<a name="API_UpdateCampaign_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [campaignArn](#API_UpdateCampaign_ResponseSyntax) **   <a name="personalize-UpdateCampaign-response-campaignArn"></a>
The same campaign ARN as given in the request.  
Type: String  
Length Constraints: Maximum length of 256.  
Pattern: `arn:([a-z\d-]+):personalize:.*:.*:.+` 

## Errors
<a name="API_UpdateCampaign_Errors"></a>

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
<a name="API_UpdateCampaign_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/personalize-2018-05-22/UpdateCampaign) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/personalize-2018-05-22/UpdateCampaign) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/personalize-2018-05-22/UpdateCampaign) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/personalize-2018-05-22/UpdateCampaign) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/personalize-2018-05-22/UpdateCampaign) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/personalize-2018-05-22/UpdateCampaign) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/personalize-2018-05-22/UpdateCampaign) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/personalize-2018-05-22/UpdateCampaign) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/personalize-2018-05-22/UpdateCampaign) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/personalize-2018-05-22/UpdateCampaign) 