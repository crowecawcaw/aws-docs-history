

# ADVSUS01-BP02 Choose HTTP/2 or HTTP/3 to lower bytes transferred and connection overhead

 Use next-generation networking protocols to address low-latency needs and reduce connection overhead. HTTP/3 with QUIC avoids TCP head-of-line blocking and reduces connection establishment overhead, lowering the compute work and bytes transferred per ad creative delivery. Those quantities are the proxy for the energy attributable to that delivery. 

 **Desired outcome:** 
+  Ad creative assets are delivered over HTTP/3 with QUIC, avoiding TCP head-of-line blocking during parallel Video Ad Serving Template (VAST) asset fetches. 
+  Connection reuse through persistent HTTP/2 or HTTP/3 connections reduces TLS handshake overhead per bid, lowering the CPU cycles and bytes consumed per transaction as a proxy for attributable energy. 

 **Common anti-patterns:** 
+  Serving VAST manifests, companion banners, and video segments over HTTP/1.1 or TCP-based HTTP/2, so a single lost packet during a parallel creative fetch stalls every other asset behind it and forces redundant retransmission. 
+  Opening a fresh TLS connection for every supply-side to demand-side bid call instead of pooling persistent connections, repeating the handshake cost on each high-QPS request. 
+  Forcing viewers who roam between Wi-Fi and cellular during a mid-roll ad break to re-establish connections and re-fetch creative, duplicating transfer work that a migration-capable transport would avoid. 
+  Treating protocol selection as a one-time default and never confirming that capable clients actually negotiate the newer protocol in production. 

 **Benefits of establishing this best practice:** 
+  Lower bytes transferred and fewer retransmissions per ad delivery, reducing the resource utilization used as the proxy for attributable energy. 
+  Reduced CPU spent on repeated TLS handshakes across high-QPS bidding connections. 
+  Faster time-to-first-byte for creative delivery, improving viewer experience during ad breaks without adding origin capacity. 
+  More resilient delivery to mobile viewers whose connections migrate across networks mid-session. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance"></a>

 HTTP/3 uses QUIC as its transport layer instead of TCP. 0-RTT resumption applies to viewer-facing creative delivery, which is idempotent retrieval. It must not be enabled for bid request traffic, for the reason given in [ADVSUS02-BP06 Reduce per-auction network overhead by consolidating bid request fan-out and reusing transport connections](advsus02-bp06.md). QUIC provides zero round-trip time (0-RTT) connection resumption: when a viewer's device reconnects during a mid-roll ad break or page navigation, QUIC resumes the previous connection state without a full TLS handshake, reducing time-to-first-byte and the associated work for ad creative delivery. Amazon CloudFront supports HTTP/3 with QUIC across all edge locations. Bytes transferred and connection setup work are engineering proxies for energy, not a direct energy measurement. 

 QUIC avoids head-of-line blocking at the transport layer, because each stream operates independently, so a lost packet on one stream doesn't delay others. For VAST video ad serving, a video player can fetch VAST XML, companion banners, and video segments in parallel over a single QUIC connection. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Enable HTTP/3 on CloudFront distributions serving ad creatives:** In CloudFront distribution settings under "Supported HTTP versions," select HTTP/3. No origin changes are required. Viewers with HTTP/3-capable clients automatically negotiate QUIC. Older clients fall back to HTTP/2 or HTTP/1.1 transparently. 

1.  **Configure persistent HTTP/2 connection pooling for partner bid connections:** For high-QPS supply-side to demand-side connections, configure HTTP/2 persistent connections with appropriate pool settings. This reuses connections across bid calls and removes the repeated per-request TLS handshake, lowering the CPU cycles used as the proxy for attributable energy. 

1.  **Verify HTTP/3 negotiation in CloudFront access logs:** After enabling, filter CloudFront access logs for QUIC protocol usage to confirm HTTP/3-capable clients negotiate it. Track cache hit rate alongside connection migration, since viewers who switch between Wi-Fi and cellular keep their connections and avoid re-fetching creative, which lowers the bytes transferred that proxy for attributable energy. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [ADVSUS02-BP06 Reduce per-auction network overhead by consolidating bid request fan-out and reusing transport connections](advsus02-bp06.md) 
+  [ADVSUS02-BP05 Minimize bid response payload sizes](advsus02-bp05.md) 
+  [ADVSUS03-BP04 Carry only the OpenRTB fields the bidding logic uses to reduce bytes on the wire](advsus03-bp04.md) 

 **Related documents:** 
+  [Amazon CloudFront distribution settings, including supported HTTP versions](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/distribution-web-values-specify.html) 

 **Related services:** 
+  [Amazon CloudFront](https://aws.amazon.com/cloudfront/) 
+  [Elastic Load Balancing](https://aws.amazon.com/elasticloadbalancing/) 