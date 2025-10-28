# Monitoring Storage Gateway

This section describes how to monitor a Storage Gateway, including monitoring resources associated
with the gateway, using Amazon CloudWatch. You can monitor the gateway's upload buffer and cache
storage. You use the Storage Gateway console to view metrics and alarms for your gateway. For
example, you can view the number of bytes used in read and write operations, the time spent
in read and write operations, and the time taken to retrieve data from the Amazon Web Services Cloud.
With metrics, you can track the health of your gateway and set up alarms to notify you when
one or more metrics fall outside a defined threshold.

Storage Gateway provides CloudWatch metrics at no additional charge. Storage Gateway metrics are
recorded for a period of two weeks. By using these metrics, you can access historical
information and get a better perspective on how your gateway and volumes are performing.
Storage Gateway also provides CloudWatch alarms, except high-resolution alarms, at no additional
charge. For more information about CloudWatch pricing, see [Amazon CloudWatch pricing](https://aws.amazon.com/cloudwatch/pricing/ "https://aws.amazon.com/cloudwatch/pricing/"). For more information about CloudWatch, see
[Amazon CloudWatch User Guide](../../../AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.md "../../../AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.md").

For information specific to monitoring a Volume Gateway and its
associated resources, see [Monitoring your
Volume Gateway](monitoring-volume-gateway.md "monitoring-volume-gateway.md").

###### Topics

- [Understanding gateway metrics](MonitoringGateways-common.md "MonitoringGateways-common.md")
- [Monitoring the upload buffer](PerfUploadBuffer-common.md "PerfUploadBuffer-common.md")
- [Monitoring cache storage](PerfCache-common.md "PerfCache-common.md")
- [Understanding CloudWatch alarms](cloudwatch-alarms.md "cloudwatch-alarms.md")
- [Creating recommended CloudWatch alarms
  for your gateway](cloudwatch-alarms-create-recommended.md "cloudwatch-alarms-create-recommended.md")
- [Creating a custom CloudWatch alarm for your
  gateway](cloudwatch-alarms-create-alarm.md "cloudwatch-alarms-create-alarm.md")
- [Monitoring your Volume Gateway](monitoring-volume-gateway.md "monitoring-volume-gateway.md")
