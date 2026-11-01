

# Monitoring License Manager
<a name="monitoring-overview"></a>

You can monitor the usage of licenses and subscriptions tracked in AWS License Manager using Amazon CloudWatch. CloudWatch collects raw data and processes it into readable, near real-time metrics. You can set alarms that watch for certain thresholds, and send notifications or take actions when those thresholds are met. For more information, see [Monitoring License Manager with Amazon CloudWatch](monitoring-cloudwatch.md).

You can capture API calls and related events made by or on behalf of your AWS account using AWS CloudTrail. Events are captured as log files and delivered to an Amazon S3 bucket that you specify. You can identify which users and accounts called AWS, the source IP address from which the calls were made, and when the calls occurred. For more information, see [Logging AWS License Manager API calls using AWS CloudTrail](logging-using-cloudtrail.md).

You can respond to license and grant changes by using Amazon EventBridge. AWS License Manager sends an event to EventBridge whenever a license or grant changes state. You can use these events to automate workflows and notifications without polling the License Manager API. For more information, see [Monitoring License Manager with Amazon EventBridge](monitoring-eventbridge.md).

**Contents**
+ [Monitoring License Manager with Amazon CloudWatch](monitoring-cloudwatch.md)
  + [Creating alarms to monitor License Manager metrics](monitoring-cloudwatch.md#monitoring-cloudwatch-alarms)
+ [Monitoring License Manager with Amazon EventBridge](monitoring-eventbridge.md)
  + [License Manager event recipients and patterns](monitoring-eventbridge-recipients.md)
    + [Create an event pattern](monitoring-eventbridge-recipients.md#monitoring-eventbridge-patterns)
  + [License Manager event structure and change events](monitoring-eventbridge-events.md)
    + [Event structure](monitoring-eventbridge-events.md#monitoring-eventbridge-structure)
    + [Event types](monitoring-eventbridge-events.md#monitoring-eventbridge-change-events)
  + [Logging AWS License Manager API calls using AWS CloudTrail](logging-using-cloudtrail.md)
    + [License Manager information in CloudTrail](license-manager-info-in-cloudtrail.md)
    + [Understanding License Manager log file entries](understanding-license-manager-entries.md)