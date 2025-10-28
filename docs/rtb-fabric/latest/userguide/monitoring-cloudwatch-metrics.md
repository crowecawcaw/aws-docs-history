# RTB Fabric metrics

RTB Fabric publishes the following metrics to CloudWatch.

| Metric                  | Description                                                                                                                                               |
| ----------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `total-request-count`   | The total number of requests received by the service. Valid Dimensions: Link Valid Statistics: Sum Units: Count                                           |
| `success-request-count` | The number of successful requests processed by the service. Valid Dimensions: Link Valid Statistics: Sum Units: Count                                     |
| `failure-request-count` | The number of failed requests. Valid Dimensions: Link Valid Statistics: Sum Units: Count                                                                  |
| `request-status-count`  | The number of requests broken down by HTTP status codes. Valid Dimensions: HttpStatusCode, Link Valid Statistics: Sum Units: Count                        |
| `forwarding-latency`    | The time taken to forward requests. Valid Dimensions: Link, Statistic (P90, P95, P99) Valid Statistics: Average, Maximum, Minimum Units: Milliseconds     |
| `total-latency`         | The end-to-end request processing time. Valid Dimensions: Link, Statistic (P90, P95, P99) Valid Statistics: Average, Maximum, Minimum Units: Milliseconds |
| `target-ip-count`       | The number of target IP addresses. Valid Statistics: Sum, Average Units: Count                                                                            |
