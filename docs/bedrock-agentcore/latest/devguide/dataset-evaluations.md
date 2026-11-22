

# Dataset evaluation

**Note**  
Dataset evaluation is in public preview. Features and APIs may change before general availability.

Dataset evaluations run your agent against a set of scenarios and automatically evaluate the results. You can have the AgentCore service invoke an AgentCore Runtime endpoint, or use an AgentCore SDK runner so that your code invokes the agent.

This is useful for regression testing, benchmark datasets, CI/CD pipelines, baseline measurement, and pre/post comparison after configuration changes.

All three options use the same [dataset schema](dataset-evaluations-schema.md) and ground truth format:
+  **AgentCore-run dataset evaluation** — AgentCore invokes your HTTP AgentCore Runtime endpoint that uses AWS Identity and Access Management (IAM) authorization. It then evaluates the sessions in a batch evaluation job.
+  **SDK on-demand dataset runner** (`OnDemandEvaluationDatasetRunner`) — Your code invokes the agent, collects spans, and calls the Evaluate API.
+  **SDK batch dataset runner** (`BatchEvaluationRunner`) — Your code invokes the agent, and then submits the sessions to the batch evaluation service.

## Choose how to run a dataset evaluation
<a name="dataset-evaluations-choose"></a>


| Aspect | AgentCore-run dataset evaluation | SDK on-demand runner | SDK batch runner | 
| --- | --- | --- | --- | 
| Who invokes your agent | AgentCore | Your code, through an agent invoker callable | Your code, through an agent invoker callable | 
| Agent location | AgentCore Runtime only | Any agent that your invoker can call | Any agent that sends telemetry to CloudWatch Logs and that your invoker can call | 
| Runtime inbound authorization | IAM (SigV4) only | IAM or JWT, handled by your invoker | IAM or JWT, handled by your invoker | 
| Runtime protocol | HTTP server protocol only | HTTP, MCP, A2A, or another protocol handled by your invoker | HTTP, MCP, A2A, or another protocol handled by your invoker | 
| Request construction |  `requestTemplate`  | Your invoker | Your invoker | 
| Simulated user | AgentCore-managed model | Model that you choose in `SimulationConfig`  | Model that you choose in `SimulationConfig`  | 
| Requires a running client process | No | Yes | Yes | 
| Evaluation processing | Service-side batch evaluation | SDK calls the Evaluate API for each evaluator and scenario | Service-side batch evaluation after the SDK invokes the scenarios | 
| Results | Aggregate results, with per-session detail in CloudWatch Logs | Structured per-scenario and per-evaluator results | Aggregate results, with per-session detail in CloudWatch Logs | 
| Best for | Managed regression runs against an IAM-authorized HTTP Runtime | Dev-time iteration, CI/CD, and immediate per-scenario detail | Custom invocation with server-side aggregate evaluation | 

To use the AgentCore-run option, see [Run a dataset evaluation with AgentCore Evaluations](batch-evaluations-dataset.md). To use an SDK option, see [SDK on-demand dataset runner](dataset-evaluations-on-demand.md) or [SDK batch dataset runner](dataset-evaluations-batch.md).

 **SDK runner prerequisites** 

The SDK runners require:
+ Python 3.10\+
+ An agent built with a supported framework and instrumentation library. For more information about supported frameworks and instrumentation libraries, see [Supported agent frameworks](supported-frameworks.md).
+ An agent deployed on AgentCore Runtime with observability enabled, or an agent built with a supported framework configured with [AgentCore Observability](observability.md), including Transaction Search. For more information about telemetry setup, see [Telemetry setup and delivery](supported-frameworks-telemetry.md).
+ The AgentCore SDK installed: `pip install bedrock-agentcore` 
+  AWS credentials configured with permissions for `bedrock-agentcore`, `bedrock-agentcore-control`, and `logs` (CloudWatch)

**Topics**