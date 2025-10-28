# Logging AWS re:Post Private API calls using AWS CloudTrail

AWS re:Post Private is integrated with AWS CloudTrail, a service that provides a record of actions
taken by a user, role, or an AWS service in re:Post Private. CloudTrail captures all API calls for
re:Post Private as events. The calls captured include calls from the re:Post Private console and
code calls to the re:Post Private API operations. If you create a trail, you can enable
continuous delivery of CloudTrail events to an Amazon S3 bucket, including events for re:Post Private. If
you don't configure a trail, you can still view the most recent events in the CloudTrail console
in **Event history**. Using the information collected by CloudTrail, you can
determine the request that was made to re:Post Private, the IP address from which the request
was made, who made the request, when it was made, and additional details.

To learn more about CloudTrail, see the [AWS CloudTrail User Guide](../../../awscloudtrail/latest/userguide/cloudtrail-user-guide.md "../../../awscloudtrail/latest/userguide/cloudtrail-user-guide.md").

## re:Post Private information in CloudTrail

CloudTrail is enabled on your AWS account when you create the account. When activity occurs
in re:Post Private, that activity is recorded in a CloudTrail event along with other AWS service events
in **Event history**. You can view, search, and download recent events in
your AWS account. For more information, see [Working with CloudTrail Event history](../../../awscloudtrail/latest/userguide/view-cloudtrail-events.md "../../../awscloudtrail/latest/userguide/view-cloudtrail-events.md").

For an ongoing record of events in your AWS account, including events for re:Post Private,
create a trail. A _trail_ enables CloudTrail to deliver log files to an Amazon S3 bucket.
By default, when you create a trail in the console, the trail applies to all AWS Regions. The trail
logs events from all Regions in the AWS partition and delivers the log files to the Amazon S3 bucket
that you specify. Additionally, you can configure other AWS services to further analyze and act
upon the event data collected in CloudTrail logs. For more information, see the following:

- [Creating a trail for your AWS account](../../../awscloudtrail/latest/userguide/cloudtrail-create-and-update-a-trail.md "../../../awscloudtrail/latest/userguide/cloudtrail-create-and-update-a-trail.md")
- [CloudTrail supported services and integrations](../../../awscloudtrail/latest/userguide/cloudtrail-aws-service-specific-topics.md "../../../awscloudtrail/latest/userguide/cloudtrail-aws-service-specific-topics.md")
- [Configuring Amazon SNS notifications
  for CloudTrail](../../../awscloudtrail/latest/userguide/configure-sns-notifications-for-cloudtrail.md "../../../awscloudtrail/latest/userguide/configure-sns-notifications-for-cloudtrail.md")
- [Receiving CloudTrail log
  files from multiple Regions](../../../awscloudtrail/latest/userguide/receive-cloudtrail-log-files-from-multiple-regions.md "../../../awscloudtrail/latest/userguide/receive-cloudtrail-log-files-from-multiple-regions.md") and [Receiving CloudTrail log
  files from multiple accounts](../../../awscloudtrail/latest/userguide/cloudtrail-receive-logs-from-multiple-accounts.md "../../../awscloudtrail/latest/userguide/cloudtrail-receive-logs-from-multiple-accounts.md")

All re:Post Private actions are logged by CloudTrail and are documented in the [AWS re:Post Private API Reference](../APIReference/Welcome.md "../APIReference/Welcome.md"). re:Post Private supports logging the following actions as events in CloudTrail log files:

- [CreateSpace](../APIReference/API_CreateSpace.md "../APIReference/API_CreateSpace.md")
- [DeleteSpace](../APIReference/API_DeleteSpace.md "../APIReference/API_DeleteSpace.md")
- [DeregisterAdmin](../APIReference/API_DeregisterAdmin.md "../APIReference/API_DeregisterAdmin.md")
- [GetSpace](../APIReference/API_GetSpace.md "../APIReference/API_GetSpace.md")
- [ListSpaces](../APIReference/APIListSpaces.md "../APIReference/APIListSpaces.md")
- [ListTagsForResource](../APIReference/API_ListTagsForResource.md "../APIReference/API_ListTagsForResource.md")
- [RegisterAdmin](../APIReference/API_RegisterAdmin.md "../APIReference/API_RegisterAdmin.md")
- [SendInvites](../APIReference/API_SendInvites.md "../APIReference/API_SendInvites.md")
- [TagResource](../APIReference/API_TagResource.md "../APIReference/API_TagResource.md")
- [UntagResource](../APIReference/API_UntagResource.md "../APIReference/API_UntagResource.md")
- [UpdateSpace](../APIReference/API_UpdateSpace.md "../APIReference/API_UpdateSpace.md")

re:Post Private supports logging the following Support actions as events in the CloudTrail log files:

- [CreateCase](../../../awssupport/latest/APIReference/API_CreateCase.md "../../../awssupport/latest/APIReference/API_CreateCase.md")
- [AddCommunicationToCase](../../../awssupport/latest/APIReference/API_AddCommunicationToCase.md "../../../awssupport/latest/APIReference/API_AddCommunicationToCase.md")
- [ResolveCase](../../../awssupport/latest/APIReference/API_ResolveCase.md "../../../awssupport/latest/APIReference/API_ResolveCase.md")

Every event or log entry contains information about who generated the request. The
identity information helps you determine the following:

- Whether the request was made with root or AWS Identity and Access Management (IAM) user credentials.
- Whether the request was made with temporary security credentials for a role or
  federated user.
- Whether the request was made by another AWS service.

For more information, see the [CloudTrail userIdentity
element](../../../awscloudtrail/latest/userguide/cloudtrail-event-reference-user-identity.md "../../../awscloudtrail/latest/userguide/cloudtrail-event-reference-user-identity.md").

## Understanding re:Post Private log file entries

A trail is a configuration that enables delivery of events as log files to an Amazon S3 bucket
that you specify. CloudTrail log files contain one or more log entries. An event represents a single
request from any source and includes information about the requested action, the date and time
of the action, request parameters, and so on. CloudTrail log files aren't an ordered stack trace of
the public API calls, so they don't appear in any specific order.

The following example shows a CloudTrail log entry that demonstrates the `CreateSpace` action.

```

 {
    "eventVersion": "1.08",
    "userIdentity": {
        "type": "AssumedRole",
        "principalId": "AROAQM47QIR7WLEXAMPLE:user",
        "arn": "arn:aws:sts::123456789012:assumed-role/User/user",
        "accountId": "123456789012",
        "accessKeyId": "EXAMPLE_KEY_ID",
        "sessionContext": {
            "sessionIssuer": {
                "type": "Role",
                "principalId": "AROAQM47QIR7WLEXAMPLE",
                "arn": "arn:aws:iam::123456789012:role/User",
                "accountId": "123456789012",
                "userName": "User"
            },
            "webIdFederationData": {},
            "attributes": {
                "creationDate": "2023-11-06T19:24:39Z",
                "mfaAuthenticated": "false"
            }
        }
    },
    "eventTime": "2023-11-06T21:37:44Z",
    "eventSource": "repostspace.amazonaws.com",
    "eventName": "CreateSpace",
    "awsRegion": "us-west-2",
    "sourceIPAddress": "205.251.233.176",
    "userAgent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36",
    "requestParameters": {
        "spaceName": "Test space name",
        "spaceSubdomain": "customsubdomain",
        "tagSet": {},
        "tier": "2000",
        "roleArn": "",
        "spaceDescription": "Test space description"
    },
    "responseElements": {
        "spaceId": "SPLPWvQmv9SIWYF30EXAMPLE",
        "Access-Control-Expose-Headers": "x-amzn-errortype, x-amzn-requestid, x-amzn-errormessage, x-amzn-trace-id, x-amz-apigw-id, date"
    },
    "requestID": "71d815e0-6632-4ec9-9fac-92af3e4a86dc",
    "eventID": "30a6c3da-ce2e-4931-ba5d-b3cc7cf16ec8",
    "readOnly": false,
    "eventType": "AwsApiCall",
    "managementEvent": true,
    "recipientAccountId": "123456789012",
    "eventCategory": "Management"
}

```

The following example shows a CloudTrail log entry that demonstrates the `RegisterAdmin` action.

```

 {
    "eventVersion": "1.08",
    "userIdentity": {
        "type": "AssumedRole",
        "principalId": "AROAQM47QIR7WLEXAMPLE:user",
        "arn": "arn:aws:sts::123456789012:assumed-role/User/user",
        "accountId": "123456789012",
        "accessKeyId": "EXAMPLE_KEY_ID",
        "sessionContext": {
            "sessionIssuer": {
                "type": "Role",
                "principalId": "AROAQM47QIR7WLEXAMPLE",
                "arn": "arn:aws:iam::123456789012:role/User",
                "accountId": "123456789012",
                "userName": "User"
            },
            "webIdFederationData": {},
            "attributes": {
                "creationDate": "2023-11-07T21:17:19Z",
                "mfaAuthenticated": "false"
            }
        }
    },
    "eventTime": "2023-11-07T21:24:23Z",
    "eventSource": "repostspace.amazonaws.com",
    "eventName": "RegisterAdmin",
    "awsRegion": "us-west-2",
    "sourceIPAddress": "205.251.233.183",
    "userAgent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36",
    "requestParameters": {
        "adminId": "08612310-a0f1-7063-3e54-fb2960444dd1",
        "spaceId": "SPlYNZE-ylQEmAXpmEXAMPLE"
    },
    "responseElements": {
        "Access-Control-Expose-Headers": "x-amzn-errortype, x-amzn-requestid, x-amzn-errormessage, x-amzn-trace-id, x-amz-apigw-id, date"
    },
    "requestID": "9939ebbe-8599-4f9a-827b-4995e3006001",
    "eventID": "e1873b18-f80c-4934-9ff2-bf5b35c78031",
    "readOnly": false,
    "eventType": "AwsApiCall",
    "managementEvent": true,
    "recipientAccountId": "123456789012",
    "eventCategory": "Management"
}

```

The following example shows a CloudTrail log entry that demonstrates the `ListSpaces` action.

```

 {
    "eventVersion": "1.08",
    "userIdentity": {
        "type": "AssumedRole",
        "principalId": "AROAQM47QIR7WLEXAMPLE:user",
        "arn": "arn:aws:sts::123456789012:assumed-role/User/user",
        "accountId": "123456789012",
        "accessKeyId": "EXAMPLE_KEY_ID",
        "sessionContext": {
            "sessionIssuer": {
                "type": "Role",
                "principalId": "AROAQM47QIR7WLEXAMPLE",
                "arn": "arn:aws:iam::123456789012:role/User",
                "accountId": "123456789012",
                "userName": "User"
            },
            "webIdFederationData": {},
            "attributes": {
                "creationDate": "2023-11-09T22:28:23Z",
                "mfaAuthenticated": "false"
            }
        }
    },
    "eventTime": "2023-11-09T22:38:34Z",
    "eventSource": "repostspace.amazonaws.com",
    "eventName": "ListSpaces",
    "awsRegion": "us-west-2",
    "sourceIPAddress": "205.251.233.176",
    "userAgent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
    "requestParameters": null,
    "responseElements": null,
    "requestID": "95be587b-c04f-4eb0-9269-12fee33ae2e3",
    "eventID": "9777da32-545f-44c4-af0b-1d9109b8cbc3",
    "readOnly": true,
    "eventType": "AwsApiCall",
    "managementEvent": true,
    "recipientAccountId": "123456789012",
    "eventCategory": "Management"
}

```

The following example shows a CloudTrail log entry that demonstrates the `ResolveCase` action. You can use the `sourceIdentity` element in this log entry to identify the user that resolved the case.

```
 {
    "eventVersion": "1.09",
    "userIdentity": {
        "type": "AssumedRole",
        "principalId": "AROAQM47QIR76DQZ7N5WX:create-support-case-Uk1iHNTWQEOLmR2BR1FDJQ",
        "arn": "arn:aws:sts::123456789012:assumed-role/AWSRepostSpaceRole/create-support-case-Uk1iHNTWQEOLmR2BR1FDJQ",
        "accountId": "123456789012",
        "accessKeyId": "EXAMPLE_KEY_ID",
        "sessionContext": {
            "sessionIssuer": {
                "type": "Role",
                "principalId": "AROAQM47QIR76DQZ7N5WX",
                "arn": "arn:aws:iam::123456789012:role/AWSRepostSpaceRole",
                "accountId": "123456789012",
                "userName": "AWSRepostSpaceRole"
            },
            "attributes": {
                "creationDate": "2023-11-17T21:46:42Z",
                "mfaAuthenticated": "false"
            },
            "sourceIdentity": "28e17330-10f1-705d-7cba-3a62a6b10e2e"
        }
    },
    "eventTime": "2023-11-17T21:46:44Z",
    "eventSource": "support.amazonaws.com",
    "eventName": "ResolveCase",
    "awsRegion": "us-west-2",
    "sourceIPAddress": "54.68.27.29",
    "userAgent": "aws-sdk-nodejs/2.1363.0 linux/v16.20.2 exec-env/AWS_ECS_FARGATE promise",
    "requestParameters": {
        "caseId": "case-123456789012-muen-2023-75d2c35481b96357"
    },
    "responseElements": {
        "initialCaseStatus": "unassigned",
        "finalCaseStatus": "resolved"
    },
    "requestID": "594b91c6-df1c-47e4-a834-d67d67f34b9d",
    "eventID": "7fc9cbe4-c8d5-4d61-a016-e076de272fff",
    "readOnly": false,
    "eventType": "AwsApiCall",
    "managementEvent": true,
    "recipientAccountId": "111111111111",
    "eventCategory": "Management",
    "tlsDetails": {
        "clientProvidedHostHeader": "support.us-west-2.amazonaws.com"
    }
}

```
