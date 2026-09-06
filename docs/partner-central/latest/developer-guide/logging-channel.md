

The AWS Partner Central API Reference was restructured. For more information about the supported API operations, see the [AWS Partner Central API Reference](https://docs.aws.amazon.com/partner-central/latest/APIReference/Welcome.html).

# Logging the AWS Partner Central Channel API
<a name="logging-channel"></a>

 [AWS CloudTrail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-user-guide.html) is a service that enables governance, compliance, operational auditing, and risk auditing of your AWS account. With AWS CloudTrail, you can log, continuously monitor, and retain account activity related to actions across your AWS infrastructure. AWS Partner Central Channel API activity is recorded as events in CloudTrail. You can create a trail, a configuration that enables delivery of events as log files to an Amazon S3 bucket. 

## Overview
<a name="overview-channel"></a>

 The AWS Partner Central Channel API is integrated with AWS CloudTrail, a service that provides a record of actions taken by a user, role, or an AWS service in AWS Partner Central. CloudTrail captures all API calls for AWS Partner Central Channel API as events. The calls captured include calls from the AWS Partner Central and from code calls to the AWS Partner Central Channel API operations. 

 If you create a trail, you can enable continuous delivery of CloudTrail events to an Amazon S3 bucket, including events for AWS Partner Central Channel API. If you don't configure a trail, you can still view the most recent events in the CloudTrail console in Event history. 

 Using the information collected by CloudTrail, you can determine the request that was made to AWS Partner Central Channel API, the IP address from which the request was made, who made the request, when it was made, and additional details. 

## Understanding AWS Partner Central Channel API log file entries
<a name="understanding-aws-partner-central-channel-log-file-entries"></a>

 A trail is a configuration that enables delivery of events as log files to an Amazon S3 bucket. When your trail tracks AWS Partner Central Channel API events, CloudTrail processes the events as log files across all the regions. Each log file can contain one or more events. 

 The following example shows a CloudTrail log entry that demonstrates the `CreateProgramManagementAccount` action on AWS Partner Central Channel API: 

```
{
    "eventVersion": "1.11",
    "userIdentity": {
        "type": "AssumedRole",
        "principalId": "AROAEXAMPLE52AGFT725JGDZ:example-user-Isengard",
        "arn": "arn:aws:sts::123456789012:assumed-role/Admin/example-user-Isengard",
        "accountId": "123456789012",
        "accessKeyId": "ASIAEXAMPLE52AGL6IXQLZ5",
        "sessionContext": {
            "sessionIssuer": {
                "type": "Role",
                "principalId": "AROAEXAMPLE52AGFT725JGDZ",
                "arn": "arn:aws:iam::123456789012:role/ExampleRole",
                "accountId": "123456789012",
                "userName": "ExampleRole"
            },
            "attributes": {
                "creationDate": "2025-10-21T17:06:47Z",
                "mfaAuthenticated": "false"
            }
        }
    },
    "eventTime": "2025-10-21T17:07:26Z",
    "eventSource": "partnercentral-channel.amazonaws.com",
    "eventName": "CreateProgramManagementAccount",
    "awsRegion": "us-east-1",
    "sourceIPAddress": "127.0.0.1",
    "userAgent": "PostmanRuntime/7.18.0",
    "requestParameters": {
        "catalog": "AWS",
        "program": "SOLUTION_PROVIDER",
        "displayName": "ExampleDisplayName",
        "accountId": "987654321098",
        "clientToken": "abcdef12-3456-7890-bcde-f123456789ab"
    },
    "responseElements": {
        "programManagementAccountDetail": {
            "id": "pma-example123456789",
            "arn": "arn:aws:partnercentral:us-east-1:123456789012:catalog/AWS/program-management-account/pma-example123456789"
        }
    },
    "requestID": "12345678-1234-5678-9abc-def012345678",
    "eventID": "87654321-4321-8765-cba9-fed098765432",
    "readOnly": false,
    "resources": [
        {
            "accountId": "123456789012",
            "type": "AWS::PartnerCentralChannel::ProgramManagementAccount",
            "ARN": "arn:aws:partnercentral:us-east-1:123456789012:catalog/AWS/program-management-account/pma-example123456789"
        }
    ],
    "eventType": "AwsApiCall",
    "managementEvent": true,
    "recipientAccountId": "123456789012",
    "eventCategory": "Management",
    "tlsDetails": {
        "clientProvidedHostHeader": "partnercentral-channel.global.api.aws"
    }
}
```

 In this example, the `CreateProgramManagementAccount` action was called by the IAM role named ExampleRole through an assumed role session. The request was made on October 21, 2025 at 17:07:26 UTC. The request created a new Program Management Account with ID `pma-example123456789` for the Solution Provider program. 

## Fields in AWS Partner Central Channel API log file entries
<a name="fields-in-aws-partner-central-channel-log-file-entries"></a>

 Each entry in a CloudTrail log file contains information about who made a request, the resources acted upon in the request, and the response elements returned by AWS Partner Central Channel API. The list of fields in a log entry, such as `eventVersion`, `userIdentity`, and `eventTime`, provide detailed information about the action. For example, the `sourceIPAddress` field shows the IP address that the request was made from. 