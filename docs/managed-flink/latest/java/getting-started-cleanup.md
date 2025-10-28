Amazon Managed Service for Apache Flink (Amazon MSF) was previously known as Amazon Kinesis Data Analytics for Apache Flink.

# Clean up AWS resources

This section includes procedures for cleaning up AWS resources created in this
Getting Started (DataStream API) tutorial.

###### This topic contains the following sections:

- [Delete your Managed Service for Apache Flink
  application](#getting-started-cleanup-app "#getting-started-cleanup-app")
- [Delete your Kinesis data
  streams](#getting-started-cleanup-stream "#getting-started-cleanup-stream")
- [Delete your Amazon S3 objects and
  bucket](#getting-started-cleanup-s3 "#getting-started-cleanup-s3")
- [Delete your IAM resources](#getting-started-cleanup-iam "#getting-started-cleanup-iam")
- [Delete your CloudWatch resources](#getting-started-cleanup-cw "#getting-started-cleanup-cw")
- [Explore additional resources for Apache Flink](#getting-started-cleanup-next-step-5 "#getting-started-cleanup-next-step-5")

## Delete your Managed Service for Apache Flink

application

Use the following procedure to delete the application.

1. Open the Kinesis console at
   [https://console.aws.amazon.com/kinesis](https://console.aws.amazon.com/kinesis "https://console.aws.amazon.com/kinesis").
2. In the Managed Service for Apache Flink panel, choose **MyApplication**.
3. From the **Actions** dropdown list, choose
   **Delete** and then confirm the deletion.

## Delete your Kinesis data

streams

1. Sign in to the AWS Management Console, and open the Amazon MSF console at https://console.aws.amazon.com/flink..
2. Choose **Data streams**.
3. Select the two streams that you created, `ExampleInputStream`
   and `ExampleOutputStream`.
4. From the **Actions** dropdown list, choose
   **Delete**, and then confirm the deletion.

## Delete your Amazon S3 objects and

bucket

Use the following procedures to delete your Amazon S3 objects and bucket.

###### To delete the object from the S3 bucket

1. Open the Amazon S3 console at
   [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
2. Select the S3 bucket that you created for the application artifact.
3. Select the application artifact you uploaded, named
   `amazon-msf-java-stream-app-1.0.jar`.
4. Choose **Delete** and confirm the deletion.

###### To delete the S3 bucket

1. Open the Amazon S3 console at
   [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
2. Select the bucket that you created for the artifacts.
3. Choose **Delete** and confirm the deletion.

###### Note

The S3 bucket must be empty to delete it.

## Delete your IAM resources

###### To delete your IAM resources

1. Open the IAM console at
   [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. In the navigation bar, choose **Policies**.
3. In the filter control, enter **kinesis**.
4. Choose the
   **kinesis-analytics-service-MyApplication-us-east-1**
   policy.
5. Choose **Policy Actions** and then choose
   **Delete**.
6. In the navigation bar, choose **Roles**.
7. Choose the **kinesis-analytics-MyApplication-us-east-1**
   role.
8. Choose **Delete role** and then confirm the
   deletion.

## Delete your CloudWatch resources

1. Open the CloudWatch console at
   [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
2. In the navigation bar, choose **Logs**.
3. Choose the **/aws/kinesis-analytics/MyApplication** log
   group.
4. Choose **Delete Log Group** and then confirm the
   deletion.

## Explore additional resources for Apache Flink

[Explore additional resources](getting-started-next-steps.md "getting-started-next-steps.md")
