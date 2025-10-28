# Monitoring Your Tape Gateway

This topics in this section describe procedures and conceptual information about how to
monitor your Tape Gateway. You can monitor the virtual tapes, cache storage, and the upload
buffer that are associated with your Tape Gateway. You use the AWS Management Console to view metrics
for your Tape Gateway. With metrics, you can track the health of your Tape Gateway and set
up alarms to notify you when one or more metrics are outside a defined threshold.

You can use Amazon CloudWatch Logs to get information about the health of your Tape Gateway and
related resources. You can use the logs to monitor your gateway for errors that it
encounters. In addition, you can use Amazon CloudWatch subscription filters to automate processing of
the log information in real time.

Storage Gateway provides CloudWatch metrics at no additional charge. Storage Gateway metrics are recorded for a
period of two weeks. By using these metrics, you can access historical information and get a
better perspective of how your Tape Gateway and virtual tapes are performing. For detailed
information about CloudWatch, see the [_Amazon CloudWatch User
Guide_](../../../AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.md "../../../AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.md").

Data throughput, data latency, and operations per second are measures that you can use to
understand how your storage applications are performing with Tape Gateway. When you use the
correct aggregation statistic, these values can be measured by using the Storage Gateway metrics
that are provided for you.

###### Topics

- [Getting Tape Gateway health logs with
  CloudWatch log groups](cw-log-groups-tape.md "cw-log-groups-tape.md")
- [Using Amazon CloudWatch
  Metrics](UsingCloudWatchConsole-vtl-common.md "UsingCloudWatchConsole-vtl-common.md")
- [Understanding virtual tape metrics](monitoring-tape.md "monitoring-tape.md")
- [Measuring Performance Between Your
  Tape Gateway and AWS](PerfGatewayAWS-vtl-common.md "PerfGatewayAWS-vtl-common.md")
