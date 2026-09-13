

# Region selection
<a name="smsus01"></a>

Region selection determines the baseline environmental cost of a streaming service. The energy mix of the Region and the distance content travels to viewers are fixed before any other optimization takes effect.


| SMSUS01: How do you select regions to optimize your streaming media workloads for sustainability? | 
| --- | 
| [SMSUS01-BP01 Optimize regional distribution of streaming workloads to reduce waste, unnecessary use of resources and use of non-renewable energy](smsus01-bp01.md) | 

## Capability intent
<a name="smsus01-intent"></a>
+ Compute-intensive workloads run in regions chosen with carbon intensity as an explicit selection criterion.
+ Content reaches viewers from nearby caches so transfer distance and energy are minimized.
+ Multi-region footprint follows demonstrated redundancy and latency needs rather than default posture.
+ Placement decisions are reviewed against measured per-region carbon data on a regular cadence.
+ Latency-sensitive delivery and latency-tolerant batch work are placed independently based on their different proximity requirements.

## Maturity levels
<a name="smsus01-maturity"></a>


| Level | Name | What it looks like | 
| --- | --- | --- | 
| 1 | Initial | Regions selected on cost or latency alone. No awareness of carbon intensity in placement decisions. | 
| 2 | Emerging | Carbon intensity data is consulted for new deployments but existing placements are not revisited. | 
| 3 | Defined | Carbon intensity is a documented selection criterion. Latency-tolerant batch is placed independently from delivery. | 
| 4 | Proactive | Placement is reviewed against per-region carbon data on a regular cadence. Multi-region footprint is justified by documented requirements. | 
| 5 | Optimized | Workloads shift dynamically or are re-evaluated as regional energy mixes change. Carbon data drives ongoing placement refinement. | 

## Common issues to watch for
<a name="smsus01-issues"></a>
+ Selecting regions on cost and latency alone with no visibility into carbon intensity.
+ Deploying to many regions for resilience that the workload doesn't require, multiplying infrastructure footprint.
+ Serving a global audience from a single distant region because the architecture was never revisited after initial deployment.
+ Placing compute-intensive transcoding in a high-carbon region for convenience when lower-carbon alternatives exist.
+ No periodic review of placement against the AWS Customer Carbon Footprint Tool data.