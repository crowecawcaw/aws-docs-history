# Standard logging (access logs)

You can configure CloudFront to create log files that contain detailed information about every
user (viewer) request that CloudFront receives. These are called _standard
logs_, also known as _access logs_.

Each log contains information such as the time the request was received, the processing
time, request paths, and server responses. You can use these access logs to analyze response
times and to troubleshoot issues.

The following diagram shows how CloudFront logs information about requests for your objects. In
this example, the distributions are configured to send access logs to an Amazon S3 bucket.

![Basic flow for access logs](images/Logging.png)

1. In this example, you have two websites, A and B, and two corresponding CloudFront
   distributions. Users request your objects using URLs that are associated with
   your distributions.
2. CloudFront routes each request to the appropriate edge location.
3. CloudFront writes data about each request to a log file specific to that
   distribution. In this example, information about requests related to
   Distribution A goes into a log file for Distribution A. Information about
   requests related to Distribution B goes into a log file for Distribution
   B.
4. CloudFront periodically saves the log file for a distribution in the Amazon S3 bucket
   that you specified when you enabled logging. CloudFront then starts saving information
   about subsequent requests in a new log file for the distribution.

If viewers don't access your content during a given hour, you don't receive
any log files for that hour.

###### Note

We recommend that you use the logs to understand the nature of the requests for
your content, not as a complete accounting of all requests. CloudFront delivers access
logs on a best-effort basis. The log entry for a particular request might be
delivered long after the request was actually processed and, in rare cases, a log
entry might not be delivered at all. When a log entry is omitted from access logs,
the number of entries in the access logs won't match the usage that appears in the
AWS billing and usage reports.

CloudFront supports two versions of standard logging. Standard logging (legacy) supports sending
your access logs to Amazon S3 _only_. Standard logging (v2) supports
additional delivery destinations. You can configure both or either logging option for your
distribution. For more information, see the following topics:

###### Topics

- [Configure standard logging (v2)](standard-logging.md "standard-logging.md")
- [Configure standard logging (legacy)](standard-logging-legacy-s3.md "standard-logging-legacy-s3.md")
- [Standard logging reference](standard-logs-reference.md "standard-logs-reference.md")

###### Tip

CloudFront also offers real-time logs, which give you information about requests made to a
distribution in real time (logs are delivered within seconds of receiving the requests).
You can use real-time logs to monitor, analyze, and take action based on content
delivery performance. For more information, see [Use real-time logs](real-time-logs.md "real-time-logs.md").
