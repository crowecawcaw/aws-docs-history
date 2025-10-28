# Monitoring overview on Amazon MWAA

This page describes the AWS services used to monitor an Amazon Managed Workflows for Apache Airflow environment.

###### Contents

- [Amazon CloudWatch overview](monitoring-overview.md#monitoring-metrics-cw-about "monitoring-overview.md#monitoring-metrics-cw-about")
- [AWS CloudTrail overview](monitoring-overview.md#monitoring-metrics-ct-about "monitoring-overview.md#monitoring-metrics-ct-about")

## Amazon CloudWatch overview

CloudWatch is a metrics repository for AWS services that you can use to retrieve statistics based on the [metrics](../../../AmazonCloudWatch/latest/monitoring/cloudwatch_concepts.md#Metric "../../../AmazonCloudWatch/latest/monitoring/cloudwatch_concepts.md#Metric") and [dimensions](../../../AmazonCloudWatch/latest/monitoring/cloudwatch_concepts.md#Dimension "../../../AmazonCloudWatch/latest/monitoring/cloudwatch_concepts.md#Dimension") published by a service. You can use these metrics to configure [alarms](../../../AmazonCloudWatch/latest/monitoring/cloudwatch_concepts.md#CloudWatchAlarms "../../../AmazonCloudWatch/latest/monitoring/cloudwatch_concepts.md#CloudWatchAlarms"), calculate statistics and then present the data in a [dashboard](../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md "../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md") that helps you assess the health of your environment in the Amazon CloudWatch console.

Apache Airflow is already set up to send [StatsD](https://github.com/etsy/statsd "https://github.com/etsy/statsd") metrics for an Amazon Managed Workflows for Apache Airflow environment to Amazon CloudWatch.

To learn more, refer to [What is Amazon CloudWatch?](../../../AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.md "../../../AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.md").

## AWS CloudTrail overview

CloudTrail is an auditing service that provides a record of actions taken by a user, role, or an AWS service in Amazon MWAA. Using the information collected by CloudTrail, you can determine the request that was made to Amazon MWAA, the IP address from which the request was made, who made the request, when it was made, and additional details available in audit logs.

To learn more, refer to [What is AWS CloudTrail?](../../../awscloudtrail/latest/userguide/cloudtrail-user-guide.md "../../../awscloudtrail/latest/userguide/cloudtrail-user-guide.md").
