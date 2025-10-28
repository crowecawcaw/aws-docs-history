End of support notice: On September 15, 2025, AWS
will discontinue support for Amazon Lex V1. After September 15, 2025, you will
no longer be able to access the Amazon Lex V1 console or Amazon Lex V1 resources. If you are using Amazon Lex V2, refer to the [Amazon Lex V2 guide](../../../lexv2/latest/dg/what-is.md "../../../lexv2/latest/dg/what-is.md") instead.
.

# Monitoring Amazon Lex API

Calls with AWS CloudTrail Logs

Amazon Lex is integrated with AWS CloudTrail, a service that provides
a record of actions taken by a user, role, or an AWS service in
Amazon Lex. CloudTrail captures a subset of API calls for Amazon Lex
as events, including calls from the Amazon Lex console and from
code calls to the Amazon Lex APIs. If you create a trail, you can
enable continuous delivery of CloudTrail events to an Amazon S3 bucket,
including events for Amazon Lex. If you don't configure a trail,
you can still view the most recent events in the CloudTrail console in
**Event history**. Using the information
collected by CloudTrail, you can determine the request that was made to
Amazon Lex, the IP address from which the request was made, who
made the request, when it was made, and additional details.

To learn more about CloudTrail, including how to configure and enable
it, see the [AWS CloudTrail User Guide](../../../awscloudtrail/latest/userguide.md "../../../awscloudtrail/latest/userguide.md").

## Amazon Lex

Information in CloudTrail

CloudTrail is enabled on your AWS account when you create the
account. When supported event activity occurs in Amazon Lex,
that activity is recorded in a CloudTrail event along with other AWS
service events in **Event history**. You can
view, search, and download recent events in your AWS account.
For more information, see [Viewing
Events with CloudTrail Event History](../../../awscloudtrail/latest/userguide/view-cloudtrail-events.md "../../../awscloudtrail/latest/userguide/view-cloudtrail-events.md").

For an ongoing record of events in your AWS account,
including events for Amazon Lex, create a trail. A trail
enables CloudTrail to deliver log files to an Amazon Simple Storage Service (Amazon S3) bucket.
By default, when you create a trail in the console, the trail
applies to all AWS Regions. The trail logs events from all
Regions in the AWS partition and delivers the log files to the
S3 bucket that you specify. Additionally, you can configure
other AWS services to further analyze and act upon the event
data collected in CloudTrail logs. For more information, see:

- [Overview for Creating a Trail](../../../awscloudtrail/latest/userguide/cloudtrail-create-and-update-a-trail.md "../../../awscloudtrail/latest/userguide/cloudtrail-create-and-update-a-trail.md")
- [CloudTrail Supported Services and
  Integrations](../../../awscloudtrail/latest/userguide/cloudtrail-aws-service-specific-topics.md#cloudtrail-aws-service-specific-topics-integrations "../../../awscloudtrail/latest/userguide/cloudtrail-aws-service-specific-topics.md#cloudtrail-aws-service-specific-topics-integrations")
- [Configuring Amazon SNS Notifications for
  CloudTrail](../../../awscloudtrail/latest/userguide/getting_notifications_top_level.md "../../../awscloudtrail/latest/userguide/getting_notifications_top_level.md")
- [Receiving CloudTrail Log Files from Multiple
  Regions](../../../awscloudtrail/latest/userguide/receive-cloudtrail-log-files-from-multiple-regions.md "../../../awscloudtrail/latest/userguide/receive-cloudtrail-log-files-from-multiple-regions.md") and [Receiving CloudTrail Log Files from Multiple
  Accounts](../../../awscloudtrail/latest/userguide/cloudtrail-receive-logs-from-multiple-accounts.md "../../../awscloudtrail/latest/userguide/cloudtrail-receive-logs-from-multiple-accounts.md")

Amazon Lex supports logging the following operations as
events in CloudTrail log files:

- [CreateBotVersion](API_CreateBotVersion.md "API_CreateBotVersion.md")
- [CreateIntentVersion](API_CreateIntentVersion.md "API_CreateIntentVersion.md")
- [CreateSlotTypeVersion](API_CreateSlotTypeVersion.md "API_CreateSlotTypeVersion.md")
- [DeleteBot](API_DeleteBot.md "API_DeleteBot.md")
- [DeleteBotAlias](API_DeleteBotAlias.md "API_DeleteBotAlias.md")
- [DeleteBotChannelAssociation](API_DeleteBotChannelAssociation.md "API_DeleteBotChannelAssociation.md")
- [DeleteBotVersion](API_DeleteBotVersion.md "API_DeleteBotVersion.md")
- [DeleteIntent](API_DeleteIntent.md "API_DeleteIntent.md")
- [DeleteIntentVersion](API_DeleteIntentVersion.md "API_DeleteIntentVersion.md")
- [DeleteSlotType](API_DeleteSlotType.md "API_DeleteSlotType.md")
- [DeleteSlotTypeVersion](API_DeleteSlotTypeVersion.md "API_DeleteSlotTypeVersion.md")
- [DeleteUtterances](API_DeleteUtterances.md "API_DeleteUtterances.md")
- [GetBot](API_GetBot.md "API_GetBot.md")
- [GetBotAlias](API_GetBotAlias.md "API_GetBotAlias.md")
- [GetBotAliases](API_GetBotAliases.md "API_GetBotAliases.md")
- [GetBotChannelAssociation](API_GetBotChannelAssociation.md "API_GetBotChannelAssociation.md")
- [GetBotChannelAssociations](API_GetBotChannelAssociations.md "API_GetBotChannelAssociations.md")
- [GetBots](API_GetBots.md "API_GetBots.md")
- [GetBotVersions](API_GetBotVersions.md "API_GetBotVersions.md")
- [GetBuiltinIntent](API_GetBuiltinIntent.md "API_GetBuiltinIntent.md")
- [GetBuiltinIntents](API_GetBuiltinIntents.md "API_GetBuiltinIntents.md")
- [GetBuiltinSlotTypes](API_GetBuiltinSlotTypes.md "API_GetBuiltinSlotTypes.md")
- [GetSlotTypeVersions](API_GetSlotTypeVersions.md "API_GetSlotTypeVersions.md")
- [GetUtterancesView](API_GetUtterancesView.md "API_GetUtterancesView.md")
- [PutBot](API_PutBot.md "API_PutBot.md")
- [PutBotAlias](API_PutBotAlias.md "API_PutBotAlias.md")
- [PutIntent](API_PutIntent.md "API_PutIntent.md")
- [PutSlotType](API_PutSlotType.md "API_PutSlotType.md")

Every event or log entry contains information about who
generated the request. This information helps you determine the
following:

- Whether the request was made with root or user
  credentials
- Whether the request was made with temporary security
  credentials for a role or federated user
- Whether the request was made by another AWS
  service

For more information, see the [CloudTrail userIdentity Element](../../../awscloudtrail/latest/userguide/cloudtrail-event-reference-user-identity.md "../../../awscloudtrail/latest/userguide/cloudtrail-event-reference-user-identity.md").

For information about the Amazon Lex actions that are logged in
CloudTrail logs, see [Amazon Lex Model Building Service](API_Operations_Amazon_Lex_Model_Building_Service.md "API_Operations_Amazon_Lex_Model_Building_Service.md"). For example,
calls to the [PutBot](API_PutBot.md "API_PutBot.md"), [GetBot](API_GetBot.md "API_GetBot.md"), and [DeleteBot](API_DeleteBot.md "API_DeleteBot.md")
operations generate entries in the CloudTrail log. The actions
documented in [Amazon Lex Runtime Service](API_Operations_Amazon_Lex_Runtime_Service.md "API_Operations_Amazon_Lex_Runtime_Service.md"), [PostContent](API_runtime_PostContent.md "API_runtime_PostContent.md") and [PostText](API_runtime_PostText.md "API_runtime_PostText.md"), are not logged.

## Example: Amazon Lex

Log File Entries

A trail is a configuration that enables delivery of events as
log files to an S3 bucket that you specify. CloudTrail log files
contain one or more log entries. An event represents a single
request from any source and includes information about the
requested action, the date and time of the action, request
parameters, and so on. CloudTrail log files are not an ordered stack
trace of the public API calls, so they do not appear in any
specific order.

The following example CloudTrail log entry shows the result of a
call to the `PutBot` operation.
