

# SMOPS02-BP02 Implement comprehensive monitoring and collect granular metrics across all layers of your streaming stack
<a name="smops02-bp02"></a>

Streaming video workloads require a complete approach to monitoring that spans all layers of the streaming stack i.e., infrastructure, encoding, packaging, delivery, and playback while collecting granular, scenario-specific metrics with near real-time latency. By combining full stack-wide monitoring with advanced analytics and anomaly detection, you can proactively identify and resolve issues before they impact viewer experience, even during high-demand periods.

**Desired outcome:**
+ Complete visibility into the health and performance of all streaming workflow components with granular, scenario-specific metrics enabling proactive issue detection, rapid resolution, and data-driven optimization.

**Benefits of establishing this best practice:**
+ Early detection of potential issues before they impact viewers
+ Reduced mean time to resolution (MTTR) for streaming issues
+ Proactive identification of potential streaming issues during high-demand events
+ Data-driven optimization of streaming infrastructure
+ Improved understanding of system performance and bottlenecks

**Level of risk exposed if this best practice is not established:** High

## Implementation guidance
<a name="implementation-guidance"></a>

Monitoring across all layers of the streaming stack, with granular metrics appropriate to each streaming scenario, provides the visibility needed to maintain quality and reliability.

At the infrastructure layer, monitoring compute resources (Amazon EC2, Lambda, and containers), storage performance and capacity, and network throughput and latency establishes the foundation for understanding system health. The encoding and processing layer requires tracking encoding job success rates and duration, encoding quality metrics, and processing queue depths and latency. For the delivery layer, content delivery network (CDN) performance and cache efficiency, origin request rates and response times, and bandwidth utilization and throughput are essential indicators. At the playback layer, quality of experience (QoE) metrics, playback errors by device type, and startup time, rebuffering, and bit rate adaptation metrics directly reflect viewer experience.

For high-profile events, additional monitoring should be deployed for critical components ahead of time, with increased metric resolution during events (1-second or sub-second for critical metrics), specialized dashboards for event monitoring, and more sensitive alerting thresholds during event windows.

Scenario-specific metrics further refine observability. Video on demand (VOD) streaming benefits from tracking content processing success rates and duration, origin request patterns and cache efficiency, playback initiation success rate by device type, and video quality metrics (resolution, bit rate, and framerate). Live streaming requires monitoring contribution feed health metrics, encoder performance (CPU, memory, and dropped frames), output rendition availability, and latency measurements. Ad-supported content introduces ad decision server response time, ad insertion latency, ad playback success rate, and ad tracking event delivery. Low-latency streaming focuses on segment creation and delivery timing, buffer levels across the delivery chain, player buffer management metrics, and network path performance metrics. Interactive streaming requires tracking real-time communication latency, synchronization metrics, interactive feature response times, and participant connection quality.

For each layer and scenario, establishing baseline performance metrics, setting appropriate thresholds, configuring alerts for anomalies, and using anomaly detection to identify deviations from expected patterns enables proactive issue resolution. Automated remediation should be implemented where possible.

### Implementation steps
<a name="implementation-steps"></a>

1. **Identify critical components:** Identify critical components in each layer of your streaming stack that require monitoring.

1. **Define key metrics:** Define key metrics for each component and streaming scenario based on their impact on viewer experience.

1. **Implement monitoring tools and agents:** Deploy monitoring tools and agents across all layers of the streaming stack.

1. **Configure metric resolution:** Configure appropriate metric resolution (1-second for critical metrics) to enable timely detection of issues.

1. **Set up anomaly detection based:** Set up anomaly detection based on historical patterns to identify deviations from expected behavior.

1. **Configure role-based dashboards:** Configure dashboards for different operational roles to surface the most relevant metrics for each team.

1. **Create event-specific monitoring dashboards:** Create event-specific monitoring dashboards with heightened alerting thresholds for large-scale streaming events.

1. **Set up alerting based:** Set up alerting based on thresholds and anomaly detection to notify the appropriate teams when issues arise.

1. **Establish escalation procedures:** Establish escalation procedures for different alert types so teams respond within defined time targets.

1. **Implement automated remediation:** Implement automated remediation for common issues to reduce manual intervention and response time.

1. **Review and refine monitoring approach:** Regularly review and refine the monitoring approach based on operational lessons and evolving requirements.

## Resources
<a name="resources"></a>

**Related documents**
+ [Observability using native Amazon CloudWatch and AWS X-Ray](https://aws.amazon.com/blogs/mt/observability-using-native-amazon-cloudwatch-and-aws-x-ray-for-serverless-modern-applications/)
+ [AWS Observability Best Practices](https://aws-observability.github.io/observability-best-practices/)
+ [Media Services Application Mapper](https://github.com/awslabs/aws-media-services-application-mapper)
+ [Monitoring AWS Media Services with workflow monitor](https://docs.aws.amazon.com/mediaconnect/latest/ug/monitor-with-workflow-monitor.html)
+ [Set up custom metrics in CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/publishingMetrics.html)
+ [Creating cross-service dashboards](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/create_dashboard.html)

**Related services**
+ [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/)
+ [AWS X-Ray](https://aws.amazon.com/xray/)
+ [Amazon Managed Grafana](https://aws.amazon.com/grafana/)
+ [Amazon Managed Service for Prometheus](https://aws.amazon.com/prometheus/)
+ [Amazon OpenSearch Service](https://aws.amazon.com/opensearch-service/)
+ [AWS CloudTrail](https://aws.amazon.com/cloudtrail/)