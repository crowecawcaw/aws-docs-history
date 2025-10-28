Amazon Managed Service for Apache Flink (Amazon MSF) was previously known as Amazon Kinesis Data Analytics for Apache Flink.

# Clean up your application and dependent resources

## Delete your Studio notebook

1. Open the Managed Service for Apache Flink console.
2. Choose **MyNotebook**.
3. Choose **Actions**, then **Delete**.

## Delete your AWS Glue database and connection

1. Open the AWS Glue console at [https://console.aws.amazon.com/glue/](https://console.aws.amazon.com/glue/ "https://console.aws.amazon.com/glue/").
2. Choose **Databases** from the left navigation bar. Check the checkbox next
   to **Default** to select it. Choose **Action**, **Delete Database**.
   Confirm your selection.
3. Choose **Connections** from the left navigation bar. Check the checkbox next
   to **ZeppelinConnection** to select it. Choose **Action**, **Delete Connection**.
   Confirm your selection.

## Delete your IAM role and policy

1. Open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. Choose **Roles** from the left navigation bar.
3. Use the search bar to search for the **ZeppelinRole** role.
4. Choose the **ZeppelinRole** role. Choose **Delete Role**. Confirm the deletion.

## Delete your CloudWatch log group

The console creates a CloudWatch Logs group and log stream for you when you create your application using the console.
You do not have a log group and stream if you created your application using the AWS CLI.

1. Open the CloudWatch console at [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
2. Choose **Log groups** from the left navigation bar.
3. Choose the **/AWS/KinesisAnalytics/MyNotebook** log group.
4. Choose **Actions**, **Delete log group(s)**. Confirm the deletion.

## Clean up Kinesis Data Streams resources

To delete your Kinesis stream, open the Kinesis Data Streams console, select your Kinesis stream, and choose
**Actions**, **Delete**.

## Clean up MSK resources

Follow the steps in this section if you created an Amazon MSK cluster for this tutorial.
This section has directions for cleaning up your Amazon EC2 client instance, Amazon VPC,
and Amazon MSK cluster.

### Delete your Amazon MSK cluster

Follow these steps if you created an Amazon MSK cluster for this tutorial.

1. Open the Amazon MSK console at [https://console.aws.amazon.com/msk/home?region=us-east-1#/home/](https://console.aws.amazon.com/msk/home?region=us-east-1#/home/ "https://console.aws.amazon.com/msk/home?region=us-east-1#/home/").
2. Choose **AWSKafkaTutorialCluster**. Choose **Delete**.
   Enter `delete` in the window that appears, and confirm your selection.

### Terminate your client instance

Follow these steps if you created an Amazon EC2 client instance for this tutorial.

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. Choose **Instances** from the left navigation bar.
3. Choose the checkbox next to **ZeppelinClient** to select it.
4. Choose **Instance State**, **Terminate Instance**.

### Delete your Amazon VPC

Follow these steps if you created an Amazon VPC for this tutorial.

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. Choose **Network Interfaces** from the left navigation bar.
3. Enter your VPC ID in the search bar and press enter to search.
4. Select the checkbox in the table header to select all the displayed network interfaces.
5. Choose **Actions**, **Detach**. In the window that appears,
   choose **Enable** under **Force
   detachment**. Choose **Detach**, and wait
   for all of the network interfaces to reach the
   **Available** status.
6. Select the checkbox in the table header to select all the displayed network interfaces again.
7. Choose **Actions**, **Delete**. Confirm the action.
8. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/").
9. Select **AWSKafkaTutorialVPC**. Choose **Actions**, **Delete VPC**.
   Enter `delete` and confirm the deletion.
