

# REL04-BP02 Implement loosely coupled dependencies

 Loose coupling isolates the behavior of one component from the components that depend on it. When a component changes or fails, that isolation limits the impact to a single boundary. Dependent components interact through a published, versioned interface or a durable intermediary, so each side can change and scale independently. 

 **Desired outcome:** 
+  Your components interact through published interfaces or durable intermediaries, not direct point-to-point calls that fail together. 
+  A failure in one component stays contained and does not degrade the components that depend on it. 
+  Your teams change, scale, or replace the implementation of a component without coordinating changes across others. 
+  Components that do not need an immediate response communicate asynchronously through a queue, stream, or workflow. 

 **Common anti-patterns:** 
+  Teams deploy a monolithic workload where a fault in one area affects the whole application. 
+  Services invoke each other directly across tiers with no failover path and no option for asynchronous processing. 
+  Components share a database or other storage, which reintroduces tight coupling and blocks independent scaling. 
+  A workload ignores back pressure and cannot slow or pause intake when a downstream component falls behind. 

 **Benefits of establishing this best practice:** 
+  A component failure is isolated to one boundary, which makes problems faster to diagnose and resolve. 
+  Development cycles shorten because teams change one component without affecting the performance of others. 
+  Components scale independently based on their own demand, which improves both resilience and cost efficiency. 
+  Asynchronous interactions let the workload keep processing without waiting on a slow or unavailable dependency. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance"></a>

 Tight coupling spreads change and failure. In a tightly coupled system, a change to one component forces changes in the components that call it. A failure in one component degrades the others that share its runtime or data. Loose coupling breaks that chain by hiding a component behind a stable interface. Callers depend only on the versioned, published contract. Behind that boundary, you can modify code, add features, scale out, or replace the underlying technology while limiting risk to the components that depend on it. 

 Asynchronous interaction strengthens the boundary by removing temporal coupling, the requirement that two components be available at the same instant. It suits any interaction that does not need an immediate response, where the caller only needs to know the request was received. One component produces events, and another consumes them. The two components integrate through a durable intermediary such as a queue, a stream, or a workflow. Figure 1 shows dependencies such as queuing systems and load balancers acting as those loosely coupled intermediaries. 

![Dependency diagram showing components integrated asynchronously through loosely coupled intermediaries such as queuing systems and load balancers.](https://docs.aws.amazon.com/wellarchitected/latest/framework/images/dependency-diagram.png)

*Components integrated through loosely coupled intermediaries*


 Match the intermediary to the interaction pattern rather than defaulting to one mechanism everywhere. For example: 
+  A queue decouples a producer from a consumer and buffers work when the consumer is busy. 
+  A pub/sub topic fans one message out to many subscribers for parallel processing. 
+  An event bus routes events from producers to consumers without either side knowing about the other. 
+  A workflow service coordinates several components into an ordered sequence with built-in retry and error handling. 

 A durable intermediary adds latency and one more component to operate and monitor. Buffered work can grow without bound, so plan for back pressure by slowing or pausing intake when a consumer cannot keep up. In hard real-time systems, a request older than a threshold, often a few seconds, is usually stale because the client has stopped waiting. Discard it and process a more recent request. Avoid sharing a database between components to move data, which reintroduces tight coupling. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Build event-driven interactions:** Use [Amazon EventBridge](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-what-is.html) to route events from producers to consumers without direct integration between them. An event, such as a user adding an item to a cart, actuates the next component in the flow. For patterns, see [Building event-driven applications with Amazon EventBridge](https://aws.amazon.com/blogs/compute/building-an-event-driven-application-with-amazon-eventbridge/). 

1.  **Decouple with queues:** Use [Amazon SQS](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/welcome.html) to place a durable queue between producers and consumers. Producers write messages to the queue, consumers read them, and the queue stores messages redundantly across servers. Review the [basic Amazon SQS architecture](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/) before you design the flow. 

1.  **Fan out with pub/sub messaging:** Use [Amazon SNS](https://docs.aws.amazon.com/sns/latest/dg/welcome.html) when one message must reach many subscribers for parallel processing. Publisher systems send to a topic, and each subscriber endpoint receives its own copy, which supports high-throughput, many-to-many delivery. 

1.  **Separate components into microservices:** Build the workload as [microservices](https://aws.amazon.com/microservices/) that independent teams own and that communicate over well-defined APIs. Run them on [Amazon ECS](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/Welcome.html) or [Amazon EKS](https://docs.aws.amazon.com/eks/latest/userguide/what-is-eks.html), and see [Implementing microservices on AWS](https://docs.aws.amazon.com/whitepapers/latest/microservices-on-aws/microservices-on-aws.html) for design patterns. 

1.  **Orchestrate multi-step flows with workflows:** Use [AWS Step Functions](https://aws.amazon.com/step-functions/getting-started/) to coordinate several components into an ordered workflow with retry and error handling built in. Orchestration decouples the components in a multi-step process, as shown in [Create a serverless workflow with AWS Step Functions and AWS Lambda](https://builder.aws.com/learn). 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [REL04-BP01 Identify the kind of distributed systems you depend on](rel04-bp01.md) 
+  [REL04-BP03 Do constant work](rel04-bp03.md) 
+  [REL04-BP04 Make mutating operations idempotent](rel04-bp04.md) 
+  [REL05-BP02 Throttle requests](rel05-bp02.md) 
+  [REL03-BP02 Build services focused on specific business domains and functionality](rel03-bp02.md) 

 **Related documents:** 
+  [The Amazon Builders' Library: Challenges with distributed systems](https://builder.aws.com/content/3F08f7GPFiZMCgXD8gny6OjxR0Z/challenges-with-distributed-systems) 
+  [The Amazon Builders' Library: Reliability, constant work, and a good cup of coffee](https://builder.aws.com/content/3F05oqNtNUWxHJ5r6L6I2HrH4rI/reliability-constant-work-and-a-good-cup-of-coffee) 
+  [Ensuring idempotency in Amazon EC2 API requests](https://docs.aws.amazon.com/ec2/latest/devguide/ec2-api-idempotency.html) 
+  [Send messages between distributed applications with Amazon SQS](https://docs.aws.amazon.com/hands-on/latest/send-messages-distributed-applications/send-messages-distributed-applications.html) 
+  [Let's Architect\! Architecting microservices with containers](https://aws.amazon.com/blogs/architecture/lets-architect-architecting-microservices-with-containers/) 
+  [Orchestrate queue-based microservices with AWS Step Functions and Amazon SQS](https://builder.aws.com/learn) 
+  [High Performance Computing Lens](https://docs.aws.amazon.com/wellarchitected/latest/high-performance-computing-lens/) 
+  [Break up with your monolith](https://pages.awscloud.com/break-up-your-monolith.html) 

 **Related videos:** 
+  [AWS re:Invent 2023 - Building next-generation applications with event-driven architecture (API302)](https://www.youtube.com/watch?v=KXR17uwLEC8) 
+  [AWS re:Invent 2023 - Getting started building serverless event-driven applications (SVS205)](https://www.youtube.com/watch?v=1aTQI-Kqs2U) 
+  [AWS re:Invent 2024 - Optimizing ELB traffic distribution for high availability (NET401)](https://www.youtube.com/watch?v=EhbFossuQhI) 

 **Related services:** 
+  [Amazon EventBridge](https://aws.amazon.com/eventbridge/) 
+  [Amazon Simple Queue Service (Amazon SQS)](https://aws.amazon.com/sqs/) 
+  [Amazon Simple Notification Service (Amazon SNS)](https://aws.amazon.com/sns/) 
+  [AWS Step Functions](https://aws.amazon.com/step-functions/) 