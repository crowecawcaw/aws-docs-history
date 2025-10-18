# Logging Amazon CloudWatch API and console operations with AWS CloudTrail

Amazon CloudWatch, CloudWatch Synthetics, CloudWatch RUM, Amazon Q Developer operational investigations, Network Flow Monitor, and Internet Monitor are integrated with AWS CloudTrail, a service that provides a record

 of actions taken by a user, role, or an AWS service. CloudTrail captures API calls made by or on
 behalf of your AWS account. The captured calls include calls from the CloudWatch console and code calls
 to CloudWatch API operations. Using the information collected by CloudTrail, you can
 determine the request that was made to CloudWatch, the IP address from which the request was
 made, when it was made, and additional details.

Every event or log entry contains information about who generated the request. The
 identity information helps you determine the following: 


* Whether the request was made with root user or user credentials.
* Whether the request was made on behalf of an IAM Identity Center user.
* Whether the request was made with temporary security credentials for a role or federated
 user.
* Whether the request was made by another AWS service.
CloudTrail is active in your AWS account when you create the account and you automatically have
 access to the CloudTrail **Event history**. The CloudTrail **Event
 history** provides a viewable, searchable, downloadable, and immutable record of the
 past 90 days of recorded management events in an AWS Region. For more information, see [Working
 with CloudTrail Event history](../../../awscloudtrail/latest/userguide/view-cloudtrail-events.md "../../../awscloudtrail/latest/userguide/view-cloudtrail-events.md") in the *AWS CloudTrail User Guide*. There are no CloudTrail
 charges for viewing the **Event history**.

For an ongoing record of events in your AWS account past 90 days, create a trail or a
 [CloudTrail
 Lake](../../../awscloudtrail/latest/userguide/cloudtrail-lake.md "../../../awscloudtrail/latest/userguide/cloudtrail-lake.md") event data store.



**CloudTrail trails**

A *trail* enables CloudTrail to deliver log files to an Amazon S3 bucket. All trails created using the AWS Management Console are multi-Region. You can create a single-Region or a multi-Region trail by using the AWS CLI. Creating a multi-Region trail is recommended because you capture activity in all AWS Regions in your account. If you create a single-Region trail, you can view only the events logged in the trail's AWS Region. For more information about trails, see [Creating a trail for your AWS account](../../../awscloudtrail/latest/userguide/cloudtrail-create-and-update-a-trail.md "../../../awscloudtrail/latest/userguide/cloudtrail-create-and-update-a-trail.md") and [Creating a trail for an organization](../../../awscloudtrail/latest/userguide/creating-trail-organization.md "../../../awscloudtrail/latest/userguide/creating-trail-organization.md") in the *AWS CloudTrail User Guide*.


You can deliver one copy of your ongoing management events to your Amazon S3 bucket at no charge from CloudTrail by creating a trail, however, there are Amazon S3 storage charges. For more information about CloudTrail pricing, see [AWS CloudTrail Pricing](https://aws.amazon.com/cloudtrail/pricing/ "https://aws.amazon.com/cloudtrail/pricing/"). For information about Amazon S3 pricing, see [Amazon S3 Pricing](https://aws.amazon.com/s3/pricing/ "https://aws.amazon.com/s3/pricing/").



**CloudTrail Lake event data stores**

*CloudTrail Lake* lets you run SQL-based queries on your events. CloudTrail Lake converts existing events in row-based JSON format to  [Apache ORC](https://orc.apache.org/ "https://orc.apache.org/") format. ORC is a columnar storage format that is optimized for fast retrieval of data. Events are aggregated into *event data stores*, which are immutable collections of events based on criteria that you select by applying [advanced event selectors](../../../awscloudtrail/latest/userguide/cloudtrail-lake-concepts.md#adv-event-selectors "../../../awscloudtrail/latest/userguide/cloudtrail-lake-concepts.md#adv-event-selectors"). The selectors that you apply to an event data store control which events persist and are available for you to query. For more information about CloudTrail Lake, see [Working with AWS CloudTrail Lake](../../../awscloudtrail/latest/userguide/cloudtrail-lake.md "../../../awscloudtrail/latest/userguide/cloudtrail-lake.md") in the *AWS CloudTrail User Guide*.


CloudTrail Lake event data stores and queries incur costs. When you create an event data store, you choose the [pricing option](../../../awscloudtrail/latest/userguide/cloudtrail-lake-manage-costs.md#cloudtrail-lake-manage-costs-pricing-option "../../../awscloudtrail/latest/userguide/cloudtrail-lake-manage-costs.md#cloudtrail-lake-manage-costs-pricing-option") you want to use for the event data store. The pricing option determines the cost for ingesting and storing events, and the default and maximum retention period for the event data store. For more information about CloudTrail pricing, see [AWS CloudTrail Pricing](https://aws.amazon.com/cloudtrail/pricing/ "https://aws.amazon.com/cloudtrail/pricing/").



###### Note

For information about CloudWatch Logs API calls that are logged in CloudTrail, see 
 [CloudWatch Logs information in CloudTrail](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/logging_cw_api_calls_cwl.html#cwl_info_in_ct "https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/logging_cw_api_calls_cwl.html#cwl_info_in_ct").

###### Topics

* [CloudWatch information in CloudTrail](#cw_info_in_ct "#cw_info_in_ct")
* [CloudWatch data events in CloudTrail](#CloudWatch-data-plane-events "#CloudWatch-data-plane-events")
* [Query generation information in CloudTrail](#cwl_query-generation-cloudtrail "#cwl_query-generation-cloudtrail")
* [Amazon Q Developer operational investigations events in CloudTrail](#Q-Developer-Investigations-Cloudtrail "#Q-Developer-Investigations-Cloudtrail")
* [Network Flow Monitor in CloudTrail](#CloudWatch-NetworkFlowMonitor-info-in-ct "#CloudWatch-NetworkFlowMonitor-info-in-ct")
* [Network Flow Monitor data plane
 events in CloudTrail](#CloudWatch-NetworkFlowMonitor-data-plane-events "#CloudWatch-NetworkFlowMonitor-data-plane-events")
* [Internet Monitor in CloudTrail](#cw_im_info_in_ct "#cw_im_info_in_ct")
* [CloudWatch Synthetics information in CloudTrail](#cw_synthetics_info_in_ct "#cw_synthetics_info_in_ct")
* [CloudWatch RUM information in CloudTrail](#RUM-CloudTrail "#RUM-CloudTrail")
* [CloudWatch RUM data plane
 events in CloudTrail](#RUM-data-plane-events "#RUM-data-plane-events")
* [Network Synthetic Monitor information in CloudTrail](#cw_network_synthetic_monitor_info_in_ct "#cw_network_synthetic_monitor_info_in_ct")
* [CloudWatch Observability Access Manager information in CloudTrail](#cw_observability_access_manager_info_in_ct "#cw_observability_access_manager_info_in_ct")
* [CloudWatch Observability Admin information in CloudTrail](#cw_observability_admin_info_in_ct "#cw_observability_admin_info_in_ct")
* [CloudWatch Application Signals information in CloudTrail](#cw_application_signals_info_in_ct "#cw_application_signals_info_in_ct")
* [CloudWatch Application Insights information in CloudTrail](#cw_application_insights_info_in_ct "#cw_application_insights_info_in_ct")
## CloudWatch information in CloudTrail


CloudWatch supports logging the following actions as events in CloudTrail log files:



* [DeleteAlarmActions](../APIReference/API_DeleteAlarmActions.md "../APIReference/API_DeleteAlarmActions.md")
* [DeleteAnomalyDetector](../APIReference/API_DeleteAnomalyDetector.md "../APIReference/API_DeleteAnomalyDetector.md")
* [DeleteDashboards](../APIReference/API_DeleteDashboards.md "../APIReference/API_DeleteDashboards.md")
* [DeleteInsightRules](../APIReference/API_DeleteInsightRules.md "../APIReference/API_DeleteInsightRules.md")
* [DeleteMetricStream](../APIReference/API_DeleteMetricStream.md "../APIReference/API_DeleteMetricStream.md")
* [DescribeAlarmHistory](../APIReference/API_DescribeAlarmHistory.md "../APIReference/API_DescribeAlarmHistory.md")
* [DescribeAlarms](../APIReference/API_DescribeAlarms.md "../APIReference/API_DescribeAlarms.md")
* [DescribeAlarmsForMetric](../APIReference/API_DescribeAlarmsForMetric.md "../APIReference/API_DescribeAlarmsForMetric.md")
* [DescribeAnomalyDetectors](../APIReference/API_DescribeAnomalyDetectors.md "../APIReference/API_DescribeAnomalyDetectors.md")
* [DescribeInsightRules](../APIReference/API_DescribeInsightRules.md "../APIReference/API_DescribeInsightRules.md")
* [DisableAlarmActions](../APIReference/API_DisableAlarmActions.md "../APIReference/API_DisableAlarmActions.md")
* [DisableInsightRules](../APIReference/API_DisableInsightRules.md "../APIReference/API_DisableInsightRules.md")
* [EnableAlarmActions](../APIReference/API_EnableAlarmActions.md "../APIReference/API_EnableAlarmActions.md")
* [EnableInsightRules](../APIReference/API_EnableInsightRules.md "../APIReference/API_EnableInsightRules.md")
* [GetDashboard](../APIReference/API_GetDashboard.md "../APIReference/API_GetDashboard.md")
* [GetInsightRuleReport](../APIReference/API_GetInsightRuleReport.md "../APIReference/API_GetInsightRuleReport.md")
* [GetMetricStream](../APIReference/API_GetMetricStream.md "../APIReference/API_GetMetricStream.md")
* [ListDashboards](../APIReference/API_ListDashboards.md "../APIReference/API_ListDashboards.md")
* [ListManagedInsightRules](../APIReference/API_ListManagedInsightRules.md "../APIReference/API_ListManagedInsightRules.md")
* [ListMetricStreams](../APIReference/API_ListMetricStreams.md "../APIReference/API_ListMetricStreams.md")
* [ListTagsForResource](../APIReference/API_ListTagsForResource.md "../APIReference/API_ListTagsForResource.md")
* [PutAnomalyDetector](../APIReference/API_PutAnomalyDetector.md "../APIReference/API_PutAnomalyDetector.md")
* [PutCompositeAlarm](../APIReference/API_PutCompositeAlarm.md "../APIReference/API_PutCompositeAlarm.md")
* [PutDashboard](../APIReference/API_PutDashboard.md "../APIReference/API_PutDashboard.md")
* [PutInsightRule](../APIReference/API_PutInsightRule.md "../APIReference/API_PutInsightRule.md")
* [PutManagedInsightRules](../APIReference/API_PutManagedInsightRules.md "../APIReference/API_PutManagedInsightRules.md")
* [PutMetricAlarm](../APIReference/API_PutMetricAlarm.md "../APIReference/API_PutMetricAlarm.md")
* [PutMetricStream](../APIReference/API_PutMetricStream.md "../APIReference/API_PutMetricStream.md")
* [SetAlarmState](../APIReference/API_SetAlarmState.md "../APIReference/API_SetAlarmState.md")
* [StartMetricStreams](../APIReference/API_StartMetricStreams.md "../APIReference/API_StartMetricStreams.md")
* [StopMetricStreams](../APIReference/API_StopMetricStreams.md "../APIReference/API_StopMetricStreams.md")
* [TagResource](../APIReference/API_TagResource.md "../APIReference/API_TagResource.md")
* [UntagResource](../APIReference/API_UntagResource.md "../APIReference/API_UntagResource.md")

### Example: CloudWatch log file
 entries


The following example shows a CloudTrail log entry that demonstrates the `PutMetricAlarm` action.



```
{
    "Records": [{
        "eventVersion": "1.01",
        "userIdentity": {
            "type": "Root",
            "principalId": "EX_PRINCIPAL_ID",
            "arn": "arn:aws:iam::123456789012:root",
            "accountId": "123456789012",
            "accessKeyId": "EXAMPLE_KEY_ID"
        },
        "eventTime": "2014-03-23T21:50:34Z",
        "eventSource": "monitoring.amazonaws.com",
        "eventName": "PutMetricAlarm",
        "awsRegion": "us-east-1",
        "sourceIPAddress": "127.0.0.1",
        "userAgent": "aws-sdk-ruby2/2.0.0.rc4 ruby/1.9.3 x86_64-linux Seahorse/0.1.0",
        "requestParameters": {
            "threshold": 50.0,
            "period": 60,
            "metricName": "CloudTrail Test",
            "evaluationPeriods": 3,
            "comparisonOperator": "GreaterThanThreshold",
            "namespace": "AWS/CloudWatch",
            "alarmName": "CloudTrail Test Alarm",
            "statistic": "Sum"
        },
        "responseElements": null,
        "requestID": "29184022-b2d5-11e3-a63d-9b463e6d0ff0",
        "eventID": "b096d5b7-dcf2-4399-998b-5a53eca76a27"
    },
    ..additional entries
  ]
  }
```

The following log file entry shows that a user called the CloudWatch Events
 `PutRule` action.



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

The following log file entry shows that a user called the CloudWatch Logs
 `CreateExportTask` action.



```
{
        "eventVersion": "1.03",
        "userIdentity": {
            "type": "IAMUser",
            "principalId": "EX_PRINCIPAL_ID",
            "arn": "arn:aws:iam::123456789012:user/someuser",
            "accountId": "123456789012",
            "accessKeyId": "AKIAIOSFODNN7EXAMPLE",
            "userName": "someuser"
        },
        "eventTime": "2016-02-08T06:35:14Z",
        "eventSource": "logs.amazonaws.com",
        "eventName": "CreateExportTask",
        "awsRegion": "us-east-1",
        "sourceIPAddress": "127.0.0.1",
        "userAgent": "aws-sdk-ruby2/2.0.0.rc4 ruby/1.9.3 x86_64-linux Seahorse/0.1.0",
        "requestParameters": {
            "destination": "yourdestination",
            "logGroupName": "yourloggroup",
            "to": 123456789012,
            "from": 0,
            "taskName": "yourtask"
        },
        "responseElements": {
            "taskId": "15e5e534-9548-44ab-a221-64d9d2b27b9b"
        },
        "requestID": "1cd74c1c-ce2e-12e6-99a9-8dbb26bd06c9",
        "eventID": "fd072859-bd7c-4865-9e76-8e364e89307c",
        "eventType": "AwsApiCall",
        "apiVersion": "20140328",
        "recipientAccountId": "123456789012"
}
```

## CloudWatch data events in CloudTrail


CloudTrail can capture API activities related to the CloudWatch data plane operations on metrics [GetMetricData](../APIReference/API_GetMetricData.md "../APIReference/API_GetMetricData.md"), [GetMetricWidgetImage](../APIReference/API_GetMetricWidgetImage.md "../APIReference/API_GetMetricWidgetImage.md"), [PutMetricData](../APIReference/API_PutMetricData.md "../APIReference/API_PutMetricData.md"), [GetMetricStatistics](../APIReference/API_GetMetricStatistics.md "../APIReference/API_GetMetricStatistics.md"), and [ListMetrics](../APIReference/API_ListMetrics.md "../APIReference/API_ListMetrics.md") APIs.


[Data events](../../../awscloudtrail/latest/userguide/logging-data-events-with-cloudtrail.md#logging-data-events "../../../awscloudtrail/latest/userguide/logging-data-events-with-cloudtrail.md#logging-data-events"), also known as data plane operations, give you insight into the resource operations performed 
 on or within a resource. Data events are often high-volume activities. 


By default, CloudTrail doesn’t log
 data events. The CloudTrail **Event history** doesn't record data events.


Additional charges apply for data events. For more information about CloudTrail pricing, see
 [AWS CloudTrail Pricing](https://aws.amazon.com/cloudtrail/pricing/ "https://aws.amazon.com/cloudtrail/pricing/").


You can log data events for the CloudWatch resource types by using the CloudTrail console, AWS CLI,
 or CloudTrail API operations. For more information about how to log data events, see [Logging data events with the AWS Management Console](../../../awscloudtrail/latest/userguide/logging-data-events-with-cloudtrail.md#logging-data-events-console "../../../awscloudtrail/latest/userguide/logging-data-events-with-cloudtrail.md#logging-data-events-console") and [Logging data events with the AWS Command Line Interface](../../../awscloudtrail/latest/userguide/logging-data-events-with-cloudtrail.md#creating-data-event-selectors-with-the-AWS-CLI "../../../awscloudtrail/latest/userguide/logging-data-events-with-cloudtrail.md#creating-data-event-selectors-with-the-AWS-CLI") in the
 *AWS CloudTrail User Guide*.


Data plane events can be filtered by resource type. Because there are additional costs for using 
 data events in CloudTrail, filtering by resource allows you to have more control over what you log and pay for. 


Using the information that CloudTrail collects, you can identify any of the metric APIs, the IP address of the requester, the requester's identity, and the date and time of the 
 request. Logging the **GetMetricData**, **GetMetricWidgetImage**, **PutMetricData**, **GetMetricStatistics**, and **ListMetrics** APIs using CloudTrail helps you enable operational and 
 risk auditing, governance, and compliance of your AWS account.


###### Note

When you view the **GetMetricData** events in CloudTrail, you might see more calls than the calls that you initiated. 
 This is because CloudWatch logs events to CloudTrail for **GetMetricData** actions that are initiated by internal components. For example, you'll 
 see **GetMetricData** calls initiated by CloudWatch dashboards to refresh widget data, and **GetMetricData** calls initiated by a 
 monitoring account to retrieve data from a source account, 
 in cross-account observability. These internally-initiated calls don't incur CloudWatch charges, but they do count toward the number of events
 logged in CloudTrail, and CloudTrail charges according to the number of events logged.


The following is an example of a CloudTrail event for a **GetMetricData** operation.



```
{
    "eventVersion": "1.09",
    "userIdentity": {
        "type": "IAMUser",
        "principalId": "AIDA2NYTR2EPCTNY7AF3L",
        "arn": "arn:aws:iam::111122223333:user/admin",
        "accountId": "111122223333",
        "accessKeyId": "EXAMPLE1234567890",
        "userName": "admin"
    },
    "eventTime": "2024-05-08T16:20:34Z",
    "eventSource": "monitoring.amazonaws.com",
    "eventName": "GetMetricData",
    "awsRegion": "us-east-1",
    "sourceIPAddress": "99.45.3.7",
    "userAgent": "aws-cli/2.13.23 Python/3.11.5 Darwin/23.4.0 exe/x86_64 prompt/off command/cloudwatch.get-metric-data",
    "requestParameters": {
        "metricDataQueries": [{
                "id": "e1",
                "expression": "m1 / m2",
                "label": "ErrorRate"
            },
            {
                "id": "m1",
                "metricStat": {
                    "metric": {
                        "namespace": "CWAgent",
                        "metricName": "disk_used_percent",
                        "dimensions": [{
                            "name": "LoadBalancerName",
                            "value": "EXAMPLE4623a5cb6a7384c5229"
                        }]
                    },
                    "period": 300,
                    "stat": "Sum",
                    "unit": "Count"
                },
                "returnData": false
            },
            {
                "id": "m2",
                "metricStat": {
                    "metric": {
                        "namespace": "CWAgent",
                        "metricName": "disk_used_percent",
                        "dimensions": [{
                            "name": "LoadBalancerName",
                            "value": "EXAMPLE4623a5cb6a7384c5229"
                        }]
                    },
                    "period": 300,
                    "stat": "Sum"
                },
                "returnData": true
            }
        ],
        "startTime": "Apr 19, 2024, 4:00:00 AM",
        "endTime": "May 8, 2024, 4:30:00 AM"
    },
    "responseElements": null,
    "requestID": "EXAMPLE-57ac-47d5-938c-f5917c6799d5",
    "eventID": "EXAMPLE-211c-404b-b13d-36d93c8b4fbf",
    "readOnly": true,
    "resources": [{
        "type": "AWS::CloudWatch::Metric"
    }],
    "eventType": "AwsApiCall",
    "managementEvent": false,
    "recipientAccountId": "111122223333",
    "eventCategory": "Data",
    "tlsDetails": {
        "tlsVersion": "TLSv1.3",
        "cipherSuite": "TLS_AES_128_GCM_SHA256",
        "clientProvidedHostHeader": "monitoring.us-east-1.amazonaws.com"
    }
}
```

The following is an example of a CloudTrail event for a **PutMetricData** operation.



```
{
      "eventVersion": "1.11",
      "userIdentity": {
        "type": "AssumedRole",
        "principalId": "111122223333:`example`.amazon.com",
        "arn": "arn:aws:sts::111122223333:assumed-role/cloudwatch.full.access/`example`.amazon.com",
        "accountId": "111122223333",
        "accessKeyId": "EXAMPLE1234567890",
        "sessionContext": {
          "sessionIssuer": {
            "type": "Role",
            "principalId": "AROA3FLD4LJVPWYJ6BCNM",
            "arn": "arn:aws:iam::111122223333:role/cloudwatch.full.access",
            "accountId": "111122223333",
            "userName": "cloudwatch.full.access"
          },
          "attributes": {
            "creationDate": "2025-06-19T23:19:50Z",
            "mfaAuthenticated": "false"
          }
        }
      },
      "eventTime": "2025-06-19T23:51:04Z",
      "eventSource": "monitoring.amazonaws.com",
      "eventName": "PutMetricData",
      "awsRegion": "us-east-1",
      "sourceIPAddress": "AWS Internal",
      "userAgent": "AWS Internal",
      "requestParameters": {
        "namespace": "CloudTrailTests",
        "metricData": [
          {
            "metricName": "CloudTrailPutMetricDataTest",
            "dimensions": [
              {
                "name": "TestDimName",
                "value": "TestDimValue"
              }
            ]
          }
        ]
      },
      "responseElements": null,
      "requestID": "877db913-2620-4929-97f3-f3c93c6f689b",
      "eventID": "0c0c4516-75f4-4b27-8a83-213821a96a2b",
      "readOnly": false,
      "resources": [
        {
          "type": "AWS::CloudWatch::Metric"
        }
      ],
      "eventType": "AwsApiCall",
      "managementEvent": false,
      "recipientAccountId": "111122223333",
      "eventCategory": "Data",
      "tlsDetails": {
        "tlsVersion": "TLSv1.3",
        "cipherSuite": "TLS_AES_128_GCM_SHA256",
        "clientProvidedHostHeader": "monitoring.us-east-1.amazonaws.com"
      }
    }
```

## Query generation information in CloudTrail


CloudTrail logging for Query generator console events is also supported. Query generator is currently supported for 
 CloudWatch Metric Insights and CloudWatch Logs Insights. In these CloudTrail events, the `eventSource` is `monitoring.amazonaws.com`.


The following example shows a 
 CloudTrail log entry that demonstrates the **GenerateQuery** action in CloudWatch Metrics Insights. 



```
{
    "eventVersion": "1.09",
    "userIdentity": {
        "type": "AssumedRole",
        "principalId": "EX_PRINCIPAL_ID",
        "arn": "arn:aws:iam::123456789012:assumed-role/role_name",
        "accountId": "123456789012",
        "accessKeyId": "AKIAIOSFODNN7EXAMPLE",
        "sessionContext": {
            "sessionIssuer": {
                "type": "Role",
                "principalId": "EX_PRINCIPAL_ID",
                "arn": "arn:aws:iam::111222333444:role/Administrator",
                "accountId": "123456789012",
                "userName": "SAMPLE_NAME"
            },
            "attributes": {
                "creationDate": "2020-04-08T21:43:24Z",
                "mfaAuthenticated": "false"
            }
        }
    },
    "eventTime": "2020-04-08T23:06:30Z",
    "eventSource": "monitoring.amazonaws.com",
    "eventName": "GenerateQuery",
    "awsRegion": "us-east-1",
    "sourceIPAddress": "127.0.0.1",
    "userAgent": "exampleUserAgent",
    "requestParameters": {
        "query_ask": "***",
        "query_type": "MetricsInsights",
        "metrics_insights": {
            "aws_namespaces": [
                "AWS/S3",
                "AWS/Lambda",
                "AWS/DynamoDB"
            ]
        },
        "include_description": true
    },
    "responseElements": null,
    "requestID": "2f56318c-cfbd-4b60-9d93-1234567890",
    "eventID": "52723fd9-4a54-478c-ac55-1234567890",
    "readOnly": true,
    "eventType": "AwsApiCall",
    "managementEvent": true,
    "recipientAccountId": "111122223333", 
    "eventCategory": "Management"
}
```

## Amazon Q Developer operational investigations events in CloudTrail


Amazon Q Developer operational investigations supports logging the following actions as events in CloudTrail log files.



* [CreateInvestigationGroup](https://docs.aws.amazon.com/cloudwatchinvestigations/latest/APIReference/API_CreateInvestigationGroup.html "https://docs.aws.amazon.com/cloudwatchinvestigations/latest/APIReference/API_CreateInvestigationGroup.html")
* [GetInvestigationGroup](https://docs.aws.amazon.com/cloudwatchinvestigations/latest/APIReference/API_GetInvestigationGroup.html "https://docs.aws.amazon.com/cloudwatchinvestigations/latest/APIReference/API_GetInvestigationGroup.html")
* [DeleteInvestigationGroup](https://docs.aws.amazon.com/cloudwatchinvestigations/latest/APIReference/API_DeleteInvestigationGroup.html "https://docs.aws.amazon.com/cloudwatchinvestigations/latest/APIReference/API_DeleteInvestigationGroup.html")
* [ListInvestigationGroup](https://docs.aws.amazon.com/cloudwatchinvestigations/latest/APIReference/API_ListInvestigationGroups.html "https://docs.aws.amazon.com/cloudwatchinvestigations/latest/APIReference/API_ListInvestigationGroups.html")
* [PutInvestigationGroupPolicy](https://docs.aws.amazon.com/cloudwatchinvestigations/latest/APIReference/API_PutInvestigationGroupPolicy.html "https://docs.aws.amazon.com/cloudwatchinvestigations/latest/APIReference/API_PutInvestigationGroupPolicy.html")
* [DeleteInvestigationGroupPolicy](https://docs.aws.amazon.com/cloudwatchinvestigations/latest/APIReference/API_DeleteInvestigationGroupPolicy.html "https://docs.aws.amazon.com/cloudwatchinvestigations/latest/APIReference/API_DeleteInvestigationGroupPolicy.html")
* [ListTagsForResource](https://docs.aws.amazon.com/cloudwatchinvestigations/latest/APIReference/API_ListTagsForResource.html "https://docs.aws.amazon.com/cloudwatchinvestigations/latest/APIReference/API_ListTagsForResource.html")
* [GetInvestigationGroupPolicy](https://docs.aws.amazon.com/cloudwatchinvestigations/latest/APIReference/API_GetInvestigationGroupPolicy.html "https://docs.aws.amazon.com/cloudwatchinvestigations/latest/APIReference/API_GetInvestigationGroupPolicy.html")
* [TagResource](https://docs.aws.amazon.com/cloudwatchinvestigations/latest/APIReference/API_TagResource.html "https://docs.aws.amazon.com/cloudwatchinvestigations/latest/APIReference/API_TagResource.html")
* [UntagResource](https://docs.aws.amazon.com/cloudwatchinvestigations/latest/APIReference/API_UntagResource.html "https://docs.aws.amazon.com/cloudwatchinvestigations/latest/APIReference/API_UntagResource.html")
* [UpdateInvestigationGroup](https://docs.aws.amazon.com/cloudwatchinvestigations/latest/APIReference/API_UpdateInvestigationGroup.html "https://docs.aws.amazon.com/cloudwatchinvestigations/latest/APIReference/API_UpdateInvestigationGroup.html")

### Example: Amazon Q Developer operational investigations
 log file entries


The following example shows a Amazon Q Developer operational investigations log entry that demonstrates the 
 `CreateInvestigationGroup` action.



```
{
	"eventVersion": "1.09",
	"userIdentity": {
		"type": "AssumedRole",
		"principalId": "EX_PRINCIPAL_ID",
		"arn": "arn:aws:iam::123456789012:assumed-role/role_name",
		"accountId": "123456789012",
		"accessKeyId": "AKIAIOSFODNN7EXAMPLE",
		"sessionContext": {
			"sessionIssuer": {
				"type": "Role",
				"principalId": "EX_PRINCIPAL_ID",
				"arn": "arn:aws:iam::123456789012:role/role_name",
				"accountId": "123456789012",
				"userName": "SAMPLE_NAME"
			},
			"attributes": {
				"creationDate": "2024-10-30T18:42:05Z",
				"mfaAuthenticated": "false"
			}
		}
	},
	"eventTime": "2024-10-30T18:48:26Z",
	"eventSource": "aiops.amazonaws.com",
	"eventName": "CreateInvestigationGroup",
	"awsRegion": "us-east-1",
	"sourceIPAddress": "127.0.0.1",
	"userAgent": "exampleUserAgent",
	"requestParameters": {
		"name": "exampleName",
		"roleArn": "arn:aws:iam::123456789012:role/role_name"	},
	"responseElements": {
		"arn": "arn:aws:aiops:us-east-1:123456789012:investigation-group/021345abcdef67890"
	},
	"requestId": "e9caf887-8d88-11e5-a331-3332aa445952",
	"requestId": "49d14f36-6450-44a5-a501-b0fdcdfaeb98",
	"readOnly": false,
	"eventType": "AwsApiCall",
	"managementEvent": true,
	"recipientAccountId": "123456789012",
	"eventCategory": "Management"
}
```

The following example shows a Amazon Q Developer operational investigations log entry that demonstrates the 
 `CreateInvestigationEvent` action.



```
{
		"eventVersion": "1.09",
		"userIdentity": {
			"type": "AssumedRole",
			"principalId": "EX_PRINCIPAL_ID",
			"arn": "arn:aws:sts::123456789012:assumed-role/role_name",
			"accountId": "123456789012",
			"accessKeyId": "AKIAIOSFODNN7EXAMPLE",
			"sessionContext": {
				"sessionIssuer": {
					"type": "Role",
					"principalId": "EX_PRINCIPAL_ID",
					"arn": "arn:aws:iam::123456789012:role/role_name",
					"accountId": "123456789012",
					"userName": "SAMPLE_NAME"
				},
				"attributes": {
					"creationDate": "2024-10-30T16:17:49Z",
					"mfaAuthenticated": "false"
				}
			}
		},
		"eventTime": "2024-10-30T16:35:34Z",
		"eventSource": "aiops.amazonaws.com",
		"eventName": "CreateInvestigationEvent",
		"awsRegion": "us-east-1",
		"sourceIPAddress": "127.0.0.1",
		"userAgent": "exampleUserAgent",
		"requestParameters": {
			"identifier": "arn:aws:aiops:us-east-1:123456789012:investigation-group/021345abcdef67890",
			"investigationId": "bcdef01234567890",
			"clientToken": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
			"type": "METRIC_OBSERVATION",
			"body": "***"
		},
		"responseElements": {
			"investigationGroupArn": "arn:aws:aiops:us-east-1:123456789012:investigation-group/021345abcdef67890",
			"investigationId": "bcdef01234567890",
			"investigationEventId": "14567890abcdef0g"
		},
		"requestId": "e9caf887-8d88-11e5-a331-3332aa445952",
		"eventId": "49d14f36-6450-44a5-a501-b0fdcdfaeb98",
		"readOnly": false,
		"resources": [{
			"accountId": "123456789012",
			"type": "AWS::AIOps::InvestigationGroup",
			"ARN": "arn:aws:aiops:us-east-1:123456789012:investigation-group/021345abcdef67890"
		}],
		"eventType": "AwsApiCall",
		"managementEvent": false,
		"recipientAccountId": "123456789012",
		"eventCategory": "Data"
	}
```

The following example shows a Amazon Q Developer operational investigations log entry that demonstrates the 
 `UpdateInvestigationEvent` action.



```
{
	"eventVersion": "1.09",
	"userIdentity": {
		"type": "AssumedRole",
		"principalId": "EX_PRINCIPAL_ID",
		"arn": "arn:aws:sts::123456789012:assumed-role/role_name",
		"accountId": "123456789012",
		"accessKeyId": "AKIAIOSFODNN7EXAMPLE",
		"sessionContext": {
			"sessionIssuer": {
				"type": "Role",
				"principalId": "EX_PRINCIPAL_ID",
				"arn": "arn:aws:iam::123456789012:role/role_name",
				"accountId": "123456789012",
				"userName": "SAMPLE_NAME"
			},
			"attributes": {
				"creationDate": "2024-10-30T16:17:49Z",
				"mfaAuthenticated": "false"
			}
		}
	},
	"eventTime": "2024-10-30T16:24:48Z",
	"eventSource": "aiops.amazonaws.com",
	"eventName": "UpdateInvestigationEvent",
	"awsRegion": "us-east-1",
	"sourceIPAddress": "127.0.0.1",
	"userAgent": "exampleUserAgent",
	"requestParameters": {
		"identifier": "arn:aws:aiops:us-east-1:123456789012:investigation-group/021345abcdef67890",
		"investigationId": "bcdef01234567890",
		"investigationEventId": "14567890abcdef0g",
		"comment": "***"
	},
	"responseElements": null,
	"requestId": "e9caf887-8d88-11e5-a331-3332aa445952",
	"eventId": "49d14f36-6450-44a5-a501-b0fdcdfaeb98",
	"readOnly": false,
	"resources": [{
		"accountId": "123456789012",
		"type": "AWS::AIOps::InvestigationGroup",
		"ARN": "arn:aws:aiops:us-east-1:123456789012:investigation-group/021345abcdef67890"
	}],
	"eventType": "AwsApiCall",
	"managementEvent": false,
	"recipientAccountId": "123456789012",
	"eventCategory": "Data"
}
```

## Network Flow Monitor in CloudTrail


Network Flow Monitor supports logging the following actions as events in CloudTrail log files.



* [CreateMonitor](https://docs.aws.amazon.com/networkflowmonitor/2.0/APIReference/API_CreateMonitor.html "https://docs.aws.amazon.com/networkflowmonitor/2.0/APIReference/API_CreateMonitor.html")
* [CreateScope](https://docs.aws.amazon.com/networkflowmonitor/2.0/APIReference/API_CreateScope.html "https://docs.aws.amazon.com/networkflowmonitor/2.0/APIReference/API_CreateScope.html")
* [DeleteMonitor](https://docs.aws.amazon.com/networkflowmonitor/2.0/APIReference/API_DeleteMonitor.html "https://docs.aws.amazon.com/networkflowmonitor/2.0/APIReference/API_DeleteMonitor.html")
* [DeleteScope](https://docs.aws.amazon.com/networkflowmonitor/2.0/APIReference/API_DeleteScope.html "https://docs.aws.amazon.com/networkflowmonitor/2.0/APIReference/API_DeleteScope.html")
* [GetMonitor](https://docs.aws.amazon.com/networkflowmonitor/2.0/APIReference/API_GetMonitor.html "https://docs.aws.amazon.com/networkflowmonitor/2.0/APIReference/API_GetMonitor.html")
* [GetScope](https://docs.aws.amazon.com/networkflowmonitor/2.0/APIReference/API_GetScope.html "https://docs.aws.amazon.com/networkflowmonitor/2.0/APIReference/API_GetScope.html")
* [ListMonitors](https://docs.aws.amazon.com/networkflowmonitor/2.0/APIReference/API_ListMonitors.html "https://docs.aws.amazon.com/networkflowmonitor/2.0/APIReference/API_ListMonitors.html")
* [ListScopes](https://docs.aws.amazon.com/networkflowmonitor/2.0/APIReference/API_ListScopes.html "https://docs.aws.amazon.com/networkflowmonitor/2.0/APIReference/API_ListScopes.html")
* [ListTagsForResource](https://docs.aws.amazon.com/networkflowmonitor/2.0/APIReference/API_ListTagsForResource.html "https://docs.aws.amazon.com/networkflowmonitor/2.0/APIReference/API_ListTagsForResource.html")
* [TagResource](https://docs.aws.amazon.com/networkflowmonitor/2.0/APIReference/API_TagResource.html "https://docs.aws.amazon.com/networkflowmonitor/2.0/APIReference/API_TagResource.html")
* [UntagResource](https://docs.aws.amazon.com/networkflowmonitor/2.0/APIReference/API_UntagResource.html "https://docs.aws.amazon.com/networkflowmonitor/2.0/APIReference/API_UntagResource.html")
* [UpdateMonitor](https://docs.aws.amazon.com/networkflowmonitor/2.0/APIReference/API_UpdateMonitor.html "https://docs.aws.amazon.com/networkflowmonitor/2.0/APIReference/API_UpdateMonitor.html")
* [UpdateScope](https://docs.aws.amazon.com/networkflowmonitor/2.0/APIReference/API_UpdateScope.html "https://docs.aws.amazon.com/networkflowmonitor/2.0/APIReference/API_UpdateScope.html")

### Example: Network Flow Monitor
 log file entry


The following example shows a Network Flow Monitor CloudTrail log file entry that demonstrates the 
 `CreateMonitor` action.



```

{
    "eventVersion": "1.09",
    "userIdentity": {
        "type": "AssumedRole",
        "principalId": "EX_PRINCIPAL_ID",
        "arn": "arn:aws:iam::000000000000:assumed-role/role_name",
        "accountId": "123456789012",
        "accessKeyId": "AKIAIOSFODNN7EXAMPLE",
        "sessionContext": {
            "sessionIssuer": {
                "type": "Role",
                "principalId": "EX_PRINCIPAL_ID",
                "arn": "arn:aws:iam::000000000000:role/Admin",
                "accountId": "123456789012",
                "userName": "SAMPLE_NAME"
            },
            "attributes": {
                "creationDate": "2024-11-03T15:43:27Z",
                "mfaAuthenticated": "false"
            }
        }
    },
    "eventTime": "2024-11-03T15:58:11Z",
    "eventSource": "networkflowmonitor.amazonaws.com",
    "eventName": "CreateMonitor",
    "awsRegion": "us-east-1",
    "sourceIPAddress": "192.0.2.0",
    "userAgent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)",
    "requestParameters": {
        "MonitorName": "TestMonitor",
        "ClientToken": "33551db7-1618-4aab-cdef-EXAMPLE33333",
        "LocalResources": [
            {
                "Type": "AWS::EC2::Subnet",
                "Identifier": "subnet-cdef-EXAMPLEbbbbb"
            },
            {
                "Type": "AWS::EC2::Subnet",
                "Identifier": "subnet-cdef-EXAMPLEccccc"
            },
            {
                "Type": "AWS::EC2::Subnet",
                "Identifier": "subnet-cdef-EXAMPLEddddd"
            },
            {
                "Type": "AWS::EC2::Subnet",
                "Identifier": "subnet-cdef-EXAMPLEeeeee"
            },
            {
                "Type": "AWS::EC2::Subnet",
                "Identifier": "subnet-cdef-EXAMPLEfffff"
            },
            {
                "Type": "AWS::EC2::Subnet",
                "Identifier": "subnet-cdef-EXAMPLEggggg"
            }
        ]
    },
    "responseElements": {
        "Access-Control-Expose-Headers": "*",
        "MonitorArn": "arn:aws:networkflowmonitor:us-east-1:000000000000:monitor/TestMonitor",
        "MonitorName": "TestMonitor",
        "MonitorStatus": "ACTIVE"
    },
    "requestID": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
    "eventID": "a1b2c3d4-5678-90ab-cdef-EXAMPLEbbbbb",
    "readOnly": false,
    "eventType": "AwsApiCall",
    "managementEvent": true,
    "recipientAccountId": "111122223333",
    "eventCategory": "Management"
}
```


```
{
        "eventVersion": "1.08",
        "userIdentity": {
            "type": "AssumedRole",
            "principalId": "EX_PRINCIPAL_ID",
            "arn": "arn:aws:iam::000000000000:assumed-role/role_name",
            "accountId":"123456789012",
            "accessKeyId":"AKIAIOSFODNN7EXAMPLE",
            "sessionContext": {
                "sessionIssuer": {
                "type": "Role",
                "principalId": "EX_PRINCIPAL_ID",
                "arn": "arn:aws:iam::000000000000:role/Admin",
                "accountId":"123456789012",
                "userName": "SAMPLE_NAME"
                },
                "webIdFederationData": {},
                "attributes": {
                    "creationDate": "2022-10-11T17:25:41Z",
                    "mfaAuthenticated": "false"
                }
            }
        },
        "eventTime": "2022-10-11T17:30:18Z",
        "eventSource": "networkflowmonitor.amazonaws.com",
        "eventName": "ListMonitors",
        "awsRegion": "us-east-2",
        "sourceIPAddress": "192.0.2.0",
        "userAgent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)",
        "requestParameters": null,
        "responseElements": null,
        "requestID": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
        "eventID": "a1b2c3d4-5678-90ab-cdef-EXAMPLEbbbbb",
        "readOnly": true,
        "eventType": "AwsApiCall",
        "managementEvent": true,
        "recipientAccountId": "111122223333",
        "eventCategory": "Management"
    }
```

## Network Flow Monitor data plane
 events in CloudTrail


CloudTrail can capture API activities related to the CloudWatch-NetworkFlowMonitor data plane operations. 


[Data events](../../../awscloudtrail/latest/userguide/logging-data-events-with-cloudtrail.md#logging-data-events "../../../awscloudtrail/latest/userguide/logging-data-events-with-cloudtrail.md#logging-data-events"), also known as data plane operations, give you insight into the resource operations performed 
 on or within a resource. Data events are often high-volume activities.


To enable logging of Network Flow Monitor data events in CloudTrail files, you'll need to enable 
 the logging of data plane API activity in CloudTrail. See [Logging data events for trails](../../../awscloudtrail/latest/userguide/logging-data-events-with-cloudtrail.md "../../../awscloudtrail/latest/userguide/logging-data-events-with-cloudtrail.md") for more information.


Data plane events can be filtered by resource type. Because there are additional costs for using 
 data events in CloudTrail, filtering by resource allows you to have more control over what you log and pay for. 


Using the information that CloudTrail collects, you can identify a specific request to the CloudWatch-NetworkFlowMonitor 
 data plane APIs, the IP address of the requester, the requester's identity, and the date and time of the 
 request. Logging the data plane APIs using CloudTrail can help you with operational and 
 risk auditing, governance, and compliance of your AWS account.


The following are data plane APIs in Network Flow Monitor.



* [GetQueryResultsMonitorTopContributors](https://docs.aws.amazon.com/networkflowmonitor/2.0/APIReference/API_GetQueryResultsMonitorTopContributors.html "https://docs.aws.amazon.com/networkflowmonitor/2.0/APIReference/API_GetQueryResultsMonitorTopContributors.html")
* [GetQueryResultsMonitorsTopContributors](https://docs.aws.amazon.com/networkflowmonitor/2.0/APIReference/API_GetQueryResultsMonitorsTopContributors.html "https://docs.aws.amazon.com/networkflowmonitor/2.0/APIReference/API_GetQueryResultsMonitorsTopContributors.html")
* [GetQueryResultsWorkloadInsightsTopContributors](https://docs.aws.amazon.com/networkflowmonitor/2.0/APIReference/API_GetQueryResultsWorkloadInsightsTopContributors.html "https://docs.aws.amazon.com/networkflowmonitor/2.0/APIReference/API_GetQueryResultsWorkloadInsightsTopContributors.html")
* [GetQueryResultsWorkloadInsightsTopContributorsData](https://docs.aws.amazon.com/networkflowmonitor/2.0/APIReference/API_GetQueryResultsWorkloadInsightsTopContributorsData.html "https://docs.aws.amazon.com/networkflowmonitor/2.0/APIReference/API_GetQueryResultsWorkloadInsightsTopContributorsData.html")
* [GetQueryStatusMonitorTopContributors](https://docs.aws.amazon.com/networkflowmonitor/2.0/APIReference/API_GetQueryStatusMonitorTopContributors.html "https://docs.aws.amazon.com/networkflowmonitor/2.0/APIReference/API_GetQueryStatusMonitorTopContributors.html")
* [GetQueryStatusMonitorsTopContributors](https://docs.aws.amazon.com/networkflowmonitor/2.0/APIReference/API_GetQueryStatusMonitorsTopContributors.html "https://docs.aws.amazon.com/networkflowmonitor/2.0/APIReference/API_GetQueryStatusMonitorsTopContributors.html")
* [GetQueryStatusWorkloadInsightsTopContributors](https://docs.aws.amazon.com/networkflowmonitor/2.0/APIReference/API_GetQueryStatusWorkloadInsightsTopContributors.html "https://docs.aws.amazon.com/networkflowmonitor/2.0/APIReference/API_GetQueryStatusWorkloadInsightsTopContributors.html")
* [GetQueryStatusWorkloadInsightsTopContributorsData](https://docs.aws.amazon.com/networkflowmonitor/2.0/APIReference/API_GetQueryStatusWorkloadInsightsTopContributorsData.html "https://docs.aws.amazon.com/networkflowmonitor/2.0/APIReference/API_GetQueryStatusWorkloadInsightsTopContributorsData.html")
* [StartQueryMonitorTopContributors](https://docs.aws.amazon.com/networkflowmonitor/2.0/APIReference/API_StartQueryMonitorTopContributors.html "https://docs.aws.amazon.com/networkflowmonitor/2.0/APIReference/API_StartQueryMonitorTopContributors.html")
* [StartQueryMonitorsTopContributors](https://docs.aws.amazon.com/networkflowmonitor/2.0/APIReference/API_StartQueryMonitorsTopContributors.html "https://docs.aws.amazon.com/networkflowmonitor/2.0/APIReference/API_StartQueryMonitorsTopContributors.html")
* [StartQueryWorkloadInsightsTopContributors](https://docs.aws.amazon.com/networkflowmonitor/2.0/APIReference/API_StartQueryWorkloadInsightsTopContributors.html "https://docs.aws.amazon.com/networkflowmonitor/2.0/APIReference/API_StartQueryWorkloadInsightsTopContributors.html")
* [StartQueryWorkloadInsightsTopContributorsData](https://docs.aws.amazon.com/networkflowmonitor/2.0/APIReference/API_StartQueryWorkloadInsightsTopContributorsData.html "https://docs.aws.amazon.com/networkflowmonitor/2.0/APIReference/API_StartQueryWorkloadInsightsTopContributorsData.html")
* [StopQueryMonitorTopContributors](https://docs.aws.amazon.com/networkflowmonitor/2.0/APIReference/API_StopQueryMonitorTopContributors.html "https://docs.aws.amazon.com/networkflowmonitor/2.0/APIReference/API_StopQueryMonitorTopContributors.html")
* [StopQueryMonitorsTopContributors](https://docs.aws.amazon.com/networkflowmonitor/2.0/APIReference/API_StopQueryMonitorsTopContributors.html "https://docs.aws.amazon.com/networkflowmonitor/2.0/APIReference/API_StopQueryMonitorsTopContributors.html")
* [StopQueryWorkloadInsightsTopContributors](https://docs.aws.amazon.com/networkflowmonitor/2.0/APIReference/API_StopQueryWorkloadInsightsTopContributors.html "https://docs.aws.amazon.com/networkflowmonitor/2.0/APIReference/API_StopQueryWorkloadInsightsTopContributors.html")
* [StopQueryWorkloadInsightsTopContributorsData](https://docs.aws.amazon.com/networkflowmonitor/2.0/APIReference/API_StopQueryWorkloadInsightsTopContributorsData.html "https://docs.aws.amazon.com/networkflowmonitor/2.0/APIReference/API_StopQueryWorkloadInsightsTopContributorsData.html")

The following example shows a CloudTrail log entry that demonstrates the [GetQueryResultsMonitorsTopContributors](https://docs.aws.amazon.com/networkflowmonitor/2.0/APIReference/API_GetQueryResultsMonitorsTopContributors.html "https://docs.aws.amazon.com/networkflowmonitor/2.0/APIReference/API_GetQueryResultsMonitorsTopContributors.html") action.



```
{
  "eventVersion": "1.09",
  "userIdentity": {
    "type": "AssumedRole",
    "principalId": "EX_PRINCIPAL_ID",
    "arn": "arn:aws:iam::000000000000:assumed-role/role_name",
    "accountId": "123456789012",
    "accessKeyId": "AKIAIOSFODNN7EXAMPLE",
    "sessionContext": {
      "sessionIssuer": {
        "type": "Role",
        "principalId": "EX_PRINCIPAL_ID",
        "arn": "arn:aws:iam::000000000000:role/Admin",
        "accountId": "123456789012",
         "userName": "SAMPLE_NAME"
      },
      "attributes": {
      "creationDate": "2024-11-03T15:43:27Z",
      "mfaAuthenticated": "false"
      }
    }
},
  "eventTime": "2024-11-15T14:08:04Z",
  "eventSource": "networkflowmonitor.amazonaws.com",
  "eventName": "GetQueryResultsMonitorTopContributors",
  "awsRegion": "us-east-1",
  "sourceIPAddress": "192.0.2.0",
  "userAgent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)",
  "errorCode": "AccessDenied",
  "requestParameters": {
    "QueryId": "a1b2c3d4-5678-90ab-cdef-EXAMPLEQuery,
    "MaxResults": "20",
    "MonitorName": "TestMonitor"
  },
  "responseElements": null,
  "requestID": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
  "eventID": "a1b2c3d4-5678-90ab-cdef-EXAMPLEbbbbb",
  "readOnly": true,
  "resources": [
    {
      "accountId": "123456789012",
      "type": "AWS::NetworkFlowMonitor::Monitor",
      "ARN": "arn:aws:networkflowmonitor:us-east-1:123456789012:monitor/TestMonitor"
    }
  ],
  "eventType": "AwsApiCall",
  "managementEvent": false,
  "recipientAccountId": "000000000000",
  "eventCategory": "Data"
}
```

The following example shows a CloudTrail log entry that demonstrates the [GetQueryResultsWorkloadInsightsTopContributors](https://docs.aws.amazon.com/networkflowmonitor/2.0/APIReference/API_GetQueryResultsWorkloadInsightsTopContributors.html "https://docs.aws.amazon.com/networkflowmonitor/2.0/APIReference/API_GetQueryResultsWorkloadInsightsTopContributors.html") action.



```
{
  "eventVersion": "1.09",
  "userIdentity": {
    "type": "AssumedRole",
    "principalId": "EX_PRINCIPAL_ID",
    "arn": "arn:aws:iam::000000000000:assumed-role/role_name",
    "accountId": "123456789012",
    "accessKeyId": "AKIAIOSFODNN7EXAMPLE",
    "sessionContext": {
      "sessionIssuer": {
        "type": "Role",
        "principalId": "EX_PRINCIPAL_ID",
        "arn": "arn:aws:iam::000000000000:role/Admin",
        "accountId": "123456789012",
         "userName": "SAMPLE_NAME"
      },
      "attributes": {
      "creationDate": "2024-11-03T15:43:27Z",
      "mfaAuthenticated": "false"
      }
    }
},
  "eventTime": "2024-11-15T14:08:04Z",
  "eventSource": "networkflowmonitor.amazonaws.com",
  "eventName": "GetQueryResultsWorkloadInsightsTopContributorsData",
  "awsRegion": "us-east-1",
  "sourceIPAddress": "192.0.2.0",
  "userAgent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)",
  "errorCode": "AccessDenied",
  "requestParameters": {
    "QueryId": "a1b2c3d4-5678-90ab-cdef-EXAMPLEQuery",
    "ScopeId": "a1b2c3d4-5678-90ab-cdef-EXAMPLEScope"
  },
  "responseElements": null,
  "requestID": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
  "eventID": "a1b2c3d4-5678-90ab-cdef-EXAMPLEbbbbb",
  "readOnly": true,
  "resources": [
    {
      "accountId": "496383180932",
      "type": "AWS::NetworkFlowMonitor::Scope",
      "ARN": "arn:aws:networkflowmonitor:us-east-1:123456789012:scope/a1b2c3d4-5678-90ab-cdef-EXAMPLEScope"
    }
  ],
  "eventType": "AwsApiCall",
  "managementEvent": false,
  "recipientAccountId": "000000000000",
  "eventCategory": "Data"
}
```

## Internet Monitor in CloudTrail


Internet Monitor supports logging the following actions as events in CloudTrail log files.



* [CreateMonitor](https://docs.aws.amazon.com/internet-monitor/latest/api/API_CreateMonitor.html "https://docs.aws.amazon.com/internet-monitor/latest/api/API_CreateMonitor.html")
* [DeleteMonitor](https://docs.aws.amazon.com/internet-monitor/latest/api/API_DeleteMonitor.html "https://docs.aws.amazon.com/internet-monitor/latest/api/API_DeleteMonitor.html")
* [GetHealthEvent](https://docs.aws.amazon.com/internet-monitor/latest/api/API_GetHealthEvent.html "https://docs.aws.amazon.com/internet-monitor/latest/api/API_GetHealthEvent.html")
* [GetMonitor](https://docs.aws.amazon.com/internet-monitor/latest/api/API_GetMonitor.html "https://docs.aws.amazon.com/internet-monitor/latest/api/API_GetMonitor.html")
* [GetQueryResults](https://docs.aws.amazon.com/internet-monitor/latest/api/API_GetQueryResults.html "https://docs.aws.amazon.com/internet-monitor/latest/api/API_GetQueryResults.html")
* [GetQueryStatus](https://docs.aws.amazon.com/internet-monitor/latest/api/API_GetQueryStatus.html "https://docs.aws.amazon.com/internet-monitor/latest/api/API_GetQueryStatus.html")
* [ListHealthEvents](https://docs.aws.amazon.com/internet-monitor/latest/api/API_ListHealthEvents.html "https://docs.aws.amazon.com/internet-monitor/latest/api/API_ListHealthEvents.html")
* [ListInternetEvents](https://docs.aws.amazon.com/internet-monitor/latest/api/API_ListInternetEvents.html "https://docs.aws.amazon.com/internet-monitor/latest/api/API_ListInternetEvents.html")
* [ListMonitors](https://docs.aws.amazon.com/internet-monitor/latest/api/API_ListMonitors.html "https://docs.aws.amazon.com/internet-monitor/latest/api/API_ListMonitors.html")
* [ListTagsForResource](https://docs.aws.amazon.com/internet-monitor/latest/api/API_ListTagsForResource.html "https://docs.aws.amazon.com/internet-monitor/latest/api/API_ListTagsForResource.html")
* [StartQuery](https://docs.aws.amazon.com/internet-monitor/latest/api/API_StartQuery.html "https://docs.aws.amazon.com/internet-monitor/latest/api/API_StartQuery.html")
* [StopQuery](https://docs.aws.amazon.com/internet-monitor/latest/api/API_StopQuery.html "https://docs.aws.amazon.com/internet-monitor/latest/api/API_StopQuery.html")
* [TagResource](https://docs.aws.amazon.com/internet-monitor/latest/api/API_TagResource.html "https://docs.aws.amazon.com/internet-monitor/latest/api/API_TagResource.html")
* [UntagResource](https://docs.aws.amazon.com/internet-monitor/latest/api/API_UntagResource.html "https://docs.aws.amazon.com/internet-monitor/latest/api/API_UntagResource.html")
* [UpdateMonitor](https://docs.aws.amazon.com/internet-monitor/latest/api/API_UpdateMonitor.html "https://docs.aws.amazon.com/internet-monitor/latest/api/API_UpdateMonitor.html")

### Example: Internet Monitor
 log file entries


The following example shows a CloudTrail Internet Monitor log entry that demonstrates the 
 `ListMonitors` action.



```
{
        "eventVersion": "1.08",
        "userIdentity": {
            "type": "AssumedRole",
            "principalId": "EX_PRINCIPAL_ID",
            "arn": "arn:aws:iam::000000000000:assumed-role/role_name",
            "accountId":"123456789012",
            "accessKeyId":"AKIAIOSFODNN7EXAMPLE",
            "sessionContext": {
                "sessionIssuer": {
                "type": "Role",
                "principalId": "EX_PRINCIPAL_ID",
                "arn": "arn:aws:iam::000000000000:role/Admin",
                "accountId":"123456789012",
                "userName": "SAMPLE_NAME"
                },
                "webIdFederationData": {},
                "attributes": {
                    "creationDate": "2022-10-11T17:25:41Z",
                    "mfaAuthenticated": "false"
                }
            }
        },
        "eventTime": "2022-10-11T17:30:18Z",
        "eventSource": "internetmonitor.amazonaws.com",
        "eventName": "ListMonitors",
        "awsRegion": "us-east-2",
        "sourceIPAddress": "192.0.2.0",
        "userAgent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)",
        "requestParameters": null,
        "responseElements": null,
        "requestID": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
        "eventID": "a1b2c3d4-5678-90ab-cdef-EXAMPLEbbbbb",
        "readOnly": true,
        "eventType": "AwsApiCall",
        "managementEvent": true,
        "recipientAccountId": "111122223333",
        "eventCategory": "Management"
    }
```

The following example shows a CloudTrail Internet Monitor log entry that demonstrates the 
 `CreateMonitor` action.



```
{
        "eventVersion": "1.08",
        "userIdentity": {
            "type": "AssumedRole",
            "principalId": "EX_PRINCIPAL_ID",
            "arn": "arn:aws:iam::000000000000:assumed-role/role_name",
            "accountId":"123456789012",
            "accessKeyId":"AKIAIOSFODNN7EXAMPLE",
            "sessionContext": {
                "sessionIssuer": {
                "type": "Role",
                "principalId": "EX_PRINCIPAL_ID",
                "arn": "arn:aws:iam::000000000000:role/Admin",
                "accountId":"123456789012",
                "userName": "SAMPLE_NAME"
                },
                "webIdFederationData": {},
                "attributes": {
                    "creationDate": "2022-10-11T17:25:41Z",
                    "mfaAuthenticated": "false"
                }
            }
        },
        "eventTime": "2022-10-11T17:30:08Z",
        "eventSource": "internetmonitor.amazonaws.com",
        "eventName": "CreateMonitor",
        "awsRegion": "us-east-2",
        "sourceIPAddress": "192.0.2.0",
        "userAgent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)",
        "requestParameters": {
            "MonitorName": "TestMonitor",
            "Resources": ["arn:aws:ec2:us-east-2:444455556666:vpc/vpc-febc0b95"],
            "ClientToken": "a1b2c3d4-5678-90ab-cdef-EXAMPLE33333"
        },
        "responseElements": {
            "Arn": "arn:aws:internetmonitor:us-east-2:444455556666:monitor/ct-onboarding-test",
            "Status": "PENDING"
        },
        "requestID": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
        "eventID": "a1b2c3d4-5678-90ab-cdef-EXAMPLEbbbbb",
        "readOnly": false,
        "eventType": "AwsApiCall",
        "managementEvent": true,
        "recipientAccountId": "111122223333",
        "eventCategory": "Management"
    }
```

## CloudWatch Synthetics information in CloudTrail


CloudWatch Synthetics supports logging the following actions as events in CloudTrail log files:



* [AssociateResource](https://docs.aws.amazon.com/AmazonSynthetics/latest/APIReference/API_AssociateResource.html "https://docs.aws.amazon.com/AmazonSynthetics/latest/APIReference/API_AssociateResource.html")
* [CreateCanary](https://docs.aws.amazon.com/AmazonSynthetics/latest/APIReference/API_CreateCanary.html "https://docs.aws.amazon.com/AmazonSynthetics/latest/APIReference/API_CreateCanary.html")
* [CreateGroup](https://docs.aws.amazon.com/AmazonSynthetics/latest/APIReference/API_CreateGroup.html "https://docs.aws.amazon.com/AmazonSynthetics/latest/APIReference/API_CreateGroup.html")
* [DeleteCanary](https://docs.aws.amazon.com/AmazonSynthetics/latest/APIReference/API_DeleteCanary.html "https://docs.aws.amazon.com/AmazonSynthetics/latest/APIReference/API_DeleteCanary.html")
* [DeleteGroup](https://docs.aws.amazon.com/AmazonSynthetics/latest/APIReference/API_DeleteGroup.html "https://docs.aws.amazon.com/AmazonSynthetics/latest/APIReference/API_DeleteGroup.html")
* [DescribeCanaries](https://docs.aws.amazon.com/AmazonSynthetics/latest/APIReference/API_DescribeCanaries.html "https://docs.aws.amazon.com/AmazonSynthetics/latest/APIReference/API_DescribeCanaries.html")
* [DescribeCanariesLastRun](https://docs.aws.amazon.com/AmazonSynthetics/latest/APIReference/API_DescribeCanariesLastRun.html "https://docs.aws.amazon.com/AmazonSynthetics/latest/APIReference/API_DescribeCanariesLastRun.html")
* [DescribeRuntimeVersions](https://docs.aws.amazon.com/AmazonSynthetics/latest/APIReference/API_DescribeRuntimeVersions.html "https://docs.aws.amazon.com/AmazonSynthetics/latest/APIReference/API_DescribeRuntimeVersions.html")
* [DisassociateResource](https://docs.aws.amazon.com/AmazonSynthetics/latest/APIReference/API_DisassociateResource.html "https://docs.aws.amazon.com/AmazonSynthetics/latest/APIReference/API_DisassociateResource.html")
* [GetCanary](https://docs.aws.amazon.com/AmazonSynthetics/latest/APIReference/API_GetCanary.html "https://docs.aws.amazon.com/AmazonSynthetics/latest/APIReference/API_GetCanary.html")
* [GetCanaryRuns](https://docs.aws.amazon.com/AmazonSynthetics/latest/APIReference/API_GetCanaryRuns.html "https://docs.aws.amazon.com/AmazonSynthetics/latest/APIReference/API_GetCanaryRuns.html")
* [GetGroup](https://docs.aws.amazon.com/AmazonSynthetics/latest/APIReference/API_GetGroup.html "https://docs.aws.amazon.com/AmazonSynthetics/latest/APIReference/API_GetGroup.html")
* [ListAssociatedGroups](https://docs.aws.amazon.com/AmazonSynthetics/latest/APIReference/API_ListAssociatedGroups.html "https://docs.aws.amazon.com/AmazonSynthetics/latest/APIReference/API_ListAssociatedGroups.html")
* [ListGroupResources](https://docs.aws.amazon.com/AmazonSynthetics/latest/APIReference/API_ListGroupResources.html "https://docs.aws.amazon.com/AmazonSynthetics/latest/APIReference/API_ListGroupResources.html")
* [ListGroups](https://docs.aws.amazon.com/AmazonSynthetics/latest/APIReference/API_ListGroups.html "https://docs.aws.amazon.com/AmazonSynthetics/latest/APIReference/API_ListGroups.html")
* [ListTagsForResource](https://docs.aws.amazon.com/AmazonSynthetics/latest/APIReference/API_ListTagsForResource.html "https://docs.aws.amazon.com/AmazonSynthetics/latest/APIReference/API_ListTagsForResource.html")
* [StartCanary](https://docs.aws.amazon.com/AmazonSynthetics/latest/APIReference/API_StartCanary.html "https://docs.aws.amazon.com/AmazonSynthetics/latest/APIReference/API_StartCanary.html")
* [StartCanaryDryRun](https://docs.aws.amazon.com/AmazonSynthetics/latest/APIReference/API_StartCanaryDryRun.html "https://docs.aws.amazon.com/AmazonSynthetics/latest/APIReference/API_StartCanaryDryRun.html")
* [StopCanary](https://docs.aws.amazon.com/AmazonSynthetics/latest/APIReference/API_StopCanary.html "https://docs.aws.amazon.com/AmazonSynthetics/latest/APIReference/API_StopCanary.html")
* [TagResource](https://docs.aws.amazon.com/AmazonSynthetics/latest/APIReference/API_TagResource.html "https://docs.aws.amazon.com/AmazonSynthetics/latest/APIReference/API_TagResource.html")
* [UntagResource](https://docs.aws.amazon.com/AmazonSynthetics/latest/APIReference/API_UntagResource.html "https://docs.aws.amazon.com/AmazonSynthetics/latest/APIReference/API_UntagResource.html")
* [UpdateCanary](https://docs.aws.amazon.com/AmazonSynthetics/latest/APIReference/API_UpdateCanary.html "https://docs.aws.amazon.com/AmazonSynthetics/latest/APIReference/API_UpdateCanary.html")

### Example: CloudWatch Synthetics
 log file entries


The following example shows a CloudTrail Synthetics log entry that demonstrates the 
 `DescribeCanaries` action.



```
{
    "eventVersion": "1.05",
    "userIdentity": {
        "type": "AssumedRole",
        "principalId": "EX_PRINCIPAL_ID",
        "arn": "arn:aws:iam::123456789012:assumed-role/role_name",
        "accountId":"123456789012",
        "accessKeyId":"AKIAIOSFODNN7EXAMPLE",
        "sessionContext": {
            "sessionIssuer": {
                "type": "Role",
                "principalId": "EX_PRINCIPAL_ID",
                "arn": "arn:aws:iam::111222333444:role/Administrator",
                "accountId":"123456789012",
                "userName": "SAMPLE_NAME"
            },
            "webIdFederationData": {},
            "attributes": {
                "mfaAuthenticated": "false",
                "creationDate": "2020-04-08T21:43:24Z"
            }
        }
    },
    "eventTime": "2020-04-08T23:06:47Z",
    "eventSource": "synthetics.amazonaws.com",
    "eventName": "DescribeCanaries",
    "awsRegion": "us-east-1",
    "sourceIPAddress": "127.0.0.1",
    "userAgent": "aws-internal/3 aws-sdk-java/1.11.590 Linux/4.9.184-0.1.ac.235.83.329.metal1.x86_64 OpenJDK_64-Bit_Server_VM/25.212-b03 java/1.8.0_212 vendor/Oracle_Corporation",
    "requestParameters": null,
    "responseElements": null,
    "requestID": "201ed5f3-15db-4f87-94a4-123456789",
    "eventID": "73ddbd81-3dd0-4ada-b246-123456789",
    "readOnly": true,
    "eventType": "AwsApiCall",
    "recipientAccountId": "111122223333"
}
```

The following example shows a CloudTrail Synthetics log entry that demonstrates the 
 `UpdateCanary` action.



```
{
    "eventVersion": "1.05",
    "userIdentity": {
        "type": "AssumedRole",
        "principalId": "EX_PRINCIPAL_ID",
        "arn": "arn:aws:iam::123456789012:assumed-role/role_name",
        "accountId":"123456789012",
        "accessKeyId":"AKIAIOSFODNN7EXAMPLE",
        "sessionContext": {
            "sessionIssuer": {
               "type": "Role",
                "principalId": "EX_PRINCIPAL_ID",
                "arn": "arn:aws:iam::111222333444:role/Administrator",
       "accountId":"123456789012",
                "userName": "SAMPLE_NAME"
            },
            "webIdFederationData": {},
            "attributes": {
                "mfaAuthenticated": "false",
                "creationDate": "2020-04-08T21:43:24Z"
            }
        }
    },
    "eventTime": "2020-04-08T23:06:47Z",
    "eventSource": "synthetics.amazonaws.com",
    "eventName": "UpdateCanary",
    "awsRegion": "us-east-1",
    "sourceIPAddress": "192.0.2.0",
    "userAgent": "aws-internal/3 aws-sdk-java/1.11.590 Linux/4.9.184-0.1.ac.235.83.329.metal1.x86_64 OpenJDK_64-Bit_Server_VM/25.212-b03 java/1.8.0_212 vendor/Oracle_Corporation",
    "requestParameters": {
        "Schedule": {
            "Expression": "rate(1 minute)"
        },
        "name": "sample_canary_name",
        "Code": {
            "Handler": "myOwnScript.handler",
            "ZipFile": "SAMPLE_ZIP_FILE"
        }
    },
    "responseElements": null,
    "requestID": "fe4759b0-0849-4e0e-be71-1234567890",
    "eventID": "9dc60c83-c3c8-4fa5-bd02-1234567890",
    "readOnly": false,
    "eventType": "AwsApiCall",
    "recipientAccountId": "111122223333"
}
```

The following example shows a CloudTrail Synthetics log entry that demonstrates the 
 `GetCanaryRuns` action.



```
{
    "eventVersion": "1.05",
    "userIdentity": {
        "type": "AssumedRole",
        "principalId": "EX_PRINCIPAL_ID",
        "arn": "arn:aws:iam::123456789012:assumed-role/role_name",
        "accountId":"123456789012",
        "accessKeyId":"AKIAIOSFODNN7EXAMPLE",
        "sessionContext": {
            "sessionIssuer": {
                "type": "Role",
                "principalId": "EX_PRINCIPAL_ID",
                "arn": "arn:aws:iam::111222333444:role/Administrator",
       "accountId":"123456789012",
                "userName": "SAMPLE_NAME"
            },
            "webIdFederationData": {},
            "attributes": {
                "mfaAuthenticated": "false",
                "creationDate": "2020-04-08T21:43:24Z"
            }
        }
    },
    "eventTime": "2020-04-08T23:06:30Z",
    "eventSource": "synthetics.amazonaws.com",
    "eventName": "GetCanaryRuns",
    "awsRegion": "us-east-1",
    "sourceIPAddress": "127.0.0.1",
    "userAgent": "aws-internal/3 aws-sdk-java/1.11.590 Linux/4.9.184-0.1.ac.235.83.329.metal1.x86_64 OpenJDK_64-Bit_Server_VM/25.212-b03 java/1.8.0_212 vendor/Oracle_Corporation",
    "requestParameters": {
        "Filter": "TIME_RANGE",
        "name": "sample_canary_name",
        "FilterValues": [
            "2020-04-08T23:00:00.000Z",
            "2020-04-08T23:10:00.000Z"
        ]
    },
    "responseElements": null,
    "requestID": "2f56318c-cfbd-4b60-9d93-1234567890",
    "eventID": "52723fd9-4a54-478c-ac55-1234567890",
    "readOnly": true,
    "eventType": "AwsApiCall",
    "recipientAccountId": "111122223333"
}
```

## CloudWatch RUM information in CloudTrail


CloudWatch RUM supports logging the following actions as events in CloudTrail log files:



* [BatchCreateRumMetricDefinitions](https://docs.aws.amazon.com/cloudwatchrum/latest/APIReference/API_BatchCreateRumMetricDefinitions.html "https://docs.aws.amazon.com/cloudwatchrum/latest/APIReference/API_BatchCreateRumMetricDefinitions.html")
* [BatchDeleteRumMetricDefinitions](https://docs.aws.amazon.com/cloudwatchrum/latest/APIReference/API_BatchDeleteRumMetricDefinitions.html "https://docs.aws.amazon.com/cloudwatchrum/latest/APIReference/API_BatchDeleteRumMetricDefinitions.html")
* [BatchGetRumMetricDefinitions](https://docs.aws.amazon.com/cloudwatchrum/latest/APIReference/API_BatchGetRumMetricDefinitions.html "https://docs.aws.amazon.com/cloudwatchrum/latest/APIReference/API_BatchGetRumMetricDefinitions.html")
* [CreateAppMonitor](https://docs.aws.amazon.com/cloudwatchrum/latest/APIReference/API_CreateAppMonitor.html "https://docs.aws.amazon.com/cloudwatchrum/latest/APIReference/API_CreateAppMonitor.html")
* [DeleteAppMonitor](https://docs.aws.amazon.com/cloudwatchrum/latest/APIReference/API_DeleteAppMonitor.html "https://docs.aws.amazon.com/cloudwatchrum/latest/APIReference/API_DeleteAppMonitor.html")
* [DeleteResourcePolicy](https://docs.aws.amazon.com/cloudwatchrum/latest/APIReference/API_DeleteResourcePolicy.html "https://docs.aws.amazon.com/cloudwatchrum/latest/APIReference/API_DeleteResourcePolicy.html")
* [DeleteRumMetricsDestination](https://docs.aws.amazon.com/cloudwatchrum/latest/APIReference/API_DeleteRumMetricsDestination.html "https://docs.aws.amazon.com/cloudwatchrum/latest/APIReference/API_DeleteRumMetricsDestination.html")
* [GetAppMonitor](https://docs.aws.amazon.com/cloudwatchrum/latest/APIReference/API_GetAppMonitor.html "https://docs.aws.amazon.com/cloudwatchrum/latest/APIReference/API_GetAppMonitor.html")
* [GetAppMonitorData](https://docs.aws.amazon.com/cloudwatchrum/latest/APIReference/API_GetAppMonitorData.html "https://docs.aws.amazon.com/cloudwatchrum/latest/APIReference/API_GetAppMonitorData.html")
* [GetResourcePolicy](https://docs.aws.amazon.com/cloudwatchrum/latest/APIReference/API_GetResourcePolicy.html "https://docs.aws.amazon.com/cloudwatchrum/latest/APIReference/API_GetResourcePolicy.html")
* [ListAppMonitors](https://docs.aws.amazon.com/cloudwatchrum/latest/APIReference/API_ListAppMonitors.html "https://docs.aws.amazon.com/cloudwatchrum/latest/APIReference/API_ListAppMonitors.html")
* [ListRumMetricsDestinations](https://docs.aws.amazon.com/cloudwatchrum/latest/APIReference/API_ListRumMetricsDestinations.html "https://docs.aws.amazon.com/cloudwatchrum/latest/APIReference/API_ListRumMetricsDestinations.html")
* [ListTagsForResource](https://docs.aws.amazon.com/cloudwatchrum/latest/APIReference/API_ListTagsForResource.html "https://docs.aws.amazon.com/cloudwatchrum/latest/APIReference/API_ListTagsForResource.html")
* [PutResourcePolicy](https://docs.aws.amazon.com/cloudwatchrum/latest/APIReference/API_PutResourcePolicy.html "https://docs.aws.amazon.com/cloudwatchrum/latest/APIReference/API_PutResourcePolicy.html")
* [PutRumMetricsDestination](https://docs.aws.amazon.com/cloudwatchrum/latest/APIReference/API_PutRumMetricsDestination.html "https://docs.aws.amazon.com/cloudwatchrum/latest/APIReference/API_PutRumMetricsDestination.html")
* [TagResource](https://docs.aws.amazon.com/cloudwatchrum/latest/APIReference/API_TagResource.html "https://docs.aws.amazon.com/cloudwatchrum/latest/APIReference/API_TagResource.html")
* [UntagResource](https://docs.aws.amazon.com/cloudwatchrum/latest/APIReference/API_UntagResource.html "https://docs.aws.amazon.com/cloudwatchrum/latest/APIReference/API_UntagResource.html")
* [UpdateAppMonitor](https://docs.aws.amazon.com/cloudwatchrum/latest/APIReference/API_UpdateAppMonitor.html "https://docs.aws.amazon.com/cloudwatchrum/latest/APIReference/API_UpdateAppMonitor.html")
* [UpdateRumMetricDefinition](https://docs.aws.amazon.com/cloudwatchrum/latest/APIReference/API_UpdateRumMetricDefinition.html "https://docs.aws.amazon.com/cloudwatchrum/latest/APIReference/API_UpdateRumMetricDefinition.html")

### Example: CloudWatch RUM log file entries


This section contains example CloudTrail entries for some CloudWatch RUM APIs.


The following example shows a CloudTrail log entry that demonstrates the [CreateAppMonitor](https://docs.aws.amazon.com/cloudwatchrum/latest/APIReference/API_CreateAppMonitor.html "https://docs.aws.amazon.com/cloudwatchrum/latest/APIReference/API_CreateAppMonitor.html") action.



```
{
    "eventVersion": "1.09",
    "userIdentity": {
        "type": "AssumedRole",
        "principalId": "EXAMPLE_PRINCIPAL_ID",
        "arn": "arn:aws:sts::777777777777:assumed-role/EXAMPLE",
        "accountId": "777777777777",
        "accessKeyId": "AKIAIOSFODNN7EXAMPLE",
        "sessionContext": {
            "sessionIssuer": {
                "type": "Role",
                "principalId": "EXAMPLE_PRINCIPAL_ID",
                "arn": "arn:aws:iam::777777777777:role/EXAMPLE",
                "accountId": "777777777777",
                "userName": "USERNAME_EXAMPLE"
            },
            "attributes": {
                "creationDate": "2024-07-23T16:48:47Z",
                "mfaAuthenticated": "false"
            }
        }
    },
    "eventTime": "2024-07-23T18:02:57Z",
    "eventSource": "rum.amazonaws.com",
    "eventName": "CreateAppMonitor",
    "awsRegion": "us-east-1",
    "sourceIPAddress": "54.240.198.39",
    "userAgent": "aws-internal/3 aws-sdk-java/1.12.641 Linux/5.10.219-186.866.amzn2int.x86_64 OpenJDK_64-Bit_Server_VM/25.402-b08 java/1.8.0_402 vendor/Oracle_Corporation cfg/retry-mode/standard",
    "requestParameters": {
        "CustomEvents": {
            "Status": "ENABLED"
        },
        "CwLogEnabled": true,
        "Domain": "*.github.io",
        "AppMonitorConfiguration": {
            "SessionSampleRate": 1,
            "IncludedPages": [],
            "ExcludedPages": [],
            "Telemetries": [
                "performance",
                "errors",
                "http"
            ],
            "EnableXRay": false,
            "AllowCookies": true,
            "IdentityPoolId": "us-east-1:c81b9a1c-a5c9-4de5-8585-eb8df04e66f0"
        },
        "Tags": {
            "TestAppMonitor": ""
        },
        "Name": "TestAppMonitor"
    },
    "responseElements": {
        "Id": "65a8cc63-4ae8-4f2c-b5fc-4a54ef43af51"
    },
    "requestID": "cf7c30ad-25d3-4274-bab1-39c95a558007",
    "eventID": "2d43cc69-7f89-4f1a-95ae-0fc7e9b9fb3b",
    "readOnly": false,
    "eventType": "AwsApiCall",
    "managementEvent": true,
    "recipientAccountId": "777777777777",
    "eventCategory": "Management"
}
```

The following example shows a CloudTrail log entry that demonstrates the [PutRumMetricsDestination](https://docs.aws.amazon.com/cloudwatchrum/latest/APIReference/API_PutRumMetricsDestination.html "https://docs.aws.amazon.com/cloudwatchrum/latest/APIReference/API_PutRumMetricsDestination.html") action.



```
{
    "eventVersion": "1.09",
    "userIdentity": {
        "type": "AssumedRole",
        "principalId": "EXAMPLE_PRINCIPAL_ID",
        "arn": "arn:aws:sts::777777777777:assumed-role/EXAMPLE",
        "accountId": "777777777777",
        "accessKeyId": "AKIAIOSFODNN7EXAMPLE",
        "sessionContext": {
            "sessionIssuer": {
                "type": "Role",
                "principalId": "EXAMPLE_PRINCIPAL_ID",
                "arn": "arn:aws:iam::777777777777:role/EXAMPLE",
                "accountId": "777777777777",
                "userName": "USERNAME_EXAMPLE"
            },
            "attributes": {
                "creationDate": "2024-07-23T16:48:47Z",
                "mfaAuthenticated": "false"
            }
        }
    },
    "eventTime": "2024-07-23T18:22:22Z",
    "eventSource": "rum.amazonaws.com",
    "eventName": "PutRumMetricsDestination",
    "awsRegion": "us-east-1",
    "sourceIPAddress": "52.94.133.142",
    "userAgent": "aws-cli/2.13.25 Python/3.11.5 Linux/5.10.219-186.866.amzn2int.x86_64 exe/x86_64.amzn.2 prompt/off command/rum.put-rum-metrics-destination",
    "requestParameters": {
        "Destination": "CloudWatch",
        "AppMonitorName": "TestAppMonitor"
    },
    "responseElements": null,
    "requestID": "9b03fcce-b3a2-44fc-b771-900e1702998a",
    "eventID": "6250f9b7-0505-4f96-9668-feb64f82de5b",
    "readOnly": false,
    "eventType": "AwsApiCall",
    "managementEvent": true,
    "recipientAccountId": "777777777777",
    "eventCategory": "Management"
}
```

The following example shows a CloudTrail log entry that demonstrates the [BatchCreateRumMetricsDefinitions](https://docs.aws.amazon.com/cloudwatchrum/latest/APIReference/API_BatchCreateRumMetricsDefinitions.html "https://docs.aws.amazon.com/cloudwatchrum/latest/APIReference/API_BatchCreateRumMetricsDefinitions.html") action.



```
{
    "eventVersion": "1.09",
    "userIdentity": {
        "type": "AssumedRole",
        "principalId": "EXAMPLE_PRINCIPAL_ID",
        "arn": "arn:aws:sts::777777777777:assumed-role/EXAMPLE",
        "accountId": "777777777777",
        "accessKeyId": "AKIAIOSFODNN7EXAMPLE",
        "sessionContext": {
            "sessionIssuer": {
                "type": "Role",
                "principalId": "EXAMPLE_PRINCIPAL_ID",
                "arn": "arn:aws:iam::777777777777:role/EXAMPLE",
                "accountId": "777777777777",
                "userName": "USERNAME_EXAMPLE"
            },
            "attributes": {
                "creationDate": "2024-07-23T16:48:47Z",
                "mfaAuthenticated": "false"
            }
        }
    },
    "eventTime": "2024-07-23T18:23:11Z",
    "eventSource": "rum.amazonaws.com",
    "eventName": "BatchCreateRumMetricDefinitions",
    "awsRegion": "us-east-1",
    "sourceIPAddress": "52.94.133.142",
    "userAgent": "aws-cli/2.13.25 Python/3.11.5 Linux/5.10.219-186.866.amzn2int.x86_64 exe/x86_64.amzn.2 prompt/off command/rum.batch-create-rum-metric-definitions",
    "requestParameters": {
        "Destination": "CloudWatch",
        "MetricDefinitions": [
            {
                "Name": "NavigationToleratedTransaction",
                "Namespace": "AWS/RUM",
                "DimensionKeys": {
                    "metadata.browserName": "BrowserName"
                },
                "EventPattern": "{\"metadata\":{\"browserName\":[\"Chrome\"]},\"event_type\":[\"com.amazon.rum.performance_navigation_event\"],\"event_details\": {\"duration\": [{\"numeric\": [\"<=\",2000,\"<\",8000]}]}}"
            },
            {
                "Name": "HttpErrorCount",
                "DimensionKeys": {
                    "metadata.browserName": "BrowserName",
                    "metadata.countryCode": "CountryCode"
                },
                "EventPattern": "{\"metadata\":{\"browserName\":[\"Chrome\"], \"countryCode\":[\"US\"]},\"event_type\":[\"com.amazon.rum.http_event\"]}"
            }
        ],
        "AppMonitorName": "TestAppMonitor"
    },
    "responseElements": {
        "Errors": [],
        "MetricDefinitions": []
    },
    "requestID": "b14c5eda-f107-48e5-afae-1ac20d0962a8",
    "eventID": "001b55c6-1de1-48c0-a236-31096dffe249",
    "readOnly": false,
    "eventType": "AwsApiCall",
    "managementEvent": true,
    "recipientAccountId": "777777777777",
    "eventCategory": "Management"
}
```

## CloudWatch RUM data plane
 events in CloudTrail


CloudTrail can capture API activities related to the CloudWatch RUM data plane operation [PutRumEvents](https://docs.aws.amazon.com/cloudwatchrum/latest/APIReference/API_PutRumEvents.html "https://docs.aws.amazon.com/cloudwatchrum/latest/APIReference/API_PutRumEvents.html"). 


[Data events](../../../awscloudtrail/latest/userguide/logging-data-events-with-cloudtrail.md#logging-data-events "../../../awscloudtrail/latest/userguide/logging-data-events-with-cloudtrail.md#logging-data-events"), also known as data plane operations, give you insight into the resource operations performed 
 on or within a resource. Data events are often high-volume activities.


To enable logging of the **PutRumEvents** data events in CloudTrail files, you'll need to enable 
 the logging of data plane API activity in CloudTrail. See [Logging data events for trails](../../../awscloudtrail/latest/userguide/logging-data-events-with-cloudtrail.md "../../../awscloudtrail/latest/userguide/logging-data-events-with-cloudtrail.md") for more information.


Data plane events can be filtered by resource type. Because there are additional costs for using 
 data events in CloudTrail, filtering by resource allows you to have more control over what you log and pay for. 


Using the information that CloudTrail collects, you can identify a specific request to the CloudWatch RUM **PutRumEvents** API, the IP address of the requester, the requester's identity, and the date and time of the 
 request. Logging the **PutRumEvents** API using CloudTrail helps you enable operational and 
 risk auditing, governance, and compliance of your AWS account.


The following example shows a CloudTrail log entry that demonstrates the [PutRumEvents](https://docs.aws.amazon.com/cloudwatchrum/latest/APIReference/API_PutRumEvents.html "https://docs.aws.amazon.com/cloudwatchrum/latest/APIReference/API_PutRumEvents.html") action.



```
{
 "Records": [
     {
         "eventVersion": "1.09",
         "userIdentity": {
             "type": "AssumedRole",
             "principalId": "EXAMPLE_PRINCIPAL_ID",
             "arn": "arn:aws:sts::777777777777:assumed-role/EXAMPLE",
             "accountId": "777777777777",
             "accessKeyId": "AKIAIOSFODNN7EXAMPLE",
             "sessionContext": {
                 "sessionIssuer": {
                     "type": "Role",
                     "principalId": "EXAMPLE_PRINCIPAL_ID",
                     "arn": "arn:aws:iam::777777777777:role/EXAMPLE",
                     "accountId": "777777777777",
                     "userName": "USERNAME_EXAMPLE"
                 },
                 "attributes": {
                     "creationDate": "2024-05-16T20:32:39Z",
                     "mfaAuthenticated": "false"
                 }
             },
             "invokedBy": "AWS Internal"
         },
         "eventTime": "2024-05-16T20:32:42Z",
         "eventSource": "rum.amazonaws.com",
         "eventName": "PutRumEvents",
         "awsRegion": "us-east-1",
         "sourceIPAddress": "AWS Internal",
         "userAgent": "AWS Internal",
         "requestParameters": {
             "id": "73ddbd81-1234-5678-b246-123456789",
             "batchId": "123456-3dd0-4ada-b246-123456789",
             "appMonitorDetails": {
                 "name": "APP-MONITOR-NAME",
                 "id": "123456-3dd0-4ada-b246-123456789",
                 "version": "1.0.0"
             },
             "userDetails": {
                 "userId": "73ddbd81-1111-9999-b246-123456789",
                 "sessionId": "a1b2c3456-15db-4f87-6789-123456789"
             },
             "rumEvents": [
                 {
                     "id": "201f367a-15db-1234-94a4-123456789",
                     "timestamp": "May 16, 2024, 8:32:20 PM",
                     "type": "com.amazon.rum.dom_event",
                     "metadata": "{}",
                     "details": "{}"
                 }
             ]
         },
         "responseElements": null,
         "requestID": "201ed5f3-15db-4f87-94a4-123456789",
         "eventID": "73ddbd81-3dd0-4ada-b246-123456789",
         "readOnly": false,
         "resources": [
             {
                 "accountId": "777777777777",
                 "type": "AWS::RUM::AppMonitor",
                 "ARN": "arn:aws:rum:us-east-1:777777777777:appmonitor/APPMONITOR_NAME_EXAMPLE"
             }
         ],
         "eventType": "AwsApiCall",
         "managementEvent": false,
         "recipientAccountId": "777777777777",
         "eventCategory": "Data"
     }
 ]
}
```

## Network Synthetic Monitor information in CloudTrail


Network Synthetic Monitor supports logging the following actions as events in CloudTrail log files:



* [CreateMonitor](https://docs.aws.amazon.com/networkmonitor/latest/APIReference/API_CreateMonitor.html "https://docs.aws.amazon.com/networkmonitor/latest/APIReference/API_CreateMonitor.html")
* [CreateProbe](https://docs.aws.amazon.com/networkmonitor/latest/APIReference/API_CreateProbe.html "https://docs.aws.amazon.com/networkmonitor/latest/APIReference/API_CreateProbe.html")
* [DeleteMonitor](https://docs.aws.amazon.com/networkmonitor/latest/APIReference/API_DeleteMonitor.html "https://docs.aws.amazon.com/networkmonitor/latest/APIReference/API_DeleteMonitor.html")
* [DeleteProbe](https://docs.aws.amazon.com/networkmonitor/latest/APIReference/API_DeleteProbe.html "https://docs.aws.amazon.com/networkmonitor/latest/APIReference/API_DeleteProbe.html")
* [GetMonitor](https://docs.aws.amazon.com/networkmonitor/latest/APIReference/API_GetMonitor.html "https://docs.aws.amazon.com/networkmonitor/latest/APIReference/API_GetMonitor.html")
* [GetProbe](https://docs.aws.amazon.com/networkmonitor/latest/APIReference/API_GetProbe.html "https://docs.aws.amazon.com/networkmonitor/latest/APIReference/API_GetProbe.html")
* [ListMonitors](https://docs.aws.amazon.com/networkmonitor/latest/APIReference/API_ListMonitors.html "https://docs.aws.amazon.com/networkmonitor/latest/APIReference/API_ListMonitors.html")
* [ListTagsForResource](https://docs.aws.amazon.com/networkmonitor/latest/APIReference/API_ListTagsForResource.html "https://docs.aws.amazon.com/networkmonitor/latest/APIReference/API_ListTagsForResource.html")
* [TagResource](https://docs.aws.amazon.com/networkmonitor/latest/APIReference/API_TagResource.html "https://docs.aws.amazon.com/networkmonitor/latest/APIReference/API_TagResource.html")
* [UntagResource](https://docs.aws.amazon.com/networkmonitor/latest/APIReference/API_UntagResource.html "https://docs.aws.amazon.com/networkmonitor/latest/APIReference/API_UntagResource.html")
* [UpdateMonitor](https://docs.aws.amazon.com/networkmonitor/latest/APIReference/API_UpdateMonitor.html "https://docs.aws.amazon.com/networkmonitor/latest/APIReference/API_UpdateMonitor.html")
* [UpdateProbe](https://docs.aws.amazon.com/networkmonitor/latest/APIReference/API_UpdateProbe.html "https://docs.aws.amazon.com/networkmonitor/latest/APIReference/API_UpdateProbe.html")

### Example: Network Synthetic Monitor log file entries


The following example shows a Network Synthetic Monitor CloudTrail log entry that demonstrates the 
 `CreateMonitor` action.



```
{
    "eventVersion": "1.09",
    "userIdentity": {
        "type": "AssumedRole",
        "principalId": "EX_PRINCIPAL_ID",
        "arn": "arn:aws:iam::111122223333:assumed-role/role_name",
        "accountId": "111122223333",
        "accessKeyId": "AKIAIOSFODNN7EXAMPLE",
        "sessionContext": {
            "sessionIssuer": {
                "type": "Role",
                "principalId": "EX_PRINCIPAL_ID",
                "arn": "arn:aws:iam::111122223333:role/Admin",
                "accountId": "111122223333",
                "userName": "SAMPLE_NAME"
            },
            "attributes": {
                "creationDate": "2024-11-03T15:43:27Z",
                "mfaAuthenticated": "false"
            }
        }
    },
    "eventTime": "2024-11-03T15:58:11Z",
    "eventSource": "networksynthetics.amazonaws.com",
    "eventName": "CreateMonitor",
    "awsRegion": "us-east-1",
    "sourceIPAddress": "192.0.2.0",
    "userAgent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)",
    "requestParameters": {
        "MonitorName": "TestNetworkSyntheticMonitor",
        "ClientToken": "33551db7-1618-4aab-cdef-EXAMPLE33333"
    },
    "responseElements": {
        "MonitorArn": "arn:aws:networksynthetics:us-east-1:111122223333:monitor/TestNetworkSyntheticMonitor",
        "MonitorName": "TestNetworkSyntheticMonitor",
        "MonitorStatus": "ACTIVE"
    },
    "requestID": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
    "eventID": "a1b2c3d4-5678-90ab-cdef-EXAMPLEbbbbb",
    "readOnly": false,
    "eventType": "AwsApiCall",
    "managementEvent": true,
    "recipientAccountId": "111122223333",
    "eventCategory": "Management"
}
```

## CloudWatch Observability Access Manager information in CloudTrail


CloudWatch Observability Access Manager supports logging the following actions as events in CloudTrail log files:



* [CreateLink](https://docs.aws.amazon.com/OAM/latest/APIReference/API_CreateLink.html "https://docs.aws.amazon.com/OAM/latest/APIReference/API_CreateLink.html")
* [CreateSink](https://docs.aws.amazon.com/OAM/latest/APIReference/API_CreateSink.html "https://docs.aws.amazon.com/OAM/latest/APIReference/API_CreateSink.html")
* [DeleteLink](https://docs.aws.amazon.com/OAM/latest/APIReference/API_DeleteLink.html "https://docs.aws.amazon.com/OAM/latest/APIReference/API_DeleteLink.html")
* [DeleteSink](https://docs.aws.amazon.com/OAM/latest/APIReference/API_DeleteSink.html "https://docs.aws.amazon.com/OAM/latest/APIReference/API_DeleteSink.html")
* [GetLink](https://docs.aws.amazon.com/OAM/latest/APIReference/API_GetLink.html "https://docs.aws.amazon.com/OAM/latest/APIReference/API_GetLink.html")
* [GetSink](https://docs.aws.amazon.com/OAM/latest/APIReference/API_GetSink.html "https://docs.aws.amazon.com/OAM/latest/APIReference/API_GetSink.html")
* [GetSinkPolicy](https://docs.aws.amazon.com/OAM/latest/APIReference/API_GetSinkPolicy.html "https://docs.aws.amazon.com/OAM/latest/APIReference/API_GetSinkPolicy.html")
* [ListAttachedLinks](https://docs.aws.amazon.com/OAM/latest/APIReference/API_ListAttachedLinks.html "https://docs.aws.amazon.com/OAM/latest/APIReference/API_ListAttachedLinks.html")
* [ListLinks](https://docs.aws.amazon.com/OAM/latest/APIReference/API_ListLinks.html "https://docs.aws.amazon.com/OAM/latest/APIReference/API_ListLinks.html")
* [ListSinks](https://docs.aws.amazon.com/OAM/latest/APIReference/API_ListSinks.html "https://docs.aws.amazon.com/OAM/latest/APIReference/API_ListSinks.html")
* [ListTagsForResource](https://docs.aws.amazon.com/OAM/latest/APIReference/API_ListTagsForResource.html "https://docs.aws.amazon.com/OAM/latest/APIReference/API_ListTagsForResource.html")
* [PutSinkPolicy](https://docs.aws.amazon.com/OAM/latest/APIReference/API_PutSinkPolicy.html "https://docs.aws.amazon.com/OAM/latest/APIReference/API_PutSinkPolicy.html")
* [TagResource](https://docs.aws.amazon.com/OAM/latest/APIReference/API_TagResource.html "https://docs.aws.amazon.com/OAM/latest/APIReference/API_TagResource.html")
* [UntagResource](https://docs.aws.amazon.com/OAM/latest/APIReference/API_UntagResource.html "https://docs.aws.amazon.com/OAM/latest/APIReference/API_UntagResource.html")
* [UpdateLink](https://docs.aws.amazon.com/OAM/latest/APIReference/API_UpdateLink.html "https://docs.aws.amazon.com/OAM/latest/APIReference/API_UpdateLink.html")

### Example: CloudWatch Observability Access Manager log file entries


The following example shows a CloudWatch Observability Access Manager CloudTrail log entry that demonstrates the 
 `CreateSink` action.



```
{
    "eventVersion": "1.09",
    "userIdentity": {
        "type": "AssumedRole",
        "principalId": "EX_PRINCIPAL_ID",
        "arn": "arn:aws:iam::111122223333:assumed-role/role_name",
        "accountId": "111122223333",
        "accessKeyId": "AKIAIOSFODNN7EXAMPLE",
        "sessionContext": {
            "sessionIssuer": {
                "type": "Role",
                "principalId": "EX_PRINCIPAL_ID",
                "arn": "arn:aws:iam::111122223333:role/Admin",
                "accountId": "111122223333",
                "userName": "SAMPLE_NAME"
            },
            "attributes": {
                "creationDate": "2024-11-03T15:43:27Z",
                "mfaAuthenticated": "false"
            }
        }
    },
    "eventTime": "2024-11-03T15:58:11Z",
    "eventSource": "oam.amazonaws.com",
    "eventName": "CreateSink",
    "awsRegion": "us-east-1",
    "sourceIPAddress": "192.0.2.0",
    "userAgent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)",
    "requestParameters": {
        "Name": "TestObservabilitySink"
    },
    "responseElements": {
        "Arn": "arn:aws:oam:us-east-1:111122223333:sink/TestObservabilitySink",
        "Id": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
        "Name": "TestObservabilitySink"
    },
    "requestID": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
    "eventID": "a1b2c3d4-5678-90ab-cdef-EXAMPLEbbbbb",
    "readOnly": false,
    "eventType": "AwsApiCall",
    "managementEvent": true,
    "recipientAccountId": "111122223333",
    "eventCategory": "Management"
}
```

## CloudWatch Observability Admin information in CloudTrail


CloudWatch Observability Admin supports logging the following actions as events in CloudTrail log files:



* [GetTelemetryEvaluationStatus](https://docs.aws.amazon.com/cloudwatch/latest/observabilityadmin/API_GetTelemetryEvaluationStatus.html "https://docs.aws.amazon.com/cloudwatch/latest/observabilityadmin/API_GetTelemetryEvaluationStatus.html")
* [GetTelemetryEvaluationStatusForOrganization](https://docs.aws.amazon.com/cloudwatch/latest/observabilityadmin/API_GetTelemetryEvaluationStatusForOrganization.html "https://docs.aws.amazon.com/cloudwatch/latest/observabilityadmin/API_GetTelemetryEvaluationStatusForOrganization.html")
* [ListResourceTelemetry](https://docs.aws.amazon.com/cloudwatch/latest/observabilityadmin/API_ListResourceTelemetry.html "https://docs.aws.amazon.com/cloudwatch/latest/observabilityadmin/API_ListResourceTelemetry.html")
* [ListResourceTelemetryForOrganization](https://docs.aws.amazon.com/cloudwatch/latest/observabilityadmin/API_ListResourceTelemetryForOrganization.html "https://docs.aws.amazon.com/cloudwatch/latest/observabilityadmin/API_ListResourceTelemetryForOrganization.html")
* [StartTelemetryEvaluation](https://docs.aws.amazon.com/cloudwatch/latest/observabilityadmin/API_StartTelemetryEvaluation.html "https://docs.aws.amazon.com/cloudwatch/latest/observabilityadmin/API_StartTelemetryEvaluation.html")
* [StartTelemetryEvaluationForOrganization](https://docs.aws.amazon.com/cloudwatch/latest/observabilityadmin/API_StartTelemetryEvaluationForOrganization.html "https://docs.aws.amazon.com/cloudwatch/latest/observabilityadmin/API_StartTelemetryEvaluationForOrganization.html")
* [StopTelemetryEvaluation](https://docs.aws.amazon.com/cloudwatch/latest/observabilityadmin/API_StopTelemetryEvaluation.html "https://docs.aws.amazon.com/cloudwatch/latest/observabilityadmin/API_StopTelemetryEvaluation.html")
* [StopTelemetryEvaluationForOrganization](https://docs.aws.amazon.com/cloudwatch/latest/observabilityadmin/API_StopTelemetryEvaluationForOrganization.html "https://docs.aws.amazon.com/cloudwatch/latest/observabilityadmin/API_StopTelemetryEvaluationForOrganization.html")

### Example: CloudWatch Observability Admin log file entries


The following example shows a CloudWatch Observability Admin CloudTrail log entry that demonstrates the 
 `StartTelemetryEvaluation` action.



```
{
    "eventVersion": "1.09",
    "userIdentity": {
        "type": "AssumedRole",
        "principalId": "EX_PRINCIPAL_ID",
        "arn": "arn:aws:iam::111122223333:assumed-role/role_name",
        "accountId": "111122223333",
        "accessKeyId": "AKIAIOSFODNN7EXAMPLE",
        "sessionContext": {
            "sessionIssuer": {
                "type": "Role",
                "principalId": "EX_PRINCIPAL_ID",
                "arn": "arn:aws:iam::111122223333:role/Admin",
                "accountId": "111122223333",
                "userName": "SAMPLE_NAME"
            },
            "attributes": {
                "creationDate": "2024-11-03T15:43:27Z",
                "mfaAuthenticated": "false"
            }
        }
    },
    "eventTime": "2024-11-03T15:58:11Z",
    "eventSource": "observabilityadmin.amazonaws.com",
    "eventName": "StartTelemetryEvaluation",
    "awsRegion": "us-east-1",
    "sourceIPAddress": "192.0.2.0",
    "userAgent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)",
    "requestParameters": {},
    "responseElements": null,
    "requestID": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
    "eventID": "a1b2c3d4-5678-90ab-cdef-EXAMPLEbbbbb",
    "readOnly": false,
    "eventType": "AwsApiCall",
    "managementEvent": true,
    "recipientAccountId": "111122223333",
    "eventCategory": "Management"
}
```

## CloudWatch Application Signals information in CloudTrail


CloudWatch Application Signals supports logging the following actions as events in CloudTrail log files:



* [BatchGetServiceLevelObjectiveBudgetReport](https://docs.aws.amazon.com/applicationsignals/latest/APIReference/API_BatchGetServiceLevelObjectiveBudgetReport.html "https://docs.aws.amazon.com/applicationsignals/latest/APIReference/API_BatchGetServiceLevelObjectiveBudgetReport.html")
* [BatchUpdateExclusionWindows](https://docs.aws.amazon.com/applicationsignals/latest/APIReference/API_BatchUpdateExclusionWindows.html "https://docs.aws.amazon.com/applicationsignals/latest/APIReference/API_BatchUpdateExclusionWindows.html")
* [CreateServiceLevelObjective](https://docs.aws.amazon.com/applicationsignals/latest/APIReference/API_CreateServiceLevelObjective.html "https://docs.aws.amazon.com/applicationsignals/latest/APIReference/API_CreateServiceLevelObjective.html")
* [DeleteServiceLevelObjective](https://docs.aws.amazon.com/applicationsignals/latest/APIReference/API_DeleteServiceLevelObjective.html "https://docs.aws.amazon.com/applicationsignals/latest/APIReference/API_DeleteServiceLevelObjective.html")
* [GetService](https://docs.aws.amazon.com/applicationsignals/latest/APIReference/API_GetService.html "https://docs.aws.amazon.com/applicationsignals/latest/APIReference/API_GetService.html")
* [GetServiceLevelObjective](https://docs.aws.amazon.com/applicationsignals/latest/APIReference/API_GetServiceLevelObjective.html "https://docs.aws.amazon.com/applicationsignals/latest/APIReference/API_GetServiceLevelObjective.html")
* [ListServiceDependencies](https://docs.aws.amazon.com/applicationsignals/latest/APIReference/API_ListServiceDependencies.html "https://docs.aws.amazon.com/applicationsignals/latest/APIReference/API_ListServiceDependencies.html")
* [ListServiceDependents](https://docs.aws.amazon.com/applicationsignals/latest/APIReference/API_ListServiceDependents.html "https://docs.aws.amazon.com/applicationsignals/latest/APIReference/API_ListServiceDependents.html")
* [ListServiceLevelObjectives](https://docs.aws.amazon.com/applicationsignals/latest/APIReference/API_ListServiceLevelObjectives.html "https://docs.aws.amazon.com/applicationsignals/latest/APIReference/API_ListServiceLevelObjectives.html")
* [ListServiceOperations](https://docs.aws.amazon.com/applicationsignals/latest/APIReference/API_ListServiceOperations.html "https://docs.aws.amazon.com/applicationsignals/latest/APIReference/API_ListServiceOperations.html")
* [ListServices](https://docs.aws.amazon.com/applicationsignals/latest/APIReference/API_ListServices.html "https://docs.aws.amazon.com/applicationsignals/latest/APIReference/API_ListServices.html")
* [ListTagsForResource](https://docs.aws.amazon.com/applicationsignals/latest/APIReference/API_ListTagsForResource.html "https://docs.aws.amazon.com/applicationsignals/latest/APIReference/API_ListTagsForResource.html")
* [StartDiscovery](https://docs.aws.amazon.com/applicationsignals/latest/APIReference/API_StartDiscovery.html "https://docs.aws.amazon.com/applicationsignals/latest/APIReference/API_StartDiscovery.html")
* [TagResource](https://docs.aws.amazon.com/applicationsignals/latest/APIReference/API_TagResource.html "https://docs.aws.amazon.com/applicationsignals/latest/APIReference/API_TagResource.html")
* [UntagResource](https://docs.aws.amazon.com/applicationsignals/latest/APIReference/API_UntagResource.html "https://docs.aws.amazon.com/applicationsignals/latest/APIReference/API_UntagResource.html")
* [UpdateServiceLevelObjective](https://docs.aws.amazon.com/applicationsignals/latest/APIReference/API_UpdateServiceLevelObjective.html "https://docs.aws.amazon.com/applicationsignals/latest/APIReference/API_UpdateServiceLevelObjective.html")

### Example: CloudWatch Application Signals log file entries


The following example shows a CloudWatch Application Signals CloudTrail log entry that demonstrates the 
 `CreateServiceLevelObjective` action.



```
{
    "eventVersion": "1.09",
    "userIdentity": {
        "type": "AssumedRole",
        "principalId": "EX_PRINCIPAL_ID",
        "arn": "arn:aws:iam::111122223333:assumed-role/role_name",
        "accountId": "111122223333",
        "accessKeyId": "AKIAIOSFODNN7EXAMPLE",
        "sessionContext": {
            "sessionIssuer": {
                "type": "Role",
                "principalId": "EX_PRINCIPAL_ID",
                "arn": "arn:aws:iam::111122223333:role/Admin",
                "accountId": "111122223333",
                "userName": "SAMPLE_NAME"
            },
            "attributes": {
                "creationDate": "2024-11-03T15:43:27Z",
                "mfaAuthenticated": "false"
            }
        }
    },
    "eventTime": "2024-11-03T15:58:11Z",
    "eventSource": "applicationsignals.amazonaws.com",
    "eventName": "CreateServiceLevelObjective",
    "awsRegion": "us-east-1",
    "sourceIPAddress": "192.0.2.0",
    "userAgent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)",
    "requestParameters": {
        "Name": "TestSLO",
        "Description": "Test Service Level Objective"
    },
    "responseElements": {
        "Arn": "arn:aws:applicationsignals:us-east-1:111122223333:slo/TestSLO"
    },
    "requestID": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
    "eventID": "a1b2c3d4-5678-90ab-cdef-EXAMPLEbbbbb",
    "readOnly": false,
    "eventType": "AwsApiCall",
    "managementEvent": true,
    "recipientAccountId": "111122223333",
    "eventCategory": "Management"
}
```

## CloudWatch Application Insights information in CloudTrail


CloudWatch Application Insights supports logging the following actions as events in CloudTrail log files:



* [AddWorkload](https://docs.aws.amazon.com/cloudwatch/latest/APIReference/API_AddWorkload.html "https://docs.aws.amazon.com/cloudwatch/latest/APIReference/API_AddWorkload.html")
* [CreateApplication](https://docs.aws.amazon.com/cloudwatch/latest/APIReference/API_CreateApplication.html "https://docs.aws.amazon.com/cloudwatch/latest/APIReference/API_CreateApplication.html")
* [CreateComponent](https://docs.aws.amazon.com/cloudwatch/latest/APIReference/API_CreateComponent.html "https://docs.aws.amazon.com/cloudwatch/latest/APIReference/API_CreateComponent.html")
* [CreateLogPattern](https://docs.aws.amazon.com/cloudwatch/latest/APIReference/API_CreateLogPattern.html "https://docs.aws.amazon.com/cloudwatch/latest/APIReference/API_CreateLogPattern.html")
* [DeleteApplication](https://docs.aws.amazon.com/cloudwatch/latest/APIReference/API_DeleteApplication.html "https://docs.aws.amazon.com/cloudwatch/latest/APIReference/API_DeleteApplication.html")
* [DeleteComponent](https://docs.aws.amazon.com/cloudwatch/latest/APIReference/API_DeleteComponent.html "https://docs.aws.amazon.com/cloudwatch/latest/APIReference/API_DeleteComponent.html")
* [DeleteLogPattern](https://docs.aws.amazon.com/cloudwatch/latest/APIReference/API_DeleteLogPattern.html "https://docs.aws.amazon.com/cloudwatch/latest/APIReference/API_DeleteLogPattern.html")
* [DescribeApplication](https://docs.aws.amazon.com/cloudwatch/latest/APIReference/API_DescribeApplication.html "https://docs.aws.amazon.com/cloudwatch/latest/APIReference/API_DescribeApplication.html")
* [DescribeComponent](https://docs.aws.amazon.com/cloudwatch/latest/APIReference/API_DescribeComponent.html "https://docs.aws.amazon.com/cloudwatch/latest/APIReference/API_DescribeComponent.html")
* [DescribeComponentConfiguration](https://docs.aws.amazon.com/cloudwatch/latest/APIReference/API_DescribeComponentConfiguration.html "https://docs.aws.amazon.com/cloudwatch/latest/APIReference/API_DescribeComponentConfiguration.html")
* [DescribeComponentConfigurationRecommendation](https://docs.aws.amazon.com/cloudwatch/latest/APIReference/API_DescribeComponentConfigurationRecommendation.html "https://docs.aws.amazon.com/cloudwatch/latest/APIReference/API_DescribeComponentConfigurationRecommendation.html")
* [DescribeLogPattern](https://docs.aws.amazon.com/cloudwatch/latest/APIReference/API_DescribeLogPattern.html "https://docs.aws.amazon.com/cloudwatch/latest/APIReference/API_DescribeLogPattern.html")
* [DescribeObservation](https://docs.aws.amazon.com/cloudwatch/latest/APIReference/API_DescribeObservation.html "https://docs.aws.amazon.com/cloudwatch/latest/APIReference/API_DescribeObservation.html")
* [DescribeProblem](https://docs.aws.amazon.com/cloudwatch/latest/APIReference/API_DescribeProblem.html "https://docs.aws.amazon.com/cloudwatch/latest/APIReference/API_DescribeProblem.html")
* [DescribeProblemObservations](https://docs.aws.amazon.com/cloudwatch/latest/APIReference/API_DescribeProblemObservations.html "https://docs.aws.amazon.com/cloudwatch/latest/APIReference/API_DescribeProblemObservations.html")
* [DescribeWorkload](https://docs.aws.amazon.com/cloudwatch/latest/APIReference/API_DescribeWorkload.html "https://docs.aws.amazon.com/cloudwatch/latest/APIReference/API_DescribeWorkload.html")
* [ListApplications](https://docs.aws.amazon.com/cloudwatch/latest/APIReference/API_ListApplications.html "https://docs.aws.amazon.com/cloudwatch/latest/APIReference/API_ListApplications.html")
* [ListComponents](https://docs.aws.amazon.com/cloudwatch/latest/APIReference/API_ListComponents.html "https://docs.aws.amazon.com/cloudwatch/latest/APIReference/API_ListComponents.html")
* [ListConfigurationHistory](https://docs.aws.amazon.com/cloudwatch/latest/APIReference/API_ListConfigurationHistory.html "https://docs.aws.amazon.com/cloudwatch/latest/APIReference/API_ListConfigurationHistory.html")
* [ListLogPatterns](https://docs.aws.amazon.com/cloudwatch/latest/APIReference/API_ListLogPatterns.html "https://docs.aws.amazon.com/cloudwatch/latest/APIReference/API_ListLogPatterns.html")
* [ListLogPatternSets](https://docs.aws.amazon.com/cloudwatch/latest/APIReference/API_ListLogPatternSets.html "https://docs.aws.amazon.com/cloudwatch/latest/APIReference/API_ListLogPatternSets.html")
* [ListProblems](https://docs.aws.amazon.com/cloudwatch/latest/APIReference/API_ListProblems.html "https://docs.aws.amazon.com/cloudwatch/latest/APIReference/API_ListProblems.html")
* [ListTagsForResource](https://docs.aws.amazon.com/cloudwatch/latest/APIReference/API_ListTagsForResource.html "https://docs.aws.amazon.com/cloudwatch/latest/APIReference/API_ListTagsForResource.html")
* [ListWorkloads](https://docs.aws.amazon.com/cloudwatch/latest/APIReference/API_ListWorkloads.html "https://docs.aws.amazon.com/cloudwatch/latest/APIReference/API_ListWorkloads.html")
* [RemoveWorkload](https://docs.aws.amazon.com/cloudwatch/latest/APIReference/API_RemoveWorkload.html "https://docs.aws.amazon.com/cloudwatch/latest/APIReference/API_RemoveWorkload.html")
* [TagResource](https://docs.aws.amazon.com/cloudwatch/latest/APIReference/API_TagResource.html "https://docs.aws.amazon.com/cloudwatch/latest/APIReference/API_TagResource.html")
* [UntagResource](https://docs.aws.amazon.com/cloudwatch/latest/APIReference/API_UntagResource.html "https://docs.aws.amazon.com/cloudwatch/latest/APIReference/API_UntagResource.html")
* [UpdateApplication](https://docs.aws.amazon.com/cloudwatch/latest/APIReference/API_UpdateApplication.html "https://docs.aws.amazon.com/cloudwatch/latest/APIReference/API_UpdateApplication.html")
* [UpdateComponent](https://docs.aws.amazon.com/cloudwatch/latest/APIReference/API_UpdateComponent.html "https://docs.aws.amazon.com/cloudwatch/latest/APIReference/API_UpdateComponent.html")
* [UpdateComponentConfiguration](https://docs.aws.amazon.com/cloudwatch/latest/APIReference/API_UpdateComponentConfiguration.html "https://docs.aws.amazon.com/cloudwatch/latest/APIReference/API_UpdateComponentConfiguration.html")
* [UpdateLogPattern](https://docs.aws.amazon.com/cloudwatch/latest/APIReference/API_UpdateLogPattern.html "https://docs.aws.amazon.com/cloudwatch/latest/APIReference/API_UpdateLogPattern.html")
* [UpdateProblem](https://docs.aws.amazon.com/cloudwatch/latest/APIReference/API_UpdateProblem.html "https://docs.aws.amazon.com/cloudwatch/latest/APIReference/API_UpdateProblem.html")
* [UpdateWorkload](https://docs.aws.amazon.com/cloudwatch/latest/APIReference/API_UpdateWorkload.html "https://docs.aws.amazon.com/cloudwatch/latest/APIReference/API_UpdateWorkload.html")

### Example: CloudWatch Application Insights log file entries


The following example shows a CloudWatch Application Insights CloudTrail log entry that demonstrates the 
 `CreateApplication` action.



```
{
    "eventVersion": "1.09",
    "userIdentity": {
        "type": "AssumedRole",
        "principalId": "EX_PRINCIPAL_ID",
        "arn": "arn:aws:iam::111122223333:assumed-role/role_name",
        "accountId": "111122223333",
        "accessKeyId": "AKIAIOSFODNN7EXAMPLE",
        "sessionContext": {
            "sessionIssuer": {
                "type": "Role",
                "principalId": "EX_PRINCIPAL_ID",
                "arn": "arn:aws:iam::111122223333:role/Admin",
                "accountId": "111122223333",
                "userName": "SAMPLE_NAME"
            },
            "attributes": {
                "creationDate": "2024-11-03T15:43:27Z",
                "mfaAuthenticated": "false"
            }
        }
    },
    "eventTime": "2024-11-03T15:58:11Z",
    "eventSource": "applicationinsights.amazonaws.com",
    "eventName": "CreateApplication",
    "awsRegion": "us-east-1",
    "sourceIPAddress": "192.0.2.0",
    "userAgent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)",
    "requestParameters": {
        "ResourceGroupName": "TestApplicationResourceGroup"
    },
    "responseElements": {
        "ApplicationInfo": {
            "ResourceGroupName": "TestApplicationResourceGroup",
            "LifeCycle": "ACTIVE"
        }
    },
    "requestID": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
    "eventID": "a1b2c3d4-5678-90ab-cdef-EXAMPLEbbbbb",
    "readOnly": false,
    "eventType": "AwsApiCall",
    "managementEvent": true,
    "recipientAccountId": "111122223333",
    "eventCategory": "Management"
}
```
