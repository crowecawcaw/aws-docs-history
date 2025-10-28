# CreateCampaign

###### Important

You incur campaign costs while it is active. To avoid unnecessary costs, make sure to delete the campaign when you are finished. For information about campaign
costs, see [Amazon Personalize pricing](https://aws.amazon.com/personalize/pricing/ "https://aws.amazon.com/personalize/pricing/").

Creates a campaign that deploys a solution version. When a client calls the
[GetRecommendations](API_RS_GetRecommendations.md "API_RS_GetRecommendations.md")
and
[GetPersonalizedRanking](API_RS_GetPersonalizedRanking.md "API_RS_GetPersonalizedRanking.md")
APIs, a campaign is specified in the request.

**Minimum Provisioned TPS and Auto-Scaling**

###### Important

A high `minProvisionedTPS` will increase your cost. We recommend starting with 1 for `minProvisionedTPS` (the default). Track
your usage using Amazon CloudWatch metrics, and increase the `minProvisionedTPS`
as necessary.

When you create an Amazon Personalize campaign, you can specify the minimum provisioned transactions per second
(`minProvisionedTPS`) for the campaign. This is the baseline transaction throughput for the campaign provisioned by
Amazon Personalize. It sets the minimum billing charge for the campaign while it is active. A transaction is a single `GetRecommendations` or
`GetPersonalizedRanking` request. The default `minProvisionedTPS` is 1.

If your TPS increases beyond the `minProvisionedTPS`, Amazon Personalize auto-scales the provisioned capacity up
and down, but never below `minProvisionedTPS`.
There's a short time delay while the capacity is increased
that might cause loss of transactions. When your traffic reduces, capacity returns to the `minProvisionedTPS`.

You are charged for the
the minimum provisioned TPS or, if your requests exceed the `minProvisionedTPS`, the actual TPS.
The actual TPS is the total number of recommendation requests you make.
We recommend starting with a low `minProvisionedTPS`, track
your usage using Amazon CloudWatch metrics, and then increase the `minProvisionedTPS` as necessary.

For more information about campaign costs, see [Amazon Personalize pricing](https://aws.amazon.com/personalize/pricing/ "https://aws.amazon.com/personalize/pricing/").

**Status**

A campaign can be in one of the following states:

- CREATE PENDING > CREATE IN_PROGRESS > ACTIVE -or- CREATE FAILED
- DELETE PENDING > DELETE IN_PROGRESS
  To get the campaign status, call [DescribeCampaign](API_DescribeCampaign.md "API_DescribeCampaign.md").

###### Note

Wait until the `status` of the campaign
is `ACTIVE` before asking the campaign for recommendations.

###### Related APIs

- [ListCampaigns](API_ListCampaigns.md "API_ListCampaigns.md")
- [DescribeCampaign](API_DescribeCampaign.md "API_DescribeCampaign.md")
- [UpdateCampaign](API_UpdateCampaign.md "API_UpdateCampaign.md")
- [DeleteCampaign](API_DeleteCampaign.md "API_DeleteCampaign.md")

## Request Syntax

```
{
   "campaignConfig": {
      "enableMetadataWithRecommendations": `boolean`,
      "itemExplorationConfig": {
         "`string`" : "`string`"
      },
      "syncWithLatestSolutionVersion": `boolean`
   },
   "minProvisionedTPS": `number`,
   "name": "`string`",
   "solutionVersionArn": "`string`",
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

**[campaignConfig](#API_CreateCampaign_RequestSyntax "#API_CreateCampaign_RequestSyntax")**

The configuration details of a campaign.

Type: [CampaignConfig](API_CampaignConfig.md "API_CampaignConfig.md") object

Required: No

**[minProvisionedTPS](#API_CreateCampaign_RequestSyntax "#API_CreateCampaign_RequestSyntax")**

Specifies the requested minimum provisioned transactions (recommendations) per second that
Amazon Personalize will support. A high `minProvisionedTPS` will increase your bill. We recommend starting with 1 for `minProvisionedTPS` (the default). Track
your usage using Amazon CloudWatch metrics, and increase the `minProvisionedTPS` as necessary.

Type: Integer

Valid Range: Minimum value of 1.

Required: No

**[name](#API_CreateCampaign_RequestSyntax "#API_CreateCampaign_RequestSyntax")**

A name for the new campaign. The campaign name must be unique within your account.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 63.

Pattern: `^[a-zA-Z0-9][a-zA-Z0-9\-_]*`

Required: Yes

**[solutionVersionArn](#API_CreateCampaign_RequestSyntax "#API_CreateCampaign_RequestSyntax")**

The Amazon Resource Name (ARN) of the trained model to deploy with the campaign. To specify the latest solution version of your solution,
specify the ARN of your _solution_ in `SolutionArn/$LATEST` format.
You must use this format if you set `syncWithLatestSolutionVersion` to `True` in the
[CampaignConfig](API_CampaignConfig.md "API_CampaignConfig.md").

To deploy a model that isn't the latest solution version of your solution, specify the ARN of the solution version.

For more information about automatic campaign updates, see
[Enabling automatic campaign updates](campaigns.md#create-campaign-automatic-latest-sv-update "campaigns.md#create-campaign-automatic-latest-sv-update").

Type: String

Length Constraints: Maximum length of 256.

Pattern: `arn:([a-z\d-]+):personalize:.*:.*:.+`

Required: Yes

**[tags](#API_CreateCampaign_RequestSyntax "#API_CreateCampaign_RequestSyntax")**

A list of [tags](tagging-resources.md "tagging-resources.md") to apply to the campaign.

Type: Array of [Tag](API_Tag.md "API_Tag.md") objects

Array Members: Minimum number of 0 items. Maximum number of 200 items.

Required: No

## Response Syntax

```
{
   "campaignArn": "***string***"
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[campaignArn](#API_CreateCampaign_ResponseSyntax "#API_CreateCampaign_ResponseSyntax")**

The Amazon Resource Name (ARN) of the campaign.

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

- [AWS Command Line Interface V2](../../../goto/cli2/personalize-2018-05-22/CreateCampaign.md "../../../goto/cli2/personalize-2018-05-22/CreateCampaign.md")
- [AWS SDK for .NET](../../../goto/DotNetSDKV3/personalize-2018-05-22/CreateCampaign.md "../../../goto/DotNetSDKV3/personalize-2018-05-22/CreateCampaign.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/personalize-2018-05-22/CreateCampaign.md "../../../goto/SdkForCpp/personalize-2018-05-22/CreateCampaign.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/personalize-2018-05-22/CreateCampaign.md "../../../goto/SdkForGoV2/personalize-2018-05-22/CreateCampaign.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/personalize-2018-05-22/CreateCampaign.md "../../../goto/SdkForJavaV2/personalize-2018-05-22/CreateCampaign.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/personalize-2018-05-22/CreateCampaign.md "../../../goto/SdkForJavaScriptV3/personalize-2018-05-22/CreateCampaign.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/personalize-2018-05-22/CreateCampaign.md "../../../goto/SdkForKotlin/personalize-2018-05-22/CreateCampaign.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/personalize-2018-05-22/CreateCampaign.md "../../../goto/SdkForPHPV3/personalize-2018-05-22/CreateCampaign.md")
- [AWS SDK for Python](../../../goto/boto3/personalize-2018-05-22/CreateCampaign.md "../../../goto/boto3/personalize-2018-05-22/CreateCampaign.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/personalize-2018-05-22/CreateCampaign.md "../../../goto/SdkForRubyV3/personalize-2018-05-22/CreateCampaign.md")
