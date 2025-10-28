# Monitoring Amazon Kinesis Video Streams

Monitoring is an important part of maintaining the reliability, availability, and performance of Amazon Kinesis Video Streams and
your AWS solutions. We recommend collecting monitoring data from all of the parts of your AWS solution to help
you debug a multi-point failure, if one occurs. Before you start monitoring Amazon Kinesis Video Streams, we recommend that you create a
monitoring plan that includes answers to the following questions:

- What are your monitoring goals?
- What resources will you monitor?
- How often will you monitor these resources?
- What monitoring tools will you use?
- Who will perform the monitoring tasks?
- Who should be notified when something goes wrong?
  After you've defined your monitoring goals and created your monitoring plan, the next step is to establish a
  baseline for normal Amazon Kinesis Video Streams performance in your environment. You should measure Amazon Kinesis Video Streams performance at various times
  and under different load conditions. As you monitor Amazon Kinesis Video Streams, store a history of monitoring data that you've
  collected. You can compare current Amazon Kinesis Video Streams performance to this historical data to help you identify normal
  performance patterns and performance anomalies, and devise methods to address issues that might arise.

###### Topics

- [Monitor Amazon Kinesis Video Streams metrics with CloudWatch](monitoring-cloudwatch.md "monitoring-cloudwatch.md")
- [Monitor the Amazon Kinesis Video Streams Edge Agent with
  CloudWatch](monitoring-edge-cloudwatch.md "monitoring-edge-cloudwatch.md")
- [Log Amazon Kinesis Video Streams API calls with AWS CloudTrail](monitoring-cloudtrail.md "monitoring-cloudtrail.md")
