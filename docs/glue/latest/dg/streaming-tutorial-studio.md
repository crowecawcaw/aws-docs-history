

# Tutorial: Build your first streaming workload using AWS Glue Studio
<a name="streaming-tutorial-studio"></a>

In this tutorial, you are going to learn how to create a streaming job using AWS Glue Studio. AWS Glue Studio is a visual interface to create AWS Glue jobs.

You can create streaming extract, transform, and load (ETL) jobs that run continuously and consume data from streaming sources in Amazon Kinesis Data Streams, Apache Kafka, and Amazon Managed Streaming for Apache Kafka (Amazon MSK).

## Prerequisites
<a name="streaming-tutorial-studio-prereqs"></a>

To follow this tutorial you'll need a user with AWS console permissions to use AWS Glue, Amazon Kinesis, Amazon S3, Amazon Athena, AWS CloudFormation, AWS Lambda and Amazon Cognito.

## Consume streaming data from Amazon Kinesis
<a name="streaming-tutorial-studio-kinesis"></a>

**Topics**
+ [Generating mock data with Kinesis Data Generator](#streaming-tutorial-studio-kinesis-generate-data)
+ [Creating an AWS Glue streaming job with AWS Glue Studio](#streaming-tutorial-studio-kinesis-create-job)
+ [Performing a transformation and storing the transformed result in Amazon S3](#streaming-tutorial-studio-kinesis-transformation)

### Generating mock data with Kinesis Data Generator
<a name="streaming-tutorial-studio-kinesis-generate-data"></a>

You can synthetically generate sample data in JSON format using the Kinesis Data Generator (KDG). You can find full instructions and details in the [tool documentation](https://awslabs.github.io/amazon-kinesis-data-generator/web/help.html).

1. To get started, click [![Orange button labeled "Launch Stack" with an arrow icon.](http://docs.aws.amazon.com/glue/latest/dg/images/cloudformation-launch-stack-button.png)](https://console.aws.amazon.com/cloudformation/home?region=us-east-2#/stacks/new?templateURL=https%3A%2F%2Faws-data-analytics-workshops.s3.amazonaws.com/aws_glue/aws_glue_streaming/docs/glue-stream.yaml&stackName=glue-stream) to run an AWS CloudFormation template on your AWS environment.
**Note**  
You may encounter a CloudFormation template failure because some resources, such as the Amazon Cognito user for Kinesis Data Generator already exist in your AWS account. This could be because you already set that up from another tutorial or blog. To address this, you can either try the template in a new AWS account for a fresh start, or explore a different AWS Region. These options let you run the tutorial without conflicting with existing resources.

   The template provisions a Kinesis data stream and a Kinesis Data Generator account for you. It also creates an Amazon S3 bucket to hold the data and a Glue Service Role with the required permission for this tutorial.

1. Enter a **Username** and **Password** that the KDG will use to authenticate. Note the username and password for further usage.

1. Select **Next** all the way to the last step. Acknowledge the creation of IAM resources. Check for any errors at the top of the screen, such as the password not meeting the minimum requirements, and deploy the template.

1. Navigate to the **Outputs** tab of the stack. Once the template is deployed, it will display the generated property **KinesisDataGeneratorUrl**. Click that URL.

1. Enter the **Username** and **Password** you noted down.

1. Select the Region you are using and select the Kinesis Stream `GlueStreamTest-{AWS::AccountId}`

1. Enter the following template:

   ```
   {
       "ventilatorid": {{random.number(100)}},
       "eventtime": "{{date.now("YYYY-MM-DD HH:mm:ss")}}",
       "serialnumber": "{{random.uuid}}",
       "pressurecontrol": {{random.number(
           {
               "min":5,
               "max":30
           }
       )}},
       "o2stats": {{random.number(
           {
               "min":92,
               "max":98
           }
       )}},
       "minutevolume": {{random.number(
           {
               "min":5,
               "max":8
           }
       )}},
       "manufacturer": "{{random.arrayElement(
           ["3M", "GE","Vyaire", "Getinge"]
       )}}"
   }
   ```

   You can now view mock data with **Test template** and ingest the mock data to Kinesis with **Send data**.

1. Click **Send data** and generate 5-10K records to Kinesis.

### Creating an AWS Glue streaming job with AWS Glue Studio
<a name="streaming-tutorial-studio-kinesis-create-job"></a>

1. Navigate to AWS Glue in the console on the same Region.

1. Select **ETL jobs** under the left side navigation bar under **Data Integration and ETL**.

1. Create an AWS Glue Job via **Visual with a blank canvas**.  
![The screenshot shows the create job dialog.](http://docs.aws.amazon.com/glue/latest/dg/images/streaming-tutorial-1a.png)

1. Navigate to the **Job Details** tab.

1. For the AWS Glue job name, enter `DemoStreamingJob`.

1. For **IAM Role**, select the role provisioned by the CloudFormation template, `glue-tutorial-role-${AWS::AccountId}`.

1. For **Glue version**, select **Glue 3.0**. Leave all other options as default.  
![The screenshot shows the job details tab.](http://docs.aws.amazon.com/glue/latest/dg/images/streaming-tutorial-1b.png)

1. Navigate to the **Visual tab**.

1. Click on the plus icon. Enter **Kinesis** in the search bar. Select the **Amazon Kinesis** data source.  
![The screenshot shows the Add nodes dialog.](http://docs.aws.amazon.com/glue/latest/dg/images/streaming-tutorial-1c.png)

1. Select **Stream details** for **Amazon Kinesis Source** under the tab **Data source properties - Kinesis Stream**.

1. Select **Stream is located in my account** for **Location of data stream**.

1. Select the Region you are using.

1. Select the `GlueStreamTest-{AWS::AccountId}` stream.

1. Keep all other settings as default.  
![The screenshot shows the Data source properties tab.](http://docs.aws.amazon.com/glue/latest/dg/images/streaming-tutorial-1d.png)

1. Navigate to the **Data preview** tab.

1. Click **Start data preview session**, which previews the mock data generated by KDG. Pick the Glue Service Role you previously created for the AWS Glue Streaming job.

   It takes 30-60 seconds for the preview data to show up. If it shows **No data to display**, click the gear icon and change the **Number of rows to sample** to `100`.

   You can see the sample data as below:  
![The screenshot shows the Data preview tab.](http://docs.aws.amazon.com/glue/latest/dg/images/streaming-tutorial-1e.png)

   You can also see the inferred schema in the **Output schema** tab.  
![The screenshot shows the Output schema tab.](http://docs.aws.amazon.com/glue/latest/dg/images/streaming-tutorial-1f.png)

### Performing a transformation and storing the transformed result in Amazon S3
<a name="streaming-tutorial-studio-kinesis-transformation"></a>

1. With the source node selected, click on the plus icon on the top left to add a **Transforms** step.

1. Select the **Change Schema** step.  
![The screenshot shows the Add nodes dialog.](http://docs.aws.amazon.com/glue/latest/dg/images/streaming-tutorial-1g.png)

1. You can rename fields and convert the data type of fields in this step. Rename the `o2stats` column to `OxygenSaturation` and convert all `long` data type to `int`.  
![The screenshot shows the Transform tab.](http://docs.aws.amazon.com/glue/latest/dg/images/streaming-tutorial-1h.png)

1. Click on the plus icon to add an **Amazon S3** target. Enter S3 in the search box and select the **Amazon S3 - Target** transform step.  
![The screenshot shows the Add nodes tab.](http://docs.aws.amazon.com/glue/latest/dg/images/streaming-tutorial-1i.png)

1. Select **Parquet** as the target file format.

1. Select **Snappy** as the compression type.

1. Enter an **S3 Target Location** created by the CloudFormation template, `streaming-tutorial-s3-target-{AWS::AccountId}`. 

1. Select to **Create a table in the Data Catalog and on subsequent runs, update the schema and add new partitions**.

1. Enter the target **Database** and **Table** name to store the schema of the Amazon S3 target table.  
![The screenshot shows the configuration page for the Amazon S3 target.](http://docs.aws.amazon.com/glue/latest/dg/images/streaming-tutorial-1j.png)

1. Click on the **Script** tab to view the generated code.

1. Click **Save** on the top right to save the ETL code and then click **Run** to kick-off the AWS Glue streaming job.

   You can find the **Run status** in the **Runs** tab. Let the job run for 3-5 minutes and then stop the job.  
![The screenshot shows the Runs tab.](http://docs.aws.amazon.com/glue/latest/dg/images/streaming-tutorial-1k.png)

1. Verify the new table created in Amazon Athena.  
![The screenshot shows the table in Amazon Athena.](http://docs.aws.amazon.com/glue/latest/dg/images/streaming-tutorial-1l.png)