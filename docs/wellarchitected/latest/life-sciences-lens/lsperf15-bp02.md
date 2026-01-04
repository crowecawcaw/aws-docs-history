# LSPERF15-BP02 Deploy synthetic transaction monitoring and real

user monitoring with automated performance
optimization

Implement synthetic monitoring methods that continuously simulate
critical clinical workflows such as record retrieval, patient
monitoring data transmission, and medication order processing to
measure end-to-end latency and automatically trigger optimization
actions when thresholds are exceeded. Use real user monitoring (RUM)
techniques to capture actual network performance experienced by
clinicians and implement adaptive optimization that adjusts network
configurations based on real-time performance data, such as
switching to alternate network paths or increasing bandwidth
allocation for degraded connections.

**Desired outcome:** You have an
integrated monitoring system combining synthetic testing and real
user monitoring that automatically detects and responds to
performance issues in clinical workflows. This enables proactive
optimization of network performance and provides reliable operation
of critical healthcare applications.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

Establish comprehensive synthetic monitoring for critical clinical
workflows, including automated tests for record retrieval and
patient data transmission. Configure monitoring scenarios that
simulate real clinical activities with defined performance
thresholds. Implement automated response mechanisms that trigger
optimization actions when performance degrades below acceptable
levels.

Deploy RUM solutions to capture actual performance metrics
experienced by clinical users across different locations and
devices. Set up data collection for key performance indicators
including page load times, API response times, and network
latency. Create performance baselines that reflect real-world
usage patterns in clinical environments.

Design automated optimization systems that respond to both
synthetic and RUM data. Implement intelligent routing algorithms
that can automatically adjust network paths based on performance
metrics. Establish bandwidth allocation rules that dynamically
adapt to changing network conditions and clinical priorities.

Create comprehensive alerting mechanisms that identify performance
issues before they impact clinical operations. Implement automated
remediation procedures for common performance issues. Establish
escalation paths for situations requiring manual intervention.

### Implementation steps

1. Establish comprehensive synthetic monitoring by deploying
   Amazon CloudWatch Synthetics with canaries simulating
   clinical workflows, AWS X-Ray traces for performance
   tracking, and custom metrics to measure healthcare-specific
   application performance.
2. Implement real user monitoring (RUM) with CloudWatch RUM for
   real-time clinical application data collection, performance
   monitoring agents on user devices, and client-side
   monitoring to track user experience metrics.
3. Deploy performance optimization tools including AWS Global Accelerator for automatic path optimization, Application
   Auto Scaling to adjust resources based on demand, and AWS Transit Gateway for intelligent network traffic routing.
4. Create integrated monitoring and alerting with CloudWatch
   dashboards visualizing synthetic and RUM metrics, Amazon EventBridge rules automating responses to performance
   issues, and Amazon SNS notifications providing rapid
   response to critical alerts.
5. Document performance baselines specific to clinical
   workflows and establish escalation procedures for different
   severity levels of performance degradation.
6. Implement regular performance reviews to identify
   optimization opportunities and validate monitoring coverage
   across critical healthcare applications.
7. Configure automated remediation for common performance
   issues to minimize impact on clinical operations.
