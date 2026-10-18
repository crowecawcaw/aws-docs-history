

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

## Common issues to watch for
<a name="smperf01-issues"></a>
+ A single origin type used for both live and VOD regardless of their different requirements.
+ Pass-through origins where just-in-time packaging would remove format proliferation.
+ Tight coupling between origin and CDN that blocks independent evolution.