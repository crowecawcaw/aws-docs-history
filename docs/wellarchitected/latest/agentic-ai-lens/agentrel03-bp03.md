

# AGENTREL03-BP03 Implement comprehensive state management and checkpoint-based recovery
<a name="agentrel03-bp03"></a>

 Long-running workflows without checkpoints pay the full restart cost for every failure, no matter how late it happens. Persisting state at natural boundaries and designing every step to be idempotent lets an agent resume from the last completed checkpoint rather than redo work. 

 **Desired outcome:** 
+  You have workflow state persisted at regular checkpoints, so interruptions resume from the last completed point rather than the beginning. 
+  You have idempotent workflow steps that produce the same result when replayed with the same input. 
+  You have a checkpoint lifecycle with TTL-based expiration and explicit cleanup after completion. 

 **Common anti-patterns:** 
+  Running long-duration agent workflows without intermediate state persistence, forcing complete restarts on any failure. 
+  Implementing checkpoints without idempotency guarantees, producing data corruption or duplicate side effects on resume. 
+  Skipping checkpoint cleanup, accumulating storage indefinitely. 

 **Benefits of establishing this best practice:** 
+  Workflow restart cost drops because resume starts from the last checkpoint. 
+  Duplicate work is prevented through idempotent checkpoint-based recovery. 
+  Compute efficiency improves because recovery avoids redundant recomputation. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance"></a>

 Checkpointing is only useful if recovery is safe, and recovery is only safe if steps are idempotent. An idempotent step produces the same result whether it runs once or five times with the same input, which means a retry or a resume doesn't add duplicate side effects. This constraint shapes everything downstream. External calls need idempotency keys, state mutations need conditional writes, and event emissions need deduplication logic. Without idempotency guarantees, checkpoint-based recovery can produce duplicate side effects or data corruption. Design each step to be idempotent before implementing checkpointing. 

 Runtime choice determines how much checkpointing discipline you need to build yourself. [Amazon Bedrock AgentCore Runtime](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/agents-tools-runtime.html) supports long-running workloads with managed session storage that persists filesystem state across stop and resume cycles, which covers the coarse-grained case. For workflow-stage-aware checkpointing with redrive from specific failure points, orchestrate through [AWS Step Functions](https://docs.aws.amazon.com/step-functions/latest/dg/welcome.html). Step Functions persists execution state at every transition and enables restart from the point of failure rather than from the beginning. For dynamic workflows driven by supervisor agents, callback patterns pause execution while the supervisor decides the next action, preserving state persistence benefits. 

 Lifecycle management keeps the checkpoint store from growing without bound. TTL-based expiration handles the common case: workflows that never complete eventually age out. Explicit cleanup after successful completion reclaims space immediately. Use [Amazon Bedrock AgentCore Memory](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/memory.html) to persist checkpoint state and specification context for agents requiring custom checkpointing. Monitor checkpoint store health through [Amazon Bedrock AgentCore Observability](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability.html) so storage growth or access latency surfaces before recovery starts failing. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Deploy agents on AgentCore Runtime with managed session storage:** Use [Amazon Bedrock AgentCore Runtime](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/agents-tools-runtime.html) for filesystem-level state persistence across stop and resume cycles. 

1.  **Orchestrate multi-step workflows through Step Functions:** Use [AWS Step Functions](https://docs.aws.amazon.com/step-functions/latest/dg/welcome.html) for state persistence at every transition with redrive capability from the point of failure. 

1.  **Design every workflow step to be idempotent:** Require idempotency keys on external calls and conditional writes on state mutations so retries and resumes don't introduce duplicate side effects. 

1.  **Use AgentCore Memory for custom checkpoint state:** Persist checkpoint state and specification context through [Amazon Bedrock AgentCore Memory](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/memory.html) for agents with bespoke checkpointing needs. 

1.  **Implement checkpoint lifecycle management:** Set TTL-based expiration and explicit cleanup after successful completion so the checkpoint store stays bounded. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [AGENTREL03-BP01 Design an information classification model to identify short-term and long-term memories](agentrel03-bp01.html) 
+  [AGENTREL03-BP02 Architect fault-tolerant memory stores with redundancy and failover](agentrel03-bp02.html) 
+  [AGENTREL07-BP01 Design workflows in stages with incremental recovery](agentrel07-bp01.html) 

 **Related documents:** 
+  [Amazon Bedrock AgentCore Runtime](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/agents-tools-runtime.html) 
+  [AWS Step Functions](https://docs.aws.amazon.com/step-functions/latest/dg/welcome.html) 
+  [Amazon Bedrock AgentCore Memory](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/memory.html) 
+  [Build resilient generative AI agents](https://aws.amazon.com/blogs/architecture/build-resilient-generative-ai-agents) 

 **Related services:** 
+  [Amazon Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/) 
+  [AWS Step Functions](https://aws.amazon.com/step-functions/) 