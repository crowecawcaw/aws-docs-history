# Monitoring your Volume Gateway

The topics in this section describe how to monitor Volume Gateway in either cached volume
or stored volume setup, including monitoring the volumes associated with the gateway and
monitoring the upload buffer. You use the AWS Management Console to view metrics for your gateway. For
example, you can view the number of bytes used in read and write operations, the time spent
in read and write operations, and the time taken to retrieve data from the Amazon Web Services cloud.
With metrics, you can track the health of your gateway and set up alarms to notify you when
one or more metrics fall outside a defined threshold.

Storage Gateway provides CloudWatch metrics at no additional charge. Storage Gateway metrics are
recorded for a period of two weeks. By using these metrics, you can access historical
information and get a better perspective on how your gateway and volumes are performing. For
detailed information about CloudWatch, see the [Amazon CloudWatch User
Guide](../../../AmazonCloudWatch/latest/monitoring.md "../../../AmazonCloudWatch/latest/monitoring.md").

**Topics**

- [Getting Volume Gateway health logs with
  Amazon CloudWatch Logs](cw-log-groups-volume.md "cw-log-groups-volume.md") -
  Learn how to use Amazon CloudWatch Logs to get information about the health of your
  Volume Gateway and related resources.
- [Using Amazon CloudWatch Metrics](UsingCloudWatchConsole-common.md "UsingCloudWatchConsole-common.md") - Learn how to get monitoring
  data for your gateway using either the AWS Management Console or the
  CloudWatch API.
- [Measuring Performance Between Your Application
  and Gateway](PerfAppGateway-common.md "PerfAppGateway-common.md") -
  Learn how to measure data throughput, data latency, and operations per second to
  understand performance between your applications and your gateway.
- [Measuring Performance Between Your Gateway and
  AWS](PerfGatewayAWS-common.md "PerfGatewayAWS-common.md") -
  Learn how to measure data throughput, data latency, and operations per second to
  understand performance between your gateway and the AWS cloud.
- [Understanding volume metrics](MonitoringVolumes-common.md "MonitoringVolumes-common.md") - Learn how to measure metrics that provide data about the volumes associated
  with a gateway.
