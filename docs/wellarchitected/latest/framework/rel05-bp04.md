

# REL05-BP04 Fail fast and limit queues

 When a service cannot respond successfully, failing fast releases the resources tied to the request and lets a strained service recover. When a service can normally succeed but falls behind during spikes, a queue buffers requests so clients can move on. Both patterns improve reliability, but only when queue backlogs are managed so the service does not process stale requests. 

 **Desired outcome:** 
+  Your services fail fast under resource contention, timeouts, or grey failures, so the system recovers sooner. 
+  Your workloads that tolerate asynchronous processing use queues to absorb spikes and let clients release resources quickly. 
+  Your queues have backlog-management strategies that prevent insurmountable backlogs and stale-request processing. 
+  Your impaired resources are removed from request routing rather than left to add latency and errors. 

 **Common anti-patterns:** 
+  Teams implement message queues without dead letter queues or alarms on dead letter volume, so failures go undetected. 
+  The age of the oldest message in a queue is not measured, so consumers falling behind are invisible. 
+  Backlogged messages are never cleared, even when the business need behind them has passed. 
+  A first-in-first-out queue is used where last-in-first-out would serve clients better, and backlog processing delays every new request. 
+  Internal queues are exposed directly to clients instead of behind an API that manages intake. 
+  Too many request types share one queue, spreading resource demand and worsening backlogs. 
+  Complex and simple requests share a queue despite needing different timeouts and resource allocation. 
+  Inputs are not validated with assertions, so faults are not surfaced early to components that could handle them. 
+  Faulty resources are left in rotation during grey failures that emit both successes and errors. 

 **Benefits of establishing this best practice:** 
+  Systems that fail fast are easier to debug, and many coding and configuration faults surface before release. 
+  Effective queueing gives the workload resilience to traffic spikes and intermittent faults. 
+  Backlog management keeps processing relevant work instead of spending capacity on requests clients have abandoned. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance"></a>

 When a request cannot succeed, holding it open consumes threads, connections, and memory that the service needs to recover, and it delays the client from moving on. Assertions, input validation, and short server-side timeouts turn a slow, ambiguous failure into an immediate, clear one that a higher-level component can handle. The same principle applies to infrastructure. A *grey failure* is a mix of successes and errors from crashing, packet loss, or reduced capacity. Remove any resource emitting one from routing so it does not add latency to every request that reaches it. 

 Queues solve a different problem and introduce their own. A queue decouples a producer from a consumer and smooths load. A service that would otherwise reject a spike can accept it and drain it at a sustainable rate. The risk is the backlog. If consumers fall behind or fail, messages accumulate, and the queue starts holding requests that clients have already timed out and abandoned. Processing those stale messages wastes capacity and can keep the system behind indefinitely. *Queue depth* and *message age* matter more than throughput by itself because they tell you whether consumers are keeping up. 

 A first-in-first-out queue processes the oldest work first. This is correct when order matters, but harmful when a large backlog means the oldest messages are the most stale. When strict ordering is not required, an approximation of last-in-first-out keeps new, time-sensitive requests flowing while older work waits. A backlog then does not force every client to breach its service level. You can approximate this by sidelining excess or aged traffic to a spillover queue and processing it only when capacity frees up. 

 How you segment queues determines how your backlogs behave. One queue for many request types spreads resource demand unpredictably and lets one type's backlog starve the others. When you separate queues by request type and complexity, you can set timeouts, concurrency, and monitoring appropriate to each. [Amazon SQS](https://aws.amazon.com/sqs/) and [Amazon MQ](https://aws.amazon.com/amazon-mq/) provide the queueing primitives. Dead letter queues capture messages that cannot be processed. [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) provides the metrics and alarms that make backlogs and impaired resources visible enough to act on. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Instrument fail-fast signals:** Add programmatic assertions and specific metrics in your software to surface faults explicitly. Use [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) to create metrics and alarms from application log patterns and SDK instrumentation. 

1.  **Fail away from impaired resources:** Use CloudWatch metrics and alarms to detect resources adding latency or repeatedly failing, and remove them from request routing. For AZ-level impairments, use [Elastic Load Balancing zonal shift](https://docs.aws.amazon.com/elasticloadbalancing/latest/network/zonal-shift.html) or [zonal autoshift](https://docs.aws.amazon.com/elasticloadbalancing/latest/network/) to evacuate traffic from the affected zone. For cross-Region failover, use [ARC Region Switch](https://docs.aws.amazon.com/r53recovery/latest/dg/region-switch.html) to orchestrate a full Regional failover. These are distinct scopes. Do not conflate AZ-level shifts with Region-level failover decisions. 

1.  **Accept work asynchronously behind an API:** Design APIs to accept a request, append it to an internal [Amazon SQS](https://aws.amazon.com/sqs/) queue, and return success so the client releases resources. Keep the queue internal rather than exposing it to clients directly. 

1.  **Monitor queue latency and depth:** Emit a CloudWatch metric for message age each time you dequeue, by comparing the current time to the message timestamp. Alarm on rising message age so you detect consumers falling behind. 

1.  **Sideline aged and excess traffic:** When failures or spikes exceed what you can process within your service level, route older or excess messages to a spillover queue. Process new work first and drain the spillover when capacity is available, approximating last-in-first-out. 

1.  **Capture unprocessable messages:** Use dead letter or redrive queues to move messages that cannot be processed out of the main backlog into a location you can investigate and resolve later. 

1.  **Drop or retry stale messages:** Compare the current time to each message timestamp, and discard messages that are no longer relevant to the requesting client where that is tolerable, rather than processing abandoned work. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [REL05-BP02 Throttle requests](rel05-bp02.md) 
+  [REL05-BP03 Control and limit retry calls](rel05-bp03.md) 
+  [REL04-BP02 Implement loosely coupled dependencies](rel04-bp02.md) 
+  [REL06-BP02 Define and calculate metrics (Aggregation)](rel06-bp02.md) 
+  [REL06-BP07 Monitor end-to-end tracing of requests through your system](rel06-bp07.md) 

 **Related documents:** 
+  [The Amazon Builders' Library: Avoiding insurmountable queue backlogs](https://builder.aws.com/content/3EuRcgkTP1MI0c7zM8W6HL3WIqA/avoiding-insurmountable-queue-backlogs) 
+  [Fail fast](https://www.martinfowler.com/ieeeSoftware/failFast.pdf) 
+  [Prevent an increase of backlog messages in your Amazon SQS queue](https://repost.aws/knowledge-center/sqs-message-backlog) 
+  [Zonal shift for your Network Load Balancer](https://docs.aws.amazon.com/elasticloadbalancing/latest/network/zonal-shift.html) 
+  [Amazon Application Recovery Controller (ARC)](https://docs.aws.amazon.com/r53recovery/latest/dg/) 

 **Related videos:** 
+  [AWS re:Invent 2025 - Global Resilient Apps: Guide to Multi-AZ/Region Architecture with ELB (NET311)](https://www.youtube.com/watch?v=_WFrt9ABrMM) 

 **Related examples:** 
+  [Dead Letter Channel - Enterprise Integration Patterns](https://www.enterpriseintegrationpatterns.com/patterns/messaging/DeadLetterChannel.html) 

 **Related tools:** 
+  [Amazon SQS](https://aws.amazon.com/sqs/) 
+  [Amazon MQ](https://aws.amazon.com/amazon-mq/) 
+  [AWS IoT Core](https://aws.amazon.com/iot-core/) 
+  [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) 