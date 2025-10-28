# Logging Amazon Kendra API calls with AWS CloudTrail logs

Amazon Kendra is integrated with AWS CloudTrail, a service that provides a record of actions
taken by a user, role, or an AWS service in Amazon Kendra. CloudTrail captures all API calls
from Amazon Kendra as events, including calls from the Amazon Kendra console and from
code calls to the Amazon Kendra APIs. If you create a trail, you can activate continuous
delivery of CloudTrail events to and Amazon S3 bucket, including events for Amazon Kendra. If you
don't configure a trail, you can still view the most recent events in the CloudTrail console
in **Event history**. Using the information collected by CloudTrail, you can
determine the request that was made to Amazon Kendra, the IP address from which the
request was made, who made the request, when it was made, and additional details.

To learn more about CloudTrail, including how to configure and activate it, see the [AWS CloudTrail User Guide](../../../awscloudtrail/latest/userguide/cloudtrail-user-guide.md "../../../awscloudtrail/latest/userguide/cloudtrail-user-guide.md").

## Amazon Kendra information in

CloudTrail

CloudTrail is activated on your AWS account when you create the account. When activity
occurs in Amazon Kendra, that activity is recorded in a CloudTrail event along with other
AWS service events in the CloudTrail **Event history**. You can view,
search, and download recent events in your AWS account. For more information, see
[Viewing Events with CloudTrail
Event History](../../../awscloudtrail/latest/userguide/view-cloudtrail-events.md "../../../awscloudtrail/latest/userguide/view-cloudtrail-events.md").

For an ongoing record of events in your AWS account, including events for
Amazon Kendra, create a trail. A _trail_ is a
configuration that allows CloudTrail to deliver events as log files to a specified S3
bucket. By default, when you create a trail in the console, the trail applies to all
AWS Regions. The trail logs events from all Regions in the AWS partition and
delivers the log files to the S3 bucket that you specify. Additionally, you can
configure other AWS services to further analyze and act upon the event data
collected in CloudTrail logs. For more information, see:

- [Overview for Creating a Trail](../../../awscloudtrail/latest/userguide/cloudtrail-create-and-update-a-trail.md "../../../awscloudtrail/latest/userguide/cloudtrail-create-and-update-a-trail.md")
- [CloudTrail Supported Services and Integrations](../../../awscloudtrail/latest/userguide/cloudtrail-aws-service-specific-topics.md#cloudtrail-aws-service-specific-topics-integrations "../../../awscloudtrail/latest/userguide/cloudtrail-aws-service-specific-topics.md#cloudtrail-aws-service-specific-topics-integrations")
- [Configuring
  Amazon SNS Notifications for CloudTrail](../../../awscloudtrail/latest/userguide/getting_notifications_top_level.md "../../../awscloudtrail/latest/userguide/getting_notifications_top_level.md")
- [Receiving CloudTrail Log Files from Multiple Regions](../../../awscloudtrail/latest/userguide/receive-cloudtrail-log-files-from-multiple-regions.md "../../../awscloudtrail/latest/userguide/receive-cloudtrail-log-files-from-multiple-regions.md") and [Receiving CloudTrail Log Files from Multiple Accounts](../../../awscloudtrail/latest/userguide/cloudtrail-receive-logs-from-multiple-accounts.md "../../../awscloudtrail/latest/userguide/cloudtrail-receive-logs-from-multiple-accounts.md")

CloudTrail logs all Amazon Kendra actions, which are documented in the [API
Reference](../APIReference/API_Reference.md "../APIReference/API_Reference.md"). For example, calls to the `CreateIndex`,
`CreateDataSource`, and `Query` operations generate
entries in the CloudTrail log files.

Every event or log entry contains information about who generated the request. For
more information, see the [CloudTrail
userIdentity Element](../../../awscloudtrail/latest/userguide/cloudtrail-event-reference-user-identity.md "../../../awscloudtrail/latest/userguide/cloudtrail-event-reference-user-identity.md").

## Example: Amazon Kendra log file

entries

A _trail_ is a configuration that allows delivery
of events as log files to a specified S3 bucket. CloudTrail log files contain one or more
log entries. An _event_ represents a single request
from any source and includes information about the requested action, the date and
time of the action, request parameters, and so on. CloudTrail log files aren't an ordered
stack trace of the public API calls, so they don't appear in any specific order.

Calls to the `Query` operation creates the following entry.

```
        {
            "eventVersion": "1.05",
            "userIdentity": {
                "type": "`AssumedRole | FederatedUser | IAMUser | Root | SAMLUser | WebIdentityUser`",
                "principalId": "`principal ID`",
                "arn": "`ARN`",
                "accountId": "`account ID`",
                "accessKeyId": "`access key ID`",
                "sessionContext": {
                    "sessionIssuer": {
                        "type": "Role",
                        "principalId": "`principal Id`",
                        "arn": "`ARN`",
                        "accountId": "`account ID`",
                        "userName": "`user name`"
                    },
                    "webIdFederationData": {

                    },
                    "attributes": {
                        "mfaAuthenticated": false,
                        "creationDate": "`timestamp`"
                    }
                }
            },
            "eventTime": "`timestamp`",
            "eventSource": "kendra.amazonaws.com",
            "eventName": "Query",
            "awsRegion": "`region`",
            "sourceIPAddress": "`source IP address`",
            "userAgent": "`user agent`",
            "requestParameters": {
                "indexId": "`index ID`"
            },
            "responseElements": null,
            "requestID": "`request ID`",
            "eventID": "`event ID`",
            "eventType": "AwsApiCall",
            "recipientAccountId": "`account ID`"
        },

```
