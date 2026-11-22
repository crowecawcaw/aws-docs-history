

# ADVOPS04-BP02 Automate runbooks to gain operational efficiency

 Document runbooks for failover, capacity scaling, and incident response workflows, then encode them as executable automation documents. For publisher workloads, automate high-frequency responses including adapter failover, SGAI manifest regeneration, FAST channel content gap remediation, and ad pod backfill. 

 **Desired outcome:** 
+  High-frequency, well-understood publisher operational responses are automated with guardrails that help avoid cascading failures while reducing MTTR. 
+  Each automated runbook includes rate control limits, error count thresholds for automation halt, and automated rollback triggers. 
+  Automation effectiveness is measured by comparing MTTR and revenue impact for automated compared to manual resolutions of the same incident types. 

 **Common anti-patterns:** 
+  Automating publisher runbooks without guardrails (rate control, error thresholds), risking cascading failures when automation acts on false positives, for example, automatically removing multiple adapters simultaneously during a brief false-positive alarm spike. 
+  Automating only infrastructure-level responses without publisher-specific yield-aware automation. 
+  Not measuring automation effectiveness against manual response baselines, making it impossible to demonstrate ROI from automation investment. 

 **Benefits of establishing this best practice:** 
+  Reduced MTTR for high-frequency publisher incidents through automated response. 
+  Consistent execution quality reducing human error during incident response. 
+  Freed engineering capacity from repetitive manual interventions enabling focus on improvement initiatives. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance"></a>

 Use AWS Systems Manager Automation to convert manual runbooks into executable workflows. Automated responses cut MTTR and revenue impact during off-hours incidents, when engineers otherwise log in, navigate consoles, and run commands manually. 

 The following patterns result in the highest impact: 
+  **Automatic adapter failover:** When a Prebid adapter's response latency exceeds threshold (indicating a demand partner issue), automatically reduce the adapter's request share or remove it from active auctions. A rate limit of one adapter removal per 15-minute window prevents removing too much demand capacity when multiple adapters show transient issues. Without this guardrail, a false-positive alarm spike might trigger removing multiple adapters, causing a yield crash worse than the original adapter issue. 
+  **Automated SGAI manifest regeneration:** When SCTE-35 validation failures exceed a threshold, automatically trigger manifest regeneration for the affected channel with a simultaneous CDN cache purge for the corrupted content. A halt threshold on consecutive regeneration failures prevents regeneration loops. Without it, regenerating on every validation failure causes a storm of requests when the fault lies in the validation logic itself. 
+  **Automated FAST channel content gap remediation:** When pre-flight validation detects upcoming content gaps, automatically insert fallback content from the slate pool. Use this for gaps discovered more than 30 minutes before playout. For gaps discovered within 30 minutes, trigger automated notification to the scheduling team while inserting slate to avoid dead air. 
+  **Automatic ad pod backfill:** When primary demand sources fail to fill ad pods above a minimum threshold, automatically trigger backfill requests to secondary demand sources. A yield floor prevents backfill from accepting impressions at CPMs that damage publisher floor rates. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Prioritize publisher runbooks for automation based on frequency and revenue impact:** Rank all runbook-documented failure modes by: frequency of occurrence per month, average MTTR under manual response, revenue impact per minute of extended MTTR, and consistency of resolution steps. Start automation with the highest-frequency, highest-revenue-impact failures where resolution steps are deterministic. Document the prioritization rationale for future review. 

1.  **Implement automated Prebid adapter failover with rate control guardrails:** Create an AWS Systems Manager Automation document that: (1) verifies the adapter timeout rate threshold has been exceeded for 5\+ consecutive minutes (avoids transient spikes triggering automation), (2) reduces the adapter's bid request share by 50%, (3) logs the action with a timestamp and current metrics to CloudWatch, (4) waits 15 minutes before evaluating whether full removal is warranted. Configure a rate control parameter that limits the document to one adapter modification per 15-minute window across all invocations. 

1.  **Implement automated SGAI manifest regeneration with CDN cache purge:** Create an SSM Automation document triggered by CloudWatch Alarm (SCTE-35 validation failure rate exceeding threshold) that: (1) regenerates manifests for the affected channel, (2) initiates CloudFront cache invalidation for affected manifest paths, (3) validates the regenerated manifests pass SCTE-35 schema validation before CDN distribution, (4) increments an error counter and halts if regeneration fails 3 consecutive times (avoiding regeneration loops). 

1.  **Configure automated rollback triggers for all automated runbooks:** For each automated runbook, define post-action validation checks: after adapter failover, verify that the remaining adapter set maintains fill rate above the threshold. After manifest regeneration, verify that ad break completion rate improves within 5 minutes. If post-action metrics don't improve, automatically revert the automation's action and escalate to the on-call engineer. By validating after each action and reverting when metrics stall, you keep automation from making the situation worse. 

1.  **Measure automation effectiveness monthly:** Compare MTTR, revenue impact, and execution success rates for automated compared to manual resolutions of the same incident types. Calculate the percentage of applicable incidents resolved by automation compared to escalated to human. Set quarterly targets for automation coverage growth and MTTR reduction. Report automation effectiveness metrics alongside workload health metrics in the monthly operational review. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [ADVOPS04-BP01 Create runbooks for the most common operational events and incidents that can impact your advertising workload](advops04-bp01.md) 

 **Related documents:** 
+  [AWS Systems Manager Automation documentation](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-automation.html) 
+  [AWS Fault Injection Service for automation validation testing](https://aws.amazon.com/fis/) 

 **Related services:** 
+  [AWS Systems Manager](https://aws.amazon.com/systems-manager/) 
+  [AWS Lambda](https://aws.amazon.com/lambda/) 
+  [AWS Step Functions](https://aws.amazon.com/step-functions/) 