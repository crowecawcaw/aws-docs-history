

# Compliance baselining and automation
<a name="dsops02"></a>

 Compliance requirements accumulate from multiple sources: cybersecurity directives, privacy legislation, industry regulations, and internal policies. Even within a single jurisdiction these requirements can overlap or diverge, and the overlap grows as jurisdictions are added. Without a structured compliance catalog, teams can't determine which controls apply to their workloads or verify that those controls are implemented correctly. 

 This capability covers building a compliance catalog that maps requirements to technical controls, and codifying those controls as policy as code with automated validation embedded in deployment pipelines. 


|  DSOPS02: How do you baseline and automate sovereignty compliance?  | 
| --- | 
| [DSOPS02-BP01 Baseline your compliance requirements](dsops02-bp01.md) | 
| [DSOPS02-BP02 Establish an automated path to compliance](dsops02-bp02.md) | 

## Capability intent
<a name="capability-intent-1"></a>
+  Compliance requirements from all applicable sources are cataloged and mapped to specific technical controls, validation criteria, and evidence requirements. 
+  Controls are codified as policy as code and enforced through automated mechanisms rather than relying on manual implementation and review. 
+  Deployment pipelines validate compliance before resources reach production, blocking noncompliant configurations at the source. 
+  The compliance catalog serves as a single reference for which requirements apply to which workloads in which jurisdictions, eliminating ambiguity for implementation teams. 
+  Baseline updates propagate automatically to affected workloads and accounts when requirements change, without requiring manual redeployment. 

## Maturity levels
<a name="maturity-levels-1"></a>

 These levels summarize what each stage of maturity looks like for this capability as a whole. 


|  Level  |  Name  |  What it looks like  | 
| --- | --- | --- | 
|  1  |  Initial  |  Compliance requirements are tracked in spreadsheets or documents without systematic mapping to technical controls. Implementation depends on individual team interpretation. Validation is manual.  | 
|  2  |  Emerging  |  A compliance catalog exists mapping some requirements to controls. Policy as code is partially implemented for high-priority requirements. Automated validation covers some resources but isn't integrated into deployment pipelines.  | 
|  3  |  Defined  |  The compliance catalog comprehensively maps requirements to technical controls with validation criteria. Policy as code enforces compliance baselines across accounts. Deployment pipelines include automated compliance gates that block noncompliant resources.  | 
|  4  |  Proactive  |  Compliance baselines are versioned and changes propagate automatically. Pipeline validation covers edge cases such as cross-account dependencies and cross-Region configurations. Exceptions are tracked with time-bound expiration and audit justification.  | 
|  5  |  Optimized  |  Compliance automation achieves near-zero false positives through continuous tuning. Baseline updates are deployed and validated across all accounts within defined timeframes. Policy as code is shared across jurisdictions as reusable modules, reducing duplication.  | 

## Common issues to watch for
<a name="common-issues-to-watch-for-1"></a>
+  Compliance catalogs that map requirements to controls at an abstract level without specifying validation criteria, which makes it impossible to automate verification or confirm control effectiveness. 
+  Policy as code that enforces a single baseline across all jurisdictions and misses requirements that differ between regulatory frameworks operating in the same environment. 
+  Deployment pipelines with compliance gates that can be bypassed through alternative deployment paths (the console or direct API calls), which creates resources that avoid automated validation. 
+  Exceptions granted without expiration dates or justification records, which accumulate over time and erode the baseline without visibility into the cumulative drift. 
+  Compliance baselines that are updated centrally but require manual redeployment to affected accounts, leading to compliance drift. 