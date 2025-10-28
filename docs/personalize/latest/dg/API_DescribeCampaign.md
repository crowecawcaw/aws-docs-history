# DescribeCampaign

Describes the given campaign, including its status.

A campaign can be in one of the following states:

- CREATE PENDING > CREATE IN_PROGRESS > ACTIVE -or- CREATE FAILED
- DELETE PENDING > DELETE IN_PROGRESS
  When the `status` is `CREATE FAILED`, the response includes the
  `failureReason` key, which describes why.

For more information on campaigns, see [CreateCampaign](API_CreateCampaign.md "API_CreateCampaign.md").

## Request Syntax

```
{
   "campaignArn": "`string`"
}
```

## Request Parameters

The request accepts the following data in JSON format.

**[campaignArn](#API_DescribeCampaign_RequestSyntax "#API_DescribeCampaign_RequestSyntax")**

The Amazon Resource Name (ARN) of the campaign.

Type: String

Length Constraints: Maximum length of 256.

Pattern: `arn:([a-z\d-]+):personalize:.*:.*:.+`

Required: Yes

## Response Syntax

```
{
   "campaign": {
      "campaignArn": "***string***",
      "campaignConfig": {
         "enableMetadataWithRecommendations": ***boolean***,
         "itemExplorationConfig": {
            "***string***" : "***string***"
         },
         "syncWithLatestSolutionVersion": ***boolean***
      },
      "creationDateTime": ***number***,
      "failureReason": "***string***",
      "lastUpdatedDateTime": ***number***,
      "latestCampaignUpdate": {
         "campaignConfig": {
            "enableMetadataWithRecommendations": ***boolean***,
            "itemExplorationConfig": {
               "***string***" : "***string***"
            },
            "syncWithLatestSolutionVersion": ***boolean***
         },
         "creationDateTime": ***number***,
         "failureReason": "***string***",
         "lastUpdatedDateTime": ***number***,
         "minProvisionedTPS": ***number***,
         "solutionVersionArn": "***string***",
         "status": "***string***"
      },
      "minProvisionedTPS": ***number***,
      "name": "***string***",
      "solutionVersionArn": "***string***",
      "status": "***string***"
   }
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[campaign](#API_DescribeCampaign_ResponseSyntax "#API_DescribeCampaign_ResponseSyntax")**

The properties of the campaign.

###### Note

The `latestCampaignUpdate` field is only returned when the campaign has had
at least one `UpdateCampaign` call.

Type: [Campaign](API_Campaign.md "API_Campaign.md") object

## Errors

**InvalidInputException**

Provide a valid value for the field or parameter.

HTTP Status Code: 400

**ResourceNotFoundException**

Could not find the specified resource.

HTTP Status Code: 400

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/personalize-2018-05-22/DescribeCampaign.md "../../../goto/cli2/personalize-2018-05-22/DescribeCampaign.md")
- [AWS SDK for .NET](../../../goto/DotNetSDKV3/personalize-2018-05-22/DescribeCampaign.md "../../../goto/DotNetSDKV3/personalize-2018-05-22/DescribeCampaign.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/personalize-2018-05-22/DescribeCampaign.md "../../../goto/SdkForCpp/personalize-2018-05-22/DescribeCampaign.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/personalize-2018-05-22/DescribeCampaign.md "../../../goto/SdkForGoV2/personalize-2018-05-22/DescribeCampaign.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/personalize-2018-05-22/DescribeCampaign.md "../../../goto/SdkForJavaV2/personalize-2018-05-22/DescribeCampaign.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/personalize-2018-05-22/DescribeCampaign.md "../../../goto/SdkForJavaScriptV3/personalize-2018-05-22/DescribeCampaign.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/personalize-2018-05-22/DescribeCampaign.md "../../../goto/SdkForKotlin/personalize-2018-05-22/DescribeCampaign.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/personalize-2018-05-22/DescribeCampaign.md "../../../goto/SdkForPHPV3/personalize-2018-05-22/DescribeCampaign.md")
- [AWS SDK for Python](../../../goto/boto3/personalize-2018-05-22/DescribeCampaign.md "../../../goto/boto3/personalize-2018-05-22/DescribeCampaign.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/personalize-2018-05-22/DescribeCampaign.md "../../../goto/SdkForRubyV3/personalize-2018-05-22/DescribeCampaign.md")
