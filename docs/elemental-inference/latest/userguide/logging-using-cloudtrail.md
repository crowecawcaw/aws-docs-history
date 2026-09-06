

# Logging Elemental Inference API calls with AWS CloudTrail
<a name="logging-using-cloudtrail"></a>

AWS Elemental Inference is integrated with AWS CloudTrail. *AWS CloudTrail* captures API calls and related events made by or on behalf of your AWS account and delivers the log files to an Amazon S3 bucket that you specify. You can identify which users and accounts called AWS, the source IP address from which the calls were made, and when the calls occurred. 

To learn more about CloudTrail, see the [AWS CloudTrail User Guide](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/).

## Elemental Inference information in CloudTrail
<a name="elemental-inference-info-in-cloudtrail"></a>

CloudTrail is enabled on your AWS account when you create the account. When activity occurs in Elemental Inference, that activity is recorded in a CloudTrail event along with other AWS service events in **Event history**. You can view, search, and download recent events in your AWS account. For more information, see [Viewing Events with CloudTrail Event History](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/view-cloudtrail-events.html). 

For an ongoing record of events in your AWS account, including events for Elemental Inference, create a trail. A *trail* enables CloudTrail to deliver log files to an Amazon S3 bucket. By default, when you create a trail in the console, the trail applies to all AWS Regions. The trail logs events from all Regions in the AWS partition and delivers the log files to the Amazon S3 bucket that you specify. Additionally, you can configure other AWS services to further analyze and act upon the event data collected in CloudTrail logs. For more information, see the following: 
+ [Overview for Creating a Trail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-create-and-update-a-trail.html)
+ [CloudTrail Supported Services and Integrations](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-aws-service-specific-topics.html#cloudtrail-aws-service-specific-topics-integrations)
+ [Configuring Amazon SNS Notifications for CloudTrail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/getting_notifications_top_level.html)
+ [Receiving CloudTrail Log Files from Multiple Regions](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/receive-cloudtrail-log-files-from-multiple-regions.html) and [Receiving CloudTrail Log Files from Multiple Accounts](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-receive-logs-from-multiple-accounts.html)

Every event or log entry contains information about who generated the request. The identity information helps you determine the following: 
+ Whether the request was made with root or AWS Identity and Access Management (IAM) user credentials.
+ Whether the request was made with temporary security credentials for a role or federated user.
+ Whether the request was made by another AWS service.

For more information, see the [CloudTrail userIdentity Element](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-event-reference-user-identity.html).

## Understanding Elemental Inference log file entries
<a name="understanding-elemental-inference-entries"></a>

A trail is a configuration that enables delivery of events as log files to an Amazon S3 bucket that you specify. CloudTrail log files contain one or more log entries. An event represents a single request from any source and includes information about the requested action, the date and time of the action, request parameters, and so on. CloudTrail log files aren't an ordered stack trace of the public API calls, so they don't appear in any specific order. 

The following example shows a CloudTrail log entry. The example shows the entry for one API call. The call is made by the identity specified in `userIdentity`, in this case a user who has assumed the Administrator role with the session name `santosp`. The call was a `CreateFeed` operation coming from the AWS CLI (as specified in `userAgent`) running on a computer with the IP address 203.0.113.33

```
{
  "eventVersion": "1.09",
  "userIdentity": {
    "type": "AssumedRole",
    "principalId": "AROAEXAMPLEID:santosp",
    "arn": "arn:aws:sts::111122223333:assumed-role/Administrator/santosp",
    "accountId": "111122223333",
    "accessKeyId": "AKIAIOSFODNN7EXAMPLE",
    "sessionContext": {
      "sessionIssuer": {
        "type": "Role",
        "principalId": "AROAEXAMPLEID",
        "arn": "arn:aws:iam::111122223333:role/Administrator",
        "accountId": "111122223333",
        "userName": "Administrator"
      },
      "attributes": {
        "creationDate": "2024-11-14T19:00:28Z",
        "mfaAuthenticated": "false"
      }
    }
  },
  "eventTime": "2024-11-14T19:00:29Z",
  "eventSource": "elemental-inference.amazonaws.com",
  "eventName": "CreateFeed",
  "awsRegion": "us-west-2",
  "sourceIPAddress": "203.0.113.33",
  "userAgent": "aws-cli/2.32.22 md/awscrt#0.29.1 ua/2.1 os/linux#6.1.159-182.297.amzn2023.x86_64 md/arch#x86_64 lang/python#3.9.25 md/pyimpl#CPython cfg/retry-mode#standard md/installer#source md/distrib#amzn.2023 md/prompt#off md/command#elemental-inference.create-feed",
  "requestParameters": {
    "outputs": [
      {
        "name": "out1",
        "outputConfig": {
          "cropping": {}
        },
        "status": "ENABLED"
      }
    ],
    "name": "live-studio-feed",
    "x-amzn-client-token": "1111aaaa-e840-4416-8ee8-a95d5ed7c031"
  },
  "responseElements": {
    "outputs": [
      {
        "name": "out1",
        "outputConfig": {
          "cropping": {}
        },
        "status": "ENABLED"
      }
    ],
    "dataEndpoints": [
      "https://abc123example.elemental-inference-data.us-west-2.amazonaws.com/"
    ],
    "name": "live-studio-feed",
    "id": "abc123example",
    "arn": "arn:aws:elemental-inference:us-west-2:111122223333:feed/abc123example",
    "status": "CREATING",
    "tags": {}
  },
  "requestID": "d2f882ac-1a9d-11e9-a0e5-afe6a8c88993",
  "eventID": "ebbe0290-7a1b-4053-a219-367404e0fe96",
  "readOnly": false,
  "resources": [
    {
      "accountId": "111122223333",
      "type": "AWS::Elemental-Inference::Feed",
      "ARN": "arn:aws:elemental-inference:us-west-2:111122223333:feed/abc123example"
    }
  ],
  "eventType": "AwsApiCall",
  "managementEvent": true,
  "recipientAccountId": "111122223333",
  "eventCategory": "Management"
}
```