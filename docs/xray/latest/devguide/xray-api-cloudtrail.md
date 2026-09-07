

# Logging X-Ray API calls with AWS CloudTrail
<a name="xray-api-cloudtrail"></a>

AWS X-Ray is integrated with [AWS CloudTrail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-user-guide.html), a service that provides a record of actions taken by a user, role, or an AWS service. CloudTrail captures all API calls for X-Ray as events. The calls captured include calls from the X-Ray console and code calls to the X-Ray API operations. Using the information collected by CloudTrail, you can determine the request that was made to X-Ray, the IP address from which the request was made, when it was made, and additional details.

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

**Topics**
+ [X-Ray management events in CloudTrail](#xray-api-cloudtrail-mgmt)
+ [X-Ray data events in CloudTrail](#cloudtrail-data-events)
+ [X-Ray event examples](#xray-cloudtrail-examples)

## X-Ray management events in CloudTrail
<a name="xray-api-cloudtrail-mgmt"></a>

AWS X-Ray integrates with AWS CloudTrail to record API actions made by a user, a role, or an AWS service in X-Ray. You can use CloudTrail to monitor X-Ray API requests in real time and store logs in Amazon S3, Amazon CloudWatch Logs, and Amazon CloudWatch Events. X-Ray supports logging the following actions as events in CloudTrail log files:

**Supported API Actions**
+ [PutEncryptionConfig](https://docs.aws.amazon.com/xray/latest/api/API_PutEncryptionConfig.html)
+ [GetEncryptionConfig](https://docs.aws.amazon.com/xray/latest/api/API_GetEncryptionConfig.html)
+ [CreateGroup](https://docs.aws.amazon.com/xray/latest/api/API_CreateGroup.html)
+ [UpdateGroup](https://docs.aws.amazon.com/xray/latest/api/API_UpdateGroup.html)
+ [DeleteGroup](https://docs.aws.amazon.com/xray/latest/api/API_DeleteGroup.html)
+ [GetGroup](https://docs.aws.amazon.com/xray/latest/api/API_GetGroup.html)
+ [GetGroups](https://docs.aws.amazon.com/xray/latest/api/API_GetGroups.html)
+ [GetInsight](https://docs.aws.amazon.com/xray/latest/api/API_GetInsight.html)
+ [GetInsightEvents](https://docs.aws.amazon.com/xray/latest/api/API_GetInsightEvents.html)
+ [GetInsightImpactGraph](https://docs.aws.amazon.com/xray/latest/api/API_GetInsightImpactGraph.html)
+ [GetInsightSummaries](https://docs.aws.amazon.com/xray/latest/api/API_GetInsightSummaries.html)
+ [GetSamplingStatisticSummaries](https://docs.aws.amazon.com/xray/latest/api/API_GetSamplingStatisticSummaries.html)

## X-Ray data events in CloudTrail
<a name="cloudtrail-data-events"></a>

[Data events](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/logging-data-events-with-cloudtrail.html#logging-data-events) provide information about the resource operations performed on or in a resource (for example, [PutTraceSegments](https://docs.aws.amazon.com/xray/latest/api/API_PutTraceSegments.html), which uploads segment documents to X-Ray).

These are also known as data plane operations. Data events are often high-volume activities. By default, CloudTrail doesn’t log data events. The CloudTrail **Event history** doesn't record data events.

Additional charges apply for data events. For more information about CloudTrail pricing, see [AWS CloudTrail Pricing](https://aws.amazon.com/cloudtrail/pricing/).

You can log data events for the X-Ray resource types by using the CloudTrail console, AWS CLI, or CloudTrail API operations. For more information about how to log data events, see [Logging data events with the AWS Management Console](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/logging-data-events-with-cloudtrail.html#logging-data-events-console) and [Logging data events with the AWS Command Line Interface](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/logging-data-events-with-cloudtrail.html#creating-data-event-selectors-with-the-AWS-CLI) in the *AWS CloudTrail User Guide*.

The following table lists the X-Ray resource types for which you can log data events. The **Data event type (console)** column shows the value to choose from the **Data event type** list on the CloudTrail console. The **resources.type value** column shows the `resources.type` value, which you would specify when configuring advanced event selectors using the AWS CLI or CloudTrail APIs. The **Data APIs logged to CloudTrail** column shows the API calls logged to CloudTrail for the resource type. 


| Data event type (console) | resources.type value | Data APIs logged to CloudTrail | 
| --- | --- | --- | 
| X-Ray trace |  AWS::XRay::Trace  |  +  [PutTraceSegments](https://docs.aws.amazon.com/xray/latest/api/API_PutTraceSegments.html) <br />+  [GetTraceSummaries](https://docs.aws.amazon.com/xray/latest/api/API_GetTraceSummaries.html) <br />+  [GetTraceGraph](https://docs.aws.amazon.com/xray/latest/api/API_GetTraceGraph.html) <br />+  [GetServiceGraph](https://docs.aws.amazon.com/xray/latest/api/API_GetServiceGraphs.html) <br />+  [BatchGetTraces](https://docs.aws.amazon.com/xray/latest/api/API_BatchGetTraces.html) <br />+  [GetTimeSeriesServiceStatistics](https://docs.aws.amazon.com/xray/latest/api/API_GetTimeSeriesServiceStatistics.html) <br />+  [PutTelemetryRecords](https://docs.aws.amazon.com/xray/latest/api/API_PutTelemetryRecords.html) <br />+  [GetSamplingTargets](https://docs.aws.amazon.com/xray/latest/api/API_GetSamplingTargets.html)   | 

You can configure advanced event selectors to filter on the `eventName` and `readOnly` fields to log only those events that are important to you. However, you cannot select events by adding the `resources.ARN` field selector, because X-Ray traces do not have ARNs. For more information about these fields, see [AdvancedFieldSelector](https://docs.aws.amazon.com/awscloudtrail/latest/APIReference/API_AdvancedFieldSelector.html) in the *AWS CloudTrail API Reference*. The following is an example of how to run the [`put-event-selectors`](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudtrail/put-event-selectors.html) AWS CLI command to log data events on a CloudTrail trail. You must run the command in or specify the Region in which the trail was created; otherwise, the operation returns an `InvalidHomeRegionException` exception.

```
aws cloudtrail put-event-selectors --trail-name myTrail --advanced-event-selectors \
'{
   "AdvancedEventSelectors": [ 
      {
         "FieldSelectors": [
            { "Field": "eventCategory", "Equals": ["Data"] },
            { "Field": "resources.type", "Equals": ["AWS::XRay::Trace"] },
            { "Field": "eventName", "Equals": ["PutTraceSegments","GetSamplingTargets"] }
         ],
         "Name": "Log X-Ray PutTraceSegments and GetSamplingTargets data events"
      }
   ]
}'
```

## X-Ray event examples
<a name="xray-cloudtrail-examples"></a>

### Management event example, `GetEncryptionConfig`
<a name="xray-example-management"></a>

The following is an example of the X-Ray GetEncryptionConfig log entry in CloudTrail.

**Example**  

```
{
    "eventVersion"=>"1.05",
    "userIdentity"=>{
        "type"=>"AssumedRole",
        "principalId"=>"AROAJVHBZWD3DN6CI2MHM:MyName",
        "arn"=>"arn:aws:sts::123456789012:assumed-role/MyRole/MyName",
        "accountId"=>"123456789012",
        "accessKeyId"=>"AKIAIOSFODNN7EXAMPLE",
        "sessionContext"=>{
            "attributes"=>{
                "mfaAuthenticated"=>"false",
                "creationDate"=>"2023-7-01T00:24:36Z"
            },
            "sessionIssuer"=>{
                "type"=>"Role",
                "principalId"=>"AROAJVHBZWD3DN6CI2MHM",
                "arn"=>"arn:aws:iam::123456789012:role/MyRole",
                "accountId"=>"123456789012",
                "userName"=>"MyRole"
            }
        }
    },
    "eventTime"=>"2023-7-01T00:24:36Z",
    "eventSource"=>"xray.amazonaws.com",
    "eventName"=>"GetEncryptionConfig",
    "awsRegion"=>"us-east-2",
    "sourceIPAddress"=>"33.255.33.255",
    "userAgent"=>"aws-sdk-ruby2/2.11.19 ruby/2.3.1 x86_64-linux",
    "requestParameters"=>nil,
    "responseElements"=>nil,
    "requestID"=>"3fda699a-32e7-4c20-37af-edc2be5acbdb",
    "eventID"=>"039c3d45-6baa-11e3-2f3e-e5a036343c9f",
    "eventType"=>"AwsApiCall",
    "recipientAccountId"=>"123456789012"
}
```

### Data event example, `PutTraceSegments`
<a name="xray-example-data"></a>

The following is an example of the X-Ray PutTraceSegments data event log entry in CloudTrail.

**Example**  

```
{
  "eventVersion": "1.09",
  "userIdentity": {
    "type": "AssumedRole",
    "principalId": "AROAWYXPW54Y4NEXAMPLE:i-0dzz2ac111c83zz0z",
    "arn": "arn:aws:sts::012345678910:assumed-role/my-service-role/i-0dzz2ac111c83zz0z",
    "accountId": "012345678910",
    "accessKeyId": "AKIAIOSFODNN7EXAMPLE",
    "sessionContext": {
      "sessionIssuer": {
        "type": "Role",
        "principalId": "AROAWYXPW54Y4NEXAMPLE",
        "arn": "arn:aws:iam::012345678910:role/service-role/my-service-role",
        "accountId": "012345678910",
        "userName": "my-service-role"
      },
      "attributes": {
        "creationDate": "2024-01-22T17:34:11Z",
        "mfaAuthenticated": "false"
      },
      "ec2RoleDelivery": "2.0"
    }
  },
  "eventTime": "2024-01-22T18:22:05Z",
  "eventSource": "xray.amazonaws.com",
  "eventName": "PutTraceSegments",
  "awsRegion": "us-west-2",
  "sourceIPAddress": "198.51.100.0",
  "userAgent": "aws-sdk-ruby3/3.190.0 md/internal ua/2.0 api/xray#1.0.0 os/linux md/x86_64 lang/ruby#2.7.8 md/2.7.8 cfg/retry-mode#legacy",
  "requestParameters": {
    "traceSegmentDocuments": [
      "trace_id:1-00zzz24z-EXAMPLE4f4e41754c77d0000",
      "trace_id:1-00zzz24z-EXAMPLE4f4e41754c77d0000",
      "trace_id:1-00zzz24z-EXAMPLE4f4e41754c77d0001",
      "trace_id:1-00zzz24z-EXAMPLE4f4e41754c77d0002"
    ]
  },
  "responseElements": {
    "unprocessedTraceSegments": []
  },
  "requestID": "5zzzzz64-acbd-46ff-z544-451a3ebcb2f8",
  "eventID": "4zz51z7z-77f9-44zz-9bd7-6c8327740f2e",
  "readOnly": false,
  "resources": [
    {
      "type": "AWS::XRay::Trace"
    }
  ],
  "eventType": "AwsApiCall",
  "managementEvent": false,
  "recipientAccountId": "012345678910",
  "eventCategory": "Data",
  "tlsDetails": {
    "tlsVersion": "TLSv1.2",
    "cipherSuite": "ZZZZZ-RSA-AAA128-GCM-SHA256",
    "clientProvidedHostHeader": "example.us-west-2.xray.cloudwatch.aws.dev"
  }
}
```