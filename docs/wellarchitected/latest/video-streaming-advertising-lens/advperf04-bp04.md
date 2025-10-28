# ADVPERF04-BP04 Enable detailed performance and observability monitoring to help tune queries and refine compute and storage

Provide access to necessary tools and metric granularity for
performance debugging and compute and storage optimization, in
particular because of the low latency requirements for advertising
workloads.

## Implementation guidance

Enable Amazon RDS enhanced monitoring, which provides deeper
visibility into database performance and health. This heightened
visibility helps you diagnose issues faster and optimize
database workloads.

Enable
[Amazon EKS Container Insights](../../../AmazonCloudWatch/latest/monitoring/deploy-container-insights-EKS.md "../../../AmazonCloudWatch/latest/monitoring/deploy-container-insights-EKS.md") to provide observability into
cluster health, performance, logs, and billing for container
workloads. This helps you run and optimize Kubernetes
applications efficiently on Amazon EKS while reducing monitoring
costs. The automated dashboards and analytics simplify
troubleshooting.

## Key AWS services

- [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/ "https://aws.amazon.com/cloudwatch/")

## Resources

- [Monitor real-time Amazon RDS OS metrics with flexible granularity
  using Enhanced Monitoring](https://aws.amazon.com/blogs/database/monitor-real-time-amazon-rds-os-metrics-with-flexible-granularity-using-enhanced-monitoring/ "https://aws.amazon.com/blogs/database/monitor-real-time-amazon-rds-os-metrics-with-flexible-granularity-using-enhanced-monitoring/")
- [Optimizing AdTech end-user experiences Using Amazon CloudWatch Internet Monitor](https://aws.amazon.com/blogs/networking-and-content-delivery/optimizing-adtech-end-user-experiences-using-amazon-cloudwatch-internet-monitor/ "https://aws.amazon.com/blogs/networking-and-content-delivery/optimizing-adtech-end-user-experiences-using-amazon-cloudwatch-internet-monitor/")
- [Tuning Amazon RDS for MySQL with Performance
  Insights](https://aws.amazon.com/blogs/database/tuning-amazon-rds-for-mysql-with-performance-insights/ "https://aws.amazon.com/blogs/database/tuning-amazon-rds-for-mysql-with-performance-insights/")
- [Analyze
  Amazon Aurora MySQL Workloads with Performance Insights](https://aws.amazon.com/blogs/database/analyze-amazon-aurora-mysql-workloads-with-performance-insights/ "https://aws.amazon.com/blogs/database/analyze-amazon-aurora-mysql-workloads-with-performance-insights/")
- [Announcing
  Amazon CloudWatch Container Insights with Enhanced Observability for Amazon EKS on EC2](https://aws.amazon.com/blogs/mt/new-container-insights-with-enhanced-observability-for-amazon-eks/ "https://aws.amazon.com/blogs/mt/new-container-insights-with-enhanced-observability-for-amazon-eks/")
