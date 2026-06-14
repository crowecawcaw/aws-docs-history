# AGENTREL02-BP01 Design agents for specific and atomic tasks

LLM outputs are stochastic, so the scope of an agent's
responsibility is also the scope of that stochasticity. Narrow,
atomic agents with explicit input contracts and structured output
schemas make the unpredictable parts of the model more observable,
testable, and containable.

**Desired outcome:**

- You have each agent scoped to one atomic function with explicit
  input validation and a structured output schema.
- Your agents are tested with deterministic, representative inputs
  before deployment.
- You track per-agent quality metrics (schema compliance rate and
  task completion rate) so regressions appear before users see
  them.

**Common anti-patterns:**

- Building multi-purpose agents that combine disparate functions,
  widening the surface area for unpredictable model behavior.
- Skipping explicit input contracts and output schemas, allowing
  ambiguous data flows that amplify LLM stochasticity.
- Treating agents as general-purpose processors without discrete
  responsibilities, making issue reproduction hard.

**Benefits of establishing this best
practice:**

- Constrained scope shrinks the surface for unpredictable
  behavior.
- Composable units can be independently validated with
  deterministic test cases.
- Clear operational boundaries speed up issue identification and
  remediation.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

Atomic design starts with the prompt. A single, well-defined
system prompt that describes exactly one capability is the easiest
constraint to enforce and the hardest to violate silently. Pair it
with explicit input validation that rejects out-of-scope requests
before the LLM is invoked, and a structured output schema that
constrains the response format. Amazon Bedrock's tool use
(function calling) limits the model's action space to operations
relevant to the agent's function. Amazon Bedrock's
[structured
output](../../../bedrock/latest/userguide/structured-output.md "../../../bedrock/latest/userguide/structured-output.md") feature enforces JSON schema compliance at the model
level to reduce output validation failures.

Deployment reinforces the atomic boundary. Each agent runs on
[Amazon
Bedrock AgentCore Runtime](../../../bedrock-agentcore/latest/devguide/agents-tools-runtime.md "../../../bedrock-agentcore/latest/devguide/agents-tools-runtime.md") with its own execution context
and dedicated tool permissions, so a misconfigured or compromised
agent can't reach beyond its scope. This gives you a physical
boundary that matches the logical one you defined in the prompt.

Testing is where atomic design pays off. Because each agent has a
narrow contract, you can run
[Amazon
Bedrock AgentCore Evaluations](../../../bedrock-agentcore/latest/devguide/evaluations.md "../../../bedrock-agentcore/latest/devguide/evaluations.md") against representative inputs
and compare outputs to expected results. LLM outputs are not fully
deterministic even with temperature=0, so the tests should
validate semantic correctness rather than exact string matching.
Monitoring each agent through
[Amazon
Bedrock AgentCore Observability](../../../bedrock-agentcore/latest/devguide/observability.md "../../../bedrock-agentcore/latest/devguide/observability.md") tracks schema compliance
rate and task completion rate, with alarms when metrics drift from
baselines.

### Implementation steps

1. **Decompose workflows into atomic
   agents:** Give each agent a single system prompt, a
   constrained tool set, and explicit input/output schemas.
2. **Deploy on AgentCore Runtime with
   structured output enforcement:** Run each agent on
   [Amazon
   Bedrock AgentCore Runtime](../../../bedrock-agentcore/latest/devguide/agents-tools-runtime.md "../../../bedrock-agentcore/latest/devguide/agents-tools-runtime.md") with dedicated tool
   permissions and
   [Bedrock
   structured output](../../../bedrock/latest/userguide/structured-output.md "../../../bedrock/latest/userguide/structured-output.md") enforcement.
3. **Implement input validation that
   rejects out-of-scope requests:** Validate inputs
   before the LLM is called so malformed or out-of-scope
   requests don't reach the model.
4. **Validate behavior with AgentCore
   Evaluations:** Use
   [Amazon
   Bedrock AgentCore Evaluations](../../../bedrock-agentcore/latest/devguide/evaluations.md "../../../bedrock-agentcore/latest/devguide/evaluations.md") with representative
   inputs and golden-path test cases, asserting semantic
   correctness rather than exact strings.
5. **Monitor per-agent quality
   metrics:** Track schema compliance rate and task
   completion rate through
   [Amazon
   Bedrock AgentCore Observability](../../../bedrock-agentcore/latest/devguide/observability.md "../../../bedrock-agentcore/latest/devguide/observability.md") with alarms for
   baseline deviations.

## Resources

**Related best practices:**

- [AGENTREL01-BP03
  Design specialized agents following actor model
  principles](agentrel01-bp03.md "agentrel01-bp03.md")
- [AGENTREL02-BP02 Limit
  agent permissions to minimum required access](agentrel02-bp02.md "agentrel02-bp02.md")
- [AGENTREL02-BP03
  Implement behavioral anomaly detection and monitoring](agentrel02-bp03.md "agentrel02-bp03.md")
- [AGENTREL02-BP04 Develop
  clear instruction protocols for agents](agentrel02-bp04.md "agentrel02-bp04.md")

**Related documents:**

- [Amazon
  Bedrock AgentCore Runtime](../../../bedrock-agentcore/latest/devguide/agents-tools-runtime.md "../../../bedrock-agentcore/latest/devguide/agents-tools-runtime.md")
- [Amazon
  Bedrock AgentCore Evaluations](../../../bedrock-agentcore/latest/devguide/evaluations.md "../../../bedrock-agentcore/latest/devguide/evaluations.md")
- [Build
  reliable AI agents with Amazon Bedrock AgentCore
  Evaluations](https://aws.amazon.com/blogs/machine-learning/build-reliable-ai-agents-with-amazon-bedrock-agentcore-evaluations/ "https://aws.amazon.com/blogs/machine-learning/build-reliable-ai-agents-with-amazon-bedrock-agentcore-evaluations/")
- [Amazon
  Bedrock structured output](../../../bedrock/latest/userguide/structured-output.md "../../../bedrock/latest/userguide/structured-output.md")
- [Strands
  Agents Custom Tools](https://strandsagents.com/docs/user-guide/concepts/tools/custom-tools/ "https://strandsagents.com/docs/user-guide/concepts/tools/custom-tools/")

**Related videos:**

- [Strands
  Tools: Building Custom AI Agents with Python](https://www.youtube.com/watch?v=EGhIZCfOvG4 "https://www.youtube.com/watch?v=EGhIZCfOvG4")

**Related examples:**

- [GitHub:
  awslabs/amazon-bedrock-agentcore-samples - Evaluations
  tutorials](https://github.com/awslabs/amazon-bedrock-agentcore-samples/tree/main/01-tutorials/07-AgentCore-evaluations "https://github.com/awslabs/amazon-bedrock-agentcore-samples/tree/main/01-tutorials/07-AgentCore-evaluations")

**Related tools:**

- [Strands
  Agents](https://strandsagents.com/ "https://strandsagents.com/")

**Related services:**

- [Amazon
  Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/ "https://aws.amazon.com/bedrock/agentcore/")
