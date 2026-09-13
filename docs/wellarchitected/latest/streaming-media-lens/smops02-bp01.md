

# SMOPS02-BP01 Establish performance metrics by defining key performance indicators (KPIs) and service-level objectives (SLOs)
<a name="smops02-bp01"></a>

Establishing a full set of operational performance metrics is critical in streaming video workloads. It helps organizations to measure, monitor, and validate the performance of streaming operations across different scenarios.

**Desired outcome:**
+ A well-defined set of metrics that provide practical insights into streaming video performance and enable data-driven operational improvements.

**Benefits of establishing this best practice:**
+ Objective measurement of streaming quality and performance
+ Early detection of potential issues
+ Ability to validate improvements over time
+ Alignment between technical metrics and business outcomes

**Level of risk exposed if this best practice is not established:** Medium

## Implementation guidance
<a name="implementation-guidance"></a>

Operational KPIs and SLOs specific to streaming video workloads provide the foundation for measuring and improving streaming performance. Different streaming scenarios require distinct metrics that reflect their unique characteristics and viewer expectations.

For video on demand (VOD) streaming, key metrics include content processing time, time to first frame, rebuffer ratio, and error rates by device type. Live streaming workloads require monitoring full-path latency, stream stability, encoder performance, and failover success rate. Ad-supported content introduces metrics such as ad insertion latency, ad fill rate, Video Ad Serving Template (VAST) response time, and ad quality parity with main content. Low-latency streaming focuses on glass-to-glass latency, consistent latency across devices, and encoder optimization metrics. Interactive streaming requires tracking real-time communication latency, synchronization between video and interactive elements, and chat message delivery time.

### Implementation steps
<a name="implementation-steps"></a>

1. **Identify critical user experience metrics:** Determine the key user experience metrics for your specific streaming scenario that most directly reflect viewer satisfaction.

1. **Define correlated technical metrics:** Define technical metrics that correlate with user experience to enable root cause analysis when viewer-facing issues arise.

1. **Establish baseline performance:** Establish baseline performance for each metric using historical data or initial measurement periods.

1. **Set SLOs aligned with business requirements:** Set SLOs that match business requirements and reflect realistic performance targets.

1. **Implement monitoring:** Implement monitoring and alerting based on these metrics to detect deviations from expected performance.

1. **Create operational dashboards:** Create dashboards for operational visibility that surface the most important metrics for each team role.

1. **Review and refine metrics regularly:** Regularly review and refine metrics based on user feedback and evolving business needs.

## Resources
<a name="resources"></a>

**Related documents**
+ [Monitoring AWS Media Services](https://docs.aws.amazon.com/mediaconnect/latest/ug/monitor-with-workflow-monitor.html)
+ [Amazon CloudWatch User Guide](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html)

**Related services**
+ [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/)
+ [AWS X-Ray](https://aws.amazon.com/xray/)
+ [Amazon Managed Grafana](https://aws.amazon.com/grafana/)
+ [Amazon Managed Service for Prometheus](https://aws.amazon.com/prometheus/)