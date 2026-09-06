

# AGENTCOST03-BP03 Implement cost-optimized state persistence and lifecycle management
<a name="agentcost03-bp03"></a>

 Agent state grows quickly when every reasoning step triggers a checkpoint, and it stays forever when no lifecycle policy removes it. Saving state at meaningful decision points, tiering by access pattern, and automating archival keeps recoverability without paying for a growing backlog of stale sessions. 

 **Desired outcome:** 
+  You checkpoint at meaningful decision points rather than after every reasoning step. 
+  You have session state tiered by access pattern, with high-performance storage reserved for active work. 
+  You have automated lifecycle policies that archive or purge stale context. 
+  You track storage cost per agent and session, with alarms for unexpected growth. 

 **Common anti-patterns:** 
+  Checkpointing after every reasoning step with synchronous writes when asynchronous checkpoints at meaningful decision points would suffice. 
+  Keeping all session state on high-performance storage regardless of activity level, paying unnecessary costs for inactive or archived sessions. 
+  Allowing agent memory to accumulate indefinitely without archival or deletion, producing unbounded storage growth. 
+  Storing agent state uncompressed when compression could reduce storage costs proportionally. 
+  Deploying state persistence without cost monitoring, hiding high-cost patterns and optimization opportunities. 

 **Benefits of establishing this best practice:** 
+  Automated lifecycle management helps prevent unbounded storage growth without manual intervention across thousands of sessions. 
+  Managed memory separates durable learning from ephemeral state, keeping knowledge that improves agent performance while cleaning up temporary artifacts. 
+  Session timeout configuration balances responsiveness with cost by controlling the compute lifecycle. 

 **Level of risk exposed if this best practice is not established:** Medium 

## Implementation guidance
<a name="implementation-guidance"></a>

 [Amazon Bedrock AgentCore Runtime](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/agents-tools-runtime.html) provides a persistent filesystem that handles tiered storage and lifecycle automatically. The filesystem survives session stop and resume cycles for up to 14 days of inactivity before automatic deletion, and the two lifecycle parameters that shape cost are idleRuntimeSessionTimeout (default 15 minutes) and maxLifetime (up to 8 hours). The 15-minute default suits interactive workloads, while longer timeouts reduce session state transitions for batch workloads. Session storage automatically synchronizes filesystem writes to durable storage throughout the session lifecycle, with data flushed during graceful shutdown when sessions stop. 

 Make a deliberate design choice about checkpointing. For use cases that require explicit checkpoints at application-defined decision points, implement custom checkpoint logic that writes state snapshots to the persistent filesystem. Checkpoint interval is a trade-off between recovery granularity and storage consumption: more frequent checkpoints enable finer-grained recovery but increase storage cost. Some agent frameworks provide built-in checkpoint capabilities using the same filesystem, which avoids reinventing the pattern. 

 Consider how you accomplish durable learning. [Amazon Bedrock AgentCore Memory](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/memory.html) persists insights across sessions (short-term memory for recent interactions, long-term memory for consolidated learning), which is different from per-session filesystem state. For compliance retention beyond the 14-day Runtime filesystem window, export completed session data to [Amazon S3](https://aws.amazon.com/s3/) with Intelligent-Tiering enabled, and configure lifecycle rules for cost-effective long-term storage. Monitor consumption per agent type using [Amazon Bedrock AgentCore Observability](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability.html) with custom dimensions, and set Amazon CloudWatch alarms when growth exceeds expected bounds. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Deploy on AgentCore Runtime with tuned lifecycle parameters:** Use [Amazon Bedrock AgentCore Runtime](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/agents-tools-runtime.html) for automatic session lifecycle management, configuring idleRuntimeSessionTimeout and maxLifetime based on workload patterns. 

1.  **Integrate managed memory for durable learning:** Configure [Amazon Bedrock AgentCore Memory](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/memory.html) short-term memory for recent context and long-term memory for persistent insights, keeping durable learning separate from ephemeral filesystem state. 

1.  **Archive compliance-required sessions to S3:** Export completed session histories to [Amazon S3 Intelligent-Tiering](https://aws.amazon.com/s3/storage-classes/intelligent-tiering/) and set lifecycle rules for cost-effective long-term retention. 

1.  **Monitor storage per agent type:** Configure [Amazon Bedrock AgentCore Observability](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability.html) with custom dimensions to track storage cost per agent type, and set Amazon CloudWatch alarms for unexpected storage growth. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [AGENTCOST01-BP01 Use the reflection pattern to design efficient agent reasoning loops](agentcost01-bp01.html) 
+  [AGENTCOST03-BP01 Design cost-effective retrieval systems with tiered memory](agentcost03-bp01.html) 
+  [AGENTCOST03-BP02 Cost optimize through intelligent compression and pruning of context windows](agentcost03-bp02.html) 
+  [AGENTCOST05-BP01 Establish agent-level reasoning cost tracking and attribution](agentcost05-bp01.html) 

 **Related documents:** 
+  [Amazon Bedrock AgentCore Runtime Sessions](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/runtime-sessions.html) 
+  [Amazon Bedrock AgentCore Memory](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/memory.html) 
+  [Amazon S3 Intelligent-Tiering](https://aws.amazon.com/s3/storage-classes/intelligent-tiering/) 
+  [Economics for agentic AI on AWS](https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-economics/index.html) 

 **Related videos:** 
+  [AWS 2025 - AgentCore Deep Dive: Runtime](https://www.youtube.com/watch?v=wizEw5a4gvM) 

 **Related examples:** 
+  [GitHub: awslabs/amazon-bedrock-agentcore-samples - Runtime advanced concepts](https://github.com/awslabs/amazon-bedrock-agentcore-samples/tree/main/01-tutorials/01-AgentCore-runtime/03-advanced-concepts) 

 **Related services:** 
+  [Amazon Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/) 
+  [Amazon S3](https://aws.amazon.com/s3/) 
+  [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) 