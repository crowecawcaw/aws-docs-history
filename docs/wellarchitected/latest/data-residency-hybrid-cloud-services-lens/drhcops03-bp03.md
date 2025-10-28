# DRHCOPS03-BP03 Build redundant network connectivity

Create redundant network connections to avoid connectivity loss to
the Region and your workloads.

**Desired outcome:** Redundant
network connectivity improves your availability posture and
supports your business continuity needs along with data residency
requirements

**Benefits of establishing this best
practice:** Deploying redundant network connectivity
using Outposts and Local Zones helps organizations maintain high
availability, minimize latency, and keep data within specified
geographic boundaries, addressing performance, resilience, and
regulatory needs.

**Level of risk exposed if this best
practice is not established:** High

## Implementation guidance

- Establish redundant network connections between Outposts and
  AWS Regions using AWS Direct Connect or VPN connections.
- Implement failover mechanisms to automatically switch over
  to a secondary network connection in case of a failure,
  reducing downtime and meeting RTO targets.
