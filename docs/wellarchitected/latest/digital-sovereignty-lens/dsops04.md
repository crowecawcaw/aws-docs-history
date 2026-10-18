

# Compliance monitoring
<a name="dsops04"></a>

 Compliance status changes as resources are created, modified, and decommissioned. Without continuous visibility, organizations find compliance gaps only during audits or incidents. Good monitoring aggregates findings across accounts and jurisdictions, scores them by severity, and alerts teams when resources drift. It also scopes views by jurisdiction so regional teams and auditors can assess each jurisdiction on its own. 

 This capability covers the aggregation, scoring, alerting, and visualization of compliance status across jurisdictions to maintain continuous visibility into sovereignty posture. 


|  DSOPS04: How do you monitor your current compliance status?  | 
| --- | 
| [DSOPS04-BP01 Maintain continuous visibility of your compliance status](dsops04-bp01.md) | 

## Capability intent
<a name="capability-intent-3"></a>
+  Compliance findings are aggregated across accounts and scored by severity, so a single view of sovereignty posture shows what to respond to first. 
+  Alerts notify responsible teams when resources drift from compliance baselines, so teams can correct the drift before findings accumulate. 
+  Compliance status is scoped by jurisdiction, so regional teams and auditors can assess each jurisdiction independently without filtering irrelevant findings. 
+  Compliance metrics are tracked over time to demonstrate improvement trends and identify recurring issues that require systemic remediation. 
+  Monitoring covers both the controls themselves and the completeness of coverage, so it detects gaps where resources are not being evaluated. 

## Common issues to watch for
<a name="common-issues-to-watch-for-3"></a>
+  Findings from all jurisdictions land in a single view. Regional teams then have to filter out irrelevant findings, and jurisdiction-level assessment becomes impractical. 
+  Notifications do not carry information required to help with prioritization or do not reach the right target audience. 
+  Some resources, especially those provisioned manually operate outside of compliance visibility. 
+  Dashboards show point-in-time status without historical trends, which leaves teams unable to demonstrate improvement or spot systemic patterns. 