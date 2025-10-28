# Logging Amazon CloudWatch API and console operations with AWS CloudTrail

Amazon CloudWatch, CloudWatch Synthetics, CloudWatch RUM, Amazon Q Developer operational investigations, Network Flow Monitor, and Internet Monitor are integrated with AWS CloudTrail, a service that provides a record

of actions taken by a user, role, or an AWS service. CloudTrail captures API calls made by or on
behalf of your AWS account. The captured calls include calls from the CloudWatch console and code calls
to CloudWatch API operations. Using the information collected by CloudTrail, you can
determine the request that was made to CloudWatch, the IP address from which the request was
made, when it was made, and additional details.

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

###### Note

For information about CloudWatch Logs API calls that are logged in CloudTrail, see
[CloudWatch Logs information in CloudTrail](../logs/logging_cw_api_calls_cwl.md#cwl_info_in_ct "../logs/logging_cw_api_calls_cwl.md#cwl_info_in_ct").

###### Topics

- [CloudWatch information in CloudTrail](#cw_info_in_ct "#cw_info_in_ct")
- [CloudWatch data events in CloudTrail](#CloudWatch-data-plane-events "#CloudWatch-data-plane-events")
- [Query generation information in CloudTrail](#cwl_query-generation-cloudtrail "#cwl_query-generation-cloudtrail")
- [Amazon Q Developer operational investigations events in CloudTrail](#Q-Developer-Investigations-Cloudtrail "#Q-Developer-Investigations-Cloudtrail")
- [Network Flow Monitor in CloudTrail](#CloudWatch-NetworkFlowMonitor-info-in-ct "#CloudWatch-NetworkFlowMonitor-info-in-ct")
- [Network Flow Monitor data plane
  events in CloudTrail](#CloudWatch-NetworkFlowMonitor-data-plane-events "#CloudWatch-NetworkFlowMonitor-data-plane-events")
- [Internet Monitor in CloudTrail](#cw_im_info_in_ct "#cw_im_info_in_ct")
- [CloudWatch Synthetics information in CloudTrail](#cw_synthetics_info_in_ct "#cw_synthetics_info_in_ct")
- [CloudWatch RUM information in CloudTrail](#RUM-CloudTrail "#RUM-CloudTrail")
- [CloudWatch RUM data plane
  events in CloudTrail](#RUM-data-plane-events "#RUM-data-plane-events")
- [Network Synthetic Monitor information in CloudTrail](#cw_network_synthetic_monitor_info_in_ct "#cw_network_synthetic_monitor_info_in_ct")
- [CloudWatch Observability Access Manager information in CloudTrail](#cw_observability_access_manager_info_in_ct "#cw_observability_access_manager_info_in_ct")
- [CloudWatch Observability Admin information in CloudTrail](#cw_observability_admin_info_in_ct "#cw_observability_admin_info_in_ct")
- [CloudWatch Application Signals information in CloudTrail](#cw_application_signals_info_in_ct "#cw_application_signals_info_in_ct")
- [CloudWatch Application Insights information in CloudTrail](#cw_application_insights_info_in_ct "#cw_application_insights_info_in_ct")

## CloudWatch information in CloudTrail

CloudWatch supports logging the following actions as events in CloudTrail log files:

- [DeleteAlarmActions](../APIReference/API_DeleteAlarmActions.md "../APIReference/API_DeleteAlarmActions.md")
- [DeleteAnomalyDetector](../APIReference/API_DeleteAnomalyDetector.md "../APIReference/API_DeleteAnomalyDetector.md")
- [DeleteDashboards](../APIReference/API_DeleteDashboards.md "../APIReference/API_DeleteDashboards.md")
- [DeleteInsightRules](../APIReference/API_DeleteInsightRules.md "../APIReference/API_DeleteInsightRules.md")
- [DeleteMetricStream](../APIReference/API_DeleteMetricStream.md "../APIReference/API_DeleteMetricStream.md")
- [DescribeAlarmHistory](../APIReference/API_DescribeAlarmHistory.md "../APIReference/API_DescribeAlarmHistory.md")
- [DescribeAlarms](../APIReference/API_DescribeAlarms.md "../APIReference/API_DescribeAlarms.md")
- [DescribeAlarmsForMetric](../APIReference/API_DescribeAlarmsForMetric.md "../APIReference/API_DescribeAlarmsForMetric.md")
- [DescribeAnomalyDetectors](../APIReference/API_DescribeAnomalyDetectors.md "../APIReference/API_DescribeAnomalyDetectors.md")
- [DescribeInsightRules](../APIReference/API_DescribeInsightRules.md "../APIReference/API_DescribeInsightRules.md")
- [DisableAlarmActions](../APIReference/API_DisableAlarmActions.md "../APIReference/API_DisableAlarmActions.md")
- [DisableInsightRules](../APIReference/API_DisableInsightRules.md "../APIReference/API_DisableInsightRules.md")
- [EnableAlarmActions](../APIReference/API_EnableAlarmActions.md "../APIReference/API_EnableAlarmActions.md")
- [EnableInsightRules](../APIReference/API_EnableInsightRules.md "../APIReference/API_EnableInsightRules.md")
- [GetDashboard](../APIReference/API_GetDashboard.md "../APIReference/API_GetDashboard.md")
- [GetInsightRuleReport](../APIReference/API_GetInsightRuleReport.md "../APIReference/API_GetInsightRuleReport.md")
- [GetMetricStream](../APIReference/API_GetMetricStream.md "../APIReference/API_GetMetricStream.md")
- [ListDashboards](../APIReference/API_ListDashboards.md "../APIReference/API_ListDashboards.md")
- [ListManagedInsightRules](../APIReference/API_ListManagedInsightRules.md "../APIReference/API_ListManagedInsightRules.md")
- [ListMetricStreams](../APIReference/API_ListMetricStreams.md "../APIReference/API_ListMetricStreams.md")
- [ListTagsForResource](../APIReference/API_ListTagsForResource.md "../APIReference/API_ListTagsForResource.md")
- [PutAnomalyDetector](../APIReference/API_PutAnomalyDetector.md "../APIReference/API_PutAnomalyDetector.md")
- [PutCompositeAlarm](../APIReference/API_PutCompositeAlarm.md "../APIReference/API_PutCompositeAlarm.md")
- [PutDashboard](../APIReference/API_PutDashboard.md "../APIReference/API_PutDashboard.md")
- [PutInsightRule](../APIReference/API_PutInsightRule.md "../APIReference/API_PutInsightRule.md")
- [PutManagedInsightRules](../APIReference/API_PutManagedInsightRules.md "../APIReference/API_PutManagedInsightRules.md")
- [PutMetricAlarm](../APIReference/API_PutMetricAlarm.md "../APIReference/API_PutMetricAlarm.md")
- [PutMetricStream](../APIReference/API_PutMetricStream.md "../APIReference/API_PutMetricStream.md")
- [SetAlarmState](../APIReference/API_SetAlarmState.md "../APIReference/API_SetAlarmState.md")
- [StartMetricStreams](../APIReference/API_StartMetricStreams.md "../APIReference/API_StartMetricStreams.md")
- [StopMetricStreams](../APIReference/API_StopMetricStreams.md "../APIReference/API_StopMetricStreams.md")
- [TagResource](../APIReference/API_TagResource.md "../APIReference/API_TagResource.md")
- [UntagResource](../APIReference/API_UntagResource.md "../APIReference/API_UntagResource.md")

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
_AWS CloudTrail User Guide_.

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

- [CreateInvestigationGroup](../../../cloudwatchinvestigations/latest/APIReference/API_CreateInvestigationGroup.md "../../../cloudwatchinvestigations/latest/APIReference/API_CreateInvestigationGroup.md")
- [GetInvestigationGroup](../../../cloudwatchinvestigations/latest/APIReference/API_GetInvestigationGroup.md "../../../cloudwatchinvestigations/latest/APIReference/API_GetInvestigationGroup.md")
- [DeleteInvestigationGroup](../../../cloudwatchinvestigations/latest/APIReference/API_DeleteInvestigationGroup.md "../../../cloudwatchinvestigations/latest/APIReference/API_DeleteInvestigationGroup.md")
- [ListInvestigationGroup](../../../cloudwatchinvestigations/latest/APIReference/API_ListInvestigationGroups.md "../../../cloudwatchinvestigations/latest/APIReference/API_ListInvestigationGroups.md")
- [PutInvestigationGroupPolicy](../../../cloudwatchinvestigations/latest/APIReference/API_PutInvestigationGroupPolicy.md "../../../cloudwatchinvestigations/latest/APIReference/API_PutInvestigationGroupPolicy.md")
- [DeleteInvestigationGroupPolicy](../../../cloudwatchinvestigations/latest/APIReference/API_DeleteInvestigationGroupPolicy.md "../../../cloudwatchinvestigations/latest/APIReference/API_DeleteInvestigationGroupPolicy.md")
- [ListTagsForResource](../../../cloudwatchinvestigations/latest/APIReference/API_ListTagsForResource.md "../../../cloudwatchinvestigations/latest/APIReference/API_ListTagsForResource.md")
- [GetInvestigationGroupPolicy](../../../cloudwatchinvestigations/latest/APIReference/API_GetInvestigationGroupPolicy.md "../../../cloudwatchinvestigations/latest/APIReference/API_GetInvestigationGroupPolicy.md")
- [TagResource](../../../cloudwatchinvestigations/latest/APIReference/API_TagResource.md "../../../cloudwatchinvestigations/latest/APIReference/API_TagResource.md")
- [UntagResource](../../../cloudwatchinvestigations/latest/APIReference/API_UntagResource.md "../../../cloudwatchinvestigations/latest/APIReference/API_UntagResource.md")
- [UpdateInvestigationGroup](../../../cloudwatchinvestigations/latest/APIReference/API_UpdateInvestigationGroup.md "../../../cloudwatchinvestigations/latest/APIReference/API_UpdateInvestigationGroup.md")

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

- [CreateMonitor](../../../networkflowmonitor/2.0/APIReference/API_CreateMonitor.md "../../../networkflowmonitor/2.0/APIReference/API_CreateMonitor.md")
- [CreateScope](../../../networkflowmonitor/2.0/APIReference/API_CreateScope.md "../../../networkflowmonitor/2.0/APIReference/API_CreateScope.md")
- [DeleteMonitor](../../../networkflowmonitor/2.0/APIReference/API_DeleteMonitor.md "../../../networkflowmonitor/2.0/APIReference/API_DeleteMonitor.md")
- [DeleteScope](../../../networkflowmonitor/2.0/APIReference/API_DeleteScope.md "../../../networkflowmonitor/2.0/APIReference/API_DeleteScope.md")
- [GetMonitor](../../../networkflowmonitor/2.0/APIReference/API_GetMonitor.md "../../../networkflowmonitor/2.0/APIReference/API_GetMonitor.md")
- [GetScope](../../../networkflowmonitor/2.0/APIReference/API_GetScope.md "../../../networkflowmonitor/2.0/APIReference/API_GetScope.md")
- [ListMonitors](../../../networkflowmonitor/2.0/APIReference/API_ListMonitors.md "../../../networkflowmonitor/2.0/APIReference/API_ListMonitors.md")
- [ListScopes](../../../networkflowmonitor/2.0/APIReference/API_ListScopes.md "../../../networkflowmonitor/2.0/APIReference/API_ListScopes.md")
- [ListTagsForResource](../../../networkflowmonitor/2.0/APIReference/API_ListTagsForResource.md "../../../networkflowmonitor/2.0/APIReference/API_ListTagsForResource.md")
- [TagResource](../../../networkflowmonitor/2.0/APIReference/API_TagResource.md "../../../networkflowmonitor/2.0/APIReference/API_TagResource.md")
- [UntagResource](../../../networkflowmonitor/2.0/APIReference/API_UntagResource.md "../../../networkflowmonitor/2.0/APIReference/API_UntagResource.md")
- [UpdateMonitor](../../../networkflowmonitor/2.0/APIReference/API_UpdateMonitor.md "../../../networkflowmonitor/2.0/APIReference/API_UpdateMonitor.md")
- [UpdateScope](../../../networkflowmonitor/2.0/APIReference/API_UpdateScope.md "../../../networkflowmonitor/2.0/APIReference/API_UpdateScope.md")

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

- [GetQueryResultsMonitorTopContributors](../../../networkflowmonitor/2.0/APIReference/API_GetQueryResultsMonitorTopContributors.md "../../../networkflowmonitor/2.0/APIReference/API_GetQueryResultsMonitorTopContributors.md")
- [GetQueryResultsMonitorsTopContributors](../../../networkflowmonitor/2.0/APIReference/API_GetQueryResultsMonitorsTopContributors.md "../../../networkflowmonitor/2.0/APIReference/API_GetQueryResultsMonitorsTopContributors.md")
- [GetQueryResultsWorkloadInsightsTopContributors](../../../networkflowmonitor/2.0/APIReference/API_GetQueryResultsWorkloadInsightsTopContributors.md "../../../networkflowmonitor/2.0/APIReference/API_GetQueryResultsWorkloadInsightsTopContributors.md")
- [GetQueryResultsWorkloadInsightsTopContributorsData](../../../networkflowmonitor/2.0/APIReference/API_GetQueryResultsWorkloadInsightsTopContributorsData.md "../../../networkflowmonitor/2.0/APIReference/API_GetQueryResultsWorkloadInsightsTopContributorsData.md")
- [GetQueryStatusMonitorTopContributors](../../../networkflowmonitor/2.0/APIReference/API_GetQueryStatusMonitorTopContributors.md "../../../networkflowmonitor/2.0/APIReference/API_GetQueryStatusMonitorTopContributors.md")
- [GetQueryStatusMonitorsTopContributors](../../../networkflowmonitor/2.0/APIReference/API_GetQueryStatusMonitorsTopContributors.md "../../../networkflowmonitor/2.0/APIReference/API_GetQueryStatusMonitorsTopContributors.md")
- [GetQueryStatusWorkloadInsightsTopContributors](../../../networkflowmonitor/2.0/APIReference/API_GetQueryStatusWorkloadInsightsTopContributors.md "../../../networkflowmonitor/2.0/APIReference/API_GetQueryStatusWorkloadInsightsTopContributors.md")
- [GetQueryStatusWorkloadInsightsTopContributorsData](../../../networkflowmonitor/2.0/APIReference/API_GetQueryStatusWorkloadInsightsTopContributorsData.md "../../../networkflowmonitor/2.0/APIReference/API_GetQueryStatusWorkloadInsightsTopContributorsData.md")
- [StartQueryMonitorTopContributors](../../../networkflowmonitor/2.0/APIReference/API_StartQueryMonitorTopContributors.md "../../../networkflowmonitor/2.0/APIReference/API_StartQueryMonitorTopContributors.md")
- [StartQueryMonitorsTopContributors](../../../networkflowmonitor/2.0/APIReference/API_StartQueryMonitorsTopContributors.md "../../../networkflowmonitor/2.0/APIReference/API_StartQueryMonitorsTopContributors.md")
- [StartQueryWorkloadInsightsTopContributors](../../../networkflowmonitor/2.0/APIReference/API_StartQueryWorkloadInsightsTopContributors.md "../../../networkflowmonitor/2.0/APIReference/API_StartQueryWorkloadInsightsTopContributors.md")
- [StartQueryWorkloadInsightsTopContributorsData](../../../networkflowmonitor/2.0/APIReference/API_StartQueryWorkloadInsightsTopContributorsData.md "../../../networkflowmonitor/2.0/APIReference/API_StartQueryWorkloadInsightsTopContributorsData.md")
- [StopQueryMonitorTopContributors](../../../networkflowmonitor/2.0/APIReference/API_StopQueryMonitorTopContributors.md "../../../networkflowmonitor/2.0/APIReference/API_StopQueryMonitorTopContributors.md")
- [StopQueryMonitorsTopContributors](../../../networkflowmonitor/2.0/APIReference/API_StopQueryMonitorsTopContributors.md "../../../networkflowmonitor/2.0/APIReference/API_StopQueryMonitorsTopContributors.md")
- [StopQueryWorkloadInsightsTopContributors](../../../networkflowmonitor/2.0/APIReference/API_StopQueryWorkloadInsightsTopContributors.md "../../../networkflowmonitor/2.0/APIReference/API_StopQueryWorkloadInsightsTopContributors.md")
- [StopQueryWorkloadInsightsTopContributorsData](../../../networkflowmonitor/2.0/APIReference/API_StopQueryWorkloadInsightsTopContributorsData.md "../../../networkflowmonitor/2.0/APIReference/API_StopQueryWorkloadInsightsTopContributorsData.md")

The following example shows a CloudTrail log entry that demonstrates the [GetQueryResultsMonitorsTopContributors](../../../networkflowmonitor/2.0/APIReference/API_GetQueryResultsMonitorsTopContributors.md "../../../networkflowmonitor/2.0/APIReference/API_GetQueryResultsMonitorsTopContributors.md") action.

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

The following example shows a CloudTrail log entry that demonstrates the [GetQueryResultsWorkloadInsightsTopContributors](../../../networkflowmonitor/2.0/APIReference/API_GetQueryResultsWorkloadInsightsTopContributors.md "../../../networkflowmonitor/2.0/APIReference/API_GetQueryResultsWorkloadInsightsTopContributors.md") action.

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

- [CreateMonitor](../../../internet-monitor/latest/api/API_CreateMonitor.md "../../../internet-monitor/latest/api/API_CreateMonitor.md")
- [DeleteMonitor](../../../internet-monitor/latest/api/API_DeleteMonitor.md "../../../internet-monitor/latest/api/API_DeleteMonitor.md")
- [GetHealthEvent](../../../internet-monitor/latest/api/API_GetHealthEvent.md "../../../internet-monitor/latest/api/API_GetHealthEvent.md")
- [GetMonitor](../../../internet-monitor/latest/api/API_GetMonitor.md "../../../internet-monitor/latest/api/API_GetMonitor.md")
- [GetQueryResults](../../../internet-monitor/latest/api/API_GetQueryResults.md "../../../internet-monitor/latest/api/API_GetQueryResults.md")
- [GetQueryStatus](../../../internet-monitor/latest/api/API_GetQueryStatus.md "../../../internet-monitor/latest/api/API_GetQueryStatus.md")
- [ListHealthEvents](../../../internet-monitor/latest/api/API_ListHealthEvents.md "../../../internet-monitor/latest/api/API_ListHealthEvents.md")
- [ListInternetEvents](../../../internet-monitor/latest/api/API_ListInternetEvents.md "../../../internet-monitor/latest/api/API_ListInternetEvents.md")
- [ListMonitors](../../../internet-monitor/latest/api/API_ListMonitors.md "../../../internet-monitor/latest/api/API_ListMonitors.md")
- [ListTagsForResource](../../../internet-monitor/latest/api/API_ListTagsForResource.md "../../../internet-monitor/latest/api/API_ListTagsForResource.md")
- [StartQuery](../../../internet-monitor/latest/api/API_StartQuery.md "../../../internet-monitor/latest/api/API_StartQuery.md")
- [StopQuery](../../../internet-monitor/latest/api/API_StopQuery.md "../../../internet-monitor/latest/api/API_StopQuery.md")
- [TagResource](../../../internet-monitor/latest/api/API_TagResource.md "../../../internet-monitor/latest/api/API_TagResource.md")
- [UntagResource](../../../internet-monitor/latest/api/API_UntagResource.md "../../../internet-monitor/latest/api/API_UntagResource.md")
- [UpdateMonitor](../../../internet-monitor/latest/api/API_UpdateMonitor.md "../../../internet-monitor/latest/api/API_UpdateMonitor.md")

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

- [AssociateResource](../../../AmazonSynthetics/latest/APIReference/API_AssociateResource.md "../../../AmazonSynthetics/latest/APIReference/API_AssociateResource.md")
- [CreateCanary](../../../AmazonSynthetics/latest/APIReference/API_CreateCanary.md "../../../AmazonSynthetics/latest/APIReference/API_CreateCanary.md")
- [CreateGroup](../../../AmazonSynthetics/latest/APIReference/API_CreateGroup.md "../../../AmazonSynthetics/latest/APIReference/API_CreateGroup.md")
- [DeleteCanary](../../../AmazonSynthetics/latest/APIReference/API_DeleteCanary.md "../../../AmazonSynthetics/latest/APIReference/API_DeleteCanary.md")
- [DeleteGroup](../../../AmazonSynthetics/latest/APIReference/API_DeleteGroup.md "../../../AmazonSynthetics/latest/APIReference/API_DeleteGroup.md")
- [DescribeCanaries](../../../AmazonSynthetics/latest/APIReference/API_DescribeCanaries.md "../../../AmazonSynthetics/latest/APIReference/API_DescribeCanaries.md")
- [DescribeCanariesLastRun](../../../AmazonSynthetics/latest/APIReference/API_DescribeCanariesLastRun.md "../../../AmazonSynthetics/latest/APIReference/API_DescribeCanariesLastRun.md")
- [DescribeRuntimeVersions](../../../AmazonSynthetics/latest/APIReference/API_DescribeRuntimeVersions.md "../../../AmazonSynthetics/latest/APIReference/API_DescribeRuntimeVersions.md")
- [DisassociateResource](../../../AmazonSynthetics/latest/APIReference/API_DisassociateResource.md "../../../AmazonSynthetics/latest/APIReference/API_DisassociateResource.md")
- [GetCanary](../../../AmazonSynthetics/latest/APIReference/API_GetCanary.md "../../../AmazonSynthetics/latest/APIReference/API_GetCanary.md")
- [GetCanaryRuns](../../../AmazonSynthetics/latest/APIReference/API_GetCanaryRuns.md "../../../AmazonSynthetics/latest/APIReference/API_GetCanaryRuns.md")
- [GetGroup](../../../AmazonSynthetics/latest/APIReference/API_GetGroup.md "../../../AmazonSynthetics/latest/APIReference/API_GetGroup.md")
- [ListAssociatedGroups](../../../AmazonSynthetics/latest/APIReference/API_ListAssociatedGroups.md "../../../AmazonSynthetics/latest/APIReference/API_ListAssociatedGroups.md")
- [ListGroupResources](../../../AmazonSynthetics/latest/APIReference/API_ListGroupResources.md "../../../AmazonSynthetics/latest/APIReference/API_ListGroupResources.md")
- [ListGroups](../../../AmazonSynthetics/latest/APIReference/API_ListGroups.md "../../../AmazonSynthetics/latest/APIReference/API_ListGroups.md")
- [ListTagsForResource](../../../AmazonSynthetics/latest/APIReference/API_ListTagsForResource.md "../../../AmazonSynthetics/latest/APIReference/API_ListTagsForResource.md")
- [StartCanary](../../../AmazonSynthetics/latest/APIReference/API_StartCanary.md "../../../AmazonSynthetics/latest/APIReference/API_StartCanary.md")
- [StartCanaryDryRun](../../../AmazonSynthetics/latest/APIReference/API_StartCanaryDryRun.md "../../../AmazonSynthetics/latest/APIReference/API_StartCanaryDryRun.md")
- [StopCanary](../../../AmazonSynthetics/latest/APIReference/API_StopCanary.md "../../../AmazonSynthetics/latest/APIReference/API_StopCanary.md")
- [TagResource](../../../AmazonSynthetics/latest/APIReference/API_TagResource.md "../../../AmazonSynthetics/latest/APIReference/API_TagResource.md")
- [UntagResource](../../../AmazonSynthetics/latest/APIReference/API_UntagResource.md "../../../AmazonSynthetics/latest/APIReference/API_UntagResource.md")
- [UpdateCanary](../../../AmazonSynthetics/latest/APIReference/API_UpdateCanary.md "../../../AmazonSynthetics/latest/APIReference/API_UpdateCanary.md")

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

- [BatchCreateRumMetricDefinitions](../../../cloudwatchrum/latest/APIReference/API_BatchCreateRumMetricDefinitions.md "../../../cloudwatchrum/latest/APIReference/API_BatchCreateRumMetricDefinitions.md")
- [BatchDeleteRumMetricDefinitions](../../../cloudwatchrum/latest/APIReference/API_BatchDeleteRumMetricDefinitions.md "../../../cloudwatchrum/latest/APIReference/API_BatchDeleteRumMetricDefinitions.md")
- [BatchGetRumMetricDefinitions](../../../cloudwatchrum/latest/APIReference/API_BatchGetRumMetricDefinitions.md "../../../cloudwatchrum/latest/APIReference/API_BatchGetRumMetricDefinitions.md")
- [CreateAppMonitor](../../../cloudwatchrum/latest/APIReference/API_CreateAppMonitor.md "../../../cloudwatchrum/latest/APIReference/API_CreateAppMonitor.md")
- [DeleteAppMonitor](../../../cloudwatchrum/latest/APIReference/API_DeleteAppMonitor.md "../../../cloudwatchrum/latest/APIReference/API_DeleteAppMonitor.md")
- [DeleteResourcePolicy](../../../cloudwatchrum/latest/APIReference/API_DeleteResourcePolicy.md "../../../cloudwatchrum/latest/APIReference/API_DeleteResourcePolicy.md")
- [DeleteRumMetricsDestination](../../../cloudwatchrum/latest/APIReference/API_DeleteRumMetricsDestination.md "../../../cloudwatchrum/latest/APIReference/API_DeleteRumMetricsDestination.md")
- [GetAppMonitor](../../../cloudwatchrum/latest/APIReference/API_GetAppMonitor.md "../../../cloudwatchrum/latest/APIReference/API_GetAppMonitor.md")
- [GetAppMonitorData](../../../cloudwatchrum/latest/APIReference/API_GetAppMonitorData.md "../../../cloudwatchrum/latest/APIReference/API_GetAppMonitorData.md")
- [GetResourcePolicy](../../../cloudwatchrum/latest/APIReference/API_GetResourcePolicy.md "../../../cloudwatchrum/latest/APIReference/API_GetResourcePolicy.md")
- [ListAppMonitors](../../../cloudwatchrum/latest/APIReference/API_ListAppMonitors.md "../../../cloudwatchrum/latest/APIReference/API_ListAppMonitors.md")
- [ListRumMetricsDestinations](../../../cloudwatchrum/latest/APIReference/API_ListRumMetricsDestinations.md "../../../cloudwatchrum/latest/APIReference/API_ListRumMetricsDestinations.md")
- [ListTagsForResource](../../../cloudwatchrum/latest/APIReference/API_ListTagsForResource.md "../../../cloudwatchrum/latest/APIReference/API_ListTagsForResource.md")
- [PutResourcePolicy](../../../cloudwatchrum/latest/APIReference/API_PutResourcePolicy.md "../../../cloudwatchrum/latest/APIReference/API_PutResourcePolicy.md")
- [PutRumMetricsDestination](../../../cloudwatchrum/latest/APIReference/API_PutRumMetricsDestination.md "../../../cloudwatchrum/latest/APIReference/API_PutRumMetricsDestination.md")
- [TagResource](../../../cloudwatchrum/latest/APIReference/API_TagResource.md "../../../cloudwatchrum/latest/APIReference/API_TagResource.md")
- [UntagResource](../../../cloudwatchrum/latest/APIReference/API_UntagResource.md "../../../cloudwatchrum/latest/APIReference/API_UntagResource.md")
- [UpdateAppMonitor](../../../cloudwatchrum/latest/APIReference/API_UpdateAppMonitor.md "../../../cloudwatchrum/latest/APIReference/API_UpdateAppMonitor.md")
- [UpdateRumMetricDefinition](../../../cloudwatchrum/latest/APIReference/API_UpdateRumMetricDefinition.md "../../../cloudwatchrum/latest/APIReference/API_UpdateRumMetricDefinition.md")

### Example: CloudWatch RUM log file entries

This section contains example CloudTrail entries for some CloudWatch RUM APIs.

The following example shows a CloudTrail log entry that demonstrates the [CreateAppMonitor](../../../cloudwatchrum/latest/APIReference/API_CreateAppMonitor.md "../../../cloudwatchrum/latest/APIReference/API_CreateAppMonitor.md") action.

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

The following example shows a CloudTrail log entry that demonstrates the [PutRumMetricsDestination](../../../cloudwatchrum/latest/APIReference/API_PutRumMetricsDestination.md "../../../cloudwatchrum/latest/APIReference/API_PutRumMetricsDestination.md") action.

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

The following example shows a CloudTrail log entry that demonstrates the [BatchCreateRumMetricsDefinitions](../../../cloudwatchrum/latest/APIReference/API_BatchCreateRumMetricsDefinitions.md "../../../cloudwatchrum/latest/APIReference/API_BatchCreateRumMetricsDefinitions.md") action.

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

CloudTrail can capture API activities related to the CloudWatch RUM data plane operation [PutRumEvents](../../../cloudwatchrum/latest/APIReference/API_PutRumEvents.md "../../../cloudwatchrum/latest/APIReference/API_PutRumEvents.md").

[Data events](../../../awscloudtrail/latest/userguide/logging-data-events-with-cloudtrail.md#logging-data-events "../../../awscloudtrail/latest/userguide/logging-data-events-with-cloudtrail.md#logging-data-events"), also known as data plane operations, give you insight into the resource operations performed
on or within a resource. Data events are often high-volume activities.

To enable logging of the **PutRumEvents** data events in CloudTrail files, you'll need to enable
the logging of data plane API activity in CloudTrail. See [Logging data events for trails](../../../awscloudtrail/latest/userguide/logging-data-events-with-cloudtrail.md "../../../awscloudtrail/latest/userguide/logging-data-events-with-cloudtrail.md") for more information.

Data plane events can be filtered by resource type. Because there are additional costs for using
data events in CloudTrail, filtering by resource allows you to have more control over what you log and pay for.

Using the information that CloudTrail collects, you can identify a specific request to the CloudWatch RUM **PutRumEvents** API, the IP address of the requester, the requester's identity, and the date and time of the
request. Logging the **PutRumEvents** API using CloudTrail helps you enable operational and
risk auditing, governance, and compliance of your AWS account.

The following example shows a CloudTrail log entry that demonstrates the [PutRumEvents](../../../cloudwatchrum/latest/APIReference/API_PutRumEvents.md "../../../cloudwatchrum/latest/APIReference/API_PutRumEvents.md") action.

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

- [CreateMonitor](../../../networkmonitor/latest/APIReference/API_CreateMonitor.md "../../../networkmonitor/latest/APIReference/API_CreateMonitor.md")
- [CreateProbe](../../../networkmonitor/latest/APIReference/API_CreateProbe.md "../../../networkmonitor/latest/APIReference/API_CreateProbe.md")
- [DeleteMonitor](../../../networkmonitor/latest/APIReference/API_DeleteMonitor.md "../../../networkmonitor/latest/APIReference/API_DeleteMonitor.md")
- [DeleteProbe](../../../networkmonitor/latest/APIReference/API_DeleteProbe.md "../../../networkmonitor/latest/APIReference/API_DeleteProbe.md")
- [GetMonitor](../../../networkmonitor/latest/APIReference/API_GetMonitor.md "../../../networkmonitor/latest/APIReference/API_GetMonitor.md")
- [GetProbe](../../../networkmonitor/latest/APIReference/API_GetProbe.md "../../../networkmonitor/latest/APIReference/API_GetProbe.md")
- [ListMonitors](../../../networkmonitor/latest/APIReference/API_ListMonitors.md "../../../networkmonitor/latest/APIReference/API_ListMonitors.md")
- [ListTagsForResource](../../../networkmonitor/latest/APIReference/API_ListTagsForResource.md "../../../networkmonitor/latest/APIReference/API_ListTagsForResource.md")
- [TagResource](../../../networkmonitor/latest/APIReference/API_TagResource.md "../../../networkmonitor/latest/APIReference/API_TagResource.md")
- [UntagResource](../../../networkmonitor/latest/APIReference/API_UntagResource.md "../../../networkmonitor/latest/APIReference/API_UntagResource.md")
- [UpdateMonitor](../../../networkmonitor/latest/APIReference/API_UpdateMonitor.md "../../../networkmonitor/latest/APIReference/API_UpdateMonitor.md")
- [UpdateProbe](../../../networkmonitor/latest/APIReference/API_UpdateProbe.md "../../../networkmonitor/latest/APIReference/API_UpdateProbe.md")

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

- [CreateLink](../../../OAM/latest/APIReference/API_CreateLink.md "../../../OAM/latest/APIReference/API_CreateLink.md")
- [CreateSink](../../../OAM/latest/APIReference/API_CreateSink.md "../../../OAM/latest/APIReference/API_CreateSink.md")
- [DeleteLink](../../../OAM/latest/APIReference/API_DeleteLink.md "../../../OAM/latest/APIReference/API_DeleteLink.md")
- [DeleteSink](../../../OAM/latest/APIReference/API_DeleteSink.md "../../../OAM/latest/APIReference/API_DeleteSink.md")
- [GetLink](../../../OAM/latest/APIReference/API_GetLink.md "../../../OAM/latest/APIReference/API_GetLink.md")
- [GetSink](../../../OAM/latest/APIReference/API_GetSink.md "../../../OAM/latest/APIReference/API_GetSink.md")
- [GetSinkPolicy](../../../OAM/latest/APIReference/API_GetSinkPolicy.md "../../../OAM/latest/APIReference/API_GetSinkPolicy.md")
- [ListAttachedLinks](../../../OAM/latest/APIReference/API_ListAttachedLinks.md "../../../OAM/latest/APIReference/API_ListAttachedLinks.md")
- [ListLinks](../../../OAM/latest/APIReference/API_ListLinks.md "../../../OAM/latest/APIReference/API_ListLinks.md")
- [ListSinks](../../../OAM/latest/APIReference/API_ListSinks.md "../../../OAM/latest/APIReference/API_ListSinks.md")
- [ListTagsForResource](../../../OAM/latest/APIReference/API_ListTagsForResource.md "../../../OAM/latest/APIReference/API_ListTagsForResource.md")
- [PutSinkPolicy](../../../OAM/latest/APIReference/API_PutSinkPolicy.md "../../../OAM/latest/APIReference/API_PutSinkPolicy.md")
- [TagResource](../../../OAM/latest/APIReference/API_TagResource.md "../../../OAM/latest/APIReference/API_TagResource.md")
- [UntagResource](../../../OAM/latest/APIReference/API_UntagResource.md "../../../OAM/latest/APIReference/API_UntagResource.md")
- [UpdateLink](../../../OAM/latest/APIReference/API_UpdateLink.md "../../../OAM/latest/APIReference/API_UpdateLink.md")

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

- [GetTelemetryEvaluationStatus](../../../cloudwatch/latest/observabilityadmin/API_GetTelemetryEvaluationStatus.md "../../../cloudwatch/latest/observabilityadmin/API_GetTelemetryEvaluationStatus.md")
- [GetTelemetryEvaluationStatusForOrganization](../../../cloudwatch/latest/observabilityadmin/API_GetTelemetryEvaluationStatusForOrganization.md "../../../cloudwatch/latest/observabilityadmin/API_GetTelemetryEvaluationStatusForOrganization.md")
- [ListResourceTelemetry](../../../cloudwatch/latest/observabilityadmin/API_ListResourceTelemetry.md "../../../cloudwatch/latest/observabilityadmin/API_ListResourceTelemetry.md")
- [ListResourceTelemetryForOrganization](../../../cloudwatch/latest/observabilityadmin/API_ListResourceTelemetryForOrganization.md "../../../cloudwatch/latest/observabilityadmin/API_ListResourceTelemetryForOrganization.md")
- [StartTelemetryEvaluation](../../../cloudwatch/latest/observabilityadmin/API_StartTelemetryEvaluation.md "../../../cloudwatch/latest/observabilityadmin/API_StartTelemetryEvaluation.md")
- [StartTelemetryEvaluationForOrganization](../../../cloudwatch/latest/observabilityadmin/API_StartTelemetryEvaluationForOrganization.md "../../../cloudwatch/latest/observabilityadmin/API_StartTelemetryEvaluationForOrganization.md")
- [StopTelemetryEvaluation](../../../cloudwatch/latest/observabilityadmin/API_StopTelemetryEvaluation.md "../../../cloudwatch/latest/observabilityadmin/API_StopTelemetryEvaluation.md")
- [StopTelemetryEvaluationForOrganization](../../../cloudwatch/latest/observabilityadmin/API_StopTelemetryEvaluationForOrganization.md "../../../cloudwatch/latest/observabilityadmin/API_StopTelemetryEvaluationForOrganization.md")

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

- [BatchGetServiceLevelObjectiveBudgetReport](../../../applicationsignals/latest/APIReference/API_BatchGetServiceLevelObjectiveBudgetReport.md "../../../applicationsignals/latest/APIReference/API_BatchGetServiceLevelObjectiveBudgetReport.md")
- [BatchUpdateExclusionWindows](../../../applicationsignals/latest/APIReference/API_BatchUpdateExclusionWindows.md "../../../applicationsignals/latest/APIReference/API_BatchUpdateExclusionWindows.md")
- [CreateServiceLevelObjective](../../../applicationsignals/latest/APIReference/API_CreateServiceLevelObjective.md "../../../applicationsignals/latest/APIReference/API_CreateServiceLevelObjective.md")
- [DeleteServiceLevelObjective](../../../applicationsignals/latest/APIReference/API_DeleteServiceLevelObjective.md "../../../applicationsignals/latest/APIReference/API_DeleteServiceLevelObjective.md")
- [GetService](../../../applicationsignals/latest/APIReference/API_GetService.md "../../../applicationsignals/latest/APIReference/API_GetService.md")
- [GetServiceLevelObjective](../../../applicationsignals/latest/APIReference/API_GetServiceLevelObjective.md "../../../applicationsignals/latest/APIReference/API_GetServiceLevelObjective.md")
- [ListServiceDependencies](../../../applicationsignals/latest/APIReference/API_ListServiceDependencies.md "../../../applicationsignals/latest/APIReference/API_ListServiceDependencies.md")
- [ListServiceDependents](../../../applicationsignals/latest/APIReference/API_ListServiceDependents.md "../../../applicationsignals/latest/APIReference/API_ListServiceDependents.md")
- [ListServiceLevelObjectives](../../../applicationsignals/latest/APIReference/API_ListServiceLevelObjectives.md "../../../applicationsignals/latest/APIReference/API_ListServiceLevelObjectives.md")
- [ListServiceOperations](../../../applicationsignals/latest/APIReference/API_ListServiceOperations.md "../../../applicationsignals/latest/APIReference/API_ListServiceOperations.md")
- [ListServices](../../../applicationsignals/latest/APIReference/API_ListServices.md "../../../applicationsignals/latest/APIReference/API_ListServices.md")
- [ListTagsForResource](../../../applicationsignals/latest/APIReference/API_ListTagsForResource.md "../../../applicationsignals/latest/APIReference/API_ListTagsForResource.md")
- [StartDiscovery](../../../applicationsignals/latest/APIReference/API_StartDiscovery.md "../../../applicationsignals/latest/APIReference/API_StartDiscovery.md")
- [TagResource](../../../applicationsignals/latest/APIReference/API_TagResource.md "../../../applicationsignals/latest/APIReference/API_TagResource.md")
- [UntagResource](../../../applicationsignals/latest/APIReference/API_UntagResource.md "../../../applicationsignals/latest/APIReference/API_UntagResource.md")
- [UpdateServiceLevelObjective](../../../applicationsignals/latest/APIReference/API_UpdateServiceLevelObjective.md "../../../applicationsignals/latest/APIReference/API_UpdateServiceLevelObjective.md")

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

- [AddWorkload](../../../cloudwatch/latest/APIReference/API_AddWorkload.md "../../../cloudwatch/latest/APIReference/API_AddWorkload.md")
- [CreateApplication](../../../cloudwatch/latest/APIReference/API_CreateApplication.md "../../../cloudwatch/latest/APIReference/API_CreateApplication.md")
- [CreateComponent](../../../cloudwatch/latest/APIReference/API_CreateComponent.md "../../../cloudwatch/latest/APIReference/API_CreateComponent.md")
- [CreateLogPattern](../../../cloudwatch/latest/APIReference/API_CreateLogPattern.md "../../../cloudwatch/latest/APIReference/API_CreateLogPattern.md")
- [DeleteApplication](../../../cloudwatch/latest/APIReference/API_DeleteApplication.md "../../../cloudwatch/latest/APIReference/API_DeleteApplication.md")
- [DeleteComponent](../../../cloudwatch/latest/APIReference/API_DeleteComponent.md "../../../cloudwatch/latest/APIReference/API_DeleteComponent.md")
- [DeleteLogPattern](../../../cloudwatch/latest/APIReference/API_DeleteLogPattern.md "../../../cloudwatch/latest/APIReference/API_DeleteLogPattern.md")
- [DescribeApplication](../../../cloudwatch/latest/APIReference/API_DescribeApplication.md "../../../cloudwatch/latest/APIReference/API_DescribeApplication.md")
- [DescribeComponent](../../../cloudwatch/latest/APIReference/API_DescribeComponent.md "../../../cloudwatch/latest/APIReference/API_DescribeComponent.md")
- [DescribeComponentConfiguration](../../../cloudwatch/latest/APIReference/API_DescribeComponentConfiguration.md "../../../cloudwatch/latest/APIReference/API_DescribeComponentConfiguration.md")
- [DescribeComponentConfigurationRecommendation](../../../cloudwatch/latest/APIReference/API_DescribeComponentConfigurationRecommendation.md "../../../cloudwatch/latest/APIReference/API_DescribeComponentConfigurationRecommendation.md")
- [DescribeLogPattern](../../../cloudwatch/latest/APIReference/API_DescribeLogPattern.md "../../../cloudwatch/latest/APIReference/API_DescribeLogPattern.md")
- [DescribeObservation](../../../cloudwatch/latest/APIReference/API_DescribeObservation.md "../../../cloudwatch/latest/APIReference/API_DescribeObservation.md")
- [DescribeProblem](../../../cloudwatch/latest/APIReference/API_DescribeProblem.md "../../../cloudwatch/latest/APIReference/API_DescribeProblem.md")
- [DescribeProblemObservations](../../../cloudwatch/latest/APIReference/API_DescribeProblemObservations.md "../../../cloudwatch/latest/APIReference/API_DescribeProblemObservations.md")
- [DescribeWorkload](../../../cloudwatch/latest/APIReference/API_DescribeWorkload.md "../../../cloudwatch/latest/APIReference/API_DescribeWorkload.md")
- [ListApplications](../../../cloudwatch/latest/APIReference/API_ListApplications.md "../../../cloudwatch/latest/APIReference/API_ListApplications.md")
- [ListComponents](../../../cloudwatch/latest/APIReference/API_ListComponents.md "../../../cloudwatch/latest/APIReference/API_ListComponents.md")
- [ListConfigurationHistory](../../../cloudwatch/latest/APIReference/API_ListConfigurationHistory.md "../../../cloudwatch/latest/APIReference/API_ListConfigurationHistory.md")
- [ListLogPatterns](../../../cloudwatch/latest/APIReference/API_ListLogPatterns.md "../../../cloudwatch/latest/APIReference/API_ListLogPatterns.md")
- [ListLogPatternSets](../../../cloudwatch/latest/APIReference/API_ListLogPatternSets.md "../../../cloudwatch/latest/APIReference/API_ListLogPatternSets.md")
- [ListProblems](../../../cloudwatch/latest/APIReference/API_ListProblems.md "../../../cloudwatch/latest/APIReference/API_ListProblems.md")
- [ListTagsForResource](../../../cloudwatch/latest/APIReference/API_ListTagsForResource.md "../../../cloudwatch/latest/APIReference/API_ListTagsForResource.md")
- [ListWorkloads](../../../cloudwatch/latest/APIReference/API_ListWorkloads.md "../../../cloudwatch/latest/APIReference/API_ListWorkloads.md")
- [RemoveWorkload](../../../cloudwatch/latest/APIReference/API_RemoveWorkload.md "../../../cloudwatch/latest/APIReference/API_RemoveWorkload.md")
- [TagResource](../../../cloudwatch/latest/APIReference/API_TagResource.md "../../../cloudwatch/latest/APIReference/API_TagResource.md")
- [UntagResource](../../../cloudwatch/latest/APIReference/API_UntagResource.md "../../../cloudwatch/latest/APIReference/API_UntagResource.md")
- [UpdateApplication](../../../cloudwatch/latest/APIReference/API_UpdateApplication.md "../../../cloudwatch/latest/APIReference/API_UpdateApplication.md")
- [UpdateComponent](../../../cloudwatch/latest/APIReference/API_UpdateComponent.md "../../../cloudwatch/latest/APIReference/API_UpdateComponent.md")
- [UpdateComponentConfiguration](../../../cloudwatch/latest/APIReference/API_UpdateComponentConfiguration.md "../../../cloudwatch/latest/APIReference/API_UpdateComponentConfiguration.md")
- [UpdateLogPattern](../../../cloudwatch/latest/APIReference/API_UpdateLogPattern.md "../../../cloudwatch/latest/APIReference/API_UpdateLogPattern.md")
- [UpdateProblem](../../../cloudwatch/latest/APIReference/API_UpdateProblem.md "../../../cloudwatch/latest/APIReference/API_UpdateProblem.md")
- [UpdateWorkload](../../../cloudwatch/latest/APIReference/API_UpdateWorkload.md "../../../cloudwatch/latest/APIReference/API_UpdateWorkload.md")

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
