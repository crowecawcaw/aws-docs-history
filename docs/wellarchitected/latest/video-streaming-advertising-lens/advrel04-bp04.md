

# ADVREL04-BP04 Design your workloads to withstand failures of individual components

 Determine which components are in the critical path for real-time bidding, ad serving, and other revenue-critical functions. Identify AWS services that provide built-in fault tolerance within your workload's response time and RTO targets. Use cell-based architectures with resources spread across multiple Availability Zones to reduce the scope of disruptive events. 

 **Desired outcome:** 
+  Individual component failures (single EC2 instance, single queue, single database node, single cache node) don't cause auction failures. 
+  Cell-based architectures limit the scope of impact of failures to a defined portion of auction traffic. 
+  Static stability mechanisms enable the data plane to continue operating during control plane failures. 

 **Common anti-patterns:** 
+  Running critical auction-path components on a single instance, queue, database node, or cache node with no redundancy. 
+  Deploying all auction traffic through a single monolithic stack, so any failure affects 100% of traffic rather than a bounded cell. 
+  Fetching configuration data (partner lists, bid floors, and targeting parameters) from the control plane on every request, so control plane impairment halts the data plane. 
+  Treating all components as equally critical instead of mapping the real-time bid path and prioritizing its fault tolerance. 

 **Benefits of establishing this best practice:** 
+  Individual component failures are absorbed without cascading into auction failures. 
+  Cell-based partitioning bounds the scope of impact of any single failure to a defined slice of traffic. 
+  Static stability keeps the bid path serving on last-known-good configuration during control plane disruptions. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance"></a>

 In advertising systems, degraded auction capacity translates into lost revenue because bid opportunities are perishable. An impression that cannot be filled in its decisioning window is gone permanently. This economic reality makes impact containment a priority here, as the cost of a failure is measured in dollars of unmonetized inventory. Size cells so the worst-case loss from any single failure stays within a tolerable revenue-impact threshold. 

 Region-based cells match latency and data-residency requirements, but they concentrate demand-side platforms into one cell, which can create hotspots during peak-traffic events. Publisher-tier cells protect premium inventory from long-tail failures, but require careful routing and complicate cross-tier frequency-cap enforcement. With auction-type cells, format-specific processing stacks stay isolated, but cross-format campaigns need shared state such as user-level frequency data and budget pacing. A cell boundary that splits data consumers from the data they need forces cross-cell calls or data replication. Cross-cell calls undermine isolation. Data replication adds consistency lag and operational cost. 

 Amazon SQS, DynamoDB, and Lambda distribute work across Availability Zones by design. Identify which tiers of the auction pipeline already benefit from this. Add fault tolerance to the components that don't, such as stateful caches, self-managed databases, and single-instance coordination services. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Identify critical path components and their single points of failure:** Map your auction pipeline and identify components where a single instance failure would cause auction failures. For each single point of failure, implement the appropriate HA pattern: Auto Scaling groups for stateless compute, Multi-AZ deployments for databases, and ElastiCache replication groups with auto-failover for caches. 

1.  **Implement cell-based architecture for highest-traffic auction components:** Define cells by a dimension that naturally partitions your traffic (geographic region, publisher tier, format type). Deploy independent copies of critical auction components per cell. Configure traffic routing to send requests to the appropriate cell. Implement cell-level health checks and automatic cell isolation when a cell becomes degraded. 

1.  **Use static stability mechanisms for configuration data:** Pre-load all configuration data (partner lists, bid floors, and targeting parameters) at service startup. Cache this configuration locally with a refresh interval. During control plane failures, services continue operating with the last-known-good configuration rather than failing when configuration can't be fetched. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [ADVREL03-BP03 Deploy stateful dependencies across multiple Availability Zones](advrel03-bp03.md) 
+  [ADVREL04-BP02 Architect defensively against failures](advrel04-bp02.md) 
+  [ADVREL03-BP03 Deploy stateful dependencies across multiple Availability Zones](advrel03-bp03.md) 

 **Related documents:** 
+  [Reducing the Scope of Impact with Cell-Based Architecture](https://docs.aws.amazon.com/wellarchitected/latest/reducing-scope-of-impact-with-cell-based-architecture/reducing-scope-of-impact-with-cell-based-architecture.html) 
+  [Static stability using Availability Zones](https://aws.amazon.com/builders-library/static-stability-using-availability-zones/) 

 **Related services:** 
+  [Amazon SQS](https://aws.amazon.com/sqs/) 
+  [Amazon DynamoDB](https://aws.amazon.com/dynamodb/) 
+  [Amazon ElastiCache](https://aws.amazon.com/elasticache/) 