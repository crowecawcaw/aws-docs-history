

# ADVREL07-BP02 Maintain data consistency and availability across collaboration workflows
<a name="advrel07-bp02"></a>

 Data consistency and availability matter when you work with multiple stakeholders in advertising collaboration workflows. Implement versioning, logging, and health checks across collaboration lifecycle events. 

 **Desired outcome:** 
+  Collaborative datasets maintain version consistency across all collaboration members. 
+  Idempotent processing means that retry events don't produce duplicate or inconsistent analysis results. 
+  Cross-region replication for critical collaboration data stores provides recovery capability. 

 **Common anti-patterns:** 
+  No schema versioning for collaborative datasets, so schema evolution breaks active collaborations. 
+  Non-idempotent query operations, so transient-failure retries re-execute and consume extra differential privacy budget. 
+  Single-region collaboration data stores with no replication or PITR, so no recovery path exists. 
+  No health checks on collaboration endpoints, so partner-facing availability gaps go undetected. 

 **Benefits of establishing this best practice:** 
+  Versioned schemas keep collaborative datasets consistent across all collaboration members. 
+  Idempotent processing avoids duplicate results and wasted privacy budget on retries. 
+  Cross-region replication and PITR provide recovery capability for critical collaboration data. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance"></a>

 A collaborative dataset is a shared contract between independent organizations. Each partner builds integrations against an agreed schema, and no single party controls all of those integrations. A schema change therefore reaches every participant at once. 

 Broken results cost more than ordinary corrupted data. Re-running a corrupted analysis consumes the differential privacy budget again, and some results become unrecoverable once that budget is spent. Backward-compatibility contracts keep schema changes from breaking active collaborations, and pinned versions provide a stable schema to those collaborations while newer versions become available. The trade-off is slower evolution, because every change must stay compatible with versions still in use. 

 Idempotency means a repeated operation produces the same effect as one execution. Matching queries need this property because a transient failure often triggers a retry, and without idempotency the retry runs the query again, spending budget twice. Transaction state in DynamoDB identifies repeated queries so the retry returns the earlier result instead of paying twice. 

 Availability across partner Regions introduces a consistency question. Replicated tables can serve reads close to each partner, but reads during the lag return stale data. Point-in-time recovery is a separate concern, as it rebuilds a table after loss or corruption. No single organization owns the shared schema, so assign a named steward to reduce the risk of drift. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Implement schema versioning for collaborative datasets:** Version all schemas used in AWS Clean Rooms collaborations using AWS Glue Schema Registry. Include schema version in all dataset metadata. Create migration procedures for schema evolution that maintain backward compatibility for active collaborations. 

1.  **Use idempotent keys for privacy computation operations:** Assign unique idempotency keys to all Clean Rooms query operations. Store query result hashes in DynamoDB with the idempotency key. If a query is retried because of a transient failure, return the cached result rather than re-executing and consuming differential privacy budget. 

1.  **Configure DynamoDB with PITR and read replicas:** Enable DynamoDB Point-in-Time Recovery on all collaboration data tables. For high-read collaboration workloads, deploy DynamoDB Global Tables to provide low-latency read access from collaboration partner regions. Monitor DynamoDB replication lag to verify consistency across regions. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [ADVREL07-BP01 Design resilient architectures with privacy-preserving fault tolerance](advrel07-bp01.md) 
+  [ADVREL03-BP03 Deploy stateful dependencies across multiple Availability Zones](advrel03-bp03.md) 

 **Related documents:** 
+  [Guidance for Maximum Data Availability Architecture on AWS](https://aws.amazon.com/solutions/guidance/maximum-data-availability-architecture-on-aws/) 

 **Related services:** 
+  [Amazon DynamoDB](https://aws.amazon.com/dynamodb/) 
+  [AWS Glue Schema Registry](https://docs.aws.amazon.com/glue/latest/dg/schema-registry.html) 