

# ADVREL02-BP03 Avoid scale mismatch of both internal services and external partners

 Implement proportional scaling across all system components in advertising workloads. Balance service capacities, particularly in DSP to SSP integrations, and use pub/sub patterns to reliably distribute load and avoid service overload in microservices architectures. 

 **Desired outcome:** 
+  All components scale proportionally: load balancers, application servers, databases, and caches are sized so that no single layer becomes a bottleneck during traffic spikes. 
+  External partner integrations scale to match your capacity so that partner requests don't overwhelm your API frontend services. 
+  Pub/sub patterns help avoid overloading any single downstream consumer during bursty traffic. 

 **Common anti-patterns:** 
+  Scaling application servers without corresponding scaling of the load balancer. 
+  A partner's bid request volume overwhelming your API frontend services through a PrivateLink connection. 
+  Microservices that produce events faster than consumers can process them, which builds unbounded queue backlogs during traffic spikes. 

 **Benefits of establishing this best practice:** 
+  No single component becomes a bottleneck that limits overall advertising throughput. 
+  Partner traffic growth is managed without affecting other partners or internal services. 
+  Load distribution through pub/sub patterns maintains reliability across microservices during bursts. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance"></a>

 Capacity planning tends to focus on services known to be expensive. In practice, the constraint is often a frequency-capping lookup, a connection limit, or an overlooked queue. Design for proportionality, so every component reaches its ceiling at roughly the same traffic multiple. A path with one component sized for three times baseline and everything else sized for ten has an effective ceiling of three. 

 When a high-throughput service calls a lower-capacity one, it can generate work faster than the downstream can retire it. The queue grows without bound, and every waiting request eventually times out. Let the component with less capacity govern the rate. An explicit buffer between components of different throughput is therefore a reliability mechanism. 

 Direct calls couple the caller's success to every recipient, so one slow consumer blocks the caller. Decoupled distribution avoids this coupling, but introduces a subtler waste. If every subscriber receives every event and discards what it doesn't need, each subscriber pays to process the whole stream. Total cost then scales with subscribers times events. Filter at the subscription rather than in consumer code to keep the isolation benefit without that multiplier. 

 Partner traffic is a shared resource with no natural fairness. The partner controls bid volume, so one integration's spike or retry storm draws from the same pool that serves other partners. Contracted rate limits per partner divide the shared pool into allocated shares. Set them even where throttling feels adversarial. The alternative is an outage distributed across all partners instead of a limit applied to one. Reserved capacity at the entry point removes scaling lag when traffic arrives faster than elastic capacity can respond. 

 Test proportionality by raising traffic across every component at once. A test that scales one service in isolation finds nothing about which one gives way first. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Size load balancers based on peak traffic parameters:** Calculate expected peak connections per second (bid requests from all SSPs at peak QPS), peak concurrent connections (persistent HTTP/2 connections × active partners), and peak bandwidth (average bid request size × peak QPS). Use these to size ALB/NLB and configure LCU reservations that guarantee capacity without scaling lag. Set scale-out triggers at 70% LCU utilization to maintain headroom. 

1.  **Implement per-partner rate limits on all API endpoints:** Configure API Gateway usage plans with per-partner API keys and tier-based rate limits. Create three tiers: Premium (highest contracted QPS, strict SLA), Standard (medium QPS), Trial (lowest QPS for new integrations). Apply AWS WAF rate-based rules as a backstop to guard against any single IP range exceeding contracted limits. Monitor per-partner throughput in CloudWatch to detect growing partners that need tier upgrades. 

1.  **Use SNS fan-out with SQS subscriptions for event distribution:** Route all event types through SNS topics with SQS queue subscriptions per consumer. Configure SQS subscription filters to limit each consumer's queue to only the event types it processes, which keeps consumers from receiving and discarding irrelevant events. Set SQS queue visibility timeouts equal to consumer processing time × 1.5 to allow for retries without causing duplicate processing. 

1.  **Configure smaller services to gate throughput from larger ones:** When a small microservice (frequency cap checker) calls a large backend (DynamoDB), implement backpressure mechanisms that limit the caller's request rate to match what the backend can sustain. Use SQS or Kinesis as a buffer between services with different throughput capacities. Set maximum concurrency on Lambda functions that call downstream services to keep Lambda fan-out from overwhelming those services. 

1.  **Validate scale proportionality through load testing:** Perform load tests that increase traffic to 3x, 5x, and 10x baseline simultaneously across all services. Monitor which component hits its scaling limit first and becomes the bottleneck. Adjust Auto Scaling policies and capacity reservations so that all components reach their capacity limits proportionally rather than one component saturating while others have idle capacity. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [ADVREL04-BP02 Architect defensively against failures](advrel04-bp02.md) 
+  [ADVREL02-BP01 To allow fast and graceful failure of latency-sensitive services, avoid exponential backoff and retry](advrel02-bp01.md) 

 **Related documents:** 
+  [Avoiding overload in distributed systems by putting smaller service in control](https://aws.amazon.com/builders-library/avoiding-overload-in-distributed-systems-by-putting-the-smaller-service-in-control/) 
+  [Pub/sub pattern](https://aws.amazon.com/what-is/pub-sub-messaging/) 

 **Related services:** 
+  [Amazon SNS](https://aws.amazon.com/sns/) 
+  [Amazon SQS](https://aws.amazon.com/sqs/) 
+  [Amazon API Gateway](https://aws.amazon.com/api-gateway/) 