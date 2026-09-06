

# Logging AWS Interconnect API calls using AWS CloudTrail
<a name="logging-using-cloudtrail"></a>

AWS Interconnect is integrated with AWS CloudTrail, a service that provides a record of actions taken by a user, role, or an AWS service in AWS Interconnect. CloudTrail captures all API calls for AWS Interconnect as events. The calls captured include calls from the AWS Interconnect console and code calls to the AWS Interconnect API operations. If you create a trail, you can enable continuous delivery of CloudTrail events to an Amazon S3 bucket, including events for AWS Interconnect. If you don’t configure a trail, you can still view the most recent events in the CloudTrail console in **Event history**. Using the information collected by CloudTrail, you can determine the request that was made to AWS Interconnect, the IP address from which the request was made, who made the request, when it was made, and additional details.

To learn more about CloudTrail, see the [AWS CloudTrail User Guide](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/).

## AWS Interconnect information in CloudTrail
<a name="service-name-info-in-cloudtrail"></a>

CloudTrail is enabled on your AWS account when you create the account. When activity occurs in AWS Interconnect, that activity is recorded in a CloudTrail event along with other AWS service events in **Event history**. You can view, search, and download recent events in your AWS account. For more information, see [Viewing Events with CloudTrail Event History](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/view-cloudtrail-events.html).

For an ongoing record of events in your AWS account, including events for AWS Interconnect, create a trail. A *trail* enables CloudTrail to deliver log files to an Amazon S3 bucket. By default, when you create a trail in the console, the trail applies to all AWS Regions. The trail logs events from all Regions in the AWS partition and delivers the log files to the Amazon S3 bucket that you specify. Additionally, you can configure other AWS services to further analyze and act upon the event data collected in CloudTrail logs. For more information, see the following:
+  [Overview for creating a trail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-create-and-update-a-trail.html) 
+  [CloudTrail supported services and integrations](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-aws-service-specific-topics.html#cloudtrail-aws-service-specific-topics-integrations) 
+  [Configuring Amazon SNS notifications for CloudTrail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/getting_notifications_top_level.html) 
+  [Receiving CloudTrail log files from multiple Regions](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/receive-cloudtrail-log-files-from-multiple-regions.html) 
+  [Receiving CloudTrail log files from multiple accounts](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-receive-logs-from-multiple-accounts.html) 

All AWS Interconnect actions are logged by CloudTrail and are documented in the [AWS Interconnect API Reference](https://docs.aws.amazon.com/interconnect/latest/api/). For example, calls to the `CreateConnection`, `AcceptConnectionPropsoal` and `DeleteConnection` actions generate entries in the CloudTrail log files.

Every event or log entry contains information about who generated the request. The identity information helps you determine the following:
+ Whether the request was made with root or AWS Identity and Access Management (IAM) user credentials.
+ Whether the request was made with temporary security credentials for a role or federated user.
+ Whether the request was made by another AWS service.
+ Whether the request was made on the partner side of the service.

For more information, see the [CloudTrail userIdentity element](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-event-reference-user-identity.html).

## Understanding AWS Interconnect log file entries
<a name="understanding-service-name-entries"></a>

A trail is a configuration that enables delivery of events as log files to an Amazon S3 bucket that you specify. CloudTrail log files contain one or more log entries. An event represents a single request from any source and includes information about the requested action, the date and time of the action, request parameters, and so on. CloudTrail log files aren’t an ordered stack trace of the public API calls, so they don’t appear in any specific order.

The following example shows a CloudTrail log entry that demonstrates the `CreateConnection` action.

```
{
    "eventVersion": "1.11",
    "userIdentity": {
        ... redacted ...
    },
    "eventTime": "2026-04-12T21:12:05Z",
    "eventSource": "interconnect.amazonaws.com",
    "eventName": "CreateConnection",
    "awsRegion": "eu-west-2",
    "sourceIPAddress": "174.179.26.172",
    "userAgent": "Mozilla/5.0 ...",
    "requestParameters": {
        "description": "My Multicloud Connection to GCP",
        "bandwidth": "1Gbps",
        "attachPoint": {
            "directConnectGateway": "ba72fdf5-e244-45ac-8374-cf9ebddd4d90"
        },
        "environmentId": "mce-aws-gcp-lhr",
        "remoteAccount": {
            "identifier": "123412341234"
        },
        "tags": {},
        "clientToken": "dcc6ca87-6770-4765-b1e6-5504b9a61bdc"
    },
    "responseElements": {
        "connection": {
            "id": "mcc-12345678",
            "arn": "arn:aws:interconnect:eu-west-2:000000000000:connection/mcc-12345678",
            "description": "Test",
            "bandwidth": "1Gbps",
            "attachPoint": {
                "directConnectGateway": "ba72fdf5-e244-45ac-8374-cf9ebddd4d90"
            },
            "environmentId": "mce-nullprov",
            "provider": {
                "cloudServiceProvider": "aws-test"
            },
            "location": "eu-west-1",
            "type": "Multicloud",
            "state": "requested",
            "sharedId": "ccc4c1c4-cb96-468a-cac9-fc8118a309db",
            "ownerAccount": "000000000000",
            "activationKey": "HIDDEN_DUE_TO_SECURITY_REASONS",
            "tags": {}
        }
    },
    "requestID": "7e60af38-196d-477f-85a0-114efe569fe8",
    "eventID": "5bc65547-bfcf-47c9-a541-1dc87acbd717",
    "readOnly": false,
    "resources": [
        {
            "accountId": "000000000000",
            "type": "AWS::INTERCONNECT::Connection",
            "ARN": "arn:aws:interconnect:eu-west-2:000000000000:connection/mcc-12345678"
        }
    ],
    "eventType": "AwsApiCall",
    "managementEvent": true,
    "recipientAccountId": "000000000000",
    "eventCategory": "Management",
    "tlsDetails": {
        "tlsVersion": "TLSv1.3",
        "cipherSuite": "TLS_AES_128_GCM_SHA256",
        "clientProvidedHostHeader": "interconnect.eu-west-2.api.aws"
    },
    "sessionCredentialFromConsole": "true"
}
```