# Troubleshooting MediaTailor event flow

issues

Understanding AWS Elemental MediaTailor event flow provides a powerful foundation for troubleshooting
ad insertion issues. By analyzing the sequence, timing, and patterns of events, you can
quickly identify where problems occur and implement targeted solutions.

This section provides practical guidance for using event flow analysis to diagnose
issues. For understanding the basic event flow concepts, see [Ad insertion event
flow](mediatailor-event-flow.md "mediatailor-event-flow.md").

## Identifying incomplete event

flows

Incomplete event flows occur when the expected sequence of events stops before
reaching successful manifest personalization (the process of MediaTailor inserting
personalized ad information into the manifest). Identifying where the flow breaks
helps pinpoint the root cause of ad insertion failures.

### Common incomplete flow

patterns

Different failure points in the event flow indicate specific types of
problems, such as the following.

- **Flow stops after ad opportunity
  detection:** Indicates issues with ad markers or the
  manifest itself that prevent MediaTailor from making an ADS request. ADS
  connectivity, configuration, or timeout problems would occur after the
  ADS request is made.
- **Flow stops after ADS request:**
  Suggests ADS response issues, VAST parsing problems, creative processing
  failures, ADS timeouts, connectivity errors, or configuration issues
  such as invalid ADS URLs that are only discovered when the request is
  made.
- **Missing tracking beacon:** Might
  indicate tracking configuration issues, server-side reporting problems,
  or client-side implementation gaps.

### CloudWatch queries for

incomplete flow analysis

Use these Amazon CloudWatch Logs Insights queries to identify incomplete event flows. Run
these queries against the appropriate log groups based on the type of analysis
needed.

**Log group selection:**

- **MediaTailor/AdDecisionServerInteractions** - Use for
  queries analyzing ad decision server interactions, ad opportunities, and
  ADS-related failures.
- **MediaTailor/TranscodeService** - Use
  for analyzing issues where ads were not inserted due to transcoding
  problems, creative processing failures, or other non-ADS related
  issues.

###### Example identify ad opportunities without successful manifest

personalization

**Log group:**
MediaTailor/AdDecisionServerInteractions

The following query identifies ad opportunities that did not result in
successful manifest personalization:

````
fields @timestamp, eventType, avail.availId, sessionId
| filter eventType = "AD_MARKER_FOUND"
| stats count() as total_opportunities by avail.availId
| join ( fields @timestamp, eventType, avail.availId
| filter eventType = "FILLED_AVAIL"
| stats count() as successful_fills by avail.availId ) on avail.availId
| where ispresent(total_opportunities) and not ispresent(successful_fills)
| sort total_opportunities desc ``` ###### Example analyze event flow completion rates **Log group:** MediaTailor/AdDecisionServerInteractions The following query analyzes completion rates across different event types: ``` fields @timestamp, eventType, avail.availId
| filter eventType in ["AD_MARKER_FOUND", "MAKING_ADS_REQUEST", "VAST_RESPONSE", "FILLED_AVAIL", "BEACON_FIRED"]
| stats count() by eventType, avail.availId
| sort avail.availId, eventType ``` ###### Example find sessions with missing beacon events **Log group:** MediaTailor/AdDecisionServerInteractions The following query identifies sessions that have filled avails but no corresponding beacon events: ``` fields @timestamp, eventType, sessionId, avail.availId
| filter eventType = "FILLED_AVAIL"
| stats count() as filled_avails by sessionId
| join ( fields @timestamp, eventType, sessionId
| filter eventType = "BEACON_FIRED"
| stats count() as beacon_events by sessionId ) on sessionId
| where filled_avails > 0 and (not ispresent(beacon_events) or beacon_events = 0)
| sort filled_avails desc ``` ###### Example identify transcoding-related ad insertion failures **Log group:** MediaTailor/TranscodeService The following query identifies transcoding issues that prevent successful ad insertion: ``` fields @timestamp, eventType, sessionId, requestId
| filter eventType in ["TRANSCODE_IN_PROGRESS", "INTERNAL_ERROR", "MISSING_VARIANTS", "PROFILE_NOT_FOUND"]
| stats count() as transcode_issues by eventType, sessionId
| sort transcode_issues desc ``` ## Analyzing event timing issues Event timing analysis helps identify performance bottlenecks and optimize ad insertion workflows. Unusual timing patterns often indicate underlying issues that affect viewer experience. ### Performance timing thresholds Use these timing thresholds to identify potential performance issues. <br>• **Total flow duration more than 5 seconds:** Can impact viewer experience and can indicate ADS performance issues, origin server problems (such as manifest retrieval timeouts), or internal MediaTailor issues including infrastructure problems with NAT Gateway, DynamoDB, EC2, or other system components. <br>• **ADS response time more than 2 seconds:** Suggests ADS performance problems or network latency issues. <br>• **Manifest personalization more than 1 second:** Can indicate creative processing delays, origin server issues (such as manifest retrieval timeouts), or internal MediaTailor system problems including infrastructure constraints with NAT Gateway, DynamoDB, EC2, or other components. ### Timing analysis queries Use these queries to analyze event timing patterns. ###### Example measure total event flow duration The following query measures the total duration of event flows and identifies those exceeding 5 seconds: ``` fields @timestamp, eventType, avail.availId
| filter avail.availId = "your-avail-id"
| filter eventType in ["AD_MARKER_FOUND", "FILLED_AVAIL"]
| sort @timestamp asc
| stats min(@timestamp) as start_time, max(@timestamp) as end_time by avail.availId
| eval duration_seconds = (end_time - start_time) / 1000
| where duration_seconds > 5 ``` ###### Example analyze ADS response timing The following query analyzes ADS response times and identifies those exceeding 2 seconds: ``` fields @timestamp, eventType, avail.availId
| filter avail.availId = "your-avail-id"
| filter eventType in ["MAKING_ADS_REQUEST", "VAST_RESPONSE"]
| sort @timestamp asc
| stats min(@timestamp) as request_time, max(@timestamp) as response_time by avail.availId
| eval ads_response_seconds = (response_time - request_time) / 1000
| where ads_response_seconds > 2 ``` ###### Example identify slow manifest personalization The following query identifies manifest personalization processes that take longer than 1 second: ``` fields @timestamp, eventType, avail.availId
| filter avail.availId = "your-avail-id"
| filter eventType in ["VAST_RESPONSE", "FILLED_AVAIL"]
| sort @timestamp asc
| stats min(@timestamp) as response_time, max(@timestamp) as filled_time by avail.availId
| eval personalization_seconds = (filled_time - response_time) / 1000
| where personalization_seconds > 1 ``` ## Common event flow problems and solutions This section provides solutions for frequently encountered event flow issues, organized by problem type and symptoms. ### Ad decision server request failures **Symptoms:** Event flow stops after ad opportunity detection. No ADS request events logged. **Common causes and solutions** <br>• **ADS URL configuration errors:** Verify the ADS URL in your playback configuration is correct and accessible. In the ads interaction log, you will see an ADS request event (`MAKING_ADS_REQUEST`) but no corresponding VAST response, often accompanied by an `ERROR_UNKNOWN` or similar error event. <br>• **Network connectivity issues:** Check network connectivity between MediaTailor and your ADS, including firewall rules and DNS resolution. <br>• **SSL/TLS certificate problems:** Ensure your ADS uses valid SSL certificates from a trusted certificate authority. For Google Ad Manager specifically, you might need to contact [AWS Support](https://aws.amazon.com/premiumsupport/ "https://aws.amazon.com/premiumsupport/") to enable a configuration flag that accepts Google's SSL certificates. **Diagnostic query** The following query helps diagnose ADS request failures by tracking the event sequence: ``` fields @timestamp, eventType, sessionId
| filter sessionId = "your-session-id"
| filter eventType in ["AD_MARKER_FOUND", "MAKING_ADS_REQUEST", "ERROR_ADS_IO", "ERROR_UNKNOWN_HOST"]
| sort @timestamp asc ``` ### Ad decision server response failures **Symptoms:** ADS requests succeed but MediaTailor doesn't receive a response, or parsing errors occur. **Common causes and solutions** <br>• **Invalid VAST format:** Validate your ADS VAST responses against VAST specification standards. <br>• **ADS timeout issues:** Increase ADS timeout settings or optimize ADS response time. <br>• **Empty ad inventory:** Check ad inventory availability and targeting criteria in your ADS configuration. **Diagnostic query** The following query helps diagnose ADS response failures by examining request and response events: ``` fields @timestamp, eventType, sessionId
| filter sessionId = "your-session-id"
| filter eventType in ["MAKING_ADS_REQUEST", "VAST_RESPONSE", "EMPTY_VAST_RESPONSE", "ERROR_ADS_RESPONSE_PARSE", "ERROR_ADS_TIMEOUT"]
| sort @timestamp asc ``` ### Manifest personalization failures **Symptoms:** VAST responses received but manifest personalization fails or ads are skipped. **Common causes and solutions:** <br>• **Creative transcoding issues:** Check if the ad is a `NEW_CREATIVE`, which requires transcoding prior to insertion. You can also check for transcoding errors by examining the MediaTailor/TranscodeService log for error events such as `INTERNAL_ERROR`, `MISSING_VARIANTS,` or `PROFILE_NOT_FOUND`. <br>• **Duration mismatch problems:** Verify ad durations fit within available ad break durations. <br>• **Personalization threshold issues:** Review personalization threshold settings in your playback configuration. **Diagnostic query** The following query helps diagnose manifest personalization failures by examining VAST responses and filled avails: ``` fields @timestamp, eventType, sessionId, skippedAds
| filter sessionId = "your-session-id"
| filter eventType in ["VAST_RESPONSE", "FILLED_AVAIL", "WARNING_NO_ADVERTISEMENTS"]
| sort @timestamp asc ``` **Query for skipped ad reasons** The following query provides detailed information about why ads were skipped: ``` fields @timestamp, eventType, sessionId, skippedAds.reason, skippedAds.creativeUniqueId
| filter sessionId = "your-session-id"
| filter eventType = "WARNING_NO_ADVERTISEMENTS" or ispresent(skippedAds)
| sort @timestamp asc ``` **Query for skipped ad reasons and creative unique IDs** The following query provides detailed skipped ad information including reasons and creative unique IDs for the first two ads in each avail: ``` fields @timestamp, eventType
| filter sessionId = "your-session-id"
| filter eventType = "FILLED_AVAIL"
| fields avail.skippedAds.0.vastDuration as SkippedDur_Ad0, avail.skippedAds.0.skippedReason as Ad0_SkipReason, avail.skippedAds.0.creativeUniqueId as SkippedCreative0_UID
| fields avail.skippedAds.1.vastDuration as SkippedDur_Ad1, avail.skippedAds.1.skippedReason as Ad1_SkipReason, avail.skippedAds.1.creativeUniqueId as SkippedCreative1_UID
| sort @timestamp desc ``` ### Tracking beacon failures **Symptoms:** Successful manifest personalization but missing or failed tracking beacons. **Common causes and solutions** <br>• **Client-side implementation issues:** Most tracking beacon issues stem from client-side implementation problems, such as not polling tracking URLs frequently enough for client-side tracking, or player-specific beacon firing logic issues. <br>• **Tracking URL accessibility issues:** Verify that tracking URLs in VAST responses are accessible and return appropriate responses. Issues can occur when URLs are not reachable or when MediaTailor encounters internal issues preventing successful tracking response delivery. <br>• **Player segment request issues:** Apparent tracking beacon failures can occur when the client player doesn't actually request any segments. This results in no beacons being sent, which appears as a tracking failure but is actually a player implementation issue rather than a beacon problem. **Diagnostic query** The following query helps diagnose tracking beacon failures by examining filled avails and beacon events: ``` fields @timestamp, eventType, sessionId
| filter sessionId = "your-session-id"
| filter eventType in ["FILLED_AVAIL", "BEACON_FIRED", "ERROR_FIRING_BEACON_FAILED"]
| sort @timestamp asc ``` ## Event flow monitoring best practices Implement these monitoring practices to proactively identify and resolve event flow issues: ### Setting up CloudWatch alarms Create Amazon CloudWatch alarms to monitor key event flow metrics. <br>• **Flow completion rate alarm:** Alert when the ratio of successful manifest personalization to ad opportunities drops below acceptable thresholds. <br>• **ADS response time alarm:** Monitor average ADS response times and alert when they exceed performance thresholds. <br>• **Error rate alarm:** Track error event frequencies and alert on unusual spikes in specific error types. ### Regular monitoring queries Run these queries regularly to maintain visibility into event flow health: ###### Example daily event flow success rate The following query provides a daily overview of event flow success rates by event type: ``` fields @timestamp, eventType
| filter @timestamp > datefloor(@timestamp, 1d)
| stats count() as total_events by eventType
| sort total_events desc ``` ###### Example hourly error rate trending The following query tracks error rates by hour to identify trending issues: ``` fields @timestamp, eventType
| filter eventType like /ERROR_/
| stats count() as error_count by datefloor(@timestamp, 1h) as hour
| sort hour desc ``` ### Performance optimization guidance Use event flow analysis to optimize ad insertion performance. <br>• **ADS optimization:** Work with your ADS provider to optimize response times and reduce latency. <br>• **Creative preparation:** Pre-transcode ad creatives to match your content profiles and reduce processing delays. <br>• **Configuration tuning:** Adjust timeout settings, personalization thresholds, and other configuration parameters based on event flow analysis. ## Additional troubleshooting resources For additional troubleshooting guidance beyond event flow analysis: <br>• For detailed log format information and technical specifications, see [Viewing logs](monitoring-through-logs.md "monitoring-through-logs.md"). <br>• For comprehensive troubleshooting of common ad insertion issues, see [Troubleshooting common issues](monitoring-and-troubleshooting.md#troubleshooting-common-issues "monitoring-and-troubleshooting.md#troubleshooting-common-issues"). <br>• For monitoring and alerting setup guidance, see [Monitoring AWS Elemental MediaTailor with Amazon CloudWatch metrics](monitoring-cloudwatch-metrics.md "monitoring-cloudwatch-metrics.md"). <br>• For debug logging procedures, see [Generating debug logs](debug-log-mode.md "debug-log-mode.md").
````
