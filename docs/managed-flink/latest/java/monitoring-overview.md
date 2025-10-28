Amazon Managed Service for Apache Flink (Amazon MSF) was previously known as Amazon Kinesis Data Analytics for Apache Flink.

# Logging and monitoring in Amazon Managed Service for Apache Flink

Monitoring is an important part of maintaining the reliability, availability, and
performance of Managed Service for Apache Flink applications. You should collect monitoring
data from all of the parts of your AWS solution so that you can more easily debug a
multipoint failure if one occurs.

Before you start monitoring Managed Service for Apache Flink, you should create a monitoring plan that includes
answers to the following questions:

- What are your monitoring goals?
- What resources will you monitor?
- How often will you monitor these resources?
- What monitoring tools will you use?
- Who will perform the monitoring tasks?
- Who should be notified when something goes wrong?
  The next step is to establish a baseline for normal Managed Service for Apache Flink performance in your environment.
  You do this by measuring performance at various times and under different load conditions.
  As you monitor Managed Service for Apache Flink, you can store historical monitoring data. You can then compare it
  with current performance data, identify normal performance patterns and performance
  anomalies, and devise methods to address issues.

###### Topics

- [Logging in Managed Service for Apache Flink](logging.md "logging.md")
- [Monitoring in Managed Service for Apache Flink](monitoring.md "monitoring.md")
- [Set up application logging in Managed Service for Apache Flink](cloudwatch-logs.md "cloudwatch-logs.md")
- [Analyze logs with CloudWatch Logs Insights](cloudwatch-logs-reading.md "cloudwatch-logs-reading.md")
- [Metrics and dimensions in Managed Service for Apache Flink](metrics-dimensions.md "metrics-dimensions.md")
- [Write custom messages to CloudWatch Logs](cloudwatch-logs-writing.md "cloudwatch-logs-writing.md")
- [Log Managed Service for Apache Flink API calls with AWS CloudTrail](logging-using-cloudtrail.md "logging-using-cloudtrail.md")
