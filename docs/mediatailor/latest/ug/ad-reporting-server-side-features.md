# MediaTailor server-side tracking features and

capabilities

AWS Elemental MediaTailor automatically applies these integrated server-side tracking features to
optimize ad measurement accuracy and reliability. The system prevents duplicate beacons,
manages traffic during high-volume periods, maintains proper event sequencing, and provides
comprehensive performance monitoring without requiring any configuration from you. You only need to ensure your ad decision server (ADS) provides the tracking beacons in the VAST response.

###### Note

These features are available for new customers starting September 30, 2025. Existing
customers will have access throughout 2025 as part of ongoing service improvements. If
you want immediate access to these features, contact [AWS Support](https://aws.amazon.com/premiumsupport/ "https://aws.amazon.com/premiumsupport/").

## Beacon

deduplication

MediaTailor prevents duplicate beacon firing for identical ad events. The server-side
tracking system sends each impression, quartile, and completion beacon only once per ad
viewing session. When video players request the same ad segment multiple times due to
network conditions, bitrate changes, or buffering strategies, MediaTailor tracks fired beacons
and blocks redundant transmissions.

Deduplication automatically resolves common scenarios that cause inflated beacon
counts:

- **Adaptive bitrate streaming** - When players
  download different quality variants of the same ad segment
- **Network retry scenarios** - When players
  re-request segments due to network issues or timeouts
- **Player buffering strategies** - When players
  pre-fetch or re-fetch segments for buffering purposes

The system ensures impression beacons fire only once, even when players switch between different quality levels.

## Adaptive throttling and

beacon retries

MediaTailor automatically manages beacon traffic rates based on
server response indicators. The system monitors HTTP response patterns,
connection timeouts, and error codes to detect congestion, then adjusts traffic rates
accordingly. When the system identifies server stress indicators, it reduces traffic
rates for the affected domain and automatically increases rates when servers
demonstrate improved capacity.

The system monitors server health using these indicators:

- **HTTP connection timeouts** - When
  measurement platforms don't respond within expected timeframes
- **Error response codes** - 503, 504, and
  507 responses that indicate server overload. Your ad server must also support these error codes for full compatibility.
- **Response patterns** - Measurement
  platform performance changes that indicate capacity issues

Retry behavior automatically attempts delivery for up to 1 hour with minimum 30-second
delays between attempts. This retry behavior cannot be configured.

## Beacon traffic per second

management

You can set TPS limits to control beacon delivery rates. This is the only configurable setting for server-side tracking features. Account-level limits cap the total number
of ad tracking requests sent across all measurement partners. MediaTailor enforces a minimum
TPS limit of 10,000 to ensure sufficient capacity for enterprise-scale
operations.

Submit an AWS support ticket to establish TPS limits with the following
information:

- **AWS account ID** - Your specific account
  identifier
- **Target region** - The AWS region where you want
  the TPS limit applied
- **Desired TPS threshold** - Your required
  transactions per second limit (minimum 10,000)

By default, there is no TPS limit. You can request a TPS limit if your ad decision server (ADS) requires it, but the limit must be greater than 10,000 TPS. MediaTailor will not exceed your specified limit, but does not guarantee consistent throughput up to that limit. Your ad decision server
will tell you what TPS limits it can support.

## In-order beaconing

MediaTailor automatically maintains sequential delivery of ad tracking
events. The system preserves beacon ordering even when network issues, retries, or traffic management occur. This ensures measurement partners receive
events in the correct order for accurate analytics.

The system follows the standard industry beacon sequence:

1. **Start events** - Fire when ad playback
   begins
2. **First quartile events** - Fire at 25% ad
   completion
3. **Midpoint events** - Fire at 50% ad
   completion
4. **Third quartile events** - Fire at 75% ad
   completion
5. **Completion events** - Fire when ads
   finish

These features work together automatically:

- Beacons are held during throttling to maintain proper order
- Each measurement partner domain has separate event queues to prevent disruption during rate adjustments
- Deduplication tracks event type and timeline position while maintaining chronological order
