

# Integrating CloudWatch metrics with Amazon Managed Service for Prometheus
<a name="integrating-cw-firehose"></a>

It can help to have all your metrics in one place. Amazon Managed Service for Prometheus does not automatically ingest Amazon CloudWatch metrics. However, you can use Amazon Data Firehose and AWS Lambda to push CloudWatch metrics to Amazon Managed Service for Prometheus.

This section describes how to instrument a [Amazon CloudWatch metric stream](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Metric-Streams.html) and use [Amazon Data Firehose](https://docs.aws.amazon.com/firehose/latest/dev/what-is-this-service.html) and [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html) to ingest metrics into Amazon Managed Service for Prometheus.

You will set up a stack using [AWS Cloud Development Kit (CDK)](https://aws.amazon.com/cdk/) to create a Firehose Delivery Stream, a Lambda, and an Amazon S3 bucket to demonstrate a complete scenario.

## Infrastructure
<a name="integ-cw-fh-infrastructure"></a>

The first thing you must do is set up the infrastructure for this recipe. 

CloudWatch metric streams allow forwarding of the streaming metric data to an HTTP endpoint or [Amazon S3 bucket](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html).

Setting up the infrastructure will consist of 4 steps:
+ Configuring prerequisites
+ Creating an Amazon Managed Service for Prometheus workspace
+ Installing dependencies
+ Deploying the stack

**Prerequisites**
+ The AWS CLI is [installed](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-install.html) and [configured](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-configure.html) in your environment.
+ The [AWS CDK Typescript](https://docs.aws.amazon.com/cdk/latest/guide/work-with-cdk-typescript.html) is installed in your environment.
+ Node.js and Go are installed in your environment.
+ The [AWS observability CloudWatch metrics exporter github repository](https://github.com/aws-observability/observability-best-practices/tree/main/sandbox/CWMetricStreamExporter) (`CWMetricsStreamExporter`) has been cloned to your local machine.

**To create a Amazon Managed Service for Prometheus workspace**

1. The demo application in this recipe will be running on top of Amazon Managed Service for Prometheus. Create your Amazon Managed Service for Prometheus Workspace via the following command:

   ```
   aws amp create-workspace --alias prometheus-demo-recipe
   ```

1. Ensure your workspace has been created with the following command:

   ```
   aws amp list-workspaces
   ```

   For more information about Amazon Managed Service for Prometheus, see [Amazon Managed Service for Prometheus ](https://docs.aws.amazon.com/prometheus/latest/userguide/AMP-getting-started.html) User Guide.

**To install dependencies**

1. **Install dependencies**

   From the root of the `aws-o11y-recipes` repository, change your directory to `CWMetricStreamExporter` using the command:

   ```
   cd sandbox/CWMetricStreamExporter
   ```

   This will now be considered the root of the repo, going forward.

1. Change directory to `/cdk` via the following command:

   ```
   cd cdk
   ```

1. Install the CDK dependencies via the following command:

   ```
   npm install
   ```

1. Change directory back to the root of the repo, and then change directory to `/lambda` using the following command:

   ```
   cd lambda
   ```

1. Once in the `/lambda` folder, install the Go dependencies using:

   ```
   go get
   ```

   All the dependencies are now installed.

**To deploy the stack**

1. In the root of the repo, open `config.yaml` and modify the Amazon Managed Service for Prometheus workspace URL by replacing the `{workspace}` with the newly created workspace id, and the region your Amazon Managed Service for Prometheus workspace is in.

   For example, modify the following with:

   ```
   AMP: 
       remote_write_url: "https://aps-workspaces.us-east-2.amazonaws.com/workspaces/{workspaceId}/api/v1/remote_write" 
       region: us-east-2
   ```

   Change the names of the Firehose delivery stream and Amazon S3 bucket to your liking.

1. To build the AWS CDK and the Lambda code, in the root of the repo run the following commend:

   ```
   npm run build
   ```

   This build step ensures that the Go Lambda binary is built, and deploys the CDK to CloudFormation.

1. To complete the deployment, review and accept the IAM changes that the stack requires.

1. (Optional) You can very if that the stack has been created by running the following command.

   ```
   aws cloudformation list-stacks
   ```

   A stack named `CDK Stack` will be in the list.

## Creating a Amazon CloudWatch stream
<a name="integ-cw-fh-stream"></a>

Now that you have a lambda function to handle the metrics, you can create the metrics stream from Amazon CloudWatch.

**To create an CloudWatch metrics stream**

1. Navigate to the CloudWatch console, at [https://console.aws.amazon.com/cloudwatch/home\#metric-streams:streamsList](https://console.aws.amazon.com/cloudwatch/home#metric-streams:streamsList) and select **Create metric stream**.

1. Select the metrics needed, either all metrics, or only from selected namespaces.

1. Under `Configuration`, choose **Select an existing Firehose owned by your account**.

1. You will be using the Firehose created earlier by the CDK. In the **Select your Kinesis data Firehose stream** drop down, select the stream created earlier. It will have a name like `CdkStack-KinesisFirehoseStream123456AB-sample1234`.

1. Change the output format to **JSON**.

1. Give the metric stream a name that is meaningful to you.

1. Choose **Create metric stream**.

1. (Optional) To verify the Lambda function invocation, navigate to the [Lambda console](https://console.aws.amazon.com/lambda/home) and choose the function `KinesisMessageHandler`. Select the **Monitor** tab and **Logs** subtab, and under **Recent Invocations** there should be entries of the Lambda function being triggered.
**Note**  
It may take up to 5 minutes before invocations begin to show in the **Monitor** tab.

Your metrics are now being streamed from Amazon CloudWatch to Amazon Managed Service for Prometheus.

## Cleanup
<a name="integ-cw-fh-cleanup"></a>

You may want to clean up the resources that were used in this example. The following procedure explains how to do so. This will stop the metrics stream that you created.

**To clean up resources**

1. Start by deleting the CloudFormation stack with the following commands:

   ```
   cd cdk
   cdk destroy
   ```

1. Remove the Amazon Managed Service for Prometheus workspace:

   ```
   aws amp delete-workspace --workspace-id \
       `aws amp list-workspaces --alias prometheus-sample-app --query 'workspaces[0].workspaceId' --output text`
   ```

1. Finally, remove the Amazon CloudWatch metric stream using the [Amazon CloudWatch console](https://console.aws.amazon.com/cloudwatch/home#metric-streams:streamsList).