

The AWS Marketplace API Reference was restructured. For more information about the supported API operations, see the [AWS Marketplace API Reference](https://docs.aws.amazon.com/marketplace/latest/APIReference/Welcome.html).

# Logging AWS Marketplace Metering API calls with CloudTrail
<a name="logging-metering-api-calls-with-cloudtrail"></a>

The Metering API is integrated with AWS CloudTrail, a service that provides a record of actions taken by a user, role, or an AWS service in AWS Marketplace. CloudTrail captures API calls for the Metering API as events. The calls captured include calls from the AWS Marketplace website, console, and other interfaces leveraging the Metering API, as well as direct code calls to Metering API operations.

If you create a trail, you can enable continuous delivery of CloudTrail events to an Amazon S3 bucket, including events for the Metering API. A *trail* enables CloudTrail to deliver log files to an Amazon S3 bucket. If you don't configure a trail, you can still view the most recent events in the CloudTrail console in **Event history**. Using the information collected by CloudTrail, you can determine the request that was made to the Metering API, the IP address from which the request was made, who made the request, when it was made, and additional details.

For more information about CloudTrail, see the [AWS CloudTrail User Guide](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-user-guide.html).

## Metering API information in CloudTrail
<a name="metering-api-info"></a>

CloudTrail is enabled on your AWS account when you create the account. When activity occurs in the Metering API, that activity is recorded in a CloudTrail event along with other AWS service events in **Event history**. You can view, search, and download recent events in your AWS account. For more information, see [Viewing events with CloudTrail Event history](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/view-cloudtrail-events.html) in the *AWS CloudTrail User Guide*.

For an ongoing record of events in your AWS account, including events for the Metering API, create a trail. A *trail* enables CloudTrail to deliver log files to an Amazon S3 bucket. By default, when you create a trail in the console, the trail applies to all AWS Regions. The trail logs events from all Regions in the AWS partition and delivers the log files to the Amazon S3 bucket that you specify. Additionally, you can configure other AWS services to further analyze and act upon the event data collected in CloudTrail logs. For more information, see the following:
+ [Overview for creating a trail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-create-and-update-a-trail.html)
+ [CloudTrail supported services and integrations](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-aws-service-specific-topics.html)
+ [Configuring Amazon SNS notifications for CloudTrail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/configure-sns-notifications-for-cloudtrail.html)
+ [Receiving CloudTrail log files from multiple regions](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/receive-cloudtrail-log-files-from-multiple-regions.html) and [Receiving CloudTrail log files from multiple accounts](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-receive-logs-from-multiple-accounts.html)

The `BatchMeterUsage` action for SaaS-based products, `RegisterUsage` action for container-based products, and `MeterUsage` action for Amazon Machine Image (AMI)-based and container based products are logged by CloudTrail.

Every event or log entry contains information about who generated the request. The identity information helps you determine the following:
+ Whether the request was made with root or user credentials.
+ Whether the request was made with temporary security credentials for a role or federated user.
+ Whether the request was made by another AWS service.

For more information, see [CloudTrail userIdentity element](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-event-reference-user-identity.html) in the *AWS CloudTrail User Guide*.

## Understanding Metering API log file entries
<a name="metering-api-log-file-entries"></a>

### Example: `BatchMeterUsage` for SaaS-based products
<a name="example-aws-marketplace-log-file-entries-batchmeterusage"></a>

The following example shows a CloudTrail log entry that demonstrates the `BatchMeterUsage` action from the AWS Marketplace Metering API. When the seller [sends metering records to report their customers' usage](https://docs.aws.amazon.com/marketplace/latest/userguide/metering-for-usage.html) for a software as a service (SaaS) product listed in AWS Marketplace, this CloudTrail log entry is logged in the seller's AWS account.

```
{
    "eventVersion": "1.05",
    "userIdentity": { 
        "type": "IAMUser",
        "principalId": "EX_PRINCIPAL_ID",
        "arn": "arn:aws:iam::123456789012:user/*****", 
        "accountId": "123456789012",
        "accessKeyId": "EXAMPLE_KEY_ID", 
        "userName": "*****"
    },
    "eventTime": "2018-04-19T16:32:51Z",
    "eventSource": "metering-marketplace.amazonaws.com", 
    "eventName": "BatchMeterUsage",
    "awsRegion": "us-east-1", 
    "sourceIPAddress": "************", 
    "userAgent": "Coral/Netty14", 
    "requestParameters": {
        "usageRecords": [
            {
                "dimension": "Dimension1", 
                "timestamp": "Apr 19, 2018 4:32:50 PM", 
                "customerIdentifier": "customer1",
                "customerAWSAccountID": "987654321098", 
                "quantity": 1
            }
        ],
        "productCode": "EXAMPLE_proCode"
    },
    "responseElements": { 
        "results": [
            {
                "usageRecord": {
                    "dimension": "Dimension1", 
                    "timestamp": "Apr 19, 2018 4:32:50 PM", 
                    "customerIdentifier": "customer1",
                    "customerAWSAccountID": "987654321098", 
                    "quantity": 1
                },
                "meteringRecordId": "bEXAMPLE-98f0-4e90-8bd2-bf0EXAMPLE1e", 
                "status": "Success"
            }
        ],
        "unprocessedRecords": [ ]
    },
    "requestID": "dEXAMPLE-251d-11e7-8d11-1f3EXAMPLE8b", 
    "eventID": "cEXAMPLE-e6c2-465d-b47f-150EXAMPLE97", 
    "readOnly": false,
    "eventType": "AwsApiCall", 
    "recipientAccountId": "123456789012"
}
```

### Example: `RegisterUsage` for containers-based products deployed on Amazon EKS
<a name="example-aws-marketplace-log-file-entries-registerusage-containers"></a>

The following example shows a CloudTrail log entry that demonstrates the `RegisterUsage` action from the AWS Marketplace Metering API. When an hourly priced container product from AWS Marketplace is deployed in the buyer's AWS account, the software in the container calls `RegisterUsage` within the buyer's AWS account to initiate the hourly metering for that Amazon Elastic Container Service (Amazon ECS) task or Amazon Elastic Kubernetes Service (Amazon EKS) pod. This CloudTrail log entry is logged in the buyer's AWS account.

```
{
    "eventVersion": "1.05",
    "userIdentity": {
        "type": "AssumedRole",
        "principalId": "EX_PRINCIPAL_ID:botocore-session-1111111111",
        "arn": "arn:aws:sts::123456789012:assumed-role/Alice/botocore-session-1111111111",
        "accountId": "123456789012",
        "accessKeyId": "EXAMPLE_KEY_ID",
        "sessionContext": {
            "sessionIssuer": {
                "type": "Role",
                "principalId": "EX_PRINCIPAL_ID",
                "arn": "arn:aws:iam::123456789012:role/Alice",
                "accountId": "123456789012",
                "userName": "Alice"
            },
            "webIdFederationData": {
                "federatedProvider": "arn:aws:iam::123456789012:oidc-provider/oidc.eks.us-east-1.amazonaws.com/id/EXAMPLEFA1C58F08CDB049167EXAMPLE",
                "attributes": {}
            },
            "attributes": {
                "mfaAuthenticated": "false",
                "creationDate": "2020-07-23T02:19:34Z"
            }
        }
    },
    "eventTime": "2020-07-23T02:19:46Z",
    "eventSource": "metering-marketplace.amazonaws.com",
    "eventName": "RegisterUsage",
    "awsRegion": "us-east-1",
    "sourceIPAddress": "1.2.3.4",
    "userAgent": "aws-cli/1.18.103 Python/3.8.2 Linux/4.14.181-142.260.amzn2.x86_64 botocore/1.17.26",
    "requestParameters": {
        "productCode": "EXAMPLE_proCode",
        "publicKeyVersion": 1
    },
    "responseElements": {
        "signature": "eyJhbGciOiJQUzI1Ni..."
    },
    "requestID": "dEXAMPLE-251d-11e7-8d11-1f3EXAMPLE8b",
    "eventID": "cEXAMPLE-e6c2-465d-b47f-150EXAMPLE97",
    "eventType": "AwsApiCall",
    "recipientAccountId": "123456789012"
}
```

### Example: `MeterUsage` for container-based products deployed on Amazon EKS
<a name="example-aws-marketplace-log-file-entries-meterusage"></a>

The following example shows a CloudTrail log entry that demonstrates the `MeterUsage` action from the AWS Marketplace Metering API for containers on Amazon EKS. When a container product with [custom metering](https://docs.aws.amazon.com/marketplace/latest/userguide/container-metering-meterusage.html) from AWS Marketplace is deployed in the buyer's AWS account, the software in the container calls `MeterUsage` within the buyer's AWS account to report each hour. This CloudTrail log entry is logged in the buyer's AWS account.

```
{
    "eventVersion": "1.05",
    "userIdentity": {
        "type": "AssumedRole",
        "principalId": "EX_PRINCIPAL_ID:botocore-session-1111111111",
        "arn": "arn:aws:sts::123456789012:assumed-role/Alice/botocore-session-1111111111",
        "accountId": "123456789012",
        "accessKeyId": "EXAMPLE_KEY_ID",
        "sessionContext": {
            "sessionIssuer": {
                "type": "Role",
                "principalId": "EX_PRINCIPAL_ID",
                "arn": "arn:aws:iam::123456789012:role/Alice",
                "accountId": "123456789012",
                "userName": "Alice"
            },
            "webIdFederationData": {
                "federatedProvider": "arn:aws:iam::123456789012:oidc-provider/oidc.eks.us-east-1.amazonaws.com/id/EXAMPLEFA1C58F08CDB049167EXAMPLE",
                "attributes": {}
            },
            "attributes": {
                "mfaAuthenticated": "false",
                "creationDate": "2020-07-23T01:03:26Z"
            }
        }
    },
    "eventTime": "2020-07-23T01:38:13Z",
    "eventSource": "metering-marketplace.amazonaws.com",
    "eventName": "MeterUsage",
    "awsRegion": "us-east-1",
    "sourceIPAddress": "1.2.3.4",
    "userAgent": "aws-cli/1.18.103 Python/3.8.2 Linux/4.14.181-142.260.amzn2.x86_64 botocore/1.17.26",
    "requestParameters": {
        "timestamp": "Jul 23, 2020 1:35:44 AM",
        "usageQuantity": 1,
        "usageDimension": "Dimension1",
        "productCode": "EXAMPLE_proCode"
    },
    "responseElements": {
        "meteringRecordId": "bEXAMPLE-98f0-4e90-8bd2-bf0EXAMPLE1e"
    },
    "requestID": "dEXAMPLE-251d-11e7-8d11-1f3EXAMPLE8b",
    "eventID": "cEXAMPLE-e6c2-465d-b47f-150EXAMPLE97",
    "eventType": "AwsApiCall",
    "recipientAccountId": "123456789012"
}
```

### Example: `MeterUsage` for AMI-based products
<a name="example-aws-marketplace-log-file-entries-meterusage-amis"></a>

The following example shows a CloudTrail log entry that demonstrates the `MeterUsage` action from the AWS Marketplace Metering API for Amazon Machine Images (AMIs). When an AMI product with custom metering from AWS Marketplace is deployed in the buyer's AWS account, the software from the AMI calls `MeterUsage` within the buyer's AWS account to report usage each hour. This CloudTrail log entry is logged in the buyer's AWS account.

```
{
    "eventVersion": "1.05",
    "userIdentity": {
        "type": "AssumedRole",
        "principalId": "EX_PRINCIPAL_ID:i-exampled859aa775c",
        "arn": "arn:aws:sts::123456789012:assumed-role/Alice/i-exampled859aa775c",
        "accountId": "123456789012",
        "accessKeyId": "EXAMPLE_KEY_ID",
        "sessionContext": {
            "sessionIssuer": {
                "type": "Role",
                "principalId": "EX_PRINCIPAL_ID",
                "arn": "arn:aws:iam::123456789012:role/Alice",
                "accountId": "123456789012",
                "userName": "Alice"
            },
            "webIdFederationData": {},
            "attributes": {
                "mfaAuthenticated": "false",
                "creationDate": "2020-07-10T23:05:20Z"
            },
            "ec2RoleDelivery": "1.0"
        }
    },
    "eventTime": "2020-07-10T23:06:42Z",
    "eventSource": "metering-marketplace.amazonaws.com",
    "eventName": "MeterUsage",
    "awsRegion": "us-east-1",
    "sourceIPAddress": "1.2.3.4",
    "userAgent": "aws-cli/1.16.102 Python/2.7.16 Linux/4.14.133-113.112.amzn2.x86_64 botocore/1.12.92",
    "requestParameters": {
        "productCode": "EXAMPLE_proCode",
        "timestamp": "Jul 10, 2020 11:06:41 PM",
        "usageDimension": "Dimension1",
        "usageQuantity": 1,
        "dryRun": false
    },
    "responseElements": {
        "meteringRecordId": "bEXAMPLE-98f0-4e90-8bd2-bf0EXAMPLE1e"
    },
    "requestID": "dEXAMPLE-251d-11e7-8d11-1f3EXAMPLE8b",
    "eventID": "cEXAMPLE-e6c2-465d-b47f-150EXAMPLE97",
    "eventType": "AwsApiCall",
    "recipientAccountId": "123456789012"
}
```