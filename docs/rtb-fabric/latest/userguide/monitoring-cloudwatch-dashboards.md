# Creating CloudWatch dashboards for RTB Fabric

You can create CloudWatch dashboards to visualize RTB Fabric metrics and monitor the health and performance of your RTB gateways and links in real time.

Consider creating dashboard widgets for:

- _Request volume trends_ – Display `total-request-count`, `success-request-count`, and `failure-request-count` metrics over time.
- _Latency performance_ – Show `total-latency` and `forwarding-latency` metrics with P90, P95, and P99 statistics.
- _Error rate monitoring_ – Track `request-status-count` metrics broken down by HTTP status codes.
- _Infrastructure health_ – Monitor `target-ip-count` to track the availability of target endpoints.
  For information about creating CloudWatch dashboards, see [Creating a CloudWatch dashboard](../../../AmazonCloudWatch/latest/monitoring/create_dashboard.md "../../../AmazonCloudWatch/latest/monitoring/create_dashboard.md") in the _Amazon CloudWatch User Guide_.
