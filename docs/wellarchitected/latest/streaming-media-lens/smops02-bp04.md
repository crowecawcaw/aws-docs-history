

# SMOPS02-BP04 Instrument your streaming application code and infrastructure for observability
<a name="smops02-bp04"></a>

Instrument your streaming application code and infrastructure to emit detailed, structured logs and metrics to achieve full visibility into streaming video workloads. This structured approach enables teams to detect, diagnose, and resolve issues quickly, optimizing performance and reliability of streaming video delivery.

**Desired outcome:**
+ Applications and infrastructure that provide rich, contextual telemetry data enabling rapid troubleshooting and ongoing optimization of the streaming experience.

**Benefits of establishing this best practice:**
+ Reduced mean time to detection (MTTD) and resolution (MTTR)
+ Improved understanding of application behavior
+ Enhanced ability to optimize streaming performance
+ Better correlation between user experience and system metrics

**Level of risk exposed if this best practice is not established:** Medium

## Implementation guidance
<a name="implementation-guidance"></a>

Full visibility into streaming video workloads requires instrumentation across four key areas that together provide full-path observability.

Application instrumentation involves adding structured logging with consistent formats, including contextual information in logs (session IDs, content IDs), implementing distributed tracing across services, and emitting custom metrics for business-relevant events. These practices enable rapid correlation of issues across the application layer.

Infrastructure instrumentation requires enabling detailed metrics for all AWS services, configuring VPC flow logs for network visibility, enabling access logging for load balancers and content delivery networks (CDNs), and implementing custom metrics for non-AWS components. This layer provides the foundation for understanding resource utilization and performance characteristics.

Player instrumentation captures the viewer's perspective by collecting quality of experience (QoE) metrics, tracking user interactions and playback events, capturing device and network information, and reporting errors with contextual information. These client-side signals are essential for understanding the actual viewer experience.

Cross-layer tracing ties all layers together by implementing correlation IDs across the streaming workflow, using distributed tracing to track request flows, correlating backend events with player experiences, and tracking third-party service dependencies. This cross-cutting capability enables rapid root cause analysis across the entire streaming stack.

### Implementation steps
<a name="implementation-steps"></a>

1. **Implement standardized logging formats and levels:** Define and implement consistent logging formats and severity levels across all application components to enable effective log aggregation and analysis.

1. **Add distributed tracing to key services:** Instrument key services with distributed tracing to enable request flow tracking across service boundaries.

1. **Define and implement custom metrics:** Define and implement custom metrics that capture business-relevant events and streaming-specific performance indicators.

1. **Configure infrastructure logging:** Configure infrastructure logging and metrics collection for all AWS services and non-AWS components in the streaming workflow.

1. **Implement player-side telemetry collection:** Implement player-side telemetry collection to capture quality of experience metrics and playback events from viewer devices.

1. **Create correlation mechanisms between components:** Create correlation mechanisms between components using shared identifiers to enable request tracing.

1. **Validate holistic observability by tracing:** Validate observability by tracing sample requests through the entire streaming workflow and confirming visibility at each layer.

## Resources
<a name="resources"></a>

**Related documents**
+ [AWS Distro for OpenTelemetry](https://aws.amazon.com/otel/)
+ [Distributed Tracing](https://aws.amazon.com/what-is/distributed-tracing/)

**Related services**
+ [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/)
+ [AWS X-Ray](https://aws.amazon.com/xray/)
+ [AWS Distro for OpenTelemetry](https://aws.amazon.com/otel/)
+ [Amazon Managed Service for Prometheus](https://aws.amazon.com/prometheus/)
+ [Amazon Managed Grafana](https://aws.amazon.com/grafana/)