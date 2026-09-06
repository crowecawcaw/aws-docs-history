

# Logging AWS B2B Data Interchange API calls using AWS CloudTrail
<a name="logging-using-cloudtrail"></a>

AWS B2B Data Interchange is integrated with AWS CloudTrail, a service that provides a record of actions taken by a user, role, or an AWS service in AWS B2B Data Interchange. CloudTrail captures all API calls for AWS B2B Data Interchange as events. The calls captured include calls from the AWS B2B Data Interchange console and code calls to the AWS B2B Data Interchange API operations. If you create a trail, you can enable continuous delivery of CloudTrail events to an Amazon S3 bucket, including events for AWS B2B Data Interchange. If you don't configure a trail, you can still view the most recent events in the CloudTrail console in **Event history**. Using the information collected by CloudTrail, you can determine the request that was made to AWS B2B Data Interchange, the IP address from which the request was made, who made the request, when it was made, and additional details.

To learn more about CloudTrail, see the [AWS CloudTrail User Guide](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-user-guide.html).

## AWS B2B Data Interchange information in CloudTrail
<a name="service-name-info-in-cloudtrail"></a>

CloudTrail is enabled on your AWS account when you create the account. When activity occurs in AWS B2B Data Interchange, that activity is recorded in a CloudTrail event along with other AWS service events in **Event history**. You can view, search, and download recent events in your AWS account. For more information, see [Viewing events with CloudTrail Event history](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/view-cloudtrail-events.html).

For an ongoing record of events in your AWS account, including events for AWS B2B Data Interchange, create a trail. A *trail* enables CloudTrail to deliver log files to an Amazon S3 bucket. By default, when you create a trail in the console, the trail applies to all AWS Regions. The trail logs events from all Regions in the AWS partition and delivers the log files to the Amazon S3 bucket that you specify. Additionally, you can configure other AWS services to further analyze and act upon the event data collected in CloudTrail logs. For more information, see the following:
+ [Overview for creating a trail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-create-and-update-a-trail.html)
+ [CloudTrail supported services and integrations](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-aws-service-specific-topics.html)
+ [Configuring Amazon SNS notifications for CloudTrail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/configure-sns-notifications-for-cloudtrail.html)
+ [Receiving CloudTrail log files from multiple regions](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/receive-cloudtrail-log-files-from-multiple-regions.html) and [Receiving CloudTrail log files from multiple accounts](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-receive-logs-from-multiple-accounts.html)

All AWS B2B Data Interchange actions are logged by CloudTrail and are documented in the [AWS B2B Data Interchange API Reference](https://docs.aws.amazon.com/b2bi/latest/APIReference/).

Every event or log entry contains information about who generated the request. The identity information helps you determine the following:
+ Whether the request was made with root or AWS Identity and Access Management (IAM) user credentials.
+ Whether the request was made with temporary security credentials for a role or federated user.
+ Whether the request was made by another AWS service.

For more information, see the [CloudTrail userIdentity element](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-event-reference-user-identity.html).

## Understanding AWS B2B Data Interchange log file entries
<a name="understanding-service-name-entries"></a>

A trail is a configuration that enables delivery of events as log files to an Amazon S3 bucket that you specify. CloudTrail log files contain one or more log entries. An event represents a single request from any source and includes information about the requested action, the date and time of the action, request parameters, and so on. CloudTrail log files aren't an ordered stack trace of the public API calls, so they don't appear in any specific order.

This is an example log entry for creating a trading capability.

```
{
    "eventVersion": "1.09",
    "userIdentity": {
        "type": "AssumedRole",
        "principalId": "{{principal-id}}",
        "arn": "arn:aws:sts::{{account-id}}:assumed-role/{{invocation-role}}/{{role-id}}",
        "accountId": "{{account-id}}",
        "accessKeyId": "xxxxxxxxxxxxxxxxxxxx",
        "sessionContext": {
            "sessionIssuer": {
                "type": "Role",
                "principalId": "XXXXXXXXXXXXXXXXXXXXX",
                "arn": "arn:aws:iam::{{account-id}}:role/{{invocation-role}}",
                "accountId": "{{account-id}}",
                "userName": "{{invocation-role}}"
            },
            "attributes": {
                "creationDate": "2023-11-24T17:24:07Z",
                "mfaAuthenticated": "false"
            }
        }
    },
    "eventTime": "2023-11-24T17:27:05Z",
    "eventSource": "b2bi.amazonaws.com",
    "eventName": "CreateCapability",
    "awsRegion": "us-east-1",
    "sourceIPAddress": "34.207.212.3",
    "userAgent": "example-user-agent",
    "requestParameters": {
        "name": "Integration Test EDI 214 Version 8 Update Capability",
        "type": "edi",
        "configuration": {
            "edi": {
                "type": {
                    "x12Details": {
                        "transactionSet": "HIDDEN_DUE_TO_SECURITY_REASONS",
                        "version": "HIDDEN_DUE_TO_SECURITY_REASONS"
                    }
                },
                "inputLocation": {
                    "bucketName": "HIDDEN_DUE_TO_SECURITY_REASONS",
                    "key": "HIDDEN_DUE_TO_SECURITY_REASONS"
                },
                "outputLocation": {
                    "bucketName": "HIDDEN_DUE_TO_SECURITY_REASONS",
                    "key": "HIDDEN_DUE_TO_SECURITY_REASONS"
                },
                "transformerId": "HIDDEN_DUE_TO_SECURITY_REASONS"
            }
        },
        "instructionsDocuments": [
            {
                "bucketName": "HIDDEN_DUE_TO_SECURITY_REASONS",
                "key": "HIDDEN_DUE_TO_SECURITY_REASONS"
            }
        ],
        "clientToken": "4b1da830-fb59-4d7f-afcf-0108e576d9ab"
    },
    "responseElements": {
        "capabilityId": "ca-1111aaaa2222bbbb3",
        "name": "Integration Test EDI 214 Version 8 Update Capability",
        "type": "edi",
        "configuration": {
            "edi": {
                "type": {
                    "x12Details": {
                        "transactionSet": "HIDDEN_DUE_TO_SECURITY_REASONS",
                        "version": "HIDDEN_DUE_TO_SECURITY_REASONS"
                    }
                },
                "inputLocation": {
                    "bucketName": "HIDDEN_DUE_TO_SECURITY_REASONS",
                    "key": "HIDDEN_DUE_TO_SECURITY_REASONS"
                },
                "outputLocation": {
                    "bucketName": "HIDDEN_DUE_TO_SECURITY_REASONS",
                    "key": "HIDDEN_DUE_TO_SECURITY_REASONS"
                },
                "transformerId": "HIDDEN_DUE_TO_SECURITY_REASONS"
            }
        },
        "instructionsDocuments": [
            {
                "bucketName": "HIDDEN_DUE_TO_SECURITY_REASONS",
                "key": "HIDDEN_DUE_TO_SECURITY_REASONS"
            }
        ],
        "createdAt": "2023-11-24T17:27:05.196Z"
    },
    "requestID": "abcdefgh-8765-4321-abcd-111111111111",
    "eventID": "99999999-aaaa-1111-2222-zyxwvu987654",
    "readOnly": false,
    "eventType": "AwsApiCall",
    "managementEvent": true,
    "recipientAccountId": "{{recipient-account-id}}",
    "eventCategory": "Management",
    "tlsDetails": {
        "clientProvidedHostHeader": "b2bi.us-east-1.amazonaws.com"
    }
}
```