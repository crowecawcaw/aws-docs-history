

# ADVOPS05-BP01 Implement manifest generation observability with SCTE-35 marker validation
<a name="advops05-bp01"></a>

 Validate every generated SGAI manifest for SCTE-35 marker integrity before CDN distribution. In hybrid SGAI architectures, manifest errors move through CDN caching layers to every viewer of cached content. 

 **Desired outcome:** 
+  The pipeline validates every manifest for SCTE-35 markers before CDN distribution. Real-time alerts fire on validation failures. 
+  Automated fallback to last-known-good manifests starts when validation failure rates exceed critical thresholds. The CDN cache purges corrupted content automatically. 
+  You monitor CDN cache hit ratios to detect manifest distribution anomalies. These anomalies show that the CDN serves corrupted manifests to viewers. 

 **Common anti-patterns:** 
+  You treat SCTE-35 as one signal type, rather than providing distinct validation logic for different message types. 
+  You deploy manifest changes without pre-distribution validation. 
+  You do not monitor CDN cache hit ratios for manifest health. 

 **Benefits of establishing this best practice:** 
+  You detect manifest errors before they spread through CDN caching to viewers. 
+  Pre-distribution validation reduces the scope of impact for SCTE-35 signaling failures. 
+  You get real-time visibility into the health of the manifest generation pipeline. This visibility shortens incident response time. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance"></a>

 SCTE-35 is a signaling protocol with multiple message types. Each message type needs its own validation logic: 
+  **spliceinsert:** Immediate ad break triggers. Validate the accuracy of splice-point timing. Does the marker arrive early enough for the player to prepare? Validate break-duration consistency. Does the signaled duration match the ad pod length? Also validate the avail\_num and avails\_expected fields. 
+  **timesignal:** Scheduled event markers for more complex ad break timing. Validate segmentation-descriptor completeness. Are all required segmentation descriptor fields present? Also validate segment-type identifiers. Are the values appropriate for the content type? 
+  **splicenull:** Heartbeat signals that maintain stream continuity. Validate that splicenull messages appear on schedule. Missing splicenull messages can show a disruption in the pipeline. 
+  **privatecommand:** Vendor-specific extensions. Validate format conformance with the vendor specification for this deployment. 

 The CDN caches a manifest with a malformed spliceinsert marker and serves it to all concurrent viewers. It keeps this manifest in cache until the cache expires, or an operator purges it. The validation service must run SCTE-35 schema validation on every generated manifest before writing it to the CDN origin path. 

 Monitor the CDN cache hit ratio for a second signal. CloudFront can detect corrupted content and refuse to serve it, and a manifest-format change can break cacheability. A drop in cache hit ratio surfaces errors that validation missed. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Catalog all SCTE-35 message types and define validation rules for each:** For each SCTE-35 message type (spliceinsert, timesignal, splicenull, and privatecommand), document the required fields, the value constraints, the expected frequency, and the failure mode if a constraint fails. This catalog becomes the specification for the automated validation service. 

1.  **Implement automated schema validation before CDN distribution:** Deploy a validation Lambda function or container service. It runs SCTE-35 schema validation on every generated manifest. Configure the manifest generation pipeline to pass manifests through validation before the pipeline writes to the CDN origin path. On validation failure, route the manifest to a quarantine prefix and trigger an SNS notification. Do not serve the corrupted manifest. 

1.  **Configure CloudWatch alarms with severity by message type:** Create a separate CloudWatch alarm for each SCTE-35 message type. Spliceinsert validation failures use a critical alarm that triggers incident response immediately. Splicenull failures use a warning alarm that triggers investigation. Timesignal failures use a warning alarm. Privatecommand failures are informational. Different severity accounts for the different revenue impact of each message type failure. 

1.  **Monitor CDN cache hit ratios with automated alerting:** Configure analysis of CloudFront access logs with Amazon Athena. Calculate cache hit ratios per manifest path on a 5-minute cadence. Publish the cache hit ratio as a custom CloudWatch metric. Set alarms when the cache hit ratio drops more than 15% below the 7-day rolling baseline. This alarm detects manifest distribution anomalies. These anomalies show that the CDN serves corrupted manifests from cache. 

1.  **Implement automated fallback to last-known-good manifests:** Deploy an SSM Automation document. Trigger it from the alarm for spliceinsert validation failures. The document runs four actions: 

   1.  Save the current (failed) manifest to a quarantine S3 path for analysis. 

   1.  Restore the last-validated-good manifest to the CDN origin path. 

   1.  Start a CloudFront cache invalidation for the affected manifest paths. 

   1.  Send an SNS notification to the on-call team with the rollback details. 

    Configure an error counter to halt automation if three consecutive regenerations also fail validation. This counter prevents regeneration loops. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [ADVOPS05-BP02 Implement observability for ad break orchestration across server and client](advops05-bp02.md) 

 **Related documents:** 
+  [ANSI/SCTE 35 specification](https://www.scte.org/standards/library/catalog/scte-35-digital-program-insertion-cueing-message/) 
+  [AWS Elemental MediaTailor documentation](https://docs.aws.amazon.com/mediatailor/latest/ug/what-is-mta.html) 

 **Related services:** 
+  [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) 
+  [Amazon CloudFront](https://aws.amazon.com/cloudfront/) 
+  [AWS Systems Manager](https://aws.amazon.com/systems-manager/) 