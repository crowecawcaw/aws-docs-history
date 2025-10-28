# TPS-based traffic shaping

AWS Elemental MediaTailor provides two optional traffic shaping approaches to limit the number of requests
to the ADS at one time. TPS-based traffic shaping offers an alternative to time-window based
traffic shaping for prefetch schedules. This approach provides more intuitive configuration by
allowing you to specify your ad decision server (ADS) capacity in terms of transactions per
second (TPS) and expected concurrent users, rather than time calculations.

## How TPS-based traffic shaping works

Instead of specifying retrieval window durations, you provide the following
parameters:

Peak TPS

The maximum number of requests per second that your ADS can handle. This parameter has
no default value.

Peak concurrent users

The expected peak number of concurrent viewers for your content. This parameter has no
default value.

MediaTailor automatically distributes prefetch requests across time to stay within your specified
TPS limit, regardless of the number of concurrent sessions.

###### Example TPS-based configuration example

Your ADS can handle 500 TPS, and you expect 100,000 concurrent viewers during peak times.
You configure:

- Peak TPS: 500
- Peak concurrent users: 100,000
  MediaTailor automatically distributes prefetch requests across time to stay within your
  specified TPS limit, regardless of the number of concurrent sessions.
