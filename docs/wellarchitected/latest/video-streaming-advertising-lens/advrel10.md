

# Linear Digital Convergence resilience
<a name="advrel10"></a>

 Linear and digital advertising pipelines have historically operated as independent systems with their own failure domains. Converging these into unified ad sales, fulfillment, and measurement introduces new reliability challenges: correlated failures across previously independent systems, data consistency issues between batch linear logs and streaming digital events pipelines, and measurement accuracy degradation when one source becomes unavailable. 


|  ADVREL10: How do you achieve reliable convergence of linear TV ad operations and programmatic workflows when either pipeline fails?  | 
| --- | 
| [ADVREL10-BP01 Design independent failure domains for linear log ingestion and digital event streams with reliable convergence](advrel10-bp01.md) | 
| [ADVREL10-BP02 Implement resilient cross-system measurement pipelines with data reconciliation guarantees](advrel10-bp02.md) | 
| [ADVREL10-BP03 Architect fault-tolerant unified ad sales and fulfillment with graceful degradation per channel](advrel10-bp03.md) | 

## Capability intent
<a name="advrel10-capability-intent"></a>
+  Linear log ingestion and digital event streaming operate as fully independent pipelines that converge reliably into a unified data lake. A failure in either pipeline doesn't block or corrupt the other. 
+  Cross-channel measurement pipelines maintain at-least-once processing with automated reconciliation that detects discrepancies within 24 hours. 
+  The unified ad sales system continues operating for both channels independently during orchestration failures, using locally cached parameters with automatic reconciliation on recovery. 

## Common issues to watch for
<a name="advrel10-common-issues-to-watch-for"></a>
+  Shared database writers between linear and digital pipelines. A malformed linear log file deadlocks digital event processing. 
+  No replay capability: processing failure results in permanently lost measurement data. 
+  Budget reservation pattern not implemented: simultaneous system outage causes frequency cap violations or over-delivery. 