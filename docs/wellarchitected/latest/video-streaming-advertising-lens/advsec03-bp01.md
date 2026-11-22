

# ADVSEC03-BP01 Protect advertising endpoints against volumetric and application-layer attacks

 Advertising platforms process variable traffic loads that can spike by orders of magnitude during live events or tentpole programming. Outside parties might exploit this variability by disguising volumetric events as legitimate bid request traffic. Without threat-aware protection tuned to advertising traffic patterns, systems can't distinguish a real traffic spike from unauthorized traffic without dropping legitimate revenue-generating requests. 

 **Desired outcome:** 
+  You have distributed denial of service (DDoS) protection that accounts for natural advertising traffic variability, with baselines tuned to expected bid volumes for each partner. 
+  Your protection distinguishes between legitimate high-traffic events (live sports, tentpole premieres) and malicious floods at the application layer. 
+  You have proactive engagement with AWS Shield Response Team before planned high-traffic events to pre-scale protection thresholds. 

 **Common anti-patterns:** 
+  Relying solely on static rate limiting that blocks legitimate traffic during high-profile live events when bid volume naturally spikes by an order of magnitude or more. 
+  Using one baseline for all bid endpoint traffic leaves you unable to detect when traffic from one supply-side platform (SSP) deviates from normal. 
+  Deploying DDoS protection on the public endpoint but leaving internal bid processing APIs unprotected, so a compromised partner connection can reach them laterally. 

 **Benefits of establishing this best practice:** 
+  Maintains bid processing availability during attacks without dropping legitimate revenue-generating bid requests from authorized partners. 
+  Detects application-layer attacks (slow-rate bid flooding, malformed bid request injection) that volumetric-only protection misses. 
+  Provides cost protection through AWS Shield Advanced and reduces attack-driven automatic scaling costs that affect advertising operations budgets. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance"></a>

 Advertising protection needs a partner traffic envelope rather than one global rate. The envelope describes expected volume, timing, request shape, and endpoint use for a partner, together with a confidence state based on available history. A low-confidence envelope needs conservative enforcement and protocol checks because a new partner can look anomalous, whereas an authorized partner can send harmful traffic that remains inside normal volume. 

 A planned event requires a time-bound event exception. The baseline remains unchanged. The exception records the affected partners and resources, forecast traffic, enforcement changes, owner, start time, and expiry. Evaluate it against business exposure and acceptable interruption. A short outage on a high-value auction path can justify proactive support even when its request volume is lower than another endpoint. 

 This best practice ends at the infrastructure and request boundary, where edge services can evaluate traffic reaching bid, ad-tag, portal, and session endpoints. Browser extensions that change rendered content and valid creatives replaced after approval never present the same evidence at that boundary, so creative-delivery integrity owns those cases. Infrastructure protection remains responsible for volumetric abuse, malicious request behavior, and injection patterns that traverse a protected endpoint. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Map critical resources to business exposure:** Associate each CloudFront distribution, Route 53 hosted zone, Application Load Balancer, and API with its advertising function, acceptable interruption, and response path. Enable AWS Shield Advanced where the exposure supports proactive protection and cost protection. 

1.  **Build partner traffic envelopes:** Publish partner-specific CloudWatch metrics for volume, timing, request shape, and errors. Record the confidence state, apply a documented fallback for limited history, and use AWS WAF rate-based rules that preserve partner context. 

1.  **Add application-layer request inspection:** Use AWS WAF Bot Control and custom rules to distinguish expected programmatic clients from malformed requests, credential abuse, and automated portal traffic. Test rule actions against authorized partner samples before blocking. 

1.  **Operate planned-event exceptions:** Create each exception from the event forecast, limit it to named partners and resources, and set an automatic expiry. Engage the Shield Response Team when the mapped business exposure requires proactive support, then compare actual traffic with the forecast. 

1.  **Detect request-layer injection:** Inspect requests to publisher-facing tags and APIs for unexpected script sources, iframe injection attempts, and overlay or clickjacking patterns. Route content substitutions that occur after delivery to the creative-integrity response path. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [ADVSEC01-BP02 Restrict DSP access to allow only authorized SSPs](advsec01-bp02.md) 

 **Related documents:** 
+  [AWS Shield Advanced overview](https://docs.aws.amazon.com/waf/latest/developerguide/ddos-advanced-summary.html) 
+  [AWS WAF Bot Control](https://docs.aws.amazon.com/waf/latest/developerguide/aws-managed-rule-groups-bot.html) 
+  [Shield Advanced cost protection](https://docs.aws.amazon.com/waf/latest/developerguide/ddos-advanced-summary-credits.html) 

 **Related services:** 
+  [AWS Shield](https://aws.amazon.com/shield/) 
+  [AWS WAF](https://aws.amazon.com/waf/) 
+  [Amazon CloudFront](https://aws.amazon.com/cloudfront/) 
+  [Amazon Route 53](https://aws.amazon.com/route53/) 