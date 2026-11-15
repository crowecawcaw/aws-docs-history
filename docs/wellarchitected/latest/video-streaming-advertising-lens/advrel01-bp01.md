

# ADVREL01-BP01 Use loosely-coupled architectures to enable graceful recovery from failures
<a name="advrel01-bp01"></a>

 Use architecture patterns like service-oriented architecture (SOA), microservices, and event-driven architecture (EDA) to recover quickly from failure. These patterns enable failure recovery through loosely coupled designs and enhance system resilience and component self-sufficiency. 

 **Desired outcome:** 
+  Component failures are isolated. A failure in one advertising service doesn't cascade to healthy services. 
+  Your data pipelines operate reliably despite unexpected failures, packet loss, or high latency. 
+  Interactions between components in your distributed advertising system are designed so that individual failures make minimal impact on overall system function. 

 **Common anti-patterns:** 
+  Synchronous, tightly coupled calls between auction components where one slow downstream dependency blocks bid response assembly. 
+  No retry or dead-letter queue logic: failed events are dropped with no record rather than processed asynchronously. 
+  Sharing mutable state between services, which creates invisible coupling and correlated failures. 

 **Benefits of establishing this best practice:** 
+  Individual component failures don't propagate across the auction pipeline. 
+  Asynchronous communication enables retries and error handling without blocking the critical bid response path. 
+  Services can be scaled, replaced, or updated independently without disrupting other components. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance"></a>

 In an auction pipeline, first identify which interactions must be synchronous. A bid response has a hard deadline measured in tens of milliseconds, and every synchronous call inside that window adds its full latency and full failure probability to the response. Post-bid work has no such deadline. An impression beacon, a billing record, or an analytics event can run seconds later with no commercial consequence. Split the system along that line, and a slow dependency delays a report instead of costing a bid. 

 Decoupling relocates failure, and the new failure is quieter than the one it replaced. A synchronous call that fails is visible immediately to the caller. An asynchronous handoff that fails downstream returns success to the producer, so the loss surfaces later as records that never arrived, discovered by reconciliation instead of an alarm. Every asynchronous boundary needs an explicit answer for what happens to a message that can't be processed. The default answer is unbounded retry, and one broken consumer then builds a growing backlog that delays everything behind it. 

 Backlogs behave worst during recovery, which is critical to the system. A component returning to service faces the accumulated queue plus current traffic. It can be overwhelmed on restart and fail again, and the cycle repeats. Bounding retries and diverting persistently failing messages breaks that cycle. Those messages stop being processed automatically and require manual handling. For advertising data, where a lost impression is lost revenue, you must assign that handling to a named owner. 

 When an external DSP or SSP slows down, continuing to call it consumes your connection pool and your latency budget on requests that will not complete in time. Retrying multiplies the load on an already-overloaded system. Stop calling a failing partner quickly and continue the auction without them, accepting thinner demand in exchange for a bid that returns. This only works if the auction can produce a valid result from a subset of partners. 

 Independent subscribers make fan-out worth its complexity, because one consumer failing leaves the others unaffected. The cost is that the same event now exists in several places with no guarantee they are all current. Downstream reconciliation must expect this. Assuming otherwise triggers discrepancy investigations that find nothing wrong. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Decompose the auction pipeline into independent microservices:** Separate bid request ingestion, user enrichment, audience matching, auction logic, and bid response assembly into independently deployable services. Define service contracts (OpenAPI or Protobuf schemas) between components. Confirm that no service holds mutable state that other services depend on synchronously. 

1.  **Implement EDA patterns with EventBridge and Amazon Simple Notification Service (SNS) for post-bid workflows:** Route post-bid events (wins, losses, click tracking, and impression beacons) through EventBridge or SNS rather than synchronous API calls. This decouples analytics, billing, and frequency-cap update workflows from the critical bid response path. Configure dead-letter queues on SQS consumers for failed event processing. 

1.  **Add circuit breakers for external partner integrations:** Implement circuit breaker patterns (using Resilience4j or equivalent) for all synchronous calls to external DSP/SSP endpoints. Set circuit open thresholds at 50% failure rate over a 30-second window. Configure half-open probing intervals (15 seconds) for recovery. Log all circuit state transitions to CloudWatch. 

1.  **Configure SQS dead-letter queues for all queue-based workflows:** Set maxReceiveCount on all SQS queues to keep messages from being retried indefinitely. Route failed messages to per-queue dead-letter queues (DLQs). Configure CloudWatch alarms on DLQ depth to alert when processing failures exceed expected thresholds. 

1.  **Validate decoupling with fault injection:** Use AWS Fault Injection Service to inject failures into individual components and verify that the remaining components continue to function correctly. Test scenarios include: user enrichment service unavailable (auction should proceed with cached or default targeting data), a DSP endpoint timing out (should not delay other DSP responses), and an analytics SQS consumer failing (should not affect bid response delivery). 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [ADVREL01-BP04 Implement chaos engineering practices](advrel01-bp04.md) 
+  [ADVREL02-BP01 To allow fast and graceful failure of latency-sensitive services, avoid exponential backoff and retry](advrel02-bp01.md) 

 **Related documents:** 
+  [What is EDA? - Event Driven Architecture Explained - AWS](https://aws.amazon.com/event-driven-architecture/) 
+  [Avoiding insurmountable queue backlogs](https://aws.amazon.com/builders-library/avoiding-insurmountable-queue-backlogs/) 

 **Related services:** 
+  [Amazon SQS](https://aws.amazon.com/sqs/) 
+  [Amazon EventBridge](https://aws.amazon.com/eventbridge/) 
+  [Amazon SNS](https://aws.amazon.com/sns/) 