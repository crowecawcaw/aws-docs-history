

# Creating a lookalike model
<a name="create-ml-model-create-model"></a>

After you have created a training dataset, you are ready to create a lookalike model. You can create many lookalike models from a single training dataset.

You must create a default database in your AWS Glue Data Catalog or include the `glue:createDatabase` permission in the provided role.

**To create a lookalike model in AWS Clean Rooms**

1. Sign in to the AWS Management Console and open the [AWS Clean Rooms console](https://console.aws.amazon.com/cleanrooms/home) with your AWS account (if you haven’t yet done so).

1. In the left navigation pane, choose **AWS ML models**.

1. On the **Lookalike models** tab, choose **Create lookalike model**.

1. On the **Create lookalike model** page, for **Lookalike model details**, enter a **Name** and optional **Description**.

   1. Choose the **Training dataset** that you want to model from the dropdown list.
**Note**  
To verify that this is the correct training dataset, turn on **Show training dataset details** to view the details.  
To create a new training dataset, choose **Create training dataset**.

   1. (Optional) Enter a **Training window**.

1. If you want to enable custom encryption settings for the lookalike model, choose **Customize encryption settings** and then enter the KMS key.

1. If you want to enable **Tags** for the lookalike model, choose **Add new tag** and then enter the **Key** and **Value** pair. 

1. Choose **Create lookalike model**. 
**Note**  
Model training can take several hours to 2 days.

For the corresponding API action, see [CreateAudienceModel](https://docs.aws.amazon.com/cleanrooms-ml/latest/APIReference/API_CreateAudienceModel.html).