# HNCOST06-BP01 Implement QoS policies for traffic

prioritization

Configure QoS rules on on-premises routers to prioritize
latency-sensitive traffic such as voice and video over bulk
transfers such as data syncs.

**Desired outcome:** Guaranteed
performance for critical workloads while optimizing bandwidth costs.

**Level of risk exposed if this best practice
is not established:** Medium

**Benefits of establishing this best
practice:**

- Prevents costly performance degradation for high-priority
  traffic
- Enables oversubscription of links without impacting critical
  workloads
- Aligns network costs with business value

## Implementation guidance

- Tag traffic with DSCP markers for on-premises traffic
  classification
- Apply shapers or queues on on-premises routers
