

# Movement and caching
<a name="smsus06"></a>

Every transfer carries energy and often triggers duplicate processing downstream. Streaming amplifies both distance and repetition because popular assets are requested millions of times.


| SMSUS06: How do you minimize data movement in your streaming architecture? | 
| --- | 
| [SMSUS06-BP01 Optimize data flow and caching strategies](smsus06-bp01.md) | 

## Capability intent
<a name="smsus06-intent"></a>
+ Content is served from caches close to viewers so repeated requests don't return to origin.
+ Processing stays within a single Region where the architecture allows.
+ Intermediate file movement between stages is minimized.
+ Hot metadata is served from memory rather than queried on every request.

## Common issues to watch for
<a name="smsus06-issues"></a>
+ Serving directly from origin on every request instead of caching at the edge.
+ Spreading a transcode pipeline across regions so large files copy between regions at each stage.
+ Re-fetching whole assets when only a portion has changed.
+ No measurement of cache hit ratio or cross-region transfer volume.