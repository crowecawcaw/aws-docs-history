# GENCOST05-BP01 Create stopping conditions to control

long-running workflows

Agentic workflows can be long-running, which can incur additional cost
to your application. Develop controls to limit agents from running
for extended periods of time without stopping.

**Desired outcome:** Maximum costs
for an agent's runtime can be predicted based on the implemented
stopping conditions.

**Benefits of establishing this best
practice:**
[Measure
overall efficiency](../framework/cost-dp.md "../framework/cost-dp.md") - Agentic workflows can be long-running, which can add additional cost to your workload. By establishing stopping conditions for long-running agentic workflows, you can optimize resources, improve user experience, and optimize workload costs.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

For generative AI prompt flows where you lack control over the
duration of the workflow, consider introducing a time-out
mechanism or regaining control over the flow. This scenario is
particularly common within agentic architectures. Agent
architectures assist customers by taking on additional tasks.
Sometimes these tasks can run for an extended duration, which may
incur additional cost considerations, especially when they call
external resources. Consider introducing a timeout over the agent
to limit long-running processes from incurring costs
unnecessarily. Additionally, evaluate asynchronous workflows
orchestrated through events. Asynchronous workflows create
opportunities to interrupt or halt long-running events after an
extended duration. Consider the entire architecture before
determining the best place to interrupt long-running workflows for
cost savings.

### Implementation steps

1. Estimate the maximum time needed for an agent to complete
   its runtime.
   - Include model response times, tool execution times, and network latency in the estimation.

2. Implement stopping conditions that enable an agent to run to
   the maximum duration.
   - Stopping conditions may be a timeout mechanism like the
     one in Amazon Bedrock.
   - Alternatively, stopping conditions may be implemented in
     the prompt flow layer or within a software abstraction
     layer.

3. Re-architect your workflows to facilitate stopping conditions.
   - Set timeouts on external tools such as Lambda functions or API endpoints, verify that your prompts understand how to handle timeout responses.
   - Set token limits on model responses to simulate timeout functionality by stopping models from printing long-running responses.

## Resources

**Related best practices:**

- [COST01-BP06](../cost-optimization-pillar/cost_cloud_financial_management_proactive_process.md "../cost-optimization-pillar/cost_cloud_financial_management_proactive_process.md")

**Related documents:**

- [AWS re:Invent 2023

* Simplify generative AI app development with Agents for
  Amazon Bedrock (AIM353)](https://www.youtube.com/watch?v=JNZPW82uv7w "https://www.youtube.com/watch?v=JNZPW82uv7w")

- [User
  Guide: Amazon Bedrock Agents](../../../bedrock/latest/userguide/agents.md "../../../bedrock/latest/userguide/agents.md")

**Related examples:**

- [Best
  practices for building robust generative AI applications with
  Amazon Bedrock Agents - Part 1](https://aws.amazon.com/blogs/machine-learning/best-practices-for-building-robust-generative-ai-applications-with-amazon-bedrock-agents-part-1/ "https://aws.amazon.com/blogs/machine-learning/best-practices-for-building-robust-generative-ai-applications-with-amazon-bedrock-agents-part-1/")
- [Best
  practices for building robust generative AI applications with
  Amazon Bedrock Agents - Part 2](https://aws.amazon.com/blogs/machine-learning/best-practices-for-building-robust-generative-ai-applications-with-amazon-bedrock-agents-part-2/ "https://aws.amazon.com/blogs/machine-learning/best-practices-for-building-robust-generative-ai-applications-with-amazon-bedrock-agents-part-2/")
