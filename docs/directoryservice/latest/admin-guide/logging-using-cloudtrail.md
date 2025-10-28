# Logging AWS Directory Service Data API calls using

AWS CloudTrail

AWS Directory Service Data integrates with AWS CloudTrail, a service that provides a record of actions taken by
a user, role, or an AWS service in Directory Service Data. CloudTrail captures all API calls for Directory Service Data as
events. The calls captured include calls from the Directory Service Data console and code calls to Directory Service Data
API operations. If you create a trail, you can enable continuous delivery of CloudTrail events to
an Amazon S3 bucket, including events for Directory Service Data. Using the information collected by CloudTrail, you
can determine the request that was made to Directory Service Data, the IP address from which the request was
made, who made the request, when it was made, and additional details.

To learn more about CloudTrail, see the [AWS CloudTrail User Guide](../../../awscloudtrail/latest/userguide/cloudtrail-user-guide.md "../../../awscloudtrail/latest/userguide/cloudtrail-user-guide.md").

## Directory Service Data information in CloudTrail

CloudTrail is enabled on your AWS account when you create the account. When supported
event activity (management events) occurs in Directory Service Data, that activity is recorded in a CloudTrail
event along with other AWS service events in **Event history**. You
can view, search, and download the last 90 days of management events in your
AWS account. For more information, see [Viewing events with CloudTrail Event history](../../../awscloudtrail/latest/userguide/view-cloudtrail-events.md "../../../awscloudtrail/latest/userguide/view-cloudtrail-events.md"). There is no
charge for viewing the **Event history**.

For an ongoing record of events in your AWS account, including events for Directory Service Data,
create a trail. A _trail_ enables CloudTrail to deliver log files to an
Amazon S3 bucket. By default, when you create a trail in the console, the trail applies to
all AWS Regions. The trail logs events from all Regions in the AWS partition and
delivers the log files to the Amazon S3 bucket that you specify. Additionally, you can
configure other AWS services to further analyze and act upon the event data collected
in CloudTrail logs. For more information, see the following:

- [Overview for creating a trail](../../../awscloudtrail/latest/userguide/cloudtrail-create-and-update-a-trail.md "../../../awscloudtrail/latest/userguide/cloudtrail-create-and-update-a-trail.md")
- [CloudTrail supported services and integrations](../../../awscloudtrail/latest/userguide/cloudtrail-aws-service-specific-topics.md "../../../awscloudtrail/latest/userguide/cloudtrail-aws-service-specific-topics.md")
- [Configuring Amazon SNS notifications for
  CloudTrail](../../../awscloudtrail/latest/userguide/configure-sns-notifications-for-cloudtrail.md "../../../awscloudtrail/latest/userguide/configure-sns-notifications-for-cloudtrail.md")
- [Receiving CloudTrail log files from multiple regions](../../../awscloudtrail/latest/userguide/receive-cloudtrail-log-files-from-multiple-regions.md "../../../awscloudtrail/latest/userguide/receive-cloudtrail-log-files-from-multiple-regions.md")
  and [Receiving CloudTrail log files from multiple
  accounts](../../../awscloudtrail/latest/userguide/cloudtrail-receive-logs-from-multiple-accounts.md "../../../awscloudtrail/latest/userguide/cloudtrail-receive-logs-from-multiple-accounts.md")

All Directory Service Data actions are logged by CloudTrail and are documented in the [Directory Service Data API Reference](../../../directoryservicedata/latest/DirectoryServiceDataAPIReference/welcome.md "../../../directoryservicedata/latest/DirectoryServiceDataAPIReference/welcome.md"). For example, calls to the
`AddGroupMember`, `DescribeUser` and `SearchGroups`
actions generate entries in the CloudTrail log files.

Every event or log entry contains information about who generated the request. The
identity information helps you determine the following:

- Whether the request was made with root or AWS Identity and Access Management (IAM) user
  credentials.
- Whether the request was made with temporary security credentials for a role or
  federated user.
- Whether the request was made by another AWS service.

For more information, see the [CloudTrail userIdentity element](../../../awscloudtrail/latest/userguide/cloudtrail-event-reference-user-identity.md "../../../awscloudtrail/latest/userguide/cloudtrail-event-reference-user-identity.md").

## Understanding Directory Service Data log file

entries

A trail is a configuration that enables delivery of events as log files to an Amazon S3
bucket that you specify. CloudTrail log files contain one or more log entries. An event
represents a single request from any source and includes information about the requested
action, the date and time of the action, request parameters, and so on. CloudTrail log files
aren't an ordered stack trace of the public API calls, so they don't appear in any
specific order.

The following example shows a CloudTrail log entry that demonstrates the [CreateUser](../../../directoryservicedata/latest/DirectoryServiceDataAPIReference/API_CreateUser.md "../../../directoryservicedata/latest/DirectoryServiceDataAPIReference/API_CreateUser.md") action.

```
{
      "eventVersion": "1.08",
      "userIdentity": {
        "type": "AssumedRole",
        "principalId": "1234567890abcdef0:admin-role",
        "arn": "arn:aws:sts::111222333444:assumed-role/AdAdmin/admin-role",
        "accountId": "111222333444",
        "accessKeyId": "021345abcdef6789",
        "sessionContext": {
          "sessionIssuer": {
            "type": "Role",
            "principalId": "1234567890abcdef0",
            "arn": "arn:aws:iam::111222333444:role/AdAdmin",
            "accountId": "111222333444",
            "userName": "AdAdmin"
          },
          "attributes": {
            "creationDate": "2023-05-30T18:22:38Z",
            "mfaAuthenticated": "false"
          }
        }
      },
      "eventTime": "2023-05-30T19:17:03Z",
      "eventSource": "ds.amazonaws.com",
      "eventName": "CreateUser",
      "awsRegion": "ap-northeast-2",
      "sourceIPAddress": ": 10.24.34.0",
      "userAgent": "aws-cli/2.9.20 Python/3.11.1 Darwin/21.6.0 source/x86_64 prompt/off command/ds-data.create-user",
      "requestParameters": {
        "directoryId": "d-1234567890",
        "sAMAccountName": "johnsmith",
        "clientToken": "example_token"
        "emailAddress": "HIDDEN_DUE_TO_SECURITY_REASONS",
        "givenName": "HIDDEN_DUE_TO_SECURITY_REASONS",
        "surname": "HIDDEN_DUE_TO_SECURITY_REASONS",
        "otherAttributes": {
          "physicalDeliveryOfficeName": {
            "s": "HIDDEN_DUE_TO_SECURITY_REASONS"
          },
          "telephoneNumber": {
            "s": "HIDDEN_DUE_TO_SECURITY_REASONS"
          },
          "streetAddress": {
            "s": "HIDDEN_DUE_TO_SECURITY_REASONS"
          },
          "displayName": {
            "s": "HIDDEN_DUE_TO_SECURITY_REASONS"
          },
          "homePhone": {
            "s": "HIDDEN_DUE_TO_SECURITY_REASONS"
          },
          "postalCode": {
            "s": "HIDDEN_DUE_TO_SECURITY_REASONS"
          },
          "description": {
            "s": "HIDDEN_DUE_TO_SECURITY_REASONS"
          }
        },
        "clientToken": "createUserToken4"
      },
      "responseElements": {
        "directoryId": "d-1234567890",
        "sID": "S-1-5-21-1234567890-123456789-123456789-1234",
        "sAMAccountName": "johnsmith"
      },
      "additionalEventData": {
        "SID": "S-1-5-21-1234567890-123456789-123456789-1234"
      },
      "requestID": "4567ab89-c12d-3333-2222-1e0012f34a7c",
      "eventID": "1234567b-f0a0-12ab-3c45-d678900d1255",
      "readOnly": false,
      "resources": [
        {
          "accountId": "111222333444",
          "type": "AWS::DirectoryService::MicrosoftAD",
          "ARN": "arn:aws:ds:ap-northeast-2:111222333444:directory/d-1234567890"
        }
      ],
      "eventType": "AwsApiCall",
      "managementEvent": true,
      "recipientAccountId": "111222333444",
      "eventCategory": "Management",
      "tlsDetails": {
        "tlsVersion": "TLSv1.3",
        "cipherSuite": "TLS_AES_128_GCM_SHA256",
        "clientProvidedHostHeader": "ds-data.ap-northeast-2.amazonaws.com"
      }
},
```

The following example shows a CloudTrail log entry that demonstrates the [ListUsers](../../../directoryservicedata/latest/DirectoryServiceDataAPIReference/API_ListUsers.md "../../../directoryservicedata/latest/DirectoryServiceDataAPIReference/API_ListUsers.md") action.

Actions that do not create or modify an object return a null response.

```
{
    "eventVersion": "1.08",
    "userIdentity": {
        "type": "AssumedRole",
        "principalId": "1234567890abcdef0:admin-role",
        "arn": "arn:aws:sts::111222333444:assumed-role/AdAdmin/admin-role",
        "accountId": "111222333444",
        "accessKeyId": "021345abcdef6789",
        "sessionContext": {
            "sessionIssuer": {
                "type": "Role",
                "principalId": "1234567890abcdef0",
                "arn": "arn:aws:iam::111222333444:role/AdAdmin",
                "accountId": "111222333444",
                "userName": "AdAdmin"
            },
            "attributes": {
                "creationDate": "2023-05-30T18:22:38Z",
                "mfaAuthenticated": "false"
            }
        }
    },
    "eventTime": "2023-05-30T18:22:52Z",
    "eventSource": "ds.amazonaws.com",
    "eventName": "ListUsers",
    "awsRegion": "ap-northeast-2",
    "sourceIPAddress": "10.24.34.0",
    "userAgent": "aws-cli/2.9.20 Python/3.11.1 Darwin/21.6.0 source/x86_64 prompt/off command/ds-data.list-users",
    "requestParameters": {
        "directoryId": "d-1234567890",
        "maxResults": 1
    },
    "responseElements": null,
    "requestID": "4567ab89-c12d-3333-2222-1e0012f34a7c",
    "eventID": "1234567b-f0a0-12ab-3c45-d678900d1244",
    "readOnly": true,
    "resources": [
        {
            "accountId": "111222333444",
            "type": "AWS::DirectoryService::MicrosoftAD",
            "ARN": "arn:aws:ds:ap-northeast-2:111222333444:directory/d-1234567890"
        }
    ],
    "eventType": "AwsApiCall",
    "managementEvent": true,
    "recipientAccountId": "111222333444",
    "eventCategory": "Management",
    "tlsDetails": {
        "tlsVersion": "TLSv1.3",
        "cipherSuite": "TLS_AES_128_GCM_SHA256",
        "clientProvidedHostHeader": "ds-data.ap-northeast-2.amazonaws.com"
    }
}
```

The following example shows a CloudTrail log entry that demonstrates the [ListGroups](../../../directoryservicedata/latest/DirectoryServiceDataAPIReference/API_ListGroups.md "../../../directoryservicedata/latest/DirectoryServiceDataAPIReference/API_ListGroups.md") action.

###### Note

The `NextToken` element is redacted from all log entries.

```
{
    "eventVersion": "1.08",
    "userIdentity": {
        "type": "AssumedRole",
        "principalId": "1234567890abcdef0:admin-role",
        "arn": "arn:aws:sts::111222333444:assumed-role/AdAdmin/admin-role",
        "accountId": "111222333444",
        "accessKeyId": "021345abcdef6789",
        "sessionContext": {
            "sessionIssuer": {
                "type": "Role",
                "principalId": "1234567890abcdef0",
                "arn": "arn:aws:iam::111222333444:role/AdAdmin",
                "accountId": "111222333444",
                "userName": "AdAdmin"
            },
            "attributes": {
                "creationDate": "2023-05-30T18:22:38Z",
                "mfaAuthenticated": "false"
            }
        }
    },
    "eventTime": "2023-05-30T18:29:15Z",
    "eventSource": "ds.amazonaws.com",
    "eventName": "ListGroups",
    "awsRegion": "ap-northeast-2",
    "sourceIPAddress": "10.24.34.0",
    "userAgent": "aws-cli/2.9.20 Python/3.11.1 Darwin/21.6.0 source/x86_64 prompt/off command/ds-data.list-groups",
    "requestParameters": {
        "directoryId": "d-1234567890",
        "nextToken": "REDACTED",
        "maxResults": 1
    },
    "responseElements": null,
    "requestID": "4567ab89-c12d-3333-2222-1e0012f34a7c",
    "eventID": "1234567b-f0a0-12ab-3c45-d678900d1255",
    "readOnly": true,
    "resources": [
        {
            "accountId": "111222333444",
            "type": "AWS::DirectoryService::MicrosoftAD",
            "ARN": "arn:aws:ds:ap-northeast-2:111222333444:directory/d-1234567890"
        }
    ],
    "eventType": "AwsApiCall",
    "managementEvent": true,
    "recipientAccountId": "111222333444",
    "eventCategory": "Management",
    "tlsDetails": {
        "tlsVersion": "TLSv1.3",
        "cipherSuite": "TLS_AES_128_GCM_SHA256",
        "clientProvidedHostHeader": "ds-data.ap-northeast-2.amazonaws.com"
    }
}
```

## Log entries for exception

errors

The following example shows a CloudTrail log entry for an Access Denied error. For help with
this error, see [Troubleshooting access
denied error messages](../../../IAM/latest/UserGuide/troubleshoot_access-denied.md "../../../IAM/latest/UserGuide/troubleshoot_access-denied.md") in the _IAM User Guide_.

###### Note

The Access Denied log doesn't show request parameters.

```
{
    "eventVersion": "1.08",
    "userIdentity": {
        "type": "AssumedRole",
        "principalId": "1234567890abcdef0:admin-role",
        "arn": "arn:aws:sts::111222333444:assumed-role/AdAdmin/admin-role",
        "accountId": "111222333444",
        "accessKeyId": "021345abcdef6789",
        "sessionContext": {
            "sessionIssuer": {
                "type": "Role",
                "principalId": "1234567890abcdef0",
                "arn": "arn:aws:iam::111222333444:role/AdAdmin",
                "accountId": "111222333444",
                "userName": "AdAdmin"
            },
            "attributes": {
                "creationDate": "2023-05-31T23:25:49Z",
                "mfaAuthenticated": "false"
            }
        }
    },
    "eventTime": "2023-05-31T23:38:18Z",
    "eventSource": "ds.amazonaws.com",
    "eventName": "CreateUser",
    "awsRegion": "ap-northeast-2",
    "sourceIPAddress": "10.24.34.0",
    "userAgent": "aws-cli/2.9.20 Python/3.11.1 Darwin/21.6.0 source/x86_64 prompt/off command/ds-data.create-user",
    "errorCode": "AccessDenied",
    "errorMessage": "User: arn:aws:sts::111222333444:assumed-role/AdAdmin/admin-role is not authorized to perform: ds-data:CreateUser on resource: arn:aws:ds:ap-northeast-2:111222333444:directory/d-1234567890 because no identity-based policy allows the ds-data:CreateUser action",
    "requestParameters": null,
    "responseElements": null,
    "requestID": "4567ab89-c12d-3333-2222-1e0012f34a7c",
    "eventID": "1234567b-f0a0-12ab-3c45-d678900d1255",
    "readOnly": false,
    "resources": [
        {
            "accountId": "111222333444",
            "type": "AWS::DirectoryService::MicrosoftAD",
            "ARN": "arn:aws:ds:ap-northeast-2:111222333444:directory/d-1234567890"
        }
    ],
    "eventType": "AwsApiCall",
    "managementEvent": true,
    "recipientAccountId": "111222333444",
    "eventCategory": "Management",
    "tlsDetails": {
        "tlsVersion": "TLSv1.3",
        "cipherSuite": "TLS_AES_128_GCM_SHA256",
        "clientProvidedHostHeader": "ds-data.ap-northeast-2.amazonaws.com"
    }
}
```

The following example shows a CloudTrail log entry for a Resource Not Found error.

```
{
    "eventVersion": "1.08",
    "userIdentity": {
        "type": "AssumedRole",
        "principalId": "1234567890abcdef0:admin-role",
        "arn": "arn:aws:sts::111222333444:assumed-role/AdAdmin/admin-role",
        "accountId": "111222333444",
        "accessKeyId": "021345abcdef6789",
        "sessionContext": {
            "sessionIssuer": {
                "type": "Role",
                "principalId": "1234567890abcdef0",
                "arn": "arn:aws:iam::111222333444:role/AdAdmin",
                "accountId": "111222333444",
                "userName": "AdAdmin"
            },
            "attributes": {
                "creationDate": "2023-05-30T20:41:50Z",
                "mfaAuthenticated": "false"
            }
        }
    },
    "eventTime": "2023-05-30T21:10:16Z",
    "eventSource": "ds.amazonaws.com",
    "eventName": "DescribeUser",
    "awsRegion": "ap-northeast-2",
    "sourceIPAddress": "10.24.34.0",
    "userAgent": "aws-cli/2.9.20 Python/3.11.1 Darwin/21.6.0 source/x86_64 prompt/off command/ds-data.describe-user",
    "errorCode": "ResourceNotFoundException",
    "errorMessage": "User not found in directory d-1234567890.",
    "requestParameters": {
        "directoryId": "d-1234567890",
        "sAMAccountName": "nonExistingUser",
        "otherAttributes": [
            "co",
            "givenName",
            "sn",
            "telephoneNumber"
        ]
    },
    "responseElements": null,
    "requestID": "4567ab89-c12d-3333-2222-1e0012f34a7c",
    "eventID": "1234567b-f0a0-12ab-3c45-d678900d1255",
    "readOnly": true,
    "resources": [
        {
            "accountId": "111222333444",
            "type": "AWS::DirectoryService::MicrosoftAD",
            "ARN": "arn:aws:ds:ap-northeast-2:111222333444:directory/d-1234567890"
        }
    ],
    "eventType": "AwsApiCall",
    "managementEvent": true,
    "recipientAccountId": "111222333444"
    "eventCategory": "Management",
    "tlsDetails": {
        "tlsVersion": "TLSv1.3",
        "cipherSuite": "TLS_AES_128_GCM_SHA256",
        "clientProvidedHostHeader": "ds-data.ap-northeast-2.amazonaws.com"
    }
}
```
