# Tutorial: Build your first streaming workload using AWS Glue Studio notebooks

In this tutorial, you will explore how to leverage AWS Glue Studio notebooks to interactively build and refine your ETL jobs for near real-time data processing. Whether you're new to AWS Glue or looking to enhance your skill set, this guide will walk you through the process, empowering you to harness the full potential of AWS Glue interactive session notebooks.

With AWS Glue Streaming, you can create streaming extract, transform, and load (ETL) jobs that run continuously and consume data from streaming sources such as Amazon Kinesis Data Streams, Apache Kafka, and Amazon Managed Streaming for Apache Kafka (Amazon MSK).

## Prerequisites

To follow this tutorial you'll need a user with AWS console permissions to use AWS Glue, Amazon Kinesis, Amazon S3, Amazon Athena, AWS CloudFormation, AWS Lambda and Amazon Cognito.

## Consume streaming data from Amazon Kinesis

###### Topics

- [Generating mock data with Kinesis Data Generator](#streaming-tutorial-studio-notebooks-kinesis-generate-data "#streaming-tutorial-studio-notebooks-kinesis-generate-data")
- [Creating an AWS Glue streaming job with AWS Glue Studio](#streaming-tutorial-studio-notebooks-kinesis-create-job "#streaming-tutorial-studio-notebooks-kinesis-create-job")
- [Clean up](#streaming-tutorial-studio-notebooks-clean "#streaming-tutorial-studio-notebooks-clean")
- [Conclusion](#streaming-tutorial-studio-notebooks-conclusion "#streaming-tutorial-studio-notebooks-conclusion")

### Generating mock data with Kinesis Data Generator

###### Note

If you have already completed our previous [Tutorial: Build your first streaming workload using AWS Glue Studio](streaming-tutorial-studio.md "streaming-tutorial-studio.md"), you already have the Kinesis Data Generator installed on your account and you can skip steps 1-8 below and move on to the section [Creating an AWS Glue streaming job with AWS Glue Studio](#streaming-tutorial-studio-notebooks-kinesis-create-job "#streaming-tutorial-studio-notebooks-kinesis-create-job").

You can synthetically generate sample data in JSON format using the Kinesis Data Generator (KDG). You can find full instructions and details in the [tool documentation](https://awslabs.github.io/amazon-kinesis-data-generator/web/help.html "https://awslabs.github.io/amazon-kinesis-data-generator/web/help.html").

1. To get started, click [![Orange button labeled "Launch Stack" with an arrow icon.](images/cloudformation-launch-stack-button.png)](https://aws-data-analytics-workshops.s3.amazonaws.com/aws_glue/aws_glue_streaming/docs/glue-stream.yaml "https://aws-data-analytics-workshops.s3.amazonaws.com/aws_glue/aws_glue_streaming/docs/glue-stream.yaml") to run an AWS CloudFormation template on your AWS environment.

###### Note

You may encounter a CloudFormation template failure because some resources, such as the Amazon Cognito user for Kinesis Data Generator already exist in your AWS account. This could be because you already set that up from another tutorial or blog. To address this, you can either try the template in a new AWS account for a fresh start, or explore a different AWS Region. These options let you run the tutorial without conflicting with existing resources.

The template provisions a Kinesis data stream and a Kinesis Data Generator account for you. 2. Enter a **Username** and **Password** that the KDG will use to authenticate. Note the username and password for further usage. 3. Select **Next** all the way to the last step. Acknowledge the creation of IAM resources. Check for any errors at the top of the screen, such as the password not meeting the minimum requirements, and deploy the template. 4. Navigate to the **Outputs** tab of the stack. Once the template is deployed, it will display the generated property **KinesisDataGeneratorUrl**. Click that URL. 5. Enter the **Username** and **Password** you noted down. 6. Select the Region you are using and select the Kinesis Stream `GlueStreamTest-{AWS::AccountId}` 7. Enter the following template:

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

You can now view mock data with **Test template** and ingest the mock data to Kinesis with **Send data**. 8. Click **Send data** and generate 5-10K records to Kinesis.

### Creating an AWS Glue streaming job with AWS Glue Studio

AWS Glue Studio is a visual interface that simplifies the process of designing, orchestrating, and monitoring data integration pipelines. It enables users to build data transformation pipelines without writing extensive code. Apart from the visual job authoring experience, AWS Glue Studio also includes a Jupyter notebook backed by AWS Glue Interactive sessions, which you will be using in the remainder of this tutorial.

#### Set up the AWS Glue Streaming interactive sessions job

1. Download the provided [notebook file](https://aws-data-analytics-workshops.s3.amazonaws.com/aws_glue/aws_glue_streaming/docs/glue_streaming_tutorial_notebook.ipynb "https://aws-data-analytics-workshops.s3.amazonaws.com/aws_glue/aws_glue_streaming/docs/glue_streaming_tutorial_notebook.ipynb") and save it to a local directory
2. Open the AWS Glue Console and on the left pane click **Notebooks** > **Jupyter Notebook** > **Upload and edit an existing notebook**. Upload the notebook from the previous step and click **Create**.

![The screenshot shows creating a Jupyter Notebook job.](images/streaming-tutorial-2a.png) 3. Provide the job a name, role and select the default Spark kernel. Next click **Start notebook**. For the **IAM Role**, select the role provisioned by the CloudFormation template. You can see this in the **Outputs** tab of CloudFormation.

![The screenshot shows the Notebook setup dialog.](images/streaming-tutorial-2b.png)

The notebook has all necessary instructions to continue the tutorial. You can either run the instructions on the notebook or follow along with this tutorial to continue with the job development.

#### Run the notebook cells

1. (Optional) The first code cell, `%help` lists all available notebook magics. You can skip this cell for now, but feel free to explore it.
2. Start with the next code block `%streaming`. This magic sets the job type to streaming which lets you develop, debug and deploy an AWS Glue streaming ETL job.
3. Run the next cell to create an AWS Glue interactive session. The output cell has a message that confirms the session creation.

![The screenshot shows starting an interactive session.](images/streaming-tutorial-2c.png) 4. The next cell defines the variables. Replace the values with ones appropriate to your job and run the cell. For example:

![The screenshot shows defining variables in an interactive session.](images/streaming-tutorial-2d.png) 5. Since the data is being streamed already to Kinesis Data Streams, your next cell will consume the results from the stream. Run the next cell. Since there are no print statements, there is no expected output from this cell. 6. In the following cell, you explore the incoming stream by taking a sample set and print its schema and the actual data. For example:

![The screenshot shows sampling and printing the incoming records in an interactive session.](images/streaming-tutorial-2e.png) 7. Next, define the actual data transformation logic. The cell consists of the `processBatch` method that is triggered during every micro-batch. Run the cell. At a high level, we do the following to the incoming stream:

    1. Select a subset of the input columns.
    2. Rename a column (o2stats to oxygen\_stats).
    3. Derive new columns (serial\_identifier, ingest\_year, ingest\_month and ingest\_day).
    4. Store the results into an Amazon S3 bucket and also create a partitioned AWS Glue catalog table

8. In the last cell, you trigger the process batch every 10 seconds. Run the cell and wait for about 30 seconds for it to populate the Amazon S3 bucket and the AWS Glue catalog table.
9. Finally, browse the stored data using the Amazon Athena query editor. You can see the renamed column and also the new partitions.

![The screenshot shows browsing the stored data in the Amazon Athena query editor.](images/streaming-tutorial-2f.png)

The notebook has all necessary instructions to continue the tutorial. You can either run the instructions on the notebook or follow along with this tutorial to continue with the job development.

#### Save and run the AWS Glue job

With the development and testing of your application complete using the interactive sessions notebook, click **Save** at the top of the notebook interface. Once saved you can also run the application as a job.

![The screenshot shows saving the notebook as an AWS Glue job.](images/streaming-tutorial-2g.png)

### Clean up

To avoid incurring additional charges to your account, stop the streaming job that you started as part of the instructions. You can do this by stopping the notebook, which will end the session. Empty the Amazon S3 bucket and delete the AWS CloudFormation stack that you provisioned earlier.

### Conclusion

In this tutorial, we demonstrated how to do the following using the AWS Glue Studio notebook

- Author a streaming ETL job using notebooks
- Preview incoming data streams
- Code and fix issues without having to publish AWS Glue jobs
- Review the end-to-end working code, remove any debugging, and print statements or cells from the notebook
- Publish the code as an AWS Glue job

The goal of this tutorial is to give you hands-on experience working with AWS Glue Streaming and interactive sessions. We encourage you to use this as a reference for your individual AWS Glue Streaming use cases. For more information, see [Getting started with AWS Glue interactive sessions](interactive-sessions.md "interactive-sessions.md").
