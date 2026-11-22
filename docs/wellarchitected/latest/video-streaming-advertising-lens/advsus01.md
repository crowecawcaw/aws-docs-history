

# Software and architecture efficiency

 Design and implement architectures that minimize the average resources (compute, storage, and network) required per unit of work for your advertising workloads. Software and architecture choices directly determine how many resources are consumed to process each bid, deliver each impression, and serve each ad creative. Optimizing these choices reduces environmental impact proportionally with the scale of advertising operations. 


|  ADVSUS01: How do you design your advertising software, architecture, and data lifecycle to minimize resource consumption per unit of work?  | 
| --- | 
| [ADVSUS01-BP01 Run advertising fleets on multiple chipsets, including ARM, to lower energy intensity](advsus01-bp01.md) | 
| [ADVSUS01-BP02 Choose HTTP/2 or HTTP/3 to lower bytes transferred and connection overhead](advsus01-bp02.md) | 
| [ADVSUS01-BP03 Reduce CPU time per bid in agent containers to lower fleet energy intensity](advsus01-bp03.md) | 
| [ADVSUS01-BP04 Tune adapter concurrency and timeouts to stop spending compute on unusable bids](advsus01-bp04.md) | 
| [ADVSUS01-BP05 Serve cacheable ad manifests to reduce origin requests and server-side compute at scale](advsus01-bp05.md) | 
| [ADVSUS01-BP06 Keep yield analytics off the auction path so its compute scales with events, not traffic](advsus01-bp06.md) | 
| [ADVSUS01-BP07 Classify content once at ingest to remove repeat inference from the auction path](advsus01-bp07.md) | 
| [ADVSUS01-BP08 Identify and remove redundant data across advertising storage infrastructure](advsus01-bp08.md) | 

## Capability intent
<a name="advsus01-capability-intent"></a>
+  Your advertising workloads use chipset-agnostic design (AMD and Intel x86 compatibility) to access the lowest-cost Spot Instance options, reducing energy consumption per impression. 
+  HTTP/3 (QUIC) is enabled for ad creative delivery, reducing connection overhead and improving parallel asset delivery efficiency. 
+  ARTF agent containers are optimized for sub-millisecond processing through pre-allocated memory pools and compiled model formats, reducing energy per bid evaluation. 
+  Prebid Server adapter concurrency and timeout budgets are optimized to complete auctions efficiently without wasting compute on adapters that consistently miss deadlines. 
+  SGAI manifest and creative delivery are optimized for CDN cacheability, reducing per-viewer processing energy at scale. 
+  Publisher content is pre-classified for contextual targeting at ingest time, removing synchronous ML inference from the bid evaluation path. 
+  Each class of advertising data is retained only as long as its own purpose requires, so storage tracks genuine need rather than accumulating by default. 

## Common issues to watch for
<a name="advsus01-common-issues-to-watch-for"></a>
+  Running contextual classification synchronously during bid evaluation, adding 50–200 ms of ML inference energy consumption to every bid request when classification could be done at ingest time. 
+  Generating viewer-specific SSAI manifests instead of CDN-cacheable SGAI manifests, multiplying per-viewer processing energy linearly with viewer count. 
+  Serving all adapters with the same timeout budget rather than disabling consistently late adapters that waste timeout cycles. 
+  Treating bid event logs, impression logs, creatives, and draft assets as one undifferentiated pool under a single retention rule, so storage grows without bound while no single category is reviewed on its own merits. 