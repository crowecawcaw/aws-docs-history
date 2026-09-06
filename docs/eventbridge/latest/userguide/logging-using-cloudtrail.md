

# Logging Amazon EventBridge API calls using AWS CloudTrail
<a name="logging-using-cloudtrail"></a>

Amazon EventBridge is integrated with [AWS CloudTrail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-user-guide.html), a service that provides a record of actions taken by a user, role, or an AWS service. CloudTrail captures all API calls for EventBridge as events. The calls captured include calls from the EventBridge console and code calls to the EventBridge API operations. Using the information collected by CloudTrail, you can determine the request that was made to EventBridge, the IP address from which the request was made, when it was made, and additional details.

Every event or log entry contains information about who generated the request. The identity information helps you determine the following:
+ Whether the request was made with root user or user credentials.
+ Whether the request was made on behalf of an IAM Identity Center user.
+ Whether the request was made with temporary security credentials for a role or federated user.
+ Whether the request was made by another AWS service.

CloudTrail is active in your AWS account when you create the account and you automatically have access to the CloudTrail **Event history**. The CloudTrail **Event history** provides a viewable, searchable, downloadable, and immutable record of the past 90 days of recorded management events in an AWS Region. For more information, see [Working with CloudTrail Event history](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/view-cloudtrail-events.html) in the *AWS CloudTrail User Guide*. There are no CloudTrail charges for viewing the **Event history**.

For an ongoing record of events in your AWS account past 90 days, create a trail or a [CloudTrail Lake](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-lake.html) event data store.

**CloudTrail trails**  
A *trail* enables CloudTrail to deliver log files to an Amazon S3 bucket. All trails created using the AWS Management Console are multi-Region. You can create a single-Region or a multi-Region trail by using the AWS CLI. Creating a multi-Region trail is recommended because you capture activity in all AWS Regions in your account. If you create a single-Region trail, you can view only the events logged in the trail's AWS Region. For more information about trails, see [Creating a trail for your AWS account](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-create-and-update-a-trail.html) and [Creating a trail for an organization](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/creating-trail-organization.html) in the *AWS CloudTrail User Guide*.  
You can deliver one copy of your ongoing management events to your Amazon S3 bucket at no charge from CloudTrail by creating a trail, however, there are Amazon S3 storage charges. For more information about CloudTrail pricing, see [AWS CloudTrail Pricing](https://aws.amazon.com/cloudtrail/pricing/). For information about Amazon S3 pricing, see [Amazon S3 Pricing](https://aws.amazon.com/s3/pricing/).

**CloudTrail Lake event data stores**  
*CloudTrail Lake* lets you run SQL-based queries on your events. CloudTrail Lake converts existing events in row-based JSON format to [ Apache ORC](https://orc.apache.org/) format. ORC is a columnar storage format that is optimized for fast retrieval of data. Events are aggregated into *event data stores*, which are immutable collections of events based on criteria that you select by applying [advanced event selectors](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-lake-concepts.html#adv-event-selectors). The selectors that you apply to an event data store control which events persist and are available for you to query. For more information about CloudTrail Lake, see [Working with AWS CloudTrail Lake](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-lake.html) in the *AWS CloudTrail User Guide*.  
CloudTrail Lake event data stores and queries incur costs. When you create an event data store, you choose the [pricing option](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-lake-manage-costs.html#cloudtrail-lake-manage-costs-pricing-option) you want to use for the event data store. The pricing option determines the cost for ingesting and storing events, and the default and maximum retention period for the event data store. For more information about CloudTrail pricing, see [AWS CloudTrail Pricing](https://aws.amazon.com/cloudtrail/pricing/).

## EventBridge management events in CloudTrail
<a name="cloudtrail-management-events"></a>

[Management events](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/logging-management-events-with-cloudtrail.html#logging-management-events) provide information about management operations that are performed on resources in your AWS account. These are also known as control plane operations. By default, CloudTrail logs management events.

All Amazon EventBridge API operations except [PutEvents](https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_PutEvents.html) and [PutPartnerEvents](https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_PutPartnerEvents.html) are control plane operations. For a complete list, see [Actions](https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_Operations.html) in the *Amazon EventBridge API Reference*. For example management events, see [EventBridge management event examples](#cloudtrail-event-examples).

## EventBridge data events in CloudTrail
<a name="cloudtrail-data-events"></a>

[Data events](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/logging-data-events-with-cloudtrail.html#logging-data-events) provide information about the resource operations performed on or in a resource (for example, publishing events to an event bus). These are also known as data plane operations. Data events are often high-volume activities. By default, CloudTrail doesn't log data events. The CloudTrail **Event history** doesn't record data events.

Additional charges apply for data events. For more information about CloudTrail pricing, see [AWS CloudTrail Pricing](https://aws.amazon.com/cloudtrail/pricing/).

You can log data events for the EventBridge resource types by using the CloudTrail console, AWS CLI, or CloudTrail API operations. For more information about how to log data events, see [Logging data events with the AWS Management Console](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/logging-data-events-with-cloudtrail.html#logging-data-events-console) and [Logging data events with the AWS Command Line Interface](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/logging-data-events-with-cloudtrail.html#creating-data-event-selectors-with-the-AWS-CLI) in the *AWS CloudTrail User Guide*.

The following table lists the EventBridge resource types for which you can log data events. The **Resource type (console)** column shows the value to choose from the **Resource type** list on the CloudTrail console. The **resources.type value** column shows the `resources.type` value, which you would specify when configuring advanced event selectors using the AWS CLI or CloudTrail APIs. The **Data APIs logged to CloudTrail** column shows the API calls logged to CloudTrail for the resource type.


| Resource type (console) | resources.type value | Data APIs logged to CloudTrail | 
| --- | --- | --- | 
| EventBridge event bus |  AWS::Events::EventBus  |  +  [PutEvents](https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_PutEvents.html)   | 
| EventBridge partner event source |  AWS::Events::EventSource  |  +  [PutPartnerEvents](https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_PutPartnerEvents.html)   | 
| EventBridge endpoint |  AWS::Events::Endpoint  |  +  [PutEvents](https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_PutEvents.html) (when using a [global endpoint](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-global-endpoints.html); successful calls only, not populated on `AccessDenied`)   | 

You can configure advanced event selectors to filter on the `eventName`, `readOnly`, and `resources.ARN` fields to log only those events that are important to you. For more information about these fields, see [AdvancedFieldSelector](https://docs.aws.amazon.com/awscloudtrail/latest/APIReference/API_AdvancedFieldSelector.html) in the *AWS CloudTrail API Reference*.

**Note**  
The `detail` field in event entries is redacted in CloudTrail data event logs to protect sensitive data.

### Data event delivery
<a name="cloudtrail-data-event-delivery"></a>

**Note**  
CloudTrail sends data events only to the AWS account that called the API.

#### `PutEvents`
<a name="cloudtrail-data-event-putevents"></a>

##### Cross-account `PutEvents` calls
<a name="cloudtrail-data-event-putevents-cross-account"></a>

When an account that you granted permission to via a resource policy calls `PutEvents` to your bus, only the caller's account receives the CloudTrail data event. Your account (the bus owner) does not.

##### Bus-to-bus forwarding
<a name="cloudtrail-data-event-putevents-bus-to-bus"></a>

Up to four accounts can be involved in a bus-to-bus forwarding scenario. The following table shows which accounts receive a CloudTrail data event.


| Account role | Receives CloudTrail data event | 
| --- | --- | 
| The account that originally called PutEvents (the sender) | Yes, always. | 
| The account that owns the source bus (the source bus owner) | No. | 
| The account that owns the rule and the IAM role on the rule target (the rule owner) | Yes, but only for cross-Region forwarding. For cross-Region forwarding, EventBridge uses the IAM role on the rule target to call `PutEvents` on the destination Region. This makes the rule owner's account the effective API caller. Same-Region forwarding does not generate an additional data event. | 
| The account that owns the destination bus (the destination bus owner) | No. | 

**Note**  
For cross-Region forwarding, the original `PutEvents` call and the forwarding `PutEvents` call are recorded as separate CloudTrail data events in their respective Regions. To capture both, ensure that CloudTrail is configured to log data events in both Regions.

##### Global endpoints with event replication
<a name="cloudtrail-data-event-putevents-global-endpoint"></a>

When you use a global endpoint with event replication enabled, EventBridge creates a managed rule that forwards events cross-Region to the secondary bus. This is a cross-Region bus-to-bus forwarding scenario, so the same rules from the table above apply:
+ Primary Region: EventBridge generates a data event for the original `PutEvents` call. The event includes both the event bus ARN and the endpoint resource ARN.
+ Secondary Region: Because you own the managed rule and the IAM role used to replicate events, your account receives a data event for the replication `PutEvents` call. The event includes only the event bus ARN. The endpoint resource ARN is not included.

#### `PutPartnerEvents`
<a name="cloudtrail-data-event-putpartnerevents"></a>

##### Events received from a SaaS partner
<a name="cloudtrail-data-event-putpartnerevents-customer"></a>

When a SaaS partner sends events to your bus, your account does not receive a `PutPartnerEvents` CloudTrail data event. Only the SaaS partner's account receives the data event.

##### Events sent to a customer bus as a SaaS partner
<a name="cloudtrail-data-event-putpartnerevents-partner"></a>

When you send events to a customer's event bus as a SaaS partner, your account receives the `PutPartnerEvents` CloudTrail data event. The event includes only the event source ARN as a resource. The customer's event bus ARN is not included.

For examples of data events that EventBridge logs to CloudTrail, see [EventBridge data event examples](#cloudtrail-data-event-examples).

## EventBridge management event examples
<a name="cloudtrail-event-examples"></a>

An event represents a single request from any source and includes information about the requested API operation, the date and time of the operation, request parameters, and so on. CloudTrail log files aren't an ordered stack trace of the public API calls, so events don't appear in any specific order.

The following example shows a CloudTrail event that demonstrates the `PutRule` operation.

```
{
  "eventVersion":"1.03",
  "userIdentity":{
    "type":"Root",
    "principalId":"123456789012",
    "arn":"arn:aws:iam::123456789012:root",
    "accountId":"123456789012",
    "accessKeyId":"AKIAIOSFODNN7EXAMPLE",
    "sessionContext":{
      "attributes":{
      "mfaAuthenticated":"false",
      "creationDate":"2015-11-17T23:56:15Z"
      }
    }
  },
  "eventTime":"2015-11-18T00:11:28Z",
  "eventSource":"events.amazonaws.com",
  "eventName":"PutRule",
  "awsRegion":"us-east-1",
  "sourceIPAddress":"AWS Internal",
  "userAgent":"AWS CloudWatch Console",
  "requestParameters":{
    "description":"",
    "name":"cttest2",
    "state":"ENABLED",
    "eventPattern":"{\"source\":[\"aws.ec2\"],\"detail-type\":[\"EC2 Instance State-change Notification\"]}",
    "scheduleExpression":""
  },
  "responseElements":{
    "ruleArn":"arn:aws:events:us-east-1:123456789012:rule/cttest2"
  },
  "requestID":"e9caf887-8d88-11e5-a331-3332aa445952",
  "eventID":"49d14f36-6450-44a5-a501-b0fdcdfaeb98",
  "eventType":"AwsApiCall",
  "apiVersion":"2015-10-07",
  "recipientAccountId":"123456789012"
}
```

For information about CloudTrail record contents, see [CloudTrail record contents](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-event-reference-record-contents.html) in the *AWS CloudTrail User Guide*.

## EventBridge data event examples
<a name="cloudtrail-data-event-examples"></a>

The following example shows a CloudTrail data event for a successful `PutEvents` call.

```
{
  "eventVersion": "1.11",
  "userIdentity": {
    "type": "AssumedRole",
    "principalId": "AROA3XFRBF23EXAMPLE:johndoe-session",
    "arn": "arn:aws:sts::111122223333:assumed-role/MyRole/johndoe-session",
    "accountId": "111122223333",
    "accessKeyId": "AKIAIOSFODNN7EXAMPLE",
    "sessionContext": {
      "sessionIssuer": {
        "type": "Role",
        "principalId": "AROA3XFRBF23EXAMPLE",
        "arn": "arn:aws:iam::111122223333:role/MyRole",
        "accountId": "111122223333",
        "userName": "MyRole"
      },
      "attributes": {
        "creationDate": "2026-03-07T00:49:09Z",
        "mfaAuthenticated": "false"
      }
    }
  },
  "eventTime": "2026-03-07T00:51:07Z",
  "eventSource": "events.amazonaws.com",
  "eventName": "PutEvents",
  "awsRegion": "us-east-1",
  "sourceIPAddress": "192.0.2.1",
  "userAgent": "aws-cli/2.33.13",
  "requestParameters": {
    "entries": [
      {
        "source": "my-application",
        "detailType": "MyDetailType",
        "detail": "HIDDEN_DUE_TO_SECURITY_REASONS",
        "eventBusName": "default"
      }
    ]
  },
  "responseElements": {
    "failedEntryCount": 0,
    "entries": [
      {
        "eventId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111"
      }
    ]
  },
  "requestID": "a1b2c3d4-5678-90ab-cdef-EXAMPLE22222",
  "eventID": "a1b2c3d4-5678-90ab-cdef-EXAMPLE33333",
  "readOnly": false,
  "resources": [
    {
      "type": "AWS::Events::EventBus",
      "ARN": "arn:aws:events:us-east-1:111122223333:event-bus/default"
    }
  ],
  "eventType": "AwsApiCall",
  "apiVersion": "2015-10-07",
  "managementEvent": false,
  "recipientAccountId": "111122223333",
  "eventCategory": "Data",
  "tlsDetails": {
    "tlsVersion": "TLSv1.3",
    "cipherSuite": "TLS_AES_128_GCM_SHA256",
    "clientProvidedHostHeader": "events.us-east-1.amazonaws.com"
  }
}
```

The following example shows a CloudTrail data event for a `PutEvents` call using a [global endpoint](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-global-endpoints.html). Note the additional `AWS::Events::Endpoint` resource in the `resources` array.

```
{
  "eventVersion": "1.11",
  "userIdentity": {
    "type": "AssumedRole",
    "principalId": "AROA3XFRBF23EXAMPLE:johndoe-session",
    "arn": "arn:aws:sts::111122223333:assumed-role/MyRole/johndoe-session",
    "accountId": "111122223333",
    "accessKeyId": "AKIAIOSFODNN7EXAMPLE",
    "sessionContext": {
      "sessionIssuer": {
        "type": "Role",
        "principalId": "AROA3XFRBF23EXAMPLE",
        "arn": "arn:aws:iam::111122223333:role/MyRole",
        "accountId": "111122223333",
        "userName": "MyRole"
      },
      "attributes": {
        "creationDate": "2026-03-07T00:49:09Z",
        "mfaAuthenticated": "false"
      }
    }
  },
  "eventTime": "2026-03-07T00:51:06Z",
  "eventSource": "events.amazonaws.com",
  "eventName": "PutEvents",
  "awsRegion": "us-east-1",
  "sourceIPAddress": "192.0.2.1",
  "userAgent": "aws-cli/2.33.13",
  "requestParameters": {
    "entries": [
      {
        "source": "my-application",
        "detailType": "MyDetailType",
        "detail": "HIDDEN_DUE_TO_SECURITY_REASONS",
        "eventBusName": "default"
      }
    ],
    "endpointId": "abc1234567.us-east-1"
  },
  "responseElements": {
    "failedEntryCount": 0,
    "entries": [
      {
        "eventId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE44444"
      }
    ]
  },
  "requestID": "a1b2c3d4-5678-90ab-cdef-EXAMPLE55555",
  "eventID": "a1b2c3d4-5678-90ab-cdef-EXAMPLE66666",
  "readOnly": false,
  "resources": [
    {
      "type": "AWS::Events::EventBus",
      "ARN": "arn:aws:events:us-east-1:111122223333:event-bus/default"
    },
    {
      "type": "AWS::Events::Endpoint",
      "ARN": "arn:aws:events:us-east-1:111122223333:endpoint/MyGlobalEndpoint"
    }
  ],
  "eventType": "AwsApiCall",
  "apiVersion": "2015-10-07",
  "managementEvent": false,
  "recipientAccountId": "111122223333",
  "eventCategory": "Data",
  "tlsDetails": {
    "tlsVersion": "TLSv1.3",
    "cipherSuite": "TLS_AES_128_GCM_SHA256",
    "clientProvidedHostHeader": "abc1234567.us-east-1.endpoint.events.amazonaws.com"
  }
}
```

The following example shows a CloudTrail data event for a successful `PutPartnerEvents` call.

```
{
  "eventVersion": "1.11",
  "userIdentity": {
    "type": "AssumedRole",
    "principalId": "AROA3XFRBF23EXAMPLE:partner-session",
    "arn": "arn:aws:sts::111122223333:assumed-role/PartnerRole/partner-session",
    "accountId": "111122223333",
    "accessKeyId": "AKIAIOSFODNN7EXAMPLE",
    "sessionContext": {
      "sessionIssuer": {
        "type": "Role",
        "principalId": "AROA3XFRBF23EXAMPLE",
        "arn": "arn:aws:iam::111122223333:role/PartnerRole",
        "accountId": "111122223333",
        "userName": "PartnerRole"
      },
      "attributes": {
        "creationDate": "2026-03-07T00:49:09Z",
        "mfaAuthenticated": "false"
      }
    }
  },
  "eventTime": "2026-03-07T00:51:07Z",
  "eventSource": "events.amazonaws.com",
  "eventName": "PutPartnerEvents",
  "awsRegion": "us-east-1",
  "sourceIPAddress": "192.0.2.1",
  "userAgent": "aws-cli/2.33.13",
  "requestParameters": {
    "entries": [
      {
        "time": "Mar 7, 2026, 12:51:07 AM",
        "source": "aws.partner/example.com/my-integration",
        "detailType": "MyDetailType",
        "detail": "HIDDEN_DUE_TO_SECURITY_REASONS"
      }
    ]
  },
  "responseElements": {
    "failedEntryCount": 0,
    "entries": [
      {
        "eventId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE77777"
      }
    ]
  },
  "requestID": "a1b2c3d4-5678-90ab-cdef-EXAMPLE88888",
  "eventID": "a1b2c3d4-5678-90ab-cdef-EXAMPLE99999",
  "readOnly": false,
  "resources": [
    {
      "type": "AWS::Events::EventSource",
      "ARN": "arn:aws:events:us-east-1::event-source/aws.partner/example.com/my-integration"
    }
  ],
  "eventType": "AwsApiCall",
  "apiVersion": "2015-10-07",
  "managementEvent": false,
  "recipientAccountId": "111122223333",
  "eventCategory": "Data",
  "tlsDetails": {
    "tlsVersion": "TLSv1.3",
    "cipherSuite": "TLS_AES_128_GCM_SHA256",
    "clientProvidedHostHeader": "events.us-east-1.amazonaws.com"
  }
}
```

## CloudTrail log entries for actions taken by EventBridge Pipes
<a name="cloudtrail-event-pipe-examples"></a>

EventBridge Pipes assumes the provided IAM role when reading events from sources, invoking enrichments, or invoking targets. For CloudTrail entries related to actions taken in your account on all enrichments, targets, and Amazon SQS, Kinesis, and DynamoDB sources, the `sourceIPAddress` and `invokedBy` fields will include `pipes.amazonaws.com`.

**Sample CloudTrail log entry for all enrichments, targets, and Amazon SQS, Kinesis, and DynamoDB sources**

```
{
  "eventVersion": "1.08",
  "userIdentity": {
    "type": "AssumedRole",
    "principalId": "...",
    "arn": "arn:aws:sts::111222333444:assumed-role/...",
    "accountId": "111222333444",
    "accessKeyId": "...",
    "sessionContext": {
      "sessionIssuer": {
        "type": "Role",
        "principalId": "...",
        "arn": "...",
        "accountId": "111222333444",
        "userName": "userName"
      },
      "webIdFederationData": {},
      "attributes": {
        "creationDate": "2022-09-22T21:41:15Z",
        "mfaAuthenticated": "false"
      }
    },
    "invokedBy": "pipes.amazonaws.com"
  },
  "eventTime": ",,,",
  "eventName": "...",
  "awsRegion": "us-west-2",
  "sourceIPAddress": "pipes.amazonaws.com",
  "userAgent": "pipes.amazonaws.com",
  "requestParameters": {
    ...
  },
  "responseElements": null,
  "requestID": "...",
  "eventID": "...",
  "readOnly": true,
  "eventType": "AwsApiCall",
  "managementEvent": true,
  "recipientAccountId": "...",
  "eventCategory": "Management"
}
```

For all other sources, the `sourceIPAddress` field of the CloudTrail log entries will have a dynamic IP address and shouldn't be relied upon for any integration or event categorization. In addition, these entries won't have the `invokedBy` field.

**Sample CloudTrail log entry for all other sources**

```
{
  "eventVersion": "1.08",
  "userIdentity": {
    ...
  },
  "eventTime": ",,,",
  "eventName": "...",
  "awsRegion": "us-west-2",
  "sourceIPAddress": "127.0.0.1",
  "userAgent": "Python-httplib2/0.8 (gzip)",
}
```