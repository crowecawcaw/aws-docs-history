# CDN integration log analysis and error code

reference for MediaTailor

AWS Elemental MediaTailor content delivery network (CDN) integration logs provide valuable insights into
performance and errors. This guide covers both CDN logs (from your content delivery network)
and MediaTailor logs and error codes that are relevant to CDN integration troubleshooting. Use
this reference when you need to understand what your content delivery network logs and error
codes are telling you about your MediaTailor integration. This guide helps you interpret log
entries and error messages to identify the root cause of issues.

**Related topics:**

- For step-by-step troubleshooting procedures, see [Troubleshoot CDN integration](cdn-troubleshooting.md "cdn-troubleshooting.md")
- For proactive monitoring and prevention strategies, see [Monitor MediaTailor CDN operations and performance](cdn-monitoring.md "cdn-monitoring.md")
- For escalation and getting additional help, see [Get CDN integration support](cdn-get-help.md "cdn-get-help.md")
- For comprehensive MediaTailor logging configuration and resources, see [MediaTailor logging configuration
  resources](#mediatailor-logging-resources "#mediatailor-logging-resources")
- For CloudFront log format reference, see [CloudFront access log format](../../../AmazonCloudFront/latest/DeveloperGuide/AccessLogs.md#LogFileFormat "../../../AmazonCloudFront/latest/DeveloperGuide/AccessLogs.md#LogFileFormat")
- For HTTP status code reference, see [HTTP response
  status codes](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status "https://developer.mozilla.org/en-US/docs/Web/HTTP/Status")

###### Topics

- [Error codes
  reference](emt-error-codes-reference.md "emt-error-codes-reference.md")
- [Log analysis tools](log-analysis-techniques.md "log-analysis-techniques.md")
- [MediaTailor logging configuration
  resources](#mediatailor-logging-resources "#mediatailor-logging-resources")

## MediaTailor logging configuration

resources

In addition to CDN logs, MediaTailor provides comprehensive logging capabilities for
monitoring ad insertion, manifest generation, and service interactions. Use these
resources to configure and analyze MediaTailor logs:

MediaTailor manifest and service logs

Configure and analyze logs for manifest generation, origin interactions,
and service events:

- [AWS Elemental MediaTailor manifest logs description and event types](log-types.md "log-types.md") - Complete
  reference for MediaTailor manifest logs and event types
- [Viewing AWS Elemental MediaTailor logs](monitoring-through-logs.md "monitoring-through-logs.md") - Guide to viewing and
  interpreting MediaTailor logs

Vended logs configuration

Configure flexible log delivery to multiple destinations with cost
optimization:

- [Using vended logs to send AWS Elemental MediaTailor logs](vended-logs.md "vended-logs.md") -
  Configure log delivery to Amazon S3, Firehose, or CloudWatch Logs
- [Migrating your AWS Elemental MediaTailor logging strategy](vended-logs-migrate.md "vended-logs-migrate.md") - Migration guide for
  existing logging configurations

CloudWatch Logs integration

Integrate MediaTailor logs with CloudWatch for monitoring and analysis:

- [Viewing AWS Elemental MediaTailor logs](monitoring-through-logs.md "monitoring-through-logs.md") -
  CloudWatch Logs configuration and analysis
- [CloudWatchInsights](../../../AmazonCloudWatch/latest/logs/AnalyzingLogData.md "../../../AmazonCloudWatch/latest/logs/AnalyzingLogData.md") - Advanced log querying and
  analysis

Ad-specific logging

Monitor ad insertion performance and troubleshoot ad-related
issues:

- ADS interaction logs - Monitor ad decision server communication
  and errors

**Key differences between CDN and MediaTailor logs:**

- **CDN logs**: Show request/response patterns,
  cache behavior, and network-level errors from your content delivery
  network
- **MediaTailor logs**: Show ad insertion details,
  manifest generation events, origin interactions, and service-specific
  errors
- **Combined analysis**: Use both log types
  together for complete visibility into your streaming workflow

For comprehensive monitoring that combines both CDN and MediaTailor logging, see [Monitor MediaTailor CDN operations and performance](cdn-monitoring.md "cdn-monitoring.md").
