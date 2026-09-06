

# CreateCampaign
<a name="API_CreateCampaign"></a>

**Important**  
 You incur campaign costs while it is active. To avoid unnecessary costs, make sure to delete the campaign when you are finished. For information about campaign costs, see [Amazon Personalize pricing](https://aws.amazon.com/personalize/pricing/).

Creates a campaign that deploys a solution version. When a client calls the [GetRecommendations](https://docs.aws.amazon.com/personalize/latest/dg/API_RS_GetRecommendations.html) and [GetPersonalizedRanking](https://docs.aws.amazon.com/personalize/latest/dg/API_RS_GetPersonalizedRanking.html) APIs, a campaign is specified in the request.

 **Minimum Provisioned TPS and Auto-Scaling** 

**Important**  
 A high `minProvisionedTPS` will increase your cost. We recommend starting with 1 for `minProvisionedTPS` (the default). Track your usage using Amazon CloudWatch metrics, and increase the `minProvisionedTPS` as necessary.

 When you create an Amazon Personalize campaign, you can specify the minimum provisioned transactions per second (`minProvisionedTPS`) for the campaign. This is the baseline transaction throughput for the campaign provisioned by Amazon Personalize. It sets the minimum billing charge for the campaign while it is active. A transaction is a single `GetRecommendations` or `GetPersonalizedRanking` request. The default `minProvisionedTPS` is 1.

 If your TPS increases beyond the `minProvisionedTPS`, Amazon Personalize auto-scales the provisioned capacity up and down, but never below `minProvisionedTPS`. There's a short time delay while the capacity is increased that might cause loss of transactions. When your traffic reduces, capacity returns to the `minProvisionedTPS`. 

You are charged for the the minimum provisioned TPS or, if your requests exceed the `minProvisionedTPS`, the actual TPS. The actual TPS is the total number of recommendation requests you make. We recommend starting with a low `minProvisionedTPS`, track your usage using Amazon CloudWatch metrics, and then increase the `minProvisionedTPS` as necessary.

For more information about campaign costs, see [Amazon Personalize pricing](https://aws.amazon.com/personalize/pricing/).

 **Status** 

A campaign can be in one of the following states:
+ CREATE PENDING > CREATE IN\_PROGRESS > ACTIVE -or- CREATE FAILED
+ DELETE PENDING > DELETE IN\_PROGRESS

To get the campaign status, call [DescribeCampaign](https://docs.aws.amazon.com/personalize/latest/dg/API_DescribeCampaign.html).

**Note**  
Wait until the `status` of the campaign is `ACTIVE` before asking the campaign for recommendations.

**Related APIs**
+  [ListCampaigns](https://docs.aws.amazon.com/personalize/latest/dg/API_ListCampaigns.html) 
+  [DescribeCampaign](https://docs.aws.amazon.com/personalize/latest/dg/API_DescribeCampaign.html) 
+  [UpdateCampaign](https://docs.aws.amazon.com/personalize/latest/dg/API_UpdateCampaign.html) 
+  [DeleteCampaign](https://docs.aws.amazon.com/personalize/latest/dg/API_DeleteCampaign.html) 

## Request Syntax
<a name="API_CreateCampaign_RequestSyntax"></a>

```
{
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
   "name": "{{string}}",
   "solutionVersionArn": "{{string}}",
   "tags": [ 
      { 
         "tagKey": "{{string}}",
         "tagValue": "{{string}}"
      }
   ]
}
```

## Request Parameters
<a name="API_CreateCampaign_RequestParameters"></a>

The request accepts the following data in JSON format.

 ** [campaignConfig](#API_CreateCampaign_RequestSyntax) **   <a name="personalize-CreateCampaign-request-campaignConfig"></a>
The configuration details of a campaign.  
Type: [CampaignConfig](API_CampaignConfig.md) object  
Required: No

 ** [minProvisionedTPS](#API_CreateCampaign_RequestSyntax) **   <a name="personalize-CreateCampaign-request-minProvisionedTPS"></a>
Specifies the requested minimum provisioned transactions (recommendations) per second that Amazon Personalize will support. A high `minProvisionedTPS` will increase your bill. We recommend starting with 1 for `minProvisionedTPS` (the default). Track your usage using Amazon CloudWatch metrics, and increase the `minProvisionedTPS` as necessary.  
Type: Integer  
Valid Range: Minimum value of 1.  
Required: No

 ** [name](#API_CreateCampaign_RequestSyntax) **   <a name="personalize-CreateCampaign-request-name"></a>
A name for the new campaign. The campaign name must be unique within your account.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 63.  
Pattern: `^[a-zA-Z0-9][a-zA-Z0-9\-_]*`   
Required: Yes

 ** [solutionVersionArn](#API_CreateCampaign_RequestSyntax) **   <a name="personalize-CreateCampaign-request-solutionVersionArn"></a>
The Amazon Resource Name (ARN) of the trained model to deploy with the campaign. To specify the latest solution version of your solution, specify the ARN of your *solution* in `SolutionArn/$LATEST` format. You must use this format if you set `syncWithLatestSolutionVersion` to `True` in the [CampaignConfig](https://docs.aws.amazon.com/personalize/latest/dg/API_CampaignConfig.html).   
 To deploy a model that isn't the latest solution version of your solution, specify the ARN of the solution version.   
 For more information about automatic campaign updates, see [Enabling automatic campaign updates](https://docs.aws.amazon.com/personalize/latest/dg/campaigns.html#create-campaign-automatic-latest-sv-update).   
Type: String  
Length Constraints: Maximum length of 256.  
Pattern: `arn:([a-z\d-]+):personalize:.*:.*:.+`   
Required: Yes

 ** [tags](#API_CreateCampaign_RequestSyntax) **   <a name="personalize-CreateCampaign-request-tags"></a>
A list of [tags](https://docs.aws.amazon.com/personalize/latest/dg/tagging-resources.html) to apply to the campaign.  
Type: Array of [Tag](API_Tag.md) objects  
Array Members: Minimum number of 0 items. Maximum number of 200 items.  
Required: No

## Response Syntax
<a name="API_CreateCampaign_ResponseSyntax"></a>

```
{
   "campaignArn": "string"
}
```

## Response Elements
<a name="API_CreateCampaign_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [campaignArn](#API_CreateCampaign_ResponseSyntax) **   <a name="personalize-CreateCampaign-response-campaignArn"></a>
The Amazon Resource Name (ARN) of the campaign.  
Type: String  
Length Constraints: Maximum length of 256.  
Pattern: `arn:([a-z\d-]+):personalize:.*:.*:.+` 

## Errors
<a name="API_CreateCampaign_Errors"></a>

 ** InvalidInputException **   
Provide a valid value for the field or parameter.  
HTTP Status Code: 400

 ** LimitExceededException **   
The limit on the number of requests per second has been exceeded.  
HTTP Status Code: 400

 ** ResourceAlreadyExistsException **   
The specified resource already exists.  
HTTP Status Code: 400

 ** ResourceInUseException **   
The specified resource is in use.  
HTTP Status Code: 400

 ** ResourceNotFoundException **   
Could not find the specified resource.  
HTTP Status Code: 400

 ** TooManyTagsException **   
You have exceeded the maximum number of tags you can apply to this resource.   
HTTP Status Code: 400

## See Also
<a name="API_CreateCampaign_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/personalize-2018-05-22/CreateCampaign) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/personalize-2018-05-22/CreateCampaign) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/personalize-2018-05-22/CreateCampaign) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/personalize-2018-05-22/CreateCampaign) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/personalize-2018-05-22/CreateCampaign) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/personalize-2018-05-22/CreateCampaign) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/personalize-2018-05-22/CreateCampaign) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/personalize-2018-05-22/CreateCampaign) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/personalize-2018-05-22/CreateCampaign) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/personalize-2018-05-22/CreateCampaign) 