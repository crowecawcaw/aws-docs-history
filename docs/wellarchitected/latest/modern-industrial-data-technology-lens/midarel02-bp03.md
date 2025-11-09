# MIDAREL02-BP03 Enable automated recovery mechanisms

Design your manufacturing workloads with automated recovery processes that allow
production to continue despite OT and IT system failures. Implement edge processing
capabilities that can operate independently when disconnected from central IT systems.

**Desired outcome:** Production operations continue without
interruption even when data collection systems, network connectivity, or cloud services
experience failures. Critical manufacturing data is preserved and synchronized once systems
are restored.

**Benefits of establishing the best practice:** Minimizing
production downtime, preserving data integrity during system failures, reducing manual
intervention during recovery processes, and maintaining product quality metrics during system
disruptions.

**Level of risk exposed if this best practice is not
established:** High

## Implementation guidance

**Implement edge computing capabilities**

Assess your manufacturing system's autonomy requirements and identify critical
processes that must continue during connectivity loss. Document acceptable operational modes
during disconnected states and establish clear thresholds for autonomous decision-making.

Design local processing systems that support offline operations, with clearly defined
rules for degraded mode operations and boundaries for autonomous decisions based on safety
requirements and operational parameters.

For implementation, deploy edge computing capabilities that can maintain essential
operations during network disruptions. This requires integration with industrial control
systems and PLCs for real-time operations with appropriate redundancy and failover
mechanisms for critical manufacturing processes.

Consider using AWS IoT Greengrass to maintain local processing and decision-making when
connectivity is lost. Configure AWS IoT Greengrass components to cache production data locally and
execute critical workflows without cloud dependency.

**Deploy local data buffering mechanisms**

Analyzing your data generation patterns and retention requirements. Define priorities
for different data types and establish minimum retention periods based on operational and
compliance needs. Document synchronization requirements for when connectivity is restored.

Implement robust local storage systems with appropriate capacity planning for expected
outage durations. Configure data retention policies that preserve critical production
metrics during disconnection periods.

Consider using AWS IoT SiteWise Edge to continually collect data during network
outages, with configured data retention policies for high-value production metrics.

**Create automated data synchronization protocols**

Map data dependencies and establishing synchronization priorities. Define conflict
resolution rules for handling data updates during disconnected operations.

Document recovery procedures for different types of outages.

Design synchronization mechanisms that can handle data reconciliation when connectivity
is restored. Implement prioritization rules for critical production data during reconnection
events.

Consider using AWS IoT Core rules to prioritize critical production data during
reconnection events, with clear handling of potential data conflicts.

**Establish monitoring and alerting systems** 

Define normal operational parameters and alert thresholds. Document escalation
procedures and response requirements for different types of failures.

Establish KPIs for measuring recovery effectiveness. Implement comprehensive monitoring
of both edge and cloud components.

Configure automated alerts based on predefined thresholds and create recovery procedure
activations.

Consider using Amazon CloudWatch to detect failures and automatically initiate recovery
procedures based on predefined thresholds specific to manufacturing processes.

## Key AWS services

- AWS IoT Greengrass
- AWS IoT SiteWise
- AWS IoT Core
- Amazon CloudWatch
- AWS Lambda
- Amazon S3

## Resources

- [Implementing local processing with AWS IoT Greengrass](../../../greengrass/v2/developerguide/local-processing.md "../../../greengrass/v2/developerguide/local-processing.md")
- [Data buffering with AWS IoT SiteWise
  Edge](../../../iot-sitewise/latest/userguide/edge-data-processing.md "../../../iot-sitewise/latest/userguide/edge-data-processing.md")
- [Designing resilient manufacturing applications with AWS IoT Core](../../../whitepapers/latest/designing-mqtt-topics-aws-iot-core/designing-mqtt-topics-aws-iot-core.md "../../../whitepapers/latest/designing-mqtt-topics-aws-iot-core/designing-mqtt-topics-aws-iot-core.md")
