# Monitoring with Amazon CloudWatch

You can monitor AWS Glue using Amazon CloudWatch, which collects and processes raw data from AWS Glue into
readable, near-real-time metrics. These statistics are recorded for a period of two weeks so
that you can access historical information for a better perspective on how your web application
or service is performing. By default, AWS Glue metrics data is sent to CloudWatch automatically. For more
information, see [What Is Amazon CloudWatch?](../../../AmazonCloudWatch/latest/DeveloperGuide/WhatIsCloudWatch.md "../../../AmazonCloudWatch/latest/DeveloperGuide/WhatIsCloudWatch.md") in the
_Amazon CloudWatch User Guide_, and [AWS Glue metrics](monitoring-awsglue-with-cloudwatch-metrics.md#awsglue-metrics "monitoring-awsglue-with-cloudwatch-metrics.md#awsglue-metrics").

**Continous logging**

AWS Glue also supports real-time continuous logging for AWS Glue jobs. When continuous logging is
enabled for a job, you can view the real-time logs on the AWS Glue console or the CloudWatch console
dashboard. For more information, see [Logging for AWS Glue jobs](monitor-continuous-logging.md "monitor-continuous-logging.md").

**Observability metrics**

When **Job observability metrics** is enabled, additional Amazon CloudWatch metrics are generated when
the job is run. Use AWS Glue Observability metrics to generate insights into what is happening inside your AWS Glue
to improve triaging and analysis of issues.

###### Topics

- [Monitoring AWS Glue using Amazon CloudWatch
  metrics](monitoring-awsglue-with-cloudwatch-metrics.md "monitoring-awsglue-with-cloudwatch-metrics.md")
- [Setting up Amazon CloudWatch alarms on AWS Glue
  job profiles](monitor-profile-glue-job-cloudwatch-alarms.md "monitor-profile-glue-job-cloudwatch-alarms.md")
- [Logging for AWS Glue jobs](monitor-continuous-logging.md "monitor-continuous-logging.md")
- [Monitoring with AWS Glue Observability metrics](monitor-observability.md "monitor-observability.md")
