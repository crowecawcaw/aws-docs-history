Amazon Managed Service for Apache Flink (Amazon MSF) was previously known as Amazon Kinesis Data Analytics for Apache Flink.

# Clean up AWS resources

This section includes procedures for cleaning up AWS resources created in the Tumbling Window tutorial.

###### This topic contains the following sections:

- [Delete your Managed Service for Apache Flink application](#examples-gs-scala-cleanup-app "#examples-gs-scala-cleanup-app")
- [Delete your Kinesis data streams](#examples-gs-scala-cleanup-stream "#examples-gs-scala-cleanup-stream")
- [Delete your Amazon S3 object and bucket](#examples-gs-scala-cleanup-s3 "#examples-gs-scala-cleanup-s3")
- [Delete your IAM resources](#examples-gs-scala-cleanup-iam "#examples-gs-scala-cleanup-iam")
- [Delete your CloudWatch resources](#examples-gs-scala-cleanup-cw "#examples-gs-scala-cleanup-cw")

## Delete your Managed Service for Apache Flink application

1. Sign in to the AWS Management Console, and open the Amazon MSF console at https://console.aws.amazon.com/flink.
2. in the Managed Service for Apache Flink panel, choose **MyApplication**.
3. In the application's page, choose **Delete** and then confirm the deletion.

## Delete your Kinesis data streams

1. Open the Kinesis console at
   [https://console.aws.amazon.com/kinesis](https://console.aws.amazon.com/kinesis "https://console.aws.amazon.com/kinesis").
2. In the Kinesis Data Streams panel, choose **ExampleInputStream**.
3. In the **ExampleInputStream** page, choose **Delete Kinesis Stream** and then confirm the deletion.
4. In the **Kinesis streams** page, choose the **ExampleOutputStream**, choose **Actions**, choose **Delete**, and then
   confirm the deletion.

## Delete your Amazon S3 object and bucket

1. Open the Amazon S3 console at
   [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
2. Choose the **ka-app-code-`<username>` bucket.**
3. Choose **Delete** and then enter the bucket name to confirm deletion.

## Delete your IAM resources

1. Open the IAM console at
   [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. In the navigation bar, choose **Policies**.
3. In the filter control, enter **kinesis**.
4. Choose the **kinesis-analytics-service-MyApplication-us-west-2** policy.
5. Choose **Policy Actions** and then choose **Delete**.
6. In the navigation bar, choose **Roles**.
7. Choose the **kinesis-analytics-MyApplication-us-west-2** role.
8. Choose **Delete role** and then confirm the deletion.

## Delete your CloudWatch resources

1. Open the CloudWatch console at
   [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
2. In the navigation bar, choose **Logs**.
3. Choose the **/aws/kinesis-analytics/MyApplication** log group.
4. Choose **Delete Log Group** and then confirm the deletion.
