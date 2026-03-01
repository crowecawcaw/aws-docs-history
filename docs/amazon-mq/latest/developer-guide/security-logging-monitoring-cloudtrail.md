# Logging Amazon MQ API calls using AWS CloudTrail

Amazon MQ is integrated with AWS CloudTrail, a service that provides a record of the Amazon MQ calls
that a user, role, or AWS service makes. CloudTrail captures API calls related to Amazon MQ
brokers and configurations as events, including calls from the Amazon MQ console and code
calls from Amazon MQ APIs. For more information about CloudTrail, see the _[AWS CloudTrail User Guide](../../../awscloudtrail/latest/userguide.md "../../../awscloudtrail/latest/userguide.md")_.

###### Note

CloudTrail doesn't log API calls related to ActiveMQ operations (for example, sending
and receiving messages) or to the ActiveMQ Web Console. To log information related
to ActiveMQ operations, you can [configure Amazon MQ to publish
general and audit logs to Amazon CloudWatch Logs](security-logging-monitoring.md "security-logging-monitoring.md").

Using the information that CloudTrail collects, you can identify a specific request to an
Amazon MQ API, the IP address of the requester, the requester's identity, the date and time
of the request, and so on. If you configure a _trail_, you can enable
continuous delivery of CloudTrail events to an Amazon S3 bucket. If you don't configure a trail,
you can view the most recent events in the event history in the CloudTrail console. For more
information, see [Overview for Creating a Trail](../../../awscloudtrail/latest/userguide/cloudtrail-create-and-update-a-trail.md "../../../awscloudtrail/latest/userguide/cloudtrail-create-and-update-a-trail.md") in the _[AWS CloudTrail User Guide](../../../awscloudtrail/latest/userguide.md "../../../awscloudtrail/latest/userguide.md")_.

## Amazon MQ Information in CloudTrail

When you create your AWS account, CloudTrail is enabled. When a supported Amazon MQ event
activity occurs, it is recorded in a CloudTrail event with other AWS service events in
the event history. You can view, search, and download recent events for your AWS
account. For more information, see [Viewing Events with CloudTrail Event
History](../../../awscloudtrail/latest/userguide/view-cloudtrail-events.md "../../../awscloudtrail/latest/userguide/view-cloudtrail-events.md") in the _AWS CloudTrail User Guide_.

A trail allows CloudTrail to deliver log files to an Amazon S3 bucket. You can create a trail
to keep an ongoing record of events in your AWS account. By default, when you
create a trail using the AWS Management Console, the trail applies to all AWS Regions. The trail
logs events from all AWS Regions and delivers log files to the specified Amazon S3
bucket. You can also configure other AWS services to further analyze and act on
the event data collected in CloudTrail logs. For more information, see the following
topics in the _AWS CloudTrail User Guide_:

- [CloudTrail Supported Services and Integrations](../../../awscloudtrail/latest/userguide/cloudtrail-aws-service-specific-topics.md#cloudtrail-aws-service-specific-topics-integrations "../../../awscloudtrail/latest/userguide/cloudtrail-aws-service-specific-topics.md#cloudtrail-aws-service-specific-topics-integrations")
- [Configuring
  Amazon SNS Notifications for CloudTrail](../../../awscloudtrail/latest/userguide/getting_notifications_top_level.md "../../../awscloudtrail/latest/userguide/getting_notifications_top_level.md")
- [Receiving CloudTrail Log Files from Multiple Regions](../../../awscloudtrail/latest/userguide/receive-cloudtrail-log-files-from-multiple-regions.md "../../../awscloudtrail/latest/userguide/receive-cloudtrail-log-files-from-multiple-regions.md")
- [Receiving CloudTrail Log Files from Multiple Accounts](../../../awscloudtrail/latest/userguide/cloudtrail-receive-logs-from-multiple-accounts.md "../../../awscloudtrail/latest/userguide/cloudtrail-receive-logs-from-multiple-accounts.md")

Amazon MQ supports logging both the request parameters and the responses for the
following APIs as events in CloudTrail log files:

- [`CreateConfiguration`](../api-reference/rest-api-configurations.md#rest-api-configurations-methods-post "../api-reference/rest-api-configurations.md#rest-api-configurations-methods-post")
- [`DeleteBroker`](../api-reference/rest-api-broker.md#rest-api-broker-methods-delete "../api-reference/rest-api-broker.md#rest-api-broker-methods-delete")
- [`DeleteUser`](../api-reference/rest-api-user.md#rest-api-user-methods-delete "../api-reference/rest-api-user.md#rest-api-user-methods-delete")
- [`RebootBroker`](../api-reference/rest-api-broker-reboot.md#rest-api-broker-reboot-methods-post "../api-reference/rest-api-broker-reboot.md#rest-api-broker-reboot-methods-post")
- [`UpdateBroker`](../api-reference/rest-api-broker.md#rest-api-broker-methods-put "../api-reference/rest-api-broker.md#rest-api-broker-methods-put")

###### Note

RebootBroker log files are logged when you reboot the broker.
During the maintenance window, the service automatically reboots, and RebootBroker log files are not logged.

###### Important

For the `GET` methods of the following APIs, the request parameters
are logged, but the responses are redacted:

- [`DescribeBroker`](../api-reference/rest-api-broker.md#rest-api-broker-methods-get "../api-reference/rest-api-broker.md#rest-api-broker-methods-get")
- [`DescribeConfiguration`](../api-reference/rest-api-configuration.md#rest-api-configuration-methods-get "../api-reference/rest-api-configuration.md#rest-api-configuration-methods-get")
- [`DescribeConfigurationRevision`](../api-reference/rest-api-configuration-revision.md#rest-api-configuration-revision-methods-get "../api-reference/rest-api-configuration-revision.md#rest-api-configuration-revision-methods-get")
- [`DescribeUser`](../api-reference/rest-api-user.md#rest-api-user-methods-get "../api-reference/rest-api-user.md#rest-api-user-methods-get")
- [`ListBrokers`](../api-reference/rest-api-brokers.md#rest-api-brokers-methods-get "../api-reference/rest-api-brokers.md#rest-api-brokers-methods-get")
- [`ListConfigurationRevisions`](../api-reference/rest-api-configuration-revisions.md#rest-api-configuration-revisions-methods-get "../api-reference/rest-api-configuration-revisions.md#rest-api-configuration-revisions-methods-get")
- [`ListConfigurations`](../api-reference/rest-api-configurations.md#rest-api-configurations-methods-get "../api-reference/rest-api-configurations.md#rest-api-configurations-methods-get")
- [`ListUsers`](../api-reference/rest-api-users.md#rest-api-users-methods-get "../api-reference/rest-api-users.md#rest-api-users-methods-get")
  For the following APIs, the `data` and `password`
  request parameters are hidden by asterisks (`***`):

- [`CreateBroker`](../api-reference/rest-api-brokers.md#rest-api-brokers-methods-post "../api-reference/rest-api-brokers.md#rest-api-brokers-methods-post") (`POST`)
- [`CreateUser`](../api-reference/rest-api-user.md#rest-api-user-methods-post "../api-reference/rest-api-user.md#rest-api-user-methods-post") (`POST`)
- [`UpdateConfiguration`](../api-reference/rest-api-configuration.md#rest-api-configuration-methods-put "../api-reference/rest-api-configuration.md#rest-api-configuration-methods-put")
  (`PUT`)
- [`UpdateUser`](../api-reference/rest-api-user.md#rest-api-user-methods-put "../api-reference/rest-api-user.md#rest-api-user-methods-put") (`PUT`)

Every event or log entry contains information about the requester. This
information helps you determine the following:

- Was the request made with root or user credentials?
- Was the request made with temporary security credentials for a role or a
  federated user?
- Was the request made by another AWS service?

For more information, see [CloudTrail
userIdentity Element](../../../awscloudtrail/latest/userguide/cloudtrail-event-reference-user-identity.md "../../../awscloudtrail/latest/userguide/cloudtrail-event-reference-user-identity.md") in the _AWS CloudTrail User Guide_.

## Example Amazon MQ Log File Entry

A _trail_ is a configuration that allows the delivery of events
as log files to the specified Amazon S3 bucket. CloudTrail log files contain one or more log
entries.

An _event_ represents a single request from any source and
includes information about the request to an Amazon MQ API, the IP address of the
requester, the requester's identity, the date and time of the request, and so
on.

The following example shows a CloudTrail log entry for a [`CreateBroker`](../api-reference/rest-api-brokers.md#rest-api-brokers-methods-post "../api-reference/rest-api-brokers.md#rest-api-brokers-methods-post") API call.

###### Note

Because CloudTrail log files aren't an ordered stack trace of public APIs, they
don't list information in any specific order.

```
{
    "eventVersion": "1.06",
    "userIdentity": {
        "type": "IAMUser",
        "principalId": "AKIAIOSFODNN7EXAMPLE",
        "arn": "arn:aws:iam::111122223333:user/AmazonMqConsole",
        "accountId": "111122223333",
        "accessKeyId": "AKIAI44QH8DHBEXAMPLE",
        "userName": "AmazonMqConsole"
    },
    "eventTime": "2018-06-28T22:23:46Z",
    "eventSource": "amazonmq.amazonaws.com",
    "eventName": "CreateBroker",
    "awsRegion": "us-west-2",
    "sourceIPAddress": "203.0.113.0",
    "userAgent": "PostmanRuntime/7.1.5",
    "requestParameters": {
        "engineVersion": "5.15.9",
        "deploymentMode": "ACTIVE_STANDBY_MULTI_AZ",
        "maintenanceWindowStartTime": {
            "dayOfWeek": "THURSDAY",
            "timeOfDay": "22:45",
            "timeZone": "America/Los_Angeles"
        },
        "engineType": "ActiveMQ",
        "hostInstanceType": "mq.m5.large",
        "users": [
            {
                "username": "MyUsername123",
                "password": "***",
                "consoleAccess": true,
                "groups": [
                    "admins",
                    "support"
                ]
            },
            {
                "username": "MyUsername456",
                "password": "***",
                "groups": [
                    "admins"
                ]
            }
        ],
        "creatorRequestId": "1",
        "publiclyAccessible": true,
        "securityGroups": [
            "sg-a1b234cd"
        ],
        "brokerName": "MyBroker",
        "autoMinorVersionUpgrade": false,
        "subnetIds": [
            "subnet-12a3b45c",
            "subnet-67d8e90f"
        ]
    },
    "responseElements": {
        "brokerId": "b-1234a5b6-78cd-901e-2fgh-3i45j6k178l9",
        "brokerArn": "arn:aws:mq:us-east-2:123456789012:broker:MyBroker:b-1234a5b6-78cd-901e-2fgh-3i45j6k178l9"
    },
    "requestID": "a1b2c345-6d78-90e1-f2g3-4hi56jk7l890",
    "eventID": "a12bcd3e-fg45-67h8-ij90-12k34d5l16mn",
    "readOnly": false,
    "eventType": "AwsApiCall",
    "recipientAccountId": "111122223333"
}
```
