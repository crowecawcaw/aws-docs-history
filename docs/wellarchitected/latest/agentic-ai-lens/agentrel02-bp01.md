

# AGENTREL02-BP01 Design agents for specific and atomic tasks
<a name="agentrel02-bp01"></a>

 LLM outputs are stochastic, so the scope of an agent's responsibility is also the scope of that stochasticity. Narrow, atomic agents with explicit input contracts and structured output schemas make the unpredictable parts of the model more observable, testable, and containable. 

 **Desired outcome:** 
+  You have each agent scoped to one atomic function with explicit input validation and a structured output schema. 
+  Your agents are tested with deterministic, representative inputs before deployment. 
+  You track per-agent quality metrics (schema compliance rate and task completion rate) so regressions appear before users see them. 

 **Common anti-patterns:** 
+  Building multi-purpose agents that combine disparate functions, widening the surface area for unpredictable model behavior. 
+  Skipping explicit input contracts and output schemas, allowing ambiguous data flows that amplify LLM stochasticity. 
+  Treating agents as general-purpose processors without discrete responsibilities, making issue reproduction hard. 

 **Benefits of establishing this best practice:** 
+  Constrained scope shrinks the surface for unpredictable behavior. 
+  Composable units can be independently validated with deterministic test cases. 
+  Clear operational boundaries speed up issue identification and remediation. 

 **Level of risk exposed if this best practice is not established:** Medium 

## Implementation guidance
<a name="implementation-guidance"></a>

 Atomic design starts with the prompt. A single, well-defined system prompt that describes exactly one capability is the easiest constraint to enforce and the hardest to violate silently. Pair it with explicit input validation that rejects out-of-scope requests before the LLM is invoked, and a structured output schema that constrains the response format. Amazon Bedrock's tool use (function calling) limits the model's action space to operations relevant to the agent's function. Amazon Bedrock's [structured output](https://docs.aws.amazon.com/bedrock/latest/userguide/structured-output.html) feature enforces JSON schema compliance at the model level to reduce output validation failures. 

 Deployment reinforces the atomic boundary. Each agent runs on [Amazon Bedrock AgentCore Runtime](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/agents-tools-runtime.html) with its own execution context and dedicated tool permissions, so a misconfigured or compromised agent can't reach beyond its scope. This gives you a physical boundary that matches the logical one you defined in the prompt. 

 Testing is where atomic design pays off. Because each agent has a narrow contract, you can run [Amazon Bedrock AgentCore Evaluations](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/evaluations.html) against representative inputs and compare outputs to expected results. LLM outputs are not fully deterministic even with temperature=0, so the tests should validate semantic correctness rather than exact string matching. Monitoring each agent through [Amazon Bedrock AgentCore Observability](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability.html) tracks schema compliance rate and task completion rate, with alarms when metrics drift from baselines. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Decompose workflows into atomic agents:** Give each agent a single system prompt, a constrained tool set, and explicit input/output schemas. 

1.  **Deploy on AgentCore Runtime with structured output enforcement:** Run each agent on [Amazon Bedrock AgentCore Runtime](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/agents-tools-runtime.html) with dedicated tool permissions and [Bedrock structured output](https://docs.aws.amazon.com/bedrock/latest/userguide/structured-output.html) enforcement. 

1.  **Implement input validation that rejects out-of-scope requests:** Validate inputs before the LLM is called so malformed or out-of-scope requests don't reach the model. 

1.  **Validate behavior with AgentCore Evaluations:** Use [Amazon Bedrock AgentCore Evaluations](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/evaluations.html) with representative inputs and golden-path test cases, asserting semantic correctness rather than exact strings. 

1.  **Monitor per-agent quality metrics:** Track schema compliance rate and task completion rate through [Amazon Bedrock AgentCore Observability](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability.html) with alarms for baseline deviations. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [AGENTREL01-BP03 Design specialized agents following actor model principles](agentrel01-bp03.html) 
+  [AGENTREL02-BP02 Limit agent permissions to minimum required access](agentrel02-bp02.html) 
+  [AGENTREL02-BP03 Implement behavioral anomaly detection and monitoring](agentrel02-bp03.html) 
+  [AGENTREL02-BP04 Develop clear instruction protocols for agents](agentrel02-bp04.html) 

 **Related documents:** 
+  [Amazon Bedrock AgentCore Runtime](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/agents-tools-runtime.html) 
+  [Amazon Bedrock AgentCore Evaluations](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/evaluations.html) 
+  [Build reliable AI agents with Amazon Bedrock AgentCore Evaluations](https://aws.amazon.com/blogs/machine-learning/build-reliable-ai-agents-with-amazon-bedrock-agentcore-evaluations/) 
+  [Amazon Bedrock structured output](https://docs.aws.amazon.com/bedrock/latest/userguide/structured-output.html) 
+  [Strands Agents Custom Tools](https://strandsagents.com/docs/user-guide/concepts/tools/custom-tools/) 

 **Related videos:** 
+  [Strands Tools: Building Custom AI Agents with Python](https://www.youtube.com/watch?v=EGhIZCfOvG4) 

 **Related examples:** 
+  [GitHub: awslabs/amazon-bedrock-agentcore-samples - Evaluations tutorials](https://github.com/awslabs/amazon-bedrock-agentcore-samples/tree/main/01-tutorials/07-AgentCore-evaluations) 

 **Related tools:** 
+  [Strands Agents](https://strandsagents.com/) 

 **Related services:** 
+  [Amazon Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/) 