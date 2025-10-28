End of support notice: On May 20, 2026, AWS will end support for
AWS IoT Events. After May 20, 2026, you will no longer be able to access the AWS IoT Events console or AWS IoT Events
resources. For more information, see [AWS IoT Events end of
support](iotevents-end-of-support.md "iotevents-end-of-support.md").

# Available tools to monitor AWS IoT Events

AWS provides various tools that you can use to monitor AWS IoT Events. You can configure some of
these tools to do the monitoring for you, while some of the tools require manual intervention.
We recommend that you automate monitoring tasks as much as possible.

## Automated monitoring tools

You can use the following automated monitoring tools to watch AWS IoT Events and report when
something is wrong:

- **Amazon CloudWatch Logs** – Monitor, store, and access your log files
  from AWS CloudTrail or other sources. For more information, see [Using Amazon CloudWatch
  dashboards](../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md "../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md") in the _Amazon CloudWatch User Guide_.
- **AWS CloudTrail Log Monitoring** – Share log files between
  accounts, monitor CloudTrail log files in real time by sending them to CloudWatch Logs, write
  log-processing applications in Java, and validate that your log files have not changed
  after delivery by CloudTrail. For more information, see [Working with CloudTrail log
  files](../../../awscloudtrail/latest/userguide/cloudtrail-working-with-log-files.md "../../../awscloudtrail/latest/userguide/cloudtrail-working-with-log-files.md") in the _AWS CloudTrail User Guide_.

## Manual monitoring tools

Another important part of monitoring AWS IoT Events involves manually monitoring those items that
the CloudWatch alarms don't cover. The AWS IoT Events, CloudWatch, and other AWS console dashboards provide an
at-a-glance view of the state of your AWS environment. We recommend that you also check
the log files on AWS IoT Events.

- The AWS IoT Events console shows:
  - Detector models
  - Detectors
  - Inputs
  - Settings

- The CloudWatch home page shows:

      + Current alarms and status
      + Graphs of alarms and resources
      + Service health status

  In addition, you can use CloudWatch to do the following:

      + Create [Creating a CloudWatch
       dashboard](../../../AmazonCloudWatch/latest/monitoring/create_dashboard.md "../../../AmazonCloudWatch/latest/monitoring/create_dashboard.md") to monitor the services you care about
      + Graph metric data to troubleshoot issues and discover trends
      + Search and browse all your AWS resource metrics
      + Create and edit alarms to be notified of problems
