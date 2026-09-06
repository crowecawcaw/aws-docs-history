

# Clean up AWS resources
<a name="gs-table-cleanup"></a>

This section includes procedures for cleaning up AWS resources created in the Getting Started (Table API) tutorial.

**Topics**
+ [Delete your Managed Service for Apache Flink application](#gs-table-cleanup-app)
+ [Delete your Amazon S3 objects and bucket](#gs-table-cleanup-s3)
+ [Delete your IAM resources](#gs-table-cleanup-iam)
+ [Delete your CloudWatch resources](#gs-table-cleanup-cw)
+ [Next step](#gs-table-cleanup-next-step-5)

## Delete your Managed Service for Apache Flink application
<a name="gs-table-cleanup-app"></a>

Use the following procedure to delete the application.

**To delete the application**

1. Open the Kinesis console at [https://console.aws.amazon.com/kinesis](https://console.aws.amazon.com/kinesis).

1. In the Managed Service for Apache Flink panel, choose **MyApplication**.

1. From the **Actions** dropdown list, choose **Delete** and then confirm the deletion.

## Delete your Amazon S3 objects and bucket
<a name="gs-table-cleanup-s3"></a>

Use the following procedure to delete your S3 objects and bucket.

**To delete the application object from the S3 bucket**

1. Open the Amazon S3 console at [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/).

1. Select the S3 bucket that you created.

1. Select the application artifact that you uploaded named `amazon-msf-java-table-app-1.0.jar`, choose **Delete**, and then confirm the deletion.

**To delete all output files written by the application**

1. Choose the `output` folder.

1. Choose **Delete**.

1. Confirm that you want to permanently delete the content. 

**To delete the S3 bucket**

1. Open the Amazon S3 console at [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/).

1. Select the S3 bucket you created.

1. Choose **Delete** and confirm the deletion.

## Delete your IAM resources
<a name="gs-table-cleanup-iam"></a>

Use the following procedure to delete your IAM resources.

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
<a name="gs-table-cleanup-cw"></a>

Use the following procedure to delete your CloudWatch resources.

**To delete your CloudWatch resources**

1. Open the CloudWatch console at [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/).

1. In the navigation bar, choose **Logs**.

1. Choose the **/aws/kinesis-analytics/MyApplication** log group.

1. Choose **Delete Log Group** and then confirm the deletion.

## Next step
<a name="gs-table-cleanup-next-step-5"></a>

[Explore additional resources](gs-table-next-steps.md)