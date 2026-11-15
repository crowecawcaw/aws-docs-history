

# ADVREL08-BP01 Implement redundant ad verification systems with automated failover mechanisms
<a name="advrel08-bp01"></a>

 Implement redundant ad-verification systems with automated failover. Use multiple verification providers and automated monitoring for reliable advertising measurement and validation. 

 **Desired outcome:** 
+  Multiple verification providers operate in parallel, and failover to backup providers is automatic. 
+  Measurement continues uninterrupted when individual verification providers experience degradation. 
+  Circuit breakers guard against degraded third-party services blocking measurement pipelines. 

 **Common anti-patterns:** 
+  Relying on a single verification provider, so its degradation halts all measurement. 
+  No circuit breaker on third-party verification calls, so a degraded provider can block the measurement pipeline. 
+  Processing measurement events without deduplication, so retries inflate counts. 
+  No health-based routing or automated failover between providers, so failover requires manual intervention. 

 **Benefits of establishing this best practice:** 
+  Multiple providers operate in parallel with automatic failover, so measurement continues during provider degradation. 
+  Circuit breakers keep degraded third-party services from blocking measurement pipelines. 
+  DynamoDB deduplication avoids duplicate counting when events are retried. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance"></a>

 IAS, DoubleVerify, and MOAT verify advertising measurement for advertisers. Because their availability is outside your control, a single-provider design ties your measurements to their availability. MRC accreditation and advertiser billing both depend on accurate measurement. 

 Two providers running in parallel can measure the same event. Agreement between them cross-validates the numbers, and disagreement signals a data quality issue worth investigating. Each added provider has its own integration cost. Route each request to a provider based on current health. 

 A measurement can drop without producing an error with no alarm to signal that loss. The loss then appears later during reconciliation, by which point Amazon Kinesis retention has expired and the original events are gone. Send failed measurements to an Amazon SQS dead-letter queue for deferred reprocessing. 

 A retried event can be counted twice if nothing tracks prior processing, and duplicate counting corrupts billing numbers. Store each event's ID in DynamoDB so retries can be identified and skipped. Circuit breaker activations feed SLA tracking and partner reporting. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Integrate multiple verification providers with health-based routing:** Configure Amazon API Gateway or an application-level routing layer that routes measurement requests to verification providers based on real-time health checks. Define primary and fallback providers per measurement type (viewability, click verification, conversion tracking). Implement automated health checks that test each provider every 60 seconds. 

1.  **Implement circuit breakers for third-party verification calls:** Deploy circuit breakers on all calls to external verification providers. Set open threshold at 30% failure rate over 60 seconds. Configure fallback to: use alternative provider, cache last-known-good measurement data, or record event for later verification. Log all circuit breaker activations for SLA tracking and partner reporting. 

1.  **Deploy DynamoDB for measurement deduplication:** Store measurement event IDs in DynamoDB with a 24-hour TTL. Before processing any measurement event, check the DynamoDB table for a previous processing record. This avoids duplicate counting when events are retried after failures. Use DynamoDB conditional writes to make deduplication atomic. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [ADVREL04-BP02 Architect defensively against failures](advrel04-bp02.md) 
+  [ADVREL08-BP02 Establish reliable data collection and validation pipelines for measurement accuracy](advrel08-bp02.md) 

 **Related documents:** 
+  [Implementing health checks - Amazon Builders' Library](https://aws.amazon.com/builders-library/implementing-health-checks/) 
+  [Making retries safe with idempotent APIs - Amazon Builders' Library](https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-apis/) 

 **Related services:** 
+  [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) 
+  [AWS Lambda](https://aws.amazon.com/lambda/) 
+  [Amazon EventBridge](https://aws.amazon.com/eventbridge/) 
+  [AWS Step Functions](https://aws.amazon.com/step-functions/) 
+  [Amazon DynamoDB](https://aws.amazon.com/dynamodb/) 