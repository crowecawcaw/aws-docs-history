

# How failure mode assessments work
<a name="next-gen-how-assessments-work"></a>

When you run a failure mode assessment, Next generation Resilience Hub performs the following steps:

1. **Reads current resource state** – Refreshes your service's resource configuration from your AWS account.

1. **Analyzes the topology** – A multi-agent AI system examines how your resources connect and interact.

1. **Evaluates against policies using the resilience analysis framework** – Compares your architecture against your resilience policies. It first performs an assessment to determine if policy components are achievable or not.

1. **Applies AWS Well-Architected best practices** – Checks for common resilience anti-patterns.

1. **Generates findings** – Identifies failure modes with severity, reasoning, and recommendations, and maps results to your resilience policies.

The assessment engine uses specialized AI agents that apply AWS Well-Architected Framework reliability best practices and the AWS Resilience Analysis Framework to your specific architecture. Agents analyze different aspects of resilience:
+ **Availability** – Single points of failure, AZ distribution, and redundancy.
+ **Disaster recovery** – Cross-region capabilities, replication, and failover readiness.
+ **Dependency resilience** – Impact of dependency failures on your service.
+ **Observability** – Monitoring gaps that could delay failure detection.

The failure mode assessment does not consume all available resources. Instead it evaluates a subset of resources known as assessed resources.

**Assessed resource:** A top-level infrastructure or service component that is directly evaluated during a resilience assessment. A resource is assessed if its configuration has a meaningful impact on availability, recoverability, or fault tolerance of the service. Resources outside of this scope will not have any impact on assessment and will not be surfaced in list-resources.