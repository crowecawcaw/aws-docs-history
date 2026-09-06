

# Logging Amazon GuardDuty API calls with AWS CloudTrail
<a name="logging-using-cloudtrail"></a>

Amazon GuardDuty is integrated with AWS CloudTrail, a service that provides a record of actions taken by a user, role, or an AWS service in GuardDuty. CloudTrail captures all API calls for GuardDuty as events, including calls from the GuardDuty console and from code calls to the GuardDuty APIs. If you create a trail, you can enable continuous delivery of CloudTrail events to an Amazon Simple Storage Service (Amazon S3) bucket, including events for GuardDuty. If you don't configure a trail, you can still view the most recent events in the CloudTrail console in **Event history**. Using the information collected by CloudTrail, you can determine the request that was made to GuardDuty, the IP address the request was made from, who made the request, when it was made, and additional details. 

For more information about CloudTrail, including how to configure and enable it, see the *[AWS CloudTrail User Guide](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/)*.

## GuardDuty information in CloudTrail
<a name="service-name-info-in-cloudtrail"></a>

CloudTrail is enabled on your AWS account when you create the account. When supported event activity occurs in GuardDuty, that activity is recorded in a CloudTrail event along with other AWS service events in **Event history**. You can view, search, and download recent events in your AWS account. For more information, see [Viewing events with CloudTrail event history](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/view-cloudtrail-events.html). 

For an ongoing record of events in your AWS account, including events for GuardDuty, create a trail. A trail enables CloudTrail to deliver log files to an Amazon S3 bucket. By default, when you create a trail in the console, the trail applies to all Regions. The trail logs events from all Regions in the AWS partition and delivers the log files to the Amazon S3 bucket that you specify. Additionally, you can configure other AWS services to further analyze and act upon the event data collected in CloudTrail logs. For more information, see: 
+ [Overview for creating a trail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-create-and-update-a-trail.html)
+ [CloudTrail supported services and integrations](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-aws-service-specific-topics.html)
+ [Configuring Amazon SNS notifications for CloudTrail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/getting_notifications_top_level.html)
+ [Receiving CloudTrail log files from multiple regions](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/receive-cloudtrail-log-files-from-multiple-regions.html) and [Receiving CloudTrail log files from multiple accounts](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-receive-logs-from-multiple-accounts.html)

Every event or log entry contains information about who generated the request. The identity information helps you determine the following: 
+ Whether the request was made with root user or IAM user's sign-in credentials
+ Whether the request was made with temporary security credentials for a role or federated user
+ Whether the request was made by another AWS service

For more information, see [CloudTrail userIdentity element](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-event-reference-user-identity.html).

## GuardDuty control plane events in CloudTrail
<a name="guardduty-control-plane-events-in-cloudtrail"></a>

By default, CloudTrail logs all the GuardDuty API operations provided in the [Amazon GuardDuty API Reference](https://docs.aws.amazon.com/guardduty/latest/APIReference/) as events in CloudTrail files.

## GuardDuty data events in CloudTrail
<a name="guardduty-data-events-in-cloudtrail"></a>

[GuardDuty Runtime Monitoring](runtime-monitoring.md) uses a GuardDuty security agent deployed to your Amazon Elastic Kubernetes Service (Amazon EKS) clusters, Amazon Elastic Compute Cloud (Amazon EC2) instances, and AWS Fargate (Amazon Elastic Container Service (Amazon ECS) only) tasks to collect add-on (`aws-guardduty-agent`) that collects [Collected runtime event types](runtime-monitoring-collected-events.md) for your AWS workloads and then send them to GuardDuty for threat detection and analysis.

### Logging and monitoring data events
<a name="runtime-monitoring-add-on-cloudtrail-logs"></a>

You can optionally configure the AWS CloudTrail logs to view the data events for your GuardDuty security agent. 

To create and configure CloudTrail, see [Data events](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/logging-data-events-with-cloudtrail.html#logging-data-events) in the *AWS CloudTrail User Guide* and follow the instructions for **Logging data events with advanced event selectors in the AWS Management Console**. While logging the trail, ensure to make the following changes:
+ For the **Data event type**, choose **GuardDuty detector**.
+ For the **Log selector template**, choose **Log all events**.
+ Expand the **JSON view** for the configuration. It should be similar to the following JSON:

  ```
  [
    {
      "name": "",
      "fieldSelectors": [
        {
          "field": "eventCategory",
          "equals": [
            "Data"
          ]
        },
        {
          "field": "resources.type",
          "equals": [
            "AWS::GuardDuty::Detector"
          ]
        }
      ]
    }
  ]
  ```

After you enable the selector for the trail, navigate to the Amazon S3 console at [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/). You can download the data events from your S3 bucket chosen at the time of configuring the CloudTrail logs.