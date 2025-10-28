# Importing training data

###### Note

You can only supply a training data set for using in a Clean Rooms ML lookalike model
that has data stored in Amazon S3. However, you can supply the seed data for a lookalike
model using SQL that runs across data stored in any supported data source.

Before you create a lookalike model, you must specify the AWS Glue table that contains
the training data. Clean Rooms ML doesn't store a copy of this data, just metadata that allows
it to access the data.

###### To import training data in AWS Clean Rooms

1. Sign in to the AWS Management Console and open the [AWS Clean Rooms console](https://console.aws.amazon.com/cleanrooms/home "https://console.aws.amazon.com/cleanrooms/home") with your AWS account (if you
   haven't yet done so).
2. In the left navigation pane, choose **AWS ML
   models**.
3. On the **Training datasets** tab, choose **Create
   training dataset**.
4. On the **Create training dataset** page, for
   **Training dataset details**, enter a
   **Name** and optional
   **Description**.
5. Choose the **Training data source** by selecting the
   **Database** and **Table** that you want
   to configure from the dropdown lists.

###### Note

To verify that this is the correct table, do either one of the
following:

    * Choose **View in AWS Glue**.
    * Turn on **View schema** to view the
     schema.

6. For **Training details**, choose the **User
   identifier column**, **Item identifier column**,
   and **Timestamp column** from the dropdown lists. The training
   data must contain these three columns. You can also select any other columns
   that you want to include in the training data.

The data in the **Timestamp column** must be in the Unix
epoch time in seconds format. 7. (Optional) If you have any **Additional columns to train**,
choose the **Column name** and **Type** from
the dropdown lists. 8. In **Service access**, you must specify a service role that
can access your data and provide a KMS key if your data is encrypted. Choose
**Create and use a new service role** and Clean Rooms ML will
automatically create a service role and add the necessary permissions policy.
Choose **Use an existing service role** and enter it in the
**Service role name** field if you have a specific service
role that you want to use.

If your data is encrypted, enter your KMS key in the
**AWS KMS key** field, or click **Create an
AWS KMS key** to generate a new KMS key. 9. If you want to enable **Tags** for the training dataset,
choose **Add new tag** and then enter the
**Key** and **Value** pair. 10. Choose **Create training dataset**.
For the corresponding API action, see [CreateTrainingDataset](../../../cleanrooms-ml/latest/APIReference/API_CreateTrainingDataset.md "../../../cleanrooms-ml/latest/APIReference/API_CreateTrainingDataset.md").
