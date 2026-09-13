

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
| YieldOptimization.Latency | Round-trip latency to APS in milliseconds. | 
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
| YieldOptimization.IndicativeBidRevenue | Summed per-impression indicative value of all RETURNED bids (bid price per impression, not per insertion). Dual-emitted alongside Revenue during a deprecation window and will be removed once dashboards cut over. Use Revenue for new dashboards. | 
| YieldOptimization.BidPriceAdsInserted | The CPM price of each ad inserted by Yield Optimization. Dimensioned by the bid response cur (currency) attribute. Not emitted per-customer, so this is account-wide. | 
| YieldOptimization.BidPriceAdsReturned | The CPM price of each bid returned in the BidResponse (before filtering to insertions). Dimensioned by cur. Not emitted per-customer, so this is account-wide. | 

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

Yield Optimization generates events in the `MidasMMSService/ads_interaction_log` log group:


| Event type | Description | 
| --- | --- | 
| RAW\_BID\_REQUEST | The complete OpenRTB bid request JSON sent to APS. Use this to verify template interpolation. | 
| RAW\_BID\_RESPONSE | The raw OpenRTB bid response from APS, including bid pricing and VAST XML. | 
| FILLED\_AVAIL | The complete avail with all ads. YO ads have fillMode: "YIELD\_OPTIMIZATION" and include bidId, bidPrice, currency, impressionId, and seatId. | 

Error events are emitted in `MidasMMSService/application.log` with loggers like `YieldOptimizationSupport`, `OrtbBidRequestBuilder`, `HttpOrtbRequestSubmitter`, and `OrtbResponseProcessor`.

## Example CloudWatch Insights queries
<a name="yield-optimization-troubleshooting-insights"></a>

### Check for YO errors
<a name="yield-optimization-troubleshooting-insights-errors"></a>

```
fields @timestamp, message.sessionId, message.message, log.logger, log.level
| filter message.awsAccountId = 'YOUR_ACCOUNT_ID'
  and (log.level = 'ERROR' or log.level = 'WARN')
  and (log.logger like /YieldOptimization/
    or log.logger like /OrtbResponseProcessor/
    or log.logger like /HttpOrtbRequestSubmitter/
    or log.logger like /OrtbBidRequestBuilder/)
| sort @timestamp desc
| limit 100
```

**Log group:** `MidasMMSService/application.log`

### Count bid requests vs responses
<a name="yield-optimization-troubleshooting-insights-count"></a>

```
fields @timestamp, sessionId, eventType
| filter awsAccountId = 'YOUR_ACCOUNT_ID'
  and (eventType = 'RAW_BID_REQUEST' or eventType = 'RAW_BID_RESPONSE')
| stats count(*) by eventType
```

**Log group:** `MidasMMSService/ads_interaction_log`

### Find YO ads in filled avails
<a name="yield-optimization-troubleshooting-insights-filled"></a>

Each `FILLED_AVAIL` event contains a `creativeAds` array. YO ads within that array carry `fillMode: "YIELD_OPTIMIZATION"` and additional bid metadata: `bidId`, `impressionId`, `bidPrice`, `seatId`, and `currency`. Use this to see which avails were filled by YO, how many YO ads were inserted per avail, and the revenue attribution per bid.

```
fields @timestamp, sessionId, avail.availId, avail.numAds, avail.fillRate, avail.filledDuration
| filter awsAccountId = 'YOUR_ACCOUNT_ID'
  and eventType = 'FILLED_AVAIL'
  and @message like /YIELD_OPTIMIZATION/
| sort @timestamp desc
| limit 50
```

To pull the individual YO ad entries (bid ids and prices) for a specific session:

```
fields @timestamp, sessionId, avail.availId, avail.creativeAds
| filter awsAccountId = 'YOUR_ACCOUNT_ID'
  and eventType = 'FILLED_AVAIL'
  and sessionId = 'YOUR_SESSION_ID'
| sort @timestamp desc
| limit 20
```

Filter the resulting `creativeAds` array client-side for entries where `fillMode == "YIELD_OPTIMIZATION"`.

**Log group:** `MidasMMSService/ads_interaction_log`

### Check for unresolved template variables
<a name="yield-optimization-troubleshooting-insights-unresolved"></a>

```
fields @timestamp, sessionId, @message
| filter awsAccountId = 'YOUR_ACCOUNT_ID'
  and eventType = 'RAW_BID_REQUEST'
  and @message like /\{[A-Z_]+\}/
| sort @timestamp desc
| limit 20
```

**Log group:** `MidasMMSService/ads_interaction_log`

### Measure YO latency and success rate
<a name="yield-optimization-troubleshooting-insights-latency"></a>

```
fields @timestamp, @message
| filter customerId = 'YOUR_ACCOUNT_ID'
  and (@message like /YieldOptimization/ or @message like /ortb_/)
| limit 10000
```

**Log group:** `MidasMMSService/service_log`

**Note**  
`service_log` uses `customerId` (not `awsAccountId`) for the account ID field.

## Calculating yield lift
<a name="yield-optimization-troubleshooting-yield-lift"></a>

To measure the revenue impact of Yield Optimization, create a CloudWatch dashboard with:

1. **Incremental fill rate:** `Sum(YieldOptimization.AdsInserted) / Sum(YieldOptimization.BidRequest)` shows what percentage of YO opportunities result in inserted ads. Alternatively, use `Average(YieldOptimization.FillRate)` for the per-avail native metric.

1. **Revenue per hour:** `Sum(YieldOptimization.Revenue)` over time shows total per-customer revenue from YO. `Sum(YieldOptimization.BidPriceAdsInserted)` gives account-wide average CPM.

1. **Duration filled:** `Sum(YieldOptimization.FilledDuration)` against `Sum(YieldOptimization.BidDuration)` shows how much of the requested duration was actually filled.

## Common issues
<a name="yield-optimization-troubleshooting-common-issues"></a>

### Yield Optimization not triggering
<a name="yield-optimization-troubleshooting-not-triggering"></a>


| Symptom | Check | Resolution | 
| --- | --- | --- | 
| No YO metrics at all | Is YO configured on the playback config? | Enable YO in the console or API. | 
| SkipMinUnfilledDurationNotExceeded emitting | Primary ADS is filling most of the break | Lower MinimumUnfilledDuration or accept that primary fill is sufficient. | 
| SkipPersonalizationTimeoutExceeded emitting | Primary ADS is too slow, leaving no time for YO | Optimize primary ADS latency or check personalization timeout SDC configuration. | 

### Bid requests failing
<a name="yield-optimization-troubleshooting-bidrequests-failing"></a>


| Symptom | Check | Resolution | 
| --- | --- | --- | 
| BidRequestConfigurationError metric | Template has missing or empty mandatory fields | Check application.log for the specific error (for example, app.bundle is required). Fix the template or ensure player params are sent. | 
| HTTP 204 from APS | YieldOptimization.NoBid incrementing | APS returned no-bid. Not an error. Inspect RAW\_BID\_REQUEST for placeholder values ({UPPER\_CASE} patterns), verify bundle and storeurl are real, lower bidfloor. | 
| HTTP 429 from APS | YieldOptimization.BidRequestThrottled incrementing | APS is throttling. Back off request rate. If persistent, contact APS support to raise TPS limits. | 
| HTTP 400 from APS | Invalid request JSON | Check the APS error message in RAW\_BID\_RESPONSE. Verify JSON structure matches OpenRTB spec. | 
| HTTP 500/503 from APS | APS server error or overload | Transient issue. Monitor YieldOptimization.Errors. If persistent, contact APS support. | 

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