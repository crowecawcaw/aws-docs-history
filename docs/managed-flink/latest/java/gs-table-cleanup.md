Amazon Managed Service for Apache Flink (Amazon MSF) was previously known as Amazon Kinesis Data Analytics for Apache Flink.

# Clean up AWS resources

This section includes procedures for cleaning up AWS resources created in the
Getting Started (Table API) tutorial.

###### This topic contains the following sections.

- [Delete your Managed Service for Apache Flink application](#gs-table-cleanup-app "#gs-table-cleanup-app")
- [Delete your Amazon S3 objects and bucket](#gs-table-cleanup-s3 "#gs-table-cleanup-s3")
- [Delete your IAM resources](#gs-table-cleanup-iam "#gs-table-cleanup-iam")
- [Delete your CloudWatch resources](#gs-table-cleanup-cw "#gs-table-cleanup-cw")
- [Next step](#gs-table-cleanup-next-step-5 "#gs-table-cleanup-next-step-5")

## Delete your Managed Service for Apache Flink application

Use the following procedure to delete the application.

###### To delete the application

1. Open the Kinesis console at
   [https://console.aws.amazon.com/kinesis](https://console.aws.amazon.com/kinesis "https://console.aws.amazon.com/kinesis").
2. In the Managed Service for Apache Flink panel, choose **MyApplication**.
3. From the **Actions** dropdown list, choose
   **Delete** and then confirm the deletion.

## Delete your Amazon S3 objects and bucket

Use the following procedure to delete your S3 objects and bucket.

###### To delete the application object from the S3 bucket

1. Open the Amazon S3 console at
   [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
2. Select the S3 bucket that you created.
3. Select the application artifact that you uploaded named
   `amazon-msf-java-table-app-1.0.jar`, choose
   **Delete**, and then confirm the deletion.

###### To delete all output files written by the application

1. Choose the `output` folder.
2. Choose **Delete**.
3. Confirm that you want to permanently delete the content.

###### To delete the S3 bucket

1. Open the Amazon S3 console at
   [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
2. Select the S3 bucket you created.
3. Choose **Delete** and confirm the deletion.

## Delete your IAM resources

Use the following procedure to delete your IAM resources.

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

Use the following procedure to delete your CloudWatch resources.

###### To delete your CloudWatch resources

1. Open the CloudWatch console at
   [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
2. In the navigation bar, choose **Logs**.
3. Choose the **/aws/kinesis-analytics/MyApplication** log
   group.
4. Choose **Delete Log Group** and then confirm the
   deletion.

## Next step

[Explore additional resources](gs-table-next-steps.md "gs-table-next-steps.md")
