# DSREL06-BP01 Design Regional service continuity controls during

system degradation

Regional service continuity controls are essential for highly
regulated industries to maintain uninterrupted operations and
regulatory adherence during system degradation or partial failures.
These controls verify that workloads remain operational during
outages while preserving data integrity and audit trails, enabling
organizations to meet compliance mandates and maintain customer
trust. Proactive implementation of these controls protects against
regulatory violations, reduces risks, and supports business-critical
operations to meet service level agreements during Regional
disruptions.

**Desired outcome:** Organizations
maintain automated, policy-driven Regional failover and recovery
procedures across multiple AWS Regions. Service continuity,
regulatory adherence, and data consistency are preserved during
system performance degradation or outages. Business operations
continue without manual intervention during Regional disruptions.

**Common anti-patterns:**

- Relying on human intervention for degradation detection and
  Regional failover, leading to extended downtime and compliance
  violations.
- Insufficient cross-Region health checks and performance metrics
  to identify and respond to degradation early.
- Poor data synchronization, conflict resolution, and session
  management across Regions during failover scenarios.
- Inadequate provisioning in secondary Regions and lack of proper
  dependency management for third-party services.
- Implementing Regional continuity without verifying that
  secondary Regions meet compliance requirements and data
  sovereignty standards.
- Insufficient testing of failover procedures and lack of graceful
  degradation strategies for maintaining core functionality.

**Benefits of establishing this best
practice:**

- Maintains business operations through automated cross-Region
  failover capabilities, reducing downtime and data loss during
  Regional outages.
- Supports ongoing adherence to regulatory requirements with audit
  trail preservation and automated logging across Regions, meeting
  uptime and data durability standards.
- Reduces revenue loss and enhances customer confidence through
  seamless failover and consistent service delivery.
- Provides immediate, policy-driven responses to degradation
  events, reducing RTO and RPO without manual intervention.
- Optimizes infrastructure costs while maintaining high
  availability and compliance standards through efficient use of
  Regional resources.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

Design Regional service continuity through multi-Region
architectures (active-active or active-passive). Set up automated
monitoring and policy-driven failover mechanisms, verifying
consistent regulatory posture and maintaining core services during
degradation. Focus on automated remediation procedures and regular
testing of failure scenarios.

- Deploy across multiple Regions (minimum two when possible) and
  Availability Zones (minimum three when possible) with
  consistent security and compliance controls, if allowed within
  the soverign jurisdictional requirements. When multi-Region
  deployments are not possible because of data residency
  constraints, consider other options. For example:
  - Deploy active or passive instances on your own managed
    infrastructure to support minimum viable service levels.
    For some types of applications AWS Outposts or AWS Local
    Zones can also be considered.
  - Deploy active or passive instances with another Cloud
    Service provider on a temporary basis.

- Implement automated health monitoring, degradation detection,
  and intelligent DNS routing for seamless failover.
- Design stateless workloads with cross-Region replication
  capabilities for improved resilience. Configure robust data
  synchronization and conflict resolution mechanisms where state
  replication is necessary. For example, to support transactions
  or maintain event ordering.
- Create automated degradation response playbooks and test
  regularly using tools like AWS Fault Injection Service.
- Configure robust data synchronization and conflict resolution
  mechanisms across Regions.

### Implementation steps

1. Deploy infrastructure across at least two Regions and three
   Availability Zones. Configure inter-Region connectivity with
   [AWS Transit Gateway](../../../vpc/latest/tgw/tgw-transit-gateways.md "../../../vpc/latest/tgw/tgw-transit-gateways.md"). Use
   [Amazon Route 53](../../../route53.md "../../../route53.md") for global DNS management to provide high
   availability and resilience during system degradation.
2. Configure cross-Region data replication and establish
   conflict resolution mechanisms to maintain data consistency
   and availability across Regions using services like
   [Amazon DynamoDB](../../../dynamodb.md "../../../dynamodb.md") Global Tables and
   [Amazon S3](../../../s3.md "../../../s3.md") cross-Region replication.
3. Set up health checks and implement custom metrics with
   [Amazon CloudWatch Synthetics](../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Canaries.md "../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Canaries.md") canaries, and use
   [AWS X-Ray](../../../xray.md "../../../xray.md") for distributed tracing to detect service
   degradation promptly and trigger appropriate responses.
4. To support seamless service continuity during degradation
   events, implement DNS health checks, and DNS failovers using
   [Amazon Route 53](../../../route53.md "../../../route53.md"). Configure Application Load Balancer routing
   policies, and set up automated failover triggers using AWS Auto Scaling.

## Resources

**Related best practices:**

- [REL 10. How do you use fault isolation to protect your workload?](../reliability-pillar/use-fault-isolation-to-protect-your-workload.md "../reliability-pillar/use-fault-isolation-to-protect-your-workload.md")
- [REL 11. How do you design your workload to withstand component failures?](../reliability-pillar/design-your-workload-to-withstand-component-failures.md "../reliability-pillar/design-your-workload-to-withstand-component-failures.md")

**Related documents:**

- [Guidance
  for Cross Region Failover & Graceful Failback on
  AWS](https://aws.amazon.com/solutions/guidance/cross-region-failover-and-graceful-failback-on-aws/ "https://aws.amazon.com/solutions/guidance/cross-region-failover-and-graceful-failback-on-aws/")
- [Creating
  a Multi-Region Application with AWS Services series](https://aws.amazon.com/blogs/architecture/tag/creating-a-multi-region-application-with-aws-services-series/ "https://aws.amazon.com/blogs/architecture/tag/creating-a-multi-region-application-with-aws-services-series/")
- [Creating
  an organizational multi-Region failover strategy](https://aws.amazon.com/blogs/architecture/creating-an-organizational-multi-region-failover-strategy/ "https://aws.amazon.com/blogs/architecture/creating-an-organizational-multi-region-failover-strategy/")

**Related videos:**

- [AWS re:Invent 2024 - Best practices for creating multi-Region
  architectures on AWS (ARC323)](https://www.youtube.com/watch?v=CbkqQznZS9Y "https://www.youtube.com/watch?v=CbkqQznZS9Y")
- [Back
  to Basics: Implementing Multi-Region Disaster Recovery with
  AWS Elastic Disaster Recovery (DRS)](https://aws.amazon.com/awstv/watch/c24c182eefd/ "https://aws.amazon.com/awstv/watch/c24c182eefd/")
- [Managing
  Cross-region Copies of Backups With AWS Backup](https://www.youtube.com/watch?v=qMN18Lpj3PE "https://www.youtube.com/watch?v=qMN18Lpj3PE")

**Related services:**

- [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/ "https://aws.amazon.com/cloudwatch/")
- [Amazon DynamoDB](https://aws.amazon.com/dynamodb/ "https://aws.amazon.com/dynamodb/")
- [Amazon Route 53](https://aws.amazon.com/route53/ "https://aws.amazon.com/route53/")
- [Amazon S3](https://aws.amazon.com/s3/ "https://aws.amazon.com/s3/")
- [AWS Auto Scaling](https://aws.amazon.com/autoscaling/ "https://aws.amazon.com/autoscaling/")
- [AWS Transit Gateway](https://aws.amazon.com/transit-gateway/ "https://aws.amazon.com/transit-gateway/")
- [AWS X-Ray](https://aws.amazon.com/xray/ "https://aws.amazon.com/xray/")
