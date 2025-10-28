# Monitor AWS Batch

Monitoring is an important part of maintaining the reliability, availability, and
performance of AWS Batch and your AWS solution.

We strongly encourage you to collect monitoring data from all parts of your AWS solution
to make it easier to debug a multi-point failure, if one occurs. Start by creating a monitoring
plan that answers the following questions. If you're not sure how to answer these, you can still
use Amazon CloudWatch Logs to establish your performance baselines.

- What are your monitoring goals?
- Which resources will you monitor?
- How often will you monitor these resources?
- Which monitoring tools will you use?
- Who will perform the monitoring tasks?
- Who should be notified when something goes wrong?
  Your next step is to establish a
  baseline of normal AWS Batch performance in your environment by measuring performance at
  various times and under different load conditions. As you monitor AWS Batch, keep historical
  monitoring data so that you can compare it with current performance data. This will help you identify normal performance patterns and performance anomalies, and devise methods to address
  issues.

The topics in this section can help you start logging and monitoring AWS Batch.

###### Topics

- [Using CloudWatch Logs with AWS Batch](using_cloudwatch_logs.md "using_cloudwatch_logs.md")
- [AWS Batch CloudWatch Container Insights](cloudwatch-container-insights.md "cloudwatch-container-insights.md")
- [Use CloudWatch Logs to monitor AWS Batch on Amazon EKS jobs](batch-eks-cloudwatch-logs.md "batch-eks-cloudwatch-logs.md")
