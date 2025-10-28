For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified
data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](timestream-for-influxdb.md "timestream-for-influxdb.md").

# Logging and monitoring in Timestream for LiveAnalytics

Monitoring is an important part of maintaining the reliability, availability, and
performance of Timestream for LiveAnalytics and your AWS solutions. You should collect monitoring data from all of the
parts of your AWS solution so that you can more easily debug a multi-point failure if one
occurs. However, before you start monitoring Timestream for LiveAnalytics, you should create a monitoring plan that
includes answers to the following questions:

- What are your monitoring goals?
- What resources will you monitor?
- How often will you monitor these resources?
- What monitoring tools will you use?
- Who will perform the monitoring tasks?
- Who should be notified when something goes wrong?
  The next step is to establish a baseline for normal Timestream for LiveAnalytics performance in your environment, by
  measuring performance at various times and under different load conditions. As you monitor Timestream for LiveAnalytics,
  store historical monitoring data so that you can compare it with current performance data,
  identify normal performance patterns and performance anomalies, and devise methods to address
  issues.

To establish a baseline, you should, at a minimum, monitor the following items:

- System errors, so that you can determine whether any requests resulted in an
  error.

###### Topics

- [Monitoring tools](monitoring-automated-manual.md "monitoring-automated-manual.md")
- [Logging Timestream for LiveAnalytics API calls with AWS CloudTrail](logging-using-cloudtrail.md "logging-using-cloudtrail.md")
