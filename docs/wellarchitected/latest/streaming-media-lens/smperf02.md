

# Source contribution
<a name="smperf02"></a>

Source quality and transport reliability constrain what the entire downstream pipeline can deliver. Contribution protocol choice and source acquisition quality have a direct effect on what viewers ultimately see.


| SMPERF02: How do you approach media source contribution? | 
| --- | 
| [SMPERF02-BP01 Start with the highest quality source reasonably obtainable](smperf02-bp01.md) | 
| [SMPERF02-BP02 Use specialized media transport and acceleration protocols](smperf02-bp02.md) | 

## Capability intent
<a name="smperf02-intent"></a>
+ Sources are acquired at the highest quality reasonably obtainable for the use case.
+ Contribution uses reliable UDP-based transport protocols with redundant paths.
+ Transport metrics (round-trip time, packet loss, jitter) are monitored in real time with auto-failover.

## Maturity levels
<a name="smperf02-maturity"></a>


| Level | Name | What it looks like | 
| --- | --- | --- | 
| 1 | Initial | Sources are accepted as-is from providers with no quality requirements or transport monitoring. | 
| 2 | Emerging | Basic bit rate monitoring exists, but transport metrics like loss and jitter are not tracked. Contribution uses RTMP without redundancy. | 
| 3 | Defined | Quality requirements are specified for source providers, reliable UDP-based protocols are in use, and redundant paths exist for critical feeds. | 
| 4 | Proactive | Transport metrics (RTT, loss, and jitter) are monitored in real time with automated failover between redundant paths. | 
| 5 | Optimized | Source quality is continuously validated against SLAs, bonded contribution adapts dynamically, and failover is exercised regularly with no viewer impact. | 

## Common issues to watch for
<a name="smperf02-issues"></a>
+ Accepting whatever a provider delivers without specifying quality requirements.
+ Using TCP-based contribution (RTMP) for mission-critical live without fallback.
+ Monitoring only bit rate while ignoring loss, jitter, and round-trip time.
+ Single network path without bonded or redundant connectivity.