

# Central observability management

 Observability gives teams a shared, reliable view of how the cloud environment is behaving. As workloads spread across more accounts and Regions, visibility fragments unless it is standardized and centralized. This capability covers the best practices for defining organization-wide observability standards and for aggregating telemetry into a common place where teams can use it. 


|  FND03: How do you establish consistent, centralized observability into your cloud resources across all accounts and Regions?  | 
| --- | 
|  [FND03-BP01 Define observability standards and policies](fnd03-bp01.md)  | 
|  [FND03-BP02 Establish central, cross-account observability capabilities](fnd03-bp02.md)  | 
|  [FND03-BP03 Establish centralized event monitoring and response](fnd03-bp03.md)  | 

## Capability intent
<a name="fnd03-intent"></a>
+  Observability is treated as a foundation capability with clear ownership, documented standards, and named accountability for telemetry quality across the organization. 
+  Foundation components and workloads are instrumented to a common baseline, so logs, metrics, and traces can be correlated across accounts and Regions without retrofitting. 
+  Telemetry from every account is available through a shared cross-account view that foundation, workload, and security teams operate from during incidents and normal operations. 
+  AWS Health events from every account are aggregated into a single organization-wide view and routed through automation, so service issues and scheduled changes reach the teams that own the affected resources. 
+  Observability configuration travels with new accounts and workloads automatically through provisioning and deployment pipelines, rather than being set up by hand after the fact. 
+  Retention, cost, and the health of the observability system itself are managed deliberately, so visibility remains reliable and affordable as the environment grows. 

## Common issues to watch for
<a name="fnd03-issues"></a>
+  Observability standards exist only as wiki pages and rely on individual teams to apply them, leading to drift between accounts and telemetry that cannot be correlated when an incident spans workloads. 
+  Workloads are well instrumented while foundation components such as networking, identity, and shared security services are not, so incidents in the foundation are diagnosed by guesswork rather than data. 
+  No single owner is accountable for telemetry quality end to end, so logs and metrics are produced but completeness, formatting, and retention silently decay over time. 
+  New accounts are onboarded into central observability manually, which leaves visibility gaps in the early life of a workload and quietly becomes the norm as the estate grows. 
+  Retention and sampling are set by default rather than by operational need, producing storage bills that surprise finance teams or data that is already gone when an investigator reaches for it. 
+  The central observability system is itself unmonitored, so broken cross-account links, ingestion throttling, and dashboard failures are discovered only when someone tries to use the data and finds it missing. 
+  AWS Health events are watched per account rather than aggregated, so organization-wide service issues and scheduled changes such as resource retirements and certificate expirations are noticed inconsistently or only after they cause impact. 