

# Logging Amazon Nova Act API calls using AWS CloudTrail
<a name="logging-using-cloudtrail"></a>

Amazon Nova Act is integrated with [AWS CloudTrail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-user-guide.html), a service that provides a record of actions taken by a user, role, or an AWS service. CloudTrail captures all API calls for Nova Act as events. The calls captured include calls from the Nova Act console and code calls to the Nova Act API operations. Using the information collected by CloudTrail, you can determine the request that was made to Nova Act, the IP address from which the request was made, when it was made, and additional details.

The event source for Nova Act is `nova-act.amazonaws.com`.

Every event or log entry contains information about who generated the request. The identity information helps you determine the following:
+ Whether the request was made with root or user credentials.
+ Whether the request was made on behalf of an IAM Identity Center user.
+ Whether the request was made with temporary security credentials for a role or federated user.
+ Whether the request was made by another AWS service.

 CloudTrail is active in your AWS account when you create the account and you automatically have access to the CloudTrail **Event history**. The CloudTrail **Event history** provides a viewable, searchable, downloadable, and immutable record of the past 90 days of recorded management events in an AWS Region. For more information, see [Working with CloudTrail Event history](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/view-cloudtrail-events.html) in the * AWS CloudTrail User Guide*. There are no CloudTrail charges for viewing the **Event history**.

For an ongoing record of events in your AWS account past 90 days, create a trail or a [CloudTrail Lake](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-lake.html) event data store.

 CloudTrail trails  
A trail enables CloudTrail to deliver log files to an Amazon Simple Storage Service bucket. All trails created using the AWS Management Console are multi-Region. You can create a single-Region or a multi-Region trail by using the AWS CLI. Creating a multi-Region trail is recommended because you capture activity in all AWS Regions in your account. If you create a single-Region trail, you can view only the events logged in the trail’s AWS Region. For more information about trails, see [Creating a trail for your AWS account](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-create-and-update-a-trail.html) and [Creating a trail for an organization](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/creating-trail-organization.html) in the * AWS CloudTrail User Guide*.

 CloudTrail Lake event data stores  
 CloudTrail Lake lets you run SQL-based queries on your events. CloudTrail Lake converts existing events in row-based JSON format to [Apache ORC](https://orc.apache.org/) format. ORC is a columnar storage format that is optimized for fast retrieval of data. Events are aggregated into event data stores, which are immutable collections of events based on criteria that you select by applying [advanced event selectors](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-lake-concepts.html#adv-event-selectors). The selectors that you apply to an event data store control which events persist and are available for you to query. For more information about CloudTrail Lake, see [Working with CloudTrail Lake](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-lake.html) in the * AWS CloudTrail User Guide*.

## Nova Act management events in CloudTrail
<a name="cloudtrail-management-events"></a>

 [Management events](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/logging-management-events-with-cloudtrail.html) provide information about management operations that are performed on resources in your AWS account. These are also known as control plane operations. By default, CloudTrail logs management events.

Amazon Nova Act logs the following control plane operations as management events in CloudTrail:
+  `CreateWorkflowDefinition` 
+  `GetWorkflowDefinition` 
+  `ListWorkflowDefinitions` 
+  `DeleteWorkflowDefinition` 
+  `GetWorkflowRun` 
+  `ListWorkflowRuns` 
+  `ListSessions` 
+  `ListActs` 
+  `ListModels` 

For full details on each operation, see the [Amazon Nova Act API Reference](https://docs.aws.amazon.com/nova-act/latest/APIReference/).

## Nova Act data events in CloudTrail
<a name="cloudtrail-data-events"></a>

 [Data events](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/logging-data-events-with-cloudtrail.html) provide information about the resource operations performed on or in a resource. These are also known as data plane operations. Data events are often high-volume activities.

By default, CloudTrail doesn’t log data events. You must explicitly enable logging of data events for Nova Act by configuring advanced event selectors on a trail or a CloudTrail Lake event data store. For more information, see [Logging data events](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/logging-data-events-with-cloudtrail.html) in the * AWS CloudTrail User Guide*.

Amazon Nova Act logs the following data plane operations as data events in CloudTrail:
+  `CreateSession` 
+  `CreateAct` 
+  `UpdateAct` 
+  `InvokeActStep` 

You can filter data events by resource ARN using the following formats:
+ Workflow definition: `arn:${Partition}:nova-act:${Region}:${Account}:workflow-definition/${WorkflowName} ` 
+ Workflow run: `arn:${Partition}:nova-act:${Region}:${Account}:workflow-definition/${WorkflowName}/workflow-run/${WorkflowRunId} ` 

**Note**  
Some data plane API requests and responses may contain personally identifiable information (PII) or user-controlled input. Certain fields in CloudTrail log entries for these APIs may be redacted to protect sensitive data.

## Nova Act event examples
<a name="cloudtrail-event-examples"></a>

An event represents a single request from any source and includes information about the requested API operation, the date and time of the operation, request parameters, and so on. CloudTrail log files aren’t an ordered stack trace of the public API calls, so events don’t appear in any specific order.

### Management event example
<a name="management-event-example"></a>

The following example shows a CloudTrail management event for the `CreateWorkflowDefinition` operation.

```
{
    "eventVersion": "1.08",
    "userIdentity": {
        "type": "AssumedRole",
        "principalId": "AROA1EXAMPLE:user",
        "arn": "arn:aws:sts::123456789012:assumed-role/ExampleRole/user",
        "accountId": "123456789012",
        "accessKeyId": "AKIAIOSFODNN7EXAMPLE",
        "sessionContext": {
            "sessionIssuer": {
                "type": "Role",
                "principalId": "AROA1EXAMPLE",
                "arn": "arn:aws:iam::123456789012:role/ExampleRole",
                "accountId": "123456789012",
                "userName": "ExampleRole"
            },
            "webIdFederationData": {},
            "attributes": {
                "creationDate": "2025-10-01T12:00:00Z",
                "mfaAuthenticated": "false"
            }
        }
    },
    "eventTime": "2025-10-01T12:30:00Z",
    "eventSource": "nova-act.amazonaws.com",
    "eventName": "CreateWorkflowDefinition",
    "awsRegion": "us-east-1",
    "sourceIPAddress": "192.0.2.1",
    "userAgent": "aws-sdk-python/1.0.0",
    "requestParameters": {
        "workflowName": "my-example-workflow"
    },
    "responseElements": {
        "workflowName": "my-example-workflow",
        "workflowDefinitionArn": "arn:aws:nova-act:us-east-1:123456789012:workflow-definition/my-example-workflow"
    },
    "requestID": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
    "eventID": "a1b2c3d4-5678-90ab-cdef-EXAMPLE22222",
    "readOnly": false,
    "eventType": "AwsApiCall",
    "managementEvent": true,
    "recipientAccountId": "123456789012",
    "eventCategory": "Management"
}
```

### Data event example
<a name="data-event-example"></a>

The following example shows a CloudTrail data event for the `InvokeActStep` operation. Data events are only logged when you have configured advanced event selectors to enable them.

```
{
    "eventVersion": "1.08",
    "userIdentity": {
        "type": "AssumedRole",
        "principalId": "AROA1EXAMPLE:user",
        "arn": "arn:aws:sts::123456789012:assumed-role/ExampleRole/user",
        "accountId": "123456789012",
        "accessKeyId": "AKIAIOSFODNN7EXAMPLE",
        "sessionContext": {
            "sessionIssuer": {
                "type": "Role",
                "principalId": "AROA1EXAMPLE",
                "arn": "arn:aws:iam::123456789012:role/ExampleRole",
                "accountId": "123456789012",
                "userName": "ExampleRole"
            },
            "webIdFederationData": {},
            "attributes": {
                "creationDate": "2025-10-01T12:00:00Z",
                "mfaAuthenticated": "false"
            }
        }
    },
    "eventTime": "2025-10-01T12:35:00Z",
    "eventSource": "nova-act.amazonaws.com",
    "eventName": "InvokeActStep",
    "awsRegion": "us-east-1",
    "sourceIPAddress": "192.0.2.1",
    "userAgent": "aws-sdk-python/1.0.0",
    "requestParameters": {
        "sessionId": "sess-1234567890abcdef0",
        "actId": "act-1234567890abcdef0"
    },
    "responseElements": null,
    "requestID": "a1b2c3d4-5678-90ab-cdef-EXAMPLE33333",
    "eventID": "a1b2c3d4-5678-90ab-cdef-EXAMPLE44444",
    "readOnly": false,
    "resources": [
        {
            "accountId": "123456789012",
            "type": "AWS::NovaAct::WorkflowDefinition",
            "ARN": "arn:aws:nova-act:us-east-1:123456789012:workflow-definition/my-example-workflow"
        }
    ],
    "eventType": "AwsApiCall",
    "managementEvent": false,
    "recipientAccountId": "123456789012",
    "eventCategory": "Data"
}
```

For information about CloudTrail record contents, see [CloudTrail record contents](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-event-reference-record-contents.html) in the * AWS CloudTrail User Guide*.