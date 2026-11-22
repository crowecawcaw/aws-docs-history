

# Plan for Disaster Recovery (DR)

 Backups and redundant workload components are where disaster recovery starts, not where it ends. A disaster recovery plan sets how fast a workload returns to service and how much data it can afford to lose, then puts the strategy, testing, and automation in place to hit those targets. [RTO and RPO](rel-availability-and-recovery-objectives.md) are the objectives that anchor the plan, set from business need rather than technical convenience. Availability and disaster recovery share practices such as monitoring for failures, deploying to multiple locations, and automatic failover, but availability works on the components of a workload while disaster recovery works with discrete copies of the whole workload and measures success by time to recover after a disaster. 

 This capability covers how an organization plans for disaster recovery across a workload's life: setting recovery objectives from business impact, choosing a recovery strategy that meets them at a cost the business accepts, testing failover under realistic conditions, keeping the recovery site in parity with the primary, and automating recovery so it runs reliably when an incident hits. 


|  REL13: How do you plan for disaster recovery (DR)?  | 
| --- | 
|  [REL13-BP01 Define recovery objectives for downtime and data loss](rel13-bp01.md)  | 
|  [REL13-BP02 Use defined recovery strategies to meet the recovery objectives](rel13-bp02.md)  | 
|  [REL13-BP03 Test disaster recovery implementation to validate the implementation](rel13-bp03.md)  | 
|  [REL13-BP04 Manage configuration drift at the DR site or Region](rel13-bp04.md)  | 
|  [REL13-BP05 Automate recovery](rel13-bp05.md)  | 

## Capability intent
<a name="rel13-intent"></a>
+  Every workload has a recovery time objective and a recovery point objective, derived from business impact and validated against regulatory and contractual obligations. 
+  Each workload has a defined, implemented recovery strategy that meets its objectives at a cost the business accepts. 
+  Failover to the recovery site is tested on a regular schedule, including in production, and confirmed against the target RTO and RPO. 
+  The recovery site stays in parity with the primary, with configuration drift and replication problems detected before an incident rather than during one. 
+  Recovery runs from tested automation where the risk is low, with human judgment reserved for the failures that need it and an abort control always available. 

## Common issues to watch for
<a name="rel13-issues"></a>
+  Teams set recovery objectives with no link to business impact, so recovery investment is either too little to protect the business or more than the workload needs. 
+  A workload has no recovery strategy defined in advance, so failover is improvised during the incident itself. 
+  The recovery path is never exercised in production, and untested assumptions about capacity, permissions, and timing surface only when the primary fails. 
+  Changes land on the primary but not the recovery site, and the drift stays invisible until a failover exposes it. 
+  Recovery depends on control plane operations or on services in the failing site, so the same event that caused the failure also disables the recovery. 
+  Recovery automation has no abort control, so a misbehaving procedure cannot be stopped once it starts. 