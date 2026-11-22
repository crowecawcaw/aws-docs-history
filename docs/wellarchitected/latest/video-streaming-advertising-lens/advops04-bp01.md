

# ADVOPS04-BP01 Create runbooks for the most common operational events and incidents that can impact your advertising workload

 Develop structured procedures to manage operational events and incidents in your advertising workloads. Runbooks provide step-by-step procedures for well-understood, routine operations, while playbooks guide your response to incidents with less predictable outcomes. For a publisher workload, runbooks cover Prebid adapter timeout escalation, SGAI manifest errors, FAST channel outages, converged linear and digital incident scenarios, and infrastructure capacity events ahead of high-traffic advertising moments. 

 **Desired outcome:** 
+  Publisher-specific runbooks exist for all well-understood failure modes, and playbooks exist for investigation of novel or intermittent failure patterns. 
+  All runbooks and playbooks are tested through quarterly exercises and maintained through version-controlled documentation. 
+  Separate repositories for linear NOC and digital ad ops are replaced by shared procedures for converged failure scenarios. 
+  Capacity runbooks cover predictable high-traffic advertising events such as holiday campaigns, tentpole product launches, and live sports, so scaling actions and on-demand capacity requests follow documented procedures rather than ad-hoc response. 

 **Common anti-patterns:** 
+  Maintaining only generic infrastructure runbooks without publisher-specific procedures for adapter, manifest, or playout failures. 
+  Not distinguishing between runbooks (step-by-step procedures for known resolution) and playbooks (investigation guides containing hypotheses and decision trees for diagnosis). 
+  Allowing runbooks to become stale without regular review and game day validation. 
+  Maintaining separate runbook repositories for linear NOC and digital ad ops with no shared procedures for converged failure scenarios. 
+  Treating predictable high-traffic advertising events as unplanned capacity incidents instead of maintaining pre-authored capacity runbooks for on-demand capacity reservations and scaling. 

 **Benefits of establishing this best practice:** 
+  Reduced MTTR for publisher-specific incidents through pre-documented response procedures. 
+  Consistent incident response quality regardless of which on-call staff member responds. 
+  Proactive identification of procedure gaps through regular review exercises. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance"></a>

 Runbooks contain one or more steps that run in sequential order, and each step performs a single action. A later step can use the output from an earlier step. Use runbooks for well-understood, routine operations where the resolution path is known. 

 Publisher-specific runbooks that are commonly missing from standard ad tech operations: 
+  **Prebid Server runbooks:** Adapter timeout escalation (when an adapter's timeout rate spikes, what specific steps determine whether the issue is in the adapter configuration, the demand partner's infrastructure, or the network path), auction failure triage (when the Prebid auction itself fails rather than individual adapters), and adapter onboarding validation (the checklist to run when a new adapter goes live and initial metrics are unexpected). 
+  **SGAI runbooks:** Manifest generation errors (how to isolate whether the error is in the SCTE-35 marker generation, the manifest templating, or the CDN distribution layer), SCTE-35 marker validation failures by message type (spliceinsert, timesignal, splicenull, and privatecommand each have distinct failure modes requiring different diagnostic steps), and AWS Elemental MediaTailor integration health degradation. 
+  **FAST channel runbooks:** Channel outage response (the sequence of steps to restore playout with minimum dead air), playout quality degradation playbook (hypothesis tree for diagnosing intermittent issues that don't appear as hard failures in infrastructure metrics), and content gap detection and remediation. 
+  **Converged linear and digital runbooks:** SSAI and DAI stitch failures affecting both linear simulcast and streaming delivery, signal/encoder failures affecting downstream ad insertion chains, and campaign under-delivery requiring redistribution across linear and digital inventory. 
+  **Infrastructure capacity runbooks:** One runbook requests On-Demand Capacity Reservations (ODCRs) ahead of anticipated high-traffic advertising events such as holiday campaigns, tentpole product launches, and live sports. Another runbook scales resources to traffic patterns with Amazon EC2 Auto Scaling, using predictive scaling for cyclical campaign demand and scheduled scaling for planned events, behind Elastic Load Balancing across healthy instances. A third runbook defines the CloudWatch alarms and monitoring thresholds that trigger each capacity procedure so capacity is provisioned before demand arrives rather than after saturation. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Inventory publisher failure modes and high-traffic capacity events, and classify each as runbook or playbook:** Catalog known failure modes across Prebid adapter timeout, auction failure, SGAI manifest errors, SCTE-35 validation failures, player-side ad fetch timeouts, FAST channel outage, playout quality degradation, scheduling gaps, and innovative ad format rendering failures, plus predictable high-traffic capacity events (anticipated campaign peaks and scheduled launches that require pre-provisioned capacity). Classify each as runbook-appropriate (known resolution path) or playbook-appropriate (requires investigation). This inventory becomes the gap analysis against your current documentation. 

1.  **Author step-by-step runbooks for well-understood failure modes:** Write runbooks for each runbook-appropriate failure mode with numbered sequential steps, each step containing exactly one action, with clear expected outputs. Include specific SCTE-35 message type diagnostics for SGAI runbooks (different validation steps for spliceinsert compared to timesignal compared to splicenull failures), and specific capacity procedures for high-traffic events (ODCR request steps and scaling-policy adjustments). Include specific CloudWatch query strings, AWS CLI commands, and service console navigation paths. Runbooks should be executable by an on-call engineer who has never seen this specific failure before. 

1.  **Author investigation playbooks for novel failure patterns:** Create playbooks for failure patterns where root cause isn't immediately apparent. Structure each playbook as: observable symptoms (what the responder is seeing in dashboards and alerts), hypothesis list (ranked by probability based on historical incidents), diagnostic steps per hypothesis (what to check to confirm or rule out each hypothesis), decision points (if hypothesis A is confirmed, go to runbook X, and if all hypotheses are ruled out, escalate to tier 2), and escalation criteria. 

1.  **Store runbooks and playbooks in version-controlled repositories:** Migrate all runbooks and playbooks from wiki pages or shared drives to a Git repository with change tracking and review approval workflows. Require pull request review for all runbook changes. Changes to production runbooks are as consequential as changes to production code. Add automated testing for runbooks that include AWS CLI commands (syntax validation at minimum, full testing in staging where feasible). 

1.  **Schedule quarterly review exercises and post-incident updates:** Run quarterly game day exercises that simulate major failure scenarios for each publisher workload type, then update runbooks and playbooks based on gaps discovered. Conduct post-incident analysis asking whether you could improve time to detection, whether metrics and alarms need updates, and whether runbook or playbook steps could be added or improved. Track the completion rate for these improvement actions as a measure of how well the process is working. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [ADVOPS04-BP02 Automate runbooks to gain operational efficiency](advops04-bp02.md) 

 **Related documents:** 
+  [OPS07-BP03 Use runbooks to perform procedures](https://docs.aws.amazon.com/wellarchitected/latest/operational-excellence-pillar/ops_resp_to_ops_plan.html) 
+  [AWS Systems Manager runbook authoring documentation](https://docs.aws.amazon.com/systems-manager/latest/userguide/automation-documents.html) 
+  [AWS Elemental MediaTailor operational guides](https://docs.aws.amazon.com/mediatailor/latest/ug/what-is-mta.html) 
+  [Amazon EC2 Auto Scaling user guide](https://docs.aws.amazon.com/autoscaling/ec2/userguide/what-is-amazon-ec2-auto-scaling.html) 
+  [On-Demand Capacity Reservations](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-capacity-reservations.html) 

 **Related services:** 
+  [AWS Systems Manager](https://aws.amazon.com/systems-manager/) 
+  [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) 
+  [Amazon EC2 Auto Scaling](https://aws.amazon.com/ec2/autoscaling/) 
+  [Elastic Load Balancing](https://aws.amazon.com/elasticloadbalancing/) 