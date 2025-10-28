# Logging AWS Cost Management API calls with AWS CloudTrail

AWS Cost Management is integrated with AWS CloudTrail, a service that provides a record of actions taken
by a user, role, or an AWS service in AWS Cost Management. CloudTrail captures API calls for AWS Cost Management as
events. The calls captured include API calls from the AWS Cost Management console and from your
applications.

If you create a trail, you can enable continuous delivery of CloudTrail events to an Amazon S3
bucket, including events for AWS Cost Management. If you don't configure a trail, you can still view
the most recent events in the CloudTrail console in **Event history**. Using
the information collected by CloudTrail, you can determine the request that was made to AWS Cost Management,
the IP address from which the request was made, who made the request, when it was made,
and additional details.

To learn more about CloudTrail, see the [AWS CloudTrail User Guide](../../../awscloudtrail/latest/userguide.md "../../../awscloudtrail/latest/userguide.md").

## AWS Cost Management information in CloudTrail

CloudTrail is enabled on your AWS account when you create the account. When activity
occurs in AWS Cost Management, that activity is recorded in a CloudTrail event along with other
AWS service events in **Event history**. You can view, search,
and download recent events in your AWS account. For more information, see [Viewing Events with CloudTrail Event
History](../../../awscloudtrail/latest/userguide/view-cloudtrail-events.md "../../../awscloudtrail/latest/userguide/view-cloudtrail-events.md").

For an ongoing record of events in your AWS account, including events for AWS Cost Management,
create a trail. A trail enables CloudTrail to deliver log files to an Amazon S3 bucket. By
default, when you create a trail in the CloudTrail console, the trail applies to all AWS
Regions. The trail logs events from all Regions in the AWS partitions and delivers
the log files to the Amazon S3 bucket that you specify. Additionally, you can configure
other AWS services to analyze and act on the event data collected in CloudTrail
logs.

For more information, see the following in the _CloudTrail User
Guide_:

- [Creating a trail for your AWS account (overview)](../../../awscloudtrail/latest/userguide/cloudtrail-create-and-update-a-trail.md "../../../awscloudtrail/latest/userguide/cloudtrail-create-and-update-a-trail.md")
- [CloudTrail supported services and integrations](../../../awscloudtrail/latest/userguide/cloudtrail-aws-service-specific-topics.md#cloudtrail-aws-service-specific-topics-integrations "../../../awscloudtrail/latest/userguide/cloudtrail-aws-service-specific-topics.md#cloudtrail-aws-service-specific-topics-integrations")
- [Configuring
  Amazon SNS Notifications for CloudTrail](../../../awscloudtrail/latest/userguide/getting_notifications_top_level.md "../../../awscloudtrail/latest/userguide/getting_notifications_top_level.md")
- [Receiving CloudTrail log files from multiple regions](../../../awscloudtrail/latest/userguide/receive-cloudtrail-log-files-from-multiple-regions.md "../../../awscloudtrail/latest/userguide/receive-cloudtrail-log-files-from-multiple-regions.md")
- [Receiving CloudTrail log files from multiple accounts](../../../awscloudtrail/latest/userguide/cloudtrail-receive-logs-from-multiple-accounts.md "../../../awscloudtrail/latest/userguide/cloudtrail-receive-logs-from-multiple-accounts.md")

AWS Cost Management actions are logged by CloudTrail and documented in the [AWS Billing and Cost Management API Reference](../../../aws-cost-management/latest/APIReference/Welcome.md "../../../aws-cost-management/latest/APIReference/Welcome.md"). For example, calls to the
`GetDimensionValues`, `GetCostCategories`, and
`GetCostandUsage` endpoints generate entries in the CloudTrail log
files.

Every event or log entry contains information about who generated the request. The
identity information helps you determine whether the request was made:

- With root or user role credentials.
- With temporary security credentials for a role or federated user.
- By another AWS service.

For more information, see the [CloudTrail
userIdentity Element](../../../awscloudtrail/latest/userguide/cloudtrail-event-reference-user-identity.md "../../../awscloudtrail/latest/userguide/cloudtrail-event-reference-user-identity.md").

## Understanding AWS Cost Management log file

entries

A trail is a configuration that enables delivery of events as log files to an Amazon S3
bucket that you specify. An event represents a single request from any source and
includes information about the requested action, the date and time of the action,
request parameters, and so on.

CloudTrail log files contain one or more log entries. CloudTrail log files are not an ordered
stack trace of the public API calls, so they do not appear in any specific
order.

The following example shows a CloudTrail log entry for the `GetCostandUsage`
endpoint.

```
{
        "eventVersion":"1.08",
        "userIdentity":{
            "accountId":"111122223333",
            "accessKeyId":"AIDACKCEVSQ6C2EXAMPLE"
        },
        "eventTime":"2022-05-24T22:38:51Z",
        "eventSource":"ce.amazonaws.com",
        "eventName":"GetCostandUsage",
        "awsRegion":"us-east-1",
        "sourceIPAddress":"100.100.10.10",
        "requestParameters":{
           "TimePeriod":{
              "Start":"2022-01-01",
              "End":"2022-01-31"
           },
           "Metrics":[
              "UnblendedCost",
              "UsageQuantity"
           ],
           "Granularity":"MONTHLY",
           "GroupBy":[
              {
                 "Type":"DIMENSION",
                 "Key":"SERVICE"
              }
           ]
        },
        "responseElements":null,
        "requestID":"3295c994-063e-44ac-80fb-b40example9f",
        "eventID":"5923c499-063e-44ac-80fb-b40example9f",
        "readOnly":true,
        "eventType":"AwsApiCall",
        "managementEvent":true,
        "recipientAccountId":"1111-2222-3333",
        "eventCategory":"Management",
        "tlsDetails":{
           "tlsVersion":"TLSv1.2",
           "clientProvidedHostHeader":"ce.us-east-1.amazonaws.com"
        }
}
```

## Understanding Cost Optimization Hub log

file entries

A trail is a configuration that enables delivery of events as log files to an Amazon S3 bucket
that you specify. CloudTrail log files contain one or more log entries. An event represents a single
request from any source and includes information about the requested action, the date and time
of the action, request parameters, and so on. CloudTrail log files aren't an ordered stack trace of
the public API calls, so they don't appear in any specific order.

The following examples show CloudTrail log entries that demonstrate API actions and exceptions
for Cost Optimization Hub.

###### Examples

- Exceptions
  - [Throttling Exception](#example-throttling-exception "#example-throttling-exception")
  - [Access denied exception](#example-access-denied "#example-access-denied")

- API actions
  - [ListEnrollmentStatus](#example-listenrollmentstatus "#example-listenrollmentstatus")
  - [ListRecommendations](#example-listrecommendations "#example-listrecommendations")
  - [ListRecommendationSummaries](#example-listrecommendationsummaries "#example-listrecommendationsummaries")
  - [GetRecommendation](#example-get-recommendation "#example-get-recommendation")
  - [UpdateEnrollmentStatus](#example-update-enrollment-status "#example-update-enrollment-status")
  - [UpdatePreferences](#example-update-preferences "#example-update-preferences")

### Throttling Exception

The following example shows a log entry for a throttling exception.

```
    {
      "eventVersion": "1.09",
      "userIdentity": {
        "type": "AssumedRole",
        "principalId": "EXAMPLEAIZ5FYRFP3POCC:john-doe",
        "arn": "arn:aws:sts::111122223333:assumed-role/Admin/john-doe",
        "accountId": "111122223333",
        "accessKeyId": "AKIAIOSFODNN7EXAMPLE",
        "sessionContext": {
          "sessionIssuer": {
            "type": "Role",
            "principalId": "EXAMPLEAIZ5FYRFP3POCC",
            "arn": "arn:aws:iam::111122223333:role/Admin",
            "accountId": "111122223333",
            "john-doe": "Admin"
          },
          "attributes": {
            "creationDate": "2023-10-14T00:48:50Z",
            "mfaAuthenticated": "false"
          }
        }
      },
      "eventTime": "2023-10-14T01:16:45Z",
      "eventSource": "cost-optimization-hub.amazonaws.com",
      "eventName": "ListEnrollmentStatuses",
      "awsRegion": "us-east-1",
      "sourceIPAddress": "192.0.2.0",
      "userAgent": "PostmanRuntime/7.28.3",
      "errorCode": "ThrottlingException",
      "requestParameters": null,
      "responseElements": null,
      "requestID": "cc04aa10-7417-4c46-b1eb-EXAMPLE1df2b",
      "eventID": "754a3aad-1b54-456a-ac1f-EXAMPLE0e9c3",
      "readOnly": true,
      "eventType": "AwsApiCall",
      "managementEvent": true,
      "recipientAccountId": "111122223333",
      "eventCategory": "Management",
      "tlsDetails": {
        "clientProvidedHostHeader": "localhost:8080"
      }
    }
```

### Access denied exception

The following example shows a log entry for an `AccessDenied`
exception.

```
{
      "eventVersion": "1.09",
      "userIdentity": {
        "type": "AssumedRole",
        "principalId": "EXAMPLEAIZ5FTKD2BZKUK:john-doe",
        "arn": "arn:aws:sts::111122223333:assumed-role/ReadOnly/john-doe",
        "accountId": "111122223333",
        "accessKeyId": "AKIAIOSFODNN7EXAMPLE",
        "sessionContext": {
          "sessionIssuer": {
            "type": "Role",
            "principalId": "EXAMPLEAIZ5FTKD2BZKUK",
            "arn": "arn:aws:iam::111122223333:role/ReadOnly",
            "accountId": "111122223333",
            "john-doe": "ReadOnly"
          },
          "attributes": {
            "creationDate": "2023-10-16T19:08:36Z",
            "mfaAuthenticated": "false"
          }
        }
      },
      "eventTime": "2023-10-16T19:11:04Z",
      "eventSource": "cost-optimization-hub.amazonaws.com",
      "eventName": "ListEnrollmentStatuses",
      "awsRegion": "us-east-1",
      "sourceIPAddress": "192.0.2.0",
      "userAgent": "PostmanRuntime/7.28.3",
      "errorCode": "AccessDenied",
      "errorMessage": "User: arn:aws:sts::111122223333:assumed-role/ReadOnly/john-doe is not authorized to perform: cost-optimization-hub:ListEnrollmentStatuses on resource: * because no identity-based policy allows the cost-optimization-hub:ListEnrollmentStatuses action",
      "requestParameters": null,
      "responseElements": null,
      "requestID": "1e02d84a-b04a-4b71-8615-EXAMPLEdcda7",
      "eventID": "71c86695-d4ec-4caa-a106-EXAMPLEe0d94",
      "readOnly": true,
      "eventType": "AwsApiCall",
      "managementEvent": true,
      "recipientAccountId": "111122223333",
      "eventCategory": "Management",
      "tlsDetails": {
        "clientProvidedHostHeader": "localhost:8080"
      }
    }
```

### ListEnrollmentStatus

The following example shows a log entry for the `ListEnrollmentStatus` API
action.

```
    {
      "eventVersion": "1.09",
      "userIdentity": {
        "type": "AssumedRole",
        "principalId": "EXAMPLEAIZ5FYRFP3POCC:john-doe",
        "arn": "arn:aws:sts::111122223333:assumed-role/Admin/john-doe",
        "accountId": "111122223333",
        "accessKeyId": "AKIAIOSFODNN7EXAMPLE",
        "sessionContext": {
          "sessionIssuer": {
            "type": "Role",
            "principalId": "EXAMPLEAIZ5FYRFP3POCC",
            "arn": "arn:aws:iam::111122223333:role/Admin",
            "accountId": "111122223333",
            "john-doe": "Admin"
          },
          "attributes": {
            "creationDate": "2023-10-14T00:48:50Z",
            "mfaAuthenticated": "false"
          }
        }
      },
      "eventTime": "2023-10-14T01:16:43Z",
      "eventSource": "cost-optimization-hub.amazonaws.com",
      "eventName": "ListEnrollmentStatuses",
      "awsRegion": "us-east-1",
      "sourceIPAddress": "192.0.2.0",
      "userAgent": "PostmanRuntime/7.28.3",
      "requestParameters": {
        "includeOrganizationInfo": false
      },
      "responseElements": null,
      "requestID": "cba87aa3-4678-41b8-a840-EXAMPLEaf3b8",
      "eventID": "57f04d0e-61f7-4c0f-805c-EXAMPLEbbbf5",
      "readOnly": true,
      "eventType": "AwsApiCall",
      "managementEvent": true,
      "recipientAccountId": "111122223333",
      "eventCategory": "Management",
      "tlsDetails": {
        "clientProvidedHostHeader": "localhost:8080"
      }
    }
```

### ListRecommendations

The following example shows a log entry for the `ListRecommendations` API
action.

```
    {
      "eventVersion": "1.09",
      "userIdentity": {
        "type": "AssumedRole",
        "principalId": "EXAMPLEAIZ5FYRFP3POCC:john-doe",
        "arn": "arn:aws:sts::111122223333:assumed-role/Admin/john-doe",
        "accountId": "111122223333",
        "accessKeyId": "AKIAI44QH8DHBEXAMPLE",
        "sessionContext": {
          "sessionIssuer": {
            "type": "Role",
            "principalId": "EXAMPLEAIZ5FYRFP3POCC",
            "arn": "arn:aws:iam::111122223333:role/Admin",
            "accountId": "111122223333",
            "john-doe": "Admin"
          },
          "attributes": {
            "creationDate": "2023-10-16T23:47:55Z",
            "mfaAuthenticated": "false"
          }
        }
      },
      "eventTime": "2023-10-17T00:45:29Z",
      "eventSource": "cost-optimization-hub.amazonaws.com",
      "eventName": "ListRecommendations",
      "awsRegion": "us-east-1",
      "sourceIPAddress": "192.0.2.0",
      "userAgent": "PostmanRuntime/7.28.3",
      "requestParameters": {
        "filter": {
          "resourceIdentifiers": [
            "arn:aws:ecs:us-east-1:111122223333:service/EXAMPLEAccountsIntegrationService-EcsCluster-ClusterEB0386A7-7fsvP2MMmxZ5/EXAMPLEAccountsIntegrationService-EcsService-Service9571FDD8-Dqm4mPMLstDn"
          ]
        },
        "includeAllRecommendations": false
      },
      "responseElements": null,
      "requestID": "a5b2df72-2cfd-4628-8a72-EXAMPLE7560a",
      "eventID": "a73bef13-6af7-4c11-a708-EXAMPLE6af5c",
      "readOnly": true,
      "eventType": "AwsApiCall",
      "managementEvent": true,
      "recipientAccountId": "111122223333",
      "eventCategory": "Management",
      "tlsDetails": {
        "clientProvidedHostHeader": "cost-optimization-hub.us-east-1.amazonaws.com"
      }
    }
```

### ListRecommendationSummaries

The following example shows a log entry for the `ListRecommendationSummaries`
API action.

```
    {
      "eventVersion": "1.09",
      "userIdentity": {
        "type": "AssumedRole",
        "principalId": "EXAMPLEAIZ5FYRFP3POCC:john-doe",
        "arn": "arn:aws:sts::111122223333:assumed-role/Admin/john-doe",
        "accountId": "111122223333",
        "accessKeyId": "AKIAI44QH8DHBEXAMPLE",
        "sessionContext": {
          "sessionIssuer": {
            "type": "Role",
            "principalId": "EXAMPLEAIZ5FYRFP3POCC",
            "arn": "arn:aws:iam::111122223333:role/Admin",
            "accountId": "111122223333",
            "userName": "Admin"
          },
          "attributes": {
            "creationDate": "2023-10-16T23:47:55Z",
            "mfaAuthenticated": "false"
          }
        }
      },
      "eventTime": "2023-10-17T00:46:16Z",
      "eventSource": "cost-optimization-hub.amazonaws.com",
      "eventName": "ListRecommendationSummaries",
      "awsRegion": "us-east-1",
      "sourceIPAddress": "192.0.2.0",
      "userAgent": "PostmanRuntime/7.28.3",
      "requestParameters": {
        "groupBy": "ResourceType"
      },
      "responseElements": null,
      "requestID": "ab54e6ad-72fe-48fe-82e9-EXAMPLEa6d1e",
      "eventID": "9288d9fa-939d-4e5f-a49a-EXAMPLEeb14b",
      "readOnly": true,
      "eventType": "AwsApiCall",
      "managementEvent": true,
      "recipientAccountId": "111122223333",
      "eventCategory": "Management",
      "tlsDetails": {
        "clientProvidedHostHeader": "cost-optimization-hub.us-east-1.amazonaws.com"
      }
    }
```

### GetRecommendation

The following example shows a log entry for the `GetRecommendation` API
action.

```
    {
      "eventVersion": "1.09",
      "userIdentity": {
        "type": "AssumedRole",
        "principalId": "EXAMPLEAIZ5FYRFP3POCC:john-doe",
        "arn": "arn:aws:sts::111122223333:assumed-role/Admin/john-doe",
        "accountId": "111122223333",
        "accessKeyId": "AKIAI44QH8DHBEXAMPLE",
        "sessionContext": {
          "sessionIssuer": {
            "type": "Role",
            "principalId": "EXAMPLEAIZ5FYRFP3POCC",
            "arn": "arn:aws:iam::111122223333:role/Admin",
            "accountId": "111122223333",
            "john-doe": "Admin"
          },
          "attributes": {
            "creationDate": "2023-10-16T23:47:55Z",
            "mfaAuthenticated": "false"
          }
        }
      },
      "eventTime": "2023-10-17T00:47:48Z",
      "eventSource": "cost-optimization-hub.amazonaws.com",
      "eventName": "GetRecommendation",
      "awsRegion": "us-east-1",
      "sourceIPAddress": "192.0.2.0",
      "userAgent": "PostmanRuntime/7.28.3",
      "requestParameters": {
        "recommendationId": "EXAMPLEwMzEwODU5XzQyNTFhNGE4LWZkZDItNDUyZi1hMjY4LWRkOTFkOTA1MTc1MA=="
      },
      "responseElements": null,
      "requestID": "e289a76a-182c-4bc9-8093-EXAMPLEbed0e",
      "eventID": "f1ed7ee6-871c-41fd-bb27-EXAMPLE24b64",
      "readOnly": true,
      "eventType": "AwsApiCall",
      "managementEvent": true,
      "recipientAccountId": "111122223333",
      "eventCategory": "Management",
      "tlsDetails": {
        "clientProvidedHostHeader": "cost-optimization-hub.us-east-1.amazonaws.com"
      }
    }
```

### UpdateEnrollmentStatus

The following example shows a log entry for the `UpdateEnrollmentStatus` API
action.

```
{
      "eventVersion": "1.09",
      "userIdentity": {
        "type": "AssumedRole",
        "principalId": "EXAMPLEAIZ5FYRFP3POCC:john-doe",
        "arn": "arn:aws:sts::111122223333:assumed-role/Admin/john-doe",
        "accountId": "111122223333",
        "accessKeyId": "AKIAI44QH8DHBEXAMPLE",
        "sessionContext": {
          "sessionIssuer": {
            "type": "Role",
            "principalId": "EXAMPLEAIZ5FYRFP3POCC",
            "arn": "arn:aws:iam::111122223333:role/Admin",
            "accountId": "111122223333",
            "john-doe": "Admin"
          },
          "attributes": {
            "creationDate": "2023-10-16T19:11:30Z",
            "mfaAuthenticated": "false"
          }
        }
      },
      "eventTime": "2023-10-16T19:12:35Z",
      "eventSource": "cost-optimization-hub.amazonaws.com",
      "eventName": "UpdateEnrollmentStatus",
      "awsRegion": "us-east-1",
      "sourceIPAddress": "192.0.2.0",
      "userAgent": "PostmanRuntime/7.28.3",
      "requestParameters": {
        "status": "Inactive"
      },
      "responseElements": {
        "status": "Inactive"
      },
      "requestID": "6bf0c8a3-af53-4c4e-8f50-EXAMPLE477f0",
      "eventID": "d2bfa850-ef3d-4317-8ac4-EXAMPLEc16b1",
      "readOnly": false,
      "eventType": "AwsApiCall",
      "managementEvent": true,
      "recipientAccountId": "111122223333",
      "eventCategory": "Management",
      "tlsDetails": {
        "clientProvidedHostHeader": "localhost:8080"
      }
    }
```

### UpdatePreferences

The following example shows a log entry for the `UpdatePreferences` API
action.

```
    {
      "eventVersion": "1.09",
      "userIdentity": {
        "type": "AssumedRole",
        "principalId": "EXAMPLEAIZ5FYRFP3POCC:john-doe",
        "arn": "arn:aws:sts::111122223333:assumed-role/Admin/john-doe",
        "accountId": "111122223333",
        "accessKeyId": "AKIAI44QH8DHBEXAMPLE",
        "sessionContext": {
          "sessionIssuer": {
            "type": "Role",
            "principalId": "EXAMPLEAIZ5FYRFP3POCC",
            "arn": "arn:aws:iam::111122223333:role/Admin",
            "accountId": "111122223333",
            "john-doe": "Admin"
          },
          "attributes": {
            "creationDate": "2023-10-16T19:11:30Z",
            "mfaAuthenticated": "false"
          }
        }
      },
      "eventTime": "2023-10-16T19:16:00Z",
      "eventSource": "cost-optimization-hub.amazonaws.com",
      "eventName": "UpdatePreferences",
      "awsRegion": "us-east-1",
      "sourceIPAddress": "192.0.2.0",
      "userAgent": "PostmanRuntime/7.28.3",
      "requestParameters": {
        "costMetricsType": "AfterDiscounts"
      },
      "responseElements": {
        "costMetricsType": "AfterDiscounts",
        "memberAccountDiscountVisibility": "None"
      },
      "requestID": "01e56ca3-47af-45f0-85aa-EXAMPLE30b42",
      "eventID": "7350ff23-35f5-4760-98b2-EXAMPLE61f13",
      "readOnly": false,
      "eventType": "AwsApiCall",
      "managementEvent": true,
      "recipientAccountId": "111122223333",
      "eventCategory": "Management",
      "tlsDetails": {
        "clientProvidedHostHeader": "localhost:8080"
      }
    }
```

## Understanding AWS Pricing Calculator log file entries

A trail is a configuration that enables delivery of events as log files to an Amazon S3 bucket
that you specifyincluding events for AWS Pricing Calculator. If you don't configure a trail, you
can still view the most recent events in the CloudTrail console in Event history. Using the
information collected by CloudTrail, you can determine the request that was made to AWS Pricing Calculator, the
IP address from which the request was made, who made the request, when it was made, and additional details.

### AWS Pricing Calculator CloudTrail events

This section shows a full list of the CloudTrail events related to Pricing Calculator.

###### Note

The event source for the following events is `bcm-pricing-calculator.amazonaws.com`.

| Event name                                       | Definition                                                                                                                                            |
| ------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `CreateWorkloadEstimate`                         | Mutating operation. Allows customers to create a Workload estimate.                                                                                   |
| `UpdateWorkloadEstimate`                         | Mutating operation. Allows customers to update a Workload estimate metadata.                                                                          |
| `DeleteWorkloadEstimate`                         | Mutating operation. Allows customers to delete a Workload estimate.                                                                                   |
| `GetWorkloadEstimate`                            | Non-mutating operation. Allows customers to get details of a Workload estimate.                                                                       |
| `ListWorkloadEstimates`                          | Non-mutating operation. Allows customers to list all Workload estimates in their account.                                                             |
| `ListWorkloadEstimateUsage`                      | Non-mutating operation. Allows customers to list all usage lines in a Workload estimate.                                                              |
| `BatchCreateWorkloadEstimateUsage`               | Mutating operation. Allows customers to create usage lines in their Workload estimate.                                                                |
| `BatchUpdateWorkloadEstimateUsage`               | Mutating operation. Allows customers to modify existing usage lines in their Workload estimate.                                                       |
| `BatchDeleteWorkloadEstimateUsage`               | Mutating operation. Allows customers to delete added usage lines in their Workload estimate.                                                          |
| `CreateBillScenario`                             | Mutating operation. Allows customers to create a Bill scenario.                                                                                       |
| `GetBillScenario`                                | Mutating operation. Allows customers to get details of a Bill scenario.                                                                               |
| `UpdateBillScenario`                             | Mutating operation. Allows customers to update metadata of a Bill scenario.                                                                           |
| `DeleteBillScenario`                             | Mutating operation. Allows customers to delete a Bill scenario.                                                                                       |
| `ListBillScenarios`                              | Non-mutating operation. Allows customers to list all Bill scenarios in their account.                                                                 |
| `BatchCreateBillScenarioUsageModifications`      | Mutating operation. Allows customers to create usage lines in their Bill scenario.                                                                    |
| `BatchUpdateBillScenarioUsageModifications`      | Mutating operation. Allows customers to modify existing usage lines in their Bill scenario.                                                           |
| `BatchDeleteBillScenarioUsageModifications`      | Mutating operation. Allows customers to delete existing usage lines in their Bill scenario.                                                           |
| `ListBillScenarioUsageModifications`             | Non-mutating operation. Allows customers to list all usage lines in a Bill scenario.                                                                  |
| `BatchCreateBillScenarioCommitmentModifications` | Mutating operation. Allows customers to model commitments in their Bill scenario.                                                                     |
| `BatchUpdateBillScenarioCommitmentModifications` | Mutating operation. Allows customers to modify modeled commitment lines in their Bill scenario.                                                       |
| `BatchDeleteBillScenarioCommitmentModifications` | Mutating operation. Allows customers to delete modeled commitment lines in their Bill scenario.                                                       |
| `ListBillScenarioCommitmentModifications`        | Non-mutating operation. Allows customers to list all modeled commitments in a Bill scenario.                                                          |
| `CreateBillEstimate`                             | Mutating operation. Allows customers to create a new Bill estimate from a Bill scenario.                                                              |
| `GetBillEstimate`                                | Mutating operation. Allows customers to get details of a Bill estimate.                                                                               |
| `UpdateBillEstimate`                             | Mutating operation. Allows customers to update metadata of a Bill estimate.                                                                           |
| `DeleteBillEstimate`                             | Mutating operation. Allows customers to delete a Bill estimate.                                                                                       |
| `ListBillEstimates`                              | Non-mutating operation. Allows customers to list all Bill estimates in their account.                                                                 |
| `ListBillEstimateLineItems`                      | Non-mutating operation. Allows customers to list all result lines of a successfull completed Bill estimate.                                           |
| `ListBillEstimateCommitments`                    | Non-mutating operation. Allows customers to list all commitments of a successfull completed Bill estimate.                                            |
| `ListBillEstimateInputUsageModifications`        | Non-mutating operation. Allows customers to list all commitments modeled in a Bill scenario that contributed to creating a Bill estimate.             |
| `GetPreferences`                                 | Non-mutating operation. Allows customers to get rate preferences set by the payer or standalone account                                               |
| `UpdatePreferences`                              | Mutating operation. Allows customers to set rate preferences for use in Workload estimates. This is a payer or standalone account only API operation. |
| `TagResource`                                    | Mutating operation. Allows customers to tag a Pricing Calculator resource.                                                                            |
| `UntagResource`                                  | Mutating operation. Allows customers to un-tag a Pricing Calculator resource.                                                                         |
| `ListTagsForResource`                            | Non-mutating operation. Allows customers to list all tags attached to a Pricing Calculator resource.                                                  | ### CreateWorkloadEstimate The following example shows a CloudTrail log entry that uses the `CreateWorkloadEstimate` API action. ``` { "eventVersion": "1.08", "userIdentity": { "accountId": "111122223333", "accessKeyId": "AKIAI44QH8DHBEXAMPLE" }, "eventTime": "2024-11-11T02:09:08Z", "eventSource": "bcm-pricing-calculator.amazonaws.com", "eventName": "CreateWorkloadEstimate", "awsRegion": "us-east-1", "sourceIPAddress": "100.100.10.10", "requestParameters": { "name": "example-estimate-name", "resourceTags": [], "rateType": "BEFORE_DISCOUNTS" }, "responseElements": { "costCurrency": "USD", "costSummary": { "cost": 0, "costStatus": "VALID", "currency": "USD" }, "createdAt": 1731290948.299, "expiresAt": 1765418948.299, "id": "15cf39cc-ce14-4943-9dcb-35ccec39ae21", "name": "example-estimate-name", "rateDescription": "BEFORE_DISCOUNTS | 2024-11-11T02:09:08.299974018Z", "rateTimestamp": 1731290948.299, "rateType": "BEFORE_DISCOUNTS", "status": "READY", "totalCost": 0 }, "eventID": "22bb9d97-6f0c-4482-830d-cde1c9ea00be", "readOnly": false, "eventType": "AwsApiCall", "managementEvent": true, "recipientAccountId": "111122223333", "eventCategory": "Management" } ``` |
