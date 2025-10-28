# View Network Flow Monitor metrics in CloudWatch

Network Flow Monitor publishes the following network flow performance metrics to your account: round-trip time, TCP retransmissions,
TCP retransmission timeouts, data transferred, and network health indicator. You can view these
metrics in CloudWatch Metrics in the Amazon CloudWatch console.

To find all metrics for your monitor, in the CloudWatch Metrics dashboard, see the custom namespace
`AWS/NetworkFlowMonitor`. Metrics are aggregated for each monitor that is deployed and active.

Network Flow Monitor provides the following metrics. Be aware that RoundTripTime data can be sparse, as this metric
is not always calculated.

| Metric          | Description                                                                                                                                                                                                                                                                                                                                                                                                       |
| --------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| DataTransferred | The number of bytes transferred for all flows for a monitor.                                                                                                                                                                                                                                                                                                                                                      |
| Retransmissions | Total number of retransmissions for a monitor. Retransmissions occur when the sender needs to resend packets that have been either damaged or lost.                                                                                                                                                                                                                                                               |
| Timeouts        | Total retransmission timeouts for a monitor. This occurs when the sender is missing too many acknowledgments, and therefore decides to take a time out and stop sending altogether.                                                                                                                                                                                                                               |
| RoundTripTime   | Average round-trip time for network flows for a monitor. This metric, measured in microseconds, is a measure of performance. It records the time it takes for traffic to be transmitted from a local resource to a remote IP address, and for the associated response to be received. The time is an average over the aggregation period. Data can be sparse, as this metric is not always calculated.            |
| HealthIndicator | Network health indicator (NHI) for a monitor overall. Network health indicator (NHI) is a value that surfaces an AWS network impairment. The NHI value is 1 (degraded) if there was an AWS network issue during a specified time frame. It's set to 0 (healthy) if no AWS network issues were detected. Observing the NHI can help you to prioritize troubleshooting for either your workload or the AWS network. |
