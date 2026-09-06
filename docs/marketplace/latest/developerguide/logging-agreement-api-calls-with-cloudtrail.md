

The AWS Marketplace API Reference was restructured. For more information about the supported API operations, see the [AWS Marketplace API Reference](https://docs.aws.amazon.com/marketplace/latest/APIReference/Welcome.html).

# Logging AWS Marketplace Agreement API calls with CloudTrail
<a name="logging-agreement-api-calls-with-cloudtrail"></a>

The Agreements API is integrated with AWS CloudTrail, a service that provides a record of actions taken by a user, role, or an AWS service in AWS Marketplace. CloudTrail captures API calls for the Agreements API as events. The calls captured include calls from the AWS Marketplace website, console, and other interfaces leveraging the Agreements API, as well as direct code calls to Agreements API operations.

If you create a trail, you can enable continuous delivery of CloudTrail events to an Amazon S3 bucket, including events for the Agreements API. A *trail* enables CloudTrail to deliver log files to an Amazon S3 bucket. If you don't configure a trail, you can still view the most recent events in the CloudTrail console in **Event history**. Using the information collected by CloudTrail, you can determine the request that was made to the Agreements API, the IP address from which the request was made, who made the request, when it was made, and additional details.

For more information about CloudTrail, see the [AWS CloudTrail User Guide](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-user-guide.html).

## Agreements API information in CloudTrail
<a name="agreement-agreements-api-info"></a>

CloudTrail is enabled on your AWS account when you create the account. When activity occurs in the Agreements API, that activity is recorded in a CloudTrail event along with other AWS service events in **Event history**. You can view, search, and download recent events in your AWS account. For more information, see [Viewing events with CloudTrail Event history](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/view-cloudtrail-events.html) in the *AWS CloudTrail User Guide*.

For an ongoing record of events in your AWS account, including events for the Agreements API, create a trail. A *trail* enables CloudTrail to deliver log files to an Amazon S3 bucket. By default, when you create a trail in the console, the trail applies to all AWS Regions. The trail logs events from all Regions in the AWS partition and delivers the log files to the Amazon S3 bucket that you specify. Additionally, you can configure other AWS services to further analyze and act upon the event data collected in CloudTrail logs. For more information, see the following:
+ [Overview for creating a trail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-create-and-update-a-trail.html)
+ [CloudTrail supported services and integrations](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-aws-service-specific-topics.html)
+ [Configuring Amazon SNS notifications for CloudTrail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/configure-sns-notifications-for-cloudtrail.html)
+ [Receiving CloudTrail log files from multiple regions](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/receive-cloudtrail-log-files-from-multiple-regions.html) and [Receiving CloudTrail log files from multiple accounts](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-receive-logs-from-multiple-accounts.html)

Every event or log entry contains information about who generated the request. The identity information helps you determine the following:
+ Whether the request was made with root or user credentials.
+ Whether the request was made with temporary security credentials for a role or federated user.
+ Whether the request was made by another AWS service.

For more information, see [CloudTrail userIdentity element](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-event-reference-user-identity.html) in the *AWS CloudTrail User Guide*.

## Understanding Agreements API actions
<a name="agreements-api-understanding"></a>

The Agreements API is used to purchase software as a service (SaaS), server (including container), and professional services products on AWS Marketplace. It's also used to manage resulting agreements or subscriptions on AWS Marketplace.

**Note**  
Purchases of AWS Data Exchange products won't be logged by CloudTrail.

The `AcceptAgreementRequest` action is used when an AWS Identity and Access Management (IAM) user or role of an AWS account purchases an applicable product on AWS Marketplace. Similarly, the `CancelAgreement` action is used when an IAM user or role cancels their agreement or subscription. By monitoring CloudTrail logs in the Agreements API, buyers can monitor the most important purchase-related actions happening in their AWS account on AWS Marketplace.

The `DescribeAgreement` action is used when the customer specifically views meta data for a specific agreement. The `GetAgreementTerms` action is used when the terms of a particular agreement are viewed. The `SearchAgreements` action is used when an IAM user or role lists or filters out a subset of their agreements from the full list of all their agreements.

**Note**  
The `AcceptAgreementRequest` and `CancelAgreement` actions are available to buyers but not sellers. However, the `DescribeAgreement`, `GetAgreementTerms`, and `SearchAgreements` actions can be used by both buyers and sellers.

Buyers can also identify the Agreement ID of the agreement from the CloudTrail log. For more information about the agreement, choose the **Manage subscriptions** tab in the AWS Marketplace console, where the Agreement ID is provided in the **Details** view. The Agreement ID can be found in `responseElements` for the `AcceptAgreementRequest` API action and in `requestParameters` for the `CancelAgreement` API action.

## Understanding Agreements API log file entries
<a name="agreements-api-log-file-entries"></a>

A trail is a configuration that enables delivery of events as log files to an Amazon S3 bucket that you specify. CloudTrail log files contain one or more log entries. An event represents a single request from any source and includes information about the requested action, the date and time of the action, request parameters, and so on. CloudTrail log files aren't an ordered stack trace of the public API calls, so they don't display in a specific order.

The following example shows a CloudTrail log entry that demonstrates the `AcceptAgreementRequest` action.

```
{
  "eventVersion": "1.08",
  "userIdentity": {
    "type": "Unknown",
    "principalId": "ABCDEFGHIJKLMNOP12345",
    "arn": "arn:aws:iam::123456789010:user/CloudTrailTestUser",
    "accountId": "123456789010",
    "accessKeyId": "ABCDEFGHIJKLMNOP123"
  },
  "eventTime": "2023-08-11T17:13:50Z",
  "eventSource": "agreement-marketplace.amazonaws.com",
  "eventName": "AcceptAgreementRequest",
  "awsRegion": "us-west-2",
  "sourceIPAddress": "127.0.0.1",
  "userAgent": "Coral/Netty4",
  "requestParameters": {
    "agreementRequestId": "ar-6xbrddjzym594imkrrezrn5wa"
  },
  "responseElements": {
    "agreementId": "agmt-1lnrq6riwpg2tczhv378zknlc"
  },
  "requestID": "fEXAMPLE-cb3e-4e21-86fd-6b3EXAMPLEd1",
  "eventID": "7EXAMPLE-97d6-4139-91e3-01aEXAMPLE48",
  "readOnly": false,
  "eventType": "AwsApiCall",
  "managementEvent": true,
  "recipientAccountId": "123456789010",
  "eventCategory": "Management"
}
```

The following example shows a CloudTrail log entry that demonstrates the `CancelAgreement` action.

```
{
  "eventVersion": "1.08",
  "userIdentity": {
    "type": "Unknown",
    "principalId": "ABCDEFGHIJKLMNOP12345",
    "arn": "arn:aws:iam::123456789010:user/CloudTrailTestUser",
    "accountId": "123456789010",
    "accessKeyId": "ABCDEFGHIJKLMNOP1234"
  },
  "eventTime": "2023-08-14T03:11:42Z",
  "eventSource": "agreement-marketplace.amazonaws.com",
  "eventName": "CancelAgreement",
  "awsRegion": "us-west-2",
  "sourceIPAddress": "127.0.0.1",
  "userAgent": "Coral/Netty4",
  "requestParameters": {
    "agreementId": "agmt-enitbfqjebjmwmomzrucf032t"
  },
  "responseElements": null,
  "requestID": "fEXAMPLE-cb3e-4e21-86fd-6b3EXAMPLEd1",
  "eventID": "7EXAMPLE-97d6-4139-91e3-01aEXAMPLE48",
  "readOnly": false,
  "eventType": "AwsApiCall",
  "managementEvent": true,
  "recipientAccountId": "123456789010",
  "eventCategory": "Management"
}
```

The following example shows a CloudTrail log entry that demonstrates the `DescribeAgreement` action.

```
{
    "eventVersion": "1.08",
    "userIdentity": {
        "type": "Unknown",
        "principalId": "ABCDEFGHIJKLMNOP12345",
        "arn": "arn:aws:iam::123456789010:user/CloudtrailTestUser",
        "accountId": "123456789010",
        "accessKeyId": "ABCDEFGHIJKLMNOP123",
    },
    "eventTime": "2023-10-30T22:45:24Z",
    "eventSource": "agreement-marketplace.amazonaws.com",
    "eventName": "DescribeAgreement",
    "awsRegion": "us-west-2",
    "sourceIPAddress": "127.0.0.1",
    "userAgent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36",
    "requestParameters": {
        "agreementId": "agmt-6wy4rhp7l6iyuu2jrcgd1shdi"
    },
    "responseElements": null,
    "requestID": "bEXAMPLE-347f-4c07-9645-cd2EXAMPLE61",
    "eventID": "dEXAMPLE-d891-42a5-8da6-1cdEXAMPLE34",
    "readOnly": true,
    "eventType": "AwsApiCall",
    "managementEvent": true,
    "recipientAccountId": "123456789010",
    "eventCategory": "Management",
}
```

The following example shows a CloudTrail log entry that demonstrates the `GetAgreementTerms` action.

```
{
    "eventVersion": "1.08",
    "userIdentity": {
        "type": "Unknown",
        "principalId": "ABCDEFGHIJKLMNOP12345",
        "arn": "arn:aws:iam::123456789010:user/CloudtrailTestUser",
        "accountId": "123456789010",
        "accessKeyId": "ABCDEFGHIJKLMNOP123",
    },
    "eventTime": "2023-10-30T22:48:37Z",
    "eventSource": "agreement-marketplace.amazonaws.com",
    "eventName": "GetAgreementTerms",
    "awsRegion": "us-west-2",
    "sourceIPAddress": "127.0.0.1",
    "userAgent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36",
    "requestParameters": {
        "agreementId": "agmt-6wy4rhp7l6iyuu2jrcgd1shdi"
    },
    "responseElements": null,
    "requestID": "eEXAMPLE-fc57-4127-bbda-bc1EXAMPLE03",
    "eventID": "bEXAMPLE-5345-4634-8b58-925EXAMPLE3e",
    "readOnly": true,
    "eventType": "AwsApiCall",
    "managementEvent": true,
    "recipientAccountId": "123456789010",
    "eventCategory": "Management",
}
```

The following example shows a CloudTrail log entry that demonstrates the `SearchAgreements` action.

```
{
    "eventVersion": "1.08",
    "userIdentity": {
        "type": "Unknown",
        "principalId": "ABCDEFGHIJKLMNOP12345",
        "arn": "arn:aws:iam::123456789010:user/CloudtrailTestUser",
        "accountId": "123456789010",
        "accessKeyId": "ABCDEFGHIJKLMNOP123",
    },
    "eventTime": "2023-10-30T18:41:10Z",
    "eventSource": "agreement-marketplace.amazonaws.com",
    "eventName": "SearchAgreements",
    "awsRegion": "us-west-2",
    "sourceIPAddress": "127.0.0.1",
    "userAgent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36",
    "requestParameters": {
        "catalog": "AWSMarketplace",
        "filters": [
            {
                "name": "PartyType",
                "values": [
                    "Proposer"
                ]
            },
            {
                "name": "ResourceType",
                "values": [
                    "SaaSProduct"
                ]
            },
            {
                "name": "Status",
                "values": [
                    "ACTIVE"
                ]
            },
            {
                "name": "AgreementType",
                "values": [
                    "PurchaseAgreement"
                ]
            }
        ],
        "maxResults": 5
    },
    "responseElements": null,
    "requestID": "fEXAMPLE-0aa6-4e42-8715-6a1EXAMPLE95",
    "eventID": "0EXAMPLE-8ce8-4814-bcf1-636EXAMPLEb5",
    "readOnly": true,
    "eventType": "AwsApiCall",
    "managementEvent": true,
    "recipientAccountId": "123456789010",
    "eventCategory": "Management",
}
```