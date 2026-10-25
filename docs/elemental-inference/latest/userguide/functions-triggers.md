

# Triggers
<a name="functions-triggers"></a>

The trigger on the function output decides how often the function runs, and therefore how much you spend on model invocations. You set it on each attachment, not on the function, so the same function can run on a fixed cadence on one feed and once per scene on another.


| Trigger | Runs | Requirements | 
| --- | --- | --- | 
| fixedInterval | Every intervalSeconds of content, from 1 through 60 seconds. With media.clip, also runs as soon as the event clipping output reports an event, and the interval restarts. | Can't be used with media.contextual. With media.clip, requires a named event clipping output. | 
| perShot | Once for each shot that Elemental Inference detects. | Can't be used with media.transcript or media.clip. With media.contextual, requires a named contextual metadata output. | 
| perScene | Once for each scene boundary that a contextual metadata output reports. | Requires a named contextual metadata output. Can't be used with media.transcript or media.clip. | 
| perClip | Once for each window in which an event clipping output reports at least one event. All the window's events are in media.clip.events. | Requires a named event clipping output. Can't be used with media.transcript or media.contextual. | 

The boundary triggers — `perShot`, `perScene`, and `perClip` — align the analysis and its cost with the editorial structure of the content instead of a clock. A one-hour program might contain a few hundred shots but 3,600 one-second intervals.

**Tip**  
Start with the longest interval that still answers your question, then shorten it. A function on a one-second interval against a large model is a continuous, high-rate workload against your own Amazon Bedrock quotas.