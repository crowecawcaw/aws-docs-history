

# Manage the lifecycle of resources

 Cloud resources are quick to create and easy to forget, and each one costs money until someone retires it. Managing the resource lifecycle keeps the estate matched to what the business uses, from provisioning through decommissioning. This capability covers tracking resources against their purpose and expected end date, adjusting and retiring them as demand changes, and enforcing retention rules on the data they leave behind. 

 Lifecycle management matters more as a workload scales, because manual cleanup does not keep pace with resources that automation creates, replicates, and clones. Systematic tracking, scheduled review, and automated retention turn cleanup into an ongoing routine, so spend follows business value. 


|  COST03: How do you manage the lifecycle of your resources?  | 
| --- | 
|  [COST03-BP01 Track resources over their lifetime](cost03-bp01.md)  | 
|  [COST03-BP02 Implement efficient resource lifecycle management](cost03-bp02.md)  | 
|  [COST03-BP03 Enforce data retention policies](cost03-bp03.md)  | 

## Capability intent
<a name="cost03-intent"></a>
+  Every resource carries current context for its purpose, owner, environment, and expected end date, so retirement is a decision based on data rather than investigation. 
+  Utilization is monitored across the estate, so idle and underutilized resources surface without manual inspection, including the resources that automation provisions. 
+  Provisioned capacity tracks real demand through automated scaling, and workloads are designed to tolerate resources appearing and disappearing as a normal event. 
+  Obsolete resources are removed through a standardized, low-risk decommissioning process that verifies the resource is unused, preserves what is needed to recreate it, and applies a cooling-off period before deletion. 
+  Data retention runs on automated policies set per data class, so aging data moves to cheaper storage or is deleted on schedule while compliance and recovery requirements are still met. 

## Common issues to watch for
<a name="cost03-issues"></a>
+  Tracking is applied only to production, so untracked development, test, and temporary resources become the largest source of waste and never surface for cleanup. 
+  Resource metadata records what a resource is but not when it should be retired, so every retirement decision requires investigation that rarely happens. 
+  Capacity is provisioned for peak demand and left running, so the workload pays for idle resources during the long stretches when demand is low. 
+  Architecture assumes resources are permanent, so decommissioning breaks dependent components and teams grow reluctant to remove anything. 
+  Review effort is spread evenly across accounts regardless of spend, so time meant to save money is consumed on accounts that cost a few dollars a month. 
+  Retention is enforced on object storage but ignored for database snapshots, backups, and logs, so forgotten data in other stores accumulates for years. 