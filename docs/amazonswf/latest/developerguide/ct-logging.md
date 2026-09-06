

# Recording API calls with AWS CloudTrail
<a name="ct-logging"></a>

Amazon Simple Workflow Service is integrated with [AWS CloudTrail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-user-guide.html), a service that provides a record of actions taken by a user, role, or an AWS service. CloudTrail captures all API calls for Amazon SWF as events. The calls captured include calls from the Amazon SWF console and code calls to the Amazon SWF API operations. Using the information collected by CloudTrail, you can determine the request that was made to Amazon SWF, the IP address from which the request was made, when it was made, and additional details.

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

## Data events in CloudTrail
<a name="cloudtrail-data-events"></a>

[Data events](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/logging-data-events-with-cloudtrail.html#logging-data-events) provide information about the resource operations performed on or in a resource (for example, reading or writing to an Amazon S3 object). These are also known as data plane operations. Data events are often high-volume activities. By default, CloudTrail doesn’t log data events. The CloudTrail **Event history** doesn't record data events.

Additional charges apply for data events. For more information about CloudTrail pricing, see [AWS CloudTrail Pricing](https://aws.amazon.com/cloudtrail/pricing/).

You can log data events for the Amazon SWF resource types by using the CloudTrail console, AWS CLI, or CloudTrail API operations. For more information about how to log data events, see [Logging data events with the AWS Management Console](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/logging-data-events-with-cloudtrail.html#logging-data-events-console) and [Logging data events with the AWS Command Line Interface](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/logging-data-events-with-cloudtrail.html#creating-data-event-selectors-with-the-AWS-CLI) in the *AWS CloudTrail User Guide*.

The following table lists the Amazon SWF resource types for which you can log data events. The **Data event type** column shows the value to choose from the **Data event type** list on the CloudTrail console. The **resources.type value** column shows the `resources.type` value, which you would specify when configuring advanced event selectors using the AWS CLI or CloudTrail APIs. The **Data APIs logged to CloudTrail** column shows the API calls logged to CloudTrail for the resource type. 

You can configure advanced event selectors to filter on the `eventName`, `readOnly`, and `resources.ARN` fields to log only those events that are important to you. For more information about these fields, see [AdvancedFieldSelector](https://docs.aws.amazon.com/awscloudtrail/latest/APIReference/API_AdvancedFieldSelector.html) in the *AWS CloudTrail API Reference*.


| Data event type | resources.type value | Data APIs logged to CloudTrail | 
| --- | --- | --- | 
| SWF Domain |  AWS::SWF::Domain  | + [CountClosedWorkflowExecutions](https://docs.aws.amazon.com/amazonswf/latest/apireference/API_CountClosedWorkflowExecutions.html)<br />+ [CountOpenWorkflowExecutions](https://docs.aws.amazon.com/amazonswf/latest/apireference/API_CountOpenWorkflowExecutions.html)<br />+ [DescribeWorkflowExecution](https://docs.aws.amazon.com/amazonswf/latest/apireference/API_DescribeWorkflowExecution.html)<br />+ [ListClosedWorkflowExecutions](https://docs.aws.amazon.com/amazonswf/latest/apireference/API_ListClosedWorkflowExecutions.html)<br />+ [ListOpenWorkflowExecutions](https://docs.aws.amazon.com/amazonswf/latest/apireference/API_ListOpenWorkflowExecutions.html)<br />+ [GetWorkflowExecutionHistory](https://docs.aws.amazon.com/amazonswf/latest/apireference/API_GetWorkflowExecutionHistory.html)<br />+ [RequestCancelWorkflowExecution](https://docs.aws.amazon.com/amazonswf/latest/apireference/API_RequestCancelWorkflowExecution.html)<br />+ [SignalWorkflowExecution](https://docs.aws.amazon.com/amazonswf/latest/apireference/API_SignalWorkflowExecution.html)<br />+ [StartWorkflowExecution](https://docs.aws.amazon.com/amazonswf/latest/apireference/API_StartWorkflowExecution.html)<br />+ [TerminateWorkflowExecution](https://docs.aws.amazon.com/amazonswf/latest/apireference/API_TerminateWorkflowExecution.html)**Task Events**+ [CountPendingActivityTasks](https://docs.aws.amazon.com/amazonswf/latest/apireference/API_CountPendingActivityTasks.html)<br />+ [PollForDecisionTask](https://docs.aws.amazon.com/amazonswf/latest/apireference/API_PollForDecisionTask.html)<br />+ [PollForActivityTask](https://docs.aws.amazon.com/amazonswf/latest/apireference/API_PollForActivityTask.html)<br />+ [RecordActivityTaskHeartbeat](https://docs.aws.amazon.com/amazonswf/latest/apireference/API_RecordActivityTaskHeartbeat.html)<br />+ [RespondActivityTaskCanceled](https://docs.aws.amazon.com/amazonswf/latest/apireference/API_RespondActivityTaskCanceled.html)<br />+ [RespondActivityTaskCompleted](https://docs.aws.amazon.com/amazonswf/latest/apireference/API_RespondActivityTaskCompleted.html)<br />+ [RespondActivityTaskFailed](https://docs.aws.amazon.com/amazonswf/latest/apireference/API_RespondActivityTaskFailed.html)<br />+ [RespondDecisionTaskCompleted](https://docs.aws.amazon.com/amazonswf/latest/apireference/API_RespondDecisionTaskCompleted.html)Decision Events+ [CancelTimer](https://docs.aws.amazon.com/amazonswf/latest/apireference/API_Decision.html)<br />+ [CancelWorkflowExecution](https://docs.aws.amazon.com/amazonswf/latest/apireference/API_Decision.html)<br />+ [CompleteWorkflowExecution](https://docs.aws.amazon.com/amazonswf/latest/apireference/API_Decision.html)<br />+ [ContinueAsNewWorkflowExecution](https://docs.aws.amazon.com/amazonswf/latest/apireference/API_Decision.html)<br />+ [FailWorkflowExecution](https://docs.aws.amazon.com/amazonswf/latest/apireference/API_Decision.html)<br />+ [RecordMarker](https://docs.aws.amazon.com/amazonswf/latest/apireference/API_Decision.html)<br />+ [RequestCancelActivityTask](https://docs.aws.amazon.com/amazonswf/latest/apireference/API_Decision.html)<br />+ [RequestCancelExternalWorkflowExecution](https://docs.aws.amazon.com/amazonswf/latest/apireference/API_Decision.html)<br />+ [ScheduleActivityTask](https://docs.aws.amazon.com/amazonswf/latest/apireference/API_Decision.html)<br />+ [ScheduleLambdaFunction](https://docs.aws.amazon.com/amazonswf/latest/apireference/API_Decision.html)<br />+ [SignalExternalWorkflowExecution](https://docs.aws.amazon.com/amazonswf/latest/apireference/API_Decision.html)<br />+ [StartChildWorkflowExecution](https://docs.aws.amazon.com/amazonswf/latest/apireference/API_Decision.html)<br />+ [StartTimer](https://docs.aws.amazon.com/amazonswf/latest/apireference/API_Decision.html) | 

**CloudTrail events and RespondDecisionTaskCompleted**  
The [RespondDecisionTaskCompleted](https://docs.aws.amazon.com/amazonswf/latest/apireference/API_RespondDecisionTaskCompleted.html) action takes a list of decisions in the request payload. A completed call will emit N\+1 CloudTrail data events, one for each decision plus one for the API call itself. The data events and API event will all have the same request id.

## Management events in CloudTrail
<a name="cloudtrail-management-events"></a>

[Management events](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/logging-management-events-with-cloudtrail.html#logging-management-events) provide information about management operations that are performed on resources in your AWS account. These are also known as control plane operations. By default, CloudTrail logs management events.

Amazon Simple Workflow Service logs the following control plane operations to CloudTrail as *management events*.

**Domain Events**
+ [RegisterDomain](https://docs.aws.amazon.com/amazonswf/latest/apireference/API_RegisterDomain.html)
+ [DescribeDomain](https://docs.aws.amazon.com/amazonswf/latest/apireference/API_DescribeDomain.html)
+ [ListDomains](https://docs.aws.amazon.com/amazonswf/latest/apireference/API_ListDomains.html)
+ [DeprecateDomain](https://docs.aws.amazon.com/amazonswf/latest/apireference/API_DeprecateDomain.html)
+ [UndeprecateDomain](https://docs.aws.amazon.com/amazonswf/latest/apireference/API_UndeprecateDomain.html)

**Activity Events**
+ [RegisterActivityType](https://docs.aws.amazon.com/amazonswf/latest/apireference/API_RegisterActivityType.html)
+ [DescribeActivityType](https://docs.aws.amazon.com/amazonswf/latest/apireference/API_DescribeActivityType.html)
+ [ListActivityTypes](https://docs.aws.amazon.com/amazonswf/latest/apireference/API_ListActivityTypes.html)
+ [DeprecateActivityType](https://docs.aws.amazon.com/amazonswf/latest/apireference/API_DeprecateActivityType.html)
+ [UndeprecateActivityType](https://docs.aws.amazon.com/amazonswf/latest/apireference/API_UndeprecateActivityType.html)
+ [DeleteActivityType](https://docs.aws.amazon.com/amazonswf/latest/apireference/API_DeleteActivityType.html)

**WorkflowType Events**
+ [RegisterWorkflowType](https://docs.aws.amazon.com/amazonswf/latest/apireference/API_RegisterWorkflowType.html)
+ [DescribeWorkflowType](https://docs.aws.amazon.com/amazonswf/latest/apireference/API_DescribeWorkflowType.html)
+ [ListWorkflowTypes](https://docs.aws.amazon.com/amazonswf/latest/apireference/API_ListWorkflowTypes.html)
+ [DeprecateWorkflowType](https://docs.aws.amazon.com/amazonswf/latest/apireference/API_DeprecateWorkflowType.html)
+ [UndeprecateWorkflowType](https://docs.aws.amazon.com/amazonswf/latest/apireference/API_UndeprecateWorkflowType.html)
+ [DeleteWorkflowType](https://docs.aws.amazon.com/amazonswf/latest/apireference/API_DeleteWorkflowType.html)

**Tag Events**
+ [TagResource](https://docs.aws.amazon.com/amazonswf/latest/apireference/API_TagResource.html)
+ [UntagResource](https://docs.aws.amazon.com/amazonswf/latest/apireference/API_UntagResource.html)
+ [ListTagsforResource](https://docs.aws.amazon.com/amazonswf/latest/apireference/API_ListTagsforResource.html)

## Example event
<a name="cloudtrail-event-examples"></a>

An event represents a single request from any source and includes information about the requested API operation, the date and time of the operation, request parameters, and so on. CloudTrail log files aren't an ordered stack trace of the public API calls, so events don't appear in any specific order.

The following example shows a CloudTrail event that demonstrates the `CountClosedWorkflowExecutions` operation.

```
{
    "eventVersion": "1.09",
    "userIdentity": {
      "type": "AssumedRole",
      "principalId": "1234567890abcdef02345:admin",
      "arn": "arn:aws:sts::111122223333:assumed-role/Admin/admin",
      "accountId": "111122223333",
      "accessKeyId": "abcdef01234567890abc",
      "sessionContext": {
        "sessionIssuer": {
          "type": "Role",
          "principalId": "1234567890abcdef02345",
          "arn": "arn:aws:iam::111122223333:role/Admin",
          "accountId": "111122223333",
          "userName": "Admin"
        },
        "attributes": {
          "creationDate": "2023-11-23T16:37:38Z",
          "mfaAuthenticated": "false"
        }
      }
    },
    "eventTime": "2023-11-23T17:52:46Z",
    "eventSource": "swf.amazonaws.com",
    "eventName": "CountClosedWorkflowExecutions",
    "awsRegion": "us-east-1",
    "sourceIPAddress": "198.51.100.42",
    "userAgent": "aws-internal/3 aws-sdk-java/1.11.42",
    "requestParameters": {
      "domain": "nsg-domain",
      "closeTimeFilter": {
        "oldestDate": "Nov 23, 2023 5:52:46 PM",
        "latestDate": "Nov 23, 2023 5:52:46 PM"
      }
    },
    "responseElements": null,
    "requestID": "a1b2c3d4-5678-90ab-cdef-EXAMPLEaaaaa",
    "eventID": "a1b2c3d4-5678-90ab-cdef-EXAMPLEbbbbb",
    "readOnly": true,
    "resources": [
      {
        "accountId": "111122223333",
        "type": "AWS::SWF::Domain",
        "ARN": "arn:aws:swf:us-east-1:111122223333:/domain/nsg-domain"
      }
    ],
    "eventType": "AwsApiCall",
    "managementEvent": false,
    "recipientAccountId": "111122223333",
    "eventCategory": "Data",
    "tlsDetails": {
      "clientProvidedHostHeader": "swf.example.amazondomains.com"
    }
  }
```

For information about CloudTrail record contents, see [CloudTrail record contents](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-event-reference-record-contents.html) in the *AWS CloudTrail User Guide*.