# Generate the CloudFormation template using the console

After the first flow logs are delivered to your S3 bucket, you can integrate with Athena
by generating a CloudFormation template and using the template to create a stack.

###### Requirements

- The selected Region must support AWS Lambda and Amazon Athena.
- The Amazon S3 buckets must be in the selected Region.
- The log record format for the flow log must include the fields used by the
  specific predefined queries that you'd like to run.

###### To generate the template using the console

1. Do one of the following:
   - Open the Amazon VPC console. In the navigation pane, choose **Your VPCs**
     and then select your VPC.
   - Open the Amazon VPC console. In the navigation pane, choose **Subnets**
     and then select your subnet.
   - Open the Amazon EC2 console. In the navigation pane, choose **Network Interfaces**
     and then select your network interface.

2. On the **Flow logs** tab, select a flow log that
   publishes to Amazon S3 and then choose **Actions**,
   **Generate Athena integration**.
3. Specify the partition load frequency. If you choose
   **None**, you must specify the partition start and end
   date, using dates that are in the past. If you choose
   **Daily**, **Weekly**, or
   **Monthly**, the partition start and end dates are
   optional. If you do not specify start and end dates, the CloudFormation
   template creates a Lambda function that loads new partitions on a recurring
   schedule.
4. Select or create an S3 bucket for the generated template, and an S3 bucket
   for the query results.
5. Choose **Generate Athena integration**.
6. (Optional) In the success message, choose the link to navigate to the bucket that you specified
   for the CloudFormation template, and customize the template.
7. In the success message, choose **Create CloudFormation
   stack** to open the **Create Stack** wizard in
   the AWS CloudFormation console. The URL for the generated CloudFormation template is
   specified in the **Template** section. Complete the wizard
   to create the resources that are specified in the template.

###### Resources created by the CloudFormation template

- An Athena database. The database name is
  vpcflowlogsathenadatabase<_flow-logs-subscription-id_>.
- An Athena workgroup. The workgroup name is
  <_flow-log-subscription-id_><_partition-load-frequency_><_start-date_><_end-date_>workgroup
- A partitioned Athena table that corresponds to your flow log records. The table
  name is
  <_flow-log-subscription-id_><_partition-load-frequency_><_start-date_><_end-date_>.
- A set of Athena named queries. For more information, see [Predefined queries](flow-logs-run-athena-query.md#predefined-queries "flow-logs-run-athena-query.md#predefined-queries").
- A Lambda function that loads new partitions to the table on the specified
  schedule (daily, weekly, or monthly).
- An IAM role that grants permission to run the Lambda functions.
