

# Creating CloudWatch dashboards for RTB Fabric
<a name="monitoring-cloudwatch-dashboards"></a>

You can create CloudWatch dashboards to visualize RTB Fabric metrics and monitor the health and performance of your RTB gateways and links in real time.

Consider creating dashboard widgets for:
+ *Request volume trends* – Display `total-request-count`, `success-request-count`, and `failure-request-count` metrics over time.
+ *Latency performance* – Show `total-latency` and `forwarding-latency` metrics with P90, P95, and P99 statistics.
+ *Error rate monitoring* – Track `request-status-count` metrics broken down by HTTP status codes.
+ *Filter and no-bid tracking* – Monitor `filter-transaction` to understand traffic filtering by modules, and `no-bid-external` / `no-bid-internal` for no-bid rates.
+ *Infrastructure health* – Monitor `target-ip-count` and `healthy-target-ip-count` to track the availability of target endpoints. If [Health checks for Managed Endpoints](health-checks-for-managed-endpoints.md) are enabled, compare `healthy-target-ip-count` against `target-ip-count` to identify instances failing health checks.

For information about creating CloudWatch dashboards, see [Creating a CloudWatch dashboard](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/create_dashboard.html) in the *Amazon CloudWatch User Guide*.