# Retrieve PCUI and AWS ParallelCluster runtime logs

Learn how to retrieve the PCUI and AWS ParallelCluster runtime logs for troubleshooting. To start, find the relevant PCUI and
AWS ParallelCluster stack names. Use the stack name to locate the installation log groups. To finish, export the logs. These logs are specific to the
AWS ParallelCluster runtime. For cluster logs, see [Retrieving and preserving logs](troubleshooting-v3-get-logs.md "troubleshooting-v3-get-logs.md").

###### Prerequisites

- The AWS CLI is installed.
- You have credentials to run AWS CLI commands on the AWS account that the PCUI is on.
- You can access the Amazon CloudWatch console on the AWS account that the PCUI is on.

## Step 1: Locate the stack names for the relevant stacks

In the following example, replace the red highlighted text with your actual values.

List the stacks, using the AWS Region where you installed the PCUI:

```
`$` `aws cloudformation list-stacks --region `aws-region-id``
```

Note the stack names for the following stacks:

- The name of the stack that deployed the PCUI on your account. You entered this name when you installed the PCUI; for example,
  `pcluster-ui`.
- The AWS ParallelCluster stack that is prefixed with the stack name you entered; for example,
  `pcluster-ui-ParallelClusterApi-ABCD1234EFGH`.

## Step 2: Locate the log groups

List the log groups of the PCUI stack, as shown in the following example:

```
`$` `aws cloudformation describe-stack-resources \
 --region `aws-region-id` \
 --stack-name `pcluster-ui` \
 --query "StackResources[?ResourceType == 'AWS::Logs::LogGroup' && (LogicalResourceId == 'ApiGatewayAccessLog' || LogicalResourceId == 'ParallelClusterUILambdaLogGroup')].PhysicalResourceId" \
 --output text`
```

List the log groups of the AWS ParallelCluster API stack, as shown in the following example:

```
`$` `aws cloudformation describe-stack-resources \
 --region `aws-region-id` \
 --stack-name `pcluster-ui-ParallelCluster-Api-ABCD1234EFGH` \
 --query "StackResources[?ResourceType == 'AWS::Logs::LogGroup' && LogicalResourceId == 'ParallelClusterFunctionLogGroup'].PhysicalResourceId" \
 --output text`
```

Note the lists of log groups for use in the next step.

## Step 3: Export the logs

Use the following steps to gather and export the logs:

1. Log in to the AWS Management Console, and then navigate to the [Amazon CloudWatch](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/") console on the AWS account
   that the PCUI is on.
2. Choose **Logs**, **Logs Insights** in the navigation pane.
3. Select all of the log groups listed in the previous step.
4. Choose a time range, such as 12 hours.
5. Run the following query:

````
`$` `fields @timestamp, @message
| sort @timestamp desc
| limit 10000` ``` 6. Choose **Export results**, **Download table (JSON)**.
````
