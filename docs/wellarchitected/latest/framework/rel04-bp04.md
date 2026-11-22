

# REL04-BP04 Make mutating operations idempotent

 An idempotent operation produces the same result whether it runs once or many times, so a client can safely retry a request. Retries and duplicate delivery are normal in distributed systems, and idempotency makes these operations safer and more consistent. 

 **Desired outcome:** 
+  You have a consistent, documented, and widely adopted approach for idempotency across all components and services. 
+  Your mutating operations produce the same result no matter how many times an identical request is received. 
+  Your clients can safely retry after a timeout or missing response without creating duplicate records. 
+  Your consumers recognize and ignore duplicate messages in event-driven flows. 

 **Common anti-patterns:** 
+  Teams apply idempotency indiscriminately, even to operations that do not need it, which adds needless complexity. 
+  A service uses timestamps as idempotency keys, so clock skew or shared timestamps across clients cause collisions. 
+  A service stores entire request payloads for idempotency and overwrites them on each request, which degrades performance and scalability. 
+  Services generate keys inconsistently, so a duplicate request is not recognized and the operation runs again. 

 **Benefits of establishing this best practice:** 
+  The system handles retries and duplicate requests without extra logic or complex state reconciliation. 
+  Reliability improves because repeated identical requests do not create duplicate records or unintended side effects. 
+  Data stays consistent across services because the same request always produces the same response. 
+  Error handling is simpler, because a client that misses a response can safely resend the same request. 

 **Level of risk exposed if this best practice is not established:** Medium 

## Implementation guidance
<a name="implementation-guidance"></a>

 Distributed systems can provide *at-most-once* delivery, where the client sends a single request, or *at-least-once* delivery, where the client keeps requesting until it confirms success. Providing an *exactly-once* effect is much harder, because the same legitimate request can arrive several times. Idempotency provides that functionality. The client generates an *idempotency token* and attaches it to each request. When a service receives a request, it checks whether the token was already processed. If so, it returns the stored response. If not, it processes the request, stores the response with the token, and returns it. 

 Asynchronous services redeliver a message after a network failure or a missing acknowledgement, and synchronous clients resend after a timeout. Without idempotency, each duplicate produces a duplicate record, a double charge, or another unintended side effect. 

 Idempotency matters most in event-driven architectures backed by a message queue or stream, where a message published once can be delivered more than once. A publisher includes a token in each message. A consumer keeps track of the tokens it has seen and ignores any message whose token it has already processed. A service must also pass the token it received to every downstream service it calls, so that each stage in the processing chain protects against reprocessing. 

 Apply idempotency to operations that mutate state, such as create, update, and delete. Read-only operations rarely need it unless they have side effects. Avoid timestamps as keys, because clock skew and shared clocks produce collisions. Store the token and a small amount of state rather than the full payload, which keeps the mechanism fast and scalable. Generate keys the same way across every service, because inconsistent keys defeat duplicate detection entirely. Expire old tokens on a schedule, since the chance of legitimate reuse falls as time passes. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Identify idempotent operations:** Determine which operations require idempotency. These are typically POST, PUT, and DELETE HTTP methods and database insert, update, or delete operations. Read-only operations usually do not need idempotency unless they have side effects. 

1.  **Generate a unique token per request:** Have the sender include a unique token in each request, either in the request body or in metadata such as an HTTP header, so the receiver can recognize duplicates. Common choices are [Universally Unique Identifiers (UUIDs)](https://datatracker.ietf.org/doc/html/rfc9562) and [K-Sortable Unique Identifiers (KSUIDs)](https://github.com/segmentio/ksuid). 

1.  **Track and manage idempotency state:** Store each token with its state, such as pending, completed, or failed, so the workload can identify and handle duplicates. Use concurrency controls such as locks, transactions, or optimistic concurrency to record the token and run the mutating operation atomically, which prevents race conditions. Expire old tokens with a time-to-live (TTL) value to manage storage and performance. 

1.  **Choose a store for idempotency state:** Select a store based on data volume, latency, durability, and how the mechanism fits your architecture. 
   +  [Amazon DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/) offers low-latency key-value storage and can expire tokens automatically with a TTL value. 
   +  [Amazon ElastiCache](https://aws.amazon.com/elasticache/) stores tokens with high throughput and low latency, and supports automatic TTL expiry. 
   +  [Amazon RDS](https://aws.amazon.com/rds/) suits workloads that already use a relational database for other purposes. 
   +  [Amazon S3](https://aws.amazon.com/s3/) provides durable object storage, and its versioning can help track the state of idempotent operations. 

1.  **Implement idempotency checks in components:** Before processing a request, check whether the token was already handled, and if so return the stored result instead of running the operation again. Build test suites that cover successful, failed, and duplicate requests. For functions, [Powertools for AWS Lambda](https://docs.aws.amazon.com/powertools/java/latest/utilities/idempotency/) provides a utility that converts a function into an idempotent operation that is safe to retry. 

1.  **Document the idempotent contract:** Document each API and component so clients understand which operations are idempotent and how to supply a token. A clear contract reduces misuse and the fear of duplicate processing. 

1.  **Monitor and audit:** Add monitoring and auditing to detect idempotency issues, such as unexpected response variations or a high rate of duplicate handling. Log requests with their tokens so you can trace and debug reprocessing. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [REL04-BP01 Identify the kind of distributed systems you depend on](rel04-bp01.md) 
+  [REL05-BP03 Control and limit retry calls](rel05-bp03.md) 
+  [REL08-BP02 Integrate functional testing as part of your deployment](rel08-bp02.md) 
+  [REL06-BP01 Monitor all components for the workload (Generation)](rel06-bp01.md) 

 **Related documents:** 
+  [The Amazon Builders' Library: Making retries safe with idempotent APIs](https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/) 
+  [The Amazon Builders' Library: Challenges with distributed systems](https://builder.aws.com/content/3F08f7GPFiZMCgXD8gny6OjxR0Z/challenges-with-distributed-systems) 
+  [The Amazon Builders' Library: Reliability, constant work, and a good cup of coffee](https://builder.aws.com/content/3F05oqNtNUWxHJ5r6L6I2HrH4rI/reliability-constant-work-and-a-good-cup-of-coffee) 
+  [Ensuring idempotency](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ECS_Idempotency.html) 
+  [Ensuring idempotency in Amazon EC2 API requests](https://docs.aws.amazon.com/ec2/latest/devguide/ec2-api-idempotency.html) 
+  [Prevent duplicate Lambda events](https://repost.aws/knowledge-center/lambda-function-idempotent) 

 **Related videos:** 
+  [AWS re:Invent 2023 - Building next-generation applications with event-driven architecture (API302)](https://www.youtube.com/watch?v=KXR17uwLEC8) 
+  [AWS re:Invent 2023 - Advanced integration patterns & trade-offs for loosely coupled systems (API309)](https://www.youtube.com/watch?v=FGKGdUiZKto) 
+  [AWS re:Invent 2023 - Advanced event-driven patterns with Amazon EventBridge (COM301-R)](https://www.youtube.com/watch?v=6X4lSPkn4ps) 
+  [AWS re:Invent 2025 - Integration patterns for distributed systems (API315)](https://www.youtube.com/watch?v=xc9P6wbhLwE) 

 **Related tools:** 
+  [Idempotency with Powertools for AWS Lambda (Java)](https://docs.aws.amazon.com/powertools/java/latest/utilities/idempotency/) 
+  [Idempotency - Powertools for AWS Lambda (Python)](https://docs.aws.amazon.com/powertools/python/latest/utilities/idempotency/) 
+  [Powertools for AWS](https://github.com/aws-powertools/) 