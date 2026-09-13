

# Media origination
<a name="smperf01"></a>

Origin technology selection directly affects delivery performance. The choice between pass-through origins and just-in-time packaging origins depends on workload characteristics. These include live compared to VOD, viewer count, latency targets, and format diversity.


| SMPERF01: How do you optimize media delivery through media origination and processing? | 
| --- | 
| [SMPERF01-BP01 Select origin technology appropriate for your workload](smperf01-bp01.md) | 

## Capability intent
<a name="smperf01-intent"></a>
+ Origin type is selected against workload characteristics rather than applied uniformly.
+ The origin architecture can evolve without re-architecting the CDN or client stack.
+ Pass-through and dynamic packaging are applied where each fits best.

## Maturity levels
<a name="smperf01-maturity"></a>


| Level | Name | What it looks like | 
| --- | --- | --- | 
| 1 | Initial | A single origin type serves all workloads with no consideration of live compared to VOD differences. | 
| 2 | Emerging | The team recognizes that live and VOD have different origin needs but has not separated them. | 
| 3 | Defined | Pass-through and JIT packaging origins are deployed for their respective use cases with documented selection criteria. | 
| 4 | Proactive | Origin selection is reviewed when new formats or latency targets emerge, and the CDN can be reconfigured independently. | 
| 5 | Optimized | Origin architecture evolves continuously based on workload telemetry, with automated format negotiation and no coupling to CDN or client changes. | 

## Common issues to watch for
<a name="smperf01-issues"></a>
+ A single origin type used for both live and VOD regardless of their different requirements.
+ Pass-through origins where just-in-time packaging would remove format proliferation.
+ Tight coupling between origin and CDN that blocks independent evolution.