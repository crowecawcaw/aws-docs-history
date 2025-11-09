# RTB Fabric metrics

RTB Fabric publishes the following metrics to CloudWatch.

| Metric                  | Description                                                                                                                                                        |
| ----------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `total-request-count`   | The total number of requests received by the service.<br>Valid Dimensions: Link<br>Valid Statistics: Sum<br>Units: Count                                           |
| `success-request-count` | The number of successful requests processed by the service.<br>Valid Dimensions: Link<br>Valid Statistics: Sum<br>Units: Count                                     |
| `failure-request-count` | The number of failed requests.<br>Valid Dimensions: Link<br>Valid Statistics: Sum<br>Units: Count                                                                  |
| `request-status-count`  | The number of requests broken down by HTTP status codes.<br>Valid Dimensions: HttpStatusCode, Link<br>Valid Statistics: Sum<br>Units: Count                        |
| `forwarding-latency`    | The time taken to forward requests.<br>Valid Dimensions: Link, Statistic (P90, P95, P99)<br>Valid Statistics: Average, Maximum, Minimum<br>Units: Milliseconds     |
| `total-latency`         | The end-to-end request processing time.<br>Valid Dimensions: Link, Statistic (P90, P95, P99)<br>Valid Statistics: Average, Maximum, Minimum<br>Units: Milliseconds |
| `target-ip-count`       | The number of target IP addresses.<br>Valid Statistics: Sum, Average<br>Units: Count                                                                               |
