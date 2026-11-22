

# ADVSEC04-BP04 Secure ad creative delivery and content integrity across converged channels

 Server-side ad insertion (SSAI) dynamically inserts ads into broadcast-grade streams. A threat actor who substitutes a creative can create a large-scale brand safety threat. One compromised creative in a free ad-supported streaming television (FAST) channel or live stream can reach the entire audience at once. Verify integrity from ad decisioning through manifest stitching and viewer delivery. 

 **Desired outcome:** 
+  You have creative integrity verification that validates ad assets against a registered hash before stitching into viewer streams. 
+  You have viewer-specific token authentication that helps protect each SSAI session and reduces the risk of unauthorized access to personalized ad streams. 
+  You have real-time detection and alerts for creative substitution, Video Ad Serving Template (VAST) response manipulation, and unauthorized session fabrication. 

 **Common anti-patterns:** 
+  Accepting a creative URL from a VAST response without verifying that it points to an approved content delivery network (CDN) origin can permit substitution after an ad server compromise. 
+  Serving SSAI manifest endpoints without session authentication, which lets bots fabricate viewing sessions for impression fraud. 
+  Deploying creative integrity checks only at upload time without re-validating that CDN-hosted creatives have not been tampered with after initial approval. 

 **Benefits of establishing this best practice:** 
+  Reduces the risk of unauthorized ad substitution in premium linear-like streams where one delivery-path compromise can affect many viewers. 
+  Blocks SSAI session fabrication by requiring authenticated session creation and evaluating device behavior. 
+  Maintains content integrity across the converged delivery chain and supports evidence requirements for broadcast-adjacent content. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance"></a>

 Creative delivery integrity relies on a delivery authorization record that is independent of the asset URL. The record binds a creative ID to an approved derivative, content digest, permitted origin, transformation history, and approval evidence. Transcoding and packaging can change an upload, but a compromised origin can return different bytes from an unchanged URL, so the URL alone cannot confirm integrity. 

 The delivery path has separate content and session decisions. Content authorization checks whether the resolved asset matches the expected derivative immediately before insertion. The session assurance level describes how strongly the service must verify a viewer session before it can create a personalized stream. Signed tokens, device characteristics, and client attestation provide different assurance, renewal behavior, startup cost, and client coverage. Select the level from client capability and fraud exposure. 

 Behavioral detection supplies evidence when authentication alone can't distinguish a legitimate automated client from fabricated Connected TV activity. Session order, duration, location changes, and creation velocity can indicate fraud, but household devices and shared networks can produce similar signals. Define fraud response tiers for observation, impression ineligibility, stronger verification, and blocking. This limits advertiser loss without making an uncertain signal interrupt playback immediately. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Create and govern delivery authorization records:** Store the approved creative ID, derivative digest, permitted origin, transformation metadata, status, and approval evidence in a controlled registry. Separate authority to approve a creative from authority to replace or revoke its record. 

1.  **Enforce content authorization before insertion:** Validate the resolved VAST origin against the permitted origin and compare the fetched derivative with its registered digest in the creative-resolution path before AWS Elemental MediaTailor stitches it. Reject mismatches and preserve the response and digest evidence. 

1.  **Apply the required session assurance level:** Protect SSAI session creation with signed viewer tokens where clients support them. Bind claims to appropriate session or device attributes, define renewal behavior for long playback, and use stronger client evidence where available. 

1.  **Evaluate session behavior and apply response tiers:** Use AWS WAF Bot Control and workload-specific signals to identify abnormal creation velocity, impossible location changes, invalid request order, or copied device profiles. Apply the response tier that matches signal confidence. 

1.  **Correlate delivery and session evidence:** Monitor authorization failures, unapproved origins, digest mismatches, token failures, session anomalies, and registry changes in one investigation view. Route creative-integrity events and suspected session fraud to their named owners. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [ADVSEC02-BP02 Protect linear distribution feeds and ad signaling in converged delivery](advsec02-bp02.md) 
+  [ADVSEC04-BP02 Create guardrails and controls to maintain brand safety and content moderation within your workload](advsec04-bp02.md) 
+  [ADVSEC04-BP01 Validate and sanitize ad creative content before campaign activation](advsec04-bp01.md) 

 **Related documents:** 
+  [Secure Media Delivery at the Edge on AWS](https://aws.amazon.com/solutions/guidance/secure-media-delivery-at-the-edge-on-aws/) 
+  [IAB Tech Lab ads.cert](https://iabtechlab.com/blog/public-release-ads-cert-securing-ctv-supply-chain/) 
+  [IAB Ad Creative ID Framework (ACIF)](https://iabtechlab.com/acif) 
+  [AWS WAF Bot Control](https://docs.aws.amazon.com/waf/latest/developerguide/aws-managed-rule-groups-bot.html) 

 **Related services:** 
+  [AWS Elemental MediaTailor](https://aws.amazon.com/mediatailor/) 
+  [Amazon CloudFront](https://aws.amazon.com/cloudfront/) 
+  [Amazon S3](https://aws.amazon.com/s3/) 
+  [AWS WAF](https://aws.amazon.com/waf/) 