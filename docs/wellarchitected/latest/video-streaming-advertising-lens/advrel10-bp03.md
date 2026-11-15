

# ADVREL10-BP03 Architect fault-tolerant unified ad sales and fulfillment with graceful degradation per channel
<a name="advrel10-bp03"></a>

 Unified ad sales systems manage campaign booking, inventory allocation, and fulfillment across both linear TV schedules and digital programmatic channels. A failure must not stop either channel from serving ads. 

 **Desired outcome:** 
+  The unified system continues operating for both channels independently during orchestration failures. 
+  Linear placements continue per pre-committed schedules. Digital auctions continue with last-known parameters. 
+  Cross-channel pacing degrades gracefully (slight over-delivery compared to under-delivery) with automatic reconciliation on recovery. 

 **Common anti-patterns:** 
+  Synchronous dependency between digital bid decisioning and the unified campaign management database, database unavailability blocks all digital ad serving 
+  Linear schedule changes requiring real-time confirmation from the unified system, network issues between the broadcast facility and cloud block schedule updates 
+  Single-writer architecture for campaign budgets across channels, linear and digital contend for the same budget record, causing lock contention and potential budget overruns during partial failures 
+  No pre-staged fallback campaign parameters at the edge, unified system outage means digital ad servers have no campaign data to work with 

 **Benefits of establishing this best practice:** 
+  Fault-tolerant unified fulfillment helps avoid revenue loss during system outages. 
+  Both channels continue monetizing inventory using locally cached parameters, with automatic reconciliation limiting material budget overruns (limited to the duration of the outage × burn rate). 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance"></a>

 Linear campaigns are planned hours or days ahead while digital auctions decide in real time. The difference between these channels is a resilience asset, as a planned channel can run from cached decisions for a long period, and a real-time channel needs only very recent parameters. Neither channel needs the central system inside the request path. 

 Synchronous budget checks give perfect accuracy, but they also tie every channel to the central system, so one system outage halts spending everywhere. A reservation model reverses that dependency by giving each channel pre-allocated budget it can keep spending without the central system. The cost is possible over-delivery during a long outage, bounded by the reservation window. 

 Convergence introduces a failure mode called split-brain. Disconnected channels keep spending, and their local decisions drift apart during the outage. Recovery then exposes the conflicts. Budget overruns, frequency cap breaches, and scheduling conflicts all appear at once. Reconciliation resolves them, but sales and operations must design the rules before an outage. 

 Configure graceful degradation to favor slight over-delivery rather than under-delivery. Define this preference before an incident so disconnected spending follows a consistent policy. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Pre-stage campaign parameters using DynamoDB global tables:** Store campaign configurations (budgets, targeting parameters, frequency caps, bid floors) in DynamoDB global tables with replicas in each operational region. Digital ad servers read from local replicas with a 5-second eventual consistency tolerance. This removes the need for a synchronous dependency on the central system for every bid decision. 

1.  **Implement budget reservation pattern:** Each channel (linear, digital-US, digital-EU) holds a pre-allocated budget reservation updated every 5 minutes through async write from the central system. Configure spending logic to limit expenditure to the current reservation. When the central system is unavailable, channels continue spending within their reservation, limiting runaway over-delivery. 

1.  **Cache linear schedules at broadcast facility:** Implement local schedule caching at each broadcast facility that stores the confirmed schedule for the next 24 hours. Configure the facility to execute the cached schedule when connectivity to the central system is lost. Flag undelivered schedule changes for reconciliation queue when connectivity restores. 

1.  **Deploy split-brain reconciliation on recovery:** Create a Lambda function triggered when system connectivity restores that: queries all channel spending records from the outage period, compares against central system expectations, identifies over-delivery (reconcile with credits) and under-delivery (extend campaign flights), and generates reconciliation reports for operations review. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [ADVREL04-BP02 Architect defensively against failures](advrel04-bp02.md) 
+  [ADVREL02-BP02 Implement a caching strategy](advrel02-bp02.md) 
+  [ADVREL03-BP03 Deploy stateful dependencies across multiple Availability Zones](advrel03-bp03.md) 

 **Related documents:** 
+  [Avoiding overload in distributed systems, Amazon Builders Library](https://aws.amazon.com/builders-library/avoiding-overload-in-distributed-systems-by-putting-the-smaller-service-in-control/) 

 **Related services:** 
+  [Amazon DynamoDB Global Tables](https://aws.amazon.com/dynamodb/global-tables/) 
+  [Amazon ElastiCache](https://aws.amazon.com/elasticache/) 
+  [Amazon EventBridge](https://aws.amazon.com/eventbridge/) 
+  [AWS Step Functions](https://aws.amazon.com/step-functions/) 
+  [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) 