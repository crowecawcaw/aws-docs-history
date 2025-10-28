# Campaign

An object that describes the deployment of a solution version.
For more information on campaigns, see [CreateCampaign](API_CreateCampaign.md "API_CreateCampaign.md").

## Contents

**campaignArn**

The Amazon Resource Name (ARN) of the campaign.

Type: String

Length Constraints: Maximum length of 256.

Pattern: `arn:([a-z\d-]+):personalize:.*:.*:.+`

Required: No

**campaignConfig**

The configuration details of a campaign.

Type: [CampaignConfig](API_CampaignConfig.md "API_CampaignConfig.md") object

Required: No

**creationDateTime**

The date and time (in Unix format) that the campaign was created.

Type: Timestamp

Required: No

**failureReason**

If a campaign fails, the reason behind the failure.

Type: String

Required: No

**lastUpdatedDateTime**

The date and time (in Unix format) that the campaign was last updated.

Type: Timestamp

Required: No

**latestCampaignUpdate**

Provides a summary of the properties of a campaign update. For a complete listing, call the [DescribeCampaign](API_DescribeCampaign.md "API_DescribeCampaign.md") API.

###### Note

The `latestCampaignUpdate` field is only returned when the campaign has had
at least one `UpdateCampaign` call.

Type: [CampaignUpdateSummary](API_CampaignUpdateSummary.md "API_CampaignUpdateSummary.md") object

Required: No

**minProvisionedTPS**

Specifies the requested minimum provisioned transactions (recommendations) per second. A high `minProvisionedTPS` will increase your bill. We recommend starting with 1 for `minProvisionedTPS` (the default). Track
your usage using Amazon CloudWatch metrics, and increase the `minProvisionedTPS`
as necessary.

Type: Integer

Valid Range: Minimum value of 1.

Required: No

**name**

The name of the campaign.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 63.

Pattern: `^[a-zA-Z0-9][a-zA-Z0-9\-_]*`

Required: No

**solutionVersionArn**

The Amazon Resource Name (ARN) of the solution version the campaign uses.

Type: String

Length Constraints: Maximum length of 256.

Pattern: `arn:([a-z\d-]+):personalize:.*:.*:.+`

Required: No

**status**

The status of the campaign.

A campaign can be in one of the following states:

- CREATE PENDING > CREATE IN_PROGRESS > ACTIVE -or- CREATE FAILED
- DELETE PENDING > DELETE IN_PROGRESS

Type: String

Length Constraints: Maximum length of 256.

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/personalize-2018-05-22/Campaign.md "../../../goto/SdkForCpp/personalize-2018-05-22/Campaign.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/personalize-2018-05-22/Campaign.md "../../../goto/SdkForJavaV2/personalize-2018-05-22/Campaign.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/personalize-2018-05-22/Campaign.md "../../../goto/SdkForRubyV3/personalize-2018-05-22/Campaign.md")
