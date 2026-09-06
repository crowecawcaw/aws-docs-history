

# Creating an ML input channel in AWS Clean Rooms ML
<a name="create-ml-input-channel"></a>

**Prerequisites: **
+ An AWS account with access to AWS Clean Rooms
+ A collaboration set up in AWS Clean Rooms where you want to create the ML input channel
+ Permissions to query data and create ML input channels in the collaboration. 
+ (Optional) An existing model algorithm to associate with the ML input channel, or permissions to create a new one
+ (Optional) Tables with analysis rules that can be run for your specified model. 
+ (Optional) An existing SQL query or analysis template to use for generating the dataset
+ (Optional) An existing service role with appropriate permissions, or permissions to create a new service role
+ (Optional) A custom AWS KMS key if you want to use your own encryption key
+ Appropriate permissions to create and manage ML models in the collaboration

An *ML input channel* is a dataset that is created from a specific data query. Members with the ability to query data can prepare their data for training and inference by creating an ML input channel. Creating an ML input channel allows that data to be used in different training models within the same collaboration. You should create separate ML input channels for training and inference.

To create an ML input channel, you must specify the SQL query that is used to query the input data and create the ML input channel. The results of this query are never shared with any member and remain within the boundaries of Clean Rooms ML. The reference Amazon Resource Name (ARN) is used in the next steps to train a model or run inference.

------
#### [ Console ]

**To create an ML input channel (console)**

1. Sign in to the AWS Management Console and open the AWS Clean Rooms console at [https://console.aws.amazon.com/cleanrooms](https://console.aws.amazon.com/cleanrooms/home).

1. In the left navigation pane, choose **Collaborations**.

1. On the **Collaborations** page, choose the collaboration where you want to create an ML input channel.

1. After the collaboration opens, choose the **ML models** tab.

1. Under **Custom ML models**, in the **ML input channels** section, choose **Create ML input channel**.

1. On the **Create ML input channel** page, for **ML input channel details**, do the following: 

   1. For **Name**, enter a unique name for your channel.

   1. (Optional) For **Description**, enter a description of your channel.

   1. For **Associated model algorithm**, select the algorithm to use.

      Choose **Associate model algorithm** to add a new one.

1. For **Dataset**, choose a method to generate the training dataset:
   + Choose **SQL query** to use the results of a SQL query as the training dataset. 

     If you chose **SQL query**, enter your query in the **SQL query** field.

     (Optional) To import a query you've used recently, choose **Import from recent queries**. 
   + Choose **Analysis template** to use the results of an analysis template as the training dataset.
**Warning**  
Synthetic data generation protects against inferring individual attributes whether specific individuals are present in the original dataset or learning attributes of those individuals are present. However, it doesn't prevent literal values from the original dataset, including personally identifiable information (PII) from appearing in the synthetic dataset.  
We recommend avoiding values in the input dataset that are associated with only one data subject because these may re-identify a data subject. For example, if only one user lives in a zip code, the presence of that zip code in the synthetic dataset would confirm that user was in the original dataset. Techniques like truncating high precision values or replacing uncommon catalogues with *other* can be used to mitigate this risk. These transformations can be part of the query used to create the ML input channel.

   1. If no tables are associated, choose **Associate table** to add tables with an analysis rule that can be run for the specified model. 

   1. Choose **Worker type** to use when creating this data channel. The default worker type is **CR.1X**. Specify the **Number of workers** to use. The default worker number is **16**. To specify **Spark properties**:

      1. Expand **Spark properties**.

      1. Choose **Add Spark properties**.

      1. On the **Spark properties** dialog box, choose a **Property name** from the dropdown list and enter a **Value**.

      The following tables provide a definition for each property.

      For more information about Spark properties, see [Spark Properties](https://spark.apache.org/docs/latest/configuration.html#spark-properties) in the Apache Spark documentation. 
**Note**  
You can configure a maximum of 50 Spark properties. Each property value can be up to 500 characters.    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/clean-rooms/latest/userguide/create-ml-input-channel.html)    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/clean-rooms/latest/userguide/create-ml-input-channel.html)

   1. For **Data retention in days**, enter the number of days to keep the data.

   1. For **Result format,** choose either **CSV** or **Parquet** as the data format the ML input channel should use.

1. For **Service access**, choose the **Existing service role name** that will be used to access this table or choose **Create and use a new service role**. 

1. For **Encryption**, choose the **Encrypt secret with a custom KMS key** to specify your own KMS key and related information. Otherwise, Clean Rooms ML will manage the encryption.

1. (Optional) For **Compute payer**, select the collaboration member who pays for query compute costs.
**Note**  
If there is only one payer candidate for query compute in the collaboration, it defaults to that payer.

1. (Optional) For **Synthetic data generation payer**, select the collaboration member who pays for synthetic data generation costs.
**Note**  
This option appears when the ML input channel uses an analysis template configured for synthetic data output. If there is only one payer candidate for synthetic data generation in the collaboration, it defaults to that payer.

1. Choose **Create ML input channel**. 

   It will take a few minutes to create the ML input channel. You can see a list of ML input channels on the **ML models** tab.

**Note**  
After the ML input channel is created, you can't edit it.

------
#### [ API ]

To create an ML input channel (API)

Run the following code with your specific parameters: 

```
import boto3 
acr_client = boto3.client('cleanroomsml')

acr_client.create_ml_input_channel(
    name="{{ml_input_channel_name}}",
    membershipIdentifier='{{membership_id}}',
    configuredModelAlgorithmAssociations=[{{configured_model_algorithm_association_arn}}],
    retentionInDays={{1}},
    inputChannel={
        "dataSource": {
            "protectedQueryInputParameters": {
                "sqlParameters": {
                    "queryString": "select * from {{table}}",
                    "computeConfiguration": {
                        "worker": {
                            "type": "{{CR.1X}}",
                            "number": {{16}},
                            "properties": {
                                "spark": {
                                    "{{spark configuration key}}": "{{spark configuration value}}",
                                }
                            }   
                        }
                    },
                    "resultFormat": "{{PARQUET}}"
                }
            }
        },
        "roleArn": "arn:aws:iam::{{111122223333}}:role/{{role_name}}"
    }
)
channel_arn = resp['{{ML Input Channel ARN}}']
```

------