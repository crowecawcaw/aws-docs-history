# Updating a configured lookalike

model

After you have associated a configured a lookalike model, you can update it to change
information such as the name, metrics to share, or output Amazon S3 location.

###### To update an associated configured lookalike model in AWS Clean Rooms

1. Sign in to the AWS Management Console and open the [AWS Clean Rooms console](https://console.aws.amazon.com/cleanrooms/home "https://console.aws.amazon.com/cleanrooms/home") with your AWS account (if you
   haven't yet done so).
2. In the left navigation pane, choose **AWS ML
   models**.
3. On the **Configured lookalike models** tab, under
   **Ready-to-use lookalike models**, choose a configured
   lookalike model and select **Edit**.
4. On the **Edit** page, for **Configured lookalike
   model association details**:
   1. Update the **Name** and optional
      **Description**.
   2. Choose the **Lookalike model** that you want
      configured from the dropdown list.
   3. Choose the **Minimum matching seed size** that you
      want. This is the minimum number of users in the seed data provider's
      data that overlap with users in the training data. This value must be
      greater than 0.

5. For **Metrics to share with other members**, choose whether
   you want the seed data provider in your collaboration to receive model metrics,
   including relevance scores.
6. For **Lookalike segment destination location**, enter the
   Amazon S3 bucket where lookalike segment is exported. This bucket must be located in
   the same region as your other resources.
7. For **Service access**, choose the **Existing service
   role name** that will be used to access this table.
8. For **Advanced bin size configuration**, choose how you want
   to configure the audience bin sizes.
9. Choose **Save changes**.
   For the corresponding API action, see [UpdateConfiguredAudienceModel](../apireference/API_UpdateConfiguredAudienceModel.md "../apireference/API_UpdateConfiguredAudienceModel.md").
