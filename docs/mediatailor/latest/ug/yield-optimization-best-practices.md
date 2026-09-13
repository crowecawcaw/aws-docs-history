

# Best practices
<a name="yield-optimization-best-practices"></a>

## Template construction
<a name="yield-optimization-best-practices-template"></a>

### Start with a minimal working template
<a name="yield-optimization-best-practices-start-minimal"></a>

Use Example 1 from [Example templates](yield-optimization-examples.md) to validate your APS integration. Add fields incrementally and test each addition by checking `RAW_BID_REQUEST` events in CloudWatch Logs.

### Provide all APS-recommended fields
<a name="yield-optimization-best-practices-recommended-fields"></a>

Fields marked "APS Recommended" in the [ORTB field reference](yield-optimization-ortb-reference.md) significantly impact fill rates. At minimum, include: `app.bundle`, `app.storeurl`, `app.name`, `device.ua`, `device.ip`, `device.make`, `device.model`, `device.os`, `video.mimes`, `video.protocols`, `video.w`, `video.h`, `video.plcmt`, and `video.ext.slotId`.

### Use session variables for device identification
<a name="yield-optimization-best-practices-session-vars"></a>

The `device.ua` and `device.ip` fields must reflect the actual viewer for proper ad targeting. Use `{{session.user_agent}}` and `{{session.client_ip}}` which are automatically populated from the viewer's HTTP connection. No player parameter setup is required for these fields.

### Provide a real `app.bundle` and `app.storeurl`
<a name="yield-optimization-best-practices-real-bundle"></a>

APS uses these for app identification and ad targeting. Incorrect or placeholder values result in no-bid (204) responses.

### Set an appropriate `imp[0].bidfloor`
<a name="yield-optimization-best-practices-bidfloor"></a>

The console default is $5 CPM. If fill rates are low, consider lowering the floor. A lower floor increases the pool of eligible advertisers but may reduce average CPM.

### Provide your actual `video.ext.slotId`
<a name="yield-optimization-best-practices-slotid"></a>

The slot ID maps to your APS inventory configuration. Providing your actual slot ID (from the APS console) allows APS to apply slot-specific targeting and floor pricing. The default value (`"default_slot_id"`) works but may result in less optimal ad selection.

### Include broad `video.protocols` support
<a name="yield-optimization-best-practices-protocols"></a>

Use `[2, 3, 5, 6]` at minimum (VAST 2.0, 3.0, 2.0 Wrapper, 3.0 Wrapper). For maximum compatibility, use `[1, 2, 3, 4, 5, 6, 7, 8]` to support all VAST versions (1.0 through 4.0, including wrappers).

### Don't set fields that EMT manages
<a name="yield-optimization-best-practices-emt-managed"></a>

Fields like `imp.video.maxduration`, `imp.video.poddur`, `imp.video.minduration`, `imp.video.maxseq`, `app.publisher.id`, and `ext.integrationType` are always set by MediaTailor using your console configuration values. Including them in your template is harmless but misleading.

### Prefer `regs.gpp` and `regs.gpp_sid` over `regs.us_privacy` for US privacy signals
<a name="yield-optimization-best-practices-gpp"></a>

When passing US privacy signals to APS, use the Global Privacy Platform (GPP) fields instead of the older `us_privacy` string:

```
"regs": {
  "coppa": 0,
  "gpp": "DBABMA~1---",
  "gpp_sid": [7]
}
```

APS applies stricter data-use restrictions when it sees a `us_privacy` string (CCPA opt-out signal), which limits the pool of eligible advertisers and reduces fill rates. GPP gives APS more granular jurisdiction-level signals, resulting in more accurate compliance enforcement and a larger pool of eligible bids. If your player sends both signals, prefer GPP and omit `us_privacy`.

**GPP section IDs for US privacy:**


| Section ID | Scope | 
| --- | --- | 
| 7 | US National (Multi-State Privacy) | 
| 8 | US California (CPRA) | 
| 9 | US Virginia (VCDPA) | 
| 10 | US Colorado (CPA) | 
| 11 | US Utah (UCPA) | 
| 12 | US Connecticut (CTDPA) | 

If you must include `us_privacy` for downstream systems, it is safe to pass both, but APS will use the GPP signal when present.

## Operational considerations
<a name="yield-optimization-best-practices-operational"></a>

### Regional configuration
<a name="yield-optimization-best-practices-regional"></a>

APS region is set per playback configuration. If you serve viewers in multiple APS regions, create separate playback configurations per region for optimal latency and ad inventory availability.

### Monitoring yield lift
<a name="yield-optimization-best-practices-monitoring-lift"></a>

Use CloudWatch metrics to calculate yield lift:
+ **Fill rate improvement:** Compare `YieldOptimization.AdsInserted` against total avails to measure incremental fill. `YieldOptimization.FillRate` (native per-avail metric) can also be averaged over a period.
+ **Revenue contribution:** Use `YieldOptimization.Revenue` for total per-customer revenue (sum of inserted ad prices). Use `YieldOptimization.BidPriceAdsInserted` for account-wide average CPM. `YieldOptimization.IndicativeBidRevenue` is dual-emitted alongside `Revenue` during a deprecation window and will be removed. Prefer `Revenue` for new dashboards.
+ **Efficiency:** Compare `YieldOptimization.BidRequest` against `YieldOptimization.AdsInserted` to measure conversion rate.

### Avoid unresolved placeholder patterns
<a name="yield-optimization-best-practices-unresolved"></a>

If your ADS URL uses `[player_params.X]` and the player doesn't send param `X`, the literal `{X}` placeholder passes through to the ORTB template. APS sees `"{APP_NAME}"` as a literal string and returns no-bid. Always verify your `RAW_BID_REQUEST` payloads don't contain `{UPPER_CASE}` patterns.

## Next steps
<a name="yield-optimization-best-practices-next-steps"></a>
+ For monitoring and debugging, see [Troubleshooting and monitoring](yield-optimization-troubleshooting.md).