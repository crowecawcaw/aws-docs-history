

# Clean up AWS resources
<a name="getting-started-cleanup"></a>

This section includes procedures for cleaning up AWS resources created in this Getting Started (DataStream API) tutorial.

**Topics**
+ [Delete your Managed Service for Apache Flink application](#getting-started-cleanup-app)
+ [Delete your Kinesis data streams](#getting-started-cleanup-stream)
+ [Delete your Amazon S3 objects and bucket](#getting-started-cleanup-s3)
+ [Delete your IAM resources](#getting-started-cleanup-iam)
+ [Delete your CloudWatch resources](#getting-started-cleanup-cw)
+ [Explore additional resources for Apache Flink](#getting-started-cleanup-next-step-5)

## Delete your Managed Service for Apache Flink application
<a name="getting-started-cleanup-app"></a>

Use the following procedure to delete the application.

1. Open the Kinesis console at [https://console.aws.amazon.com/kinesis](https://console.aws.amazon.com/kinesis).

1. In the Managed Service for Apache Flink panel, choose **MyApplication**.

1. From the **Actions** dropdown list, choose **Delete** and then confirm the deletion.

## Delete your Kinesis data streams
<a name="getting-started-cleanup-stream"></a>

1. Sign in to the AWS Management Console, and open the Amazon MSF console at https://console.aws.amazon.com/flink..

1. Choose **Data streams**.

1. Select the two streams that you created, `ExampleInputStream` and `ExampleOutputStream`. 

1. From the **Actions** dropdown list, choose **Delete**, and then confirm the deletion.

## Delete your Amazon S3 objects and bucket
<a name="getting-started-cleanup-s3"></a>

Use the following procedures to delete your Amazon S3 objects and bucket.

**To delete the object from the S3 bucket**

1. Open the Amazon S3 console at [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/).

1. Select the S3 bucket that you created for the application artifact.

1. Select the application artifact you uploaded, named `amazon-msf-java-stream-app-1.0.jar`.

1. Choose **Delete** and confirm the deletion.

**To delete the S3 bucket**

1. Open the Amazon S3 console at [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/).

1. Select the bucket that you created for the artifacts.

1. Choose **Delete** and confirm the deletion.
**Note**  
The S3 bucket must be empty to delete it.

## Delete your IAM resources
<a name="getting-started-cleanup-iam"></a>

**To delete your IAM resources**

1. Open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/).

1. In the navigation bar, choose **Policies**.

1. In the filter control, enter **kinesis**.

1. Choose the **kinesis-analytics-service-MyApplication-us-east-1** policy.

1. Choose **Policy Actions** and then choose **Delete**.

1. In the navigation bar, choose **Roles**.

1. Choose the **kinesis-analytics-MyApplication-us-east-1** role.

1. Choose **Delete role** and then confirm the deletion.

## Delete your CloudWatch resources
<a name="getting-started-cleanup-cw"></a>

1. Open the CloudWatch console at [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/).

1. In the navigation bar, choose **Logs**.

1. Choose the **/aws/kinesis-analytics/MyApplication** log group.

1. Choose **Delete Log Group** and then confirm the deletion.

## Explore additional resources for Apache Flink
<a name="getting-started-cleanup-next-step-5"></a>

[Explore additional resources](getting-started-next-steps.md)