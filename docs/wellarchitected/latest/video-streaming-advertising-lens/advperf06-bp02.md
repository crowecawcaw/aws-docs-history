

# ADVPERF06-BP02 Optimize your intake request format (HTTP/2 or HTTP/3) for faster processing
<a name="advperf06-bp02"></a>

 HTTP/3 with QUIC addresses two performance limitations for advertising workloads that HTTP/1.1 and HTTP/2 can't solve in transport: connection setup overhead and head-of-line blocking during parallel ad creative delivery. 

 **Desired outcome:** 
+  Ad creative assets (VAST XML responses, companion banners, video segments) are delivered to viewers over HTTP/3 with QUIC, avoiding TCP head-of-line blocking during parallel asset fetches. 
+  Returning viewers benefit from QUIC 0-RTT connection resumption, reducing time-to-first-byte for ad creative delivery. 
+  Mobile viewers experience uninterrupted ad delivery when switching between Wi-Fi and cellular networks during ad breaks. 

 **Common anti-patterns:** 
+  Serving ad creatives over HTTP/1.1 or HTTP/2 without QUIC, which forgoes the head-of-line blocking removal that speeds parallel VAST asset delivery. 
+  Not enabling HTTP/3 on [Amazon CloudFront](https://aws.amazon.com/cloudfront/) because of perceived complexity. 

 **Benefits of establishing this best practice:** 
+  HTTP/3 removes head-of-line blocking at the transport layer: each stream operates independently, so a lost packet on one stream doesn't delay others. For VAST video ad serving, this means a video player can fetch the VAST XML response, companion banners, and video segments in parallel. 
+  QUIC 0-RTT connection resumption reduces time-to-first-byte for returning viewers, which especially helps mid-roll ad breaks where the player reconnects to Amazon CloudFront. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance"></a>

 HTTP/2 over TCP provides *multiplexing*, where multiple requests share a single TCP connection, which removes the per-connection overhead of HTTP/1.1. However, TCP-level head-of-line blocking remains, where a single lost packet stalls all multiplexed streams on the connection until the packet is retransmitted and acknowledged. For ad creative delivery where the video player simultaneously requests a VAST XML file, companion banner images, and video segments, one packet loss delays all these assets. 

 HTTP/3 uses QUIC as its transport protocol instead of TCP. QUIC provides stream-level independence. A lost packet on one stream pauses only that stream while all other streams continue delivering their content. For VAST ad pod assembly where multiple assets must be fetched simultaneously, this removes the correlated delay caused by a single packet loss event under HTTP/2. 

 QUIC's 0-RTT connection resumption benefits returning viewers. When a viewer reconnects to CloudFront after navigating between pages or switching networks, HTTP/2 over TCP requires a full TCP \+ TLS handshake (2–3 round trips) before the first byte of content can be delivered. QUIC 0-RTT resumes the previous connection state without handshake, delivering the first byte immediately on reconnection. For mid-roll ad breaks, this removes the startup latency that would otherwise delay the ad break beginning. 

 CloudFront supports HTTP/3 across all edge locations. Enabling it requires selecting HTTP/3 in your distribution's supported HTTP versions settings. No origin changes are required. Older clients that don't support HTTP/3 automatically negotiate HTTP/2 or HTTP/1.1 through CloudFront's protocol fallback. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Enable HTTP/3 on CloudFront distributions serving ad creatives:** In your CloudFront distribution's supported HTTP versions settings, select HTTP/3 to enable QUIC across all CloudFront edge locations. This is a low-risk configuration change with no impact on compatibility. Viewers with HTTP/3-capable clients negotiate QUIC, and older clients fall back transparently. 

1.  **Verify HTTP/3 negotiation with CloudFront access logs:** Enable CloudFront access logs and add the x-edge-result-type and protocol fields. After enabling HTTP/3, verify that a portion of requests are being served with HTTP/3 by filtering logs for the QUIC protocol identifier. The adoption rate depends on viewer client capabilities. Modern Chrome, Firefox, and Safari versions all support HTTP/3. 

1.  **Confirm HTTP/2 is enabled as the minimum baseline:** For viewers not on HTTP/3-capable clients, verify that HTTP/2 is enabled on your CloudFront distributions. HTTP/2 multiplexing reduces the number of TCP connections required per viewer compared to HTTP/1.1, removing per-connection handshake overhead for parallel VAST asset fetches even without QUIC. 

1.  **Monitor ad creative delivery performance by protocol version:** Use CloudFront real-time logs or CloudWatch metrics to monitor cache hit rate, time-to-first-byte, and viewer latency by protocol version. Compare HTTP/3 compared to HTTP/2 latency distributions to validate the improvement from QUIC. For regions with higher packet loss rates (mobile networks in some regions), the benefit from head-of-line blocking removal is most pronounced. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [ADVPERF05-BP02 Use edge services for static content caching and dynamic request acceleration](advperf05-bp02.md) 

 **Related documents:** 
+  [New HTTP/3 Support for Amazon CloudFront](https://aws.amazon.com/blogs/aws/new-http-3-support-for-amazon-cloudfront/) 

 **Related services:** 
+  [Amazon CloudFront](https://aws.amazon.com/cloudfront/) 