# [O.DIP.2] Centralize logs for enhanced security investigations

**Category:** FOUNDATIONAL 

Effective security investigations require the aggregation,
standardization, and centralization of logs and events so they
are readily accessible to investigation teams. Centralized
logs and event data enhance the ability of security teams to
conduct effective investigations, improve threat detection,
and accelerate incident response times.

Use cloud native tools or Security Information and Event Management (SIEM) solutions
to aggregate, standardize, and centralize logs and event data, while respecting regional
boundaries and data sovereignty requirements. These tools are designed to collect and
analyze logs and security events from various sources to provide a centralized view of an
organization's security posture. Centralizing, normalizing, deduping, and removing
unnecessary data allows security teams to use automation and scripted investigation tools
which leads to a faster and more efficient response process.

Given the sensitivity of this data, verify that the data is accessible only to
authorized security personnel and that strong access controls are in place to maintain data
security and confidentiality. Only grant least-privilege permission to the data so that it
is only accessible to authorized users with the minimum level of access required to perform
investigations. For instance, access to overwrite this data should be restricted.

**Related information:**

- [AWS Well-Architected Performance Pillar: PERF07-BP02 Analyze
  metrics when events or incidents occur](../performance-efficiency-pillar/perf_monitor_instances_post_launch_review_metrics.md "../performance-efficiency-pillar/perf_monitor_instances_post_launch_review_metrics.md")
- [Collect,
  analyze, and display Amazon CloudWatch Logs in a single
  dashboard with the Centralized Logging on AWS solution](../../../solutions/latest/centralized-logging-on-aws/welcome.md "../../../solutions/latest/centralized-logging-on-aws/welcome.md")
- [Cross-account
  cross-Region CloudWatch console](../../../AmazonCloudWatch/latest/monitoring/Cross-Account-Cross-Region.md "../../../AmazonCloudWatch/latest/monitoring/Cross-Account-Cross-Region.md")
- [AWS Well-Architected Framework - Security Pillar -
  Detection](../framework/sec-detection.md "../framework/sec-detection.md")
- [Amazon
  Security Lake](https://aws.amazon.com/security-lake/ "https://aws.amazon.com/security-lake/")
- [Centralized
  Logging on AWS](https://aws.amazon.com/solutions/implementations/centralized-logging/ "https://aws.amazon.com/solutions/implementations/centralized-logging/")
- [Amazon OpenSearch Service](https://aws.amazon.com/opensearch-service/ "https://aws.amazon.com/opensearch-service/")
- [Centralized
  Logging with OpenSearch](https://aws.amazon.com/solutions/implementations/centralized-logging-with-opensearch/ "https://aws.amazon.com/solutions/implementations/centralized-logging-with-opensearch/")
- [AWS Marketplace: SIEM](https://aws.amazon.com/marketplace/solutions/security/siem "https://aws.amazon.com/marketplace/solutions/security/siem")
