

# Logging Amazon SageMaker Unified Studio MCP calls using AWS CloudTrail

Amazon SageMaker Unified Studio MCP Server is integrated with AWS CloudTrail, a service that provides a record of actions taken by a user, role, or an AWS service in Amazon SageMaker Unified Studio MCP Server. CloudTrail captures all API calls for Amazon SageMaker Unified Studio MCP Server as events. The calls captured include calls to Amazon SageMaker Unified Studio MCP Server and code calls to other AWS operations during the tool executions from the SageMaker Unified Studio MCP Server. If you create a trail, you can enable continuous delivery of CloudTrail events to an Amazon S3 bucket, including events for Amazon SageMaker Unified Studio MCP Server. If you don't configure a trail, you can still view the most recent events in the CloudTrail console in **Event history**. Using the information collected by CloudTrail, you can determine the request that was made to Amazon SageMaker Unified Studio MCP Server, the IP address from which the request was made, who made the request, when it was made, and additional details.

To learn more about CloudTrail, see the [AWS CloudTrail User Guide](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/).

## Amazon SageMaker Unified Studio MCP Server information in CloudTrail
<a name="sagemaker-mcp-info-in-cloudtrail"></a>

CloudTrail is enabled on your AWS account when you create the account. When activity occurs in Amazon SageMaker Unified Studio MCP Server, that activity is recorded in a CloudTrail event along with other AWS service events in **Event history**. You can view, search, and download recent events in your AWS account. For more information, see [Viewing events with CloudTrail Event history](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/view-cloudtrail-events.html).

For an ongoing record of events in your AWS account, including events for SageMaker Unified Studio MCP Server, create a trail. A trail enables CloudTrail to deliver log files to an Amazon S3 bucket. By default, when you create a trail in the console, the trail applies to all AWS Regions. The trail logs events from all Regions in the AWS partition and delivers the log files to the Amazon S3 bucket that you specify. Additionally, you can configure other AWS services to further analyze and act upon the event data collected in CloudTrail logs. For more information, see the following:
+ [Overview for creating a trail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-create-and-update-a-trail.html)
+ [CloudTrail supported services and integrations](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-aws-service-specific-topics.html)
+ [Configuring Amazon SNS notifications for CloudTrail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/configure-sns-notifications-for-cloudtrail.html)
+ [Receiving CloudTrail log files from multiple regions](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/receive-cloudtrail-log-files-from-multiple-regions.html) and [Receiving CloudTrail log files from multiple accounts](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-receive-logs-from-multiple-accounts.html)

All SageMaker Unified Studio MCP Server tool invocations and API calls to AWS services during the tool executions are logged by CloudTrail. For example, calls to the different tools and AWS service calls made from the tools generate entries in the CloudTrail log files.

Every event or log entry contains information about who generated the request. The identity information helps you determine the following:
+ Whether the request was made with root or IAM user credentials.
+ Whether the request was made with temporary security credentials for a role or federated user.
+ Whether the request was made by another AWS service.

For more information, see the [CloudTrail userIdentity element](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-event-reference-user-identity.html).

## Understanding Amazon SageMaker Unified Studio MCP Server log file entries
<a name="understanding-mcp-log-entries"></a>

A trail is a configuration that enables delivery of events as log files to an Amazon S3 bucket that you specify. CloudTrail log files contain one or more log entries. An event represents a single request from any source and includes information about the requested action, the date and time of the action, request parameters, and so on. CloudTrail log files aren't an ordered stack trace of the public API calls, so they don't appear in any specific order.

The following example shows a CloudTrail log entry that demonstrates the `CallPrivilegedTool` action for an `analyze_spark_workload` invocation.

```
{
    "eventVersion": "1.11",
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
            "name": "analyze_spark_workload",
            "arguments": "***",
            "_meta": {
                "AWS_REGION": "us-east-1",
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
    "eventCategory": "Management",
    "tlsDetails": {
        "tlsVersion": "TLSv1.3",
        "cipherSuite": "TLS_AES_128_GCM_SHA256"
    }
}
```

The following example shows a CloudTrail log entry that demonstrates the Amazon EMR Serverless `GetJobRun` action that Amazon SageMaker Unified Studio MCP calls during a tool invocation.

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
        "invokedBy": "us-east-1.dataprocessing-mcp.amazonaws.com"
    },
    "eventTime": "...",
    "eventSource": "emr-serverless.amazonaws.com",
    "eventName": "GetJobRun",
    "awsRegion": "us-east-1",
    "sourceIPAddress": "us-east-1.dataprocessing-mcp.amazonaws.com",
    "userAgent": "us-east-1.dataprocessing-mcp.amazonaws.com",
    "requestParameters": {
        "jobRunId": "00xxxxxxxxxxxxxx",
        "applicationId": "00yyyyyyyyyyyyyy"
    },
    "responseElements": null,
    "requestID": "12345678-1234-1234-1234-123456789013",
    "eventID": "87654321-4321-4321-4321-210987654322",
    "readOnly": true,
    "eventType": "AwsApiCall",
    "managementEvent": true,
    "recipientAccountId": "123456789012",
    "vpcEndpointId": "vpce-1234567890abcdef0",
    "eventCategory": "Management"
}
```