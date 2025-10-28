Amazon Managed Service for Apache Flink (Amazon MSF) was previously known as Amazon Kinesis Data Analytics for Apache Flink.

# Tutorial: Deploy a Studio notebook as a Managed Service for Apache Flink

application with durable state

The following tutorial demonstrates how to deploy a Studio notebook as a Managed Service for Apache Flink application
with durable state.

###### This tutorial contains the following sections:

- [Complete prerequisites](#example-notebook-durable-setup "#example-notebook-durable-setup")
- [Deploy an application with durable state using the
  AWS Management Console](#example-notebook-deploy-console "#example-notebook-deploy-console")
- [Deploy an application with durable state using the
  AWS CLI](#example-notebook-deploy-cli "#example-notebook-deploy-cli")

## Complete prerequisites

Create a new Studio notebook by following the [Tutorial: Create a Studio notebook in
Managed Service for Apache Flink](example-notebook.md "example-notebook.md"), using either Kinesis Data Streams or Amazon MSK. Name the
Studio notebook `ExampleTestDeploy`.

## Deploy an application with durable state using the

AWS Management Console

1. Add an S3 bucket location where you want the packaged code to be stored under
   **Application code location -
   _optional_** in the console. This enables the
   steps to deploy and run your application directly from the notebook.
2. Add required permissions to the application role to enable the role you are using to read and write to an Amazon S3 bucket,
   and to launch a Managed Service for Apache Flink application:
   - AmazonS3FullAccess
   - Amazonmanaged-flinkFullAccess
   - Access to your sources, destinations, and VPCs as applicable. For more information, see [Review IAM permissions for Studio notebooks](how-zeppelin-iam.md "how-zeppelin-iam.md").

3. Use the following sample code:

```
%flink.ssql(type=update)
CREATE TABLE exampleoutput (
  'ticket' VARCHAR,
  'price' DOUBLE
)
WITH (
  'connector' = 'kinesis',
  'stream' = 'ExampleOutputStream',
  'aws.region' = 'us-east-1',
  'scan.stream.initpos' = 'LATEST',
  'format' = 'json'
);

`INSERT INTO exampleoutput SELECT ticker, price FROM exampleinputstream`
```

4. With this feature launch, you will see a new dropdown on the right top corner of each note in
   your notebook with the name of the notebook. You can do the following:
   - View the Studio notebook settings in the AWS Management Console.
   - Build your Zeppelin Note and export it to Amazon S3. At this point, provide a name for your application and choose **Build and Export**.
     You will get a notification when the export completes.
   - If you need to, you can view and run any additional tests on the executable in Amazon S3.
   - Once the build is complete, you will be able to deploy your code as a Kinesis streaming application with durable state and autoscaling.
   - Use the dropdown and choose **Deploy Zeppelin Note as Kinesis streaming application**.
     Review the application name and choose **Deploy via AWS Console**.
   - This will lead you to the AWS Management Console page for creating a Managed Service for Apache Flink application. Note that application name, parallelism, code location,
     default Glue DB, VPC (if applicable) and IAM roles have been pre-populated. Validate that the IAM roles have the required permissions
     to your sources and destinations. Snapshots are enabled by default for durable application state management.
   - Choose **create application**.
   - You can choose **configure** and modify any settings, and choose **Run** to
     start your streaming application.

## Deploy an application with durable state using the

AWS CLI

To deploy an application using the AWS CLI, you must update your AWS CLI to use the service model provided with your Beta 2 information.
For information about how to use the updated service model, see [Complete the prerequisites](example-notebook.md#example-notebook-setup "example-notebook.md#example-notebook-setup").

The following example code creates a new Studio notebook:

```
aws kinesisanalyticsv2 create-application \
     --application-name <app-name> \
     --runtime-environment ZEPPELIN-FLINK-3_0 \
     --application-mode INTERACTIVE \
     --service-execution-role <iam-role>
     --application-configuration '{
       "ZeppelinApplicationConfiguration": {
         "CatalogConfiguration": {
           "GlueDataCatalogConfiguration": {
             "DatabaseARN": "arn:aws:glue:us-east-1:<account>:database/<glue-database-name>"
           }
         }
       },
       "FlinkApplicationConfiguration": {
         "ParallelismConfiguration": {
           "ConfigurationType": "CUSTOM",
           "Parallelism": 4,
           "ParallelismPerKPU": 4
         }
       },
       "DeployAsApplicationConfiguration": {
            "S3ContentLocation": {
               "BucketARN": "arn:aws:s3:::<s3bucket>",
               "BasePath": "/something/"
            }
        },
       "VpcConfigurations": [
         {
           "SecurityGroupIds": [
             "<security-group>"
           ],
           "SubnetIds": [
             "<subnet-1>",
             "<subnet-2>"
           ]
         }
       ]
     }' \
     --region us-east-1
```

The following code example starts a Studio notebook:

```
aws kinesisanalyticsv2 start-application \
    --application-name <app-name> \
    --region us-east-1 \
    --no-verify-ssl
```

The following code returns the URL for an application's Apache Zeppelin notebook page:

```
aws kinesisanalyticsv2 create-application-presigned-url \
    --application-name <app-name> \
    --url-type ZEPPELIN_UI_URL \

    --region us-east-1 \
    --no-verify-ssl
```
