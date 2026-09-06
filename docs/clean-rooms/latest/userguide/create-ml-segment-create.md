

# Creating a lookalike segment
<a name="create-ml-segment-create"></a>

**Note**  
You can only supply a training data set for using in a Clean Rooms ML lookalike model that has data stored in Amazon S3. However, you can supply the seed data for a lookalike model using SQL that runs across data stored in any supported data source. 

A lookalike segment is a subset of the training data that most closely resembles the seed data.

**To create a lookalike segment in AWS Clean Rooms**

1. Sign in to the AWS Management Console and open the [AWS Clean Rooms console](https://console.aws.amazon.com/cleanrooms/home) with your AWS account (if you haven't yet done so).

1. In the left navigation pane, choose **Collaborations**.

1. On the **With active membership** tab, choose a collaboration.

1. On the **ML Models** tab, choose **Create lookalike segment**.

1. On the **Create lookalike segment** page, for **Associated configured lookalike model**, choose the associated configured lookalike model to use for this lookalike segment. 

   

1. For **Lookalike segment details** enter a **Name** and optional **Description**.

   

1. For **Seed profiles**, choose your **Seed method** by selecting an option and then taking the recommended action.    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/clean-rooms/latest/userguide/create-ml-segment-create.html)

1. Choose the **Worker type** to use when creating this data source. The default worker type is **CR.1X**. Specify the **Number of workers** to use. The default is worker number **16**. To specify **Spark properties**:

   1. Expand **Spark properties**.

   1. Choose **Add Spark properties**.

   1. On the **Spark properties** dialog box, choose a **Property name** from the dropdown list and enter a **Value**.

   The following tables provide a definition for each property.

   For more information about Spark properties, see [Spark Properties](https://spark.apache.org/docs/latest/configuration.html#spark-properties) in the Apache Spark documentation. 
**Note**  
You can configure a maximum of 50 Spark properties. Each property value can be up to 500 characters.    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/clean-rooms/latest/userguide/create-ml-segment-create.html)    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/clean-rooms/latest/userguide/create-ml-segment-create.html)

1. For **Service access**, choose the **Existing service role name** that will be used to access this table.

1. If you want to enable **Tags** for the training dataset, choose **Add new tag** and then enter the **Key** and **Value** pair. 

1. Choose **Create lookalike segment**. 

For the corresponding API action, see [StartAudienceGenerationJob](https://docs.aws.amazon.com/cleanrooms-ml/latest/APIReference/API_StartAudienceGenerationJob.html).