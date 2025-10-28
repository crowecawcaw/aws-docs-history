Amazon Managed Service for Apache Flink (Amazon MSF) was previously known as Amazon Kinesis Data Analytics for Apache Flink.

# Create and run the application (console)

Follow these steps to create, configure, update, and run the application using
the console.

## Create the

Application

1. Sign in to the AWS Management Console, and open the Amazon MSF console at https://console.aws.amazon.com/flink.
2. On the Managed Service for Apache Flink dashboard, choose **Create analytics
   application**.
3. On the **Managed Service for Apache Flink - Create application**
   page, provide the application details as follows:
   - For **Application name**, enter
     `MyApplication`.
   - For **Description**, enter `My
scala test app`.
   - For **Runtime**, choose **Apache
     Flink**.
   - Keep the version as **Apache Flink version
     1.19.1**.

4. For **Access permissions**, choose
   **Create / update IAM role
   `kinesis-analytics-MyApplication-us-west-2`**.
5. Choose **Create application**.

###### Note

When you create a Managed Service for Apache Flink application using the console, you have the option of
having an IAM role and policy created for your application. Your
application uses this role and policy to access its dependent resources.
These IAM resources are named using your application name and Region
as follows:

- Policy:
  `kinesis-analytics-service-`MyApplication`-`us-west-2``
- Role:
  `kinesisanalytics-`MyApplication`-`us-west-2``

## Configure the

application

Use the following procedure to configure the application.

###### To configure the application

1. On the **MyApplication** page, choose
   **Configure**.
2. On the **Configure application** page, provide
   the **Code location**:
   - For **Amazon S3 bucket**, enter
     `ka-app-code-`<username>``.
   - For **Path to Amazon S3 object**, enter
     `getting-started-scala-1.0.jar.`.

3. Under **Access to application resources**, for
   **Access permissions**, choose **Create
   / update IAM role
   `kinesis-analytics-MyApplication-us-west-2`**.
4. Under **Properties**, choose **Add group**.
5. Enter the following:

| Group ID                   | Key                    | Value                 |
| -------------------------- | ---------------------- | --------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `ConsumerConfigProperties` | `input.stream.name`    | `ExampleInputStream`  |
| `ConsumerConfigProperties` | `aws.region`           | `us-west-2`           |
| `ConsumerConfigProperties` | `flink.stream.initpos` | `LATEST`              | Choose **Save**. 6. Under **Properties**, choose **Add group** again. 7. Enter the following:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| Group ID                   | Key                    | Value                 |
| ---                        | ---                    | ---                   |
| `ProducerConfigProperties` | `output.stream.name`   | `ExampleOutputStream` |
| `ProducerConfigProperties` | `aws.region`           | `us-west-2`           | 8. Under **Monitoring**, ensure that the **Monitoring metrics level** is set to **Application**. 9. For **CloudWatch logging**, choose the **Enable** check box. 10. Choose **Update**. ###### Note When you choose to enable Amazon CloudWatch logging, Managed Service for Apache Flink creates a log group and log stream for you. The names of these resources are as follows: <br>• Log group: `/aws/kinesis-analytics/MyApplication` <br>• Log stream: `kinesis-analytics-log-stream` ## Edit the IAM policy Edit the IAM policy to add permissions to access the Amazon S3 bucket. ###### To edit the IAM policy to add S3 bucket permissions 1. Open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/"). 2. Choose **Policies**. Choose the **`kinesis-analytics-service-MyApplication-us-west-2`** policy that the console created for you in the previous section. 3. On the **Summary** page, choose **Edit policy**. Choose the **JSON** tab. 4. Add the highlighted section of the following policy example to the policy. Replace the sample account IDs (`012345678901`) with your account ID. JSON `` `{ "Version":"2012-10-17", "Statement": [ { "Sid": "ReadCode", "Effect": "Allow", "Action": [ "s3:GetObject", "s3:GetObjectVersion" ], "Resource": [ "arn:aws:s3:::ka-app-code-`username`/getting-started-scala-1.0.jar" ] }, { "Sid": "DescribeLogGroups", "Effect": "Allow", "Action": [ "logs:DescribeLogGroups" ], "Resource": [ "arn:aws:logs:us-west-2:`012345678901`:log-group:*" ] }, { "Sid": "DescribeLogStreams", "Effect": "Allow", "Action": [ "logs:DescribeLogStreams" ], "Resource": [ "arn:aws:logs:us-west-2:`012345678901`:log-group:/aws/kinesis-analytics/MyApplication:log-stream:*" ] }, { "Sid": "PutLogEvents", "Effect": "Allow", "Action": [ "logs:PutLogEvents" ], "Resource": [ "arn:aws:logs:us-west-2:`012345678901`:log-group:/aws/kinesis-analytics/MyApplication:log-stream:kinesis-analytics-log-stream" ] }, { "Sid": "ReadInputStream", "Effect": "Allow", "Action": "kinesis:*", "Resource": "arn:aws:kinesis:us-west-2:`012345678901`:stream/ExampleInputStream" }, { "Sid": "WriteOutputStream", "Effect": "Allow", "Action": "kinesis:*", "Resource": "arn:aws:kinesis:us-west-2:`012345678901`:stream/ExampleOutputStream" } ] }` `` ## Run the application The Flink job graph can be viewed by running the application, opening the Apache Flink dashboard, and choosing the desired Flink job. ## Stop the application To stop the application, on the **MyApplication** page, choose **Stop**. Confirm the action. |
