# Deploying an Amazon Personalize solution version with a campaign

For real-time recommendations with custom resources, after you complete [Manually creating a solution version](creating-a-solution-version.md "creating-a-solution-version.md"),
you are ready to deploy your solution version with a campaign.

A _campaign_ deploys a solution version (trained model) with a provisioned transaction capacity for generating real-time recommendations.
After you create a campaign, you use the
[GetRecommendations](API_RS_GetRecommendations.md "API_RS_GetRecommendations.md") or [GetPersonalizedRanking](API_RS_GetPersonalizedRanking.md "API_RS_GetPersonalizedRanking.md")
API operations to get recommendations. If you are getting batch item recommendations or user segments, you don't need to create a campaign.
For more information, see [Getting batch item recommendations](getting-batch-recommendations.md "getting-batch-recommendations.md") or [Getting batch user segments](getting-user-segments.md "getting-user-segments.md").

When you create a campaign, you can configure the following:

- You can configure the campaign to automatically update to use your solution's latest solution version. For more
  information see [Automatic campaign updates](#create-campaign-automatic-latest-sv-update "#create-campaign-automatic-latest-sv-update").
- You can enable item metadata in recommendations. For more information, see [Item metadata in recommendations](#create-campaign-return-metadata "#create-campaign-return-metadata").
- You can specify the minimum provisioned transactions per second for the campaign. This is the baseline
  transaction throughput for the campaign provisioned by Amazon Personalize. It sets the minimum billing charge for the
  campaign while it is active. For more information, see [Minimum provisioned transactions per second and auto-scaling](#min-tps-auto-scaling "#min-tps-auto-scaling").
  You can create a campaign with the Amazon Personalize console, AWS Command Line Interface (AWS CLI), or AWS SDKs. If you want to change an existing campaign's settings, such as enabling
  metadata in recommendations, you must update your campaign. For more information, see [Updating an Amazon Personalize campaign's configuration](update-campaigns.md "update-campaigns.md").

You incur campaign costs while the campaign is active. To avoid unnecessary costs, make sure to delete the campaign when you are finished. For information about campaign
costs, see [Amazon Personalize pricing](https://aws.amazon.com/personalize/pricing/ "https://aws.amazon.com/personalize/pricing/").

###### Topics

- [Automatic campaign updates](#create-campaign-automatic-latest-sv-update "#create-campaign-automatic-latest-sv-update")
- [Minimum provisioned transactions per second and auto-scaling](#min-tps-auto-scaling "#min-tps-auto-scaling")
- [Item metadata in recommendations](#create-campaign-return-metadata "#create-campaign-return-metadata")
- [Creating a campaign (console)](#create-campaign-console "#create-campaign-console")
- [Creating a campaign (AWS CLI)](#create-campaign-cli "#create-campaign-cli")
- [Creating a campaign (AWS SDKs)](#create-campaign-sdk "#create-campaign-sdk")

## Automatic campaign updates

When you create a campaign, you can enable automatic campaign updates. With automatic updates, the campaign
automatically updates to deploy the latest automatically or manually trained solution version of your solution. This
makes it easier for you to keep your campaign current.

For example, if your solution uses [automatic training](solution-config-auto-training.md "solution-config-auto-training.md") to create a new solution version every seven
days, your campaign would automatically update to use the latest solution version for every weekly training. If you
don't use automatic campaign updates, you must manually update the campaign to deploy the latest trained model.

- To enable automatic campaign updates when you create a campaign with the Amazon Personalize console, choose
  **Automatically update to use your solution's latest solution version** in the
  **Campaign details**. You can find the timestamp for the latest update on the campaign
  details page.

For more information, see [Creating a campaign (console)](#create-campaign-console "#create-campaign-console").

- To enable automatic campaign updates when you use the [CreateCampaign](API_CreateCampaign.md "API_CreateCampaign.md") API operation, for
  the `SolutionVersionArn` parameter, specify the Amazon Resource Name (ARN) of your solution in
  `SolutionArn/$LATEST` format. In the `campaignConfig`, set
  `enableMetadataWithRecommendations` to `true`.

To get the timestamp of the latest campaign update, you can use the [DescribeCampaign](API_DescribeCampaign.md "API_DescribeCampaign.md") API operation and check `latestCampaignUpdate` details
in the response.

For code samples that show you how to enable automatic updates, see [Creating a campaign (AWS CLI)](#create-campaign-cli "#create-campaign-cli") or [Creating a campaign (AWS SDKs)](#create-campaign-sdk "#create-campaign-sdk").

## Minimum provisioned transactions per second and auto-scaling

###### Important

A high `minProvisionedTPS` will increase your cost. We recommend starting with 1 for `minProvisionedTPS` (the default). Track
your usage using Amazon CloudWatch metrics, and increase the `minProvisionedTPS` as necessary.

When you create an Amazon Personalize campaign, you can specify the minimum provisioned transactions per second
(`minProvisionedTPS`) for the campaign. This is the baseline transaction throughput for the campaign provisioned by
Amazon Personalize. It sets the minimum billing charge for the campaign while it is active. A transaction is a single `GetRecommendations` or
`GetPersonalizedRanking` request. The default `minProvisionedTPS` is 1.

If your TPS increases beyond the `minProvisionedTPS`, Amazon Personalize auto-scales the provisioned capacity up
and down, but never below `minProvisionedTPS`.
There's a short time delay while the capacity is increased
that might cause loss of transactions. When your traffic reduces, capacity returns to the `minProvisionedTPS`.

You are charged for the minimum provisioned TPS or, if your requests exceed the `minProvisionedTPS`, the
actual TPS. The actual TPS is the total number of recommendation requests you make. We recommend starting with a low
`minProvisionedTPS`, track your usage using Amazon CloudWatch metrics, and then increase the
`minProvisionedTPS` as necessary.

For more information about campaign costs, see [Amazon Personalize pricing](https://aws.amazon.com/personalize/pricing/ "https://aws.amazon.com/personalize/pricing/").

## Item metadata in recommendations

###### Important

If you use the User-Personalization-v2 or Personalized-Ranking-v2 recipe, you don't incur additional costs for metadata. For all
other recipes and all domain use cases, you incur additional costs. For more information, see [Amazon Personalize pricing](https://aws.amazon.com/personalize/pricing/ "https://aws.amazon.com/personalize/pricing/").

When you get recommendations, you can have Amazon Personalize include item metadata in recommendation results.
In your request, you can choose the columns from your Items dataset to include. Amazon Personalize returns this data for each item in the recommendation response.

You might use metadata to enrich recommendations in your user interface, such as adding the genres for
movies to carousels. Or you might use it to visually assess recommendation quality. If you use generative AI in your app, you can plug the
metadata into AI prompts to generate more relevant content. For more information about using Amazon Personalize with generative AI, see
[Amazon Personalize and generative AI](personalize-with-gen-ai.md "personalize-with-gen-ai.md").

### Enabling metadata

To add metadata to recommendations, you must have an Items dataset with a column of metadata. You don't have
to use the metadata in training. For information
about creating a dataset, see [Creating a schema and a dataset](data-prep-creating-datasets.md "data-prep-creating-datasets.md"). For information updating data, see [Updating data in datasets after training](updating-datasets.md "updating-datasets.md").

If you use the User-Personalization-v2 or Personalized-Ranking-v2 recipe,
new campaigns automatically have the option to include item metadata with recommendation results. You don't have manually enable metadata for
your campaign.
For all other recipes and domain use cases, you must enable the metadata option:

- To enable metadata with the Amazon Personalize console, when you create the campaign, choose **Return items
  metadata in recommendation results** in the **Campaign details**. For more
  information, see [Creating a campaign (console)](#create-campaign-console "#create-campaign-console").
- To enable metadata with the AWS SDKs or AWS CLI, use the [CreateCampaign](API_CreateCampaign.md "API_CreateCampaign.md") API operation and in the `campaignConfig` set
  `enableMetadataWithRecommendations` to `true`. For more information, see [Creating a campaign (AWS CLI)](#create-campaign-cli "#create-campaign-cli") or [Creating a campaign (AWS SDKs)](#create-campaign-sdk "#create-campaign-sdk").

## Creating a campaign (console)

###### Important

You incur campaign costs while the campaign is active. To avoid unnecessary costs, make sure to delete the campaign when you are finished. For information about campaign
costs, see [Amazon Personalize pricing](https://aws.amazon.com/personalize/pricing/ "https://aws.amazon.com/personalize/pricing/").

After your solution version status is Active, you are ready to deploy it with an Amazon Personalize campaign.

###### To create a campaign (console)

1. Open the Amazon Personalize console at [https://console.aws.amazon.com/personalize/home](https://console.aws.amazon.com/personalize/home "https://console.aws.amazon.com/personalize/home") and sign into your
   account.
2. Choose the dataset group with the solution version that you want to deploy.
3. In the navigation pane, under **Custom resources**, choose **Campaigns**.
4. On the **Campaigns** page, choose **Create campaign**.
5. On the **Create new campaign** page, for **Campaign details**, provide the following information:
   - **Campaign name** – Enter the name of the
     campaign. The text you enter here appears on the Campaign dashboard and
     details page.
   - **Solution** – Choose the solution that
     you just created.
   - **Automatically update to use your solution's latest solution version**
     – Choose this option to have the campaign automatically use the latest active solution version.
     If you don't choose this, you must manually update the campaign each time you want to deploy a new
     solution version. For more information, see [Automatic campaign updates](#create-campaign-automatic-latest-sv-update "#create-campaign-automatic-latest-sv-update").
   - **Solution version ID** – If you don't use automatic campaign updates to use the latest solution version,
     choose the ID of the solution version that you want to deploy.
   - **Minimum provisioned transactions per second (called minProvisionedTPS in
     APIs)** – Set the minimum provisioned transactions per second that Amazon Personalize
     supports. A high value will increase your charges. We recommend that you start with 1 (the default).
     Track your usage by using Amazon CloudWatch metrics, and increase the `minProvisionedTPS` as
     necessary. For more information, see [Minimum provisioned transactions per second and auto-scaling](#min-tps-auto-scaling "#min-tps-auto-scaling").
   - **Return items metadata in recommendation results** – Choose
     this option if you want the option to include metadata with recommendation results. If enabled, you
     can specify the columns from your Items dataset when you get recommendations. For more information,
     see [Item metadata in recommendations](#create-campaign-return-metadata "#create-campaign-return-metadata").

6. If you used the User-Personalization recipe, in **Campaign configuration**, you can
   optionally enter values for the **Exploration weight** and **Exploration item age cut
   off**. For more information, see [User-Personalization](native-recipe-new-item-USER_PERSONALIZATION.md "native-recipe-new-item-USER_PERSONALIZATION.md").
7. For **Tags**, optionally add any tags. For more information about tagging Amazon Personalize resources, see
   [Tagging Amazon Personalize resources](tagging-resources.md "tagging-resources.md").
8. Choose **Create campaign**.
9. On the campaign details page, when the campaign status is **Active**, you can use the campaign to get
   recommendations and record impressions. For more information, see [Getting recommendations from Amazon Personalize](getting-recommendations.md "getting-recommendations.md").

The campaign is ready when its status is ACTIVE. If you retrain your solution version, or if you want to
change your campaign settings, you must update your campaign. For more information, see [Updating an Amazon Personalize campaign's configuration](update-campaigns.md "update-campaigns.md").

## Creating a campaign (AWS CLI)

###### Important

You incur campaign costs while the campaign is active. To avoid unnecessary costs, make sure to delete the campaign when you are finished. For information about campaign
costs, see [Amazon Personalize pricing](https://aws.amazon.com/personalize/pricing/ "https://aws.amazon.com/personalize/pricing/").

After your solution version is Active, you are ready to deploy it with an Amazon Personalize campaign.
To create a campaign with the AWS CLI, you use the `create-campaign` command.

The following code sample shows you how to create a campaign. It deploys the latest solution version of a solution
that uses the User-Personalization recipe. The campaign it creates automatically updates to use future solution
versions. The code uses the following configuration:

- It configures the campaign to automatically update to use the latest solution version for your solution: The
  `solution-version-arn` is in ``solution ARN`/$LATEST`format, and`syncWithLatestSolutionVersion`is`True`. To use the code, replace
`solution ARN` with the Amazon Resource Name (ARN) of your solution.

To disable automatic `syncWithLatestSolutionVersion`, specify only the solution version ARN
(without `/$LATEST`), and set `syncWithLatestSolutionVersion` to `False`.

- It sets the `enableMetadataWithRecommendations` option to `True`. This enables a
  recommendation request option to include item metadata from an Items dataset with recommendation results. To
  disable this option, set it to `False`. For more information, see [Item metadata in recommendations](#create-campaign-return-metadata "#create-campaign-return-metadata").
- It sets `min-provisioned-tps` to 1 (the default). We recommend starting with 1 for
  `minProvisionedTPS` (the default). Track your usage by using Amazon CloudWatch metrics, and increase the
  `minProvisionedTPS` as necessary. For more information, see [Minimum provisioned transactions per second and auto-scaling](#min-tps-auto-scaling "#min-tps-auto-scaling").

For a complete list of all parameters, see [CreateCampaign](API_CreateCampaign.md "API_CreateCampaign.md").

```
aws personalize create-campaign \
--name `campaign-name` \
--solution-version-arn `solution-arn`/\$LATEST \
--min-provisioned-tps 1 \
--campaign-config "{"\"syncWithLatestSolutionVersion"\": "true", "\"enableMetadataWithRecommendations"\": "true"}"
```

The campaign is ready when its status is ACTIVE. To get the current status,
call [DescribeCampaign](API_DescribeCampaign.md "API_DescribeCampaign.md") and
check that the `status` field is `ACTIVE`.

If you retrain your solution version and your campaign doesn't automatically update to use the latest solution
version, or if your want to change your campaign settings, you must update your campaign. For more information, see
[Updating an Amazon Personalize campaign's configuration](update-campaigns.md "update-campaigns.md").

Amazon Personalize provides you with operations for managing campaigns such as [ListCampaigns](API_ListCampaigns.md "API_ListCampaigns.md") to list the campaigns that you have created. You can delete a campaign by
calling [DeleteCampaign](API_DeleteCampaign.md "API_DeleteCampaign.md"). If you delete a campaign, the
solution versions that are part of the campaign are not deleted.

After you have created your campaign, you can use it to make recommendations. For more information, see [Getting recommendations from Amazon Personalize](getting-recommendations.md "getting-recommendations.md").

## Creating a campaign (AWS SDKs)

###### Important

You incur campaign costs while the campaign is active. To avoid unnecessary costs, make sure to delete the campaign when you are finished. For information about campaign
costs, see [Amazon Personalize pricing](https://aws.amazon.com/personalize/pricing/ "https://aws.amazon.com/personalize/pricing/").

After your solution version is Active, you are ready to deploy it with an Amazon Personalize campaign. To create a campaign with
AWS SDKs, you use the [CreateCampaign](API_CreateCampaign.md "API_CreateCampaign.md") API operation.

The following code sample shows you how to create a campaign. The code deploys the latest solution version of a
solution that uses the User-Personalization recipe. The campaign it creates automatically updates to use future
solution versions. The code uses the following configuration:

- It configures the campaign to automatically update to use the latest solution version for your solution: The
  `solutionVersionArn` is in ``solution ARN`/$LATEST`format,
and`syncWithLatestSolutionVersion`is`True`. To use the code, replace `solution
  ARN` with the Amazon Resource Name (ARN) of your solution version.

To disable automatic `syncWithLatestSolutionVersion`, specify only the solution version ARN
(without `/$LATEST`), and set `syncWithLatestSolutionVersion` to `False`.

- It sets the `enableMetadataWithRecommendations` option to `True`. This enables a
  recommendation request option to include item metadata from an Items dataset with recommendation results. To
  disable this option, set it to `False`. For more information, see [Item metadata in recommendations](#create-campaign-return-metadata "#create-campaign-return-metadata").
- It sets `minProvisionedTPS` to 1 (the default). We recommend that you start with 1 for
  `minProvisionedTPS` (the default). Track your usage by using Amazon CloudWatch metrics, and increase the
  `minProvisionedTPS` as necessary. For more information, see [Minimum provisioned transactions per second and auto-scaling](#min-tps-auto-scaling "#min-tps-auto-scaling").

For a complete list of all parameters, see [CreateCampaign](API_CreateCampaign.md "API_CreateCampaign.md").

SDK for Python (Boto3)

```
import boto3

personalize = boto3.client('personalize')

response = personalize.create_campaign(
    name = '`campaign name`',
    solutionVersionArn = '`solution ARN`/$LATEST',
    minProvisionedTPS = `1`,
    campaignConfig = {"syncWithLatestSolutionVersion": `True`, "enableMetadataWithRecommendations": `True`}
)

arn = response['campaignArn']

description = personalize.describe_campaign(campaignArn = arn)['campaign']
print('Name: ' + description['name'])
print('ARN: ' + description['campaignArn'])
print('Status: ' + description['status'])
```

SDK for JavaScript v3

```
// Get service clients module and commands using ES6 syntax.
import { CreateCampaignCommand, PersonalizeClient } from
  "@aws-sdk/client-personalize";

// create personalizeClient
const personalizeClient = new PersonalizeClient({ region: "REGION" });

// set the campaign parameters
export const createCampaignParam = {
  solutionVersionArn: "SOLUTION_ARN/$LATEST" /* required */,
  name: "NAME" /* required */,
  minProvisionedTPS: 1 /* optional */,
  campaignConfig: {   /* optional */
    syncWithLatestSolutionVersion: true,
    enableMetadataWithRecommendations: true,
  },
};

export const run = async () => {
  try {
    const response = await personalizeClient.send(
      new CreateCampaignCommand(createCampaignParam)
    );
    console.log("Success", response);
    return response; // For unit tests.
  } catch (err) {
    console.log("Error", err);
  }
};
run();
```

The campaign is ready when its status is ACTIVE. To get the current status, call [DescribeCampaign](API_DescribeCampaign.md "API_DescribeCampaign.md"), and check that the `status`
field is `ACTIVE`.

If you manually retrain your solution version, or if you want to change your campaign settings, you must update your
campaign. For more information, see [Updating an Amazon Personalize campaign's configuration](update-campaigns.md "update-campaigns.md").

Amazon Personalize provides you with operations for managing campaigns such as [ListCampaigns](API_ListCampaigns.md "API_ListCampaigns.md") to list the campaigns that you have created. You can delete a campaign by
calling [DeleteCampaign](API_DeleteCampaign.md "API_DeleteCampaign.md"). If you delete a campaign, the
solution versions that are part of the campaign are not deleted.

After you have created your campaign, use it to make
recommendations. For more information, see
[Getting recommendations from Amazon Personalize](getting-recommendations.md "getting-recommendations.md").
