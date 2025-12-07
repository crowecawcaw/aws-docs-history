# Logging Amazon SageMaker Unified Studio MCP calls using AWS CloudTrail

Amazon SageMaker Unified Studio MCP Server is integrated with AWS CloudTrail, a service that provides a record of actions taken by a user, role, or an AWS service in Amazon SageMaker Unified Studio MCP Server. CloudTrail captures all API calls for Amazon SageMaker Unified Studio MCP Server as events. The calls captured include calls to Amazon SageMaker Unified Studio MCP Server and code calls to other AWS operations during the tool executions from the SageMaker Unified Studio MCP Server. If you create a trail, you can enable continuous delivery of CloudTrail events to an Amazon S3 bucket, including events for Amazon SageMaker Unified Studio MCP Server. If you don't configure a trail, you can still view the most recent events in the CloudTrail console in **Event history**. Using the information collected by CloudTrail, you can determine the request that was made to Amazon SageMaker Unified Studio MCP Server, the IP address from which the request was made, who made the request, when it was made, and additional details.

To learn more about CloudTrail, see the [AWS CloudTrail User Guide](../../../awscloudtrail/latest/userguide.md "../../../awscloudtrail/latest/userguide.md").

## Amazon SageMaker Unified Studio MCP Server information in CloudTrail

CloudTrail is enabled on your AWS account when you create the account. When activity occurs in Amazon SageMaker Unified Studio MCP Server, that activity is recorded in a CloudTrail event along with other AWS service events in **Event history**. You can view, search, and download recent events in your AWS account. For more information, see [Viewing events with CloudTrail Event history](../../../awscloudtrail/latest/userguide/view-cloudtrail-events.md "../../../awscloudtrail/latest/userguide/view-cloudtrail-events.md").

For an ongoing record of events in your AWS account, including events for SageMaker Unified Studio MCP Server, create a trail. A trail enables CloudTrail to deliver log files to an Amazon S3 bucket. By default, when you create a trail in the console, the trail applies to all AWS Regions. The trail logs events from all Regions in the AWS partition and delivers the log files to the Amazon S3 bucket that you specify. Additionally, you can configure other AWS services to further analyze and act upon the event data collected in CloudTrail logs. For more information, see the following:

- [Overview for creating a trail](../../../awscloudtrail/latest/userguide/cloudtrail-create-and-update-a-trail.md "../../../awscloudtrail/latest/userguide/cloudtrail-create-and-update-a-trail.md")
- [CloudTrail supported services and integrations](../../../awscloudtrail/latest/userguide/cloudtrail-aws-service-specific-topics.md "../../../awscloudtrail/latest/userguide/cloudtrail-aws-service-specific-topics.md")
- [Configuring Amazon SNS notifications for CloudTrail](../../../awscloudtrail/latest/userguide/configure-sns-notifications-for-cloudtrail.md "../../../awscloudtrail/latest/userguide/configure-sns-notifications-for-cloudtrail.md")
- [Receiving CloudTrail log files from multiple regions](../../../awscloudtrail/latest/userguide/receive-cloudtrail-log-files-from-multiple-regions.md "../../../awscloudtrail/latest/userguide/receive-cloudtrail-log-files-from-multiple-regions.md") and [Receiving CloudTrail log files from multiple accounts](../../../awscloudtrail/latest/userguide/cloudtrail-receive-logs-from-multiple-accounts.md "../../../awscloudtrail/latest/userguide/cloudtrail-receive-logs-from-multiple-accounts.md")

All SageMaker Unified Studio MCP Server tool invocations and API calls to AWS services during the tool executions are logged by CloudTrail. For example, calls to the different tools and AWS service calls made from the tools generate entries in the CloudTrail log files.

Every event or log entry contains information about who generated the request. The identity information helps you determine the following:

- Whether the request was made with root or IAM user credentials.
- Whether the request was made with temporary security credentials for a role or federated user.
- Whether the request was made by another AWS service.

For more information, see the [CloudTrail userIdentity element](../../../awscloudtrail/latest/userguide/cloudtrail-event-reference-user-identity.md "../../../awscloudtrail/latest/userguide/cloudtrail-event-reference-user-identity.md").

## Understanding Amazon SageMaker Unified Studio MCP Server log file entries

A trail is a configuration that enables delivery of events as log files to an Amazon S3 bucket that you specify. CloudTrail log files contain one or more log entries. An event represents a single request from any source and includes information about the requested action, the date and time of the action, request parameters, and so on. CloudTrail log files aren't an ordered stack trace of the public API calls, so they don't appear in any specific order.

The following example shows a CloudTrail log entry that demonstrates the `CallTool` action.

```
{
    "eventVersion": "1.09",
    "userIdentity": {
        ...
    },
    "eventTime": "...",
    "eventSource": "sagemaker-unified-studio-mcp.amazonaws.com",
    "eventName": "CallPrivilegedTool",
    "awsRegion": "us-east-1",
    "sourceIPAddress": "...",
    "userAgent": "...",
    "requestParameters": {
        "id": 1,
        "method": "tools/call",
        "params": {
            "name": "generate_spark_upgrade_plan",
            "arguments": "***",
            "_meta": {
                "progressToken": 1
            }
        },
        "jsonrpc": "2.0"
    },
    "responseElements": {
        "result": {
            "content": "***",
            "structuredContent": "***",
            "isError": false
        },
        "id": 1,
        "jsonrpc": "2.0"
    },
    "requestID": "12345678-1234-1234-1234-123456789012",
    "eventID": "87654321-4321-4321-4321-210987654321",
    "readOnly": false,
    "eventType": "AwsMcpEvent",
    "managementEvent": true,
    "recipientAccountId": "123456789012",
    "eventCategory": "Management"
}
```

The following example shows a CloudTrail log entry that demonstrates the `AddJobFlowSteps` action from Amazon SageMaker Unified Studio MCP during an upgrade tool invocation.

```
{
    "eventVersion": "1.11",
    "userIdentity": {
        "type": "AssumedRole",
        "principalId": "...",
        "arn": "...",
        "accountId": "123456789012",
        "accessKeyId": "...",
        "sessionContext": {
            ...
        },
        "invokedBy": "sagemaker-unified-studio-mcp.amazonaws.com"
    },
    "eventTime": "...",
    "eventSource": "elasticmapreduce.amazonaws.com",
    "eventName": "AddJobFlowSteps",
    "awsRegion": "us-east-1",
    "sourceIPAddress": "sagemaker-unified-studio-mcp.amazonaws.com",
    "userAgent": "sagemaker-unified-studio-mcp.amazonaws.com",
    "requestParameters": {
        "jobFlowId": "j-2PY4KXXXXXX63",
        "steps": [
            ...
        ]
    },
    "responseElements": {
        "stepIds": [
            ...
        ]
    },
    "requestID": "12345678-1234-1234-1234-123456789013",
    "eventID": "87654321-4321-4321-4321-210987654322",
    "readOnly": false,
    "eventType": "AwsApiCall",
    "managementEvent": true,
    "recipientAccountId": "123456789012",
    "sharedEventID": "12345678-1234-1234-1234-123456789012",
    "vpcEndpointId": "sagemaker-unified-studio-mcp.amazonaws.com",
    "vpcEndpointAccountId": "sagemaker-unified-studio-mcp.amazonaws.com",
    "eventCategory": "Management"
}
```
