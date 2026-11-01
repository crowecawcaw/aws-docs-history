

# Beaconing configuration
<a name="beaconing-configuration"></a>

In client-side reporting, your player sends ad tracking beacons directly to your ad server and to your ad-verification providers. MediaTailor doesn't see those requests, so the ad tracking metrics and logs that you get with server-side reporting have no client-side equivalent. This makes it hard to compare ad delivery across the two reporting modes, or to tell whether a drop in reported impressions is an ad problem or a player problem.

With the beaconing configuration, MediaTailor includes a beacon of its own in the ad tracking response, alongside the ad server beacons that are already there. Your player sends all of them as it normally would, and the request to MediaTailor reports that the event happened. MediaTailor then publishes the same `Avail.*` CloudWatch metrics that it publishes for server-side reporting, and writes a `BEACON_RECEIVED` log entry for the event that fired.

**Important**  
MediaTailor **vends** its beacon in the tracking response. Your ad server URLs are preserved, MediaTailor doesn't remove or replace any of them, and it doesn't send any beacon on your player's behalf. Your existing ad tracking and verification workflow continues to work as it did before.

You configure this behavior with the `BeaconingConfiguration` setting on your playback configuration, or in the MediaTailor console. For more information, see [Configuring beaconing](#beaconing-configuration-configure).

## How beaconing works
<a name="beaconing-configuration-how-it-works"></a>

1. Your player starts a client-side reporting session and requests tracking data, as described in [Client-side reporting workflow](ad-reporting-client-side.md#ad-reporting-client-side-workflow).

1. For each ad in the response, MediaTailor vends a beacon of its own in the `beaconUrls` list of every tracking event that it reports on. Your ad server URLs stay in the list.

1. Your player sends every URL in the list when the matching playback milestone happens. You don't need to change your player.

1. MediaTailor receives the request and identifies the session, the ad, and the tracking event from the URL. It then publishes the `Avail.*` metric for that event type and writes a `BEACON_RECEIVED` log entry.

MediaTailor beacons look like the following, where {{N}} is an internal partition number and {{region}} is the AWS Region of your playback configuration:

```
https://{{N}}.ping.mediatailor.{{region}}.amazonaws.com/v1/e/{{N}}/{{accountId}}/{{configurationName}}/{{sessionId}}/{{token}}
```

If your player, content delivery network, or network policy limits the destinations that a player can call, allow this domain so that MediaTailor can report your events.

**Note**  
MediaTailor always answers these requests with HTTP 200, even when it can't process the request. A problem with beaconing never shows up as a player error and never affects playback. It also means you can't use the response status to confirm that an event was recorded – check the `Avail.*` metrics or the `BEACON_RECEIVED` log entries instead.

## Tracking events that MediaTailor reports on
<a name="beaconing-configuration-event-types"></a>

MediaTailor always reports on the following ad progress events. If your ad server's VAST response doesn't include a tracking event for one of them, MediaTailor adds that event to the tracking response with only its own beacon, so that you get a complete ad completion funnel even when your ad server doesn't ask for every milestone.


| Tracking event | Metric | 
| --- | --- | 
| impression | Avail.Impression | 
| start | Avail.Start | 
| firstQuartile | Avail.FirstQuartile | 
| midpoint | Avail.Midpoint | 
| thirdQuartile | Avail.ThirdQuartile | 
| complete | Avail.Complete | 

You can also choose to report on the following player operation events. MediaTailor never sends these beacons itself, because only a player can tell when a viewer performs the action, so these metrics have no server-side equivalent. MediaTailor vends a beacon for each event type that you choose, so the event always appears for an ad in the tracking response.


| Event type | Metric | Description | 
| --- | --- | --- | 
| MUTE | Avail.Mute | The viewer muted the ad. | 
| UNMUTE | Avail.Unmute | The viewer unmuted the ad. | 
| PAUSE | Avail.Pause | The viewer paused the ad. | 
| SKIP | Avail.Skip | The viewer skipped the ad. Compare Avail.Skip to Avail.Impression to measure the skip rate for your skippable ads. | 

## Configuring beaconing
<a name="beaconing-configuration-configure"></a>

Beaconing is on by default. To change it, set `BeaconingConfiguration` on your playback configuration with the `PutPlaybackConfiguration` API, or edit your playback configuration in the MediaTailor console.

The settings are nested inside a `ClientSide` object, which leaves room for server-side beaconing settings in the same structure later:


| API setting | Console field | Description | 
| --- | --- | --- | 
| ClientSide.ReportingMode | Reporting mode | Whether MediaTailor includes its beacons in the ad tracking response. Valid values are `INSIGHTS` and `DISABLED`. If you send a `ClientSide` object, this setting is **required**. If you omit `BeaconingConfiguration` or `ClientSide` entirely, MediaTailor uses `INSIGHTS`. | 
| ClientSide.AdditionalEventTypes | Additional event types | The player operation events to report on, in addition to the ad progress events that MediaTailor always reports on. Valid values are `MUTE`, `UNMUTE`, `PAUSE`, and `SKIP`. The default is an empty list. Valid only when `ReportingMode` is `INSIGHTS`. | 

Both values are case-sensitive. MediaTailor rejects a request that uses any other capitalization, such as `insights` or `mute`.

**Important**  
`PutPlaybackConfiguration` replaces your whole playback configuration, and MediaTailor treats an absent `BeaconingConfiguration` as `INSIGHTS`. If you turned beaconing off, you must send `DISABLED` on **every** subsequent write – a later update that omits the setting turns beaconing back on.

MediaTailor rejects the following requests:
+ A `ClientSide` object with no `ReportingMode`.
+ `AdditionalEventTypes` with one or more values when `ReportingMode` is `DISABLED`. An empty list is allowed.
+ A duplicate value in `AdditionalEventTypes`.

`GetPlaybackConfiguration` always returns a `BeaconingConfiguration`. For a playback configuration you created before this setting existed, MediaTailor reports `ReportingMode` as `INSIGHTS`, which is how it treats that configuration at playback time.

In the console, these fields are in the **Beaconing configuration** section of your playback configuration, and their current values appear on the **Beaconing** tab of the configuration details page.

### Reporting mode values
<a name="beaconing-configuration-modes"></a>

`INSIGHTS`  
For each ad, MediaTailor includes a beacon of its own for `impression`, `start`, `firstQuartile`, `midpoint`, `thirdQuartile`, and `complete`, alongside your existing ad server beacons. Your ad server URLs are preserved. This is the default, and it also applies to playback configurations that have never set `BeaconingConfiguration`.

`DISABLED`  
MediaTailor doesn't include any beacons of its own, and the tracking response stays as it was before. MediaTailor publishes no `Avail.*` metrics and writes no `BEACON_RECEIVED` log entries for your client-side reporting sessions. Choose this if you don't want the extra requests from your players.

### Example configuration
<a name="beaconing-configuration-example"></a>

The following example turns on beaconing and reports on the mute, unmute, and skip player operation events:

```
{
    "Name": "my-playback-configuration",
    "BeaconingConfiguration": {
        "ClientSide": {
            "ReportingMode": "INSIGHTS",
            "AdditionalEventTypes": ["MUTE", "UNMUTE", "SKIP"]
        }
    }
}
```

The following example turns beaconing off. Omit `AdditionalEventTypes` here – sending event types with `DISABLED` is rejected.

```
{
    "Name": "my-playback-configuration",
    "BeaconingConfiguration": {
        "ClientSide": {
            "ReportingMode": "DISABLED"
        }
    }
}
```

## Metrics and log monitoring
<a name="beaconing-configuration-monitoring"></a>

### Metrics
<a name="beaconing-configuration-metrics"></a>

MediaTailor publishes the `Avail.*` metrics listed in [Tracking events that MediaTailor reports on](#beaconing-configuration-event-types). The ad progress metrics are the **same metrics** that server-side reporting publishes, and nothing tells the two apart: a count from an event that your player reported and a count from a beacon that MediaTailor sent add up in one metric. This is intentional, so that a single graph covers your ad delivery no matter which reporting mode a session uses.

All of these metrics have the `ConfigurationName` dimension, and MediaTailor also publishes them at the account level with no dimensions. For full descriptions, see [Monitoring AWS Elemental MediaTailor with Amazon CloudWatch metrics](monitoring-cloudwatch-metrics.md).

**Note**  
Because the ad progress metrics combine both sources, don't read `Avail.Impression` as a count of the beacons that MediaTailor sent. If you need per-destination delivery detail for the beacons that MediaTailor sends itself, use `Avail.Impression.Fired`, `Avail.Impression.Retried`, `Avail.Impression.Recovered`, and the matching `Avail.Complete.*` metrics instead.

### BEACON\_RECEIVED log event
<a name="beaconing-configuration-logs"></a>

Each time MediaTailor receives a tracking event from your player, it writes a `BEACON_RECEIVED` entry to your `AdDecisionServerInteractions` logs. This is the client-side counterpart of `BEACON_FIRED`, which MediaTailor writes for the beacons that it sends itself. For the full list of ADS log events, see [AdDecisionServerInteractions events](ads-log-format.md#log-types-adsinteraction).

**Note**  
You can't currently exclude `BEACON_RECEIVED` from your logs with `AdsInteractionExcludeEventTypes`. To stop receiving these entries, set `ReportingMode` to `DISABLED`.

The entry includes the following fields.


| Field | Description | 
| --- | --- | 
| beaconInfo.trackingEvent | The tracking event that your player reported, such as impression or midpoint. | 
| beaconInfo.beaconUri | The path of the MediaTailor beacon that your player requested. | 
| beaconInfo.source | How your player reported the event. For beacons that your player sends, this is client\_beacon. | 
| beaconInfo.headers | Request headers from your player, including User-Agent and X-Forwarded-For. | 
| sessionId | The playback session that reported the event. | 
| adBreakCorrelationId | Matches the event to the FILLED\_AVAIL entry for the same ad break. Not present for non-linear ads. | 
| avail.creativeUniqueId | The unique identifier of the creative that your player was playing. | 
| avail.creativeUri | The location of the creative that your player was playing. For a non-linear ad, this is the resource from your ad server's VAST response, because MediaTailor doesn't transcode overlays. | 

The following CloudWatch Logs Insights query returns the tracking events that your players reported, with the reporting device's user agent and IP address:

```
fields @timestamp, beaconInfo.trackingEvent, beaconInfo.source, beaconInfo.headers.0.value as @userAgent, beaconInfo.headers.1.value as @xForwardedFor, sessionId, requestId
| filter eventType = "BEACON_RECEIVED"
| sort @timestamp asc
```

For more query examples, see [Querying the ADS logs](querying-the-ads-logs.md).

## Limitations
<a name="beaconing-configuration-limitations"></a>
+ **Non-linear ads report a narrower set of events.** MediaTailor includes its beacons in non-linear ad breaks, such as pause and display overlays, as well as in linear ad breaks. For non-linear ads, though, MediaTailor only adds an event that your ad server's VAST response omitted when that event is `impression`, `firstQuartile`, `midpoint`, `thirdQuartile`, or `complete`. It never adds a missing `start`, because a display overlay has no playback start that MediaTailor can observe. If your VAST response does carry `start` on a non-linear ad, MediaTailor vends its beacon for it as usual.
+ **Reporting depends on your player.** MediaTailor can only report an event if your player sends the beacon for it. A player that ignores tracking events it doesn't recognize, or that doesn't send an event missing from your ad server's VAST response, produces no metric for that event. Read these metrics as a measure of what your players reported, not as a guarantee of what the viewer saw.
+ **Extra player requests.** Each event that MediaTailor reports on adds one request from your player. Set `ReportingMode` to `DISABLED` if that traffic is a concern for your workflow.

## See also
<a name="beaconing-configuration-see-also"></a>
+ [Client-side ad tracking](ad-reporting-client-side.md) – How client-side reporting works, including the tracking response that MediaTailor vends its beacons in.
+ [Monitoring AWS Elemental MediaTailor with Amazon CloudWatch metrics](monitoring-cloudwatch-metrics.md) – Full reference for all MediaTailor CloudWatch metrics, including the `Avail.*` metrics described here.
+ [AWS Elemental MediaTailor ADS logs description and event types](ads-log-format.md) – The `AdDecisionServerInteractions` log format and the full list of event types.
+ [PutPlaybackConfiguration API Reference](https://docs.aws.amazon.com/mediatailor/latest/apireference/API_PutPlaybackConfiguration.html) – Full parameter reference for configuring `BeaconingConfiguration`.