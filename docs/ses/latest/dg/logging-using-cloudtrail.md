# Logging Amazon SES API calls with AWS CloudTrail

Amazon SES is integrated with AWS CloudTrail, a service that provides a record of actions taken by a
user, role, or an AWS service in SES. CloudTrail captures API calls for SES as events.
The calls captured include calls from the SES console and code calls to the SES
API operations. If you create a trail, you can enable continuous delivery of CloudTrail events to an
Amazon S3 bucket, including events for SES. If you don't configure a trail, you can still view
the most recent events in the CloudTrail console in **Event history**. Using the
information collected by CloudTrail, you can determine the request that was made to SES, the IP
address from which the request was made, who made the request, when it was made, and additional
details.

To learn more about CloudTrail, including how to configure and enable it, see the [AWS CloudTrail User Guide](../../../awscloudtrail/latest/userguide.md "../../../awscloudtrail/latest/userguide.md").

## SES information in CloudTrail

CloudTrail is enabled on your AWS account when you create the account. When supported event
activity occurs in SES, that activity is recorded in a CloudTrail event along with other
AWS service events in **Event history**. You can view, search, and download
recent events in your AWS account. For more information, see [Viewing Events with CloudTrail Event
History](../../../awscloudtrail/latest/userguide/view-cloudtrail-events.md "../../../awscloudtrail/latest/userguide/view-cloudtrail-events.md").

For an ongoing record of events in your AWS account, including events for SES,
create a trail. A _trail_ enables CloudTrail to deliver log files to an Amazon S3
bucket. By default, when you create a trail in the console, the trail applies to all
AWS Regions. The trail logs events from all Regions in the AWS partition and delivers the
log files to the Amazon S3 bucket that you specify. Additionally, you can configure other AWS
services to further analyze and act upon the event data collected in CloudTrail logs. For more
information, see the following:

- [Overview for
  Creating a Trail](../../../awscloudtrail/latest/userguide/cloudtrail-create-and-update-a-trail.md "../../../awscloudtrail/latest/userguide/cloudtrail-create-and-update-a-trail.md")
- [CloudTrail Supported Services and Integrations](../../../awscloudtrail/latest/userguide/cloudtrail-aws-service-specific-topics.md#cloudtrail-aws-service-specific-topics-integrations "../../../awscloudtrail/latest/userguide/cloudtrail-aws-service-specific-topics.md#cloudtrail-aws-service-specific-topics-integrations")
- [Configuring Amazon SNS
  Notifications for CloudTrail](../../../awscloudtrail/latest/userguide/getting_notifications_top_level.md "../../../awscloudtrail/latest/userguide/getting_notifications_top_level.md")
- [Receiving CloudTrail Log Files from Multiple Regions](../../../awscloudtrail/latest/userguide/receive-cloudtrail-log-files-from-multiple-regions.md "../../../awscloudtrail/latest/userguide/receive-cloudtrail-log-files-from-multiple-regions.md") and [Receiving CloudTrail
  Log Files from Multiple Accounts](../../../awscloudtrail/latest/userguide/cloudtrail-receive-logs-from-multiple-accounts.md "../../../awscloudtrail/latest/userguide/cloudtrail-receive-logs-from-multiple-accounts.md")

Every event or log entry contains information about who generated the request. The
identity information helps you determine the following:

- Whether the request was made with root or AWS Identity and Access Management (IAM) user credentials.
- Whether the request was made with temporary security credentials for a role or
  federated user.
- Whether the request was made by another AWS service.

For more information, see the [CloudTrail userIdentity
Element](../../../awscloudtrail/latest/userguide/cloudtrail-event-reference-user-identity.md "../../../awscloudtrail/latest/userguide/cloudtrail-event-reference-user-identity.md").

## SES data events in CloudTrail

[Data events](../../../awscloudtrail/latest/userguide/logging-data-events-with-cloudtrail.md#logging-data-events "../../../awscloudtrail/latest/userguide/logging-data-events-with-cloudtrail.md#logging-data-events") provide information about the resource operations performed on or in a
resource. These are also known as data plane operations. Data events are often high-volume
activities. By default, CloudTrail doesn’t log data events. The CloudTrail event history doesn't record
data events.

Additional charges apply for data events. For more information about CloudTrail pricing, see
[AWS CloudTrail pricing](https://aws.amazon.com/cloudtrail/pricing/ "https://aws.amazon.com/cloudtrail/pricing/").

###### Note

Email sending activity via SES SMTP Interface is not logged to CloudTrail events. For
comprehensive activity logging, use the latest SES APIs in the [SES API Reference](../APIReference/API_Operations.md "../APIReference/API_Operations.md") and [SES API v2 Reference](../APIReference-V2/API_Operations.md "../APIReference-V2/API_Operations.md").

The following table lists the SES resource types for which you can log data events.
The _Data event type (console)_ column shows the value to choose from the
**Data event type** list on the CloudTrail console. The _resources.type
value_ column shows the `resources.type` value, which you would specify
when configuring advanced event selectors using the column shows the AWS CLI or CloudTrail APIs. The
_Data APIs logged to CloudTrail_ column shows the API calls logged to CloudTrail for
the resource type.

| SES resource types for data events | Data event type (console)  | resources.type value                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | Data APIs logged to CloudTrail |
| ---------------------------------- | -------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------ |
| SES identity                       | AWS::SES::EmailIdentity    | **SES:**<br>[SendEmail](../APIReference/API_SendEmail.md "../APIReference/API_SendEmail.md")<br>[SendRawEmail](../APIReference/API_SendRawEmail.md "../APIReference/API_SendRawEmail.md")<br>[SendTemplatedEmail](../APIReference/API_SendTemplatedEmail.md "../APIReference/API_SendTemplatedEmail.md")<br>[SendBulkTemplatedEmail](../APIReference/API_SendBulkTemplatedEmail.md "../APIReference/API_SendBulkTemplatedEmail.md")<br>**SES v2:**<br>[SendEmail](../APIReference-V2/API_SendEmail.md "../APIReference-V2/API_SendEmail.md")<br>[SendBulkEmail](../APIReference-V2/API_SendBulkEmail.md "../APIReference-V2/API_SendBulkEmail.md") |
| SES configuration set              | AWS::SES::ConfigurationSet |
| SES template                       | AWS::SES::Template         | **SES:**<br>[SendTemplatedEmail](../APIReference/API_SendTemplatedEmail.md "../APIReference/API_SendTemplatedEmail.md")<br>[SendBulkTemplatedEmail](../APIReference/API_SendBulkTemplatedEmail.md "../APIReference/API_SendBulkTemplatedEmail.md")<br>**SES v2:**<br>[SendEmail](../APIReference-V2/API_SendEmail.md "../APIReference-V2/API_SendEmail.md")<br>[SendBulkEmail](../APIReference-V2/API_SendBulkEmail.md "../APIReference-V2/API_SendBulkEmail.md")                                                                                                                                                                                  |

The following example shows how to log all data events for all SES email identities
by using the `--advanced-event-selectors` parameter:

```
aws cloudtrail put-event-selectors \
--region Region \
--trail-name TrailName \
--advanced-event-selectors
'[
    {
        "Name": "Log SES data plane actions for all email identities",
        "FieldSelectors": [
        { "Field": "eventCategory", "Equals": ["Data"] },
        { "Field": "resources.type", "Equals": ["AWS::SES::EmailIdentity"] }
       ]
    }
]'
```

You can further refine the advanced event selectors to filter on the
`eventName`, `readOnly`, and `resources.ARN` fields to log
only those events that are important to you. For more information about these fields, see
[AdvancedFieldSelector](../../../awscloudtrail/latest/APIReference/API_AdvancedFieldSelector.md "../../../awscloudtrail/latest/APIReference/API_AdvancedFieldSelector.md") in the
_AWS CloudTrail API Reference_. For more examples on how to log data events see [Logging data events](../../../awscloudtrail/latest/userguide/logging-data-events-with-cloudtrail.md "../../../awscloudtrail/latest/userguide/logging-data-events-with-cloudtrail.md") for
trails.

## CloudTrail log delivery scenarios for SES logging

CloudTrail delivers logs based on such factors as account and resource ownership, identity type,
and region. The following matrix explains to whom and where the logs would be delivered to
based on specific combinations of these factors.

| Scenario type                        | Account roles                                                                                 | Resources                                                                     | Request flow                                | Log delivery                                                                                                       |
| ------------------------------------ | --------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ------------------------------------------- | ------------------------------------------------------------------------------------------------------------------ |
| **Single cross-account**             | Account A:_resource owner_<br>Account B*: requester*                                          | Email identity                                                                | B → A's email identity                      | Logs delivered to both A and B                                                                                     |
| Feedback forwarding email            | B → A's feedback email                                                                        | Logs delivered to both A and B                                                |
| **Multiple cross-account**           | Account A:_feedback email owner_<br>Account B:_email identity owner_<br>Account C:_requester_ | Feedback email (A)<br>Email identity (B)                                      | C → A's feedback email + B's email identity | Logs delivered to A, B, and C                                                                                      |
| **Global endpoint (Single account)** | Account A:_owner & requester_                                                                 | Global endpoint (primary: *eu‑west‑1<br>• &<br>secondary: *us‑west‑2\*)       | A → Global endpoint                         | Logs delivered to A in region that processed the request (either<br>*eu‑west‑1<br>• or<br>*us‑west‑2\*)            |
| **Global endpoint (Cross-account)**  | Account A:_email identity owner_<br>Account B:_requester_                                     | Email identity (A)<br>Global endpoint (B) (*eu‑west‑1<br>• &<br>*us‑west‑2\*) | B → A's email identity via Global endpoint  | Logs delivered to both A and B in region that processed the request (either<br>*eu‑west‑1<br>• or<br>*us‑west‑2\*) |

###### Note

- CloudTrail always delivers logs to the requester account.
- Resource owners receive logs even if they didn't perform the operation.
- For Global endpoints, both accounts need CloudTrail subscriptions in all configured regions.
- During regional impairments, all logs appear in the healthy region.

## SES management events in CloudTrail

SES delivers management events to CloudTrail. Management events include actions that are
related to creating and managing resources within your AWS account. In Amazon SES,
management events include actions such as creating and deleting identities or receipt rules.
For more information about SES API operations, see the [SES API Reference](../APIReference/API_Operations.md "../APIReference/API_Operations.md") and [SES API v2 Reference](../APIReference-V2/API_Operations.md "../APIReference-V2/API_Operations.md").

## CloudTrail log file entries for SES

A trail is a configuration that enables delivery of events as log files to an Amazon S3
bucket that you specify. CloudTrail log files contain one or more log entries. An event represents a
single request from any source and includes information about the requested action, the date
and time of the action, request parameters, and so on. CloudTrail log files aren't an ordered stack
trace of the public API calls, so they don't appear in any specific order.

The following examples demonstrate CloudTrail logs of these event types:

###### Event types

- [DeleteIdentity](#DeleteIdentity "#DeleteIdentity")
- [VerifyEmailIdentity](#VerifyEmailIdentity "#VerifyEmailIdentity")
- [SendEmail with simple content](#SendEmail-with-simple-content "#SendEmail-with-simple-content")
- [SendEmail with templated content](#SendEmail-with-templated-content "#SendEmail-with-templated-content")

### DeleteIdentity

```
{
  "Records":[
    {
        "eventVersion": "1.11",
        "userIdentity": {
            "type": "AssumedRole",
            "principalId": "AROA4DO2KAWIPZEXAMPLE:myUserName",
            "arn": "arn:aws:sts::111122223333:assumed-role/users/myUserName",
            "accountId": "111122223333",
            "accessKeyId": "AKIAIOSFODNN7EXAMPLE",
            "sessionContext": {
                "sessionIssuer": {
                    "type": "Role",
                    "principalId": "AROA4DO2KAWIPZEXAMPLE",
                    "arn": "arn:aws:iam::111122223333:role/admin-role",
                    "accountId": "111122223333",
                    "userName": "myUserName"
                },
                "attributes": {
                    "creationDate": "2025-02-27T09:53:35Z",
                    "mfaAuthenticated": "false"
                }
            }
        },
        "eventTime": "2025-02-27T09:54:31Z",
        "eventSource": "ses.amazonaws.com",
        "eventName": "DeleteIdentity",
        "awsRegion": "us-east-1",
        "sourceIPAddress": "192.0.2.0",
        "userAgent": "aws-cli/2.23.4",
        "requestParameters": {
            "identity": "sender@example.com"
        },
        "responseElements": null,
        "requestID": "50b87bfe-ab23-11e4-9106-5b36376f9d12",
        "eventID": "0ffa308d-1467-4259-8be3-c749753be325",
        "readOnly": false,
        "eventType": "AwsApiCall",
        "managementEvent": true,
        "recipientAccountId": "111122223333",
        "eventCategory": "Management",
        "tlsDetails": {
            "tlsVersion": "TLSv1.3",
            "cipherSuite": "TLS_AES_128_GCM_SHA256",
            "clientProvidedHostHeader": "email.us-east-1.amazonaws.com"
        }
    }
  ]
}
```

### VerifyEmailIdentity

```
{
  "Records":[
    {
        "eventVersion": "1.11",
        "userIdentity": {
            "type": "AssumedRole",
            "principalId": "AROA4DO2KAWIPZEXAMPLE:myUserName",
            "arn": "arn:aws:sts::111122223333:assumed-role/users/myUserName",
            "accountId": "111122223333",
            "accessKeyId": "AKIAIOSFODNN7EXAMPLE",
            "sessionContext": {
                "sessionIssuer": {
                    "type": "Role",
                    "principalId": "AROA4DO2KAWIPZEXAMPLE",
                    "arn": "arn:aws:iam::111122223333:role/admin-role",
                    "accountId": "111122223333",
                    "userName": "myUserName"
                },
                "attributes": {
                    "creationDate": "2025-02-27T09:53:35Z",
                    "mfaAuthenticated": "false"
                }
            }
        },
        "eventTime": "2025-02-27T09:56:20Z",
        "eventSource": "ses.amazonaws.com",
        "eventName": "VerifyEmailIdentity",
        "awsRegion": "us-east-1",
        "sourceIPAddress": "192.0.2.0",
        "userAgent": "aws-cli/2.23.4",
        "requestParameters": {
            "emailAddress": "sender@example.com"
        },
        "responseElements": null,
        "requestID": "eb2ff803-ac09-11e4-8ff5-a56a3119e253",
        "eventID": "5613b0ff-d6c6-4526-9b53-a603a9231725",
        "readOnly": false,
        "eventType": "AwsApiCall",
        "managementEvent": true,
        "recipientAccountId": "111122223333",
        "eventCategory": "Management",
        "tlsDetails": {
            "tlsVersion": "TLSv1.3",
            "cipherSuite": "TLS_AES_128_GCM_SHA256",
            "clientProvidedHostHeader": "email.us-east-1.amazonaws.com"
        }
    }
  ]
}
```

### SendEmail with simple content

```
{
  "Records":[{
       "eventTime": "2025-01-24T11:43:00Z",
        "eventSource": "ses.amazonaws.com",
        "eventName": "SendEmail",
        "awsRegion": "us-east-1",
        "sourceIPAddress": "192.0.2.0",
        "userAgent": "aws-cli/2.23.4 md/awscrt#0.23.4",
        "requestParameters": {
            "destination": {
                "bccAddresses": ["HIDDEN_DUE_TO_SECURITY_REASONS"],
                "toAddresses": ["HIDDEN_DUE_TO_SECURITY_REASONS"],
                "ccAddresses": ["HIDDEN_DUE_TO_SECURITY_REASONS"]
            },
            "message": {
                "subject": {
                    "charset": "UTF-8",
                    "data": "HIDDEN_DUE_TO_SECURITY_REASONS"
                },
                "body": {
                    "html": {
                        "charset": "UTF-8",
                        "data": "HIDDEN_DUE_TO_SECURITY_REASONS"
                    },
                    "text": {
                        "charset": "UTF-8",
                        "data": "HIDDEN_DUE_TO_SECURITY_REASONS"
                    }
                }
            },
            "source": "sender@example.com"
        },
        "responseElements": null,
        "additionalEventData": {
            "sesMessageId": "01000100a11a11aa-00aa0a00-00a0-48a8-aaa7-a174a83b456a-000000"
        },
        "requestID": "ab2cc803-ac09-11d7-8bb8-a56a3119e476",
        "eventID": "eb834e01-f168-435f-92c0-c36278378b6e",
        "readOnly": true,
        "resources": [{
            "accountId": "111122223333",
            "type": "AWS::SES::EmailIdentity",
            "ARN": "arn:aws:ses:us-east-1:111122223333:identity/sender@example.com"
        }],
        "eventType": "AwsApiCall",
        "managementEvent": false,
        "recipientAccountId": "111122223333",
        "eventCategory": "Data",
        "tlsDetails": {
            "tlsVersion": "TLSv1.3",
            "cipherSuite": "TLS_AES_128_GCM_SHA256",
            "clientProvidedHostHeader": "email.us-east-1.amazonaws.com"
        }
    }
  ]
}
```

### SendEmail with templated content

```
{
        "eventVersion": "1.11",
        "userIdentity": {
            "type": "AssumedRole",
            "principalId": "AROA4DO2KAWIPZEXAMPLE:myUserName",
            "arn": "arn:aws:sts::111122223333:assumed-role/users/myUserName",
            "accountId": "111122223333",
            "accessKeyId": "AKIAIOSFODNN7EXAMPLE",
            "sessionContext": {
                "sessionIssuer": {
                    "type": "Role",
                    "principalId": "AROA4DO2KAWIPZEXAMPLE",
                    "arn": "arn:aws:iam::111122223333:role/admin-role",
                    "accountId": "111122223333",
                    "userName": "admin-role"
                },
                "attributes": {
                    "creationDate": "2025-03-05T18:51:06Z",
                    "mfaAuthenticated": "false"
                }
            }
        },
        "eventTime": "2025-03-05T19:16:29Z",
        "eventSource": "ses.amazonaws.com",
        "eventName": "SendEmail",
        "awsRegion": "us-east-1",
        "sourceIPAddress": "192.0.2.0",
        "userAgent": "aws-cli/2.23.4",
        "requestParameters": {
            "fromEmailAddress": "sender@example.com",
            "destination": {
                "toAddresses": ["HIDDEN_DUE_TO_SECURITY_REASONS"],
                "bccAddresses": ["HIDDEN_DUE_TO_SECURITY_REASONS"],
                "ccAddresses": ["HIDDEN_DUE_TO_SECURITY_REASONS"]
            },
            "emailTags": [{
                "value": "test",
                "name": "campaign"
            }, {
                "value": "cli-test",
                "name": "sender"
            }],
            "replyToAddresses": ["HIDDEN_DUE_TO_SECURITY_REASONS"],
            "content": {
                "template": {
                    "templateData": "HIDDEN_DUE_TO_SECURITY_REASONS",
                    "templateName": "TestTemplate"
                }
            }
        },
        "responseElements": null,
        "additionalEventData": {
            "sesMessageId": "01000100a11a11aa-00aa0a00-00a0-48a8-aaa7-a174a83b456a-000000"
        },
        "requestID": "50b87bfe-ab23-11e4-9106-5b36376f9d12",
        "eventID": "0ffa308d-1467-4259-8be3-c749753be325",
        "readOnly": true,
        "resources": [{
            "accountId": "111122223333",
            "type": "AWS::SES::EmailIdentity",
            "ARN": "arn:aws:ses:us-east-1:111122223333:identity/sender@example.com"
        }, {
            "accountId": "111122223333",
            "type": "AWS::SES::Template",
            "ARN": "arn:aws:ses:us-east-1:111122223333:template/TestTemplate"
        }],
        "eventType": "AwsApiCall",
        "managementEvent": false,
        "recipientAccountId": "111122223333",
        "eventCategory": "Data",
        "tlsDetails": {
            "tlsVersion": "TLSv1.3",
            "cipherSuite": "TLS_AES_128_GCM_SHA256",
            "clientProvidedHostHeader": "email.us-east-1.amazonaws.com"
        }
    }
```
