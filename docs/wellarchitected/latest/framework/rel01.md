

# Manage service quotas and constraints

 Cloud services cap how many resources you can provision and how fast you can call operations. Service quotas, also called service limits, guard against provisioning more than you intend and protect shared services from abuse. Resource constraints are physical or design limits, such as the throughput of a network link or the maximum size of a message. Some quotas you can raise on request, others are fixed by the resource itself, and a workload that does not know which is which plans capacity on assumptions rather than facts. 

 This capability covers how an organization knows, monitors, and manages the quotas and constraints its workloads depend on: distinguishing adjustable quotas from fixed constraints, tracking usage across every account and Region, accommodating fixed quotas through architecture, automating quota management, and keeping enough headroom for a failover to succeed within the quotas that remain. 


|  REL01: How do you manage service quotas and constraints?  | 
| --- | 
|  [REL01-BP01 Aware of service quotas and constraints](rel01-bp01.md)  | 
|  [REL01-BP02 Manage service quotas across accounts and regions](rel01-bp02.md)  | 
|  [REL01-BP03 Accommodate fixed service quotas and constraints through architecture](rel01-bp03.md)  | 
|  [REL01-BP04 Monitor and manage quotas](rel01-bp04.md)  | 
|  [REL01-BP05 Automate quota management](rel01-bp05.md)  | 
|  [REL01-BP06 Verify that a sufficient gap exists between the current quotas and the maximum usage to accommodate failover](rel01-bp06.md)  | 

## Capability intent
<a name="rel01-intent"></a>
+  Every service a workload uses has its adjustable quotas and fixed constraints inventoried, per account and per Region. 
+  Usage is tracked against each quota, with alerts that reach the right team while there is still time to request and receive an increase. 
+  Fixed constraints are identified during design and accommodated through architecture, rather than discovered when the workload reaches them at scale. 
+  Quotas are reconciled across accounts and Regions, so a secondary location holds enough capacity to run peak load after a failover. 
+  Quota monitoring and increase requests are automated where practical, and enough headroom is held that a zone or Region failure is absorbed within the quota. 

## Common issues to watch for
<a name="rel01-issues"></a>
+  Teams treat a fixed constraint as if it were negotiable, so a design reaches a ceiling it cannot raise and has no path forward at scale. 
+  Quotas are set in the primary Region only, so a failover Region sits at default quotas and cannot absorb the load it inherits. 
+  Monitoring alerts at the quota rather than before it, leaving no time for an increase request that Support must review. 
+  An alert fires but no one owns the response, so the quota is reached anyway despite the warning. 
+  Failover planning forgets that inaccessible resources still count against a quota until they are terminated, so replacements cannot start. 
+  Quota tracking lives in spreadsheets that drift out of date as the workload grows across accounts and Regions. 