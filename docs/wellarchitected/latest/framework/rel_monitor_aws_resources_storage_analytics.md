# REL06-BP05 Analyze logs

Collect log files and metrics histories and analyze these for
broader trends and workload insights.

Amazon CloudWatch Logs Insights supports
a [simple
yet powerful query language](../../../AmazonCloudWatch/latest/logs/CWL_QuerySyntax.md "../../../AmazonCloudWatch/latest/logs/CWL_QuerySyntax.md") that you can use to analyze log
data. Amazon CloudWatch Logs also supports subscriptions that allow
data to flow seamlessly to Amazon S3 where you can use or Amazon Athena to query the data. It also supports queries on a large array
of formats.
See [Supported
SerDes and Data Formats](../../../athena/latest/ug/supported-format.md "../../../athena/latest/ug/supported-format.md") in the Amazon Athena User Guide for
more information. For analysis of huge log file sets, you can run an
Amazon EMR cluster to run petabyte-scale analyses.

There are a number of tools provided by AWS Partners and third
parties that allow for aggregation, processing, storage, and
analytics. These tools include New Relic, Splunk, Loggly, Logstash,
CloudHealth, and Nagios. However, outside generation of system and
application logs is unique to each cloud provider, and often unique
to each service.

An often-overlooked part of the monitoring process is data
management. You need to determine the retention requirements for
monitoring data, and then apply lifecycle policies accordingly.
Amazon S3 supports lifecycle management at the S3 bucket level. This
lifecycle management can be applied differently to different paths
in the bucket. Toward the end of the lifecycle, you can transition
data to Amazon Glacier for long-term storage, and then expiration
after the end of the retention period is reached. The S3
Intelligent-Tiering storage class is designed to optimize costs by
automatically moving data to the most cost-effective access tier,
without performance impact or operational overhead.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

- CloudWatch Logs Insights allows you to interactively search and
  analyze your log data in Amazon CloudWatch Logs.
  - [Analyzing Log Data
    with CloudWatch Logs Insights](../../../AmazonECS/latest/developerguide/using_cloudwatch_logs.md "../../../AmazonECS/latest/developerguide/using_cloudwatch_logs.md")
  - [Amazon CloudWatch Logs Insights Sample Queries](../../../AmazonCloudWatch/latest/logs/AnalyzingLogData.md "../../../AmazonCloudWatch/latest/logs/AnalyzingLogData.md")

- Use Amazon CloudWatch Logs to send logs to Amazon S3 where you can
  use or Amazon Athena to query the data.
  - [How
    do I analyze my Amazon S3 server access logs using Athena?](https://aws.amazon.com/premiumsupport/knowledge-center/analyze-logs-athena/ "https://aws.amazon.com/premiumsupport/knowledge-center/analyze-logs-athena/")
    - Create an S3 lifecycle policy for your server access logs bucket. Configure
      the lifecycle policy to periodically remove log files. Doing so reduces the amount
      of data that Athena analyzes for each query.
      - [How Do I Create a
        Lifecycle Policy for an S3 Bucket?](../../../AmazonS3/latest/user-guide/create-lifecycle.md "../../../AmazonS3/latest/user-guide/create-lifecycle.md")

## Resources

**Related documents:**

- [Amazon CloudWatch Logs Insights Sample Queries](../../../AmazonCloudWatch/latest/logs/CWL_QuerySyntax-examples.md "../../../AmazonCloudWatch/latest/logs/CWL_QuerySyntax-examples.md")
- [Analyzing
  Log Data with CloudWatch Logs Insights](../../../AmazonECS/latest/developerguide/using_cloudwatch_logs.md "../../../AmazonECS/latest/developerguide/using_cloudwatch_logs.md")
- [Debugging
  with Amazon CloudWatch Synthetics and AWS X-Ray](https://aws.amazon.com/blogs/devops/debugging-with-amazon-cloudwatch-synthetics-and-aws-x-ray/ "https://aws.amazon.com/blogs/devops/debugging-with-amazon-cloudwatch-synthetics-and-aws-x-ray/")
- [How
  Do I Create a Lifecycle Policy for an S3 Bucket?](../../../AmazonS3/latest/user-guide/create-lifecycle.md "../../../AmazonS3/latest/user-guide/create-lifecycle.md")
- [How
  do I analyze my Amazon S3 server access logs using
  Athena?](https://aws.amazon.com/premiumsupport/knowledge-center/analyze-logs-athena/ "https://aws.amazon.com/premiumsupport/knowledge-center/analyze-logs-athena/")
- [One
  Observability Workshop](https://observability.workshop.aws/ "https://observability.workshop.aws/")
- [The
  Amazon Builders' Library: Instrumenting distributed systems
  for operational visibility](https://aws.amazon.com/builders-library/instrumenting-distributed-systems-for-operational-visibility/ "https://aws.amazon.com/builders-library/instrumenting-distributed-systems-for-operational-visibility/")
