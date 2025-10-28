# EMR Observability Best Practices

EMR Observability encompasses a comprehensive monitoring and management approach for AWS EMR clusters. The foundation rests on Amazon CloudWatch as
the primary monitoring service, complemented by EMR Studio, and third-party tools like Prometheus and Grafana for enhanced visibility. In this document, we explore
specific aspects of cluster observability:

1. _[Spark observability](https://github.com/aws/aws-emr-best-practices/blob/main/website/docs/bestpractices/Applications/Spark/observability.md "https://github.com/aws/aws-emr-best-practices/blob/main/website/docs/bestpractices/Applications/Spark/observability.md")_ (GitHub) – With regards to the Spark user interface, you have three options in Amazon EMR.
2. _[Spark troubleshooting](https://github.com/aws/aws-emr-best-practices/blob/main/website/docs/bestpractices/Applications/Spark/troubleshooting.md "https://github.com/aws/aws-emr-best-practices/blob/main/website/docs/bestpractices/Applications/Spark/troubleshooting.md")_ (GitHub) – Resolutions for errors.
3. _[EMR Cluster monitoring](https://aws.github.io/aws-emr-best-practices/docs/bestpractices/Observability/best_practices/ "https://aws.github.io/aws-emr-best-practices/docs/bestpractices/Observability/best_practices/")_ (GitHub) – Monitoring cluster performance.
4. _[Troubleshooting EMR](https://github.com/aws/aws-emr-best-practices/blob/main/website/docs/bestpractices/Troubleshooting/Troubleshooting%20EMR.md "https://github.com/aws/aws-emr-best-practices/blob/main/website/docs/bestpractices/Troubleshooting/Troubleshooting%20EMR.md")_ (GitHub) – Identify, diagnose, and resolve common EMR cluster problems.
5. _[Cost optimization](https://github.com/aws/aws-emr-best-practices/blob/main/website/docs/bestpractices/Cost%20Optimizations/best_practices.md "https://github.com/aws/aws-emr-best-practices/blob/main/website/docs/bestpractices/Cost%20Optimizations/best_practices.md")_ (GitHub) – This section outlines the best practices for
   running cost-effective workloads.

## Performance Optimization Tool for Apache Spark Applications

1. [AWS EMR Advisor](https://github.com/aws-samples/aws-emr-advisor "https://github.com/aws-samples/aws-emr-advisor") tool analyzes Spark event logs to provide tailored recommendations for optimizing EMR cluster configurations, enhancing performance, and
   reducing costs. By leveraging historical data, it suggests ideal executor sizes and infrastructure settings, enabling more efficient resource
   utilization and improved overall cluster performance.
2. [Amazon CodeGuru Profiler](https://github.com/amzn/amazon-codeguru-profiler-for-spark "https://github.com/amzn/amazon-codeguru-profiler-for-spark") tool helps developers identify performance bottlenecks and inefficiencies in their Spark applications by collecting
   and analyzing runtime data. The tool integrates seamlessly with existing Spark applications, requiring minimal setup, and provides
   detailed insights through the AWS Console about CPU usage, memory patterns, and performance hotspots.
