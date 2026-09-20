

# Workload interoperability and portability
<a name="dsrel03"></a>

 A large-scale disruption can force an organization to move a workload to a different jurisdiction with little warning. Design decisions made during initial development determine whether that move is feasible within acceptable timelines or requires extensive rework. Jurisdictional portability depends on three things done in advance: abstracting Region-specific and service-specific dependencies, using open standards and portable data formats, and planning for data export and migration before conditions require it. 

 This capability covers workload design patterns that enable deployment, migration, and recovery across jurisdictions with minimal rework when conditions change. 


|  DSREL03: How do you design workloads for interoperability and portability across jurisdictions?  | 
| --- | 
| [DSREL03-BP01 Design workloads for greater interoperability and portability](dsrel03-bp01.md) | 

## Capability intent
<a name="capability-intent-2"></a>
+  Workloads abstract Region-specific and service-specific dependencies through configuration rather than hardcoded bindings, so they can be redeployed to a different jurisdiction without code changes. 
+  Data is stored in open, portable formats with documented schemas, and export mechanisms are validated before they are needed. 
+  Infrastructure is defined as code with parameterized Region and service selections, so deployment to a new jurisdiction is a configuration change rather than a redesign. 
+  Integration points use open standards and well-defined APIs so proprietary lock-in does not block jurisdictional movement. 
+  Migration timelines are estimated, tested, and documented for critical workloads, so decision-makers know what portability means in practice (hours, days, weeks) for their specific systems. 

## Maturity levels
<a name="maturity-levels-2"></a>

 These levels summarize what each stage of maturity looks like for this capability as a whole. 


|  Level  |  Name  |  What it looks like  | 
| --- | --- | --- | 
|  1  |  Initial  |  Workloads are built with hardcoded Region and service dependencies. Data formats are proprietary or undocumented. No export or migration planning has been done.  | 
|  2  |  Emerging  |  Some workloads use infrastructure as code with basic parameterization. Data export exists but has not been validated for completeness or portability. Migration timelines are estimated but not tested.  | 
|  3  |  Defined  |  Workloads abstract Region and service dependencies through configuration. Data is stored in portable formats with documented schemas. Export and migration procedures are documented and validated for critical workloads.  | 
|  4  |  Proactive  |  Portability is tested through cross-jurisdiction deployment exercises. Migration timelines are measured and meet defined objectives. Workload designs are reviewed against portability criteria before production deployment.  | 
|  5  |  Optimized  |  Portability is a standard design requirement for new workloads. Migration procedures are automated and run as part of regular operational exercises. Lessons from portability testing feed back into architecture standards.  | 

## Common issues to watch for
<a name="common-issues-to-watch-for-2"></a>
+  Hardcoded Region identifiers, service endpoints, or account references embedded in application code rather than externalized as configuration. Jurisdictional movement then requires a code change instead of a deployment change. 
+  Data stored in proprietary formats without documented export mechanisms. The resulting lock-in often surfaces only when migration is needed under time pressure. 
+  Portability claimed on the basis of infrastructure as code without testing an actual redeployment, which misses runtime dependencies and data migration that the code does not capture. 
+  Migration timelines estimated but never validated, which gives decision-makers inaccurate information about the feasibility and cost of jurisdictional movement. 
+  Open standards adopted for external interfaces but not for internal data storage. Portability then reaches only the API layer while the data layer stays locked in. 