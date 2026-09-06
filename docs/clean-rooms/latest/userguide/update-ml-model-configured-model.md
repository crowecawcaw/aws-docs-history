

# Updating a configured lookalike model
<a name="update-ml-model-configured-model"></a>

After you have associated a configured a lookalike model, you can update it to change information such as the name, metrics to share, or output Amazon S3 location.

**To update an associated configured lookalike model in AWS Clean Rooms**

1. Sign in to the AWS Management Console and open the [AWS Clean Rooms console](https://console.aws.amazon.com/cleanrooms/home) with your AWS account (if you haven't yet done so).

1. In the left navigation pane, choose **AWS ML models**.

1. On the **Configured lookalike models** tab, under **Ready-to-use lookalike models**, choose a configured lookalike model and select **Edit**.

1. On the **Edit** page, for **Configured lookalike model association details**: 

   1. Update the **Name** and optional **Description**.

   1. Choose the **Lookalike model** that you want configured from the dropdown list.

   1. Choose the **Minimum matching seed size** that you want. This is the minimum number of users in the seed data provider's data that overlap with users in the training data. This value must be greater than 0.

1. For **Metrics to share with other members**, choose whether you want the seed data provider in your collaboration to receive model metrics, including relevance scores. 

1. For **Lookalike segment destination location**, enter the Amazon S3 bucket where lookalike segment is exported. This bucket must be located in the same region as your other resources.

1. For **Service access**, choose the **Existing service role name** that will be used to access this table.

1. For **Advanced bin size configuration**, choose how you want to configure the audience bin sizes.

1. Choose **Save changes**. 

For the corresponding API action, see [UpdateConfiguredAudienceModel](https://docs.aws.amazon.com/clean-rooms/latest/apireference/API_UpdateConfiguredAudienceModel.html).