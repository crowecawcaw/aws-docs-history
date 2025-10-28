Amazon FSx File Gateway is no longer available to new customers. Existing
customers of FSx File Gateway can continue to use the service normally. For capabilities
similar to FSx File Gateway, visit [this blog post](https://aws.amazon.com/blogs/storage/switch-your-file-share-access-from-amazon-fsx-file-gateway-to-amazon-fsx-for-windows-file-server/ "https://aws.amazon.com/blogs/storage/switch-your-file-share-access-from-amazon-fsx-file-gateway-to-amazon-fsx-for-windows-file-server/").

# Monitoring Storage Gateway

The topics in this section describe how to monitor a gateway using Amazon CloudWatch, including
monitoring cache storage and other resources associated with the gateway. You use the
Storage Gateway console to view metrics and alarms for your gateway. For example, you can view the
number of bytes used in read and write operations, the time spent in read and write
operations, and the time taken to retrieve data from the AWS Cloud. With metrics, you can
track the health of your gateway and set up alarms to notify you when one or more metrics
fall outside a defined threshold.

Storage Gateway provides CloudWatch metrics at no additional charge. Storage Gateway metrics are
recorded for a period of two weeks. By using these metrics, you can access historical
information and get a better perspective on how your gateways are performing. Storage Gateway
also provides CloudWatch alarms, except high-resolution alarms, at no additional charge. For more
information about CloudWatch pricing, see [Amazon CloudWatch pricing](https://aws.amazon.com/cloudwatch/pricing/ "https://aws.amazon.com/cloudwatch/pricing/"). For more information about CloudWatch, see the [Amazon CloudWatch User Guide](../../../AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.md "../../../AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.md").

###### Topics

- [Understanding CloudWatch alarms](cloudwatch-alarms.md "cloudwatch-alarms.md") - Learn
  basic information about CloudWatch alarms, including alarm states and recommended
  configurations.
- [Create recommended
  CloudWatch alarms](cloudwatch-alarms-create-recommended.md "cloudwatch-alarms-create-recommended.md") - Learn how you can
  quickly and automatically configure all recommended CloudWatch alarms as part of the
  initial File Gateway setup process.
- [Create a custom CloudWatch
  alarm](cloudwatch-alarms-create-alarm.md "cloudwatch-alarms-create-alarm.md") - Learn how you can
  create a custom CloudWatch alarm to monitor a specific metric using specific evaluation
  criteria to trigger alarm states and send notifications.
- [Monitoring your FSx File Gateway](monitoring-file-gateway.md "monitoring-file-gateway.md")

* Learn how to view CloudWatch logs and audit logs, and find information about the
  specific gateway and file sharefile system metrics
  that are reported by your gateway.
