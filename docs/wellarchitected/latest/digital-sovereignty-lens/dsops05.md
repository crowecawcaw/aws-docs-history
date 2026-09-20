

# Compliance remediation
<a name="dsops05"></a>

 Detecting a compliance finding accomplishes nothing until someone remediates it. When a finding appears, regional teams need to investigate root causes and apply fixes independently, without waiting for a central team to triage and respond. Good remediation gives those teams jurisdiction-scoped access to findings, a standardized root cause analysis process, pre-approved runbooks, and automated fixes that keep audit trails. 

 This capability covers the investigation, root cause analysis, and remediation of compliance findings. It emphasizes letting regional teams act independently and automating remediation where possible. 


|  DSOPS05: How do you remediate non-compliance?  | 
| --- | 
| [DSOPS05-BP01 Enable independent root cause analysis and remediation](dsops05-bp01.md) | 
| [DSOPS05-BP02 Automate compliance remediation](dsops05-bp02.md) | 

## Capability intent
<a name="capability-intent-4"></a>
+  Regional teams can investigate and remediate compliance findings within their jurisdiction independently, without waiting for a central team in another jurisdiction. 
+  Root cause analysis follows a standardized process that identifies systemic issues rather than treating each finding as an isolated event. 
+  Pre-approved remediation runbooks provide consistent, auditable procedures that regional teams can execute within their authority. 
+  Automated remediation handles known finding types with consistent fixes, traceable to the regulatory requirement each fix addresses. 
+  Remediation effectiveness is measured (time-to-remediate and recurrence rate) and feeds back into control design and prevention mechanisms. 

## Maturity levels
<a name="maturity-levels-4"></a>

 These levels summarize what each stage of maturity looks like for this capability as a whole. 


|  Level  |  Name  |  What it looks like  | 
| --- | --- | --- | 
|  1  |  Initial  |  Remediation is handled case by case and centralized. Regional teams submit tickets to a central team and wait for resolution. Root cause analysis is informal and inconsistent. Recurrence is common.  | 
|  2  |  Emerging  |  Some remediation runbooks exist for common findings. Regional teams have partial access to findings but limited authority to apply fixes. Automated remediation covers a small number of finding types.  | 
|  3  |  Defined  |  Regional teams have jurisdiction-scoped access to findings and pre-approved runbooks for known finding types. Root cause analysis follows a documented process. Automated remediation covers common findings with audit trails. Escalation paths are clear for findings outside runbook coverage.  | 
|  4  |  Proactive  |  Automated remediation covers the majority of common findings. Root cause analysis identifies systemic patterns and feeds improvements back into preventive controls. Remediation metrics (time-to-fix and recurrence rate) are tracked per jurisdiction.  | 
|  5  |  Optimized  |  Remediation is predominantly automated with human oversight for exceptions. Systemic root causes are addressed at the control level, reducing finding recurrence to near zero for known patterns. Remediation effectiveness benchmarks drive continuous improvement across jurisdictions.  | 

## Common issues to watch for
<a name="common-issues-to-watch-for-4"></a>
+  Regional teams can see findings but lack the authority or tooling to remediate them. That creates a dependency on central teams, which delays resolution and lets compliance debt pile up. 
+  Remediation is applied to individual findings without root cause analysis, so the same type of noncompliance keeps recurring across accounts and deployments. 
+  Automated remediation runs without sufficient guard rails and makes unintended changes, such as restricting access in a way that breaks legitimate workloads, which erodes trust in automation. 
+  Audit trails record what was changed but not why, which makes it hard to demonstrate regulatory alignment during audits. 
+  Escalation paths are unclear or untested, so regional teams have no recourse when findings fall outside their runbook coverage. 