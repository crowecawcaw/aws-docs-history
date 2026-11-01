

# Troubleshooting and monitoring
<a name="yield-optimization-troubleshooting"></a>

This page helps you monitor Yield Optimization performance, diagnose common issues, and validate that your configuration is working correctly.

## Metrics
<a name="yield-optimization-troubleshooting-metrics"></a>

MediaTailor publishes the following CloudWatch metrics for Yield Optimization. All metrics are emitted with a `configurationName` dimension unless noted otherwise.

### Bid request metrics
<a name="yield-optimization-troubleshooting-metrics-bidrequest"></a>


| Metric | Description | 
| --- | --- | 
| YieldOptimization.BidRequest | Emitted as 1 when a bid request opportunity is identified. | 
| YieldOptimization.BidResponse | Emitted as 1 when a successful bid response is received. | 
| YieldOptimization.BidDuration | The break duration (seconds) requested in the bid, calculated from avail duration minus primary ad duration. | 
| YieldOptimization.Latency | Round-trip latency to Amazon Publisher Services (APS) in milliseconds. | 
| YieldOptimization.NoBid | Emitted as 1 when APS returns HTTP 204 (no matching demand). The request itself was valid. | 
| YieldOptimization.BidRequestThrottled | Emitted as 1 when APS returns HTTP 429 (throttled). APS is applying back-pressure. Back off before retrying. | 

### Ad insertion metrics
<a name="yield-optimization-troubleshooting-metrics-adinsertion"></a>


| Metric | Description | 
| --- | --- | 
| YieldOptimization.AdsInserted | Number of YO ads inserted into the avail. | 
| YieldOptimization.AdsReturned | Number of ads returned in the BidResponse (before filtering). Only emitted when greater than 0. | 
| YieldOptimization.FilledDuration | Duration (ms) filled by YO ads. | 
| YieldOptimization.UnfilledDuration | Duration (ms) sent to APS in the bid request (opportunity gap). | 
| YieldOptimization.FillRate | Per-avail fill rate: transcoded YO duration divided by the pre-YO unfilled duration. The numerator is transcoded and the denominator is VAST-based (neither subtracts bumper), so the value can exceed 1.0. | 

### Revenue and pricing metrics
<a name="yield-optimization-troubleshooting-metrics-revenue"></a>


| Metric | Description | 
| --- | --- | 
| YieldOptimization.Revenue | Total revenue for the customer, sourced from the price attribute of the oRTB bid response. Sum of price across inserted ads. | 
| YieldOptimization.IndicativeBidRevenue | Summed per-impression indicative value of all returned bids (bid price per impression, not per insertion). Don't use this metric in your new dashboards. This metric is deprecated, and AWS might remove it in a future release. Use YieldOptimization.Revenue instead. | 
| YieldOptimization.BidPriceAdsInserted | The CPM price of each ad inserted by Yield Optimization, in the currency from the bid response cur attribute. | 
| YieldOptimization.BidPriceAdsReturned | The CPM price of each bid returned in the bid response (before filtering to insertions), in the currency from the bid response cur attribute. | 

### Error and skip metrics
<a name="yield-optimization-troubleshooting-metrics-error"></a>


| Metric | Description | 
| --- | --- | 
| YieldOptimization.Errors | Emitted as 1 for connection errors, response processing errors, or unexpected exceptions. Also emitted as 0 on success (use Sum, not SampleCount). | 
| YieldOptimization.Timeouts | Emitted as 1 when the APS request times out. Also emitted as 0 on success (use Sum, not SampleCount). | 
| YieldOptimization.BidRequestConfigurationError | Emitted as 1 when the template or bid construction fails (missing fields, invalid JSON). | 
| YieldOptimization.SkipMinUnfilledDurationNotExceeded | Emitted as 1 when YO was skipped because unfilled duration was below the threshold. | 
| YieldOptimization.SkipPersonalizationTimeoutExceeded | Emitted as 1 when YO was skipped because insufficient personalization time remained. | 

**Important**  
`YieldOptimization.Errors` and `YieldOptimization.Timeouts` are emitted as 0 on every successful request. Use **Sum** (not SampleCount) in CloudWatch to get the actual error or timeout count. `NoBid` and `BidRequestThrottled` are NOT counted in `Errors`. They are separate signals for legitimate no-demand and back-pressure conditions.

## Log events
<a name="yield-optimization-troubleshooting-log-events"></a>

Yield Optimization generates events in the `MediaTailor/AdDecisionServerInteractions` log group:


| Event type | Description | 
| --- | --- | 
| RAW\_BID\_REQUEST | The complete OpenRTB bid request JSON sent to APS. Use this to verify template interpolation. | 
| RAW\_BID\_RESPONSE | The raw OpenRTB bid response from APS, including bid pricing and VAST XML. | 
| FILLED\_AVAIL | The complete avail with all ads. YO ads have fillMode: "YIELD\_OPTIMIZATION" and include bidId, bidPrice, currency, impressionId, and seatId. | 
| EMPTY\_BID\_RESPONSE | APS returned no bids (HTTP 204). APS found no matching demand, even though the request was valid. | 
| ERROR\_INVALID\_BID\_REQUEST | APS rejected the bid request (HTTP 4xx other than 429). The additionalInfo field contains the APS error response. | 
| ERROR\_BID\_REQUEST\_THROTTLED | APS throttled the bid request (HTTP 429). | 
| ERROR\_BID\_RESPONSE\_SERVER\_ERROR | APS returned a server error (HTTP 5xx). The additionalInfo field contains the APS error response. | 
| ERROR\_BID\_RESPONSE\_PARSE | APS returned an unexpected HTTP status, or MediaTailor could not process the bid response. | 

## Example CloudWatch Insights queries
<a name="yield-optimization-troubleshooting-insights"></a>

### Check for YO errors
<a name="yield-optimization-troubleshooting-insights-errors"></a>

```
fields @timestamp, sessionId, eventType, additionalInfo
| filter eventType in ['ERROR_INVALID_BID_REQUEST',
    'ERROR_BID_REQUEST_THROTTLED', 'ERROR_BID_RESPONSE_SERVER_ERROR',
    'ERROR_BID_RESPONSE_PARSE']
| sort @timestamp desc
| limit 100
```

**Log group:** `MediaTailor/AdDecisionServerInteractions`

### Count bid requests vs responses
<a name="yield-optimization-troubleshooting-insights-count"></a>

```
fields @timestamp, sessionId, eventType
| filter eventType = 'RAW_BID_REQUEST' or eventType = 'RAW_BID_RESPONSE'
| stats count(*) by eventType
```

**Log group:** `MediaTailor/AdDecisionServerInteractions`

### Find YO ads in filled avails
<a name="yield-optimization-troubleshooting-insights-filled"></a>

Each `FILLED_AVAIL` event contains a `creativeAds` array. YO ads within that array carry `fillMode: "YIELD_OPTIMIZATION"` and additional bid metadata: `bidId`, `impressionId`, `bidPrice`, `seatId`, and `currency`. Use this to see which avails were filled by YO, how many YO ads were inserted per avail, and the revenue attribution per bid.

```
fields @timestamp, sessionId, avail.availId, avail.numAds, avail.fillRate, avail.filledDuration
| filter eventType = 'FILLED_AVAIL'
  and @message like /YIELD_OPTIMIZATION/
| sort @timestamp desc
| limit 50
```

To pull the individual YO ad entries (bid ids and prices) for a specific session:

```
fields @timestamp, sessionId, avail.availId, avail.creativeAds
| filter eventType = 'FILLED_AVAIL'
  and sessionId = 'YOUR_SESSION_ID'
| sort @timestamp desc
| limit 20
```

Filter the resulting `creativeAds` array client-side for entries where `fillMode == "YIELD_OPTIMIZATION"`.

**Log group:** `MediaTailor/AdDecisionServerInteractions`

### Check for unresolved template variables
<a name="yield-optimization-troubleshooting-insights-unresolved"></a>

```
fields @timestamp, sessionId, @message
| filter eventType = 'RAW_BID_REQUEST'
  and @message like /\{[A-Z_]+\}/
| sort @timestamp desc
| limit 20
```

**Log group:** `MediaTailor/AdDecisionServerInteractions`

## Calculating yield lift
<a name="yield-optimization-troubleshooting-yield-lift"></a>

To measure the revenue impact of Yield Optimization, create a CloudWatch dashboard with:

1. **Incremental fill rate:** `Sum(YieldOptimization.AdsInserted) / Sum(YieldOptimization.BidRequest)` shows what percentage of YO opportunities result in inserted ads. Alternatively, use `Average(YieldOptimization.FillRate)` for the per-avail native metric.

1. **Revenue per hour:** `Sum(YieldOptimization.Revenue)` over time shows total revenue from YO. `Average(YieldOptimization.BidPriceAdsInserted)` gives the average CPM of inserted YO ads.

1. **Duration filled:** `Sum(YieldOptimization.FilledDuration)` against `Sum(YieldOptimization.BidDuration)` shows how much of the requested duration was actually filled.

## Common issues
<a name="yield-optimization-troubleshooting-common-issues"></a>

### Yield Optimization not triggering
<a name="yield-optimization-troubleshooting-not-triggering"></a>


| Symptom | Check | Resolution | 
| --- | --- | --- | 
| No YO metrics at all | Is YO configured on the playback config? | Enable YO in the console or API. | 
| SkipMinUnfilledDurationNotExceeded emitting | Primary ADS is filling most of the break | Lower MinimumUnfilledDuration or accept that primary fill is sufficient. | 
| SkipPersonalizationTimeoutExceeded emitting | Primary ADS is too slow, leaving no time for YO | Reduce primary ADS latency so that more personalization time remains for YO. | 

### Bid requests failing
<a name="yield-optimization-troubleshooting-bidrequests-failing"></a>


| Symptom | Check | Resolution | 
| --- | --- | --- | 
| BidRequestConfigurationError metric | Template has missing or empty mandatory fields | Verify that every mandatory field in your template (for example, app.bundle) resolves to a non-empty value, and that the player sends the player parameters that the template references. | 
| HTTP 204 from APS | YieldOptimization.NoBid incrementing | APS returned no-bid. Not an error. Inspect RAW\_BID\_REQUEST for placeholder values ({UPPER\_CASE} patterns), verify bundle and storeurl are real, lower bidfloor. | 
| HTTP 429 from APS | YieldOptimization.BidRequestThrottled incrementing | APS is throttling. Back off request rate. If persistent, contact APS support to raise TPS limits. | 
| HTTP 400 from APS | Invalid request JSON | Check the APS error message in the additionalInfo field of the ERROR\_INVALID\_BID\_REQUEST event. Verify JSON structure matches OpenRTB spec. | 
| HTTP 500/503 from APS | APS server error or overload | Transient issue. Check the APS error message in the additionalInfo field of the ERROR\_BID\_RESPONSE\_SERVER\_ERROR event, and monitor YieldOptimization.Errors. If persistent, contact APS support. | 

### Ads returned but not inserted
<a name="yield-optimization-troubleshooting-not-inserted"></a>


| Symptom | Check | Resolution | 
| --- | --- | --- | 
| AdsReturned > 0 but AdsInserted = 0 | Ads filtered during insertion | Check FILLED\_AVAIL logs for skip reasons: duplicate creatives, leftover threshold exceeded, or ad variant not found (transcoding not complete). | 

## APS error codes reference
<a name="yield-optimization-troubleshooting-error-codes"></a>


| Code | Meaning | Common causes | 
| --- | --- | --- | 
| 200 | Success with bids | Working correctly. | 
| 204 | No bid | The request is valid but no bids were available. This does not indicate an error in your template. | 
| 400 | Bad request | Invalid JSON, missing required fields per OpenRTB spec. | 
| 500 | Server error | APS internal issue, service throttled, timeout. | 
| 503 | Service overloaded | APS back-pressure. Do not retry aggressively. | 
| 429 | Throttled | APS has manually started to throttle requests. Contact APS support if persistent. | 