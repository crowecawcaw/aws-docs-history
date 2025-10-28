# Creating a lookalike segment

###### Note

You can only supply a training data set for using in a Clean Rooms ML lookalike model
that has data stored in Amazon S3. However, you can supply the seed data for a lookalike
model using SQL that runs across data stored in any supported data source.

A lookalike segment is a subset of the training data that most closely resembles the
seed data.

###### To create a lookalike segment in AWS Clean Rooms

1. Sign in to the AWS Management Console and open the [AWS Clean Rooms console](https://console.aws.amazon.com/cleanrooms/home "https://console.aws.amazon.com/cleanrooms/home") with your AWS account (if you
   haven't yet done so).
2. In the left navigation pane, choose
   **Collaborations**.
3. On the **With active membership** tab, choose a
   collaboration.
4. On the **ML Models** tab, choose **Create lookalike
   segment**.
5. On the **Create lookalike segment** page, for
   **Associated configured lookalike model**, choose the
   associated configured lookalike model to use for this lookalike segment.
6. For **Lookalike segment details** enter a
   **Name** and optional
   **Description**.
7. For **Seed profiles**, choose your **Seed
   method** by selecting an option and then taking the recommended
   action.

| Option                | Recommended action                                                                                      |
| --------------------- | ------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Amazon S3 path**    | 1. Select an Amazon S3 location. 2. (Optional) Choose **Include seed profiles in the output**.          |
| **SQL query**         | Write a SQL query and use its results as the seed data.                                                 |
| **Analysis template** | Choose an analysis template from the dropdown list and use the results created by an analysis template. | 8. Choose the **Worker type** and **Number of workers** to use when creating this data channel. 9. For **Service access**, choose the **Existing service role name** that will be used to access this table. 10. If you want to enable **Tags** for the training dataset, choose **Add new tag** and then enter the **Key** and **Value** pair. 11. Choose **Create lookalike segment**. For the corresponding API action, see [StartAudienceGenerationJob](../../../cleanrooms-ml/latest/APIReference/API_StartAudienceGenerationJob.md "../../../cleanrooms-ml/latest/APIReference/API_StartAudienceGenerationJob.md"). |
