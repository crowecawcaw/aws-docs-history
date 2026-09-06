

# Query flow logs using Amazon Athena
<a name="flow-logs-athena"></a>

Amazon Athena is an interactive query service that enables you to analyze data in Amazon S3, such as your flow logs, using standard SQL. You can use Athena with VPC Flow Logs to quickly get actionable insights about the traffic flowing through your VPC. For example, you can identify which resources in your virtual private clouds (VPCs) are the top talkers or identify the IP addresses with the most rejected TCP connections.

**Options**
+ You can streamline and automate the integration of your VPC flow logs with Athena. Generate a CloudFormation template that creates the required AWS resources and predefined queries to obtain insights about the traffic flowing through your VPC.
+ You can create your own queries using Athena. For more information, see [Query flow logs using Amazon Athena](https://docs.aws.amazon.com/athena/latest/ug/vpc-flow-logs.html) in the *Amazon Athena User Guide*.

**Pricing**  
You incur standard [Amazon Athena charges](https://aws.amazon.com/athena/pricing/) for running queries. You incur standard [AWS Lambda charges](https://aws.amazon.com/lambda/pricing/) for the Lambda function that loads new partitions on a recurring schedule (when you specify a partition load frequency but do not specify a start and end date.)

**Topics**
+ [Generate the CloudFormation template using the console](flow-logs-generate-template-console.md)
+ [Generate the CloudFormation template using the AWS CLI](flow-logs-generate-template-cli.md)
+ [Run a predefined query](flow-logs-run-athena-query.md)