

# RTB Fabric metrics
<a name="monitoring-cloudwatch-metrics"></a>

RTB Fabric publishes the following metrics to CloudWatch.

**Important**  
The following metrics are emitted as multiple data points per minute: `total-request-count`, `success-request-count`, `failure-request-count`, `request-status-count`, `filter-transaction`, `no-bid-external`, and `no-bid-internal`. View these metrics with the `Sum` statistic to see the actual volume for the time period. Other statistics, such as `Average`, will not reflect the true total.

**Request metrics**


| Metric | Description | 
| --- | --- | 
| `total-request-count` | The total number of requests received by the service.<br />Valid Dimensions: Link<br />Valid Statistics: Sum<br />Units: Count | 
| `success-request-count` | The number of successful requests processed by the service.<br />Valid Dimensions: Link<br />Valid Statistics: Sum<br />Units: Count | 
| `failure-request-count` | The number of failed requests.<br />Valid Dimensions: Link<br />Valid Statistics: Sum<br />Units: Count | 
| `request-status-count` | The number of requests broken down by HTTP status codes.<br />Valid Dimensions: HttpStatusCode, Link<br />Valid Statistics: Sum<br />Units: Count | 

**Latency metrics**


| Metric | Description | 
| --- | --- | 
| `forwarding-latency` | The time taken to forward requests to the responder.<br />Valid Dimensions: Link, Statistic (P90, P95, P99)<br />Valid Statistics: Average, Maximum, Minimum<br />Units: Microseconds | 
| `total-latency` | The end-to-end request processing time, including service overhead.<br />Valid Dimensions: Link, Statistic (P90, P95, P99)<br />Valid Statistics: Average, Maximum, Minimum<br />Units: Microseconds | 

**Infrastructure metrics**


| Metric | Description | 
| --- | --- | 
| `target-ip-count` | The number of target IP addresses discovered in your managed endpoints.<br />Valid Statistics: Sum, Average<br />Units: Count | 
| `healthy-target-ip-count` | The number of target IP addresses that passed [Health checks for Managed Endpoints](health-checks-for-managed-endpoints.md) and are receiving traffic. This metric is only available when health checks are enabled on Auto Scaling group managed endpoints.<br />Valid Statistics: Sum, Average<br />Units: Count | 

**Metering metrics**


| Metric | Description | 
| --- | --- | 
| `no-bid-external` | The number of no-bid responses for external bid transactions.<br />Valid Dimensions: GatewayId<br />Valid Statistics: Sum<br />Units: Count | 
| `no-bid-internal` | The number of no-bid responses for internal bid transactions.<br />Valid Dimensions: GatewayId<br />Valid Statistics: Sum<br />Units: Count | 

**Filter metrics**


| Metric | Description | 
| --- | --- | 
| `filter-transaction` | The number of transactions filtered (not forwarded to the responder) by a module.<br />Valid Dimensions: Link, ModuleId, Reason<br />Valid Statistics: Sum<br />Units: Count | 