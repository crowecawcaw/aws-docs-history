End of support notice: On November 13, 2025, AWS will discontinue support for Amazon Elastic Transcoder. After November 13, 2025, you will no longer be able to access the Elastic Transcoder console or Elastic Transcoder resources.

For more information about transitioning to AWS Elemental MediaConvert, visit this [blog post](https://aws.amazon.com/blogs/media/how-to-migrate-workflows-from-amazon-elastic-transcoder-to-aws-elemental-mediaconvert/ "https://aws.amazon.com/blogs/media/how-to-migrate-workflows-from-amazon-elastic-transcoder-to-aws-elemental-mediaconvert/").

# Monitoring with Amazon CloudWatch

You can monitor pipelines and operations using CloudWatch, which collects and
processes raw data from Elastic Transcoder into readable, near real-time
metrics. These statistics are recorded for a period of two weeks, so that you can access
historical information and gain a better perspective on how your web application or service is
performing. By default, Elastic Transcoder metric data is automatically
sent to CloudWatch in 1-minute periods. For more information, see
[What Are Amazon CloudWatch, Amazon CloudWatch Events, and Amazon CloudWatch Logs?](../../../AmazonCloudWatch/latest/DeveloperGuide/WhatIsCloudWatch.md "../../../AmazonCloudWatch/latest/DeveloperGuide/WhatIsCloudWatch.md") in the _Amazon CloudWatch User Guide_.

###### Topics

- [Elastic Transcoder Metrics and Dimensions](metrics-dimensions.md "metrics-dimensions.md")
- [How Do I Use Elastic Transcoder Metrics?](#how-to-use-metrics "#how-to-use-metrics")
- [Creating CloudWatch Alarms to Monitor Elastic Transcoder](creating-alarms.md "creating-alarms.md")

## How Do I Use Elastic Transcoder Metrics?

The metrics reported by Elastic Transcoder provide information that
you can analyze in different ways. The list below shows some common uses for the metrics.
These are suggestions to get you started, not a comprehensive list.

- [How can I track the wait time before my job is started?](creating-alarms.md#track-standby "creating-alarms.md#track-standby")
- [How can I be notified when a job fails due to an error?](creating-alarms.md#track-jobs-errored "creating-alarms.md#track-jobs-errored")
- [How can I be notitifed when a job completes?](creating-alarms.md#track-jobs-completed "creating-alarms.md#track-jobs-completed")
