

# Logging Amazon Managed Blockchain (AMB) Access Bitcoin events by using AWS CloudTrail
<a name="logging-using-cloudtrail"></a>

**Note**  
Amazon Managed Blockchain (AMB) Access Bitcoin doesn’t support management events.

Amazon Managed Blockchain is integrated with AWS CloudTrail, a service that provides a record of actions taken by a user, role, or an AWS service in Managed Blockchain. CloudTrail captures who invoked the AMB Access Bitcoin endpoints for Managed Blockchain as data plane events.

If you create a properly configured trail that is subscribed to receive the desired data plane events, you can receive continuous delivery of AMB Access Bitcoin-related CloudTrail events to an Amazon S3 bucket. Using the information that's collected by CloudTrail, you can determine that a request was made to one of the AMB Access Bitcoin endpoints, the IP address that the request came from, who made the request, when it was made, and other additional details.

To learn more about CloudTrail, see the [AWS CloudTrail User Guide](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-user-guide.html).

## AMB Access Bitcoin information in CloudTrail
<a name="service-name-info-in-cloudtrail"></a>

AWS CloudTrail is enabled by default when you create your AWS account. However, to see who invoked the AMB Access Bitcoin endpoints, you must configure CloudTrail to log *data plane* events. 

To keep an ongoing record of events in your AWS account, including the data plane events for AMB Access Bitcoin, you must create a *trail*. A trail makes CloudTrail deliver log files to an Amazon S3 bucket. By default, when you create a trail in the AWS Management Console, the trail applies to all AWS Regions. The trail logs events from all supported Regions in the AWS partition and delivers the log files to the Amazon S3 bucket that you specify. Additionally, you can configure other AWS services to analyze this data further and act on the events data collected in the CloudTrail logs. For more information, see the following: 
+ [Using CloudTrail to track Bitcoin JSON-RPCs](#bitcoin-logging)
+ [Overview for creating a trail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-create-and-update-a-trail.html)
+ [CloudTrail supported services and integrations](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-aws-service-specific-topics.html)
+ [Configuring Amazon SNS notifications for CloudTrail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/configure-sns-notifications-for-cloudtrail.html)
+ [Receiving CloudTrail log files from multiple regions](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/receive-cloudtrail-log-files-from-multiple-regions.html) and [Receiving CloudTrail log files from multiple accounts](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-receive-logs-from-multiple-accounts.html)

By analyzing the CloudTrail data events, you can monitor who invoked the AMB Access Bitcoin endpoints.

Every event or log entry contains information about who generated the request. The identity information helps you determine the following:
+ Whether the request was made with root or AWS Identity and Access Management (IAM) user credentials.
+ Whether the request was made with temporary security credentials for a role or a federated user.
+ Whether the request was made by another AWS service.

For more information, see the [CloudTrail userIdentity element](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-event-reference-user-identity.html).

## Understanding AMB Access Bitcoin log file entries
<a name="understanding-service-name-entries"></a>

For data plane events, a trail is a configuration that enables delivery of events as log files to a specified S3 bucket. Each CloudTrail log file contains one or more log entries that represent a single request from any source. These entries provide details about the requested action, including the date and time of the action, and any associated request parameters. 

**Note**  
CloudTrail data events in the log files aren't an ordered stack trace of the AMB Access Bitcoin API calls, so they don't appear in any specific order.

### Using CloudTrail to track Bitcoin JSON-RPCs
<a name="bitcoin-logging"></a>

You can use CloudTrail to track who in your account invoked the AMB Access Bitcoin endpoints and what JSON-RPC was invoked as *data events*. By default, when you create a trail, data events aren't logged. To record who invoked the AMB Access Bitcoin endpoints as CloudTrail data events, you must explicitly add the supported resources or resource types for which you want to collect activity to a trail. Amazon Managed Blockchain supports adding data events by using the AWS Management Console, AWS SDK, and AWS CLI. For more information, see [Log events by using advanced selectors](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/logging-data-events-with-cloudtrail.html#creating-data-event-selectors-advanced) in the *AWS CloudTrail User Guide *.

To log data events in a trail, use the [put-event-selectors](https://docs.aws.amazon.com/cli/latest/reference/cloudtrail/put-event-selectors.html) operation after you create the trail. Use the `--advanced-event-selectors` option to specify the `AWS::ManagedBlockchain::Network` resource types in order to start logging data events to determine who invoked the AMB Access Bitcoin endpoints.

**Example Data event log entry of all your account's AMB Access Bitcoin endpoints requests**  
The following example demonstrates how to use the `put-event-selectors` operation to log all your account's AMB Access Bitcoin endpoint requests for the trail `my-bitcoin-trail` in the `us-east-1` Region.  

```
aws cloudtrail put-event-selectors \                                                                                                         
--region {{us-east-1}} \
--trail-name {{my-bitcoin-trail}}  \
--advanced-event-selectors '[{
    "Name": "{{Test}}",
    "FieldSelectors": [
      { "Field": "eventCategory", "Equals": ["Data"] },
      { "Field": "resources.type", "Equals": ["AWS::ManagedBlockchain::Network"] } ]}]'
```
After you subscribe, you can track usage in the S3 bucket that is connected to the trail specified in the previous example.  
The following result shows a CloudTrail data event log entry of the information that's collected by CloudTrail. You can determine that a Bitcoin JSON-RPC request was made to one of the AMB Access Bitcoin endpoints, the IP address that the request came from, who made the request, when it was made, and other additional details.  

```
{
        "eventVersion": "1.08",
        "userIdentity": {
            "type": "AssumedRole",
            "principalId": "AROA554UO62RJ7KSB7FAX:777777777777",
            "arn": "arn:aws:sts::111122223333:assumed-role/Admin/777777777777",
            "accountId": "111122223333"
        },
        "eventTime": "2023-04-12T19:00:22Z",
        "eventSource": "managedblockchain.amazonaws.com",
        "eventName": "getblock",
        "awsRegion": "{{us-east-1}}",
        "sourceIPAddress": "111.222.333.444",
        "userAgent": "python-requests/2.28.1",
        "errorCode": "-",
        "errorMessage": "-",
        "requestParameters": {
            "jsonrpc": "2.0",
            "method": "getblock",
            "params": [],
            "id": 1
        },
        "responseElements": null,
        "requestID": "DRznHHEjIAMFSzA=",
        "eventID": "baeb232d-2c6b-46cd-992c-0e4033aace86",
        "readOnly": true,
        "resources": [{
            "type": "AWS::ManagedBlockchain::Network",
            "ARN": "arn:aws:managedblockchain:::networks/n-bitcoin-mainnet"
        }],
        "eventType": "AwsApiCall",
        "managementEvent": false,
        "recipientAccountId": "111122223333",
        "eventCategory": "Data"
}
```