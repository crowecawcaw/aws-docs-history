

# ADVOPS05-BP03 Create SGAI-specific runbooks and playbooks for manifest and player failures

 Without documented response procedures, SGAI incidents require unplanned troubleshooting across multiple system layers (manifest generation, CDN caching, and client-side ad fetching), which extends MTTR and compounds revenue impact. Use runbooks for known failure modes and playbooks for novel failure patterns. 

 **Desired outcome:** 
+  Documented, tested runbooks exist for all anticipated SGAI failure modes, enabling rapid incident response with clear escalation paths. 
+  Playbooks with hypothesis trees guide investigation of novel or intermittent failure patterns. 
+  On-call staff are trained on SGAI-specific procedures through structured walkthroughs before rotation begins. 

 **Common anti-patterns:** 
+  Relying on ad-hoc troubleshooting for SGAI incidents. SGAI spans multiple system layers and requires specific diagnostic steps for each. 
+  Maintaining only runbooks without investigation playbooks for novel failure patterns. The most challenging SGAI failures are intermittent and not covered by known resolution paths. 
+  Not distinguishing between hybrid and personalized SGAI failure modes in response procedures. Hybrid SGAI failures have CDN-level scope of impact while personalized SGAI failures are session-scoped. 

 **Benefits of establishing this best practice:** 
+  Reduced MTTR for SGAI incidents through pre-documented response procedures. 
+  Consistent incident response quality regardless of which on-call team member responds. 
+  Proactive identification of runbook gaps through regular game day exercises. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance"></a>

 SGAI incidents span a wider range of system layers than most ad tech failures, and the hybrid SGAI scope of impact (all concurrent viewers of a channel) means that investigation delays translate to large-scale revenue impact. 

 Runbook categories for hybrid SGAI: 
+  **Manifest generation errors:** Diagnosis steps (check manifest generation service logs for error codes, validate SCTE-35 message types against schema, check CDN origin path for malformed manifests), regeneration procedure (execute SSM Automation document for manifest regeneration with CDN cache purge), and validation steps (confirm ad break completion rate recovering within 5 minutes). 
+  **SCTE-35 marker validation failures:** Separate procedures for each message type (check splice point timing arithmetic for spliceinsert, segmentation descriptor fields for timesignal, heartbeat signal interval for splicenull, and vendor spec conformance for privatecommand). 
+  **Player-side ad fetch timeouts:** Diagnosis steps (check demand partner health dashboard, check ADS response latency, validate creative asset CDN availability), fallback activation (configure player to use fallback creative pool), and demand partner health check (invoke partner notification procedure if timeout rate exceeds threshold on their links). 
+  **AWS Elemental MediaTailor integration health degradation:** Service health verification (check AWS Service Health Dashboard for MediaTailor), configuration validation (verify playback configuration parameters), and failover procedures (route traffic to secondary MediaTailor configuration if primary is degraded). 

 Playbooks with hypothesis trees address intermittent failures that don't manifest consistently enough to have a known resolution path. A playbook for intermittent ad break completion rate drops would structure hypotheses by layer (CDN intermittent caching failures to SCTE-35 timing boundary conditions to demand partner intermittent latency spikes to client network condition correlation) with specific diagnostic steps to confirm or rule out each hypothesis. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Catalog all known SGAI failure modes by classification:** List all failure modes observed in production or identified through risk analysis, classified as runbook-appropriate (known resolution) or playbook-appropriate (investigation required). Include all four SCTE-35 message type failure modes, all three pipeline layer failure modes, and both hybrid and personalized SGAI failure profiles. This inventory is the gap analysis against your current documentation. 

1.  **Author step-by-step runbooks for known failure modes:** For each runbook-appropriate failure mode, write numbered sequential steps with specific commands. Include: the exact CloudWatch query to determine which SCTE-35 message type is failing, the specific SSM Automation document to invoke for manifest regeneration, the CloudFront cache invalidation API call syntax, and the verification step to confirm resolution. Test each runbook in a staging environment before publishing. 

1.  **Author playbooks with hypothesis trees for novel failure patterns:** Create playbooks for intermittent or novel failure patterns structured as: observable symptoms (the specific alarm and dashboard state that the responder is seeing), hypothesis list (ranked by historical probability for this symptom pattern), diagnostic steps per hypothesis (what to check, in sequence, to confirm or rule out each hypothesis), decision points (if hypothesis is confirmed, go to runbook X, and if ruled out, check next hypothesis), and escalation criteria (after all hypotheses are ruled out, escalate to tier 2 with specific data to bring to the escalation). 

1.  **Implement automated manifest regeneration through Systems Manager Automation:** Create an SSM Automation document for SGAI manifest regeneration triggered by the spliceinsert validation failure alarm: (1) log incident context (channel ID, affected manifest paths, failure details) to CloudWatch, (2) execute manifest regeneration API call, (3) validate regenerated manifest passes SCTE-35 schema validation, (4) execute CloudFront cache invalidation for affected paths, (5) verify ad break completion rate metric recovery within 5 minutes. Configure rate control and error threshold guardrails to guard against runaway automation. 

1.  **Conduct quarterly game day exercises and on-call onboarding walkthroughs:** Schedule quarterly game days that simulate SGAI failures: inject a simulated SCTE-35 validation failure, activate the manifest regeneration runbook, and measure time from alarm to recovery. After each game day, update runbooks based on gaps discovered. Conduct structured walkthroughs of SGAI runbooks and playbooks with all new on-call engineers before their first rotation, so they have at minimum read through and understood each procedure. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [ADVOPS05-BP01 Implement manifest generation observability with SCTE-35 marker validation](advops05-bp01.md) 
+  [ADVOPS05-BP02 Implement observability for ad break orchestration across server and client](advops05-bp02.md) 

 **Related documents:** 
+  [AWS Systems Manager Automation documentation](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-automation.html) 
+  [ANSI/SCTE 35 specification](https://www.scte.org/standards/library/catalog/scte-35-digital-program-insertion-cueing-message/) 

 **Related services:** 
+  [AWS Systems Manager](https://aws.amazon.com/systems-manager/) 
+  [Amazon CloudFront](https://aws.amazon.com/cloudfront/) 