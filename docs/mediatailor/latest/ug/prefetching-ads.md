# Prefetching ads

Use AWS Elemental MediaTailor ad prefetching for live streams to help reduce peak load on ad decision servers
(ADS) and decrease manifest delivery latency at the start of each ad break. When you define a
prefetch schedule, MediaTailor follows the schedule to retrieve ads from the ADS and prepare them for ad
insertion before they’re needed for an ad break. During live streams, prefetching can help
mitigate decreased ad fill rates and missed monetization opportunities because of ad request and
transcoding timeouts or other network delays.

To set up ad prefetching, you create one or more _prefetch
schedules_ on your playback configuration. A prefetch schedule tells MediaTailor how and when
to retrieve and prepare ads for an upcoming ad break.

- If an event has ad avails that are on a predictable schedule, use a _single prefetch schedule_. Each single prefetch schedule defines a single set of ads
  for MediaTailor to place in a single ad avail. To prefetch ads for multiple ad avails when you use
  single prefetch schedules, you must create multiple prefetch schedules (up to 24 hours before
  the ad avail) that correlate to each ad avail.
- If an event has ad avails that aren't on a predictable schedule, use a _recurring prefetch schedule_. A recurring prefetch schedule
  automatically creates a schedule and prefetches ads before each ad break in an event. The
  recurring prefetch schedule retrieves ads for every ad avail within a defined period of time (up
  to 24 hours before the event ends). You don’t need to create a schedule for each ad avail, but
  you do lose some of the timing control that single prefetch offers.
  The following topics describe more about ad prefetching.

###### Topics

- [How prefetching works](understanding-prefetching.md "understanding-prefetching.md")
- [Creating prefetch schedules](creating-prefetch-schedules.md "creating-prefetch-schedules.md")
- [TPS-based traffic shaping](tps-traffic-shaping.md "tps-traffic-shaping.md")
- [Deleting prefetch schedules](deleting-prefetch-schedules.md "deleting-prefetch-schedules.md")
