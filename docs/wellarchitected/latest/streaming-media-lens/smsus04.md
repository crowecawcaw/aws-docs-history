

# Live streaming efficiency
<a name="smsus04"></a>

Live workflow resource cost is governed by event duration and concurrent audience rather than catalog size. Channels that run idle between events or default to ultra-low latency for every stream consume resources without corresponding value.


| SMSUS04: How do you optimize your live streaming architecture for sustainability? | 
| --- | 
| [SMSUS04-BP01 Design efficient, scalable live streaming workflows](smsus04-bp01.md) | 

## Capability intent
<a name="smsus04-intent"></a>
+ Live channels run only for the scheduled event window and stop when the event ends.
+ The latency tier for each event matches the experience requirement rather than defaulting to the lowest available.
+ Pipeline redundancy is applied where availability justifies it, not uniformly.
+ Supporting components scale to observed concurrency rather than a peak assumption.

## Common issues to watch for
<a name="smsus04-issues"></a>
+ Channels left running continuously between events.
+ Ultra-low latency applied as a blanket default regardless of content type.
+ Standing redundant pipelines for all channels regardless of the event's availability needs.
+ No tracking of channel run-hours or redundant pipeline-hours per event.