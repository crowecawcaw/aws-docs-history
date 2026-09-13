

# Integrating with APS
<a name="yield-optimization-integrating-aps"></a>

At launch, Yield Optimization uses Amazon Publisher Services (APS) as the programmatic ad provider, with additional demand sources coming over time. To enable Yield Optimization, you need an APS Publisher ID from an active APS Streaming TV publisher account.

## What is APS?
<a name="yield-optimization-integrating-aps-what-is"></a>

Amazon Publisher Services is Amazon's advertising technology platform that connects publishers with advertisers through programmatic advertising. Through APS, publishers make their inventory available to Amazon DSP and Sponsored TV advertisers through real-time bidding.

## Activation process
<a name="yield-optimization-integrating-aps-activation"></a>

1. **Obtain your Publisher ID.** Contact your APS account team to get your Publisher ID, a universally unique identifier (UUID) similar to the example `8caf35b3-402b-4d75-bab2-f2aef63a66d3`.

1. **Enable Yield Optimization.** Enter your Publisher ID in the MediaTailor console or through the API to enable the feature.

## APS regions
<a name="yield-optimization-integrating-aps-regions"></a>

APS operates in three regions. Select the region closest to your primary audience:


| Region | Identifier | Coverage | 
| --- | --- | --- | 
| Americas | AMERICAS | North America, South America | 
| Europe | EUROPE | Europe, Middle East, Africa | 
| Asia Pacific | ASIA\_PACIFIC | Asia, Australia, Pacific | 

**Important**  
APS region selection is per playback configuration. If you serve multi-region traffic from a single playback configuration, you must select one APS region. For multi-region support, create separate playback configurations per region.

## Rate limits
<a name="yield-optimization-integrating-aps-rate-limits"></a>

Amazon Publisher Services scales to accommodate large publishers. No customer-facing rate limit applies.

## OpenRTB protocol
<a name="yield-optimization-integrating-aps-ortb-protocol"></a>

MediaTailor communicates with APS using the [OpenRTB 2.6 specification](https://github.com/InteractiveAdvertisingBureau/openrtb2.x/blob/main/2.6.md). The bid request is an HTTP POST with a JSON body conforming to the OpenRTB BidRequest schema. APS validates the request against the full OpenRTB spec and returns appropriate error codes.

## Next steps
<a name="yield-optimization-integrating-aps-next-steps"></a>
+ To understand how MediaTailor decides when to make bid requests, see [How Yield Optimization works](yield-optimization-how-it-works.md).
+ To configure your template, see [Bid construction and templating](yield-optimization-bid-construction.md).