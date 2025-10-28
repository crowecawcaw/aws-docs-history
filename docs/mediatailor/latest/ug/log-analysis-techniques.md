# CDN log analysis tools and monitoring

techniques for MediaTailor

AWS Elemental MediaTailor content delivery network (CDN) integration generates large volumes of log
data that require efficient analysis tools and techniques. Use these approaches to
efficiently analyze content delivery network and MediaTailor logs:

- **Command-line analysis:** Use tools like
  `grep`, `awk`, and `sort` to filter and
  analyze log patterns
- **Amazon CloudWatch Logs Insights:** Query CDN and MediaTailor
  logs with SQL-like syntax for advanced analysis
- **Third-party tools:** Consider log analysis
  platforms for comprehensive monitoring and alerting
- **Custom dashboards:** Create visualizations that
  combine CDN metrics with MediaTailor performance data
  If you need additional assistance with log analysis or interpreting complex error
  patterns, see [Get CDN integration support](cdn-get-help.md "cdn-get-help.md").

**Log analysis tools and resources:**

- [CloudWatch Logs Insights](../../../AmazonCloudWatch/latest/logs/AnalyzingLogData.md "../../../AmazonCloudWatch/latest/logs/AnalyzingLogData.md") - SQL-like queries for log analysis
- [Amazon OpenSearch Service](../../../opensearch-service/latest/developerguide/what-is.md "../../../opensearch-service/latest/developerguide/what-is.md") - Advanced log search and analytics
- [CloudWatch dashboards](../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md "../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md") - Custom visualization and monitoring
- [Instrumenting distributed systems for operational visibility](https://aws.amazon.com/builders-library/instrumenting-distributed-systems-for-operational-visibility/ "https://aws.amazon.com/builders-library/instrumenting-distributed-systems-for-operational-visibility/") -
  Advanced observability patterns
- [Design workload observability](../../../wellarchitected/latest/operational-excellence-pillar/design-workload-observability.md "../../../wellarchitected/latest/operational-excellence-pillar/design-workload-observability.md") - Well-Architected observability
  guidance
