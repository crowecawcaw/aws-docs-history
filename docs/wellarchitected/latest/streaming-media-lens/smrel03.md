

# Content distribution
<a name="smrel03"></a>

Content distribution is the final step before viewers. Failures here directly cause buffering, playback errors, or complete outages. Distribution reliability covers origin redundancy, CDN failover, and multi-tier caching.


| SMREL03: How does your streaming workflow provide reliable content distribution from origin to viewers? | 
| --- | 
| [SMREL03-BP01 Implement multi-tier distribution with origin redundancy and content delivery network (CDN) failover](smrel03-bp01.md) | 

## Capability intent
<a name="smrel03-intent"></a>
+ Viewers receive uninterrupted streaming when individual origin servers, CDN points of presence, or entire regions experience outages.
+ Origin failover is health-check-driven and automatic.
+ Cache warming prepares edge locations ahead of high-demand live events.
+ Multi-CDN or multi-origin strategies provide fallback when a single path fails.

## Common issues to watch for
<a name="smrel03-issues"></a>
+ Single origin without failover or health-check-based routing.
+ No origin shielding, so cache misses overwhelm origin during spikes.
+ No cache warming for live events, causing a thundering herd at the origin on event start.
+ Single CDN reliance with no fallback path for regional CDN failures.