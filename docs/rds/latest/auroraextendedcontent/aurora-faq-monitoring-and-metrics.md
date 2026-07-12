# Monitoring and Metrics

###### Topics

- [What is CloudWatch Database Insights?](#aurora-faq-what-is-cloudwatch-database-insights "#aurora-faq-what-is-cloudwatch-database-insights")
- [What is Amazon DevOps Guru for RDS?](#aurora-faq-what-is-amazon-devops-guru-for-rds "#aurora-faq-what-is-amazon-devops-guru-for-rds")
- [What is the difference between CloudWatch Database Insights and DevOps Guru?](#aurora-faq-what-is-the-difference-between-cloudwatch-database-insights- "#aurora-faq-what-is-the-difference-between-cloudwatch-database-insights-")
- [How does CloudWatch Database Insights collect telemetry?](#aurora-faq-how-does-cloudwatch-database-insights-collect-telemetry "#aurora-faq-how-does-cloudwatch-database-insights-collect-telemetry")

## What is CloudWatch Database Insights?

[CloudWatch Database Insights](../../../AmazonCloudWatch/latest/monitoring/Database-Insights.md "../../../AmazonCloudWatch/latest/monitoring/Database-Insights.md") is a monitoring solution that simplifies database troubleshooting by automating telemetry collection — metrics, logs, and traces — without manual setup. Key benefits include:

- Pre-built dashboards and alarms for monitoring database performance
- AI/ML anomaly detection to reduce manual troubleshooting
- Fleet and instance-level views for both high-level monitoring and root cause analysis
- Application context monitoring to correlate database and application performance
- Integration with [Amazon CloudWatch Application Signals](https://aws.amazon.com/cloudwatch/ "https://aws.amazon.com/cloudwatch/") and AWS X-Ray

## What is Amazon DevOps Guru for RDS?

[Amazon DevOps Guru for RDS](https://aws.amazon.com/devops-guru/features/devops-guru-for-rds/ "https://aws.amazon.com/devops-guru/features/devops-guru-for-rds/") is an ML-powered capability that automatically detects and diagnoses database performance and operational issues, enabling resolution in minutes rather than days. It analyzes telemetry from [CloudWatch Database Insights](../../../AmazonCloudWatch/latest/monitoring/Database-Insights.md "../../../AmazonCloudWatch/latest/monitoring/Database-Insights.md") to identify issues like lock pile-ups, connection storms, SQL regressions, CPU/I/O contention, and memory issues — making database administration more accessible to non-experts.

How can I get started with Amazon DevOps Guru for RDS?

To [get started with DevOps Guru for RDS](../../../devops-guru/latest/userguide/working-with-rds.enabling.md "../../../devops-guru/latest/userguide/working-with-rds.enabling.md"), enable CloudWatch Database Insights through the RDS console, then enable DevOps Guru for your Aurora databases. You can scope analysis to your entire AWS account, specific [AWS CloudFormation](https://aws.amazon.com/cloudformation/ "https://aws.amazon.com/cloudformation/") stacks, or use AWS tags. DevOps Guru publishes insights to the AWS/DevOps-Guru namespace in CloudWatch, so you can monitor anomalies alongside your database metrics in a single dashboard.

## What is the difference between CloudWatch Database Insights and DevOps Guru?

[CloudWatch Database Insights](../../../AmazonCloudWatch/latest/monitoring/Database-Insights.md "../../../AmazonCloudWatch/latest/monitoring/Database-Insights.md") monitors Aurora resources in real time with customizable dashboards, pre-built alarms, and fleet-level monitoring. It inherits all [RDS Performance Insights](https://aws.amazon.com/rds/performance-insights/ "https://aws.amazon.com/rds/performance-insights/") capabilities and adds application performance integration and correlation of database metrics with logs and events. [DevOps Guru](https://aws.amazon.com/devops-guru/ "https://aws.amazon.com/devops-guru/") uses ML to analyze metrics over time, detect anomalies, and offer insights and recommendations. You can monitor DevOps Guru insights via the AWS/DevOps-Guru namespace in CloudWatch for a single-pane-of-glass view.

## How does CloudWatch Database Insights collect telemetry?

CloudWatch Database Insights automates telemetry collection, including metrics, logs, and traces, eliminating the need for manual setup and configuration. By consolidating this telemetry into Amazon CloudWatch, it provides a unified view of database performance and health.
