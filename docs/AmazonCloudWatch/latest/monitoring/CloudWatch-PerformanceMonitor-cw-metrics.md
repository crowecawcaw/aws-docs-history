

# View Performance Monitor metrics in CloudWatch

Performance Monitor publishes one set of metrics for each network path in a monitor. A network path is the route between a local Availability Zone and a remote location, which is another Availability Zone or an AWS service. The `LocalLocation` and `RemoteLocation` dimensions identify the path. For more information, see [Components and features of Performance Monitor](CloudWatch-PerformanceMonitor-components.md). Performance Monitor doesn't publish subnet-level metrics. You can view these metrics in the `AWS/NetworkFlowMonitor` namespace in the CloudWatch console.

Each metric has the following dimensions: `MonitorId`, `LocalLocation`, and `RemoteLocation`.

The following table lists the metrics that Performance Monitor publishes.


| Metric | Description | 
| --- | --- | 
| `ImpactScore` | The impact score for the network path. The value is fixed for each impact level: 0 (None), 25 (Low), 65 (Medium), or 95 (High). For more information about how the impact score is calculated, see [How Performance Monitor works](CloudWatch-PerformanceMonitor-how-it-works.md). | 
| `RoundTripTimeMs` | The average round-trip latency between the local and remote locations, in milliseconds. | 
| `RoundTripTimeP95Ms` | The 95th percentile round-trip latency between the local and remote locations, in milliseconds. This metric is published only when a p95 value is available. | 
| `BytesIn` | The inbound traffic (bytes received) for the network path. | 
| `BytesOut` | The outbound traffic (bytes sent) for the network path. | 

The impact score for a network path is traffic weighted, so subnet flows with more traffic contribute more to the path's score. Performance Monitor doesn't publish a monitor-level metric. To alarm on any path in a monitor, see [Create alarms with Performance Monitor](CloudWatch-PerformanceMonitor-create-alarm.md).

You can use these metrics to create dashboards, set alarms, and perform analysis.