# Monitor Amazon Bedrock API calls using CloudTrail

Amazon Bedrock is integrated with AWS CloudTrail, a service that provides a record of actions
taken by a user, role, or an AWS service in Amazon Bedrock. CloudTrail captures all API calls for
Amazon Bedrock as events. The calls captured include calls from the Amazon Bedrock console and
code calls to the Amazon Bedrock API operations. If you create a trail, you can enable
continuous delivery of CloudTrail events to an Amazon S3 bucket, including events for Amazon Bedrock.

If you don't configure a trail, you can still view the most recent events in the CloudTrail console
in **Event history**.

Using the information collected by CloudTrail, you can
determine the request that was made to Amazon Bedrock, the IP address from which the request
was made, who made the request, when it was made, and additional details.

To learn more about CloudTrail, see the [AWS CloudTrail User Guide](../../../awscloudtrail/latest/userguide/cloudtrail-user-guide.md "../../../awscloudtrail/latest/userguide/cloudtrail-user-guide.md").

## Amazon Bedrock information in CloudTrail

CloudTrail is enabled on your AWS account when you create the account. When activity occurs
in Amazon Bedrock, that activity is recorded in a CloudTrail event along with other AWS service events
in **Event history**. You can view, search, and download recent events in
your AWS account. For more information, see [Viewing events with CloudTrail Event
history](../../../awscloudtrail/latest/userguide/view-cloudtrail-events.md "../../../awscloudtrail/latest/userguide/view-cloudtrail-events.md").

For an ongoing record of events in your AWS account, including events for Amazon Bedrock,
create a trail. A _trail_ enables CloudTrail to deliver log files to an Amazon S3 bucket.
By default, when you create a trail in the console, the trail applies to all AWS Regions. The trail
logs events from all Regions in the AWS partition and delivers the log files to the Amazon S3 bucket
that you specify. Additionally, you can configure other AWS services to further analyze and act
upon the event data collected in CloudTrail logs. For more information, see the following:

- [Overview for creating a trail](../../../awscloudtrail/latest/userguide/cloudtrail-create-and-update-a-trail.md "../../../awscloudtrail/latest/userguide/cloudtrail-create-and-update-a-trail.md")
- [CloudTrail supported services and integrations](../../../awscloudtrail/latest/userguide/cloudtrail-aws-service-specific-topics.md "../../../awscloudtrail/latest/userguide/cloudtrail-aws-service-specific-topics.md")
- [Configuring Amazon SNS notifications
  for CloudTrail](../../../awscloudtrail/latest/userguide/configure-sns-notifications-for-cloudtrail.md "../../../awscloudtrail/latest/userguide/configure-sns-notifications-for-cloudtrail.md")
- [Receiving CloudTrail log
  files from multiple Regions](../../../awscloudtrail/latest/userguide/receive-cloudtrail-log-files-from-multiple-regions.md "../../../awscloudtrail/latest/userguide/receive-cloudtrail-log-files-from-multiple-regions.md") and [Receiving CloudTrail log
  files from multiple accounts](../../../awscloudtrail/latest/userguide/cloudtrail-receive-logs-from-multiple-accounts.md "../../../awscloudtrail/latest/userguide/cloudtrail-receive-logs-from-multiple-accounts.md")

Every event or log entry contains information about who generated the request. The
identity information helps you determine the following:

- Whether the request was made with root or AWS Identity and Access Management (IAM) user credentials.
- Whether the request was made with temporary security credentials for a role or
  federated user.
- Whether the request was made by another AWS service.

For more information, see the [CloudTrail userIdentity
element](../../../awscloudtrail/latest/userguide/cloudtrail-event-reference-user-identity.md "../../../awscloudtrail/latest/userguide/cloudtrail-event-reference-user-identity.md").

## Amazon Bedrock data events in CloudTrail

[Data events](../../../awscloudtrail/latest/userguide/logging-data-events-with-cloudtrail.md#logging-data-events "../../../awscloudtrail/latest/userguide/logging-data-events-with-cloudtrail.md#logging-data-events") provide information about the resource operations performed on or in a resource (for example, reading or writing to an Amazon S3 object). These are also known as data plane operations. Data events are often high-volume activities that CloudTrail doesn’t log by default.

Amazon Bedrock logs some [Amazon Bedrock Runtime API operations](../APIReference/API_Operations_Amazon_Bedrock_Runtime.md "../APIReference/API_Operations_Amazon_Bedrock_Runtime.md") (such as `InvokeModel`, `InvokeModelWithResponseStream`, `Converse`, `ConverseStream`, and `ListAsyncInvokes`) as
[management events](../../../awscloudtrail/latest/userguide/logging-management-events-with-cloudtrail.md#logging-management-events "../../../awscloudtrail/latest/userguide/logging-management-events-with-cloudtrail.md#logging-management-events").

Amazon Bedrock logs other [Amazon Bedrock Runtime API operations](../APIReference/API_Operations_Amazon_Bedrock_Runtime.md "../APIReference/API_Operations_Amazon_Bedrock_Runtime.md") (such as `InvokeModelWithBidirectionalStream`, `GetAsyncInvoke`, and `StartAsyncInvokes`) as data events.

Amazon Bedrock logs all [Agents for Amazon Bedrock Runtime API operations](../APIReference/API_Operations_Agents_for_Amazon_Bedrock_Runtime.md "../APIReference/API_Operations_Agents_for_Amazon_Bedrock_Runtime.md") (such as `InvokeAgent` and `InvokeInlineAgent`) actions to CloudTrail as data events.

- To log [InvokeAgent](../APIReference/API_agent-runtime_InvokeAgent.md "../APIReference/API_agent-runtime_InvokeAgent.md") calls, configure advanced event selectors to record data events for the `AWS::Bedrock::AgentAlias` resource type.
- To log [InvokeInlineAgent](../APIReference/API_agent-runtime_InvokeInlineAgent.md "../APIReference/API_agent-runtime_InvokeInlineAgent.md")
  calls, configure advanced event selectors to record data events for the `AWS::Bedrock::InlineAgent` resource type.
- To log [InvokeModelWithBidirectionalStream](../APIReference/API_runtime_InvokeModelWithBidirectionalStream.md "../APIReference/API_runtime_InvokeModelWithBidirectionalStream.md") calls,
  configure advanced event selectors to record data events for the `AWS::Bedrock::Model` resource type and `AWS:Bedrock::AsyncInvoke`.
- To log [GetAsyncInvoke](../APIReference/API_runtime_GetAsyncInvoke.md "../APIReference/API_runtime_GetAsyncInvoke.md") and
  [StartAsyncInvoke](../APIReference/API_runtime_StartAsyncInvoke.md "../APIReference/API_runtime_StartAsyncInvoke.md") calls, configure advanced event selectors
  to record data events for the `AWS::Bedrock::Model` resource type and `AWS:Bedrock::AsyncInvoke`.
- To log [Retrieve](../APIReference/API_agent-runtime_Retrieve.md "../APIReference/API_agent-runtime_Retrieve.md") and [RetrieveAndGenerate](../APIReference/API_agent-runtime_RetrieveAndGenerate.md "../APIReference/API_agent-runtime_RetrieveAndGenerate.md") calls, configure advanced event selectors to record data events
  for the `AWS::Bedrock::KnowledgeBase` resource type.
- To log [InvokeFlow](../APIReference/API_agent-runtime_InvokeFlow.md "../APIReference/API_agent-runtime_InvokeFlow.md") calls, configure advanced event selectors to record data events for the `AWS::Bedrock::FlowAlias` resource type.
- To log `RenderPrompt` calls, configure advanced event selectors to record data events for the `AWS::Bedrock::Prompt` resource type. `RenderPrompt` is a permission-only [action](../../../service-authorization/latest/reference/list_amazonbedrock.md#amazonbedrock-actions-as-permissions "../../../service-authorization/latest/reference/list_amazonbedrock.md#amazonbedrock-actions-as-permissions") that renders prompts, created using [Prompt management](prompt-management.md "prompt-management.md"), for model invocation (`InvokeModel(WithResponseStream)` and `Converse(Stream)`).

From the CloudTrail console, choose **Bedrock agent alias** or **Bedrock knowledge base** for the **Data event type**. You can additionally filter on the `eventName` and `resources.ARN` fields by choosing a custom log selector template. For more information, see [Logging data events with the AWS Management Console](../../../awscloudtrail/latest/userguide/logging-data-events-with-cloudtrail.md "../../../awscloudtrail/latest/userguide/logging-data-events-with-cloudtrail.md").

From the AWS CLI, set the `resource.type` value equal to `AWS::Bedrock::AgentAlias`, `AWS::Bedrock::KnowledgeBase`, or `AWS::Bedrock::FlowAlias` and set the `eventCategory` equal to `Data`. For more information, see [Logging data events with the AWS CLI](../../../awscloudtrail/latest/userguide/logging-data-events-with-cloudtrail.md#creating-data-event-selectors-with-the-AWS-CLI "../../../awscloudtrail/latest/userguide/logging-data-events-with-cloudtrail.md#creating-data-event-selectors-with-the-AWS-CLI").

The following example shows how to configure a trail to log all Amazon Bedrock data events for all Amazon Bedrock resource types in the AWS CLI.

```
aws cloudtrail put-event-selectors --trail-name `trailName` \
--advanced-event-selectors \
'[
  {
    "Name": "Log all data events on an alias of an agent in Amazon Bedrock.",
    "FieldSelectors": [
      { "Field": "eventCategory", "Equals": ["Data"] },
      { "Field": "resources.type", "Equals": ["AWS::Bedrock::AgentAlias"] }
    ]
  },
  {
    "Name": "Log all data events on a knowledge base in Amazon Bedrock.",
    "FieldSelectors": [
      { "Field": "eventCategory", "Equals": ["Data"] },
      { "Field": "resources.type", "Equals": ["AWS::Bedrock::KnowledgeBase"] }
    ]
  },
  {
    "Name": "Log all data events on a flow in Amazon Bedrock.",
    "FieldSelectors": [
      { "Field": "eventCategory", "Equals": ["Data"] },
      { "Field": "resources.type", "Equals": ["AWS::Bedrock::FlowAlias"] }
    ]
  }
  {
    "Name": "Log all data events on a guardrail in Amazon Bedrock.",
    "FieldSelectors": [
      { "Field": "eventCategory", "Equals": ["Data"] },
      { "Field": "resources.type", "Equals": ["AWS::Bedrock::Guardrail"] }
    ]
  }
]'
```

You can additionally filter on the `eventName` and
`resources.ARN` fields. For more information about these fields, see [AdvancedFieldSelector](../../../awscloudtrail/latest/APIReference/API_AdvancedFieldSelector.md "../../../awscloudtrail/latest/APIReference/API_AdvancedFieldSelector.md").

Additional charges apply for data events. For more information about CloudTrail pricing, see [AWS CloudTrail Pricing](https://aws.amazon.com/cloudtrail/pricing/ "https://aws.amazon.com/cloudtrail/pricing/").

## Amazon Bedrock management events in CloudTrail

[Management events](../../../awscloudtrail/latest/userguide/logging-management-events-with-cloudtrail.md#logging-management-events "../../../awscloudtrail/latest/userguide/logging-management-events-with-cloudtrail.md#logging-management-events") provide information about management operations that are performed on resources in your AWS account. These are also known as control plane operations. CloudTrail logs management event API operations by default.

Amazon Bedrock logs [Amazon Bedrock Runtime API operations](../APIReference/API_Operations_Amazon_Bedrock_Runtime.md "../APIReference/API_Operations_Amazon_Bedrock_Runtime.md") (`InvokeModel`, `InvokeModelWithResponseStream`, `Converse`,
and `ConverseStream`) as [management events](../../../awscloudtrail/latest/userguide/logging-management-events-with-cloudtrail.md#logging-management-events "../../../awscloudtrail/latest/userguide/logging-management-events-with-cloudtrail.md#logging-management-events").

Amazon Bedrock logs the remainder of Amazon Bedrock API operations as management events. For a list of the
Amazon Bedrock API operations that Amazon Bedrock logs to CloudTrail, see the following pages in the Amazon Bedrock API reference.

- [Amazon Bedrock](../APIReference/API_Operations_Amazon_Bedrock.md "../APIReference/API_Operations_Amazon_Bedrock.md").
- [Amazon Bedrock Agents](../APIReference/API_Operations_Agents_for_Amazon_Bedrock.md "../APIReference/API_Operations_Agents_for_Amazon_Bedrock.md").
- [Amazon Bedrock Agents Runtime](../APIReference/API_Operations_Agents_for_Amazon_Bedrock_Runtime.md "../APIReference/API_Operations_Agents_for_Amazon_Bedrock_Runtime.md").
- [Amazon Bedrock Runtime](../APIReference/API_Operations_Amazon_Bedrock_Runtime.md "../APIReference/API_Operations_Amazon_Bedrock_Runtime.md").

All [Amazon Bedrock API operations](../APIReference/API_Operations_Amazon_Bedrock.md "../APIReference/API_Operations_Amazon_Bedrock.md") and [Agents for Amazon Bedrock API operations](../APIReference/API_Operations_Agents_for_Amazon_Bedrock.md "../APIReference/API_Operations_Agents_for_Amazon_Bedrock.md") are logged by CloudTrail and documented in the [Amazon Bedrock API Reference](../APIReference.md "../APIReference.md"). For example,
calls to the `InvokeModel`, `StopModelCustomizationJob`, and `CreateAgent` actions generate
entries in the CloudTrail log files.

[Amazon GuardDuty](https://aws.amazon.com/guardduty/ "https://aws.amazon.com/guardduty/") continuously monitors and
analyzes your CloudTrail management and event logs to detect potential security issues. When you
enable Amazon GuardDuty for an AWS account, it automatically starts analyzing CloudTrail logs to detect
suspicious activity in Amazon Bedrock APIs, such as a user logging in from a new location and using
Amazon Bedrock APIs to remove Amazon Bedrock Guardrails, or change the Amazon S3 bucket set for model training
data.

## Understanding Amazon Bedrock log file entries

A trail is a configuration that enables delivery of events as log files to an Amazon S3 bucket
that you specify. CloudTrail log files contain one or more log entries. An event represents a single
request from any source and includes information about the requested action, the date and time
of the action, request parameters, and so on. CloudTrail log files aren't an ordered stack trace of
the public API calls, so they don't appear in any specific order.

The following example shows a CloudTrail log entry that demonstrates the `InvokeModel` action.

```
{
    "eventVersion": "1.08",
    "userIdentity": {
        "type": "IAMUser",
        "principalId": "AROAICFHPEXAMPLE",
        "arn": "arn:aws:iam::111122223333:user/userxyz",
        "accountId": "111122223333",
        "accessKeyId": "AKIAIOSFODNN7EXAMPLE",
        "userName": "userxyz"
    },
    "eventTime": "2023-10-11T21:58:59Z",
    "eventSource": "bedrock.amazonaws.com",
    "eventName": "InvokeModel",
    "awsRegion": "us-west-2",
    "sourceIPAddress": "192.0.2.0",
    "userAgent": "Boto3/1.28.62 md/Botocore#1.31.62 ua/2.0 os/macos#22.6.0 md/arch#arm64 lang/python#3.9.6 md/pyimpl#CPython cfg/retry-mode#legacy Botocore/1.31.62",
    "requestParameters": {
        "modelId": "stability.stable-diffusion-xl-v0"
    },
    "responseElements": null,
    "requestID": "a1b2c3d4-5678-90ab-cdef-EXAMPLE22222",
    "eventID": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111 ",
    "readOnly": false,
    "eventType": "AwsApiCall",
    "managementEvent": true,
    "recipientAccountId": "111122223333",
    "eventCategory": "Management",
    "tlsDetails": {
        "tlsVersion": "TLSv1.2",
        "cipherSuite": "cipher suite",
        "clientProvidedHostHeader": "bedrock-runtime.us-west-2.amazonaws.com"
    }
}
```
