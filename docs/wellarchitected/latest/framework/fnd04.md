

# Resource and inventory management

 Clear visibility and control over cloud resources is essential for running an efficient and compliant environment at scale. This capability covers the best practices for standardized attribution, organization-wide inventory and dependency views, central repositories of shared patterns, patch management, service quota management, and the resilience foundations — centralized backup, cross-Region replication and failover, and resilience testing — that protect the resources workloads depend on. Together these give teams the metadata, discoverability, reusable building blocks, and recovery capabilities they need to move fast without creating drift or losing data during the events that matter most. 


|  FND04: How do you maintain visibility, control, and governance over resources, configurations, and assets across accounts and Regions?  | 
| --- | 
|  [FND04-BP01 Implement standardized attribution policies](fnd04-bp01.md)  | 
|  [FND04-BP02 Establish an organization view of cloud inventory and dependencies](fnd04-bp02.md)  | 
|  [FND04-BP03 Establish standard repositories of shared resources and patterns](fnd04-bp03.md)  | 
|  [FND04-BP04 Implement mechanisms for patch management](fnd04-bp04.md)  | 
|  [FND04-BP05 Establish service quota management](fnd04-bp05.md)  | 
|  [FND04-BP06 Establish centralized backup standards and mechanisms](fnd04-bp06.md)  | 
|  [FND04-BP07 Establish cross-Region replication and failover capabilities](fnd04-bp07.md)  | 
|  [FND04-BP08 Establish resilience testing tooling](fnd04-bp08.md)  | 

## Capability intent
<a name="fnd04-intent"></a>
+  The organization has an authoritative, continuously maintained view of what exists in the cloud, who owns it, and how resources depend on each other, without relying on manual collection or point-in-time snapshots. 
+  Common infrastructure is consumed from curated, versioned, security-vetted building blocks rather than rebuilt by each team, so the secure and compliant path is also the easiest path. 
+  Resources stay healthy and within their operating envelope over time, with patching, configuration compliance, and service quota headroom managed as foundation concerns rather than workload-by-workload ones. 
+  Recovery and cross-Region resilience are provided as shared foundation services — isolated backups, standard replication patterns, multi-Region shared services, and coordinated failover — so workload teams inherit a working recovery path instead of designing one from scratch. 
+  Recovery and resilience claims are validated by exercise rather than by assertion, with restores, failovers, and fault-injection experiments run on a regular cadence and their findings fed back into the shared patterns. 
+  Attribution, inventory, and usage data feed cost, security, capacity, and architectural decisions, so the capability informs how the organization operates rather than sitting as a governance artefact. 

## Common issues to watch for
<a name="fnd04-issues"></a>
+  Inventory built from periodic exports or spreadsheets and tagging applied by convention rather than enforced at provisioning, so the data describing the environment is stale or inconsistent by the time anyone tries to use it for cost, security, or change decisions. 
+  Shared catalogues and patterns that are hard to discover, poorly documented, or too rigid to fit real use cases, so teams quietly build their own alternatives and the central standard erodes into a parallel set of team-specific implementations. 
+  Patch management scoped narrowly to long-running EC2 and ignoring container images, AMIs in use, hybrid nodes, and serverless runtimes, or with no expedited path for zero-days, so critical vulnerabilities sit unpatched until the next scheduled maintenance window. 
+  Service quotas treated as a per-account concern and surfaced only during incidents, with disaster recovery Regions sized for resting load rather than failover load, so workloads cannot scale when they need to and failovers fail because the target Region cannot absorb production traffic. 
+  Backups configured per workload and stored in the same account or Region as the data they protect, without vault lock or restore exercises, so unauthorized access at the account level or a ransomware event takes the recovery path with it and the first real restore is the one that has to work. 
+  Cross-Region and resilience designs asserted on paper but never exercised, with shared services that exist only in the primary Region and fault-injection experiments that are aspirational rather than scheduled, so the first real failure is the first real test of whether the recovery path actually works. 