# Monitor your Application Load Balancers

You can use the following features to monitor your load balancers, analyze traffic
patterns, and troubleshoot issues with your load balancers and targets.

**CloudWatch metrics**

You can use Amazon CloudWatch to retrieve statistics about data points for your load
balancers and targets as an ordered set of time-series data, known as
_metrics_. You can use these metrics to verify that your
system is performing as expected. For more information, see [CloudWatch metrics for your Application Load Balancer](load-balancer-cloudwatch-metrics.md "load-balancer-cloudwatch-metrics.md").

**Access logs**

You can use access logs to capture detailed information about the requests
made to your load balancer and store them as log files in Amazon S3. You can use
these access logs to analyze traffic patterns and to troubleshoot issues with
your targets. For more information, see [Access logs for your Application Load Balancer](load-balancer-access-logs.md "load-balancer-access-logs.md").

**Connection logs**

You can use connection logs to capture attributes about the requests sent to
your load balancer, and store them as log files in Amazon S3. You can use these
connection logs to determine the client IP address and port, client certificate
information, connection results, and TLS ciphers being used. These connection
logs can then be used to review request patterns, and other trends. For more
information, see [Connection logs for your Application Load Balancer](load-balancer-connection-logs.md "load-balancer-connection-logs.md").

**Health check logs**

You can use health check logs to capture detailed information about the health checks
made to your registered targets for your load balancer and store them as log files in Amazon S3.
You can use these health check logs to troubleshoot issues with your targets.
For more information, see [Health check logs](load-balancer-health-check-logs.md "load-balancer-health-check-logs.md").

**Request tracing**

You can use request tracing to track HTTP requests. The load balancer adds a
header with a trace identifier to each request it receives. For more
information, see [Request tracing for your Application Load Balancer](load-balancer-request-tracing.md "load-balancer-request-tracing.md").

**CloudTrail logs**

You can use AWS CloudTrail to capture detailed information about the calls made to
the Elastic Load Balancing API and store them as log files in Amazon S3. You can use these CloudTrail logs
to determine which calls were made, the source IP address where the call came
from, who made the call, when the call was made, and so on. For more information,
see [Log API calls for Elastic Load Balancing using CloudTrail](../userguide/cloudtrail-logs.md "../userguide/cloudtrail-logs.md").
