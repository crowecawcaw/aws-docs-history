# Monitoring AWS Parallel Computing Service with Amazon CloudWatch

Amazon CloudWatch provides monitoring of your AWS Parallel Computing Service (AWS PCS) cluster health and
performance by collecting metrics from the cluster at intervals. These metrics are retained,
allowing you to access historical data and gain insights into your cluster's performance over
time.

CloudWatch also enables you to monitor the EC2 instances launched by AWS PCS to meet your
scaling requirements. While you can inspect logs on running instances, CloudWatch metrics and
logging data are typically deleted once instances are terminated. However, you can configure
the CloudWatch agent on instances using an EC2 launch template to persist metrics and logs even
after instance termination, enabling long-term monitoring and analysis.

Explore the topics in this section to learn more about monitoring AWS PCS using CloudWatch.

###### Topics

- [Monitoring AWS PCS metrics using
  CloudWatch](monitoring-cloudwatch_metrics.md "monitoring-cloudwatch_metrics.md")
- [Monitoring AWS PCS instances using
  Amazon CloudWatch](monitoring-cloudwatch_instances.md "monitoring-cloudwatch_instances.md")
