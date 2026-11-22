

# ADVOPS04-BP03 Monitor and manage the health of publisher operations processes

 Beyond workload health, track the health of operational processes: incident response efficiency, runbook execution accuracy, and on-call rotation effectiveness. 

 **Desired outcome:** 
+  Publisher teams track operational process KPIs (MTTD and MTTR for incidents that affect yield, runbook execution success rate, on-call escalation frequency) alongside workload metrics. 
+  Monthly retrospectives identify systemic patterns and set quarterly improvement targets. 
+  Automation coverage percentage is tracked and growing, with a defined target for the fraction of applicable incidents resolved without human intervention. 

 **Common anti-patterns:** 
+  Tracking only workload metrics without measuring operational process effectiveness, creating a blind spot where systemic process failures (consistently slow incident detection, ineffective runbooks, undertrained on-call staff) compound revenue losses without being identified. 
+  Never reviewing runbook execution success rates, missing the signal that a runbook is consistently failing to resolve the incidents it is supposed to address. 
+  Lacking on-call retrospectives that would surface patterns in escalation frequency and duration. 

 **Benefits of establishing this best practice:** 
+  Visibility into systemic process failures. 
+  Data-driven improvement of incident response. 
+  Measurable automation coverage growth tied to revenue impact. 

 **Level of risk exposed if this best practice is not established:** Medium 

## Implementation guidance
<a name="implementation-guidance"></a>

 Many publisher operations teams focus exclusively on workload metrics (eCPM, fill rates, ad break completion) without measuring the effectiveness of the operational processes that respond to workload anomalies. This creates a problem where systemic process failures (such as slow incident detection or undertrained on-call staff) compound revenue losses over time without being identified or addressed. 

 The key process metrics to track: 
+  **MTTD (Mean Time to Detect):** From yield degradation onset to first alarm or detection. Measured per incident from CloudWatch alarm trigger timestamps against the actual onset time identified in post-incident analysis. High MTTD indicates insufficient monitoring coverage or alarm threshold misconfiguration. 
+  **MTTR (Mean Time to Resolve):** From incident declaration to resolution. Measured from incident management system records. High MTTR per incident type indicates runbook gaps, automation opportunities, or knowledge deficiencies in the on-call rotation. 
+  **Runbook execution success rate:** Percentage of runbook executions that resolve the issue without escalation. Low success rate for a specific runbook indicates the runbook needs updating: the steps are incorrect, incomplete, or the issue has evolved. 
+  **Automation coverage:** Percentage of applicable incidents resolved by automated runbooks compared to manual intervention. Track by incident type category. 
+  **On-call escalation frequency:** Number of escalations from tier-1 to tier-2 per rotation period. High escalation frequency indicates insufficient tier-1 training or runbook gaps that limit tier-1 resolution. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Define operational process KPIs and instrument incident workflows:** Define the specific KPIs: MTTD per incident category, MTTR per incident category, runbook execution success rate per runbook, automation coverage percentage by incident type, and on-call escalation frequency per rotation period. Instrument your incident management workflows to automatically capture detection timestamp, runbook invoked, resolution timestamp, escalation events, and resolution method (automated compared to manual). 

1.  **Build operational health dashboards:** Create CloudWatch dashboards displaying process KPIs alongside workload health metrics. Include trend lines showing MTTD and MTTR over the past 13 weeks, runbook success rates per runbook (with the lowest-performing runbooks highlighted), automation coverage percentage with a trend line and target, and escalation frequency per on-call rotation period. Make these dashboards accessible to both engineering and ad operations leadership. 

1.  **Establish monthly on-call retrospectives:** Schedule monthly retrospectives where on-call engineers review the period's incidents, runbook invocations, escalations, and automation outcomes. Structure the retrospective to identify: systemic patterns in MTTD (are there incident types where detection consistently lags onset?), runbooks with low success rates (are there runbooks that are consistently escalated after invocation?), and automation candidates (high-frequency, low-complexity incidents still requiring manual response). 

1.  **Set quarterly improvement targets:** At the start of each quarter, set specific improvement targets based on retrospective findings: "Reduce MTTR for SGAI manifest errors from 22 minutes to 12 minutes by automating manifest regeneration," "Increase automation coverage for Prebid adapter failures from 40% to 70% by adding two new automated runbooks," "Improve MTTD for fill rate drops by adding anomaly detection to three additional metrics." Track progress against targets in the monthly retrospective and report quarterly results to leadership. 

1.  **Report automation effectiveness alongside workload metrics:** Include automation coverage percentage, MTTD trend, and MTTR trend in the same operational health report that covers eCPM, fill rate, and ad break completion. This treats operational process health as a primary concern alongside revenue metrics and reinforces the view that operational efficiency drives revenue directly. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [ADVOPS07-BP04 Conduct post-incident reviews for revenue-affecting events](advops07-bp04.md) 

 **Related documents:** 
+  [AWS Well-Architected OE pillar OPS09-BP01 guidance on operational KPIs](https://docs.aws.amazon.com/wellarchitected/latest/operational-excellence-pillar/ops_workload_observability_eval_internal_customers.html) 

 **Related services:** 
+  [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) 
+  [Quick](https://aws.amazon.com/quicksight/) 