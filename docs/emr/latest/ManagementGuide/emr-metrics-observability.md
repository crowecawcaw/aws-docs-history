

# EMR Observability Best Practices
<a name="emr-metrics-observability"></a>

EMR Observability encompasses a comprehensive monitoring and management approach for AWS EMR clusters. The foundation rests on Amazon CloudWatch as the primary monitoring service, complemented by EMR Studio, and third-party tools like Prometheus and Grafana for enhanced visibility. In this document, we explore specific aspects of cluster observability:

1. *[Spark observability](https://github.com/aws/aws-emr-best-practices/blob/main/website/docs/bestpractices/Applications/Spark/observability.md)* (GitHub) – With regards to the Spark user interface, you have three options in Amazon EMR.

1. *[Spark troubleshooting](https://github.com/aws/aws-emr-best-practices/blob/main/website/docs/bestpractices/Applications/Spark/troubleshooting.md)* (GitHub) – Resolutions for errors.

1. *[EMR Cluster monitoring](https://aws.github.io/aws-emr-best-practices/docs/bestpractices/Observability/best_practices/) * (GitHub) – Monitoring cluster performance.

1. *[Troubleshooting EMR](https://github.com/aws/aws-emr-best-practices/blob/main/website/docs/bestpractices/Troubleshooting/Troubleshooting%20EMR.md)* (GitHub) – Identify, diagnose, and resolve common EMR cluster problems.

1. *[Cost optimization](https://github.com/aws/aws-emr-best-practices/blob/main/website/docs/bestpractices/Cost%20Optimizations/best_practices.md)* (GitHub) – This section outlines the best practices for running cost-effective workloads.

## Performance Optimization Tool for Apache Spark Applications
<a name="performance-optimization"></a>

1. [AWS EMR Advisor](https://github.com/aws-samples/aws-emr-advisor) tool analyzes Spark event logs to provide tailored recommendations for optimizing EMR cluster configurations, enhancing performance, and reducing costs. By leveraging historical data, it suggests ideal executor sizes and infrastructure settings, enabling more efficient resource utilization and improved overall cluster performance.

1. [Amazon CodeGuru Profiler](https://github.com/amzn/amazon-codeguru-profiler-for-spark) tool helps developers identify performance bottlenecks and inefficiencies in their Spark applications by collecting and analyzing runtime data. The tool integrates seamlessly with existing Spark applications, requiring minimal setup, and provides detailed insights through the AWS Console about CPU usage, memory patterns, and performance hotspots.