# Logging AWS Launch Wizard API calls using AWS CloudTrail

AWS Launch Wizard is integrated with AWS CloudTrail, a service that provides a record of actions taken
by a user, role, or an AWS service. CloudTrail captures API calls for AWS Launch Wizard as events. The
calls captured include calls from the AWS Management Console and code calls to the AWS Launch Wizard API operations.
Using the information collected by CloudTrail, you can determine the request that was made to
AWS Launch Wizard, the IP address from which the request was made, when it was made, and additional
details.

Every event or log entry contains information about who generated the request. The
identity information helps you determine the following:

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

## AWS Launch Wizard management events in CloudTrail

[Management events](../../../awscloudtrail/latest/userguide/logging-management-events-with-cloudtrail.md#logging-management-events "../../../awscloudtrail/latest/userguide/logging-management-events-with-cloudtrail.md#logging-management-events") provide information about management operations that are performed on resources in your AWS account. These are also known as control plane operations. By default, CloudTrail logs management events.

AWS Launch Wizard logs control plane operations as management events. For a list of the
control plane operations, see the [AWS Launch Wizard API Reference](../APIReference.md "../APIReference.md").

## CloudTrail event examples

An event represents a single request from any source and includes information about the requested API operation, the date and time of the operation, request parameters, and so on. CloudTrail log files aren't an ordered stack trace of the public API calls, so events don't appear in any specific order.

###### Examples

- [Example: CreateDeployment](#cloudtrail-event-example-createdeployment "#cloudtrail-event-example-createdeployment")
- [Example: DeleteDeployment](#cloudtrail-event-example-deletedeployment "#cloudtrail-event-example-deletedeployment")
- [Example: GetDeployment](#cloudtrail-event-example-getdeployment "#cloudtrail-event-example-getdeployment")
- [Example: GetWorkload](#cloudtrail-event-example-getworkload "#cloudtrail-event-example-getworkload")
- [Example: ListDeploymentEvents](#cloudtrail-event-example-listdeploymentevents "#cloudtrail-event-example-listdeploymentevents")
- [Example: ListDeployments](#cloudtrail-event-example-listdeployments "#cloudtrail-event-example-listdeployments")
- [Example: ListWorkloadDeploymentPattern](#cloudtrail-event-example-listWorkloaddeploymentpattern "#cloudtrail-event-example-listWorkloaddeploymentpattern")
- [Example: ListWorkloads](#cloudtrail-event-example-listworkloads "#cloudtrail-event-example-listworkloads")

### Example: CreateDeployment

The following example shows a CloudTrail log entry that demonstrates the
`CreateDeployment` operation.

```
{
    "eventVersion": "1.08",
    "userIdentity": {
        "type": "AssumedRole",
        "principalId": "AIDAQRSTUVWXYZEXAMPLE:ExampleAssumedRoleSessionName",
        "arn": "arn:aws:sts::123456789012:assumed-role/ExampleAssumedRole/ExampleRoleSessionName",
        "accountId": "123456789012",
        "accessKeyId": "AKIAIOSFODNN7EXAMPLE",
        "sessionContext": {
            "sessionIssuer": {
                "type": "Role",
                "principalId": "AIDAQRSTUVWXYZEXAMPLE",
                "arn": "arn:aws:iam::123456789012:role/ExampleAssumedRole",
                "accountId": "123456789012",
                "userName": "ExampleAssumedRole"
            },
            "webIdFederationData": {},
            "attributes": {
                "creationDate": "2023-09-05T17:45:15Z",
                "mfaAuthenticated": "false"
            }
        }
    },
    "eventTime": "2023-09-05T17:45:27Z",
    "eventSource": "launchwizard.amazonaws.com",
    "eventName": "CreateDeployment",
    "awsRegion": "us-east-1",
    "sourceIPAddress": "192.0.2.0",
    "userAgent": "aws-cli/2.2.17 Python/3.8.8 Darwin/21.6.0 exe/x86_64 prompt/off command/example",
    "errorCode": "InternalServerException",
    "requestParameters": {
        "workloadName": "SAP",
        "name": "Example",
        "specifications": "Example",
        "deploymentPatternName": "SapHanaSingle"
    },
    "responseElements": $null,
    "requestID": "86168559-75e9-11e4-8cf8-75d18EXAMPLE",
    "eventID": "832b82d5-d474-44e8-a51d-093ccEXAMPLE",
    "readOnly": false,
    "eventType": "AwsApiCall",
    "managementEvent": true,
    "recipientAccountId": "123456789012",
    "eventCategory": "Management"
}
```

[Show moreShow less](# "#")

### Example: DeleteDeployment

The following example shows a CloudTrail log entry that demonstrates the
`DeleteDeployment` operation.

```
{
    "eventVersion": "1.08",
    "userIdentity": {
        "type": "AssumedRole",
        "principalId": "AIDAQRSTUVWXYZEXAMPLE:ExampleAssumedRoleSessionName",
        "arn": "arn:aws:sts::123456789012:assumed-role/ExampleAssumedRole/ExampleRoleSessionName",
        "accountId": "123456789012",
        "accessKeyId": "AKIAIOSFODNN7EXAMPLE",
        "sessionContext": {
            "sessionIssuer": {
                "type": "Role",
                "principalId": "AIDAQRSTUVWXYZEXAMPLE",
                "arn": "arn:aws:iam::123456789012:role/ExampleAssumedRole",
                "accountId": "123456789012",
                "userName": "ExampleAssumedRole"
            },
            "webIdFederationData": {},
            "attributes": {
                "creationDate": "2023-09-05T17:45:15Z",
                "mfaAuthenticated": "false"
            }
        }
    },
    "eventTime": "2023-09-06T16:42:53Z",
    "eventSource": "launchwizard.amazonaws.com",
    "eventName": "DeleteDeployment",
    "awsRegion": "us-east-1",
    "sourceIPAddress": "192.0.2.0",
    "userAgent": "aws-cli/2.2.17 Python/3.8.8 Darwin/21.6.0 exe/x86_64 prompt/off command/lw.delete-deployment",
    "errorCode": "ValidationException",
    "requestParameters": {
        "deploymentId": "DeploymentIdExample"
    },
    "responseElements": {
        "message": "Example Message."
    },
    "requestID": "86168559-75e9-11e4-8cf8-75d18EXAMPLE",
    "eventID": "832b82d5-d474-44e8-a51d-093ccEXAMPLE",
    "readOnly": false,
    "eventType": "AwsApiCall",
    "managementEvent": true,
    "recipientAccountId": "123456789012",
    "eventCategory": "Management"
}
```

[Show moreShow less](# "#")

### Example: GetDeployment

The following example shows a CloudTrail log entry that demonstrates the
`GetDeployment` operation.

```
{
    "eventVersion": "1.08",
    "userIdentity": {
        "type": "AssumedRole",
        "principalId": "AIDAQRSTUVWXYZEXAMPLE:ExampleAssumedRoleSessionName",
        "arn": "arn:aws:sts::123456789012:assumed-role/ExampleAssumedRole/ExampleRoleSessionName",
        "accountId": "123456789012",
        "accessKeyId": "AKIAIOSFODNN7EXAMPLE",
        "sessionContext": {
            "sessionIssuer": {
                "type": "Role",
                "principalId": "AIDAQRSTUVWXYZEXAMPLE",
                "arn": "arn:aws:iam::123456789012:role/ExampleAssumedRole",
                "accountId": "123456789012",
                "userName": "ExampleAssumedRole"
            },
            "webIdFederationData": {},
            "attributes": {
                "creationDate": "2023-09-05T17:45:15Z",
                "mfaAuthenticated": "false"
            }
        }
    },
    "eventTime": "2023-09-06T03:39:02Z",
    "eventSource": "launchwizard.amazonaws.com",
    "eventName": "GetDeployment",
    "awsRegion": "us-east-1",
    "sourceIPAddress": "192.0.2.0",
    "userAgent": "aws-cli/2.2.17 Python/3.8.8 Darwin/21.6.0 exe/x86_64 prompt/off command/example",
    "requestParameters": {
        "deploymentId": "DeploymentIdExample"
    },
    "responseElements": null,
    "requestID": "86168559-75e9-11e4-8cf8-75d18EXAMPLE",
    "eventID": "832b82d5-d474-44e8-a51d-093ccEXAMPLE",
    "readOnly": true,
    "eventType": "AwsApiCall",
    "managementEvent": true,
    "recipientAccountId": "123456789012",
    "eventCategory": "Management"
}
```

[Show moreShow less](# "#")

### Example: GetWorkload

The following example shows a CloudTrail log entry that demonstrates the
`GetWorkload` operation.

```
{
    "eventVersion": "1.08",
    "userIdentity": {
        "type": "AssumedRole",
        "principalId": "AIDAQRSTUVWXYZEXAMPLE:ExampleAssumedRoleSessionName",
        "arn": "arn:aws:sts::123456789012:assumed-role/ExampleAssumedRole/ExampleRoleSessionName",
        "accountId": "123456789012",
        "accessKeyId": "AKIAIOSFODNN7EXAMPLE",
        "sessionContext": {
            "sessionIssuer": {
                "type": "Role",
                "principalId": "AIDAQRSTUVWXYZEXAMPLE",
                "arn": "arn:aws:iam::123456789012:role/ExampleAssumedRole",
                "accountId": "123456789012",
                "userName": "ExampleAssumedRole"
            },
            "webIdFederationData": {},
            "attributes": {
                "creationDate": "2023-09-05T17:45:15Z",
                "mfaAuthenticated": "false"
            }
        }
    },
    "eventTime": "2023-09-06T03:59:32Z",
    "eventSource": "launchwizard.amazonaws.com",
    "eventName": "GetWorkload",
    "awsRegion": "us-east-1",
    "sourceIPAddress": "192.0.2.0",
    "userAgent": "aws-cli/2.2.17 Python/3.8.8 Darwin/21.6.0 exe/x86_64 prompt/off command/example",
    "requestParameters": {
        "workloadName": "SAP"
    },
    "responseElements": null,
    "requestID": "86168559-75e9-11e4-8cf8-75d18EXAMPLE",
    "eventID": "832b82d5-d474-44e8-a51d-093ccEXAMPLE",
    "readOnly": true,
    "eventType": "AwsApiCall",
    "managementEvent": true,
    "recipientAccountId": "123456789012",
    "eventCategory": "Management"
}
```

[Show moreShow less](# "#")

### Example: ListDeploymentEvents

The following example shows a CloudTrail log entry that demonstrates the
`ListDeploymentEvents` operation.

```
{
    "eventVersion": "1.08",
    "userIdentity": {
        "type": "AssumedRole",
        "principalId": "AIDAQRSTUVWXYZEXAMPLE:ExampleAssumedRoleSessionName",
        "arn": "arn:aws:sts::123456789012:assumed-role/ExampleAssumedRole/ExampleRoleSessionName",
        "accountId": "123456789012",
        "accessKeyId": "AKIAIOSFODNN7EXAMPLE",
        "sessionContext": {
            "sessionIssuer": {
                "type": "Role",
                "principalId": "AIDAQRSTUVWXYZEXAMPLE",
                "arn": "arn:aws:iam::123456789012:role/ExampleAssumedRole",
                "accountId": "123456789012",
                "userName": "ExampleAssumedRole"
            },
            "webIdFederationData": {},
            "attributes": {
                "creationDate": "2023-09-05T17:45:15Z",
                "mfaAuthenticated": "false"
            }
        }
    },
    "eventTime": "2023-09-06T03:38:02Z",
    "eventSource": "launchwizard.amazonaws.com",
    "eventName": "ListDeploymentEvents",
    "awsRegion": "us-east-1",
    "sourceIPAddress": "192.0.2.0",
    "userAgent": "aws-cli/2.2.17 Python/3.8.8 Darwin/21.6.0 exe/x86_64 prompt/off command/example",
    "requestParameters": {
        "deploymentId": "DeploymentIdExample"
    },
    "responseElements": null,
    "requestID": "86168559-75e9-11e4-8cf8-75d18EXAMPLE",
    "eventID": "832b82d5-d474-44e8-a51d-093ccEXAMPLE",
    "readOnly": true,
    "eventType": "AwsApiCall",
    "managementEvent": true,
    "recipientAccountId": "123456789012",
    "eventCategory": "Management"
}
```

[Show moreShow less](# "#")

### Example: ListDeployments

The following example shows a CloudTrail log entry that demonstrates the
`ListDeployments` operation.

```
{
    "eventVersion": "1.08",
    "userIdentity": {
        "type": "AssumedRole",
        "principalId": "AIDAQRSTUVWXYZEXAMPLE:ExampleAssumedRoleSessionName",
        "arn": "arn:aws:sts::123456789012:assumed-role/ExampleAssumedRole/ExampleRoleSessionName",
        "accountId": "123456789012",
        "accessKeyId": "AKIAIOSFODNN7EXAMPLE",
        "sessionContext": {
            "sessionIssuer": {
                "type": "Role",
                "principalId": "AIDAQRSTUVWXYZEXAMPLE",
                "arn": "arn:aws:iam::123456789012:role/ExampleAssumedRole",
                "accountId": "123456789012",
                "userName": "ExampleAssumedRole"
            },
            "webIdFederationData": {},
            "attributes": {
                "creationDate": "2023-09-05T17:45:15Z",
                "mfaAuthenticated": "false"
            }
        }
    },
    "eventTime": "2023-09-06T03:38:02Z",
    "eventSource": "launchwizard.amazonaws.com",
    "eventName": "ListDeployments",
    "awsRegion": "us-east-1",
    "sourceIPAddress": "192.0.2.0",
    "userAgent": "aws-cli/2.2.17 Python/3.8.8 Darwin/21.6.0 exe/x86_64 prompt/off command/example",
    "requestParameters": {
        "maxResults": 100
    },
    "responseElements": null,
    "requestID": "86168559-75e9-11e4-8cf8-75d18EXAMPLE",
    "eventID": "832b82d5-d474-44e8-a51d-093ccEXAMPLE",
    "readOnly": true,
    "eventType": "AwsApiCall",
    "managementEvent": true,
    "recipientAccountId": "123456789012",
    "eventCategory": "Management"
}
```

[Show moreShow less](# "#")

### Example: ListWorkloadDeploymentPattern

The following example shows a CloudTrail log entry that demonstrates the
`ListWorkloadDeploymentPattern` operation.

```
{
    "eventVersion": "1.08",
    "userIdentity": {
        "type": "AssumedRole",
        "principalId": "AIDAQRSTUVWXYZEXAMPLE:ExampleAssumedRoleSessionName",
        "arn": "arn:aws:sts::123456789012:assumed-role/ExampleAssumedRole/ExampleRoleSessionName",
        "accountId": "123456789012",
        "accessKeyId": "AKIAIOSFODNN7EXAMPLE",
        "sessionContext": {
            "sessionIssuer": {
                "type": "Role",
                "principalId": "AIDAQRSTUVWXYZEXAMPLE",
                "arn": "arn:aws:iam::123456789012:role/ExampleAssumedRole",
                "accountId": "123456789012",
                "userName": "ExampleAssumedRole"
            },
            "webIdFederationData": {},
            "attributes": {
                "creationDate": "2023-09-05T17:45:15Z",
                "mfaAuthenticated": "false"
            }
        }
    },
    "eventTime": "2023-09-06T03:59:32Z",
    "eventSource": "launchwizard.amazonaws.com",
    "eventName": "ListWorkloadDeploymentPatterns",
    "awsRegion": "us-east-1",
    "sourceIPAddress": "192.0.2.0",
    "userAgent": "aws-cli/2.2.17 Python/3.8.8 Darwin/21.6.0 exe/x86_64 prompt/off command/example",
    "requestParameters": {
        "workloadName": "SAP",
        "maxResults": 10
    },
    "responseElements": null,
    "requestID": "86168559-75e9-11e4-8cf8-75d18EXAMPLE",
    "eventID": "832b82d5-d474-44e8-a51d-093ccEXAMPLE",
    "readOnly": true,
    "eventType": "AwsApiCall",
    "managementEvent": true,
    "recipientAccountId": "123456789012",
    "eventCategory": "Management"
}
```

[Show moreShow less](# "#")

### Example: ListWorkloads

The following example shows a CloudTrail log entry that demonstrates the
`ListWorkloads` operation.

```
{
    "eventVersion": "1.08",
    "userIdentity": {
        "type": "AssumedRole",
        "principalId": "AIDAQRSTUVWXYZEXAMPLE:ExampleAssumedRoleSessionName",
        "arn": "arn:aws:sts::123456789012:assumed-role/ExampleAssumedRole/ExampleRoleSessionName",
        "accountId": "123456789012",
        "accessKeyId": "AKIAIOSFODNN7EXAMPLE",
        "sessionContext": {
            "sessionIssuer": {
                "type": "Role",
                "principalId": "AIDAQRSTUVWXYZEXAMPLE",
                "arn": "arn:aws:iam::123456789012:role/ExampleAssumedRole",
                "accountId": "123456789012",
                "userName": "ExampleAssumedRole"
            },
            "webIdFederationData": {},
            "attributes": {
                "creationDate": "2023-09-05T17:45:15Z",
                "mfaAuthenticated": "false"
            }
        }
    },
    "eventTime": "2023-09-06T03:59:32Z",
    "eventSource": "launchwizard.amazonaws.com",
    "eventName": "ListWorkloads",
    "awsRegion": "us-east-1",
    "sourceIPAddress": "192.0.2.0",
    "userAgent": "aws-cli/2.2.17 Python/3.8.8 Darwin/21.6.0 exe/x86_64 prompt/off command/example",
    "requestParameters": null,
    "responseElements": null,
    "requestID": "86168559-75e9-11e4-8cf8-75d18EXAMPLE",
    "eventID": "832b82d5-d474-44e8-a51d-093ccEXAMPLE",
    "readOnly": true,
    "eventType": "AwsApiCall",
    "managementEvent": true,
    "recipientAccountId": "123456789012",
    "eventCategory": "Management"
}
```

[Show moreShow less](# "#")
