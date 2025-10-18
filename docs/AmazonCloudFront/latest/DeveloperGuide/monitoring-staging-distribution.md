# Monitor a staging
 distribution

To monitor the performance of a staging distribution, you can use the same [metrics, logs, and reports](reports-and-monitoring.md "reports-and-monitoring.md") that CloudFront provides
 for all distributions. For example:


* You can view the [default CloudFront
 distribution metrics](viewing-cloudfront-metrics.md#monitoring-console.distributions "viewing-cloudfront-metrics.md#monitoring-console.distributions") (such as total requests and error rate) in the CloudFront
 console, and you can [turn on additional metrics](viewing-cloudfront-metrics.md#monitoring-console.distributions-additional "viewing-cloudfront-metrics.md#monitoring-console.distributions-additional") (such as cache hit rate and error rate by
 status code) for an additional cost. You can also create alarms based on these
 metrics.
* You can view [standard logs](AccessLogs.md "AccessLogs.md") and [real-time logs](real-time-logs.md "real-time-logs.md") to get detailed information about
 the requests that are received by the staging distribution. Standard logs
 contain the following two fields that help you identify the primary distribution
 that the request was originally sent to before CloudFront routed it to the staging
 distribution: `primary-distribution-id` and
 `primary-distribution-dns-name`.
* You can view and download [reports](reports.md "reports.md") in the CloudFront
 console, for example the cache statistics report.
