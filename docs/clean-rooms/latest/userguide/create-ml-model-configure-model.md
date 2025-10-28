# Configuring a lookalike model

After you have created a lookalike model, you are ready to configure it for use in a
collaboration. You can create multiple configured lookalike models from a single
lookalike model.

###### To configure a lookalike model in AWS Clean Rooms

1. Sign in to the AWS Management Console and open the [AWS Clean Rooms console](https://console.aws.amazon.com/cleanrooms/home "https://console.aws.amazon.com/cleanrooms/home") with your AWS account (if you
   haven't yet done so).
2. In the left navigation pane, choose **AWS ML
   models**.
3. On the **Configured lookalike models** tab, choose
   **Configure lookalike model**.
4. On the **Configure lookalike model** page, for
   **Configured lookalike model details**, enter a
   **Name** and optional
   **Description**.
   1. Choose the **Lookalike model** that you want to
      configure from the dropdown list.

   ###### Note

   To verify that this is the correct lookalike model, turn on
   **Show lookalike model details** to view the
   details.

   To create a new lookalike model, choose **Create lookalike
   model**. 2. Choose the **Minimum matching seed size** that you
   want. This is the minimum number of users in the seed data provider's
   data that overlap with users in the training data. This value must be
   greater than 0.

5. For **Metrics to share with other members**, choose whether
   you want the seed data provider in your collaboration to receive model metrics,
   including relevance scores.
6. For **Lookalike segment destination location**, enter the
   Amazon S3 bucket where the lookalike segment is exported. This bucket must be located
   in the same region as your other resources.
7. For **Service access**, choose the **Existing service
   role name** that will be used to access this table.
8. For **Advanced bin size configuration**, specify the
   **Audience size type** as either an
   **Absolute** number or a
   **Percentage**.
9. If you want to enable **Tags** for the configured table
   resource, choose **Add new tag** and then enter the
   **Key** and **Value** pair.
10. Choose **Configure lookalike model**.
    For the corresponding API action, see [CreateConfiguredAudienceModel](../../../cleanrooms-ml/latest/APIReference/API_CreateConfiguredAudienceModel.md "../../../cleanrooms-ml/latest/APIReference/API_CreateConfiguredAudienceModel.md").
