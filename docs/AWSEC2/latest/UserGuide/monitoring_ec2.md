# Monitor Amazon EC2 resources

Monitoring is an important part of maintaining the reliability, availability, and
performance of your Amazon EC2 instances and your AWS solutions. You should collect
monitoring data from all of the parts in your AWS solutions so that you can more easily
debug a multi-point failure if one occurs.

AWS provides various tools that you can use to monitor Amazon EC2. The Amazon EC2 and CloudWatch
console dashboards provide an at-a-glance view of the state of your Amazon EC2 environment.
In addition, we provide the following:

- **System status checks** – Monitor the AWS systems
  required to use your instance to ensure that they are working properly.
  These checks detect problems with your instance that require AWS involvement
  to repair. When a system status check fails, you can choose to wait for AWS
  to fix the issue or you can resolve it yourself (for example, by stopping
  and restarting or terminating and replacing an instance). Examples of
  problems that cause system status checks to fail include:

      + Loss of network connectivity
      + Loss of system power
      + Software issues on the physical host
      + Hardware issues on the physical host that impact network
       reachability

  For more information, see [Status checks for Amazon EC2
  instances](monitoring-system-instance-status-check.md "monitoring-system-instance-status-check.md").

- **Instance status checks** – Monitor the software
  and network configuration of your individual instance. These checks detect
  problems that require your involvement to repair. When an instance status
  check fails, typically you will need to address the problem yourself (for
  example, by rebooting the instance or by making modifications in your
  operating system). Examples of problems that may cause instance status
  checks to fail include:

      + Failed system status checks
      + Misconfigured networking or startup configuration
      + Exhausted memory
      + Corrupted file system
      + Incompatible kernel

  For more information, see [Status checks for Amazon EC2
  instances](monitoring-system-instance-status-check.md "monitoring-system-instance-status-check.md").

- **Amazon CloudWatch alarms** – Watch a single metric over a
  time period you specify, and perform one or more actions based on the value
  of the metric relative to a given threshold over a number of time periods.
  The action is a notification sent to an Amazon Simple Notification Service (Amazon SNS) topic or Amazon EC2 Auto Scaling
  policy. Alarms invoke actions for sustained state changes only. CloudWatch alarms
  will not invoke actions simply because they are in a particular state; the
  state must have changed and been maintained for a specified number of
  periods. For more information, see [Monitor your instances using CloudWatch](using-cloudwatch.md "using-cloudwatch.md").
- **Amazon EventBridge events** – Automate your AWS services and
  respond automatically to system events. Events from AWS services are
  delivered to EventBridge in near real time, and you can specify automated actions
  to take when an event matches a rule you write. For more information, see
  [Automate Amazon EC2 using EventBridge](automating_with_eventbridge.md "automating_with_eventbridge.md").
- **AWS CloudTrail logs** – Capture detailed information
  about the calls made to the Amazon EC2 API and stores them as log files in Amazon S3.
  You can use CloudTrail logs to determine which calls were made, the source IP
  address for the call, who made the call, and when the call was made. For
  more information, see [Log Amazon EC2 API calls using AWS CloudTrail](monitor-with-cloudtrail.md "monitor-with-cloudtrail.md").
- **CloudWatch agent** – Collect logs and system-level
  metrics from both hosts and guests on your EC2 instances and on-premises
  servers. For more information, see [Collecting Metrics and Logs from Amazon EC2 Instances and On-Premises
  Servers with the CloudWatch Agent](../../../AmazonCloudWatch/latest/monitoring/Install-CloudWatch-Agent.md "../../../AmazonCloudWatch/latest/monitoring/Install-CloudWatch-Agent.md") in the _Amazon CloudWatch User Guide_.
