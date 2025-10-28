# Custom setup with Firehose

Use this method to create a metric stream and direct it to an
Amazon Data Firehose delivery stream that delivers your CloudWatch metrics to where you want them to go.
You can stream them to a data lake such as
Amazon S3, or to any destination or endpoint supported by Firehose including third-party providers.

JSON, OpenTelemetry 1.0.0, and OpenTelemetry 0.7.0 formats are supported natively,
or you can configure transformations in your Firehose delivery stream to convert the data to a different format such as
Parquet. With a metric stream,
you can continually
update monitoring data, or combine this
CloudWatch metric data with billing and performance data to create rich datasets. You can
then use tools such as Amazon Athena to get insight into cost optimization, resource
performance, and resource utilization.

You can use the CloudWatch console, the AWS CLI, AWS CloudFormation, or the AWS Cloud Development Kit (AWS CDK) to set up
a metric stream.

The Firehose delivery stream that you use for your metric stream must be in the same
account and the same Region where you set up the metric stream. To achieve
cross-Region functionality, you can configure the Firehose delivery stream to stream to a
final destination that is in a different account or a different Region.

## CloudWatch console

This section describes how to use the CloudWatch console to set up a
metric stream using Firehose.

###### To set up a custom metric stream using Firehose

1. Open the CloudWatch console at
   [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
2. In the navigation pane, choose **Metrics**,
   **Streams**. Then choose **Create metric stream**.
3. (Optional) If you are signed in to an account that is set up as a monitoring account
   in CloudWatch cross-account observability, you can choose whether to include metrics from linked source
   accounts in this metric stream. To include metrics from source accounts, choose
   **Include source account metrics**.
4. Choose **Custom setup with Firehose**.
5. For **Select your Kinesis Data Firehose stream**, select
   the
   Firehose delivery stream to use. It must be in the same account. The default format for this
   option is OpenTelemetry 0.7.0, but you can
   change the format later in this procedure.

Then select the Firehose delivery stream to use under
**Select your Firehose delivery stream**. 6. (Optional)You can choose **Select existing service
role** to use an existing IAM role instead of having CloudWatch
create a new one for you. 7. (Optional) To change the output format from the default format for your scenario, choose
**Change output format**. The supported formats are
JSON, OpenTelemetry 1.0.0, and OpenTelemetry 0.7.0. 8. For **Metrics to be streamed**, choose either
**All metrics** or **Select metrics**.

If you choose **All metrics**, all metrics from this account
will be included in the stream.

Consider carefully whether to stream all metrics, because the more metrics that you stream the
higher your metric stream charges will be.

If you choose **Select metrics**, do one of the following:

    * To stream most metric namespaces, choose **Exclude**
     and select the namespaces or metrics to
     exclude. When you specify a namespace in **Exclude**,
     you can optionally select some specific metrics from that namespace to exclude. If you choose
     to exclude a namespace but don't then select metrics in that namespace, all metrics from that namespace
     are excluded.
    * To include only a few metric namespaces or metrics in the metric stream,
     choose **Include** and
     then select the namespaces or metrics to include. If you choose
     to include a namespace but don't then select metrics in that namespace, all metrics from that namespace
     are included.

9. (Optional) To stream additional statistics for some of these metrics beyond Minimum, Maximum,
   SampleCount, and Sum, choose **Add additional statistics**. Either
   choose **Add recommended metrics** to add some commonly used statistics, or
   manually select the
   namespace and metric name to stream additional statistics for. Next, select
   the additional statistics to stream.

To then choose another group of metrics to stream a different set of additional statistics for, choose
**Add additional statistics**. Each metric can include as many
as 20 additional statistics, and as many as 100 metrics within a metric stream can include
additional statistics.

Streaming additional statistics incurs more charges. For more information,
see [Statistics that can be streamed](CloudWatch-metric-streams-statistics.md "CloudWatch-metric-streams-statistics.md").

For definitions of the additional statistics, see
[CloudWatch statistics definitions](Statistics-definitions.md "Statistics-definitions.md"). 10. (Optional) Customize the name of the new metric stream under
**Metric stream name**. 11. Choose **Create metric stream**.

## AWS CLI or AWS API

Use the following steps to create a CloudWatch metric stream.

###### To use the AWS CLI or AWS API to create a metric stream

1. If you're streaming to Amazon S3, first create the bucket. For more information, see [Creating a bucket](../../../AmazonS3/latest/userguide/create-bucket-overview.md "../../../AmazonS3/latest/userguide/create-bucket-overview.md").
2. Create the Firehose delivery stream. For more information, see
   [Creating a Firehose stream](../../../firehose/latest/dev/basic-create.md "../../../firehose/latest/dev/basic-create.md").
3. Create an IAM role that enables CloudWatch to write to the Firehose delivery stream.
   For more information about the contents of this role, see
   [Trust between CloudWatch and Firehose](CloudWatch-metric-streams-trustpolicy.md "CloudWatch-metric-streams-trustpolicy.md").
4. Use the `aws cloudwatch put-metric-stream` CLI command or the
   `PutMetricStream` API to create the CloudWatch metric stream.

## AWS CloudFormation

You can use AWS CloudFormation to set up a metric stream. For more information, see [AWS::CloudWatch::MetricStream](../../../AWSCloudFormation/latest/UserGuide/aws-resource-cloudwatch-metricstream.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-cloudwatch-metricstream.md").

###### To use AWS CloudFormation to create a metric stream

1. If you're streaming to Amazon S3, first create the bucket. For more information, see [Creating a bucket](../../../AmazonS3/latest/userguide/create-bucket-overview.md "../../../AmazonS3/latest/userguide/create-bucket-overview.md").
2. Create the Firehose delivery stream. For more information, see
   [Creating a Firehose stream](../../../firehose/latest/dev/basic-create.md "../../../firehose/latest/dev/basic-create.md").
3. Create an IAM role that enables CloudWatch to write to the Firehose delivery stream.
   For more information about the contents of this role, see
   [Trust between CloudWatch and Firehose](CloudWatch-metric-streams-trustpolicy.md "CloudWatch-metric-streams-trustpolicy.md").
4. Create the stream in AWS CloudFormation. For more information,
   see [AWS::CloudWatch::MetricStream](../../../AWSCloudFormation/latest/UserGuide/aws-resource-cloudwatch-metricstream.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-cloudwatch-metricstream.md").

## AWS Cloud Development Kit (AWS CDK)

You can use AWS Cloud Development Kit (AWS CDK) to set up a metric stream.

###### To use the AWS CDK to create a metric stream

1. If you're streaming to Amazon S3, first create the bucket. For more information, see [Creating a bucket](../../../AmazonS3/latest/userguide/create-bucket-overview.md "../../../AmazonS3/latest/userguide/create-bucket-overview.md").
2. Create the Firehose delivery stream. For more information, see
   [Creating an Amazon Data Firehose Delivery Stream](../../../firehose/latest/dev/basic-create.md "../../../firehose/latest/dev/basic-create.md").
3. Create an IAM role that enables CloudWatch to write to the Firehose delivery stream.
   For more information about the contents of this role, see
   [Trust between CloudWatch and Firehose](CloudWatch-metric-streams-trustpolicy.md "CloudWatch-metric-streams-trustpolicy.md").
4. Create the metric stream. The metric stream resource
   is available in AWS CDK as a Level 1 (L1) Construct named `CfnMetricStream`.
   For more information, see
   [Using L1 constructs](../../../cdk/latest/guide/constructs.md#constructs_l1_using.html "../../../cdk/latest/guide/constructs.md#constructs_l1_using.html").
