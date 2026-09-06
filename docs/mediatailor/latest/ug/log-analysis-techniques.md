

# CDN log analysis tools and monitoring techniques for MediaTailor
<a name="log-analysis-techniques"></a>

AWS Elemental MediaTailor content delivery network (CDN) integration generates large volumes of log data that require efficient analysis tools and techniques. Use these approaches to efficiently analyze content delivery network and MediaTailor logs:
+ **Command-line analysis:** Use tools like `grep`, `awk`, and `sort` to filter and analyze log patterns
+ **Amazon CloudWatch Logs Insights:** Query CDN and MediaTailor logs with SQL-like syntax for advanced analysis
+ **Third-party tools:** Consider log analysis platforms for comprehensive monitoring and alerting
+ **Custom dashboards:** Create visualizations that combine CDN metrics with MediaTailor performance data

If you need additional assistance with log analysis or interpreting complex error patterns, see [Get CDN integration support](cdn-get-help.md).

**Log analysis tools and resources:**
+ [CloudWatch Logs Insights](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/AnalyzingLogData.html) - SQL-like queries for log analysis
+ [Amazon OpenSearch Service](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/what-is.html) - Advanced log search and analytics
+ [CloudWatch dashboards](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.html) - Custom visualization and monitoring
+ [Instrumenting distributed systems for operational visibility](https://aws.amazon.com/builders-library/instrumenting-distributed-systems-for-operational-visibility/) - Advanced observability patterns
+ [Design workload observability](https://docs.aws.amazon.com/wellarchitected/latest/operational-excellence-pillar/design-workload-observability.html) - Well-Architected observability guidance