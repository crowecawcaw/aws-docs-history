# DRHCPERF01-BP02 Monitor hybrid edge-specific metrics, and update resource configurations

Monitor your current capacity and plan for scaling to meet demand.

**Desired outcome:** You are aware
of what capacity you have, and you scale as needed.

**Benefits of establishing this best
practice:** You can proactively make decisions to acquire
the appropriate capacity for your workloads.

**Level of risk exposed if this best
practice is not established:** Medium

## Implementation guidance

Outposts surfaces Amazon CloudWatch metric data, including CPU,
network, and storage. You should monitor these metrics as you
would in-Region to verify that you are achieving your
performance targets. Monitor your resource consumption, and
right-size compute and storage configurations based on the
metric data. This is an iterative process as workloads change
over time. Each server has a specific slotting configuration
based on initial order. This can be modified based on metric
data as long as the configuration is supported by the underlying
server. For supported configurations, see
[Modify
AWS Outposts instance capacity](../../../outposts/latest/userguide/modify-instance-capacity.md "../../../outposts/latest/userguide/modify-instance-capacity.md").
