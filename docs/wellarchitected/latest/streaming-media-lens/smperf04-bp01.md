

# SMPERF04-BP01 Collect and analyze real user logs and metrics
<a name="smperf04-bp01"></a>

Collect client-side telemetry alongside content delivery network (CDN)

real-time logs to measure what viewers actually experience, not just what the infrastructure delivers.

**Desired outcome:**
+ You have client-side telemetry through Common Media Client Data (CMCD) combined with CDN real-time logs so viewer experience is measured, not inferred.
+ Your metrics are broken down by geography, device, internet service provider (ISP), and content title, not just averaged across all sessions.
+ Your alerts correlate client-side issues (rebuffers, startup spikes) with infrastructure events (origin errors, cache misses) automatically.

**Common anti-patterns:**
+ Relying solely on server-side CDN logs to infer viewer experience, missing rebuffers that happen inside the player.
+ Collecting client telemetry but storing it in a general-purpose log system that can't correlate with CDN real-time logs.
+ Skipping client-side monitoring because server-side dashboards look healthy.

**Benefits of establishing this best practice:**
+ Visibility into rebuffers, startup time, and quality switches that server logs can't show
+ Ability to trace a viewer complaint back to the specific cache miss or origin error that caused it
+ Earlier detection of quality degradation because client metrics surface before support tickets
+ Segmented analysis by geography, device, and ISP rather than fleet-wide averages
+ Faster incident response when client-side and infrastructure alerts correlate automatically

**Level of risk exposed if this best practice is not established:** High

## Implementation guidance
<a name="implementation-guidance"></a>

Streaming observability requires both server-side and client-side data. Server-side logs tell you what the infrastructure delivered. Client metrics from CMCD tell you what the viewer experienced. Rebuffers happen inside the player, often after the last successful HTTP request, so they are invisible in server logs until the client reports them. A shared session ID is what connects the two data sources. Without it, a rebuffer can't be traced back to the cache miss or origin error that caused it. CMCD also has a timing property that affects how you use it for alerting. It piggybacks on the next media request, so the telemetry arrives after the event. A rebuffer shows up in the log for the segment that finished after recovery, not during the stall. This is fine for detection and post-mortem. It isn't a real-time alerting channel. Live incident response and service level agreement (SLA) alerts need a separate telemetry path, not CMCD alone.

### Implementation steps
<a name="implementation-steps"></a>

1. **Enable Amazon CloudFront real-time logs with CMCD parameters:** Configure CloudFront to capture CMCD data in real-time log streams.

1. **Create correlation analysis between client and infrastructure metrics:** Establish mechanisms to link client-side and server-side data.

1. **Integrate CMCD in media players:** Use CMCD-compatible players (HLS.js, Video.js), configure players to send CMCD parameters through HTTP headers or query strings, and assign unique session IDs across viewing sessions.

1. **Deploy log processing pipeline:** Set up data ingestion and processing for real-time log analysis.

1. **Set up time-series storage:** Configure Amazon Timestream or equivalent for metrics retention.

1. **Create monitoring dashboards:** Set alerts for high rebuffering rates and time to first byte (TTFB) spikes, configure geographic and device-specific monitoring, and enable automated correlation between client issues and infrastructure events.

## Resources
<a name="resources"></a>

**Related best practices**
+ [SMPERF03-BP01 Use a content delivery network and monitor your cache-hit-ratio](smperf03-bp01.html)

**Related documents**
+ [Improving Video Observability with CMCD and CloudFront blog
+ [Cloudfront CMCD Realtime Dashboard

**Related services**
+ [Amazon Kinesis](https://aws.amazon.com/kinesis/)
+ [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/)
+ [AWS Lambda](https://aws.amazon.com/lambda/)
+ [Amazon Timestream](https://aws.amazon.com/timestream/)