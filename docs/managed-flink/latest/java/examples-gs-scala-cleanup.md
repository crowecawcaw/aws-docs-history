

# Clean up AWS resources
<a name="examples-gs-scala-cleanup"></a>

This section includes procedures for cleaning up AWS resources created in the Tumbling Window tutorial.

**Topics**
+ [Delete your Managed Service for Apache Flink application](#examples-gs-scala-cleanup-app)
+ [Delete your Kinesis data streams](#examples-gs-scala-cleanup-stream)
+ [Delete your Amazon S3 object and bucket](#examples-gs-scala-cleanup-s3)
+ [Delete your IAM resources](#examples-gs-scala-cleanup-iam)
+ [Delete your CloudWatch resources](#examples-gs-scala-cleanup-cw)

## Delete your Managed Service for Apache Flink application
<a name="examples-gs-scala-cleanup-app"></a>

1. Sign in to the AWS Management Console, and open the Amazon MSF console at https://console.aws.amazon.com/flink.

1. in the Managed Service for Apache Flink panel, choose **MyApplication**.

1. In the application's page, choose **Delete** and then confirm the deletion.

## Delete your Kinesis data streams
<a name="examples-gs-scala-cleanup-stream"></a>

1. Open the Kinesis console at [https://console.aws.amazon.com/kinesis](https://console.aws.amazon.com/kinesis).

1. In the Kinesis Data Streams panel, choose **ExampleInputStream**.

1. In the **ExampleInputStream** page, choose **Delete Kinesis Stream** and then confirm the deletion.

1. In the **Kinesis streams** page, choose the **ExampleOutputStream**, choose **Actions**, choose **Delete**, and then confirm the deletion.

## Delete your Amazon S3 object and bucket
<a name="examples-gs-scala-cleanup-s3"></a>

1. Open the Amazon S3 console at [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/).

1. Choose the **ka-app-code-{{<username>}} bucket.**

1. Choose **Delete** and then enter the bucket name to confirm deletion.

## Delete your IAM resources
<a name="examples-gs-scala-cleanup-iam"></a>

1. Open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/).

1. In the navigation bar, choose **Policies**.

1. In the filter control, enter **kinesis**.

1. Choose the **kinesis-analytics-service-MyApplication-us-west-2** policy.

1. Choose **Policy Actions** and then choose **Delete**.

1. In the navigation bar, choose **Roles**.

1. Choose the **kinesis-analytics-MyApplication-us-west-2** role.

1. Choose **Delete role** and then confirm the deletion.

## Delete your CloudWatch resources
<a name="examples-gs-scala-cleanup-cw"></a>

1. Open the CloudWatch console at [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/).

1. In the navigation bar, choose **Logs**.

1. Choose the **/aws/kinesis-analytics/MyApplication** log group.

1. Choose **Delete Log Group** and then confirm the deletion.