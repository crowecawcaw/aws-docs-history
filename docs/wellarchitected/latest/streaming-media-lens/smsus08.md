

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

## Maturity levels
<a name="smsus08-maturity"></a>


| Level | Name | What it looks like | 
| --- | --- | --- | 
| 1 | Initial | Most capabilities self-managed on standing infrastructure provisioned for peak. Low average utilization. | 
| 2 | Emerging | Managed services adopted for new workloads. Legacy self-managed infrastructure remains but is identified. | 
| 3 | Defined | A documented policy defaults to managed services where the workload fits. Self-managed components are justified by specific requirements. | 
| 4 | Proactive | The share of workloads on managed services is tracked. Idle capacity removed by migration is measured. | 
| 5 | Optimized | Remaining self-managed components are periodically re-evaluated as managed offerings evolve. Utilization improvement from the shift is reviewed alongside carbon data. | 

## Common issues to watch for
<a name="smsus08-issues"></a>
+ Building bespoke infrastructure when a managed service provides the same capability at higher utilization.
+ Standing clusters sized for peak to run intermittent work, idle between jobs.
+ Self-hosting ML inference on persistent instances when managed inference scales with request volume.
+ Assuming that managed is unconditionally better without evaluating workload fit.