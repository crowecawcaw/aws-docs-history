

# Managed services
<a name="smsus08"></a>

A self-managed component provisioned for one team's peak sits idle most of the time. Managed services aggregate demand across customers and scale to match, reaching higher average utilization.


| SMSUS08: How do you use managed services to improve sustainability? | 
| --- | 
| [SMSUS08-BP01 use AWS managed services for efficient resource utilization](smsus08-bp01.md) | 

## Capability intent
<a name="smsus08-intent"></a>
+ Capabilities that have a managed equivalent are consumed as managed services.
+ Workloads scale with demand rather than holding idle capacity for rare peaks.
+ Engineering effort goes to streaming-specific differentiation rather than operating commodity infrastructure.

## Common issues to watch for
<a name="smsus08-issues"></a>
+ Building bespoke infrastructure when a managed service provides the same capability at higher utilization.
+ Standing clusters sized for peak to run intermittent work, idle between jobs.
+ Self-hosting ML inference on persistent instances when managed inference scales with request volume.
+ Assuming that managed is unconditionally better without evaluating workload fit.