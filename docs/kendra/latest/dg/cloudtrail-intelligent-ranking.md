# Logging Amazon Kendra Intelligent

Ranking API calls with AWS CloudTrail logs

Amazon Kendra Intelligent Ranking is integrated with AWS CloudTrail, a service that provides
a record of actions taken by a user, role, or an AWS service in Amazon Kendra
Intelligent Ranking. CloudTrail captures all API calls from Amazon Kendra intelligent Ranking
as events, including code calls to the Amazon Kendra Intelligent Ranking APIs. If you
create a trail, you can activate continuous delivery of CloudTrail events to and Amazon S3 bucket,
including events for Amazon Kendra Intelligent Ranking. If you don't configure a trail,
you can still view the most recent events in the CloudTrail console in **Event
history**. Using the information collected by CloudTrail, you can determine the
request that was made to Amazon Kendra Intelligent Ranking, the IP address from which
the request was made, who made the request, when it was made, and additional
details.

To learn more about CloudTrail, including how to configure and activate it, see the [AWS CloudTrail User Guide](../../../awscloudtrail/latest/userguide/cloudtrail-user-guide.md "../../../awscloudtrail/latest/userguide/cloudtrail-user-guide.md").

## Amazon Kendra

Intelligent Ranking information in CloudTrail

CloudTrail is activated on your AWS account when you create the account. When activity
occurs in Amazon Kendra Intelligent Ranking, that activity is recorded in a CloudTrail
event along with other AWS service events in the CloudTrail **Event
history**. You can view, search, and download recent events in your
AWS account. For more information, see [Viewing Events with CloudTrail Event
History](../../../awscloudtrail/latest/userguide/view-cloudtrail-events.md "../../../awscloudtrail/latest/userguide/view-cloudtrail-events.md").

For an ongoing record of events in your AWS account, including events for
Amazon Kendra Intelligent Ranking, create a trail. A _trail_ is a configuration that allows CloudTrail to deliver events as log
files to a specified S3 bucket. By default, when you create a trail in the console,
the trail applies to all AWS Regions. The trail logs events from all Regions in
the AWS partition and delivers the log files to the S3 bucket that you specify.
Additionally, you can configure other AWS services to further analyze and act upon
the event data collected in CloudTrail logs. For more information, see:

- [Overview for Creating a Trail](../../../awscloudtrail/latest/userguide/cloudtrail-create-and-update-a-trail.md "../../../awscloudtrail/latest/userguide/cloudtrail-create-and-update-a-trail.md")
- [CloudTrail Supported Services and Integrations](../../../awscloudtrail/latest/userguide/cloudtrail-aws-service-specific-topics.md#cloudtrail-aws-service-specific-topics-integrations "../../../awscloudtrail/latest/userguide/cloudtrail-aws-service-specific-topics.md#cloudtrail-aws-service-specific-topics-integrations")
- [Configuring
  Amazon SNS Notifications for CloudTrail](../../../awscloudtrail/latest/userguide/getting_notifications_top_level.md "../../../awscloudtrail/latest/userguide/getting_notifications_top_level.md")
- [Receiving CloudTrail Log Files from Multiple Regions](../../../awscloudtrail/latest/userguide/receive-cloudtrail-log-files-from-multiple-regions.md "../../../awscloudtrail/latest/userguide/receive-cloudtrail-log-files-from-multiple-regions.md") and [Receiving CloudTrail Log Files from Multiple Accounts](../../../awscloudtrail/latest/userguide/cloudtrail-receive-logs-from-multiple-accounts.md "../../../awscloudtrail/latest/userguide/cloudtrail-receive-logs-from-multiple-accounts.md")

CloudTrail logs all Amazon Kendra Intelligent Ranking actions, which are documented in
the [API Reference](../APIReference/API_Reference.md "../APIReference/API_Reference.md"). For example, calls to the
`CreateRescoreExecutionPlan` generate entries in the CloudTrail log
files.

Every event or log entry contains information about who generated the request. For
more information, see the [CloudTrail
userIdentity Element](../../../awscloudtrail/latest/userguide/cloudtrail-event-reference-user-identity.md "../../../awscloudtrail/latest/userguide/cloudtrail-event-reference-user-identity.md").

## Example: Amazon Kendra

Intelligent Ranking log file entries

A _trail_ is a configuration that allows delivery
of events as log files to a specified S3 bucket. CloudTrail log files contain one or more
log entries. An _event_ represents a single request
from any source and includes information about the requested action, the date and
time of the action, request parameters, and so on. CloudTrail log files aren't an ordered
stack trace of the public API calls, so they don't appear in any specific order.

Calls to the `CreateRescoreExecutionPlan` operation creates the
following entry.

```
{
            "eventVersion": "1.08",
            "userIdentity": {
                "type": "`AssumedRole`",
                "principalId": "`principal ID`",
                "arn": "`ARN`",
                "accountId": "`account ID`",
                "accessKeyId": "`access key ID`",
                "sessionContext": {
                    "sessionIssuer": {
                        "type": "Role",
                        "principalId": "`principal ID`",
                        "arn": "`ARN`",
                        "accountId": "`account ID`",
                        "userName": "`user name`"
                    },
                    "webIdFederationData": {},
                    "attributes": {
                        "creationDate": "`yyyy-mm-ddThh:mm:ssZ`",
                        "mfaAuthenticated": "false"
                    }
                }
            },
            "eventTime": "`yyyy-mm-ddThh:mm:ssZ`",
            "eventSource": "kendra-ranking.amazonaws.com",
            "eventName": "`CreateRescoreExecutionPlan`",
            "awsRegion": "`region`",
            "sourceIPAddress": "`source IP address`",
            "userAgent": "`user agent`",
            "requestParameters": {
                "name": "`name`",
                "description": "`description`",
                "clientToken": "`client token`"
            },
            "responseElements": {
                "id": "`rescore execution plan ID`",
                "arn": "`rescore execution plan ARN`"
            },
            "requestID": "`request ID`",
            "eventID": "`event ID`",
            "readOnly": false,
            "eventType": "AwsApiCall",
            "managementEvent": true,
            "recipientAccountId": "`account ID`",
            "eventCategory": "`Management`",
            "tlsDetails": {
                "tlsVersion": "`TLS version`",
                "cipherSuite": "`cipher suite`",
                "clientProvidedHostHeader": "kendra-ranking.`[region]`.api.aws"
            }
        }
```
