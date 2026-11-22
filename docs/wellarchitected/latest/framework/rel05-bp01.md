

# REL05-BP01 Implement graceful degradation to transform applicable hard dependencies into soft dependencies

 A component with a hard dependency fails when the dependency fails. Graceful degradation converts hard dependencies into soft dependencies, so a component continues to deliver its core function even when a dependency is unhealthy. The component might return stale data, alternate data, or a reduced response, but it does not fail outright. 

 **Desired outcome:** 
+  Your components continue to serve their core function when one or more dependencies are unavailable, in a reduced but predictable manner. 
+  Your degraded pathways return the most critical data or functionality, not an error page, when partial results are still useful. 
+  Your components reach predictable, recoverable states during dependency failure rather than inconsistent or corrupt states. 
+  Your degraded pathways are tested and exercised, so they work when a real failure occurs. 

 **Common anti-patterns:** 
+  Teams do not identify the core business function of a component, and never test that it works during a dependency failure. 
+  A component returns no data on any error, even when one of several dependencies is available and partial results would still be useful. 
+  A partial transaction failure leaves the system in an inconsistent state. 
+  An application has no alternate path to critical configuration when its parameter store is unavailable. 
+  A failed cache refresh empties local state, and the component loses data it could have continued serving. 

 **Benefits of establishing this best practice:** 
+  Overall availability improves because localized failures no longer cascade across the whole workload. 
+  Critical functions keep operating during partial failures, preserving the central business value of the workload. 
+  Failure modes become normal, tested operating conditions rather than unhandled edge cases. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance"></a>

 The *core function* is the minimum output that still delivers business value. Everything outside this output can be considered enhancement. When you separate core function from enhancement, you can design each dependency so that its failure removes an enhancement rather than the whole component. For example, a product page that loses its recommendation service should still show the product, the price, and the buy button. 

 When a failure means you cannot meet every requirement, someone must decide which requirements to drop. A payment system usually favors consistency over availability. On the other hand, a real-time dashboard usually favors availability over completeness. Choose your trade-offs based on the which experiences you can safely degrade. 

 When a component calls several dependencies, treat a partial failure as partial success and return what you have, then record failures for retry. When a downstream system is overloaded, the *circuit breaker* pattern stops calls after failures cross a threshold and periodically probes for recovery. This avoids adding load to a system already struggling. When a transaction spans multiple systems, the *saga* pattern rolls back completed operations if a later one fails, preserving consistency. When a parameter store is unavailable, a set of sane default parameters baked into the deployment image keeps the component running. 

 Fallback logic that is never exercised tends to be broken by the time you need it, and it can introduce failure modes of its own. Keep degraded pathways simpler than the primary path, test them on the same cadence as production code, and keep any embedded defaults current. For more on the risks, see [Avoiding fallback in distributed systems](https://builder.aws.com/content/3EuS9Sakq7L3VLQIF3qzfMfke1Y/avoiding-fallback-in-distributed-systems). 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Map dependencies and define core function:** Identify every external and internal dependency for the component. For each one, state what the component must still do if that dependency fails. This defines the degraded contract you will build and test against. 

1.  **Handle partial dependency failures:** When a component issues multiple downstream requests, return successful results and record the failures rather than failing the whole response. Return per-operation status to the caller, or route failed requests to a dead letter queue for asynchronous retry, and log each failure. 

1.  **Protect against overloaded dependencies:** Apply the circuit breaker pattern to a dependency that is failing under load. After failures cross a threshold, stop calling it and let only occasional probe requests through until it recovers, so you do not deepen the impairment. 

1.  **Provide fallbacks for configuration dependencies:** When a component reads from a parameter store, package a default parameter set in the container or machine image. Keep these defaults current and include them in your test suite so they match production expectations. 

1.  **Keep non-functional dependency failures non-blocking:** When a monitoring, logging, or metrics dependency is unavailable, continue running business functions. Buffer telemetry where you can, and account for compliance cases that require complete audit records before you discard anything. 

1.  **Reduce reliance on single-writer datastores:** For a relational database with a single primary writer, use a Multi-AZ configuration for failover and read replicas for read scaling. Where write availability must survive the loss of the primary, buffer writes in a queue so the workload keeps accepting requests while the primary is unavailable. 

1.  **Test every degraded pathway:** Exercise each fallback under simulated dependency failure. Confirm the component reaches a predictable, recoverable state and that the degraded path stays simpler than the primary path. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [REL05-BP02 Throttle requests](rel05-bp02.md) 
+  [REL05-BP04 Fail fast and limit queues](rel05-bp04.md) 
+  [REL05-BP07 Implement emergency levers](rel05-bp07.md) 
+  [REL04-BP02 Implement loosely coupled dependencies](rel04-bp02.md) 

 **Related documents:** 
+  [The Amazon Builders' Library: Avoiding fallback in distributed systems](https://builder.aws.com/content/3EuS9Sakq7L3VLQIF3qzfMfke1Y/avoiding-fallback-in-distributed-systems) 
+  [The Amazon Builders' Library: Avoiding insurmountable queue backlogs](https://builder.aws.com/content/3EuRcgkTP1MI0c7zM8W6HL3WIqA/avoiding-insurmountable-queue-backlogs) 
+  [Caching challenges and strategies](https://builder.aws.com/content/3K9TeXp6strMiJ4vhakpRD7BQWO/caching-challenges-and-strategies) 
+  [The Amazon Builders' Library: Timeouts, retries, and backoff with jitter](https://builder.aws.com/content/3EumjoZascWd1oZiEgL8ORlv3qE/timeouts-retries-and-backoff-with-jitter) 
+  [Retry behavior](https://docs.aws.amazon.com/sdkref/latest/guide/feature-retry-behavior.html) 
+  [Throttle requests to your REST APIs for better throughput in API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-request-throttling.html) 
+  [Circuit Breaker](https://martinfowler.com/bliki/CircuitBreaker.html) 
+  [Release It\! Second Edition: Design and Deploy Production-Ready Software by Michael Nygard](https://pragprog.com/titles/mnee2/release-it-second-edition/) 

 **Related videos:** 
+  [AWS re:Invent 2023 - A consistent approach to resilience analysis for critical workloads (ARC313)](https://www.youtube.com/watch?v=fEOeP08cQdk) 
+  [AWS re:Invent 2024 - Try again: The tools and techniques behind resilient systems (ARC403)](https://www.youtube.com/watch?v=rvHd4Y76-fs) 