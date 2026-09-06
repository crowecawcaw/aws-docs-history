

# Logging and monitoring in Amazon Connect Health
<a name="logging-using-cloudtrail"></a>

Monitoring is an important part of maintaining the reliability, availability, and performance of Amazon Connect Health and your other AWS solutions. AWS provides the following monitoring tools to watch Amazon Connect Health, report when something is wrong, and take automatic actions when appropriate.

## AWS CloudTrail
<a name="cloudtrail-integration"></a>

Amazon Connect Health is integrated with AWS CloudTrail, a service that provides a record of actions taken by a user, role, or an AWS service in Amazon Connect Health. CloudTrail captures all API calls for Amazon Connect Health as events. The calls captured include calls from the Amazon Connect Health console and code calls to the Amazon Connect Health API operations.

If you create a trail, you can enable continuous delivery of CloudTrail events to an Amazon S3 bucket, including events for Amazon Connect Health. If you don’t configure a trail, you can still view the most recent events in the CloudTrail console in **Event history**. Using the information collected by CloudTrail, you can determine the request that was made to Amazon Connect Health, the IP address from which the request was made, who made the request, when it was made, and additional details.

For more information about CloudTrail, see the [AWS CloudTrail User Guide](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/).

The event source for Amazon Connect Health is `health-agent.amazonaws.com`.

### Management events
<a name="cloudtrail-management-events"></a>

All Amazon Connect Health control plane API calls are logged as management events by default. You don’t need to configure anything to receive management events.

### Data events
<a name="cloudtrail-data-events"></a>

Amazon Connect Health logs data plane API calls as data events. Data events are not logged by default. To log data events, you must create a trail or event data store and configure it to log data events. For more information about configuring data events, see [Logging data events](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/logging-data-events-with-cloudtrail.html) in the *AWS CloudTrail User Guide*.

## Understanding Amazon Connect Health log file entries
<a name="cloudtrail-example"></a>

CloudTrail log files contain one or more log entries. An event represents a single request from any source and includes information about the requested action, the date and time of the action, request parameters, and so on.

The following example shows a CloudTrail log entry that demonstrates the `CreateSubscription` action.

```
{
  "eventVersion": "1.09",
  "userIdentity": {
    "type": "AssumedRole",
    "principalId": "AROA123456789EXAMPLE:session-name",
    "arn": "arn:aws:sts::123456789012:assumed-role/ExampleRole/session-name",
    "accountId": "123456789012"
  },
  "eventTime": "2026-03-12T19:54:27Z",
  "eventSource": "health-agent.amazonaws.com",
  "eventName": "CreateSubscription",
  "awsRegion": "us-west-2",
  "sourceIPAddress": "192.0.2.1",
  "userAgent": "aws-cli/2.18.6",
  "requestParameters": {
    "domainId": "dom-EXAMPLE1234567890"
  },
  "responseElements": {
    "subscriptionId": "sub-EXAMPLE1234567890",
    "domainId": "dom-EXAMPLE1234567890",
    "status": "ACTIVE"
  },
  "requestID": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
  "eventID": "a1b2c3d4-5678-90ab-cdef-EXAMPLE22222",
  "readOnly": false,
  "resources": [
    {
      "accountId": "123456789012",
      "type": "AWS::HealthAgent::Subscription",
      "ARN": "arn:aws:health-agent:us-west-2:123456789012:domain/dom-EXAMPLE1234567890/subscription/*"
    }
  ],
  "eventType": "AwsApiCall",
  "managementEvent": true,
  "recipientAccountId": "123456789012",
  "eventCategory": "Management"
}
```