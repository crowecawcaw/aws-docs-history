# MIDAREL02-BP02 Verify data consistency and availability across OT/IT systems through

redundancy and failover mechanisms

Manufacturing environments operate with complex interactions between OT and IT systems.
When these systems fail, the impact can cascade through production lines, quality control
processes, and enterprise planning systems. Successfully maintaining data consistency and
system availability requires careful orchestration of data synchronization, communication
paths, and recovery procedures across the manufacturing technology stack.

**Desired outcome:** Production operations continue with
minimal disruption during system failures. Critical operational data remains available and
consistent during disruptions, allowing for automated or manual fallback procedures to
maintain production output while primary systems are restored.

**Benefits of establishing the Best Practice:**

- Minimize production downtime and associated revenue losses.
- Preserve data integrity across manufacturing systems.
- Enable smooth recovery without data reconciliation challenges.
- Maintain quality control and regulatory compliance during system failures.

**Level of risk exposed if this best practice is not
established:** High

## Implementation guidance

**Real-time manufacturing data management**

First, map your critical manufacturing data flows and establish requirements for data
synchronization across OT/IT systems. Document recovery time objectives (RTOs), recovery
point objectives (RPOs), and regulatory compliance needs.

Define data models that support consistent representation of equipment states and
process parameters across systems.

For implementation, establish standardized data models and real-time state management
systems for production equipment and processes. Verify data consistency through distributed
databases with conflict resolution capabilities.

Consider using AWS IoT SiteWise for consistent equipment and process data models, AWS IoT Core's Device Shadow service for reliable state management, and Amazon DynamoDB global
tables for distributed manufacturing data management.

**Data validation and quality controls**

Document data quality requirements for different manufacturing processes and establish
validation rules. Define acceptable tolerance ranges for process parameters and identify
critical quality metrics that must be maintained during system transitions.

Implement automated validation mechanisms that verify data integrity across systems,
with standardized data quality rules and monitoring.

Set up continuous validation of data synchronization between OT/IT systems and
establish regular backup points for critical manufacturing datasets.

Consider implementing AWS Glue Data Quality rules for automated validation, AWS IoT SiteWise Asset Models for standardized validation, and AWS Backup for consistent recovery
points.

**Recovery mechanisms and failover systems** 

Document system dependencies and define acceptable failover scenarios. Establish clear
procedures for both automated and manual recovery processes.

Determine sequence of operations for graceful system transitions that preserve data
integrity. Design idempotent processing mechanisms to help prevent data duplication during
recovery.

Implement point-in-time recovery capabilities for critical production systems and
configure automated failover with health monitoring.

Consider using Amazon DynamoDB Point-in-Time Recovery for maintaining accurate
operational states, Amazon Route 53 health checks for automated failover, and AWS Systems Manager for coordinated recovery automation.

## Key AWS services

- AWS IoT SiteWise
- AWS IoT Core
- Amazon Timestream
- Amazon DynamoDB
- AWS Glue Data Quality
- Amazon CloudWatch
- AWS Backup
- Amazon Route 53
- AWS Systems Manager

## Resources

- [AWS IoT SiteWise for industrial data collection and monitoring](../../../iot-sitewise/latest/userguide/what-is-sitewise.md "../../../iot-sitewise/latest/userguide/what-is-sitewise.md")
- [Using Device Shadows for manufacturing equipment state management](../../../iot/latest/developerguide/iot-device-shadows.md "../../../iot/latest/developerguide/iot-device-shadows.md")
- [Implementing DynamoDB Global Tables for distributed manufacturing data](../../../amazondynamodb/latest/developerguide/GlobalTables.md "../../../amazondynamodb/latest/developerguide/GlobalTables.md")
- [AWS Glue
  Data Quality for manufacturing data validation](../../../glue/latest/dg/data-quality.md "../../../glue/latest/dg/data-quality.md")
