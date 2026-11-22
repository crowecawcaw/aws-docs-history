

# REL05-BP06 Make systems stateless where possible

 A stateless component keeps no client-specific data on local disk or in memory between requests. Any compute node can serve any request, so you can replace or scale nodes without an availability impact. Offloading session and user data to a shared store makes horizontal scaling and node-level fault tolerance possible. 

 **Desired outcome:** 
+  Your components hold no session or user data locally between requests, so any node can serve any request. 
+  Your compute nodes can be replaced at will without affecting availability. 
+  Your components scale horizontally in response to fluctuating traffic, adding and removing capacity freely. 
+  Your session and user data live in a shared store decoupled from application logic. 

 **Common anti-patterns:** 
+  Applications store session data on the local disk or in the memory of the node that handled the first request. 
+  Replacing or scaling a node drops active sessions, forcing users to reauthenticate or lose progress. 
+  Teams scale vertically because sticky sessions tie users to a single node and block horizontal scaling. 
+  User data and secrets are embedded in application code rather than retrieved from a decoupled store. 

 **Benefits of establishing this best practice:** 
+  Horizontal scaling becomes possible, so capacity tracks fluctuating traffic and demand. 
+  Components tolerate the failure of an individual node, because no request depends on node-local data. 
+  Application development gains flexibility, because components scale and deploy independently. 

 **Level of risk exposed if this best practice is not established:** Medium 

## Implementation guidance
<a name="implementation-guidance"></a>

 When a component stores session data locally, the node that handled the first request must handle every later request in that session. Lose the node and you lose the session. This coupling forces sticky sessions, blocks free replacement of nodes, and pushes teams toward vertical scaling because they cannot spread a session across a fleet. Removing local state breaks the coupling, so any node can serve any request and the fleet becomes both scalable and fault-tolerant. 

 Not all state can move, so understand what state a component holds and why. A *session* is the unique, per-user data that persists across requests during use of the application. Some of it is application state that must be preserved, and some of it is incidental caching that can be recomputed. Separating application state from caching identifies what needs to move outside the node. Analyzing the stateful components before you redesign them reveals the cost and risk of the transition, so you can decide which components are worth converting. 

 Decouple user data by pulling profiles, secrets, and large objects out of application memory into purpose-built stores the application queries when needed. Offload session data by moving the per-request session state into a shared cache, database, or file system every node can reach. Once state lives outside the compute layer, nodes become interchangeable, and you can adopt serverless compute where any function instance serves any request. Each request adds a network hop to the state store, so match each store's latency and consistency to its access pattern. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Identify stateful components:** Analyze the application and locate every component that holds session or user state locally. Classify each piece of state as data that must be persisted or caching that can be recomputed, so you know what must move. 

1.  **Decouple user data from application logic:** Separate user data from core logic and move it into purpose-built stores. Use [Amazon Cognito](https://aws.amazon.com/cognito/) [identity pools](https://docs.aws.amazon.com/cognito/latest/developerguide/getting-started-with-identity-pools.html) and [user pools](https://docs.aws.amazon.com/cognito/latest/developerguide/getting-started-user-pools-application.html) for user identity, [AWS Secrets Manager](https://aws.amazon.com/secrets-manager/) for secrets, [Amazon S3](https://aws.amazon.com/s3/) for large unstructured objects, and [Amazon DynamoDB](https://aws.amazon.com/dynamodb/) for structured data such as user profiles. 

1.  **Offload session data to a shared store:** Move per-request session state into a store every node can reach, such as [Amazon ElastiCache](https://aws.amazon.com/elasticache/), Amazon DynamoDB, [Amazon Elastic File System](https://aws.amazon.com/efs/), or [Amazon MemoryDB](https://aws.amazon.com/memorydb/). Choose the store whose latency and consistency match your session access pattern. 

1.  **Design and validate the stateless architecture:** After identifying which state must persist and selecting the stores, redesign the components to hold no local state between requests. Confirm that replacing a node mid-session has no availability impact. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [REL05-BP01 Implement graceful degradation to transform applicable hard dependencies into soft dependencies](rel05-bp01.md) 
+  [REL05-BP04 Fail fast and limit queues](rel05-bp04.md) 
+  [REL11-BP03 Automate healing on all layers](rel11-bp03.md) 

 **Related documents:** 
+  [The Amazon Builders' Library: Avoiding fallback in distributed systems](https://builder.aws.com/content/3EuS9Sakq7L3VLQIF3qzfMfke1Y/avoiding-fallback-in-distributed-systems) 
+  [The Amazon Builders' Library: Avoiding insurmountable queue backlogs](https://builder.aws.com/content/3EuRcgkTP1MI0c7zM8W6HL3WIqA/avoiding-insurmountable-queue-backlogs) 
+  [Caching challenges and strategies](https://builder.aws.com/content/3K9TeXp6strMiJ4vhakpRD7BQWO/caching-challenges-and-strategies) 
+  [Tutorial: Host a WordPress blog on Amazon Linux 2023](https://docs.aws.amazon.com/linux/al2023/ug/hosting-wordpress-aml-2023.html) 

 **Related tools:** 
+  [Amazon Cognito](https://aws.amazon.com/cognito/) 
+  [Amazon DynamoDB](https://aws.amazon.com/dynamodb/) 
+  [Amazon ElastiCache](https://aws.amazon.com/elasticache/) 
+  [Amazon MemoryDB](https://aws.amazon.com/memorydb/) 
+  [AWS Secrets Manager](https://aws.amazon.com/secrets-manager/) 