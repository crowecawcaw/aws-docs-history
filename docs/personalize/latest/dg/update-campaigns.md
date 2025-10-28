# Updating an Amazon Personalize campaign's configuration

To change your campaign's [Minimum provisioned TPS](campaigns.md#min-tps-auto-scaling "campaigns.md#min-tps-auto-scaling"), manually deploy a
new solution version, or modify a campaign's configuration,
such as turning on the option to include metadata in recommendations, you must manually update the campaign.

The following doesn't require a manual campaign update:

- If your campaign uses automatic campaign updates, you don't have to update it to
  deploy the latest automatically or manually trained solution version of your solution. For more information, see
  [Automatic campaign updates](campaigns.md#create-campaign-automatic-latest-sv-update "campaigns.md#create-campaign-automatic-latest-sv-update").
- With User-Personalization-v2, User-Personalization, or Next-Best-Action, Amazon Personalize automatically updates your latest solution version
  every two hours to include new items or actions in recommendations. Your campaign automatically uses
  the updated solution version.
  You manually update a campaign with the Amazon Personalize console, AWS Command Line Interface (AWS CLI), or AWS SDKs.

###### Note

To update a campaign to turn on the option to include metadata in recommendations, you must have an Items dataset with a column of metadata. You don't have
to use the metadata in training.

If your campaign previously deployed a solution version that used
User-Personalization-v2 or Personalized-Ranking-v2, and you are switching to an older version of the recipes,
the option to include metadata is off by default. You can enable it when you update the campaign. For more information, see [Item metadata in recommendations](campaigns.md#create-campaign-return-metadata "campaigns.md#create-campaign-return-metadata").

###### Topics

- [Updating a campaign (console)](#update-campaign-console "#update-campaign-console")
- [Updating a campaign (AWS CLI)](#update-campaign-cli "#update-campaign-cli")
- [Updating a campaign (AWS SDKs)](#update-campaign-sdk "#update-campaign-sdk")

## Updating a campaign (console)

To deploy a manually retrained solution version or make changes to your campaign configuration, you must update your campaign.

###### To update a campaign (console)

1. Open the Amazon Personalize console at [https://console.aws.amazon.com/personalize/home](https://console.aws.amazon.com/personalize/home "https://console.aws.amazon.com/personalize/home") and sign into your
   account.
2. Choose the dataset group with the campaign you want to update.
3. In the navigation pane, choose **Campaigns**.
4. On the **Campaigns** page, choose the campaign you want to update.
5. On the campaign details page, choose **Update**.
6. On the **Update campaign** page, make your changes. For example, if you
   are deploying a retrained solution version, for **Solution version ID**, choose the identification number
   for the new solution version.
7. Choose **Update**. Amazon Personalize updates the campaign to use the new solution version and any changed configurations.

## Updating a campaign (AWS CLI)

To deploy a new solution version, change your campaign's [Minimum provisioned TPS](campaigns.md#min-tps-auto-scaling "campaigns.md#min-tps-auto-scaling"),
or change your campaign's configuration, you must update your campaign. Use the following `update-campaign` command to update a campaign
to use a new solution version with the AWS CLI.

Replace `campaign arn` with the Amazon Resource Name (ARN) of the campaign you want to update. Replace `new solution version arn` with the solution version you want to deploy.

```
aws personalize update-campaign \
--campaign-arn `campaign arn` \
--solution-version-arn `new solution version arn` \
--min-provisioned-tps `1`
```

## Updating a campaign (AWS SDKs)

To deploy a new solution version, change your campaign's [Minimum provisioned TPS](campaigns.md#min-tps-auto-scaling "campaigns.md#min-tps-auto-scaling")
or change your campaign's configuration, you must update your campaign.
Use the following code to update a campaign with the SDK for Python (Boto3) or SDK for Java 2.x.
For a complete list of parameters, see [UpdateCampaign](API_UpdateCampaign.md "API_UpdateCampaign.md").

SDK for Python (Boto3)
Use the following `update_campaign` method to deploy a new solution version.
Replace `campaign arn` with the Amazon Resource Name (ARN) of the campaign you want to update, replace the
`new solution version arn` with the new solution version ARN and optionally change the `minProvisionedTPS`.

```
import boto3

personalize = boto3.client('personalize')

response = personalize.update_campaign(
    campaignArn = '`campaign arn`',
    solutionVersionArn = '`new solution version arn`',
    minProvisionedTPS = `1`,
)

arn = response['campaignArn']

description = personalize.describe_campaign(campaignArn = arn)['campaign']
print('Name: ' + description['name'])
print('ARN: ' + description['campaignArn'])
print('Status: ' + description['status'])
```

SDK for Java 2.xUse the following `updateCampaign` method to update a campaign to use a new solution version. Pass as parameters
an Amazon Personalize service client, the new solution version's Amazon Resource Name (ARN), and the [Minimum provisioned TPS](campaigns.md#min-tps-auto-scaling "campaigns.md#min-tps-auto-scaling").

```
public static void updateCampaign(PersonalizeClient personalizeClient,
                                String campaignArn,
                                String solutionVersionArn,
                                Integer minProvisionedTPS) {

    try {
        // build the updateCampaignRequest
        UpdateCampaignRequest updateCampaignRequest = UpdateCampaignRequest.builder()
            .campaignArn(campaignArn)
            .solutionVersionArn(solutionVersionArn)
            .minProvisionedTPS(minProvisionedTPS)
            .build();

        // update the campaign
        personalizeClient.updateCampaign(updateCampaignRequest);

        DescribeCampaignRequest campaignRequest = DescribeCampaignRequest.builder()
              .campaignArn(campaignArn)
              .build();

        DescribeCampaignResponse campaignResponse = personalizeClient.describeCampaign(campaignRequest);
        Campaign updatedCampaign = campaignResponse.campaign();

        System.out.println("The Campaign status is " + updatedCampaign.status());

    } catch (PersonalizeException e) {
        System.err.println(e.awsErrorDetails().errorMessage());
        System.exit(1);
    }
}
```
