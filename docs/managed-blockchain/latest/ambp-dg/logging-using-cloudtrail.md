Amazon Managed Blockchain (AMB) Access Polygon is in preview release and is subject to change.

# Logging Amazon Managed Blockchain (AMB) Access Polygon events by using

AWS CloudTrail

###### Note

Amazon Managed Blockchain (AMB) Access Polygon doesn’t support management events.

Amazon Managed Blockchain runs on AWS CloudTrail, a service that provides a record of actions taken by a user,
role, or an AWS service in Managed Blockchain. CloudTrail captures who invoked the AMB Access Polygon endpoints for Managed Blockchain
as data plane events.

If you create a properly configured trail that is subscribed
to receive the desired
data plane events, you can receive continuous delivery of AMB Access Polygon related CloudTrail events to an S3
bucket. Using the information that's collected by CloudTrail, you can determine that a request was
made to one of the AMB Access Polygon endpoints, the IP address that the request came from, who made the
request, when it was made, and other additional details.

To learn more about CloudTrail, see the [AWS CloudTrail User Guide](../../../awscloudtrail/latest/userguide/cloudtrail-user-guide.md "../../../awscloudtrail/latest/userguide/cloudtrail-user-guide.md").

## AMB Access Polygon information in CloudTrail

CloudTrail is enabled on your AWS account when you create it. However, you must configure the
data plane events to view who invoked the AMB Access Polygon endpoints.

For an ongoing record of events in your AWS account, including events for AMB Access Polygon,
create a trail. A _trail_ enables CloudTrail to deliver log files to an S3
bucket. By default, when you create a trail in the console, the trail applies to all
AWS Regions. The trail logs events from all supported Regions in the AWS partition and
delivers the log files to the S3 bucket that you specify. Additionally, you can configure
other AWS services to analyze further and act on the event data collected in CloudTrail logs. For
more information, see the following:

- [Using CloudTrail to track Polygon JSON-RPCs](#polygon-logging "#polygon-logging")
- [Overview for creating a trail](../../../awscloudtrail/latest/userguide/cloudtrail-create-and-update-a-trail.md "../../../awscloudtrail/latest/userguide/cloudtrail-create-and-update-a-trail.md")
- [CloudTrail supported services and integrations](../../../awscloudtrail/latest/userguide/cloudtrail-aws-service-specific-topics.md "../../../awscloudtrail/latest/userguide/cloudtrail-aws-service-specific-topics.md")
- [Configuring Amazon SNS notifications for CloudTrail](../../../awscloudtrail/latest/userguide/configure-sns-notifications-for-cloudtrail.md "../../../awscloudtrail/latest/userguide/configure-sns-notifications-for-cloudtrail.md")
- [Receiving CloudTrail log files from multiple Regions](../../../awscloudtrail/latest/userguide/receive-cloudtrail-log-files-from-multiple-regions.md "../../../awscloudtrail/latest/userguide/receive-cloudtrail-log-files-from-multiple-regions.md") and [Receiving CloudTrail log files from multiple accounts](../../../awscloudtrail/latest/userguide/cloudtrail-receive-logs-from-multiple-accounts.md "../../../awscloudtrail/latest/userguide/cloudtrail-receive-logs-from-multiple-accounts.md")

By analyzing the CloudTrail data events, you can monitor who invoked the AMB Access Polygon
endpoints.

Every event or log entry contains information about who generated
the request. The identity information helps you determine the following:

- Whether the request was made with root or AWS Identity and Access Management (IAM) user credentials
- Whether the request was made with temporary security credentials for a role or a
  federated user
- Whether the request was made by another AWS service

For more information, see the [CloudTrail userIdentity
element](../../../awscloudtrail/latest/userguide/cloudtrail-event-reference-user-identity.md "../../../awscloudtrail/latest/userguide/cloudtrail-event-reference-user-identity.md").

## Understanding

AMB Access Polygon log file entries

For data plane events, a trail is a configuration that enables delivery of events as log
files to a specified S3 bucket. Each CloudTrail log file contains one or more log entries that
represent a single request from any source. These entries provide details about the requested
action, including the date and time of the action, and any associated request parameters.

###### Note

CloudTrail data events in the log files aren't an ordered stack trace of the
AMB Access Polygon API calls, so they don't appear in any specific order.

### Using CloudTrail to track Polygon JSON-RPCs

You can use CloudTrail to track who in your account invoked the AMB Access Polygon endpoints and which
JSON-RPC was invoked as _data events_. By default, when you create a
trail, data events aren't logged. To record who invoked the AMB Access Polygon endpoints as CloudTrail data
events, you must explicitly add the supported resources or resource types for which you want
to collect activity to a trail. AMB Access Polygon supports adding data events by using the
AWS Management Console, AWS CLI, and SDK. For more information, see [Log events by using advanced selectors](../../../awscloudtrail/latest/userguide/logging-data-events-with-cloudtrail.md#creating-data-event-selectors-advanced "../../../awscloudtrail/latest/userguide/logging-data-events-with-cloudtrail.md#creating-data-event-selectors-advanced") in the _AWS CloudTrail User Guide_ .

To log data events in a trail, use the [put-event-selectors](../../../cli/latest/reference/cloudtrail/put-event-selectors.md "../../../cli/latest/reference/cloudtrail/put-event-selectors.md")
operation after you create the trail. Use the `--advanced-event-selectors` option
to specify the `AWS::ManagedBlockchain::Network` resource types in order to start
logging data events to determine who invoked the AMB Access Polygon endpoints.

###### Example Data event log entry of all your account's AMB Access Polygon endpoints requests

The following example demonstrates how to use the `put-event-selectors`
operation to log all your account's AMB Access Polygon endpoint requests for the trail `my-polygon-trail` in the
`us-east-1` Region.

```
aws cloudtrail put-event-selectors \
--region `us-east-1` \
--trail-name `my-polygon-trail`  \
--advanced-event-selectors '[{
    "Name": "`Test`",
    "FieldSelectors": [
      { "Field": "eventCategory", "Equals": ["Data"] },
      { "Field": "resources.type", "Equals": ["AWS::ManagedBlockchain::Network"] } ]}]'
```

After you subscribe, you can track usage in the S3 bucket that is connected to the
trail specified in the previous example.

The following result shows a CloudTrail data event log entry of the information that's
collected by CloudTrail. You can determine that a Polygon JSON-RPC request was made to one of
the AMB Access Polygon endpoints, the IP address that the request came from, who made the request,
when it was made, and other additional details. Some values in the following example have
been obfuscated for security reasons but appear fully in actual log entries.

```
{
        "eventVersion": "1.09",
        "userIdentity": {
            "type": "AssumedRole",
            "principalId": "AROA554UO62RJ7KSB7FAX:777777777777",
            "arn": "arn:aws:sts::111122223333:assumed-role/Admin/777777777777",
            "accountId": "111122223333"
        },
        "eventTime": "2023-04-12T19:00:22Z",
        "eventSource": "managedblockchain.amazonaws.com",
        "eventName": "gettxout",
        "awsRegion": "`us-east-1`",
        "sourceIPAddress": "111.222.333.444",
        "userAgent": "python-requests/2.28.1",
        "errorCode": "-",
        "errorMessage": "-",
        "requestParameters": {
            "jsonrpc": "2.0",
            "method": "gettxout",
            "params": [],
            "id": 1
        },
        "responseElements": null,
        "requestID": "DRznHHEj********",
        "eventID": "baeb232d-2c6b-46cd-992c-0e40********",
        "readOnly": true,
        "resources": [{
            "type": "AWS::ManagedBlockchain::Network",
            "ARN": "arn:aws:managedblockchain:::networks/n-polygon-mainnet"
        }],
        "eventType": "AwsApiCall",
        "managementEvent": false,
        "recipientAccountId": "111122223333",
        "eventCategory": "Data"
}
```
