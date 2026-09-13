

# How Yield Optimization works
<a name="yield-optimization-how-it-works"></a>

This page explains the internal mechanics of Yield Optimization: when it triggers, how timing works, and how it interacts with other MediaTailor features.

## When Yield Optimization triggers
<a name="yield-optimization-how-it-works-triggers"></a>

MediaTailor evaluates three conditions before making a bid request to APS. All three must be true:

1. **Yield Optimization is configured.** The playback configuration has a `YieldOptimizationConfiguration` with a valid Publisher ID, region, and template.

1. **Sufficient unfilled duration.** After the primary ADS response, the remaining unfilled time in the ad break exceeds the configured `MinimumUnfilledDuration` threshold.

1. **Sufficient personalization time remaining.** Enough time remains in the personalization budget to make the APS request and process the response.

If any condition is not met, Yield Optimization is skipped and MediaTailor proceeds with only the primary ADS ads.

## How underfill is calculated
<a name="yield-optimization-how-it-works-underfill"></a>

1. MediaTailor reads the total ad break duration from the SCTE signal.

1. MediaTailor sums the durations of all ads returned by the primary ADS (from VAST durations).

1. The unfilled duration equals the total break duration minus the sum of primary ad durations.

1. If unfilled duration is greater than or equal to `MinimumUnfilledDuration`, Yield Optimization proceeds.

**Example:** A 60-second ad break where the primary ADS returns 30 seconds of ads leaves 30 seconds unfilled. If `MinimumUnfilledDuration` is set to 15, Yield Optimization triggers and requests ads for the remaining 30 seconds.

## Personalization time management
<a name="yield-optimization-how-it-works-timing"></a>

MediaTailor operates within a strict timing budget for ad personalization. Yield Optimization uses the *remaining* personalization time after the primary ADS request completes.

**Key SDC (Safe Dynamic Configuration) flags that affect timing:**


| Flag | Description | 
| --- | --- | 
| maximumLivePersonalizationLatencyMs | Maximum total time for all ad personalization (primary ADS plus YO) for live content. | 
| adsRequestTimeOutMilliseconds | Timeout for the primary ADS request. | 

**Timing behavior:**
+ If insufficient time remains to start the APS request, YO is skipped entirely (emits the `SkipPersonalizationTimeoutExceeded` metric).
+ If the APS request starts but does not complete in time, it times out (emits the `Timeouts` metric).
+ MediaTailor enforces tight timeouts on both the APS HTTP request and VAST processing to ensure personalization completes within limits.

## Fail-open behavior
<a name="yield-optimization-how-it-works-fail-open"></a>

Yield Optimization always fails open. If any of the following occur, MediaTailor proceeds with only the primary ADS ads:
+ APS returns an error (4xx, 5xx).
+ The request times out.
+ The bid response contains no valid ads.
+ VAST parsing fails for all returned bids.

The viewer's playback experience is never interrupted by a Yield Optimization failure.

## APS response codes
<a name="yield-optimization-how-it-works-response-codes"></a>


| Code | Meaning | 
| --- | --- | 
| 200 | Successful bid response with ads. | 
| 204 | No bid. The request is valid but no bids were available. | 
| 400 | Bad request (invalid JSON or missing required fields). | 
| 500 | APS server error. | 
| 503 | APS overloaded (back-pressure signal). | 
| 429 | APS throttling. APS has manually started to throttle requests. | 

## Interaction with other MediaTailor features
<a name="yield-optimization-how-it-works-interactions"></a>


| Feature | Interaction | 
| --- | --- | 
| Ad Decision Server Configuration (ADSC) | No interaction. ADSC controls the primary ADS request. YO is independent. | 
| Prefetch | Not supported with YO in the current release. | 
| Overlay ads | Not supported with YO in the current release. | 

## Next steps
<a name="yield-optimization-how-it-works-next-steps"></a>
+ To learn how the bid request is built from your template, see [Bid construction and templating](yield-optimization-bid-construction.md).
+ For the complete field reference, see [ORTB field reference](yield-optimization-ortb-reference.md).