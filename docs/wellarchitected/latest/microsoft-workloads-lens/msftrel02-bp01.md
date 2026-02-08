# MSFTREL02-BP01 Implement comprehensive monitoring for potential

failures across the application, AWS infrastructure, and network
connectivity

Monitoring your Microsoft application, AWS resources, and network
connectivity enables prompt responses to both actual and potential
failures, enhancing overall system reliability.

**Desired outcome:** Comprehensive
monitoring across the Microsoft application, AWS infrastructure, and
network components will enable early detection of issues and prompt
response to potential failures, optimizing system reliability and
performance.

**Common anti-patterns:**

- Only responding to issues after they cause significant
  disruptions, rather than proactively monitoring for potential
  problems.
- Monitoring individual components in isolation without
  considering the interconnected nature of the application,
  infrastructure, and network.
- Focusing monitoring efforts solely on the application layer
  while neglecting AWS infrastructure and network connectivity
  monitoring.

**Benefits of establishing this best
practice:**

- Comprehensive monitoring enables quick identification and
  resolution of issues, reducing downtime and enhancing overall
  system stability.
- Continuous monitoring provides valuable insights into system
  behavior, allowing for data-driven optimizations and resource
  allocation.
- Proactive monitoring reduces the time and resources spent on
  troubleshooting, allowing IT teams to focus on strategic
  initiatives rather than firefighting.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

Begin by identifying critical monitoring metrics across each layer
(application, infrastructure, and network) and implement a primary
monitoring solution like Amazon CloudWatch. Set up custom metrics
and dashboards for Microsoft application-specific monitoring,
configure detailed AWS resource monitoring, and establish network
connectivity checks.

Set up automated alerting and aggregate logs. Define clear
thresholds and escalation procedures, and implement automated
responses where appropriate.

Regularly review and refine your monitoring parameters to maintain
the effectiveness of the monitoring strategy.

### Implementation steps

1. Define and configure essential metrics and alarms for
   Microsoft workloads with thresholds appropriate to your
   specific environment and SLA requirements, including:
   1. SQL Server performance monitoring (CPU utilization,
      memory availability, deadlock detection, backup status)
   2. Active Directory health checks (authentication failures,
      replication status, SYSVOL synchronization)
   3. IIS or .NET application monitoring (application pool
      health, HTTP error rates, worker process status)
   4. Windows system alerts (disk space, memory utilization,
      critical service status)
   5. AWS infrastructure monitoring for underlying EC2, EBS,
      and network components

2. Create consolidated dashboards for unified visibility across
   your monitored components.
3. Set up topics and subscription endpoints for automated
   alerting based on predefined thresholds.
4. Implement centralized logging and configure log metric
   filters.
5. Establish automated remediation actions in response to
   specific alarm conditions.

## Resources

**Related documents:**

- [Monitor
  workload resources](../reliability-pillar/monitor-workload-resources.md "../reliability-pillar/monitor-workload-resources.md")
- [Designing
  and implementing logging and monitoring with Amazon CloudWatch](../../../prescriptive-guidance/latest/implementing-logging-monitoring-cloudwatch/welcome.md "../../../prescriptive-guidance/latest/implementing-logging-monitoring-cloudwatch/welcome.md")

**Related tools:**

- [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/ "https://aws.amazon.com/cloudwatch/")
- [Amazon Simple Notification Service](https://aws.amazon.com/sns/ "https://aws.amazon.com/sns/")
- [AWS Lambda](https://aws.amazon.com/lambda/ "https://aws.amazon.com/lambda/")
