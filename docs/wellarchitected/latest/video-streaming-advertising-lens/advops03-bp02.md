

# ADVOPS03-BP02 Establish operational readiness reviews for publisher launches

 New SSP adapter integrations, SGAI pipeline deployments, FAST channel launches, and innovative ad format rollouts must undergo an operational readiness review before entering production. The review is a formal gate. A workload that fails any checklist item must not activate. 

 **Desired outcome:** 
+  Every publisher workload launch has verified monitoring coverage, documented runbooks, defined escalation paths, and validated rollback procedures before serving live traffic. 
+  The readiness review is a formal gate with a named owner accountable for sign-off. 
+  Load testing has been completed at expected peak traffic levels before activation. 

 **Common anti-patterns:** 
+  Launching new SSP adapter integrations without verifying monitoring coverage. The most common manifestation is discovering after launch that there are no alarms for adapter timeout spikes. 
+  Deploying SGAI pipelines without documented playbooks for investigation of novel failure modes, leaving on-call engineers to improvise investigation procedures during incidents. 
+  Skipping load testing before FAST channel launches. Live events drive traffic spikes that may exceed design capacity. 
+  Treating readiness review as a checkbox exercise rather than a genuine gate that can block activation. 

 **Benefits of establishing this best practice:** 
+  Reduced risk of unmonitored production failures. 
+  Faster incident response through pre-validated runbooks and on-call training. 
+  Improved team confidence during launches. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance"></a>

 Publisher ad tech launches routinely proceed without formal readiness validation. Engineering completes a feature, ad operations confirms it works in staging, and it goes live. In the first production incident, no monitoring dashboard shows the relevant metrics, no runbook exists for the failure mode, and the on-call engineer is debugging a system they have never operated in production. 

 A readiness gate helps you discover problems earlier. Every useful checklist item captures a lesson from a past incident. A checklist built built from your own past failures and problems is shorter and more effective, especially when it is kept up to date with your environment. 

 An item belongs on the checklist only if it could plausibly fail. Questions that are answered by default can produce false sign-offs that do not certify anything about your workload. Useful checklist examples include whether the on-call engineer has operated the workload before, whether a failure mode has a documented response, and whether a recovery path has been exercised. 

 Baselines are often skipped but are the most expensive item to skip, because you can't create them retroactively. After a launch, you can only judge whether current behavior is normal against a record of what preceded it. You can capture a baseline before activation for almost nothing, but you can't reconstruct it afterward. 

 A checklist becomes a control only when one person owns it. When a team owns the checklist, no specific person verifies each item, because every item looks like another member's responsibility. Naming one owner also assigns accountability when a launch fails after passing. 

 Launches fail at the peak. Testing at expected load leaves that risk untested. The margin above expected peak reflects how wrong the forecast could be. Set it generously for scheduled events where a third party controls the programming. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Define a standardized publisher operational readiness checklist template:** Create a checklist template covering: monitoring dashboards configured and displaying expected metrics, runbooks documented for well-understood failure modes, playbooks documented for novel failure investigation, on-call rotation includes staff trained on this workload, load testing completed at expected peak traffic levels, rollback procedures fully tested, and a designated readiness review owner with sign-off authority. 

1.  **Customize the checklist per publisher workload theme:** Extend the standard checklist with workload-specific requirements. Prebid adapter additions: timeout threshold configuration, bid response validation, yield baseline metrics captured. SGAI additions: full-pipeline validation, SCTE-35 validation active, CDN cacheability verified. FAST channel additions: multi-AZ MediaLive configuration, EPG completeness validation, live event load testing. 

1.  **Assign a readiness review owner for each launch:** Name a specific individual (not a team) as the readiness review owner who is Responsible for verifying all checklist items and Accountable for the sign-off decision. This owner must have the authority to block activation if checklist items are incomplete. Document the owner's name in the launch planning record alongside the expected activation date. 

1.  **Conduct load testing at expected peak levels:** For FAST channel launches, run load tests at 150% of expected peak concurrent viewer count. For Prebid Server launches with a new SSP adapter, run synthetic auction traffic at 2x the expected adapter bid rate for 30 minutes. Validate that all monitoring dashboards accurately reflect workload behavior under load and that no unexpected alerts fire during the load test. 

1.  **Execute a rollback dry-run and require formal sign-off:** Before activation, execute a full rollback dry-run: deploy the workload to production, then trigger the rollback procedure, verifying that traffic reverts to the pre-launch state within the target time. Obtain formal written sign-off from the readiness review owner only after all checklist items are verified including the rollback dry-run. Document the sign-off with timestamp in the launch record. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [ADVOPS03-BP01 Mitigate deployment risks for publisher workload changes](advops03-bp01.md) 
+  [ADVOPS04-BP01 Create runbooks for the most common operational events and incidents that can impact your advertising workload](advops04-bp01.md) 

 **Related documents:** 
+  [AWS Well-Architected Operational Readiness Review (ORR) process](https://docs.aws.amazon.com/wellarchitected/latest/operational-readiness-reviews/wa-operational-readiness-reviews.html) 
+  [AWS Systems Manager runbook authoring documentation](https://docs.aws.amazon.com/systems-manager/latest/userguide/automation-documents.html) 

 **Related services:** 
+  [AWS Systems Manager](https://aws.amazon.com/systems-manager/) 
+  [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) 