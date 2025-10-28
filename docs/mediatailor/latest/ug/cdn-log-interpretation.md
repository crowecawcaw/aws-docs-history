# CDN log interpretation and analysis techniques

for MediaTailor

AWS Elemental MediaTailor content delivery network (CDN) integration generates detailed logs that help
you understand request patterns and identify issues. When analyzing content delivery
network logs, focus on these key indicators:

**Note:** The following examples use Amazon CloudFront
terminology. Other CDN providers may use different terms for similar concepts.

HTTP status codes

- `200` - Successful request
- `404` - Resource not found (check routing rules and
  MediaTailor configuration)
- `403` - Access denied (check CDN security settings and
  origin permissions)
- `502/503/504` - Origin server errors (check MediaTailor
  service health and origin connectivity)

Cache behavior indicators

- `Hit` - Content served from CDN cache
- `Miss` - Content fetched from origin
- `RefreshHit` - Cached content validated with
  origin
- `Error` - Request resulted in an error

Request patterns to monitor

- Manifest requests should typically result in `Miss` or
  `RefreshHit` due to low TTL settings
- Content segments should show `Hit` for popular
  content
- Ad segments may show `Miss` due to
  personalization

**Service health monitoring**

When analyzing CDN logs and troubleshooting issues, check MediaTailor service health to
determine if problems are service-related:

AWS Service Health Dashboard

Check current MediaTailor service status and any ongoing service events

Access: [AWS
Service Health Dashboard](https://aws.amazon.com/https://status.aws.amazon.com/ "https://aws.amazon.com/https://status.aws.amazon.com/")

Use this when: You see widespread 5xx errors or service timeouts in CDN
logs

AWS Personal Health Dashboard

View account-specific service health notifications and maintenance
events

Access: [AWS Personal Health
Dashboard](https://console.aws.amazon.com/phd/home "https://console.aws.amazon.com/phd/home")

Use this when: You need account-specific service health information or
maintenance notifications

Amazon CloudWatch metrics monitoring

Monitor MediaTailor service health indicators through CloudWatch metrics:

- `GetManifest.Errors` - Track manifest generation
  errors
- `GetManifest.Latency` - Monitor response time
  performance
- `AdDecisionServer.Errors` - Monitor ad server
  connectivity issues
- `Origin.Errors` - Track origin server connectivity
  problems

Access: [CloudWatch
Console](https://console.aws.amazon.com/cloudwatch/home "https://console.aws.amazon.com/cloudwatch/home")

Use this when: You need detailed service performance metrics and
historical trends

**Service health troubleshooting workflow:**

1. Check AWS Service Health Dashboard for current service status
2. Review AWS Personal Health Dashboard for account-specific
   notifications
3. Monitor CloudWatch metrics for service performance indicators
4. Correlate service health status with CDN log patterns and error rates
5. If service health is normal, focus on CDN configuration and origin server
   issues
   **CDN log analysis resources**

- [CloudFront access logs](../../../AmazonCloudFront/latest/DeveloperGuide/AccessLogs.md "../../../AmazonCloudFront/latest/DeveloperGuide/AccessLogs.md") - Complete guide to CDN log format and
  fields
- [CloudFront real-time logs](../../../AmazonCloudFront/latest/DeveloperGuide/real-time-logs.md "../../../AmazonCloudFront/latest/DeveloperGuide/real-time-logs.md") - Real-time log streaming and analysis
- [Analyzing log data with CloudWatch Logs Insights](../../../AmazonCloudWatch/latest/logs/AnalyzingLogData.md "../../../AmazonCloudWatch/latest/logs/AnalyzingLogData.md") - Advanced log querying and
  analysis
- [Monitor workload resources](../../../wellarchitected/latest/reliability-pillar/monitor-workload-resources.md "../../../wellarchitected/latest/reliability-pillar/monitor-workload-resources.md") - Well-Architected monitoring
  patterns
