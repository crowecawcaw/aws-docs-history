# DRHCOPS05-BP01 Understand monitoring requirements in your Local Zones

Focus on similar observability and alerting as in an Availability
Zone.

**Desired outcome:** Establish
monitoring capabilities that align with the architecture and
deployment model of workloads within an Availability Zone,
ensuring comprehensive visibility and observability across the
entire stack.

**Benefits of establishing this best
practice:** Implementing monitoring solutions enables
granular monitoring, accurate detection of issues, and targeted
troubleshooting, ultimately improving operational efficiency.

**Level of risk exposed if this best
practice is not established:** High

## Implementation guidance

Use the same mechanism for your workloads as you do in
[Availability
Zones](../framework/ops-04.md "../framework/ops-04.md") by implementing monitoring and alerting at
infrastructure and application layer through CloudWatch or
third-party tools.
