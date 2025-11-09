# MIDAOPS02-BP01 Use enhanced monitoring and alerting in the cloud and at the edge

Comprehensive observability is crucial for manufacturing teams to proactively monitor the
health and performance of the data infrastructure.

**Desired outcome:** Achieve real-time visibility into the
entire industrial data infrastructure, enabling proactive issue detection, rapid
troubleshooting, and maintenance of optimal system performance across both cloud and edge
environments.

**Benefits of establishing this best practice:** By
implementing this robust observability framework, a manufacturing organization can gain
visibility and insight needed to proactively manage the reliability, performance, and security
of their data-driven operations. The observability tools and practices enable the team to
quickly detect, investigate, and resolve issues before they impact production.

- Enables proactive identification of potential issues before they impact operations
- Reduces mean time to detection (MTTD) and resolution (MTTR)
- Provides comprehensive visibility across the entire data infrastructure
- Facilitates data-driven decision making for system optimization
- Enhances overall system reliability and performance

**Level of risk exposed if this best practice is not
established:** High

## Implementation guidance

Establish a comprehensive monitoring and alerting framework that covers both cloud and
edge components of your industrial data infrastructure.

### Implementation steps

1. Use AWS AWS IoT Greengrass to collect and stream operational telemetry data, such as
   device health metrics and diagnostic logs, back to the cloud. This allows the
   manufacturing team to maintain visibility into the state of edge components, even in
   disconnected scenarios.
2. Use Amazon CloudWatch to collect and analyze metrics, logs, and events from
   across the hybrid edge-cloud architecture. This includes metrics like data ingestion
   rates, database performance, and resource utilization. CloudWatch dashboards and
   alarms provide visibility into the overall system health, allowing the team to quickly
   identify and address issues. Set baseline performance metrics and configure automated
   alerting thresholds.
3. To enable end-to-end tracing and diagnostics, use AWS X-Ray. X-Ray provides
   detailed insights into the performance and dependencies of distributed components,
   helping the team rapidly pinpoint the root cause of problems.
4. Consider recording all API calls and configuration changes using AWS CloudTrail,
   enabling comprehensive auditing and security monitoring of the data infrastructure.

## Key AWS services

- AWS CloudTrail
- Amazon CloudWatch
- AWS AWS IoT Greengrass
- AWS X-Ray

## Resources

**Related documents:**

- [Security Best Practices for Manufacturing OT](../../../whitepapers/latest/security-best-practices-for-manufacturing-ot/security-best-practices-for-manufacturing-ot.md "../../../whitepapers/latest/security-best-practices-for-manufacturing-ot/security-best-practices-for-manufacturing-ot.md")
- [Monitor edge application performance using AWS IoT Greengrass and AWS Distro for
  OpenTelemetry](https://aws.amazon.com/blogs/iot/monitor-edge-application-performance-using-aws-iot-greengrass-and-aws-distro-for-opentelemetry/ "https://aws.amazon.com/blogs/iot/monitor-edge-application-performance-using-aws-iot-greengrass-and-aws-distro-for-opentelemetry/")
