

# ADVPERF02-BP06 Use a managed serverless runtime for AI agent compute
<a name="advperf02-bp06"></a>

 Run AI agent workloads on a managed serverless runtime instead of self-managed containers, so agent sessions scale automatically with request volume and you avoid provisioning and operating the underlying compute. On AWS, [Amazon Bedrock AgentCore Runtime](https://aws.amazon.com/bedrock/agentcore/) provides this model, with serverless execution, built-in session management, automatic scaling, and deployment workflows. This removes the operational overhead of running AI advertising agents on self-managed containers. 

 **Desired outcome:** 
+  Your AI agent workloads scale automatically with request volume (adding sessions during traffic spikes and releasing them during quieter periods) without requiring you to provision, configure, or operate the underlying infrastructure. 
+  Session state persists across invocations within the session timeout window, and warm sessions are reused to avoid cold-start penalties on the critical path. 
+  Agent infrastructure cost scales proportionally with bid volume and campaign activity, avoiding idle compute during off-peak periods. 

 **Common anti-patterns:** 
+  Managing agent infrastructure manually adds operational complexity that can degrade performance under burst traffic. 
+  Manual scaling policies that react to CloudWatch alarms introduce a detection-to-action delay (typically one to several minutes) during which new agent requests either queue or fail. 
+  Custom session management requires implementing sticky routing, session state persistence, and health checking on top of every request. 

 **Benefits of establishing this best practice:** 
+  AgentCore Runtime removes the undifferentiated heavy lifting of managing agent infrastructure. Automatic scaling, built-in session management, and serverless execution let your team focus on agent logic rather than capacity planning. 
+  For advertising workloads where AI agents handle bid optimization, audience scoring, or creative selection under burst conditions, removing manual scaling lag directly improves p99 request latency and session consistency. 
+  Warm session reuse avoids the startup penalty that Lambda cold starts and Fargate task launches incur on each new burst. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance"></a>

 AI agents are increasingly central to advertising platforms, managing bid optimization, dynamic creative selection, media planning, brand safety assessment, and campaign pacing. These agent workloads share a common operational challenge in session management at advertising scale. 

 For workflows that span multiple agent invocations, context from earlier steps (campaign constraints, audience data, budget state) must be available in later steps within the same session. Without session persistence, each invocation reloads context, which increases token consumption and latency. With managed session state, warm sessions retain that context without reinitialization. 

 AgentCore Runtime provides managed session state with a serverless execution model that routes sessions, persists state, and scales automatically. When a request arrives for an existing session, AgentCore routes it to a warm container with the session context loaded. It provisions new sessions when demand grows and releases them when demand falls. 

 For advertising workloads, AgentCore's automatic scaling is valuable during campaign launches and live events, when AI agent invocation rates spike as advertisers increase campaign activity. Under a self-managed ECS or EKS deployment with CloudWatch-triggered auto scaling, this spike triggers alarms, scale policies execute, new tasks provision, and by the time capacity is available, the peak might have already passed. 

 The default 15-minute idle session timeout is appropriate for most advertising agent workflows. Campaign planning sessions, creative review workflows, and bid optimization sessions that span multiple agent invocations can all complete within this window. For longer-running workflows, implement an application-level checkpoint mechanism that persists state to DynamoDB or S3 and rehydrates it at the start of a new session. 

### Considerations
<a name="considerations"></a>
+  **Region availability:** AgentCore Runtime is available in a subset of AWS Regions (20 at the time of writing, including AWS GovCloud US-West). Confirm availability in your target Regions against [Supported AWS Regions for AgentCore](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/agentcore-regions.html) before committing the architecture, and default active-session quotas are higher in us-east-1 and us-west-2 than in other Regions. 
+  **Session timeouts:** the 15-minute figure is the *default idle session timeout*, adjustable from 1 minute to 8 hours through the lifecycle configuration's idleRuntimeSessionTimeout, alongside a maxLifetime maximum session duration (default 8 hours). Separately, a single synchronous invocation has a hard, non-adjustable 15-minute ceiling. See [AgentCore lifecycle settings](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/runtime-lifecycle-settings.html). 
+  **Cold-start behavior:** AgentCore Runtime doesn't publish a cold-start latency figure. New-session startup varies with deployment type (container image size or direct code package) and initialization work (model loading, tool registration, and memory hydration). Reusing session IDs for session affinity and caching initialization artifacts on the session's persistent filesystem are the documented mitigations. Monitor p99 session startup time (step 5) to quantify it for your workload. 
+  **Service quotas:** session creation rates, concurrent active sessions, and invocation payload sizes are bounded per Region. Review [Quotas for Amazon Bedrock AgentCore](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/bedrock-agentcore-limits.html) and request increases ahead of campaign-launch traffic peaks. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Deploy AI agent workloads on Amazon Bedrock AgentCore Runtime instead of self-managed containers:** Package your advertising agent logic as an AgentCore-compatible application using the app.entrypoint decorator pattern. Deploy using the AgentCore deployment APIs rather than pushing container images to ECS or EKS. Verify that agent initialization (model loading, tool registration, system prompt configuration) completes within the session startup window. 

1.  **Design agent invocations to use warm session reuse:** Structure your advertising agent workflows to make multiple invocations within a single session where the workflow has multiple steps (for example: brief analysis → audience selection → creative recommendations → campaign structure generation). This reuses the warm session context rather than reinitializing the agent on each step, reducing both latency and token consumption for context reconstruction. 

1.  **Rely on AgentCore Runtime's automatic scaling for burst traffic events:** Remove manual auto scaling configurations (CloudWatch alarms, scaling policies, target tracking) that you previously used to scale ECS tasks or EKS pods for agent workloads. AgentCore handles scaling based on real-time request volume. For advertising campaigns with known launch windows, no pre-scaling action is required. AgentCore responds to the actual traffic as it arrives. 

1.  **Implement application-level checkpointing for workflows that exceed the session timeout:** For advertising agent workflows that may span more than 15 minutes (complex media planning sessions, large-scale audience analysis), implement a checkpoint mechanism at natural pause points. Persist the workflow state to [Amazon DynamoDB](https://aws.amazon.com/dynamodb/) with the session ID as the key. At the start of a new session, check for an existing checkpoint and rehydrate state before continuing the workflow. 

1.  **Monitor AgentCore Runtime performance with CloudWatch:** Enable CloudWatch metrics for AgentCore Runtime and monitor session startup time, warm session hit rate, invocation latency, and error rates. Set alarms on p99 session startup time to detect when cold starts are affecting agent response times. Track warm session utilization to validate that session reuse is occurring as expected for your advertising agent workflows. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [ADVPERF01-BP04 Evaluate AI/ML-based architecture for optimization](advperf01-bp04.md) 

 **Related documents:** 
+  [Amazon Bedrock AgentCore Runtime Getting started](https://docs.aws.amazon.com/bedrock/latest/userguide/agentcore-runtime.html) 
+  [What is Amazon Bedrock AgentCore?](https://docs.aws.amazon.com/bedrock/latest/userguide/agentcore.html) 
+  [Guidance for Advertising Agents on AWS](https://aws.amazon.com/solutions/guidance/advertising-agents-on-aws/) 

 **Related services:** 
+  [Amazon Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/) 