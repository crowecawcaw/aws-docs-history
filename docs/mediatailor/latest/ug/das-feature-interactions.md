

# Feature interactions

The following table describes how dynamic avail sizing interacts with other MediaTailor features.


**Dynamic avail sizing feature interactions**  

| Feature | Behavior | 
| --- | --- | 
| Pre-roll | MediaTailor doesn't shorten or inflate pre-roll avails. For more information, see [MediaTailor pre-roll ad insertion](ad-behavior-preroll.md). | 
| Ad break suppression | MediaTailor doesn't shorten or inflate suppressed avails, and suppressed avails don't consume or refill the reserve. For more information, see [Configuring ad break suppression](ad-rules.md#ad-suppression). | 
| Low-Latency HLS | Not supported. MediaTailor ignores the dynamic avail sizing parameters on LL-HLS workflows. | 
| Prefetch | Prefetched avails aren't eligible for inflation. For more information, see [Prefetching ads](prefetching-ads.md). | 
| VOD | Not supported. Dynamic avail sizing applies to live and live-to-VOD HLS workflows only. MediaTailor ignores the dynamic avail sizing parameters on VOD workflows. | 
| Server-guided ad insertion (SGAI) | Not supported. Dynamic avail sizing applies to server-side ad insertion only. For more information, see [Server-guided ad insertion overview](server-guided.md). | 
| Yield optimization | When yield optimization is enabled and MediaTailor inflates an avail, yield optimization bids to fill the part of the inflated duration that the ADS didn't fill.<br />Ads from yield optimization count toward the avail's fill, the same as ads from the ADS, so they can also fill an inflated avail and refill the reserve.<br />For more information, see [How Yield Optimization works](yield-optimization-how-it-works.md). | 