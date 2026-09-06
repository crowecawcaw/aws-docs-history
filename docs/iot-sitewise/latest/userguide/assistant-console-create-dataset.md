

# Create a dataset
<a name="assistant-console-create-dataset"></a>

**Note**  
The SiteWise Monitor feature is no longer available to new customers. Existing customers can continue to use the service as normal. For more information, see [SiteWise Monitor availability change](https://docs.aws.amazon.com/iot-sitewise/latest/appguide/iotsitewise-monitor-availability-change.html).

**Note**  
 The AWS IoT SiteWise Assistant must use a dataset with an [Amazon Kendra](https://docs.aws.amazon.com/kendra/latest/dg/what-is-kendra.html) index for enterprise level knowledge and guidance. If you do not have a Amazon Kendra index, see [Creating an index](https://docs.aws.amazon.com/kendra/latest/dg/create-index.html) to create one. Adding a [dataset](concept-overview.md#concept-dataset) improves the quality of the Assistant's response, and minimizes hallucinations. 

------
#### [ Console ]

**Create a dataset in the AWS IoT SiteWise console**

1.  Datasets are displayed in the **Datasets** section of the **AWS IoT SiteWise Assistant** page. 

1.  If no datasets exist, choose **Create dataset**. 

1.  In the **Dataset details** page, choose a Kendra index from the drop down menu to associate with the dataset. 

1.  The dataset name is populated by the Kendra index selected in Step 3. Edit the name if needed. 

1.  (Optional) The dataset description is populated by the Kendra index selected in Step 3. Edit the description if needed. 

1.  In the **Permissions** section, choose from below: 

   1.  Choose **Create and use a new service role**. By default, AWS IoT SiteWise automatically creates a service role. This role allows the AWS IoT SiteWise Assistant to access your Kendra indexes. 

   1.  Choose **Use an existing service role**, and then choose the target role. 

1. Choose **Create**.

![Creating a dataset final picture in the Assistant page of the console](http://docs.aws.amazon.com/iot-sitewise/latest/userguide/images/ai-assistant-create-dataset.png)


The service role created by AWS IoT SiteWise for the user, if the user chose to **Create and use a new service role**.

![Creating a dataset final picture in the Assistant page of the console](http://docs.aws.amazon.com/iot-sitewise/latest/userguide/images/ai-create-dataset-permissions.png)


------
#### [ AWS CLI ]

**Create a dataset in AWS CLI**

1.  Create an IAM role used to create a dataset. Use the following permissions policy: 

------
#### [ JSON ]

****  

   ```
   {
       "Version":"2012-10-17",		 	 	 
       "Statement": [
           {
               "Effect": "Allow",
               "Action": [
                   "kendra:Retrieve"
               ],
               "Resource": "arn:aws:kendra:*:*:index/*"
           }
       ]
   }
   ```

------

    Use the following trust relationship: 

------
#### [ JSON ]

****  

   ```
   {
       "Version":"2012-10-17",		 	 	 
       "Statement": [
           {
               "Effect": "Allow",
               "Principal": {
                   "Service": "iotsitewise.amazonaws.com"
               },
               "Action": "sts:AssumeRole"
           }
       ]
   }
   ```

------

1.  Create a file **create-dataset.json** with the template provided in the example. Populate `datasetId`, `kendra knowledgeBaseArn` and `roleArn` to connect with this dataset. 

   ```
   {
       "datasetId": "<UUID>",
       "datasetName": "DatasetForAssistant",
       "datasetSource": {
          "sourceType": "KENDRA",
          "sourceFormat": "KNOWLEDGE_BASE",
          "sourceDetail": {
             "kendra": {
               "knowledgeBaseArn": "arn:aws:kendra::%s:index/index",
               "roleArn": "arn:aws:iam::%s:role/role"
             }
          }
       }
   }
   ```

1.  Create the dataset with the following command: 

   ```
   aws iotsitewise create-dataset --cli-input-json {{file://create-dataset.json}} —-region us-east-1
   ```

------