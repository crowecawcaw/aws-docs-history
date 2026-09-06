

AWS FinOps Agent is in preview release and is subject to change.

# Monitoring and observability
<a name="monitoring-overview"></a>

## Logging AWS FinOps Agent API calls using AWS CloudTrail
<a name="logging-using-cloudtrail"></a>

AWS FinOps Agent is integrated with AWS CloudTrail. CloudTrail provides a record of actions taken by a user, role, or AWS service in AWS FinOps Agent. CloudTrail captures all API calls for AWS FinOps Agent as events, including calls from the AWS FinOps Agent console and code calls to the AWS FinOps Agent API operations.

If you create a trail, you can enable continuous delivery of CloudTrail events to an Amazon S3 bucket, including events for AWS FinOps Agent. If you don't configure a trail, you can still view the most recent events in the CloudTrail console in **Event history**.

Using the information collected by CloudTrail, you can determine which request was sent to AWS FinOps Agent, the source IP address, who made the request, when it was made, and other details. To learn more about CloudTrail, see the [AWS CloudTrail User Guide](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-user-guide.html).

### AWS FinOps Agent information in CloudTrail
<a name="service-name-info-in-cloudtrail"></a>

CloudTrail is enabled on your AWS account when you create the account. When activity occurs in AWS FinOps Agent, that activity is recorded in a CloudTrail event along with other AWS service events in **Event history**. You can view, search, and download recent events in your AWS account. For more information, see [Viewing events with CloudTrail Event history](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/view-cloudtrail-events.html).

For an ongoing record of events in your AWS account, including events for AWS FinOps Agent, create a trail. A *trail* enables CloudTrail to deliver log files to an Amazon S3 bucket. By default, when you create a trail in the console, the trail applies to all AWS Regions. The trail logs events from all Regions in the AWS partition and delivers the log files to the Amazon S3 bucket that you specify. For more information, see [Overview for creating a trail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-create-and-update-a-trail.html).

CloudTrail records the following AWS FinOps Agent API calls as management events:
+ Agent management (`CreateAgentSpace`, `UpdateAgentSpace`, `DeleteAgentSpace`).
+ Integration and connection management (`CreateIntegration`, `DeleteIntegration`, `CreateConnection`, `UpdateConnection`, `DeleteConnection`).
+ Document management (`CreateDocument`, `UpdateDocument`, `DeleteDocument`, `RestoreDocument`).
+ Artifact management (`ListArtifacts`, `GetArtifactContent`, `GetArtifactMetadata`).
+ Task and automation management (`CreateTask`, `CancelTask`, `CreateAutomation`, `UpdateAutomation`, `DeleteAutomation`).
+ Conversations (`CreateConversation`, `CreateTurn`, `CancelTurn`).
+ Agent request responses (`AcceptAgentRequest`, `RejectAgentRequest`).

### How caller identity appears in CloudTrail
<a name="cloudtrail-caller-identity"></a>

CloudTrail logs the identity of whoever made the API call:
+ **Administrator actions** (`CreateAgentSpace`, `CreateIntegration`, and so on) are logged under the administrator's own IAM identity.
+ **Web application actions** (`CreateConversation`, `CreateTask`, `CreateAutomation`, and so on) are logged under the assumed operator role session. The role is shared across web application users, but the calling user's IAM unique identifier is stamped on the session as `sourceIdentity`, so each event in CloudTrail can be attributed back to the individual user who initiated it. This requires the operator role's trust policy to grant `sts:SetSourceIdentity`; see [Trust policy](setting-up.md#setting-up-trust-policy).
+ **Calls the agent makes to other AWS services** (`ce:GetCostAndUsage`, `cloudtrail:LookupEvents`, and so on) are logged under the assumed agent role session. These appear as standard AWS API activity in CloudTrail and carry the same `sourceIdentity` attribution as web application actions.

To find every action a specific user initiated, filter CloudTrail events by `userIdentity.sessionContext.sourceIdentity` (the user's IAM unique identifier, beginning with `AIDA` for IAM users or `AROA` for assumed roles).

### What is not logged in CloudTrail
<a name="cloudtrail-not-logged"></a>

The agent's internal reasoning, tool calls, and conversation content are not logged to CloudTrail. These are recorded in the agent's internal journal system.

API calls the agent makes to other AWS services (such as Cost Explorer or CloudTrail `LookupEvents`) using the agent's IAM role are logged to CloudTrail under that IAM role's identity, as standard AWS API activity.