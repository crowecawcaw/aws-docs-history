# UpdateCampaign

Updates a campaign to deploy a retrained solution version with an existing campaign, change your campaign's `minProvisionedTPS`,
or modify your campaign's configuration. For example, you can set `enableMetadataWithRecommendations` to true for an existing campaign.

To update a campaign to start automatically using the latest solution version, specify the following:

- For the `SolutionVersionArn` parameter, specify the Amazon Resource Name (ARN) of your solution in
  `SolutionArn/$LATEST` format.
- In the `campaignConfig`, set `syncWithLatestSolutionVersion` to `true`.
  To update a campaign, the campaign status must be ACTIVE or CREATE FAILED.
  Check the campaign status using the [DescribeCampaign](API_DescribeCampaign.md "API_DescribeCampaign.md") operation.

###### Note

You can still get recommendations from a campaign while an update is in progress.
The campaign will use the previous solution version and campaign configuration to generate recommendations until the latest campaign update status is `Active`.

For more information about updating a campaign, including code samples, see [Updating a campaign](update-campaigns.md "update-campaigns.md").
For more information about campaigns, see [Creating a campaign](campaigns.md "campaigns.md").

## Request Syntax

```
{
   "campaignArn": "`string`",
   "campaignConfig": {
      "enableMetadataWithRecommendations": `boolean`,
      "itemExplorationConfig": {
         "`string`" : "`string`"
      },
      "rankingInfluence": {
         "`string`" : `number`
      },
      "syncWithLatestSolutionVersion": `boolean`
   },
   "minProvisionedTPS": `number`,
   "solutionVersionArn": "`string`"
}
```

## Request Parameters

The request accepts the following data in JSON format.

**[campaignArn](#API_UpdateCampaign_RequestSyntax "#API_UpdateCampaign_RequestSyntax")**

The Amazon Resource Name (ARN) of the campaign.

Type: String

Length Constraints: Maximum length of 256.

Pattern: `arn:([a-z\d-]+):personalize:.*:.*:.+`

Required: Yes

**[campaignConfig](#API_UpdateCampaign_RequestSyntax "#API_UpdateCampaign_RequestSyntax")**

The configuration details of a campaign.

Type: [CampaignConfig](API_CampaignConfig.md "API_CampaignConfig.md") object

Required: No

**[minProvisionedTPS](#API_UpdateCampaign_RequestSyntax "#API_UpdateCampaign_RequestSyntax")**

Specifies the requested minimum provisioned transactions (recommendations) per second that
Amazon Personalize will support. A high `minProvisionedTPS` will increase your bill. We recommend starting with 1 for `minProvisionedTPS` (the default). Track
your usage using Amazon CloudWatch metrics, and increase the `minProvisionedTPS`
as necessary.

Type: Integer

Valid Range: Minimum value of 1.

Required: No

**[solutionVersionArn](#API_UpdateCampaign_RequestSyntax "#API_UpdateCampaign_RequestSyntax")**

The Amazon Resource Name (ARN) of a new model to deploy. To specify the latest solution version of your solution,
specify the ARN of your _solution_ in `SolutionArn/$LATEST` format.
You must use this format if you set `syncWithLatestSolutionVersion` to `True` in the
[CampaignConfig](API_CampaignConfig.md "API_CampaignConfig.md").

To deploy a model that isn't the latest solution version of your solution, specify the ARN of the solution version.

For more information about automatic campaign updates, see
[Enabling automatic campaign updates](campaigns.md#create-campaign-automatic-latest-sv-update "campaigns.md#create-campaign-automatic-latest-sv-update").

Type: String

Length Constraints: Maximum length of 256.

Pattern: `arn:([a-z\d-]+):personalize:.*:.*:.+`

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

**[campaignArn](#API_UpdateCampaign_ResponseSyntax "#API_UpdateCampaign_ResponseSyntax")**

The same campaign ARN as given in the request.

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

- [AWS Command Line Interface V2](../../../goto/cli2/personalize-2018-05-22/UpdateCampaign.md "../../../goto/cli2/personalize-2018-05-22/UpdateCampaign.md")
- [AWS SDK for .NET V4](../../../goto/DotNetSDKV4/personalize-2018-05-22/UpdateCampaign.md "../../../goto/DotNetSDKV4/personalize-2018-05-22/UpdateCampaign.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/personalize-2018-05-22/UpdateCampaign.md "../../../goto/SdkForCpp/personalize-2018-05-22/UpdateCampaign.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/personalize-2018-05-22/UpdateCampaign.md "../../../goto/SdkForGoV2/personalize-2018-05-22/UpdateCampaign.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/personalize-2018-05-22/UpdateCampaign.md "../../../goto/SdkForJavaV2/personalize-2018-05-22/UpdateCampaign.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/personalize-2018-05-22/UpdateCampaign.md "../../../goto/SdkForJavaScriptV3/personalize-2018-05-22/UpdateCampaign.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/personalize-2018-05-22/UpdateCampaign.md "../../../goto/SdkForKotlin/personalize-2018-05-22/UpdateCampaign.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/personalize-2018-05-22/UpdateCampaign.md "../../../goto/SdkForPHPV3/personalize-2018-05-22/UpdateCampaign.md")
- [AWS SDK for Python](../../../goto/boto3/personalize-2018-05-22/UpdateCampaign.md "../../../goto/boto3/personalize-2018-05-22/UpdateCampaign.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/personalize-2018-05-22/UpdateCampaign.md "../../../goto/SdkForRubyV3/personalize-2018-05-22/UpdateCampaign.md")
