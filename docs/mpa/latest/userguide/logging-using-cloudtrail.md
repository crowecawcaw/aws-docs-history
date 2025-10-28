# Logging Multi-party approval API calls using

AWS CloudTrail

Multi-party approval works with [AWS CloudTrail](../../../awscloudtrail/latest/userguide/cloudtrail-user-guide.md "../../../awscloudtrail/latest/userguide/cloudtrail-user-guide.md"), a service that provides a record of actions taken by a user, role, or an
AWS service. CloudTrail captures all
API calls for Multi-party approval as events. The calls captured include calls from the Multi-party approval console
and code calls to the Multi-party approval API operations. Using the information collected by CloudTrail, you can
determine the request that was made to Multi-party approval, the IP address from which the request was
made, when it was made, and additional details.

Every event or log entry contains information about who generated the request. The identity
information helps you determine the following:

- Whether the request was made with root user or user credentials.
- Whether the request was made on behalf of an IAM Identity Center user.
- Whether the request was made with temporary security credentials for a role or federated
  user.
- Whether the request was made by another AWS service.
  CloudTrail is active in your AWS account when you create the account and you automatically have
  access to the CloudTrail **Event history**. The CloudTrail **Event
  history** provides a viewable, searchable, downloadable, and immutable record of the
  past 90 days of recorded management events in an AWS Region. For more information, see [Working
  with CloudTrail Event history](../../../awscloudtrail/latest/userguide/view-cloudtrail-events.md "../../../awscloudtrail/latest/userguide/view-cloudtrail-events.md") in the _AWS CloudTrail User Guide_. There are no CloudTrail
  charges for viewing the **Event history**.

For an ongoing record of events in your AWS account past 90 days, create a trail or a
[CloudTrail
Lake](../../../awscloudtrail/latest/userguide/cloudtrail-lake.md "../../../awscloudtrail/latest/userguide/cloudtrail-lake.md") event data store.

**CloudTrail trails**

A _trail_ enables CloudTrail to deliver log files to an Amazon S3 bucket. All trails created using the AWS Management Console are multi-Region. You can create a single-Region or a multi-Region trail by using the AWS CLI. Creating a multi-Region trail is recommended because you capture activity in all AWS Regions in your account. If you create a single-Region trail, you can view only the events logged in the trail's AWS Region. For more information about trails, see [Creating a trail for your AWS account](../../../awscloudtrail/latest/userguide/cloudtrail-create-and-update-a-trail.md "../../../awscloudtrail/latest/userguide/cloudtrail-create-and-update-a-trail.md") and [Creating a trail for an organization](../../../awscloudtrail/latest/userguide/creating-trail-organization.md "../../../awscloudtrail/latest/userguide/creating-trail-organization.md") in the _AWS CloudTrail User Guide_.

You can deliver one copy of your ongoing management events to your Amazon S3 bucket at no charge from CloudTrail by creating a trail, however, there are Amazon S3 storage charges. For more information about CloudTrail pricing, see [AWS CloudTrail Pricing](https://aws.amazon.com/cloudtrail/pricing/ "https://aws.amazon.com/cloudtrail/pricing/"). For information about Amazon S3 pricing, see [Amazon S3 Pricing](https://aws.amazon.com/s3/pricing/ "https://aws.amazon.com/s3/pricing/").

**CloudTrail Lake event data stores**

_CloudTrail Lake_ lets you run SQL-based queries on your events. CloudTrail Lake converts existing events in row-based JSON format to [Apache ORC](https://orc.apache.org/ "https://orc.apache.org/") format. ORC is a columnar storage format that is optimized for fast retrieval of data. Events are aggregated into _event data stores_, which are immutable collections of events based on criteria that you select by applying [advanced event selectors](../../../awscloudtrail/latest/userguide/cloudtrail-lake-concepts.md#adv-event-selectors "../../../awscloudtrail/latest/userguide/cloudtrail-lake-concepts.md#adv-event-selectors"). The selectors that you apply to an event data store control which events persist and are available for you to query. For more information about CloudTrail Lake, see [Working with AWS CloudTrail Lake](../../../awscloudtrail/latest/userguide/cloudtrail-lake.md "../../../awscloudtrail/latest/userguide/cloudtrail-lake.md") in the _AWS CloudTrail User Guide_.

CloudTrail Lake event data stores and queries incur costs. When you create an event data store, you choose the [pricing option](../../../awscloudtrail/latest/userguide/cloudtrail-lake-manage-costs.md#cloudtrail-lake-manage-costs-pricing-option "../../../awscloudtrail/latest/userguide/cloudtrail-lake-manage-costs.md#cloudtrail-lake-manage-costs-pricing-option") you want to use for the event data store. The pricing option determines the cost for ingesting and storing events, and the default and maximum retention period for the event data store. For more information about CloudTrail pricing, see [AWS CloudTrail Pricing](https://aws.amazon.com/cloudtrail/pricing/ "https://aws.amazon.com/cloudtrail/pricing/").

## Multi-party approval management events in CloudTrail

[Management events](../../../awscloudtrail/latest/userguide/logging-management-events-with-cloudtrail.md#logging-management-events "../../../awscloudtrail/latest/userguide/logging-management-events-with-cloudtrail.md#logging-management-events") provide information about management operations that are performed on resources in your AWS account. These are also known as control plane operations. By default, CloudTrail logs management events.

Multi-party approval logs all Multi-party approval control plane operations as management events. For a list
of the Multi-party approval control plane operations that Multi-party approval logs to CloudTrail, see the
[Multi-party approval API Reference](../APIReference/Welcome.md "../APIReference/Welcome.md").

## Multi-party approval event examples

An event represents a single request from any source and includes information about the requested API operation, the date and time of the operation, request parameters, and so on. CloudTrail log files aren't an ordered stack trace of the public API calls, so events don't appear in any specific order.

**Asynchronous events**

The following tabbed list displays some examples for approval teams.

ASYNC_DELETION_APPROVAL_FAILURE [DELETE]
The following example shows a CloudTrail event for an asynchronous deletion approval failure:

```
{
    "eventVersion": "[default]",
    "userIdentity": {
        "accountId": "[MPA Team owner account]",
        "invokedBy": "mpa.amazonaws.com"
    },
    "eventTime": "2021-01-14T01:41:59Z",
    "eventSource": "mpa.amazonaws.com",
    "eventName": "TeamDeletionApprovalFailure",
    "awsRegion": "[team region]",
    "sourceIPAddress": "AWS Internal",
    "userAgent": "AWS Internal",
    "requestParameters": null,
    "responseElements": null,
    "eventID": "a24b3967-ddad-417f-9b22-2332b918db06",
    "readOnly": false,
    "resources": [
        {
            "accountId": "111122223333",
            "type": "AWS::MPA::Team",
            "ARN": "arn:aws:mpa:[team ARN]"
        }
    ],
    "eventType": "AwsServiceEvent",
    "recipientAccountId": "[MPA Team owner account]",
    "serviceEventDetails": {
        "teamStatus": "ACTIVE",
        "teamStatusCode": "DELETE_FAILED_APPROVAL",
        "updateSessionId": "[session ID]"
    },
    "eventCategory": "Management"
}
```

ASYNC_DELETION_APPROVAL_SUCCESS [DELETE]
The following example shows a CloudTrail event for an asynchronous deletion approval success:

```
{
    "eventName": "TeamDeletionApprovalSuccess",
    "serviceEventDetails": {
        "teamStatus": "DELETED",
        "updateSessionId": "[session ID]"
    }
}
```

ASYNC_UPDATE_ACTIVATION_FAILURE [UPDATE]
The following example shows a CloudTrail event for an asynchronous update activation failure:

```
{
    "eventName": "TeamUpdateActivationFailure",
    "serviceEventDetails": {
        "teamStatus": "ACTIVE",
        "teamStatusCode": "UPDATE_FAILED_ACTIVATION"
    }
}
```

ASYNC_UPDATE_ACTIVATION_SUCCESS [UPDATE]
The following example shows a CloudTrail event for an asynchronous update activation success:

```
{
    "eventName": "TeamUpdateActivationSuccess",
    "serviceEventDetails": {
        "teamStatus": "ACTIVE"
    }
}
```

ASYNC_UPDATE_APPROVAL_FAILURE [UPDATE]
The following example shows a CloudTrail event for an asynchronous update approval failure:

```
{
    "eventName": "TeamUpdateApprovalFailure",
    "serviceEventDetails": {
        "teamStatus": "ACTIVE",
        "teamStatusCode": "UPDATE_FAILED_ACTIVATION",
        "updateSessionId": "[session ID]"
    }
}
```

ASYNC_UPDATE_APPROVAL_SUCCESS [UPDATE]
The following example shows a CloudTrail event for an asynchronous update approval success:

```
{
    "eventName": "TeamUpdateApprovalSuccess",
    "serviceEventDetails": {
        "teamStatus": "ACTIVE",
        "teamStatusCode": "UPDATE_PENDING_ACTIVATION",
        "updateSessionId": "[session ID]"
    }
}
```

ASYNC_VALIDATION_FAILURE [UPDATE]
The following example shows a CloudTrail event for an asynchronous validation failure during an update:

```
{
    "eventName": "TeamUpdateValidationFailure",
    "serviceEventDetails": {
        "teamStatus": "ACTIVE",
        "teamStatusCode": "UPDATE_FAILED_VALIDATION"
    }
}
```

ASYNC_VALIDATION_SUCCESS [UPDATE]
The following example shows a CloudTrail event for an asynchronous validation success during an update:

```
{
    "eventName": "TeamUpdateValidationSuccess",
    "serviceEventDetails": {
        "teamStatus": "ACTIVE",
        "teamStatusCode": "UPDATE_PENDING_APPROVAL",
        "updateSessionId": "[session ID]"
    }
}
```

ASYNC_ACTIVATION_SUCCESS [CREATE]
The following example shows a CloudTrail event for an asynchronous activation success during creation:

```
{
    "eventName": "TeamCreationActivationSuccess",
    "serviceEventDetails": {
        "teamStatus": "ACTIVE"
    }
}
```

ASYNC_ACTIVATION_FAILURE [CREATE]
The following example shows a CloudTrail event for an asynchronous activation failure during creation:

```
{
    "eventName": "TeamCreationActivationFailure",
    "serviceEventDetails": {
        "teamStatus": "INACTIVE",
        "teamStatusCode": "FAILED_ACTIVATION"
    }
}
```

ASYNC_VALIDATION_FAILURE [CREATE]
The following example shows a CloudTrail event for an asynchronous validation failure during creation:

```
{
    "eventName": "TeamCreationValidationFailure",
    "serviceEventDetails": {
        "teamStatus": "INACTIVE",
        "teamStatusCode": "FAILED_VALIDATION"
    }
}
```

ASYNC_VALIDATION_SUCCESS [CREATE]
The following example shows a CloudTrail event for an asynchronous validation success during creation:

```
{
    "eventName": "TeamCreationValidationSuccess",
    "serviceEventDetails": {
        "teamStatus": "PENDING",
        "teamStatusCode": "PENDING_ACTIVATION"
    }
}
```

The following tabbed list displays some examples for approval sessions.

ASYNC_EXPIRED [EXPIRATION]
The following example shows a CloudTrail event for an asynchronous session expiration:

```
{
    "eventVersion": "[default]",
    "userIdentity": {
        "accountId": "[MPA Team owner account]",
        "invokedBy": "mpa.amazonaws.com"
    },
    "eventTime": "2021-01-14T01:41:59Z",
    "eventSource": "mpa.amazonaws.com",
    "eventName": "SessionExpiration",
    "awsRegion": "[team region]",
    "sourceIPAddress": "AWS Internal",
    "userAgent": "AWS Internal",
    "requestParameters": null,
    "responseElements": null,
    "eventID": "a24b3967-ddad-417f-9b22-2332b918db06",
    "readOnly": false,
    "resources": [
        {
            "accountId": "111122223333",
            "type": "AWS::MPA::Session",
            "ARN": "arn:aws:mpa:[Session ARN]"
        }
    ],
    "eventType": "AwsServiceEvent",
    "recipientAccountId": "[MPA Team owner account]",
    "serviceEventDetails": {
        "sessionStatus": "FAILED",
        "sessionStatusCode": "EXPIRED",
        "approvedBy": "[identityStoreArn/userId1],[identityStoreArn/userId2],...",
        "rejectedBy": "[identityStoreArn/userId1],[identityStoreArn/userId2],...",
        "noParticipationBy": "[identityStoreArn/userId1],[identityStoreArn/userId2],..."
    },
    "eventCategory": "Management"
}
```

ASYNC_CANCELLED_TEAM_CONFIGURATION_CHANGED [CANCELATION]
The following example shows a CloudTrail event for a session cancellation due to team configuration changes:

```
{
    "eventName": "SessionCancellation",
    "serviceEventDetails": {
        "sessionStatus": "CANCELLED",
        "sessionStatusCode": "CONFIGURATION_CHANGED",
        "approvedBy": "[identityStoreArn/userId1],[identityStoreArn/userId2],...",
        "rejectedBy": "[identityStoreArn/userId1],[identityStoreArn/userId2],...",
        "noParticipationBy": "[identityStoreArn/userId1],[identityStoreArn/userId2],..."
    }
}
```

ASYNC_CANCELLED_TEAM_DELETED [CANCELATION]
The following example shows a CloudTrail event for a session cancellation due to team deletion:

```
{
    "eventName": "SessionCancellation",
    "serviceEventDetails": {
        "sessionStatus": "CANCELLED",
        "sessionStatusCode": "TEAM_DELETED",
        "approvedBy": "[identityStoreArn/userId1],[identityStoreArn/userId2],...",
        "rejectedBy": "[identityStoreArn/userId1],[identityStoreArn/userId2],...",
        "noParticipationBy": "[identityStoreArn/userId1],[identityStoreArn/userId2],..."
    }
}
```

ASYNC_CANCELLED_BY_USER [CANCELATION]
The following example shows a CloudTrail event for a user-initiated session cancellation:

```
{
    "eventName": "SessionCancellation",
    "serviceEventDetails": {
        "sessionStatus": "CANCELLED",
        "sessionStatusCode": "CANCELLED_BY_USER",
        "approvedBy": "[identityStoreArn/userId1],[identityStoreArn/userId2],...",
        "rejectedBy": "[identityStoreArn/userId1],[identityStoreArn/userId2],...",
        "noParticipationBy": "[identityStoreArn/userId1],[identityStoreArn/userId2],..."
    }
}
```

ASYNC_VALIDATION_SUCCESS [VALIDATION]
The following example shows a CloudTrail event for an asynchronous validation success:

```
{
    "eventName": "SessionValidationSuccess",
    "serviceEventDetails": {
        "sessionStatus": "PENDING"
    }
}
```

ASYNC_SESSION_APPROVED [APPROVAL]
The following example shows a CloudTrail event for an approved session:

```
{
    "eventName": "SessionApproved",
    "serviceEventDetails": {
        "sessionStatus": "APPROVED",
        "approvedBy": "[identityStoreArn/userId1],[identityStoreArn/userId2],...",
        "rejectedBy": "[identityStoreArn/userId1],[identityStoreArn/userId2],...",
        "noParticipationBy": "[identityStoreArn/userId1],[identityStoreArn/userId2],..."
    }
}
```

ASYNC_SESSION_REJECTED [REJECTION]
The following example shows a CloudTrail event for a rejected session:

```
{
    "eventName": "SessionApproved",
    "serviceEventDetails": {
        "sessionStatus": "FAILED",
        "sessionStatusCode": "REJECTED",
        "approvedBy": "[identityStoreArn/userId1],[identityStoreArn/userId2],...",
        "rejectedBy": "[identityStoreArn/userId1],[identityStoreArn/userId2],...",
        "noParticipationBy": "[identityStoreArn/userId1],[identityStoreArn/userId2],..."
    }
}
```

**Events**

The following tabbed list displays some examples for standard success flow.

CancelSession (Success)
The following example shows a CloudTrail event that demonstrates the `CancelSession` operation.

```
{
  "eventVersion": "1.10",
  "userIdentity": {
    "type": "AssumedRole",
    "principalId": "AROA123456789EXAMPLE:ExampleRole-mpa",
    "arn": "arn:aws:sts::111122223333:assumed-role/ExampleRole/ExampleRole-mpa",
    "accountId": "111122223333",
    "accessKeyId": "AKIA1234567890EXAMPLE",
    "sessionContext": {
      "sessionIssuer": {
        "type": "Role",
        "principalId": "AROA123456789EXAMPLE",
        "arn": "arn:aws:iam::111122223333:role/ExampleRole",
        "accountId": "111122223333",
        "userName": "ExampleRole"
      },
      "attributes": {
        "creationDate": "2025-03-11T00:07:31Z",
        "mfaAuthenticated": "false"
      }
    }
  },
  "eventTime": "2025-03-11T00:07:31Z",
  "eventSource": "multi-party-approval.amazonaws.com",
  "eventName": "CancelSession",
  "awsRegion": "us-east-1",
  "sourceIPAddress": "192.0.2.0",
  "userAgent": "aws-sdk-java/2.30.32 Linux/5.10.233-224.894.amzn2.x86_64",
  "requestParameters": {
    "sessionArn": "arn:aws:mpa:us-east-1:111122223333:session/ExampleTest-a1b2c3d4-5678-90ab-cdef-EXAMPLE11111/a1b2c3d4-5678-90ab-cdef-EXAMPLE22222"
  },
  "responseElements": null,
  "requestID": "a1b2c3d4-5678-90ab-cdef-EXAMPLE33333",
  "eventID": "a1b2c3d4-5678-90ab-cdef-EXAMPLE44444",
  "readOnly": false,
  "resources": [
    {
      "accountId": "111122223333",
      "type": "AWS::MPA::ApprovalTeam",
      "ARN": "arn:aws:mpa:us-east-1:111122223333:approval-team/ExampleTest-a1b2c3d4-5678-90ab-cdef-EXAMPLE11111"
    },
    {
      "accountId": "111122223333",
      "type": "AWS::MPA::Session",
      "ARN": "arn:aws:mpa:us-east-1:111122223333:session/ExampleTest-a1b2c3d4-5678-90ab-cdef-EXAMPLE11111/a1b2c3d4-5678-90ab-cdef-EXAMPLE22222"
    }
  ],
  "eventType": "AwsApiCall",
  "managementEvent": true,
  "recipientAccountId": "111122223333",
  "eventCategory": "Management",
  "tlsDetails": {
    "tlsVersion": "TLSv1.3",
    "cipherSuite": "TLS_AES_128_GCM_SHA256",
    "clientProvidedHostHeader": "multi-party-approval.us-east-1.amazonaws.com"
  }
}
```

CreateApprovalTeam (Success)
The following example shows a CloudTrail event that demonstrates the `CreateApprovalTeam` operation.

```
{
  "eventVersion": "1.10",
  "userIdentity": {
    "type": "AssumedRole",
    "principalId": "AROA123456789EXAMPLE:ExampleRole-mpa",
    "arn": "arn:aws:sts::111122223333:assumed-role/ExampleRole/ExampleRole-mpa",
    "accountId": "111122223333",
    "accessKeyId": "AKIA1234567890EXAMPLE",
    "sessionContext": {
      "sessionIssuer": {
        "type": "Role",
        "principalId": "AROA123456789EXAMPLE",
        "arn": "arn:aws:iam::111122223333:role/ExampleRole",
        "accountId": "111122223333",
        "userName": "ExampleRole"
      },
      "attributes": {
        "creationDate": "2025-03-11T00:04:23Z",
        "mfaAuthenticated": "false"
      }
    }
  },
  "eventTime": "2025-03-11T00:04:23Z",
  "eventSource": "multi-party-approval.amazonaws.com",
  "eventName": "CreateApprovalTeam",
  "awsRegion": "us-east-1",
  "sourceIPAddress": "192.0.2.0",
  "userAgent": "aws-sdk-java/2.30.32 Linux/5.10.233-224.894.amzn2.x86_64",
  "requestParameters": {
    "clientToken": "vGjlhLiwFPAaBsQ",
    "approvalStrategy": {
      "mofN": {
        "minApprovalsRequired": 2
      }
    },
    "approvers": [
      {
        "primaryIdentityId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
        "primaryIdentitySourceArn": "arn:aws:mpa:us-east-1:111122223333:identity-source/IamIdentityCenter"
      },
      {
        "primaryIdentityId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE22222",
        "primaryIdentitySourceArn": "arn:aws:mpa:us-east-1:111122223333:identity-source/IamIdentityCenter"
      }
    ],
    "description": "HIDDEN_DUE_TO_SECURITY_REASONS",
    "policies": [
      {
        "policyArn": "arn:aws:mpa:::aws:policy/backup.amazonaws.com/CreateRestoreAccessVault/$DEFAULT"
      }
    ],
    "name": "CloudtrailTest",
    "tags": "HIDDEN_DUE_TO_SECURITY_REASONS"
  },
  "responseElements": {
    "creationTime": "Mar 11, 2025, 12:04:23 AM",
    "arn": "arn:aws:mpa:us-east-1:111122223333:approval-team/CloudtrailTest-a1b2c3d4-5678-90ab-cdef-EXAMPLE33333",
    "name": "CloudtrailTest",
    "versionId": "1741651463452"
  },
  "requestID": "a1b2c3d4-5678-90ab-cdef-EXAMPLE44444",
  "eventID": "a1b2c3d4-5678-90ab-cdef-EXAMPLE55555",
  "readOnly": false,
  "resources": [
    {
      "accountId": "111122223333",
      "type": "AWS::MPA::ApprovalTeam",
      "ARN": "arn:aws:mpa:us-east-1:111122223333:approval-team/CloudtrailTest-a1b2c3d4-5678-90ab-cdef-EXAMPLE33333"
    }
  ],
  "eventType": "AwsApiCall",
  "managementEvent": true,
  "recipientAccountId": "111122223333",
  "eventCategory": "Management",
  "tlsDetails": {
    "tlsVersion": "TLSv1.3",
    "cipherSuite": "TLS_AES_128_GCM_SHA256",
    "clientProvidedHostHeader": "multi-party-approval.us-east-1.amazonaws.com"
  }
}
```

CreateIdentitySource (Success)
The following example shows a CloudTrail event that demonstrates the `CreateIdentitySource` operation.

```
{
  "eventVersion": "1.10",
  "userIdentity": {
    "type": "AssumedRole",
    "principalId": "AROA123456789EXAMPLE:ExampleRole-mpa",
    "arn": "arn:aws:sts::111122223333:assumed-role/ExampleRole/ExampleRole-mpa",
    "accountId": "111122223333",
    "accessKeyId": "AKIA1234567890EXAMPLE",
    "sessionContext": {
      "sessionIssuer": {
        "type": "Role",
        "principalId": "AROA123456789EXAMPLE",
        "arn": "arn:aws:iam::111122223333:role/ExampleRole",
        "accountId": "111122223333",
        "userName": "ExampleRole"
      },
      "attributes": {
        "creationDate": "2025-03-06T20:40:03Z",
        "mfaAuthenticated": "false"
      }
    }
  },
  "eventTime": "2025-03-06T20:40:05Z",
  "eventSource": "multi-party-approval.amazonaws.com",
  "eventName": "CreateIdentitySource",
  "awsRegion": "us-east-1",
  "sourceIPAddress": "192.0.2.0",
  "userAgent": "aws-sdk-java/2.30.32 Linux/5.10.233-224.894.amzn2.x86_64",
  "requestParameters": {
    "identitySourceParameters": {
      "iamIdentityCenter": {
        "instanceArn": "arn:aws:sso:::instance/ssoins-a1b2c3d4e5f6g7h8i",
        "region": "us-east-1"
      }
    },
    "clientToken": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111"
  },
  "responseElements": {
    "identitySourceType": "IAM_IDENTITY_CENTER",
    "identitySourceArn": "arn:aws:mpa:us-east-1:111122223333:identity-source/IamIdentityCenter",
    "creationTime": "Mar 6, 2025, 8:40:05 PM"
  },
  "requestID": "a1b2c3d4-5678-90ab-cdef-EXAMPLE22222",
  "eventID": "a1b2c3d4-5678-90ab-cdef-EXAMPLE33333",
  "readOnly": false,
  "eventType": "AwsApiCall",
  "managementEvent": true,
  "recipientAccountId": "111122223333",
  "eventCategory": "Management",
  "tlsDetails": {
    "tlsVersion": "TLSv1.3",
    "cipherSuite": "TLS_AES_128_GCM_SHA256",
    "clientProvidedHostHeader": "multi-party-approval.us-east-1.amazonaws.com"
  }
}
```

DeleteIdentitySource (Success)
The following example shows a CloudTrail event that demonstrates the `DeleteIdentitySource` operation.

```
{
  "eventVersion": "1.10",
  "userIdentity": {
    "type": "AssumedRole",
    "principalId": "AROA123456789EXAMPLE:ExampleRole-mpa",
    "arn": "arn:aws:sts::111122223333:assumed-role/ExampleRole/ExampleRole-mpa",
    "accountId": "111122223333",
    "accessKeyId": "AKIA1234567890EXAMPLE",
    "sessionContext": {
      "sessionIssuer": {
        "type": "Role",
        "principalId": "AROA123456789EXAMPLE",
        "arn": "arn:aws:iam::111122223333:role/ExampleRole",
        "accountId": "111122223333",
        "userName": "ExampleRole"
      },
      "attributes": {
        "creationDate": "2025-03-11T16:21:31Z",
        "mfaAuthenticated": "false"
      }
    }
  },
  "eventTime": "2025-03-11T16:27:00Z",
  "eventSource": "multi-party-approval.amazonaws.com",
  "eventName": "DeleteIdentitySource",
  "awsRegion": "us-east-1",
  "sourceIPAddress": "192.0.2.0",
  "userAgent": "aws-cli/2.15.13 Python/3.11.6 Darwin/24.3.0",
  "requestParameters": {
    "identitySourceArn": "arn:aws:mpa:us-east-1:111122223333:identity-source/IamIdentityCenter"
  },
  "responseElements": null,
  "requestID": "a1b2c3d4-5678-90ab-cdef-EXAMPLE44444",
  "eventID": "a1b2c3d4-5678-90ab-cdef-EXAMPLE55555",
  "readOnly": false,
  "resources": [
    {
      "accountId": "111122223333",
      "type": "AWS::MPA::IdentitySource",
      "ARN": "arn:aws:mpa:us-east-1:111122223333:identity-source/IamIdentityCenter"
    }
  ],
  "eventType": "AwsApiCall",
  "managementEvent": true,
  "recipientAccountId": "111122223333",
  "eventCategory": "Management",
  "tlsDetails": {
    "tlsVersion": "TLSv1.3",
    "cipherSuite": "TLS_AES_128_GCM_SHA256",
    "clientProvidedHostHeader": "multi-party-approval.us-east-1.amazonaws.com"
  }
}
```

DeleteInactiveApprovalTeamVersion (Success)
The following example shows a CloudTrail event that demonstrates the `DeleteInactiveApprovalTeamVersion` operation.

```
{
  "eventVersion": "1.10",
  "userIdentity": {
    "type": "AssumedRole",
    "principalId": "AROA123456789EXAMPLE:ExampleRole-mpa",
    "arn": "arn:aws:sts::111122223333:assumed-role/ExampleRole/ExampleRole-mpa",
    "accountId": "111122223333",
    "accessKeyId": "AKIA1234567890EXAMPLE",
    "sessionContext": {
      "sessionIssuer": {
        "type": "Role",
        "principalId": "AROA123456789EXAMPLE",
        "arn": "arn:aws:iam::111122223333:role/ExampleRole",
        "accountId": "111122223333",
        "userName": "ExampleRole"
      },
      "attributes": {
        "creationDate": "2025-03-11T00:04:14Z",
        "mfaAuthenticated": "false"
      }
    }
  },
  "eventTime": "2025-03-11T00:06:54Z",
  "eventSource": "multi-party-approval.amazonaws.com",
  "eventName": "DeleteInactiveApprovalTeamVersion",
  "awsRegion": "us-east-1",
  "sourceIPAddress": "192.0.2.0",
  "userAgent": "aws-sdk-java/2.30.32 Linux/5.10.233-224.894.amzn2.x86_64",
  "requestParameters": {
    "arn": "arn:aws:mpa:us-east-1:111122223333:approval-team/ExampleApprovalTeam-a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
    "versionId": "1741651519207"
  },
  "responseElements": null,
  "requestID": "a1b2c3d4-5678-90ab-cdef-EXAMPLE22222",
  "eventID": "a1b2c3d4-5678-90ab-cdef-EXAMPLE33333",
  "readOnly": false,
  "resources": [
    {
      "accountId": "111122223333",
      "type": "AWS::MPA::ApprovalTeam",
      "ARN": "arn:aws:mpa:us-east-1:111122223333:approval-team/ExampleApprovalTeam-a1b2c3d4-5678-90ab-cdef-EXAMPLE11111"
    }
  ],
  "eventType": "AwsApiCall",
  "managementEvent": true,
  "recipientAccountId": "111122223333",
  "eventCategory": "Management",
  "tlsDetails": {
    "tlsVersion": "TLSv1.3",
    "cipherSuite": "TLS_AES_128_GCM_SHA256",
    "clientProvidedHostHeader": "multi-party-approval.us-east-1.amazonaws.com"
  }
}
```

DeleteResourcePolicy (Success)
The following example shows a CloudTrail event that demonstrates the `DeleteResourcePolicy` operation.

```
{
  "eventVersion": "1.10",
  "userIdentity": {
    "type": "AssumedRole",
    "principalId": "AROA123456789EXAMPLE:ExampleRole-mpa",
    "arn": "arn:aws:sts::111122223333:assumed-role/ExampleRole/ExampleRole-mpa",
    "accountId": "111122223333",
    "accessKeyId": "AKIA1234567890EXAMPLE",
    "sessionContext": {
      "sessionIssuer": {
        "type": "Role",
        "principalId": "AROA123456789EXAMPLE",
        "arn": "arn:aws:iam::111122223333:role/ExampleRole",
        "accountId": "111122223333",
        "userName": "ExampleRole"
      },
      "attributes": {
        "creationDate": "2025-03-11T17:28:00Z",
        "mfaAuthenticated": "false"
      }
    }
  },
  "eventTime": "2025-03-11T18:01:49Z",
  "eventSource": "multi-party-approval.amazonaws.com",
  "eventName": "DeleteResourcePolicy",
  "awsRegion": "us-east-1",
  "sourceIPAddress": "192.0.2.0",
  "userAgent": "aws-cli/2.15.13 Python/3.11.6 Darwin/24.3.0",
  "requestParameters": {
    "resourceArn": "arn:aws:mpa:us-east-1:111122223333:approval-team/ExampleTeam-a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
    "policyName": "ExamplePolicy",
    "policyType": "AWS_MANAGED"
  },
  "responseElements": null,
  "requestID": "a1b2c3d4-5678-90ab-cdef-EXAMPLE22222",
  "eventID": "a1b2c3d4-5678-90ab-cdef-EXAMPLE33333",
  "readOnly": false,
  "resources": [
    {
      "accountId": "111122223333",
      "type": "AWS::MPA::ApprovalTeam",
      "ARN": "arn:aws:mpa:us-east-1:111122223333:approval-team/ExampleTeam-a1b2c3d4-5678-90ab-cdef-EXAMPLE11111"
    }
  ],
  "eventType": "AwsApiCall",
  "managementEvent": true,
  "recipientAccountId": "111122223333",
  "eventCategory": "Management",
  "tlsDetails": {
    "tlsVersion": "TLSv1.3",
    "cipherSuite": "TLS_AES_128_GCM_SHA256",
    "clientProvidedHostHeader": "multi-party-approval.us-east-1.amazonaws.com"
  }
}
```

GetApprovalTeam (Success)
The following example shows a CloudTrail event that demonstrates the `GetApprovalTeam` operation.

```
{
  "eventVersion": "1.10",
  "userIdentity": {
    "type": "AssumedRole",
    "principalId": "AROA123456789EXAMPLE:ExampleRole-mpa",
    "arn": "arn:aws:sts::111122223333:assumed-role/ExampleRole/ExampleRole-mpa",
    "accountId": "111122223333",
    "accessKeyId": "AKIA1234567890EXAMPLE",
    "sessionContext": {
      "sessionIssuer": {
        "type": "Role",
        "principalId": "AROA123456789EXAMPLE",
        "arn": "arn:aws:iam::111122223333:role/ExampleRole",
        "accountId": "111122223333",
        "userName": "ExampleRole"
      },
      "attributes": {
        "creationDate": "2025-03-11T00:04:14Z",
        "mfaAuthenticated": "false"
      }
    }
  },
  "eventTime": "2025-03-11T00:06:33Z",
  "eventSource": "multi-party-approval.amazonaws.com",
  "eventName": "GetApprovalTeam",
  "awsRegion": "us-east-1",
  "sourceIPAddress": "192.0.2.0",
  "userAgent": "aws-sdk-java/2.30.32 Linux/5.10.233-224.894.amzn2.x86_64",
  "requestParameters": {
    "arn": "arn:aws:mpa:us-east-1:111122223333:approval-team/ExampleTeam-a1b2c3d4-5678-90ab-cdef-EXAMPLE11111"
  },
  "responseElements": null,
  "requestID": "a1b2c3d4-5678-90ab-cdef-EXAMPLE22222",
  "eventID": "a1b2c3d4-5678-90ab-cdef-EXAMPLE33333",
  "readOnly": true,
  "resources": [
    {
      "accountId": "111122223333",
      "type": "AWS::MPA::ApprovalTeam",
      "ARN": "arn:aws:mpa:us-east-1:111122223333:approval-team/ExampleTeam-a1b2c3d4-5678-90ab-cdef-EXAMPLE11111"
    }
  ],
  "eventType": "AwsApiCall",
  "managementEvent": true,
  "recipientAccountId": "111122223333",
  "eventCategory": "Management",
  "tlsDetails": {
    "tlsVersion": "TLSv1.3",
    "cipherSuite": "TLS_AES_128_GCM_SHA256",
    "clientProvidedHostHeader": "multi-party-approval.us-east-1.amazonaws.com"
  }
}
```

GetIdentitySource (Success)
The following example shows a CloudTrail event that demonstrates the `GetIdentitySource` operation.

```
{
  "eventVersion": "1.10",
  "userIdentity": {
    "type": "AssumedRole",
    "principalId": "AROA123456789EXAMPLE:ExampleRole-mpa",
    "arn": "arn:aws:sts::111122223333:assumed-role/ExampleRole/ExampleRole-mpa",
    "accountId": "111122223333",
    "accessKeyId": "AKIA1234567890EXAMPLE",
    "sessionContext": {
      "sessionIssuer": {
        "type": "Role",
        "principalId": "AROA123456789EXAMPLE",
        "arn": "arn:aws:iam::111122223333:role/ExampleRole",
        "accountId": "111122223333",
        "userName": "ExampleRole"
      },
      "attributes": {
        "creationDate": "2025-03-11T00:04:14Z",
        "mfaAuthenticated": "false"
      }
    }
  },
  "eventTime": "2025-03-11T00:05:19Z",
  "eventSource": "multi-party-approval.amazonaws.com",
  "eventName": "GetIdentitySource",
  "awsRegion": "us-east-1",
  "sourceIPAddress": "192.0.2.0",
  "userAgent": "aws-sdk-java/2.30.32 Linux/5.10.233-224.894.amzn2.x86_64",
  "requestParameters": {
    "identitySourceArn": "arn:aws:mpa:us-east-1:111122223333:identity-source/IamIdentityCenter"
  },
  "responseElements": null,
  "requestID": "a1b2c3d4-5678-90ab-cdef-EXAMPLE44444",
  "eventID": "a1b2c3d4-5678-90ab-cdef-EXAMPLE55555",
  "readOnly": true,
  "resources": [
    {
      "accountId": "111122223333",
      "type": "AWS::MPA::IdentitySource",
      "ARN": "arn:aws:mpa:us-east-1:111122223333:identity-source/IamIdentityCenter"
    }
  ],
  "eventType": "AwsApiCall",
  "managementEvent": true,
  "recipientAccountId": "111122223333",
  "eventCategory": "Management",
  "tlsDetails": {
    "tlsVersion": "TLSv1.3",
    "cipherSuite": "TLS_AES_128_GCM_SHA256",
    "clientProvidedHostHeader": "multi-party-approval.us-east-1.amazonaws.com"
  }
}
```

GetPolicyVersion (Success)
The following example shows a CloudTrail event that demonstrates the `GetPolicyVersion` operation.

```
{
  "eventVersion": "1.10",
  "userIdentity": {
    "type": "AssumedRole",
    "principalId": "AROA123456789EXAMPLE:ExampleRole-mpa",
    "arn": "arn:aws:sts::111122223333:assumed-role/ExampleRole/ExampleRole-mpa",
    "accountId": "111122223333",
    "accessKeyId": "AKIA1234567890EXAMPLE",
    "sessionContext": {
      "sessionIssuer": {
        "type": "Role",
        "principalId": "AROA123456789EXAMPLE",
        "arn": "arn:aws:iam::111122223333:role/ExampleRole",
        "accountId": "111122223333",
        "userName": "ExampleRole"
      },
      "attributes": {
        "creationDate": "2025-03-11T00:05:38Z",
        "mfaAuthenticated": "false"
      }
    }
  },
  "eventTime": "2025-03-11T00:05:38Z",
  "eventSource": "multi-party-approval.amazonaws.com",
  "eventName": "GetPolicyVersion",
  "awsRegion": "us-east-1",
  "sourceIPAddress": "192.0.2.0",
  "userAgent": "aws-sdk-java/2.30.32 Linux/5.10.233-224.894.amzn2.x86_64",
  "requestParameters": {
    "policyVersionArn": "arn:aws:mpa:::aws:policy/backup.amazonaws.com/CreateRestoreAccessVault/1"
  },
  "responseElements": null,
  "requestID": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
  "eventID": "a1b2c3d4-5678-90ab-cdef-EXAMPLE22222",
  "readOnly": true,
  "eventType": "AwsApiCall",
  "managementEvent": true,
  "recipientAccountId": "111122223333",
  "eventCategory": "Management",
  "tlsDetails": {
    "tlsVersion": "TLSv1.3",
    "cipherSuite": "TLS_AES_128_GCM_SHA256",
    "clientProvidedHostHeader": "multi-party-approval.us-east-1.amazonaws.com"
  }
}
```

GetResourcePolicy (Success)
The following example shows a CloudTrail event that demonstrates the `GetResourcePolicy` operation.

```
{
  "eventVersion": "1.10",
  "userIdentity": {
    "type": "AssumedRole",
    "principalId": "AROA123456789EXAMPLE:ExampleRole-mpa",
    "arn": "arn:aws:sts::111122223333:assumed-role/ExampleRole/ExampleRole-mpa",
    "accountId": "111122223333",
    "accessKeyId": "AKIA1234567890EXAMPLE",
    "sessionContext": {
      "sessionIssuer": {
        "type": "Role",
        "principalId": "AROA123456789EXAMPLE",
        "arn": "arn:aws:iam::111122223333:role/ExampleRole",
        "accountId": "111122223333",
        "userName": "ExampleRole"
      },
      "attributes": {
        "creationDate": "2025-03-11T00:05:38Z",
        "mfaAuthenticated": "false"
      }
    }
  },
  "eventTime": "2025-03-11T00:05:38Z",
  "eventSource": "multi-party-approval.amazonaws.com",
  "eventName": "GetResourcePolicy",
  "awsRegion": "us-east-1",
  "sourceIPAddress": "192.0.2.0",
  "userAgent": "aws-sdk-java/2.30.32 Linux/5.10.233-224.894.amzn2.x86_64",
  "requestParameters": {
    "resourceArn": "arn:aws:mpa:us-east-1:111122223333:approval-team/ExampleTeam-a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
    "policyType": "AWS_MANAGED",
    "policyName": "ExamplePolicy"
  },
  "responseElements": null,
  "requestID": "a1b2c3d4-5678-90ab-cdef-EXAMPLE33333",
  "eventID": "a1b2c3d4-5678-90ab-cdef-EXAMPLE44444",
  "readOnly": true,
  "resources": [
    {
      "accountId": "111122223333",
      "type": "AWS::MPA::ApprovalTeam",
      "ARN": "arn:aws:mpa:us-east-1:111122223333:approval-team/ExampleTeam-a1b2c3d4-5678-90ab-cdef-EXAMPLE11111"
    }
  ],
  "eventType": "AwsApiCall",
  "managementEvent": true,
  "recipientAccountId": "111122223333",
  "eventCategory": "Management",
  "tlsDetails": {
    "tlsVersion": "TLSv1.3",
    "cipherSuite": "TLS_AES_128_GCM_SHA256",
    "clientProvidedHostHeader": "multi-party-approval.us-east-1.amazonaws.com"
  }
}
```

GetSession (Success)
The following example shows a CloudTrail event that demonstrates the `GetSession` operation.

```
{
  "eventVersion": "1.10",
  "userIdentity": {
    "type": "AssumedRole",
    "principalId": "AROA123456789EXAMPLE:ExampleRole-mpa",
    "arn": "arn:aws:sts::111122223333:assumed-role/ExampleRole/ExampleRole-mpa",
    "accountId": "111122223333",
    "accessKeyId": "AKIA1234567890EXAMPLE",
    "sessionContext": {
      "sessionIssuer": {
        "type": "Role",
        "principalId": "AROA123456789EXAMPLE",
        "arn": "arn:aws:iam::111122223333:role/ExampleRole",
        "accountId": "111122223333",
        "userName": "ExampleRole"
      },
      "attributes": {
        "creationDate": "2025-03-11T00:04:14Z",
        "mfaAuthenticated": "false"
      }
    }
  },
  "eventTime": "2025-03-11T00:04:23Z",
  "eventSource": "multi-party-approval.amazonaws.com",
  "eventName": "GetSession",
  "awsRegion": "us-east-1",
  "sourceIPAddress": "192.0.2.0",
  "userAgent": "aws-sdk-java/2.30.32 Linux/5.10.233-224.894.amzn2.x86_64",
  "requestParameters": {
    "sessionArn": "arn:aws:mpa:us-east-1:111122223333:session/ExampleTeam-a1b2c3d4-5678-90ab-cdef-EXAMPLE11111/a1b2c3d4-5678-90ab-cdef-EXAMPLE22222"
  },
  "responseElements": null,
  "requestID": "a1b2c3d4-5678-90ab-cdef-EXAMPLE33333",
  "eventID": "a1b2c3d4-5678-90ab-cdef-EXAMPLE44444",
  "readOnly": true,
  "resources": [
    {
      "accountId": "111122223333",
      "type": "AWS::MPA::ApprovalTeam",
      "ARN": "arn:aws:mpa:us-east-1:111122223333:approval-team/ExampleTeam-a1b2c3d4-5678-90ab-cdef-EXAMPLE11111"
    },
    {
      "accountId": "111122223333",
      "type": "AWS::MPA::Session",
      "ARN": "arn:aws:mpa:us-east-1:111122223333:session/ExampleTeam-a1b2c3d4-5678-90ab-cdef-EXAMPLE11111/a1b2c3d4-5678-90ab-cdef-EXAMPLE22222"
    }
  ],
  "eventType": "AwsApiCall",
  "managementEvent": true,
  "recipientAccountId": "111122223333",
  "eventCategory": "Management",
  "tlsDetails": {
    "tlsVersion": "TLSv1.3",
    "cipherSuite": "TLS_AES_128_GCM_SHA256",
    "clientProvidedHostHeader": "multi-party-approval.us-east-1.amazonaws.com"
  }
}
```

ListApprovalTeams (Success)
The following example shows a CloudTrail event that demonstrates the `ListApprovalTeams` operation.

```
{
  "eventVersion": "1.10",
  "userIdentity": {
    "type": "AssumedRole",
    "principalId": "AROA123456789EXAMPLE:ExampleRole-mpa",
    "arn": "arn:aws:sts::111122223333:assumed-role/ExampleRole/ExampleRole-mpa",
    "accountId": "111122223333",
    "accessKeyId": "AKIA1234567890EXAMPLE",
    "sessionContext": {
      "sessionIssuer": {
        "type": "Role",
        "principalId": "AROA123456789EXAMPLE",
        "arn": "arn:aws:iam::111122223333:role/ExampleRole",
        "accountId": "111122223333",
        "userName": "ExampleRole"
      },
      "attributes": {
        "creationDate": "2025-03-11T00:04:14Z",
        "mfaAuthenticated": "false"
      }
    }
  },
  "eventTime": "2025-03-11T00:04:14Z",
  "eventSource": "multi-party-approval.amazonaws.com",
  "eventName": "ListApprovalTeams",
  "awsRegion": "us-east-1",
  "sourceIPAddress": "192.0.2.0",
  "userAgent": "aws-sdk-java/2.30.32 Linux/5.10.233-224.894.amzn2.x86_64",
  "requestParameters": {
    "maxResults": 1
  },
  "responseElements": null,
  "requestID": "a1b2c3d4-5678-90ab-cdef-EXAMPLE55555",
  "eventID": "a1b2c3d4-5678-90ab-cdef-EXAMPLE66666",
  "readOnly": true,
  "eventType": "AwsApiCall",
  "managementEvent": true,
  "recipientAccountId": "111122223333",
  "eventCategory": "Management",
  "tlsDetails": {
    "tlsVersion": "TLSv1.3",
    "cipherSuite": "TLS_AES_128_GCM_SHA256",
    "clientProvidedHostHeader": "multi-party-approval.us-east-1.amazonaws.com"
  }
}
```

ListIdentitySources (Success)
The following example shows a CloudTrail event that demonstrates the `ListIdentitySources` operation.

```
{
  "eventVersion": "1.10",
  "userIdentity": {
    "type": "AssumedRole",
    "principalId": "AROA123456789EXAMPLE:ExampleRole-mpa",
    "arn": "arn:aws:sts::111122223333:assumed-role/ExampleRole/ExampleRole-mpa",
    "accountId": "111122223333",
    "accessKeyId": "AKIA1234567890EXAMPLE",
    "sessionContext": {
      "sessionIssuer": {
        "type": "Role",
        "principalId": "AROA123456789EXAMPLE",
        "arn": "arn:aws:iam::111122223333:role/ExampleRole",
        "accountId": "111122223333",
        "userName": "ExampleRole"
      },
      "attributes": {
        "creationDate": "2025-03-10T23:59:07Z",
        "mfaAuthenticated": "false"
      }
    }
  },
  "eventTime": "2025-03-10T23:59:09Z",
  "eventSource": "multi-party-approval.amazonaws.com",
  "eventName": "ListIdentitySources",
  "awsRegion": "us-east-1",
  "sourceIPAddress": "192.0.2.0",
  "userAgent": "aws-sdk-java/2.30.32 Linux/5.10.233-224.894.amzn2.x86_64",
  "requestParameters": null,
  "responseElements": null,
  "requestID": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
  "eventID": "a1b2c3d4-5678-90ab-cdef-EXAMPLE22222",
  "readOnly": true,
  "eventType": "AwsApiCall",
  "managementEvent": true,
  "recipientAccountId": "111122223333",
  "eventCategory": "Management",
  "tlsDetails": {
    "tlsVersion": "TLSv1.3",
    "cipherSuite": "TLS_AES_128_GCM_SHA256",
    "clientProvidedHostHeader": "multi-party-approval.us-east-1.amazonaws.com"
  }
}
```

ListPolicies (Success)
The following example shows a CloudTrail event that demonstrates the `ListPolicies` operation.

```
{
  "eventVersion": "1.10",
  "userIdentity": {
    "type": "AssumedRole",
    "principalId": "AROA123456789EXAMPLE:ExampleRole-mpa",
    "arn": "arn:aws:sts::111122223333:assumed-role/ExampleRole/ExampleRole-mpa",
    "accountId": "111122223333",
    "accessKeyId": "AKIA1234567890EXAMPLE",
    "sessionContext": {
      "sessionIssuer": {
        "type": "Role",
        "principalId": "AROA123456789EXAMPLE",
        "arn": "arn:aws:iam::111122223333:role/ExampleRole",
        "accountId": "111122223333",
        "userName": "ExampleRole"
      },
      "attributes": {
        "creationDate": "2025-03-11T00:05:38Z",
        "mfaAuthenticated": "false"
      }
    }
  },
  "eventTime": "2025-03-11T00:05:38Z",
  "eventSource": "multi-party-approval.amazonaws.com",
  "eventName": "ListPolicies",
  "awsRegion": "us-east-1",
  "sourceIPAddress": "192.0.2.0",
  "userAgent": "aws-sdk-java/2.30.32 Linux/5.10.233-224.894.amzn2.x86_64",
  "requestParameters": null,
  "responseElements": null,
  "requestID": "a1b2c3d4-5678-90ab-cdef-EXAMPLE33333",
  "eventID": "a1b2c3d4-5678-90ab-cdef-EXAMPLE44444",
  "readOnly": true,
  "eventType": "AwsApiCall",
  "managementEvent": true,
  "recipientAccountId": "111122223333",
  "eventCategory": "Management",
  "tlsDetails": {
    "tlsVersion": "TLSv1.3",
    "cipherSuite": "TLS_AES_128_GCM_SHA256",
    "clientProvidedHostHeader": "multi-party-approval.us-east-1.amazonaws.com"
  }
}
```

ListPolicyVersions (Success)
The following example shows a CloudTrail event that demonstrates the `ListPolicyVersions` operation.

```
{
  "eventVersion": "1.10",
  "userIdentity": {
    "type": "AssumedRole",
    "principalId": "AROA123456789EXAMPLE:ExampleRole-mpa",
    "arn": "arn:aws:sts::111122223333:assumed-role/ExampleRole/ExampleRole-mpa",
    "accountId": "111122223333",
    "accessKeyId": "AKIA1234567890EXAMPLE",
    "sessionContext": {
      "sessionIssuer": {
        "type": "Role",
        "principalId": "AROA123456789EXAMPLE",
        "arn": "arn:aws:iam::111122223333:role/ExampleRole",
        "accountId": "111122223333",
        "userName": "ExampleRole"
      },
      "attributes": {
        "creationDate": "2025-03-11T00:06:06Z",
        "mfaAuthenticated": "false"
      }
    }
  },
  "eventTime": "2025-03-11T00:06:06Z",
  "eventSource": "multi-party-approval.amazonaws.com",
  "eventName": "ListPolicyVersions",
  "awsRegion": "us-east-1",
  "sourceIPAddress": "192.0.2.0",
  "userAgent": "aws-sdk-java/2.30.32 Linux/5.10.233-224.894.amzn2.x86_64",
  "requestParameters": {
    "policyArn": "arn:aws:mpa:::aws:policy/backup.amazonaws.com/CreateRestoreAccessVault"
  },
  "responseElements": null,
  "requestID": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
  "eventID": "a1b2c3d4-5678-90ab-cdef-EXAMPLE22222",
  "readOnly": true,
  "eventType": "AwsApiCall",
  "managementEvent": true,
  "recipientAccountId": "111122223333",
  "eventCategory": "Management",
  "tlsDetails": {
    "tlsVersion": "TLSv1.3",
    "cipherSuite": "TLS_AES_128_GCM_SHA256",
    "clientProvidedHostHeader": "multi-party-approval.us-east-1.amazonaws.com"
  }
}
```

ListResourcePolicies (Success)
The following example shows a CloudTrail event that demonstrates the `ListResourcePolicies` operation.

```
{
  "eventVersion": "1.10",
  "userIdentity": {
    "type": "AssumedRole",
    "principalId": "AROA123456789EXAMPLE:ExampleRole-mpa",
    "arn": "arn:aws:sts::111122223333:assumed-role/ExampleRole/ExampleRole-mpa",
    "accountId": "111122223333",
    "accessKeyId": "AKIA1234567890EXAMPLE",
    "sessionContext": {
      "sessionIssuer": {
        "type": "Role",
        "principalId": "AROA123456789EXAMPLE",
        "arn": "arn:aws:iam::111122223333:role/ExampleRole",
        "accountId": "111122223333",
        "userName": "ExampleRole"
      },
      "attributes": {
        "creationDate": "2025-03-09T18:42:04Z",
        "mfaAuthenticated": "false"
      }
    }
  },
  "eventTime": "2025-03-09T18:42:04Z",
  "eventSource": "multi-party-approval.amazonaws.com",
  "eventName": "ListResourcePolicies",
  "awsRegion": "us-east-1",
  "sourceIPAddress": "192.0.2.0",
  "userAgent": "aws-sdk-java/2.30.32 Linux/5.10.233-224.894.amzn2.x86_64",
  "requestParameters": {
    "resourceArn": "arn:aws:mpa:us-east-1:111122223333:approval-team/ExampleTeam-a1b2c3d4-5678-90ab-cdef-EXAMPLE11111"
  },
  "responseElements": null,
  "requestID": "a1b2c3d4-5678-90ab-cdef-EXAMPLE33333",
  "eventID": "a1b2c3d4-5678-90ab-cdef-EXAMPLE44444",
  "readOnly": true,
  "resources": [
    {
      "type": "AWS::IAM::PolicyVersion",
      "ARN": "arn:aws:mpa:::aws:policy/backup.amazonaws.com/CreateRestoreAccessVault/1"
    },
    {
      "accountId": "111122223333",
      "type": "AWS::MPA::ApprovalTeam",
      "ARN": "arn:aws:mpa:us-east-1:111122223333:approval-team/ExampleTeam-a1b2c3d4-5678-90ab-cdef-EXAMPLE11111"
    }
  ],
  "eventType": "AwsApiCall",
  "managementEvent": true,
  "recipientAccountId": "111122223333",
  "eventCategory": "Management",
  "tlsDetails": {
    "tlsVersion": "TLSv1.3",
    "cipherSuite": "TLS_AES_128_GCM_SHA256",
    "clientProvidedHostHeader": "multi-party-approval.us-east-1.amazonaws.com"
  }
}
```

ListSessions (Success)
The following example shows a CloudTrail event that demonstrates the `ListSessions` operation.

```
{
  "eventVersion": "1.10",
  "userIdentity": {
    "type": "AssumedRole",
    "principalId": "AROA123456789EXAMPLE:ExampleRole-mpa",
    "arn": "arn:aws:sts::111122223333:assumed-role/ExampleRole/ExampleRole-mpa",
    "accountId": "111122223333",
    "accessKeyId": "AKIA1234567890EXAMPLE",
    "sessionContext": {
      "sessionIssuer": {
        "type": "Role",
        "principalId": "AROA123456789EXAMPLE",
        "arn": "arn:aws:iam::111122223333:role/ExampleRole",
        "accountId": "111122223333",
        "userName": "ExampleRole"
      },
      "attributes": {
        "creationDate": "2025-03-11T00:04:14Z",
        "mfaAuthenticated": "false"
      }
    }
  },
  "eventTime": "2025-03-11T00:04:14Z",
  "eventSource": "multi-party-approval.amazonaws.com",
  "eventName": "ListSessions",
  "awsRegion": "us-east-1",
  "sourceIPAddress": "192.0.2.0",
  "userAgent": "aws-sdk-java/2.30.32 Linux/5.10.233-224.894.amzn2.x86_64",
  "requestParameters": {
    "approvalTeamArn": "arn:aws:mpa:us-east-1:111122223333:approval-team/ExampleTeam-a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
    "maxResults": 100,
    "filters": [
      {
        "fieldName": "InitiationTime",
        "operator": "GTE",
        "value": "2025-03-11T00:04:14.495844317Z"
      }
    ]
  },
  "responseElements": null,
  "requestID": "a1b2c3d4-5678-90ab-cdef-EXAMPLE22222",
  "eventID": "a1b2c3d4-5678-90ab-cdef-EXAMPLE33333",
  "readOnly": true,
  "resources": [
    {
      "accountId": "111122223333",
      "type": "AWS::MPA::ApprovalTeam",
      "ARN": "arn:aws:mpa:us-east-1:111122223333:approval-team/ExampleTeam-a1b2c3d4-5678-90ab-cdef-EXAMPLE11111"
    }
  ],
  "eventType": "AwsApiCall",
  "managementEvent": true,
  "recipientAccountId": "111122223333",
  "eventCategory": "Management",
  "tlsDetails": {
    "tlsVersion": "TLSv1.3",
    "cipherSuite": "TLS_AES_128_GCM_SHA256",
    "clientProvidedHostHeader": "multi-party-approval.us-east-1.amazonaws.com"
  }
}
```

ListTagsForResource (Success)
The following example shows a CloudTrail event that demonstrates the `ListTagsForResource` operation.

```
{
  "eventVersion": "1.10",
  "userIdentity": {
    "type": "AssumedRole",
    "principalId": "AROA123456789EXAMPLE:ExampleRole-mpa",
    "arn": "arn:aws:sts::111122223333:assumed-role/ExampleRole/ExampleRole-mpa",
    "accountId": "111122223333",
    "accessKeyId": "AKIA1234567890EXAMPLE",
    "sessionContext": {
      "sessionIssuer": {
        "type": "Role",
        "principalId": "AROA123456789EXAMPLE",
        "arn": "arn:aws:iam::111122223333:role/ExampleRole",
        "accountId": "111122223333",
        "userName": "ExampleRole"
      },
      "attributes": {
        "creationDate": "2025-03-11T00:05:00Z",
        "mfaAuthenticated": "false"
      }
    }
  },
  "eventTime": "2025-03-11T00:05:00Z",
  "eventSource": "multi-party-approval.amazonaws.com",
  "eventName": "ListTagsForResource",
  "awsRegion": "us-east-1",
  "sourceIPAddress": "192.0.2.0",
  "userAgent": "aws-sdk-java/2.30.32 Linux/5.10.233-224.894.amzn2.x86_64",
  "requestParameters": {
    "resourceArn": "arn:aws:mpa:us-east-1:111122223333:approval-team/ExampleTeam-a1b2c3d4-5678-90ab-cdef-EXAMPLE11111"
  },
  "responseElements": null,
  "requestID": "a1b2c3d4-5678-90ab-cdef-EXAMPLE44444",
  "eventID": "a1b2c3d4-5678-90ab-cdef-EXAMPLE55555",
  "readOnly": true,
  "eventType": "AwsApiCall",
  "managementEvent": true,
  "recipientAccountId": "111122223333",
  "eventCategory": "Management",
  "tlsDetails": {
    "tlsVersion": "TLSv1.3",
    "cipherSuite": "TLS_AES_128_GCM_SHA256",
    "clientProvidedHostHeader": "multi-party-approval.us-east-1.amazonaws.com"
  }
}
```

PutResourcePolicy (Success)
The following example shows a CloudTrail event that demonstrates the `PutResourcePolicy` operation.

```
{
  "eventVersion": "1.10",
  "userIdentity": {
    "type": "AssumedRole",
    "principalId": "AROA123456789EXAMPLE:ExampleRole-mpa",
    "arn": "arn:aws:sts::111122223333:assumed-role/ExampleRole/ExampleRole-mpa",
    "accountId": "111122223333",
    "accessKeyId": "AKIA1234567890EXAMPLE",
    "sessionContext": {
      "sessionIssuer": {
        "type": "Role",
        "principalId": "AROA123456789EXAMPLE",
        "arn": "arn:aws:iam::111122223333:role/ExampleRole",
        "accountId": "111122223333",
        "userName": "ExampleRole"
      },
      "attributes": {
        "creationDate": "2025-03-11T17:28:00Z",
        "mfaAuthenticated": "false"
      }
    }
  },
  "eventTime": "2025-03-11T18:01:22Z",
  "eventSource": "multi-party-approval.amazonaws.com",
  "eventName": "PutResourcePolicy",
  "awsRegion": "us-east-1",
  "sourceIPAddress": "192.0.2.0",
  "userAgent": "aws-cli/2.15.13 Python/3.11.6 Darwin/24.3.0",
  "requestParameters": {
    "resourceArn": "arn:aws:mpa:us-east-1:111122223333:approval-team/ExampleTeam-a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
    "policyDocument": "{}",
    "policyType": "AWS_MANAGED",
    "policyName": "ExamplePolicy"
  },
  "responseElements": {
    "resourceArn": "arn:aws:mpa:us-east-1:111122223333:approval-team/ExampleTeam-a1b2c3d4-5678-90ab-cdef-EXAMPLE11111"
  },
  "requestID": "a1b2c3d4-5678-90ab-cdef-EXAMPLE22222",
  "eventID": "a1b2c3d4-5678-90ab-cdef-EXAMPLE33333",
  "readOnly": false,
  "resources": [
    {
      "accountId": "111122223333",
      "type": "AWS::MPA::ApprovalTeam",
      "ARN": "arn:aws:mpa:us-east-1:111122223333:approval-team/ExampleTeam-a1b2c3d4-5678-90ab-cdef-EXAMPLE11111"
    }
  ],
  "eventType": "AwsApiCall",
  "managementEvent": true,
  "recipientAccountId": "111122223333",
  "eventCategory": "Management",
  "tlsDetails": {
    "tlsVersion": "TLSv1.3",
    "cipherSuite": "TLS_AES_128_GCM_SHA256",
    "clientProvidedHostHeader": "multi-party-approval.us-east-1.amazonaws.com"
  }
}
```

StartActiveApprovalTeamDeletion (Success)
The following example shows a CloudTrail event that demonstrates the `StartActiveApprovalTeamDeletion` operation.

```
{
  "eventVersion": "1.10",
  "userIdentity": {
    "type": "AssumedRole",
    "principalId": "AROA123456789EXAMPLE:ExampleRole-mpa",
    "arn": "arn:aws:sts::111122223333:assumed-role/ExampleRole/ExampleRole-mpa",
    "accountId": "111122223333",
    "accessKeyId": "AKIA1234567890EXAMPLE",
    "sessionContext": {
      "sessionIssuer": {
        "type": "Role",
        "principalId": "AROA123456789EXAMPLE",
        "arn": "arn:aws:iam::111122223333:role/ExampleRole",
        "accountId": "111122223333",
        "userName": "ExampleRole"
      },
      "attributes": {
        "creationDate": "2025-03-11T00:08:55Z",
        "mfaAuthenticated": "false"
      }
    }
  },
  "eventTime": "2025-03-11T00:08:55Z",
  "eventSource": "multi-party-approval.amazonaws.com",
  "eventName": "StartActiveApprovalTeamDeletion",
  "awsRegion": "us-east-1",
  "sourceIPAddress": "192.0.2.0",
  "userAgent": "aws-sdk-java/2.30.32 Linux/5.10.233-224.894.amzn2.x86_64",
  "requestParameters": {
    "arn": "arn:aws:mpa:us-east-1:111122223333:approval-team/ExampleTeam-a1b2c3d4-5678-90ab-cdef-EXAMPLE11111"
  },
  "responseElements": {
    "deletionStartTime": "Mar 11, 2025, 12:08:55 AM"
  },
  "requestID": "a1b2c3d4-5678-90ab-cdef-EXAMPLE44444",
  "eventID": "a1b2c3d4-5678-90ab-cdef-EXAMPLE55555",
  "readOnly": false,
  "resources": [
    {
      "accountId": "111122223333",
      "type": "AWS::MPA::ApprovalTeam",
      "ARN": "arn:aws:mpa:us-east-1:111122223333:approval-team/ExampleTeam-a1b2c3d4-5678-90ab-cdef-EXAMPLE11111"
    }
  ],
  "eventType": "AwsApiCall",
  "managementEvent": true,
  "recipientAccountId": "111122223333",
  "eventCategory": "Management",
  "tlsDetails": {
    "tlsVersion": "TLSv1.3",
    "cipherSuite": "TLS_AES_128_GCM_SHA256",
    "clientProvidedHostHeader": "multi-party-approval.us-east-1.amazonaws.com"
  }
}
```

StartSession (Success)
The following example shows a CloudTrail event that demonstrates the `StartSession` operation.

```
{
  "eventVersion": "1.10",
  "userIdentity": {
    "type": "AssumedRole",
    "principalId": "AROA123456789EXAMPLE:ExampleRole-mpa",
    "arn": "arn:aws:sts::111122223333:assumed-role/ExampleRole/ExampleRole-mpa",
    "accountId": "111122223333",
    "accessKeyId": "AKIA1234567890EXAMPLE",
    "sessionContext": {
      "sessionIssuer": {
        "type": "Role",
        "principalId": "AROA123456789EXAMPLE",
        "arn": "arn:aws:iam::111122223333:role/ExampleRole",
        "accountId": "111122223333",
        "userName": "ExampleRole"
      },
      "attributes": {
        "creationDate": "2025-03-07T16:37:51Z",
        "mfaAuthenticated": "false"
      }
    }
  },
  "eventTime": "2025-03-07T16:37:51Z",
  "eventSource": "multi-party-approval.amazonaws.com",
  "eventName": "StartSession",
  "awsRegion": "us-east-1",
  "sourceIPAddress": "192.0.2.0",
  "userAgent": "aws-sdk-java/2.30.32 Linux/5.10.233-224.894.amzn2.x86_64",
  "requestParameters": {
    "sessionId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
    "initiationTime": "Mar 7, 2025, 4:37:51 PM",
    "deduplicationToken": "a1b2c3d4e5f6g7h8",
    "approvalTeamArn": "arn:aws:mpa:us-east-1:111122223333:approval-team/ExampleTeam-a1b2c3d4-5678-90ab-cdef-EXAMPLE22222",
    "durationMinutes": 60,
    "actionName": "example:action",
    "description": "HIDDEN_DUE_TO_SECURITY_REASONS",
    "protectedResourceArn": "arn:aws:ec2:us-east-1:111122223333:vpc/vpc-a1b2c3d4e5f6g7h8i",
    "metadata": "HIDDEN_DUE_TO_SECURITY_REASONS",
    "requesterRegion": "us-east-1",
    "requesterComment": "HIDDEN_DUE_TO_SECURITY_REASONS"
  },
  "responseElements": {
    "arn": "arn:aws:mpa:us-east-1:111122223333:session/ExampleTeam-a1b2c3d4-5678-90ab-cdef-EXAMPLE22222/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111"
  },
  "requestID": "a1b2c3d4-5678-90ab-cdef-EXAMPLE33333",
  "eventID": "a1b2c3d4-5678-90ab-cdef-EXAMPLE44444",
  "readOnly": false,
  "resources": [
    {
      "accountId": "111122223333",
      "type": "AWS::MPA::ApprovalTeam",
      "ARN": "arn:aws:mpa:us-east-1:111122223333:approval-team/ExampleTeam-a1b2c3d4-5678-90ab-cdef-EXAMPLE22222"
    }
  ],
  "eventType": "AwsApiCall",
  "managementEvent": true,
  "recipientAccountId": "111122223333",
  "eventCategory": "Management",
  "tlsDetails": {
    "tlsVersion": "TLSv1.3",
    "cipherSuite": "TLS_AES_128_GCM_SHA256",
    "clientProvidedHostHeader": "multi-party-approval.us-east-1.amazonaws.com"
  }
}
```

TagResource (Success)
The following example shows a CloudTrail event that demonstrates the `TagResource` operation.

```
{
  "eventVersion": "1.10",
  "userIdentity": {
    "type": "AssumedRole",
    "principalId": "AROA123456789EXAMPLE:ExampleRole-mpa",
    "arn": "arn:aws:sts::111122223333:assumed-role/ExampleRole/ExampleRole-mpa",
    "accountId": "111122223333",
    "accessKeyId": "AKIA1234567890EXAMPLE",
    "sessionContext": {
      "sessionIssuer": {
        "type": "Role",
        "principalId": "AROA123456789EXAMPLE",
        "arn": "arn:aws:iam::111122223333:role/ExampleRole",
        "accountId": "111122223333",
        "userName": "ExampleRole"
      },
      "attributes": {
        "creationDate": "2025-03-11T00:04:23Z",
        "mfaAuthenticated": "false"
      }
    }
  },
  "eventTime": "2025-03-11T00:04:23Z",
  "eventSource": "multi-party-approval.amazonaws.com",
  "eventName": "TagResource",
  "awsRegion": "us-east-1",
  "sourceIPAddress": "192.0.2.0",
  "userAgent": "aws-sdk-java/2.30.32 Linux/5.10.233-224.894.amzn2.x86_64",
  "requestParameters": {
    "resourceArn": "arn:aws:mpa:us-east-1:111122223333:approval-team/ExampleTeam-a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
    "tags": "HIDDEN_DUE_TO_SECURITY_REASONS"
  },
  "responseElements": null,
  "requestID": "a1b2c3d4-5678-90ab-cdef-EXAMPLE55555",
  "eventID": "a1b2c3d4-5678-90ab-cdef-EXAMPLE66666",
  "readOnly": false,
  "eventType": "AwsApiCall",
  "managementEvent": true,
  "recipientAccountId": "111122223333",
  "eventCategory": "Management",
  "tlsDetails": {
    "tlsVersion": "TLSv1.3",
    "cipherSuite": "TLS_AES_128_GCM_SHA256",
    "clientProvidedHostHeader": "multi-party-approval.us-east-1.amazonaws.com"
  }
}
```

UntagResource (Success)
The following example shows a CloudTrail event that demonstrates the `UntagResource` operation.

```
{
  "eventVersion": "1.10",
  "userIdentity": {
    "type": "AssumedRole",
    "principalId": "AROA123456789EXAMPLE:ExampleRole-mpa",
    "arn": "arn:aws:sts::111122223333:assumed-role/ExampleRole/ExampleRole-mpa",
    "accountId": "111122223333",
    "accessKeyId": "AKIA1234567890EXAMPLE",
    "sessionContext": {
      "sessionIssuer": {
        "type": "Role",
        "principalId": "AROA123456789EXAMPLE",
        "arn": "arn:aws:iam::111122223333:role/ExampleRole",
        "accountId": "111122223333",
        "userName": "ExampleRole"
      },
      "attributes": {
        "creationDate": "2025-03-11T00:04:31Z",
        "mfaAuthenticated": "false"
      }
    }
  },
  "eventTime": "2025-03-11T00:04:31Z",
  "eventSource": "multi-party-approval.amazonaws.com",
  "eventName": "UntagResource",
  "awsRegion": "us-east-1",
  "sourceIPAddress": "192.0.2.0",
  "userAgent": "aws-sdk-java/2.30.32 Linux/5.10.233-224.894.amzn2.x86_64",
  "requestParameters": {
    "resourceArn": "arn:aws:mpa:us-east-1:111122223333:approval-team/ExampleTeam-a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
    "tagKeys": "HIDDEN_DUE_TO_SECURITY_REASONS"
  },
  "responseElements": null,
  "requestID": "a1b2c3d4-5678-90ab-cdef-EXAMPLE22222",
  "eventID": "a1b2c3d4-5678-90ab-cdef-EXAMPLE33333",
  "readOnly": false,
  "eventType": "AwsApiCall",
  "managementEvent": true,
  "recipientAccountId": "111122223333",
  "eventCategory": "Management",
  "tlsDetails": {
    "tlsVersion": "TLSv1.3",
    "cipherSuite": "TLS_AES_128_GCM_SHA256",
    "clientProvidedHostHeader": "multi-party-approval.us-east-1.amazonaws.com"
  }
}
```

UpdateApprovalTeam (Success)
The following example shows a CloudTrail event that demonstrates the `UpdateApprovalTeam` operation.

```
{
  "eventVersion": "1.10",
  "userIdentity": {
    "type": "AssumedRole",
    "principalId": "AROA123456789EXAMPLE:ExampleRole-mpa",
    "arn": "arn:aws:sts::111122223333:assumed-role/ExampleRole/ExampleRole-mpa",
    "accountId": "111122223333",
    "accessKeyId": "AKIA1234567890EXAMPLE",
    "sessionContext": {
      "sessionIssuer": {
        "type": "Role",
        "principalId": "AROA123456789EXAMPLE",
        "arn": "arn:aws:iam::111122223333:role/ExampleRole",
        "accountId": "111122223333",
        "userName": "ExampleRole"
      },
      "attributes": {
        "creationDate": "2025-03-11T00:06:34Z",
        "mfaAuthenticated": "false"
      }
    }
  },
  "eventTime": "2025-03-11T00:06:34Z",
  "eventSource": "multi-party-approval.amazonaws.com",
  "eventName": "UpdateApprovalTeam",
  "awsRegion": "us-east-1",
  "sourceIPAddress": "192.0.2.0",
  "userAgent": "aws-sdk-java/2.30.32 Linux/5.10.233-224.894.amzn2.x86_64",
  "requestParameters": {
    "arn": "arn:aws:mpa:us-east-1:111122223333:approval-team/ExampleTeam-a1b2c3d4-5678-90ab-cdef-EXAMPLE11111"
  },
  "responseElements": {
    "versionId": "1234567890123"
  },
  "requestID": "a1b2c3d4-5678-90ab-cdef-EXAMPLE44444",
  "eventID": "a1b2c3d4-5678-90ab-cdef-EXAMPLE55555",
  "readOnly": false,
  "resources": [
    {
      "accountId": "111122223333",
      "type": "AWS::MPA::ApprovalTeam",
      "ARN": "arn:aws:mpa:us-east-1:111122223333:approval-team/ExampleTeam-a1b2c3d4-5678-90ab-cdef-EXAMPLE11111"
    }
  ],
  "eventType": "AwsApiCall",
  "managementEvent": true,
  "recipientAccountId": "111122223333",
  "eventCategory": "Management",
  "tlsDetails": {
    "tlsVersion": "TLSv1.3",
    "cipherSuite": "TLS_AES_128_GCM_SHA256",
    "clientProvidedHostHeader": "multi-party-approval.us-east-1.amazonaws.com"
  }
}
```

The following tabbed list displays some examples the access denied flow.

CreateIdentitySource (Error)
The following example shows a CloudTrail event that demonstrates an unsuccessful `CreateIdentitySource` operation due to insufficient permissions.

```
{
  "eventVersion": "1.10",
  "userIdentity": {
    "type": "AssumedRole",
    "principalId": "AROA123456789EXAMPLE:ExampleRole-mpa",
    "arn": "arn:aws:sts::111122223333:assumed-role/ExampleRole/ExampleRole-mpa",
    "accountId": "111122223333",
    "accessKeyId": "AKIA1234567890EXAMPLE",
    "sessionContext": {
      "sessionIssuer": {
        "type": "Role",
        "principalId": "AROA123456789EXAMPLE",
        "arn": "arn:aws:iam::111122223333:role/ExampleRole",
        "accountId": "111122223333",
        "userName": "ExampleRole"
      },
      "attributes": {
        "creationDate": "2025-03-22T01:09:56Z",
        "mfaAuthenticated": "false"
      }
    }
  },
  "eventTime": "2025-03-22T01:09:56Z",
  "eventSource": "multi-party-approval.amazonaws.com",
  "eventName": "CreateIdentitySource",
  "awsRegion": "us-east-1",
  "sourceIPAddress": "192.0.2.0",
  "userAgent": "aws-sdk-java/2.31.4 Linux/5.10.234-225.910.amzn2.x86_64",
  "errorCode": "AccessDenied",
  "errorMessage": "User: arn:aws:sts::111122223333:assumed-role/ExampleRole/ExampleRole-mpa is not authorized to perform: mpa:CreateIdentitySource on resource: arn:aws:mpa:us-east-1:111122223333:identity-source/IamIdentityCenter because no identity-based policy allows the mpa:CreateIdentitySource action",
  "requestParameters": null,
  "responseElements": null,
  "requestID": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
  "eventID": "a1b2c3d4-5678-90ab-cdef-EXAMPLE22222",
  "readOnly": false,
  "eventType": "AwsApiCall",
  "managementEvent": true,
  "recipientAccountId": "111122223333",
  "eventCategory": "Management",
  "tlsDetails": {
    "tlsVersion": "TLSv1.3",
    "cipherSuite": "TLS_AES_128_GCM_SHA256",
    "clientProvidedHostHeader": "multi-party-approval.us-east-1.amazonaws.com"
  }
}
```

GetIdentitySource (Error)
The following example shows a CloudTrail event that demonstrates an unsuccessful `GetIdentitySource` operation due to insufficient permissions.

```
{
  "eventVersion": "1.10",
  "userIdentity": {
    "type": "AssumedRole",
    "principalId": "AROA123456789EXAMPLE:ExampleRole-mpa",
    "arn": "arn:aws:sts::111122223333:assumed-role/ExampleRole/ExampleRole-mpa",
    "accountId": "111122223333",
    "accessKeyId": "AKIA1234567890EXAMPLE",
    "sessionContext": {
      "sessionIssuer": {
        "type": "Role",
        "principalId": "AROA123456789EXAMPLE",
        "arn": "arn:aws:iam::111122223333:role/ExampleRole",
        "accountId": "111122223333",
        "userName": "ExampleRole"
      },
      "attributes": {
        "creationDate": "2025-03-22T00:55:50Z",
        "mfaAuthenticated": "false"
      }
    }
  },
  "eventTime": "2025-03-22T00:55:50Z",
  "eventSource": "multi-party-approval.amazonaws.com",
  "eventName": "GetIdentitySource",
  "awsRegion": "us-east-1",
  "sourceIPAddress": "192.0.2.0",
  "userAgent": "aws-sdk-java/2.31.4 Linux/5.10.234-225.910.amzn2.x86_64",
  "errorCode": "AccessDenied",
  "errorMessage": "User: arn:aws:sts::111122223333:assumed-role/ExampleRole/ExampleRole-mpa is not authorized to perform: mpa:GetIdentitySource on resource: arn:aws:mpa:us-east-1:111122223333:identity-source/IamIdentityCenter because no identity-based policy allows the mpa:GetIdentitySource action",
  "requestParameters": null,
  "responseElements": null,
  "requestID": "a1b2c3d4-5678-90ab-cdef-EXAMPLE33333",
  "eventID": "a1b2c3d4-5678-90ab-cdef-EXAMPLE44444",
  "readOnly": true,
  "eventType": "AwsApiCall",
  "managementEvent": true,
  "recipientAccountId": "111122223333",
  "eventCategory": "Management",
  "tlsDetails": {
    "tlsVersion": "TLSv1.3",
    "cipherSuite": "TLS_AES_128_GCM_SHA256",
    "clientProvidedHostHeader": "multi-party-approval.us-east-1.amazonaws.com"
  }
}
```

DeleteIdentitySource (Error)
The following example shows a CloudTrail event that demonstrates an unsuccessful `DeleteIdentitySource` operation due to insufficient permissions.

```
{
  "eventVersion": "1.10",
  "userIdentity": {
    "type": "AssumedRole",
    "principalId": "AROA123456789EXAMPLE:ExampleRole-mpa",
    "arn": "arn:aws:sts::111122223333:assumed-role/ExampleRole/ExampleRole-mpa",
    "accountId": "111122223333",
    "accessKeyId": "AKIA1234567890EXAMPLE",
    "sessionContext": {
      "sessionIssuer": {
        "type": "Role",
        "principalId": "AROA123456789EXAMPLE",
        "arn": "arn:aws:iam::111122223333:role/ExampleRole",
        "accountId": "111122223333",
        "userName": "ExampleRole"
      },
      "attributes": {
        "creationDate": "2025-03-22T00:53:56Z",
        "mfaAuthenticated": "false"
      }
    }
  },
  "eventTime": "2025-03-22T00:53:56Z",
  "eventSource": "multi-party-approval.amazonaws.com",
  "eventName": "DeleteIdentitySource",
  "awsRegion": "us-east-1",
  "sourceIPAddress": "192.0.2.0",
  "userAgent": "aws-sdk-java/2.31.4 Linux/5.10.234-225.910.amzn2.x86_64",
  "errorCode": "AccessDenied",
  "errorMessage": "User: arn:aws:sts::111122223333:assumed-role/ExampleRole/ExampleRole-mpa is not authorized to perform: mpa:DeleteIdentitySource on resource: arn:aws:mpa:us-east-1:111122223333:identity-source/DummyIdentityCenter because no identity-based policy allows the mpa:DeleteIdentitySource action",
  "requestParameters": null,
  "responseElements": null,
  "requestID": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
  "eventID": "a1b2c3d4-5678-90ab-cdef-EXAMPLE22222",
  "readOnly": false,
  "eventType": "AwsApiCall",
  "managementEvent": true,
  "recipientAccountId": "111122223333",
  "eventCategory": "Management",
  "tlsDetails": {
    "tlsVersion": "TLSv1.3",
    "cipherSuite": "TLS_AES_128_GCM_SHA256",
    "clientProvidedHostHeader": "multi-party-approval.us-east-1.amazonaws.com"
  }
}
```

ListIdentitySources (Error)
The following example shows a CloudTrail event that demonstrates an unsuccessful `ListIdentitySources` operation due to insufficient permissions.

```
{
  "eventVersion": "1.10",
  "userIdentity": {
    "type": "AssumedRole",
    "principalId": "AROA123456789EXAMPLE:ExampleRole-mpa",
    "arn": "arn:aws:sts::111122223333:assumed-role/ExampleRole/ExampleRole-mpa",
    "accountId": "111122223333",
    "accessKeyId": "AKIA1234567890EXAMPLE",
    "sessionContext": {
      "sessionIssuer": {
        "type": "Role",
        "principalId": "AROA123456789EXAMPLE",
        "arn": "arn:aws:iam::111122223333:role/ExampleRole",
        "accountId": "111122223333",
        "userName": "ExampleRole"
      },
      "attributes": {
        "creationDate": "2025-03-22T00:55:50Z",
        "mfaAuthenticated": "false"
      }
    }
  },
  "eventTime": "2025-03-22T00:55:50Z",
  "eventSource": "multi-party-approval.amazonaws.com",
  "eventName": "ListIdentitySources",
  "awsRegion": "us-east-1",
  "sourceIPAddress": "192.0.2.0",
  "userAgent": "aws-sdk-java/2.31.4 Linux/5.10.234-225.910.amzn2.x86_64",
  "errorCode": "AccessDenied",
  "errorMessage": "User: arn:aws:sts::111122223333:assumed-role/ExampleRole/ExampleRole-mpa is not authorized to perform: mpa:ListIdentitySources on resource: arn:aws:mpa:us-east-1:111122223333:identity-source/* because no identity-based policy allows the mpa:ListIdentitySources action",
  "requestParameters": null,
  "responseElements": null,
  "requestID": "a1b2c3d4-5678-90ab-cdef-EXAMPLE33333",
  "eventID": "a1b2c3d4-5678-90ab-cdef-EXAMPLE44444",
  "readOnly": true,
  "eventType": "AwsApiCall",
  "managementEvent": true,
  "recipientAccountId": "111122223333",
  "eventCategory": "Management",
  "tlsDetails": {
    "tlsVersion": "TLSv1.3",
    "cipherSuite": "TLS_AES_128_GCM_SHA256",
    "clientProvidedHostHeader": "multi-party-approval.us-east-1.amazonaws.com"
  }
}
```

CreateApprovalTeam (Error)
The following example shows a CloudTrail event that demonstrates an unsuccessful `CreateApprovalTeam` operation due to insufficient permissions.

```
{
  "eventVersion": "1.10",
  "userIdentity": {
    "type": "AssumedRole",
    "principalId": "AROA123456789EXAMPLE:ExampleRole-mpa",
    "arn": "arn:aws:sts::111122223333:assumed-role/ExampleRole/ExampleRole-mpa",
    "accountId": "111122223333",
    "accessKeyId": "AKIA1234567890EXAMPLE",
    "sessionContext": {
      "sessionIssuer": {
        "type": "Role",
        "principalId": "AROA123456789EXAMPLE",
        "arn": "arn:aws:iam::111122223333:role/ExampleRole",
        "accountId": "111122223333",
        "userName": "ExampleRole"
      },
      "attributes": {
        "creationDate": "2025-03-22T00:56:18Z",
        "mfaAuthenticated": "false"
      }
    }
  },
  "eventTime": "2025-03-22T00:56:18Z",
  "eventSource": "multi-party-approval.amazonaws.com",
  "eventName": "CreateApprovalTeam",
  "awsRegion": "us-east-1",
  "sourceIPAddress": "192.0.2.0",
  "userAgent": "aws-sdk-java/2.31.4 Linux/5.10.234-225.910.amzn2.x86_64",
  "errorCode": "AccessDenied",
  "errorMessage": "User: arn:aws:sts::111122223333:assumed-role/ExampleRole/ExampleRole-mpa is not authorized to perform: mpa:CreateApprovalTeam on resource: arn:aws:mpa:us-east-1:111122223333:approval-team/ExampleTeam-a1b2c3d4-5678-90ab-cdef-EXAMPLE11111 because no identity-based policy allows the mpa:CreateApprovalTeam action",
  "requestParameters": null,
  "responseElements": null,
  "requestID": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
  "eventID": "a1b2c3d4-5678-90ab-cdef-EXAMPLE22222",
  "readOnly": false,
  "eventType": "AwsApiCall",
  "managementEvent": true,
  "recipientAccountId": "111122223333",
  "eventCategory": "Management",
  "tlsDetails": {
    "tlsVersion": "TLSv1.3",
    "cipherSuite": "TLS_AES_128_GCM_SHA256",
    "clientProvidedHostHeader": "multi-party-approval.us-east-1.amazonaws.com"
  }
}
```

UpdateApprovalTeam (Error)
The following example shows a CloudTrail event that demonstrates an unsuccessful `UpdateApprovalTeam` operation due to insufficient permissions.

```
{
  "eventVersion": "1.10",
  "userIdentity": {
    "type": "AssumedRole",
    "principalId": "AROA123456789EXAMPLE:ExampleRole-mpa",
    "arn": "arn:aws:sts::111122223333:assumed-role/ExampleRole/ExampleRole-mpa",
    "accountId": "111122223333",
    "accessKeyId": "AKIA1234567890EXAMPLE",
    "sessionContext": {
      "sessionIssuer": {
        "type": "Role",
        "principalId": "AROA123456789EXAMPLE",
        "arn": "arn:aws:iam::111122223333:role/ExampleRole",
        "accountId": "111122223333",
        "userName": "ExampleRole"
      },
      "attributes": {
        "creationDate": "2025-03-22T00:53:06Z",
        "mfaAuthenticated": "false"
      }
    }
  },
  "eventTime": "2025-03-22T00:55:09Z",
  "eventSource": "multi-party-approval.amazonaws.com",
  "eventName": "UpdateApprovalTeam",
  "awsRegion": "us-east-1",
  "sourceIPAddress": "192.0.2.0",
  "userAgent": "aws-sdk-java/2.31.4 Linux/5.10.234-225.910.amzn2.x86_64",
  "errorCode": "AccessDenied",
  "errorMessage": "User: arn:aws:sts::111122223333:assumed-role/ExampleRole/ExampleRole-mpa is not authorized to perform: mpa:UpdateApprovalTeam on resource: arn:aws:mpa:us-east-1:000000000000:approval-team/example-group because no resource-based policy allows the mpa:UpdateApprovalTeam action",
  "requestParameters": null,
  "responseElements": null,
  "requestID": "a1b2c3d4-5678-90ab-cdef-EXAMPLE33333",
  "eventID": "a1b2c3d4-5678-90ab-cdef-EXAMPLE44444",
  "readOnly": false,
  "eventType": "AwsApiCall",
  "managementEvent": true,
  "recipientAccountId": "111122223333",
  "eventCategory": "Management",
  "tlsDetails": {
    "tlsVersion": "TLSv1.3",
    "cipherSuite": "TLS_AES_128_GCM_SHA256",
    "clientProvidedHostHeader": "multi-party-approval.us-east-1.amazonaws.com"
  }
}
```

GetApprovalTeam (Error)
The following example shows a CloudTrail event that demonstrates an unsuccessful `GetApprovalTeam` operation due to insufficient permissions.

```
{
  "eventVersion": "1.10",
  "userIdentity": {
    "type": "AssumedRole",
    "principalId": "AROA123456789EXAMPLE:ExampleRole-mpa",
    "arn": "arn:aws:sts::111122223333:assumed-role/ExampleRole/ExampleRole-mpa",
    "accountId": "111122223333",
    "accessKeyId": "AKIA1234567890EXAMPLE",
    "sessionContext": {
      "sessionIssuer": {
        "type": "Role",
        "principalId": "AROA123456789EXAMPLE",
        "arn": "arn:aws:iam::111122223333:role/ExampleRole",
        "accountId": "111122223333",
        "userName": "ExampleRole"
      },
      "attributes": {
        "creationDate": "2025-03-22T00:56:18Z",
        "mfaAuthenticated": "false"
      }
    }
  },
  "eventTime": "2025-03-22T00:56:18Z",
  "eventSource": "multi-party-approval.amazonaws.com",
  "eventName": "GetApprovalTeam",
  "awsRegion": "us-east-1",
  "sourceIPAddress": "192.0.2.0",
  "userAgent": "aws-sdk-java/2.31.4 Linux/5.10.234-225.910.amzn2.x86_64",
  "errorCode": "AccessDenied",
  "errorMessage": "User: arn:aws:sts::111122223333:assumed-role/ExampleRole/ExampleRole-mpa is not authorized to perform: mpa:GetApprovalTeam on resource: arn:aws:mpa:us-east-1:111122223333:approval-team/ExampleTeam-a1b2c3d4-5678-90ab-cdef-EXAMPLE11111 because no identity-based policy allows the mpa:GetApprovalTeam action",
  "requestParameters": null,
  "responseElements": null,
  "requestID": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
  "eventID": "a1b2c3d4-5678-90ab-cdef-EXAMPLE22222",
  "readOnly": true,
  "eventType": "AwsApiCall",
  "managementEvent": true,
  "recipientAccountId": "111122223333",
  "eventCategory": "Management",
  "tlsDetails": {
    "tlsVersion": "TLSv1.3",
    "cipherSuite": "TLS_AES_128_GCM_SHA256",
    "clientProvidedHostHeader": "multi-party-approval.us-east-1.amazonaws.com"
  }
}
```

ListApprovalTeams (Error)
The following example shows a CloudTrail event that demonstrates an unsuccessful `ListApprovalTeams` operation due to insufficient permissions.

```
{
  "eventVersion": "1.10",
  "userIdentity": {
    "type": "AssumedRole",
    "principalId": "AROA123456789EXAMPLE:ExampleRole-mpa",
    "arn": "arn:aws:sts::111122223333:assumed-role/ExampleRole/ExampleRole-mpa",
    "accountId": "111122223333",
    "accessKeyId": "AKIA1234567890EXAMPLE",
    "sessionContext": {
      "sessionIssuer": {
        "type": "Role",
        "principalId": "AROA123456789EXAMPLE",
        "arn": "arn:aws:iam::111122223333:role/ExampleRole",
        "accountId": "111122223333",
        "userName": "ExampleRole"
      },
      "attributes": {
        "creationDate": "2025-03-22T00:54:25Z",
        "mfaAuthenticated": "false"
      }
    }
  },
  "eventTime": "2025-03-22T00:54:25Z",
  "eventSource": "multi-party-approval.amazonaws.com",
  "eventName": "ListApprovalTeams",
  "awsRegion": "us-east-1",
  "sourceIPAddress": "192.0.2.0",
  "userAgent": "aws-sdk-java/2.31.4 Linux/5.10.234-225.910.amzn2.x86_64",
  "errorCode": "AccessDenied",
  "errorMessage": "User: arn:aws:sts::111122223333:assumed-role/ExampleRole/ExampleRole-mpa is not authorized to perform: mpa:ListApprovalTeams on resource: arn:aws:mpa:us-east-1:111122223333:approval-team/* because no identity-based policy allows the mpa:ListApprovalTeams action",
  "requestParameters": null,
  "responseElements": null,
  "requestID": "a1b2c3d4-5678-90ab-cdef-EXAMPLE33333",
  "eventID": "a1b2c3d4-5678-90ab-cdef-EXAMPLE44444",
  "readOnly": true,
  "eventType": "AwsApiCall",
  "managementEvent": true,
  "recipientAccountId": "111122223333",
  "eventCategory": "Management",
  "tlsDetails": {
    "tlsVersion": "TLSv1.3",
    "cipherSuite": "TLS_AES_128_GCM_SHA256",
    "clientProvidedHostHeader": "multi-party-approval.us-east-1.amazonaws.com"
  }
}
```

StartActiveApprovalTeamDeletion (Error)
The following example shows a CloudTrail event that demonstrates an unsuccessful `StartActiveApprovalTeamDeletion` operation due to insufficient permissions.

```
{
  "eventVersion": "1.10",
  "userIdentity": {
    "type": "AssumedRole",
    "principalId": "AROA123456789EXAMPLE:ExampleRole-mpa",
    "arn": "arn:aws:sts::111122223333:assumed-role/ExampleRole/ExampleRole-mpa",
    "accountId": "111122223333",
    "accessKeyId": "AKIA1234567890EXAMPLE",
    "sessionContext": {
      "sessionIssuer": {
        "type": "Role",
        "principalId": "AROA123456789EXAMPLE",
        "arn": "arn:aws:iam::111122223333:role/ExampleRole",
        "accountId": "111122223333",
        "userName": "ExampleRole"
      },
      "attributes": {
        "creationDate": "2025-03-22T00:53:06Z",
        "mfaAuthenticated": "false"
      }
    }
  },
  "eventTime": "2025-03-22T00:53:54Z",
  "eventSource": "multi-party-approval.amazonaws.com",
  "eventName": "StartActiveApprovalTeamDeletion",
  "awsRegion": "us-east-1",
  "sourceIPAddress": "192.0.2.0",
  "userAgent": "aws-sdk-java/2.31.4 Linux/5.10.234-225.910.amzn2.x86_64",
  "errorCode": "AccessDenied",
  "errorMessage": "User: arn:aws:sts::111122223333:assumed-role/ExampleRole/ExampleRole-mpa is not authorized to perform: mpa:StartActiveApprovalTeamDeletion on resource: arn:aws:mpa:us-east-1:000000000000:approval-team/example-group because no resource-based policy allows the mpa:StartActiveApprovalTeamDeletion action",
  "requestParameters": null,
  "responseElements": null,
  "requestID": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
  "eventID": "a1b2c3d4-5678-90ab-cdef-EXAMPLE22222",
  "readOnly": false,
  "eventType": "AwsApiCall",
  "managementEvent": true,
  "recipientAccountId": "111122223333",
  "eventCategory": "Management",
  "tlsDetails": {
    "tlsVersion": "TLSv1.3",
    "cipherSuite": "TLS_AES_128_GCM_SHA256",
    "clientProvidedHostHeader": "multi-party-approval.us-east-1.amazonaws.com"
  }
}
```

DeleteInactiveApprovalTeamVersion (Error)
The following example shows a CloudTrail event that demonstrates an unsuccessful `DeleteInactiveApprovalTeamVersion` operation due to insufficient permissions.

```
{
  "eventVersion": "1.10",
  "userIdentity": {
    "type": "AssumedRole",
    "principalId": "AROA123456789EXAMPLE:ExampleRole-mpa",
    "arn": "arn:aws:sts::111122223333:assumed-role/ExampleRole/ExampleRole-mpa",
    "accountId": "111122223333",
    "accessKeyId": "AKIA1234567890EXAMPLE",
    "sessionContext": {
      "sessionIssuer": {
        "type": "Role",
        "principalId": "AROA123456789EXAMPLE",
        "arn": "arn:aws:iam::111122223333:role/ExampleRole",
        "accountId": "111122223333",
        "userName": "ExampleRole"
      },
      "attributes": {
        "creationDate": "2025-03-22T00:56:18Z",
        "mfaAuthenticated": "false"
      }
    }
  },
  "eventTime": "2025-03-22T00:56:18Z",
  "eventSource": "multi-party-approval.amazonaws.com",
  "eventName": "DeleteInactiveApprovalTeamVersion",
  "awsRegion": "us-east-1",
  "sourceIPAddress": "192.0.2.0",
  "userAgent": "aws-sdk-java/2.31.4 Linux/5.10.234-225.910.amzn2.x86_64",
  "errorCode": "AccessDenied",
  "errorMessage": "User: arn:aws:sts::111122223333:assumed-role/ExampleRole/ExampleRole-mpa is not authorized to perform: mpa:DeleteInactiveApprovalTeamVersion on resource: arn:aws:mpa:us-east-1:111122223333:approval-team/example-group because no identity-based policy allows the mpa:DeleteInactiveApprovalTeamVersion action",
  "requestParameters": null,
  "responseElements": null,
  "requestID": "a1b2c3d4-5678-90ab-cdef-EXAMPLE33333",
  "eventID": "a1b2c3d4-5678-90ab-cdef-EXAMPLE44444",
  "readOnly": false,
  "eventType": "AwsApiCall",
  "managementEvent": true,
  "recipientAccountId": "111122223333",
  "eventCategory": "Management",
  "tlsDetails": {
    "tlsVersion": "TLSv1.3",
    "cipherSuite": "TLS_AES_128_GCM_SHA256",
    "clientProvidedHostHeader": "multi-party-approval.us-east-1.amazonaws.com"
  }
}
```

GetSession (Error)
The following example shows a CloudTrail event that demonstrates an unsuccessful `GetSession` operation due to an explicit deny in an identity-based policy.

```
{
  "eventVersion": "1.10",
  "userIdentity": {
    "type": "AssumedRole",
    "principalId": "AROA123456789EXAMPLE:ExampleRole-mpa",
    "arn": "arn:aws:sts::111122223333:assumed-role/ExampleRole/ExampleRole-mpa",
    "accountId": "111122223333",
    "accessKeyId": "AKIA1234567890EXAMPLE",
    "sessionContext": {
      "sessionIssuer": {
        "type": "Role",
        "principalId": "AROA123456789EXAMPLE",
        "arn": "arn:aws:iam::111122223333:role/ExampleRole",
        "accountId": "111122223333",
        "userName": "ExampleRole"
      },
      "attributes": {
        "creationDate": "2025-03-22T00:53:16Z",
        "mfaAuthenticated": "false"
      }
    }
  },
  "eventTime": "2025-03-22T00:53:16Z",
  "eventSource": "multi-party-approval.amazonaws.com",
  "eventName": "GetSession",
  "awsRegion": "us-east-1",
  "sourceIPAddress": "192.0.2.0",
  "userAgent": "aws-sdk-java/2.31.4 Linux/5.10.234-225.910.amzn2.x86_64",
  "errorCode": "AccessDenied",
  "errorMessage": "User: arn:aws:sts::111122223333:assumed-role/ExampleRole/ExampleRole-mpa is not authorized to perform: mpa:GetSession on resource: arn:aws:mpa:us-east-1:111122223333:session/ExampleSession-a1b2c3d4-5678-90ab-cdef-EXAMPLE11111/a1b2c3d4-5678-90ab-cdef-EXAMPLE22222 with an explicit deny in an identity-based policy",
  "requestParameters": null,
  "responseElements": null,
  "requestID": "a1b2c3d4-5678-90ab-cdef-EXAMPLE33333",
  "eventID": "a1b2c3d4-5678-90ab-cdef-EXAMPLE44444",
  "readOnly": true,
  "eventType": "AwsApiCall",
  "managementEvent": true,
  "recipientAccountId": "111122223333",
  "eventCategory": "Management",
  "tlsDetails": {
    "tlsVersion": "TLSv1.3",
    "cipherSuite": "TLS_AES_128_GCM_SHA256",
    "clientProvidedHostHeader": "multi-party-approval.us-east-1.amazonaws.com"
  }
}
```

ListSessions (Error)
The following example shows a CloudTrail event that demonstrates an unsuccessful `ListSessions` operation due to insufficient permissions.

```
{
  "eventVersion": "1.10",
  "userIdentity": {
    "type": "AssumedRole",
    "principalId": "AROA123456789EXAMPLE:ExampleRole-mpa",
    "arn": "arn:aws:sts::111122223333:assumed-role/ExampleRole/ExampleRole-mpa",
    "accountId": "111122223333",
    "accessKeyId": "AKIA1234567890EXAMPLE",
    "sessionContext": {
      "sessionIssuer": {
        "type": "Role",
        "principalId": "AROA123456789EXAMPLE",
        "arn": "arn:aws:iam::111122223333:role/ExampleRole",
        "accountId": "111122223333",
        "userName": "ExampleRole"
      },
      "attributes": {
        "creationDate": "2025-03-22T00:55:21Z",
        "mfaAuthenticated": "false"
      }
    }
  },
  "eventTime": "2025-03-22T00:55:21Z",
  "eventSource": "multi-party-approval.amazonaws.com",
  "eventName": "ListSessions",
  "awsRegion": "us-east-1",
  "sourceIPAddress": "192.0.2.0",
  "userAgent": "aws-sdk-java/2.31.4 Linux/5.10.234-225.910.amzn2.x86_64",
  "errorCode": "AccessDenied",
  "errorMessage": "User: arn:aws:sts::111122223333:assumed-role/ExampleRole/ExampleRole-mpa is not authorized to perform: mpa:ListSessions on resource: arn:aws:mpa:us-east-1:111122223333:approval-team/ExampleTeam-a1b2c3d4-5678-90ab-cdef-EXAMPLE11111 because no identity-based policy allows the mpa:ListSessions action",
  "requestParameters": null,
  "responseElements": null,
  "requestID": "a1b2c3d4-5678-90ab-cdef-EXAMPLE55555",
  "eventID": "a1b2c3d4-5678-90ab-cdef-EXAMPLE66666",
  "readOnly": true,
  "eventType": "AwsApiCall",
  "managementEvent": true,
  "recipientAccountId": "111122223333",
  "eventCategory": "Management",
  "tlsDetails": {
    "tlsVersion": "TLSv1.3",
    "cipherSuite": "TLS_AES_128_GCM_SHA256",
    "clientProvidedHostHeader": "multi-party-approval.us-east-1.amazonaws.com"
  }
}
```

CancelSession (Error)
The following example shows a CloudTrail event that demonstrates an unsuccessful `CancelSession` operation due to insufficient permissions.

```
{
  "eventVersion": "1.10",
  "userIdentity": {
    "type": "AssumedRole",
    "principalId": "AROA123456789EXAMPLE:ExampleRole-mpa",
    "arn": "arn:aws:sts::111122223333:assumed-role/ExampleRole/ExampleRole-mpa",
    "accountId": "111122223333",
    "accessKeyId": "AKIA1234567890EXAMPLE",
    "sessionContext": {
      "sessionIssuer": {
        "type": "Role",
        "principalId": "AROA123456789EXAMPLE",
        "arn": "arn:aws:iam::111122223333:role/ExampleRole",
        "accountId": "111122223333",
        "userName": "ExampleRole"
      },
      "attributes": {
        "creationDate": "2025-03-22T00:57:05Z",
        "mfaAuthenticated": "false"
      }
    }
  },
  "eventTime": "2025-03-22T00:57:05Z",
  "eventSource": "multi-party-approval.amazonaws.com",
  "eventName": "CancelSession",
  "awsRegion": "us-east-1",
  "sourceIPAddress": "192.0.2.0",
  "userAgent": "aws-sdk-java/2.31.4 Linux/5.10.234-225.910.amzn2.x86_64",
  "errorCode": "AccessDenied",
  "errorMessage": "User: arn:aws:sts::111122223333:assumed-role/ExampleRole/ExampleRole-mpa is not authorized to perform: mpa:CancelSession on resource: arn:aws:mpa:us-east-1:111122223333:session/ExampleTeam-a1b2c3d4-5678-90ab-cdef-EXAMPLE11111/a1b2c3d4-5678-90ab-cdef-EXAMPLE22222 because no identity-based policy allows the mpa:CancelSession action",
  "requestParameters": null,
  "responseElements": null,
  "requestID": "a1b2c3d4-5678-90ab-cdef-EXAMPLE33333",
  "eventID": "a1b2c3d4-5678-90ab-cdef-EXAMPLE44444",
  "readOnly": false,
  "eventType": "AwsApiCall",
  "managementEvent": true,
  "recipientAccountId": "111122223333",
  "eventCategory": "Management",
  "tlsDetails": {
    "tlsVersion": "TLSv1.3",
    "cipherSuite": "TLS_AES_128_GCM_SHA256",
    "clientProvidedHostHeader": "multi-party-approval.us-east-1.amazonaws.com"
  }
}
```

StartSession (Error)
The following example shows a CloudTrail event that demonstrates an unsuccessful `StartSession` operation due to insufficient permissions.

```
{
  "eventVersion": "1.10",
  "userIdentity": {
    "type": "AssumedRole",
    "principalId": "AROA123456789EXAMPLE:ExampleRole-mpa",
    "arn": "arn:aws:sts::111122223333:assumed-role/ExampleRole/ExampleRole-mpa",
    "accountId": "111122223333",
    "accessKeyId": "AKIA1234567890EXAMPLE",
    "sessionContext": {
      "sessionIssuer": {
        "type": "Role",
        "principalId": "AROA123456789EXAMPLE",
        "arn": "arn:aws:iam::111122223333:role/ExampleRole",
        "accountId": "111122223333",
        "userName": "ExampleRole"
      },
      "attributes": {
        "creationDate": "2025-03-22T00:53:07Z",
        "mfaAuthenticated": "false"
      }
    }
  },
  "eventTime": "2025-03-22T00:53:10Z",
  "eventSource": "multi-party-approval.amazonaws.com",
  "eventName": "StartSession",
  "awsRegion": "us-east-1",
  "sourceIPAddress": "192.0.2.0",
  "userAgent": "aws-sdk-java/2.31.4 Linux/5.10.234-225.910.amzn2.x86_64",
  "errorCode": "AccessDenied",
  "errorMessage": "User: arn:aws:sts::111122223333:assumed-role/ExampleRole/ExampleRole-mpa is not authorized to perform: mpa:StartSession on resource: arn:aws:mpa:us-east-1:000000000000:approval-team/example-group because no resource-based policy allows the mpa:StartSession action",
  "requestParameters": null,
  "responseElements": null,
  "requestID": "a1b2c3d4-5678-90ab-cdef-EXAMPLE55555",
  "eventID": "a1b2c3d4-5678-90ab-cdef-EXAMPLE66666",
  "readOnly": false,
  "eventType": "AwsApiCall",
  "managementEvent": true,
  "recipientAccountId": "111122223333",
  "eventCategory": "Management",
  "tlsDetails": {
    "tlsVersion": "TLSv1.3",
    "cipherSuite": "TLS_AES_128_GCM_SHA256",
    "clientProvidedHostHeader": "multi-party-approval.us-east-1.amazonaws.com"
  }
}
```

GetPolicyVersion (Error)
The following example shows a CloudTrail event that demonstrates an unsuccessful `GetPolicyVersion` operation due to insufficient permissions.

```
{
  "eventVersion": "1.10",
  "userIdentity": {
    "type": "AssumedRole",
    "principalId": "AROA123456789EXAMPLE:ExampleRole-mpa",
    "arn": "arn:aws:sts::111122223333:assumed-role/ExampleRole/ExampleRole-mpa",
    "accountId": "111122223333",
    "accessKeyId": "AKIA1234567890EXAMPLE",
    "sessionContext": {
      "sessionIssuer": {
        "type": "Role",
        "principalId": "AROA123456789EXAMPLE",
        "arn": "arn:aws:iam::111122223333:role/ExampleRole",
        "accountId": "111122223333",
        "userName": "ExampleRole"
      },
      "attributes": {
        "creationDate": "2025-03-22T00:54:25Z",
        "mfaAuthenticated": "false"
      }
    }
  },
  "eventTime": "2025-03-22T00:54:25Z",
  "eventSource": "multi-party-approval.amazonaws.com",
  "eventName": "GetPolicyVersion",
  "awsRegion": "us-east-1",
  "sourceIPAddress": "192.0.2.0",
  "userAgent": "aws-sdk-java/2.31.4 Linux/5.10.234-225.910.amzn2.x86_64",
  "errorCode": "AccessDenied",
  "errorMessage": "User: arn:aws:sts::111122223333:assumed-role/ExampleRole/ExampleRole-mpa is not authorized to perform: mpa:GetPolicyVersion on resource: arn:aws:mpa:::aws:policy/backup.amazonaws.com/CreateRestoreAccessVault/1 because no identity-based policy allows the mpa:GetPolicyVersion action",
  "requestParameters": null,
  "responseElements": null,
  "requestID": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
  "eventID": "a1b2c3d4-5678-90ab-cdef-EXAMPLE22222",
  "readOnly": true,
  "eventType": "AwsApiCall",
  "managementEvent": true,
  "recipientAccountId": "111122223333",
  "eventCategory": "Management",
  "tlsDetails": {
    "tlsVersion": "TLSv1.3",
    "cipherSuite": "TLS_AES_128_GCM_SHA256",
    "clientProvidedHostHeader": "multi-party-approval.us-east-1.amazonaws.com"
  }
}
```

ListPolicies (Error)
The following example shows a CloudTrail event that demonstrates an unsuccessful `ListPolicies` operation due to insufficient permissions.

```
{
  "eventVersion": "1.10",
  "userIdentity": {
    "type": "AssumedRole",
    "principalId": "AROA123456789EXAMPLE:ExampleRole-mpa",
    "arn": "arn:aws:sts::111122223333:assumed-role/ExampleRole/ExampleRole-mpa",
    "accountId": "111122223333",
    "accessKeyId": "AKIA1234567890EXAMPLE",
    "sessionContext": {
      "sessionIssuer": {
        "type": "Role",
        "principalId": "AROA123456789EXAMPLE",
        "arn": "arn:aws:iam::111122223333:role/ExampleRole",
        "accountId": "111122223333",
        "userName": "ExampleRole"
      },
      "attributes": {
        "creationDate": "2025-03-22T00:54:53Z",
        "mfaAuthenticated": "false"
      }
    }
  },
  "eventTime": "2025-03-22T00:54:53Z",
  "eventSource": "multi-party-approval.amazonaws.com",
  "eventName": "ListPolicies",
  "awsRegion": "us-east-1",
  "sourceIPAddress": "192.0.2.0",
  "userAgent": "aws-sdk-java/2.31.4 Linux/5.10.234-225.910.amzn2.x86_64",
  "errorCode": "AccessDenied",
  "errorMessage": "User: arn:aws:sts::111122223333:assumed-role/ExampleRole/ExampleRole-mpa is not authorized to perform: mpa:ListPolicies on resource: arn:aws:mpa:::aws:policy/* because no identity-based policy allows the mpa:ListPolicies action",
  "requestParameters": null,
  "responseElements": null,
  "requestID": "a1b2c3d4-5678-90ab-cdef-EXAMPLE33333",
  "eventID": "a1b2c3d4-5678-90ab-cdef-EXAMPLE44444",
  "readOnly": true,
  "eventType": "AwsApiCall",
  "managementEvent": true,
  "recipientAccountId": "111122223333",
  "eventCategory": "Management",
  "tlsDetails": {
    "tlsVersion": "TLSv1.3",
    "cipherSuite": "TLS_AES_128_GCM_SHA256",
    "clientProvidedHostHeader": "multi-party-approval.us-east-1.amazonaws.com"
  }
}
```

ListPolicyVersions (Error)
The following example shows a CloudTrail event that demonstrates an unsuccessful `ListPolicyVersions` operation due to insufficient permissions.

```
{
  "eventVersion": "1.10",
  "userIdentity": {
    "type": "AssumedRole",
    "principalId": "AROA123456789EXAMPLE:ExampleRole-mpa",
    "arn": "arn:aws:sts::111122223333:assumed-role/ExampleRole/ExampleRole-mpa",
    "accountId": "111122223333",
    "accessKeyId": "AKIA1234567890EXAMPLE",
    "sessionContext": {
      "sessionIssuer": {
        "type": "Role",
        "principalId": "AROA123456789EXAMPLE",
        "arn": "arn:aws:iam::111122223333:role/ExampleRole",
        "accountId": "111122223333",
        "userName": "ExampleRole"
      },
      "attributes": {
        "creationDate": "2025-03-22T00:54:53Z",
        "mfaAuthenticated": "false"
      }
    }
  },
  "eventTime": "2025-03-22T00:54:53Z",
  "eventSource": "multi-party-approval.amazonaws.com",
  "eventName": "ListPolicyVersions",
  "awsRegion": "us-east-1",
  "sourceIPAddress": "192.0.2.0",
  "userAgent": "aws-sdk-java/2.31.4 Linux/5.10.234-225.910.amzn2.x86_64",
  "errorCode": "AccessDenied",
  "errorMessage": "User: arn:aws:sts::111122223333:assumed-role/ExampleRole/ExampleRole-mpa is not authorized to perform: mpa:ListPolicyVersions on resource: arn:aws:mpa:::aws:policy/backup.amazonaws.com/CreateRestoreAccessVault because no identity-based policy allows the mpa:ListPolicyVersions action",
  "requestParameters": null,
  "responseElements": null,
  "requestID": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
  "eventID": "a1b2c3d4-5678-90ab-cdef-EXAMPLE22222",
  "readOnly": true,
  "eventType": "AwsApiCall",
  "managementEvent": true,
  "recipientAccountId": "111122223333",
  "eventCategory": "Management",
  "tlsDetails": {
    "tlsVersion": "TLSv1.3",
    "cipherSuite": "TLS_AES_128_GCM_SHA256",
    "clientProvidedHostHeader": "multi-party-approval.us-east-1.amazonaws.com"
  }
}
```

ListResourcePolicies (Error)
The following example shows a CloudTrail event that demonstrates an unsuccessful `ListResourcePolicies` operation due to insufficient permissions.

```
{
  "eventVersion": "1.10",
  "userIdentity": {
    "type": "AssumedRole",
    "principalId": "AROA123456789EXAMPLE:ExampleRole-mpa",
    "arn": "arn:aws:sts::111122223333:assumed-role/ExampleRole/ExampleRole-mpa",
    "accountId": "111122223333",
    "accessKeyId": "AKIA1234567890EXAMPLE",
    "sessionContext": {
      "sessionIssuer": {
        "type": "Role",
        "principalId": "AROA123456789EXAMPLE",
        "arn": "arn:aws:iam::111122223333:role/ExampleRole",
        "accountId": "111122223333",
        "userName": "ExampleRole"
      },
      "attributes": {
        "creationDate": "2025-03-22T00:55:21Z",
        "mfaAuthenticated": "false"
      }
    }
  },
  "eventTime": "2025-03-22T00:55:21Z",
  "eventSource": "multi-party-approval.amazonaws.com",
  "eventName": "ListResourcePolicies",
  "awsRegion": "us-east-1",
  "sourceIPAddress": "192.0.2.0",
  "userAgent": "aws-sdk-java/2.31.4 Linux/5.10.234-225.910.amzn2.x86_64",
  "errorCode": "AccessDenied",
  "errorMessage": "User: arn:aws:sts::111122223333:assumed-role/ExampleRole/ExampleRole-mpa is not authorized to perform: mpa:ListResourcePolicies on resource: arn:aws:mpa:us-east-1:111122223333:approval-team/ExampleTeam-a1b2c3d4-5678-90ab-cdef-EXAMPLE11111 because no identity-based policy allows the mpa:ListResourcePolicies action",
  "requestParameters": null,
  "responseElements": null,
  "requestID": "a1b2c3d4-5678-90ab-cdef-EXAMPLE33333",
  "eventID": "a1b2c3d4-5678-90ab-cdef-EXAMPLE44444",
  "readOnly": true,
  "eventType": "AwsApiCall",
  "managementEvent": true,
  "recipientAccountId": "111122223333",
  "eventCategory": "Management",
  "tlsDetails": {
    "tlsVersion": "TLSv1.3",
    "cipherSuite": "TLS_AES_128_GCM_SHA256",
    "clientProvidedHostHeader": "multi-party-approval.us-east-1.amazonaws.com"
  }
}
```

GetResourcePolicy (Error)
The following example shows a CloudTrail event that demonstrates an unsuccessful `GetResourcePolicy` operation due to insufficient permissions.

```
{
  "eventVersion": "1.10",
  "userIdentity": {
    "type": "AssumedRole",
    "principalId": "AROA123456789EXAMPLE:ExampleRole-mpa",
    "arn": "arn:aws:sts::111122223333:assumed-role/ExampleRole/ExampleRole-mpa",
    "accountId": "111122223333",
    "accessKeyId": "AKIA1234567890EXAMPLE",
    "sessionContext": {
      "sessionIssuer": {
        "type": "Role",
        "principalId": "AROA123456789EXAMPLE",
        "arn": "arn:aws:iam::111122223333:role/ExampleRole",
        "accountId": "111122223333",
        "userName": "ExampleRole"
      },
      "attributes": {
        "creationDate": "2025-03-22T01:08:49Z",
        "mfaAuthenticated": "false"
      }
    }
  },
  "eventTime": "2025-03-22T01:08:50Z",
  "eventSource": "multi-party-approval.amazonaws.com",
  "eventName": "GetPolicyVersion",
  "awsRegion": "us-east-1",
  "sourceIPAddress": "192.0.2.0",
  "userAgent": "aws-sdk-java/2.31.4 Linux/5.10.234-225.910.amzn2.x86_64",
  "errorCode": "AccessDenied",
  "errorMessage": "User: arn:aws:sts::111122223333:assumed-role/ExampleRole/ExampleRole-mpa is not authorized to perform: mpa:GetPolicyVersion on resource: arn:aws:mpa:::aws:policy/backup.amazonaws.com/CreateRestoreAccessVault/1 because no identity-based policy allows the mpa:GetPolicyVersion action",
  "requestParameters": null,
  "responseElements": null,
  "requestID": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
  "eventID": "a1b2c3d4-5678-90ab-cdef-EXAMPLE22222",
  "readOnly": true,
  "eventType": "AwsApiCall",
  "managementEvent": true,
  "recipientAccountId": "111122223333",
  "eventCategory": "Management",
  "tlsDetails": {
    "tlsVersion": "TLSv1.3",
    "cipherSuite": "TLS_AES_128_GCM_SHA256",
    "clientProvidedHostHeader": "multi-party-approval.us-east-1.amazonaws.com"
  }
}
```

PutResourcePolicy (Error)
The following example shows a CloudTrail event that demonstrates an unsuccessful `PutResourcePolicy` operation due to insufficient permissions.

```
{
  "eventVersion": "1.10",
  "userIdentity": {
    "type": "AssumedRole",
    "principalId": "AROA123456789EXAMPLE:ExampleRole-mpa",
    "arn": "arn:aws:sts::111122223333:assumed-role/ExampleRole/ExampleRole-mpa",
    "accountId": "111122223333",
    "accessKeyId": "AKIA1234567890EXAMPLE",
    "sessionContext": {
      "sessionIssuer": {
        "type": "Role",
        "principalId": "AROA123456789EXAMPLE",
        "arn": "arn:aws:iam::111122223333:role/ExampleRole",
        "accountId": "111122223333",
        "userName": "ExampleRole"
      },
      "attributes": {
        "creationDate": "2025-03-22T00:54:25Z",
        "mfaAuthenticated": "false"
      }
    }
  },
  "eventTime": "2025-03-22T00:54:25Z",
  "eventSource": "multi-party-approval.amazonaws.com",
  "eventName": "PutResourcePolicy",
  "awsRegion": "us-east-1",
  "sourceIPAddress": "192.0.2.0",
  "userAgent": "aws-sdk-java/2.31.4 Linux/5.10.234-225.910.amzn2.x86_64",
  "errorCode": "AccessDenied",
  "errorMessage": "User: arn:aws:sts::111122223333:assumed-role/ExampleRole/ExampleRole-mpa is not authorized to perform: mpa:PutResourcePolicy on resource: arn:aws:mpa:us-east-1:111122223333:approval-team/ExampleTeam-a1b2c3d4-5678-90ab-cdef-EXAMPLE11111 because no identity-based policy allows the mpa:PutResourcePolicy action",
  "requestParameters": null,
  "responseElements": null,
  "requestID": "a1b2c3d4-5678-90ab-cdef-EXAMPLE33333",
  "eventID": "a1b2c3d4-5678-90ab-cdef-EXAMPLE44444",
  "readOnly": false,
  "eventType": "AwsApiCall",
  "managementEvent": true,
  "recipientAccountId": "111122223333",
  "eventCategory": "Management",
  "tlsDetails": {
    "tlsVersion": "TLSv1.3",
    "cipherSuite": "TLS_AES_128_GCM_SHA256",
    "clientProvidedHostHeader": "multi-party-approval.us-east-1.amazonaws.com"
  }
}
```

DeleteResourcePolicy (Error)
The following example shows a CloudTrail event that demonstrates an unsuccessful `DeleteResourcePolicy` operation due to insufficient permissions.

```
{
  "eventVersion": "1.10",
  "userIdentity": {
    "type": "AssumedRole",
    "principalId": "AROA123456789EXAMPLE:ExampleRole-mpa",
    "arn": "arn:aws:sts::111122223333:assumed-role/ExampleRole/ExampleRole-mpa",
    "accountId": "111122223333",
    "accessKeyId": "AKIA1234567890EXAMPLE",
    "sessionContext": {
      "sessionIssuer": {
        "type": "Role",
        "principalId": "AROA123456789EXAMPLE",
        "arn": "arn:aws:iam::111122223333:role/ExampleRole",
        "accountId": "111122223333",
        "userName": "ExampleRole"
      },
      "attributes": {
        "creationDate": "2025-03-22T00:53:56Z",
        "mfaAuthenticated": "false"
      }
    }
  },
  "eventTime": "2025-03-22T00:53:56Z",
  "eventSource": "multi-party-approval.amazonaws.com",
  "eventName": "DeleteResourcePolicy",
  "awsRegion": "us-east-1",
  "sourceIPAddress": "192.0.2.0",
  "userAgent": "aws-sdk-java/2.31.4 Linux/5.10.234-225.910.amzn2.x86_64",
  "errorCode": "AccessDenied",
  "errorMessage": "User: arn:aws:sts::111122223333:assumed-role/ExampleRole/ExampleRole-mpa is not authorized to perform: mpa:DeleteResourcePolicy on resource: arn:aws:mpa:us-east-1:111122223333:approval-team/ExampleTeam-a1b2c3d4-5678-90ab-cdef-EXAMPLE11111 because no identity-based policy allows the mpa:DeleteResourcePolicy action",
  "requestParameters": null,
  "responseElements": null,
  "requestID": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
  "eventID": "a1b2c3d4-5678-90ab-cdef-EXAMPLE22222",
  "readOnly": false,
  "eventType": "AwsApiCall",
  "managementEvent": true,
  "recipientAccountId": "111122223333",
  "eventCategory": "Management",
  "tlsDetails": {
    "tlsVersion": "TLSv1.3",
    "cipherSuite": "TLS_AES_128_GCM_SHA256",
    "clientProvidedHostHeader": "multi-party-approval.us-east-1.amazonaws.com"
  }
}
```

ListTagsForResource (Error)
The following example shows a CloudTrail event that demonstrates an unsuccessful `ListTagsForResource` operation due to insufficient permissions.

```
{
  "eventVersion": "1.10",
  "userIdentity": {
    "type": "AssumedRole",
    "principalId": "AROA123456789EXAMPLE:ExampleRole-mpa",
    "arn": "arn:aws:sts::111122223333:assumed-role/ExampleRole/ExampleRole-mpa",
    "accountId": "111122223333",
    "accessKeyId": "AKIA1234567890EXAMPLE",
    "sessionContext": {
      "sessionIssuer": {
        "type": "Role",
        "principalId": "AROA123456789EXAMPLE",
        "arn": "arn:aws:iam::111122223333:role/ExampleRole",
        "accountId": "111122223333",
        "userName": "ExampleRole"
      },
      "attributes": {
        "creationDate": "2025-03-22T00:57:23Z",
        "mfaAuthenticated": "false"
      }
    }
  },
  "eventTime": "2025-03-22T00:57:23Z",
  "eventSource": "multi-party-approval.amazonaws.com",
  "eventName": "ListTagsForResource",
  "awsRegion": "us-east-1",
  "sourceIPAddress": "192.0.2.0",
  "userAgent": "aws-sdk-java/2.31.4 Linux/5.10.234-225.910.amzn2.x86_64",
  "errorCode": "AccessDenied",
  "errorMessage": "User: arn:aws:sts::111122223333:assumed-role/ExampleRole/ExampleRole-mpa is not authorized to perform: mpa:ListTagsForResource on resource: arn:aws:mpa:us-east-1:111122223333:approval-team/ExampleTeam-a1b2c3d4-5678-90ab-cdef-EXAMPLE11111 because no identity-based policy allows the mpa:ListTagsForResource action",
  "requestParameters": null,
  "responseElements": null,
  "requestID": "a1b2c3d4-5678-90ab-cdef-EXAMPLE33333",
  "eventID": "a1b2c3d4-5678-90ab-cdef-EXAMPLE44444",
  "readOnly": true,
  "eventType": "AwsApiCall",
  "managementEvent": true,
  "recipientAccountId": "111122223333",
  "eventCategory": "Management",
  "tlsDetails": {
    "tlsVersion": "TLSv1.3",
    "cipherSuite": "TLS_AES_128_GCM_SHA256",
    "clientProvidedHostHeader": "multi-party-approval.us-east-1.amazonaws.com"
  }
}
```

TagResource (Error)
The following example shows a CloudTrail event that demonstrates an unsuccessful `TagResource` operation due to insufficient permissions.

```
{
  "eventVersion": "1.10",
  "userIdentity": {
    "type": "AssumedRole",
    "principalId": "AROA123456789EXAMPLE:ExampleRole-mpa",
    "arn": "arn:aws:sts::111122223333:assumed-role/ExampleRole/ExampleRole-mpa",
    "accountId": "111122223333",
    "accessKeyId": "AKIA1234567890EXAMPLE",
    "sessionContext": {
      "sessionIssuer": {
        "type": "Role",
        "principalId": "AROA123456789EXAMPLE",
        "arn": "arn:aws:iam::111122223333:role/ExampleRole",
        "accountId": "111122223333",
        "userName": "ExampleRole"
      },
      "attributes": {
        "creationDate": "2025-03-22T00:55:50Z",
        "mfaAuthenticated": "false"
      }
    }
  },
  "eventTime": "2025-03-22T00:55:50Z",
  "eventSource": "multi-party-approval.amazonaws.com",
  "eventName": "TagResource",
  "awsRegion": "us-east-1",
  "sourceIPAddress": "192.0.2.0",
  "userAgent": "aws-sdk-java/2.31.4 Linux/5.10.234-225.910.amzn2.x86_64",
  "errorCode": "AccessDenied",
  "errorMessage": "User: arn:aws:sts::111122223333:assumed-role/ExampleRole/ExampleRole-mpa is not authorized to perform: mpa:TagResource on resource: arn:aws:mpa:us-east-1:111122223333:approval-team/ExampleTeam-a1b2c3d4-5678-90ab-cdef-EXAMPLE11111 because no identity-based policy allows the mpa:TagResource action",
  "requestParameters": null,
  "responseElements": null,
  "requestID": "a1b2c3d4-5678-90ab-cdef-EXAMPLE55555",
  "eventID": "a1b2c3d4-5678-90ab-cdef-EXAMPLE66666",
  "readOnly": false,
  "eventType": "AwsApiCall",
  "managementEvent": true,
  "recipientAccountId": "111122223333",
  "eventCategory": "Management",
  "tlsDetails": {
    "tlsVersion": "TLSv1.3",
    "cipherSuite": "TLS_AES_128_GCM_SHA256",
    "clientProvidedHostHeader": "multi-party-approval.us-east-1.amazonaws.com"
  }
}
```

UntagResource (Error)
The following example shows a CloudTrail event that demonstrates an unsuccessful `UntagResource` operation due to insufficient permissions.

```
{
  "eventVersion": "1.10",
  "userIdentity": {
    "type": "AssumedRole",
    "principalId": "AROA123456789EXAMPLE:ExampleRole-mpa",
    "arn": "arn:aws:sts::111122223333:assumed-role/ExampleRole/ExampleRole-mpa",
    "accountId": "111122223333",
    "accessKeyId": "AKIA1234567890EXAMPLE",
    "sessionContext": {
      "sessionIssuer": {
        "type": "Role",
        "principalId": "AROA123456789EXAMPLE",
        "arn": "arn:aws:iam::111122223333:role/ExampleRole",
        "accountId": "111122223333",
        "userName": "ExampleRole"
      },
      "attributes": {
        "creationDate": "2025-03-22T00:56:56Z",
        "mfaAuthenticated": "false"
      }
    }
  },
  "eventTime": "2025-03-22T00:56:56Z",
  "eventSource": "multi-party-approval.amazonaws.com",
  "eventName": "UntagResource",
  "awsRegion": "us-east-1",
  "sourceIPAddress": "192.0.2.0",
  "userAgent": "aws-sdk-java/2.31.4 Linux/5.10.234-225.910.amzn2.x86_64",
  "errorCode": "AccessDenied",
  "errorMessage": "User: arn:aws:sts::111122223333:assumed-role/ExampleRole/ExampleRole-mpa is not authorized to perform: mpa:UntagResource on resource: arn:aws:mpa:us-east-1:111122223333:approval-team/ExampleTeam-a1b2c3d4-5678-90ab-cdef-EXAMPLE11111 because no identity-based policy allows the mpa:UntagResource action",
  "requestParameters": null,
  "responseElements": null,
  "requestID": "a1b2c3d4-5678-90ab-cdef-EXAMPLE77777",
  "eventID": "a1b2c3d4-5678-90ab-cdef-EXAMPLE88888",
  "readOnly": false,
  "eventType": "AwsApiCall",
  "managementEvent": true,
  "recipientAccountId": "111122223333",
  "eventCategory": "Management",
  "tlsDetails": {
    "tlsVersion": "TLSv1.3",
    "cipherSuite": "TLS_AES_128_GCM_SHA256",
    "clientProvidedHostHeader": "multi-party-approval.us-east-1.amazonaws.com"
  }
}
```

The following tabbed list displays some examples for the Multi-party approval integration with AWS IAM Identity Center.

CreateApplication
The following example shows a CloudTrail event that demonstrates the `CreateApplication` operation for the Multi-party approval integration with IAM Identity Center.

```
{
  "eventVersion": "1.09",
  "userIdentity": {
    "type": "AssumedRole",
    "principalId": "AROA123456789EXAMPLE:ExampleRole-mpa",
    "arn": "arn:aws:sts::111122223333:assumed-role/ExampleRole/ExampleRole-mpa",
    "accountId": "111122223333",
    "accessKeyId": "AKIA1234567890EXAMPLE",
    "sessionContext": {
      "sessionIssuer": {
        "type": "Role",
        "principalId": "AROA123456789EXAMPLE",
        "arn": "arn:aws:iam::111122223333:role/ExampleRole",
        "accountId": "111122223333",
        "userName": "ExampleRole"
      },
      "attributes": {
        "creationDate": "2025-02-18T19:56:17Z",
        "mfaAuthenticated": "false"
      }
    },
    "invokedBy": "AWS Internal"
  },
  "eventTime": "2025-02-18T19:56:28Z",
  "eventSource": "sso.amazonaws.com",
  "eventName": "CreateApplication",
  "awsRegion": "us-east-1",
  "sourceIPAddress": "AWS Internal",
  "userAgent": "AWS Internal",
  "requestParameters": {
    "instanceArn": "arn:aws:sso:::instance/ssoins-a1b2c3d4e5f6g7h8",
    "applicationProviderArn": "arn:aws:sso::aws:applicationProvider/app-EXAMPLE11111/WIP",
    "name": "Multi-party Approval",
    "description": "Multi-party Approval",
    "portalOptions": {
      "signInOptions": {
        "origin": "APPLICATION",
        "applicationUrl": "https://example-id.alpha-mpa-portal.us-east-1.on.aws/"
      },
      "visibility": "ENABLED"
    },
    "status": "ENABLED",
    "clientToken": "a1b2c3d4-5678-90ab-cdef-EXAMPLE22222"
  },
  "responseElements": {
    "applicationArn": "arn:aws:sso::111122223333:application/ssoins-a1b2c3d4e5f6g7h8/apl-a1b2c3d4e5f6g7h8"
  },
  "requestID": "a1b2c3d4-5678-90ab-cdef-EXAMPLE33333",
  "eventID": "a1b2c3d4-5678-90ab-cdef-EXAMPLE44444",
  "readOnly": false,
  "resources": [
    {
      "accountId": "111122223333",
      "type": "AWS::SSO::Instance",
      "ARN": "arn:aws:sso:::instance/ssoins-a1b2c3d4e5f6g7h8"
    }
  ],
  "eventType": "AwsApiCall",
  "managementEvent": true,
  "recipientAccountId": "111122223333",
  "eventCategory": "Management"
}
```

DescribeInstance
The following example shows a CloudTrail event that demonstrates the `DescribeInstance` operation for the Multi-party approval integration with IAM Identity Center.

```
{
  "eventVersion": "1.09",
  "userIdentity": {
    "type": "AssumedRole",
    "principalId": "AROA123456789EXAMPLE:ExampleRole-mpa",
    "arn": "arn:aws:sts::111122223333:assumed-role/ExampleRole/ExampleRole-mpa",
    "accountId": "111122223333",
    "accessKeyId": "AKIA1234567890EXAMPLE",
    "sessionContext": {
      "sessionIssuer": {
        "type": "Role",
        "principalId": "AROA123456789EXAMPLE",
        "arn": "arn:aws:iam::111122223333:role/ExampleRole",
        "accountId": "111122223333",
        "userName": "ExampleRole"
      },
      "attributes": {
        "creationDate": "2025-02-18T19:56:17Z",
        "mfaAuthenticated": "false"
      }
    },
    "invokedBy": "AWS Internal"
  },
  "eventTime": "2025-02-18T19:56:27Z",
  "eventSource": "sso.amazonaws.com",
  "eventName": "DescribeInstance",
  "awsRegion": "us-east-1",
  "sourceIPAddress": "AWS Internal",
  "userAgent": "AWS Internal",
  "requestParameters": {
    "instanceArn": "arn:aws:sso:::instance/ssoins-a1b2c3d4e5f6g7h8"
  },
  "responseElements": null,
  "requestID": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
  "eventID": "a1b2c3d4-5678-90ab-cdef-EXAMPLE22222",
  "readOnly": true,
  "eventType": "AwsApiCall",
  "managementEvent": true,
  "recipientAccountId": "111122223333",
  "eventCategory": "Management"
}
```

PutApplicationAuthenticationMethod
The following example shows a CloudTrail event that demonstrates the `PutApplicationAuthenticationMethod` operation for the Multi-party approval integration with IAM Identity Center.

```
{
  "eventVersion": "1.09",
  "userIdentity": {
    "type": "AssumedRole",
    "principalId": "AROA123456789EXAMPLE:ExampleRole-mpa",
    "arn": "arn:aws:sts::111122223333:assumed-role/ExampleRole/ExampleRole-mpa",
    "accountId": "111122223333",
    "accessKeyId": "AKIA1234567890EXAMPLE",
    "sessionContext": {
      "sessionIssuer": {
        "type": "Role",
        "principalId": "AROA123456789EXAMPLE",
        "arn": "arn:aws:iam::111122223333:role/ExampleRole",
        "accountId": "111122223333",
        "userName": "ExampleRole"
      },
      "attributes": {
        "creationDate": "2025-02-18T19:56:17Z",
        "mfaAuthenticated": "false"
      }
    },
    "invokedBy": "AWS Internal"
  },
  "eventTime": "2025-02-18T19:56:28Z",
  "eventSource": "sso.amazonaws.com",
  "eventName": "PutApplicationAuthenticationMethod",
  "awsRegion": "us-east-1",
  "sourceIPAddress": "AWS Internal",
  "userAgent": "AWS Internal",
  "requestParameters": {
    "applicationArn": "arn:aws:sso::111122223333:application/ssoins-a1b2c3d4e5f6g7h8/apl-a1b2c3d4e5f6g7h8",
    "authenticationMethodType": "IAM",
    "authenticationMethod": {
      "iam": {
        "actorPolicy": {
          "Version": "2012-10-17",
          "Statement": [
            {
              "Effect": "Allow",
              "Principal": {
                "Service": [
                  "us-east-1.alpha.mpa.awsfluffy.aws.internal",
                  "test.awsagora.aws.internal",
                  "developer.awsagora.aws.internal"
                ]
              },
              "Action": [
                "sso-oauth:CreateTokenWithIAM",
                "sso-oauth:IntrospectTokenWithIAM",
                "sso-oauth:RevokeTokenWithIAM"
              ]
            }
          ]
        }
      }
    }
  },
  "responseElements": null,
  "requestID": "a1b2c3d4-5678-90ab-cdef-EXAMPLE33333",
  "eventID": "a1b2c3d4-5678-90ab-cdef-EXAMPLE44444",
  "readOnly": false,
  "resources": [
    {
      "accountId": "111122223333",
      "type": "AWS::SSO::Instance",
      "ARN": "arn:aws:sso:::instance/ssoins-a1b2c3d4e5f6g7h8"
    },
    {
      "accountId": "111122223333",
      "type": "AWS::SSO::Application",
      "ARN": "arn:aws:sso::111122223333:application/ssoins-a1b2c3d4e5f6g7h8/apl-a1b2c3d4e5f6g7h8"
    }
  ],
  "eventType": "AwsApiCall",
  "managementEvent": true,
  "recipientAccountId": "111122223333",
  "eventCategory": "Management"
}
```

DescribeInstance
The following example shows a CloudTrail event that demonstrates the `DescribeInstance` operation for the Multi-party approval integration with IAM Identity Center.

```
{
  "eventVersion": "1.09",
  "userIdentity": {
    "type": "AssumedRole",
    "principalId": "AROA123456789EXAMPLE:ExampleRole-mpa",
    "arn": "arn:aws:sts::111122223333:assumed-role/ExampleRole/ExampleRole-mpa",
    "accountId": "111122223333",
    "accessKeyId": "AKIA1234567890EXAMPLE",
    "sessionContext": {
      "sessionIssuer": {
        "type": "Role",
        "principalId": "AROA123456789EXAMPLE",
        "arn": "arn:aws:iam::111122223333:role/ExampleRole",
        "accountId": "111122223333",
        "userName": "ExampleRole"
      },
      "attributes": {
        "creationDate": "2025-02-18T19:56:17Z",
        "mfaAuthenticated": "false"
      }
    },
    "invokedBy": "AWS Internal"
  },
  "eventTime": "2025-02-18T19:56:27Z",
  "eventSource": "sso.amazonaws.com",
  "eventName": "DescribeInstance",
  "awsRegion": "us-east-1",
  "sourceIPAddress": "AWS Internal",
  "userAgent": "AWS Internal",
  "requestParameters": {
    "instanceArn": "arn:aws:sso:::instance/ssoins-a1b2c3d4e5f6g7h8"
  },
  "responseElements": null,
  "requestID": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
  "eventID": "a1b2c3d4-5678-90ab-cdef-EXAMPLE22222",
  "readOnly": true,
  "eventType": "AwsApiCall",
  "managementEvent": true,
  "recipientAccountId": "111122223333",
  "eventCategory": "Management"
}
```

PutApplicationAuthenticationMethod
The following example shows a CloudTrail event that demonstrates the `PutApplicationAuthenticationMethod` operation for the Multi-party approval integration with IAM Identity Center.

```
{
  "eventVersion": "1.09",
  "userIdentity": {
    "type": "AssumedRole",
    "principalId": "AROA123456789EXAMPLE:ExampleRole-mpa",
    "arn": "arn:aws:sts::111122223333:assumed-role/ExampleRole/ExampleRole-mpa",
    "accountId": "111122223333",
    "accessKeyId": "AKIA1234567890EXAMPLE",
    "sessionContext": {
      "sessionIssuer": {
        "type": "Role",
        "principalId": "AROA123456789EXAMPLE",
        "arn": "arn:aws:iam::111122223333:role/ExampleRole",
        "accountId": "111122223333",
        "userName": "ExampleRole"
      },
      "attributes": {
        "creationDate": "2025-02-18T19:56:17Z",
        "mfaAuthenticated": "false"
      }
    },
    "invokedBy": "AWS Internal"
  },
  "eventTime": "2025-02-18T19:56:28Z",
  "eventSource": "sso.amazonaws.com",
  "eventName": "PutApplicationAuthenticationMethod",
  "awsRegion": "us-east-1",
  "sourceIPAddress": "AWS Internal",
  "userAgent": "AWS Internal",
  "requestParameters": {
    "applicationArn": "arn:aws:sso::111122223333:application/ssoins-a1b2c3d4e5f6g7h8/apl-a1b2c3d4e5f6g7h8",
    "authenticationMethodType": "IAM",
    "authenticationMethod": {
      "iam": {
        "actorPolicy": {
          "Version": "2012-10-17",
          "Statement": [
            {
              "Effect": "Allow",
              "Principal": {
                "Service": [
                  "us-east-1.alpha.mpa.awsfluffy.aws.internal",
                  "test.awsagora.aws.internal",
                  "developer.awsagora.aws.internal"
                ]
              },
              "Action": [
                "sso-oauth:CreateTokenWithIAM",
                "sso-oauth:IntrospectTokenWithIAM",
                "sso-oauth:RevokeTokenWithIAM"
              ]
            }
          ]
        }
      }
    }
  },
  "responseElements": null,
  "requestID": "a1b2c3d4-5678-90ab-cdef-EXAMPLE33333",
  "eventID": "a1b2c3d4-5678-90ab-cdef-EXAMPLE44444",
  "readOnly": false,
  "resources": [
    {
      "accountId": "111122223333",
      "type": "AWS::SSO::Instance",
      "ARN": "arn:aws:sso:::instance/ssoins-a1b2c3d4e5f6g7h8"
    },
    {
      "accountId": "111122223333",
      "type": "AWS::SSO::Application",
      "ARN": "arn:aws:sso::111122223333:application/ssoins-a1b2c3d4e5f6g7h8/apl-a1b2c3d4e5f6g7h8"
    }
  ],
  "eventType": "AwsApiCall",
  "managementEvent": true,
  "recipientAccountId": "111122223333",
  "eventCategory": "Management"
}
```

PutApplicationGrant
The following example shows a CloudTrail event that demonstrates the `PutApplicationGrant` operation for the Multi-party approval integration with IAM Identity Center.

```
{
  "eventVersion": "1.09",
  "userIdentity": {
    "type": "AssumedRole",
    "principalId": "AROA123456789EXAMPLE:ExampleRole-mpa",
    "arn": "arn:aws:sts::111122223333:assumed-role/ExampleRole/ExampleRole-mpa",
    "accountId": "111122223333",
    "accessKeyId": "AKIA1234567890EXAMPLE",
    "sessionContext": {
      "sessionIssuer": {
        "type": "Role",
        "principalId": "AROA123456789EXAMPLE",
        "arn": "arn:aws:iam::111122223333:role/ExampleRole",
        "accountId": "111122223333",
        "userName": "ExampleRole"
      },
      "attributes": {
        "creationDate": "2025-02-18T19:56:17Z",
        "mfaAuthenticated": "false"
      }
    },
    "invokedBy": "AWS Internal"
  },
  "eventTime": "2025-02-18T19:56:29Z",
  "eventSource": "sso.amazonaws.com",
  "eventName": "PutApplicationGrant",
  "awsRegion": "us-east-1",
  "sourceIPAddress": "AWS Internal",
  "userAgent": "AWS Internal",
  "requestParameters": {
    "applicationArn": "arn:aws:sso::111122223333:application/ssoins-a1b2c3d4e5f6g7h8/apl-a1b2c3d4e5f6g7h8",
    "grantType": "refresh_token",
    "grant": {
      "refreshToken": {}
    }
  },
  "responseElements": null,
  "requestID": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
  "eventID": "a1b2c3d4-5678-90ab-cdef-EXAMPLE22222",
  "readOnly": false,
  "resources": [
    {
      "accountId": "111122223333",
      "type": "AWS::SSO::Instance",
      "ARN": "arn:aws:sso:::instance/ssoins-a1b2c3d4e5f6g7h8"
    },
    {
      "accountId": "111122223333",
      "type": "AWS::SSO::Application",
      "ARN": "arn:aws:sso::111122223333:application/ssoins-a1b2c3d4e5f6g7h8/apl-a1b2c3d4e5f6g7h8"
    }
  ],
  "eventType": "AwsApiCall",
  "managementEvent": true,
  "recipientAccountId": "111122223333",
  "eventCategory": "Management"
}
```

PutApplicationAccessScope
The following example shows a CloudTrail event that demonstrates the `PutApplicationAccessScope` operation for the Multi-party approval integration with IAM Identity Center.

```
{
  "eventVersion": "1.09",
  "userIdentity": {
    "type": "AssumedRole",
    "principalId": "AROA123456789EXAMPLE:ExampleRole-mpa",
    "arn": "arn:aws:sts::111122223333:assumed-role/ExampleRole/ExampleRole-mpa",
    "accountId": "111122223333",
    "accessKeyId": "AKIA1234567890EXAMPLE",
    "sessionContext": {
      "sessionIssuer": {
        "type": "Role",
        "principalId": "AROA123456789EXAMPLE",
        "arn": "arn:aws:iam::111122223333:role/ExampleRole",
        "accountId": "111122223333",
        "userName": "ExampleRole"
      },
      "attributes": {
        "creationDate": "2025-02-18T19:56:17Z",
        "mfaAuthenticated": "false"
      }
    },
    "invokedBy": "AWS Internal"
  },
  "eventTime": "2025-02-18T19:56:29Z",
  "eventSource": "sso.amazonaws.com",
  "eventName": "PutApplicationAccessScope",
  "awsRegion": "us-east-1",
  "sourceIPAddress": "AWS Internal",
  "userAgent": "AWS Internal",
  "requestParameters": {
    "scope": "mpa_test:test",
    "applicationArn": "arn:aws:sso::111122223333:application/ssoins-a1b2c3d4e5f6g7h8/apl-a1b2c3d4e5f6g7h8"
  },
  "responseElements": null,
  "requestID": "a1b2c3d4-5678-90ab-cdef-EXAMPLE33333",
  "eventID": "a1b2c3d4-5678-90ab-cdef-EXAMPLE44444",
  "readOnly": false,
  "resources": [
    {
      "accountId": "111122223333",
      "type": "AWS::SSO::Instance",
      "ARN": "arn:aws:sso:::instance/ssoins-a1b2c3d4e5f6g7h8"
    },
    {
      "accountId": "111122223333",
      "type": "AWS::SSO::Application",
      "ARN": "arn:aws:sso::111122223333:application/ssoins-a1b2c3d4e5f6g7h8/apl-a1b2c3d4e5f6g7h8"
    }
  ],
  "eventType": "AwsApiCall",
  "managementEvent": true,
  "recipientAccountId": "111122223333",
  "eventCategory": "Management"
}
```

PutApplicationAssignmentConfiguration
The following example shows a CloudTrail event that demonstrates the `PutApplicationAssignmentConfiguration` operation for the Multi-party approval integration with IAM Identity Center.

```
{
  "eventVersion": "1.09",
  "userIdentity": {
    "type": "AssumedRole",
    "principalId": "AROA123456789EXAMPLE:ExampleRole-mpa",
    "arn": "arn:aws:sts::111122223333:assumed-role/ExampleRole/ExampleRole-mpa",
    "accountId": "111122223333",
    "accessKeyId": "AKIA1234567890EXAMPLE",
    "sessionContext": {
      "sessionIssuer": {
        "type": "Role",
        "principalId": "AROA123456789EXAMPLE",
        "arn": "arn:aws:iam::111122223333:role/ExampleRole",
        "accountId": "111122223333",
        "userName": "ExampleRole"
      },
      "attributes": {
        "creationDate": "2025-02-18T19:56:17Z",
        "mfaAuthenticated": "false"
      }
    },
    "invokedBy": "AWS Internal"
  },
  "eventTime": "2025-02-18T19:56:28Z",
  "eventSource": "sso.amazonaws.com",
  "eventName": "PutApplicationAssignmentConfiguration",
  "awsRegion": "us-east-1",
  "sourceIPAddress": "AWS Internal",
  "userAgent": "AWS Internal",
  "requestParameters": {
    "applicationArn": "arn:aws:sso::111122223333:application/ssoins-a1b2c3d4e5f6g7h8/apl-a1b2c3d4e5f6g7h8",
    "assignmentRequired": false
  },
  "responseElements": null,
  "requestID": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
  "eventID": "a1b2c3d4-5678-90ab-cdef-EXAMPLE22222",
  "readOnly": false,
  "resources": [
    {
      "accountId": "111122223333",
      "type": "AWS::SSO::Instance",
      "ARN": "arn:aws:sso:::instance/ssoins-a1b2c3d4e5f6g7h8"
    },
    {
      "accountId": "111122223333",
      "type": "AWS::SSO::Application",
      "ARN": "arn:aws:sso::111122223333:application/ssoins-a1b2c3d4e5f6g7h8/apl-a1b2c3d4e5f6g7h8"
    }
  ],
  "eventType": "AwsApiCall",
  "managementEvent": true,
  "recipientAccountId": "111122223333",
  "eventCategory": "Management"
}
```

Authenticate
The following example shows a CloudTrail event that demonstrates the `Authenticate` operation for the Multi-party approval integration with IAM Identity Center.

```
{
  "eventVersion": "1.10",
  "userIdentity": {
    "type": "Unknown",
    "principalId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
    "accountId": "111122223333",
    "userName": "************************************************************",
    "onBehalfOf": {
      "userId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
      "identityStoreArn": "arn:aws:identitystore::111122223333:identitystore/d-a1b2c3d4e5"
    },
    "credentialId": "us-east-1-a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6"
  },
  "eventTime": "2025-02-18T19:57:36Z",
  "eventSource": "sso.amazonaws.com",
  "eventName": "Authenticate",
  "awsRegion": "us-east-1",
  "sourceIPAddress": "192.0.2.0",
  "userAgent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:135.0) Gecko/20100101 Firefox/135.0",
  "requestParameters": null,
  "responseElements": null,
  "requestID": "a1b2c3d4-5678-90ab-cdef-EXAMPLE33333",
  "eventID": "a1b2c3d4-5678-90ab-cdef-EXAMPLE44444",
  "readOnly": false,
  "eventType": "AwsServiceEvent",
  "managementEvent": true,
  "recipientAccountId": "111122223333",
  "eventCategory": "Management"
}
```

For information about CloudTrail record contents, see [CloudTrail
record contents](../../../awscloudtrail/latest/userguide/cloudtrail-event-reference-record-contents.md "../../../awscloudtrail/latest/userguide/cloudtrail-event-reference-record-contents.md") in the _AWS CloudTrail User Guide_.
