

# ADVSEC04-BP01 Validate and sanitize ad creative content before campaign activation
<a name="advsec04-bp01"></a>

 Unauthorized ad creatives (malvertising) are a direct security threat to viewers and publishers. Compromised creatives can contain JavaScript-based issues, redirect chains to fraudulent sites, cryptomining code, or forced downloads. Without pre-activation scanning, your service can serve one compromised creative millions of times before you detect it. 

 **Desired outcome:** 
+  You have automated scanning of all ad creatives (display, video, and rich media) for malicious content before they enter your ad-serving pipeline. 
+  Your validation pipeline detects known malvertising patterns including JavaScript exploits, suspicious redirect chains, and unauthorized data collection mechanisms. 
+  You have creative security and policy controls that verify each asset and its resolved dependencies before activation. 

 **Common anti-patterns:** 
+  Accepting ad creatives from programmatic demand sources without scanning, relying solely on the DSP or exchange to perform creative quality checks. 
+  Scanning only static images and ignoring HTML5 rich media ads, Video Ad Serving Template (VAST) wrappers, or interactive creatives where threat actors can embed malicious code. 
+  Performing creative validation only at upload time without rescanning creatives that reference external resources, which might change after initial approval. 

 **Benefits of establishing this best practice:** 
+  Reduces the risk of malvertising distribution through your ad-serving infrastructure, helping protect viewer security and publisher reputation. 
+  Provides creative-validation evidence that an accountable owner can assess against the Trustworthy Accountability Group (TAG) Certified Against Malvertising (CAM) requirements. 
+  Reduces incident response costs by catching malicious creatives before distribution rather than after viewer reports. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance"></a>

 Creative security depends on a release-state model that separates unreviewed, quarantined, eligible, and revoked creatives. Brand suitability evaluates the publisher environment, whereas malvertising analysis evaluates creative behavior and destinations. This split places harmful behavior with security and campaign context with ad operations and brand teams. 

 Inspection identifies risk in an asset without changing it, so a creative that passes inspection still carries whatever active content it arrived with. Sanitization produces a different asset, either by re-encoding a static file so that only media survives or by rebuilding a renderable creative from approved elements. Isolated execution runs a dynamic creative in a disposable environment and records its behavior. This is the only way to observe behavior that appears at runtime. Inspection alone means your service serves the original bytes with only an audit note that inspection cleared them. 

 The release policy sets the permitted exposure window before a decision becomes final. A blocking model keeps an unreviewed creative out of delivery and adds campaign delay. An asynchronous model can preserve launch speed but needs immediate revocation, a record of every affected placement, and an accountable risk owner. Campaign urgency alone doesn't justify serving an unreviewed creative. 

 Treat the evidence unit as the submitted asset plus every dependency that can change its behavior. VAST wrappers, scripts, style sheets, remote media, and redirect destinations can change without altering the creative ID. Approval therefore applies to the observed dependency graph and validation evidence at a point in time. When a dependency or threat indicator changes, identify every eligible creative that relied on it. 

 Detection thresholds and human decisions form one control. A false negative can expose viewers before reports arrive, whereas excessive false positives can stop legitimate campaigns and overwhelm review queues. Assign owners for rejection, quarantine, release, and threshold changes. Preserve enough evidence to reconstruct the automated findings, human decision, later rescans, and incident response without relying on ordinary access logs. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Define and enforce creative release states:** Record the blocking or asynchronous policy for each creative type and demand source, along with the accountable owner, the approval date, and the next review date. Block unreviewed, quarantined, and revoked creatives from becoming serve-eligible outside the approved exposure-window policy. 

1.  **Inspect and sanitize static and renderable creatives:** Trigger validation when a creative enters Amazon S3. Evaluate images and video against applicable content policy, then re-encode them so that only media survives, and serve the derived asset rather than the original. Rebuild HTML5 and rich media from approved elements, removing or rewriting inline and referenced scripts, event handlers, and external references you have not approved. 

1.  **Execute dynamic creatives in an isolated environment:** Run HTML5, rich media, and VAST-referenced players in a single-use environment with default-deny egress, and record code behavior, DOM changes, and every outbound request. Set a wall-clock limit and CPU, memory, and disk quotas for each analysis. Fail an asset that exceeds a limit or requests a destination you have not approved. 

1.  **Resolve and preserve the evidence unit:** Traverse VAST wrapper chains to the final media, record every redirect and remote dependency, and compare destinations with approved origins. Store the dependency graph with the validation result. 

1.  **Map each analysis result to a release state:** Assign eligible only when every check passes, the sanitized derivative exists, and every dependency resolves to an approved origin. Assign quarantined for uncertain or incomplete results, such as a timeout, an unresolved dependency, or a borderline detection score. Assign revoked for confirmed harmful behavior, an unapproved outbound destination, or a failed sanitization rebuild. 

1.  **Re-evaluate active creatives when evidence changes:** Identify eligible creatives affected by changed scripts, media, destinations, detection rules, or threat indicators. Move uncertain results to quarantined and confirmed harmful results to revoked before further delivery. 

1.  **Record decisions and operating metrics:** Retain the creative ID, evidence unit, automated findings, release-state transitions, reviewer, reason, and timestamps for the required audit period. Measure false positives, false negatives found after release, review time, and exposure-window exceptions by source and creative type. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [ADVSEC04-BP02 Create guardrails and controls to maintain brand safety and content moderation within your workload](advsec04-bp02.md) 
+  [ADVSEC04-BP03 Implement supply chain transparency controls to block ad fraud](advsec04-bp03.md) 

 **Related documents:** 
+  [Amazon S3 object integrity checking](https://docs.aws.amazon.com/AmazonS3/latest/userguide/checking-object-integrity.html) 
+  [TAG Certified Against Malvertising (CAM)](https://www.tagtoday.net/threat-sharing) 

 **Related services:** 
+  [Amazon S3](https://aws.amazon.com/s3/) 
+  [Amazon Rekognition](https://aws.amazon.com/rekognition/) 
+  [Amazon Comprehend](https://aws.amazon.com/comprehend/) 
+  [AWS CloudTrail](https://aws.amazon.com/cloudtrail/) 
+  [AWS WAF](https://aws.amazon.com/waf/) 