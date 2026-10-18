

# Alignment to demand
<a name="smsus02"></a>

Streaming demand varies by orders of magnitude across the day and across events. Infrastructure sized for a theoretical peak sits idle most of its life.


| SMSUS02: How do you align streaming quality and infrastructure with viewer demand? | 
| --- | 
| [SMSUS02-BP01 Implement adaptive infrastructure scaling based on viewer patterns](smsus02-bp01.md) | 

## Capability intent
<a name="smsus02-intent"></a>
+ Media processing capacity follows real-time audience size rather than holding a static peak.
+ Delivery bit rate adapts to each session's network and device capability.
+ Deferrable processing runs during off-peak or lower-carbon-intensity periods.
+ Scaling responds to both predictable patterns and unexpected demand spikes.
+ Utilization is tracked and idle capacity is treated as waste to be reduced.

## Common issues to watch for
<a name="smsus02-issues"></a>
+ Fixed provisioning based on a worst-case assumption that is never revisited.
+ Delivering a single high bit rate to all viewers regardless of what their session can use.
+ Running batch work during peak demand, competing with live traffic for resources.
+ Reactive-only scaling without predictive pre-warming for known events.