# GENREL03-BP02 Implement timeout mechanisms on agentic

workflows

Implement controls to detect and terminate long-running unexpected
workflows.

**Desired outcome:** When
implemented, this best practice improves the reliability of your
generative AI workload by freeing resources that might have been
consumed by unexpected long-running execution loops.

**Benefits of establishing this best
practice:**
[Automatically
recover from failure](../framework/rel-dp.md "../framework/rel-dp.md") - Implementing agent timeouts helps to
reduce the likelihood of blocking failures on agentic workflows and
executions.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Agentic workflows take action on behalf of a user by making calls
to external systems. External systems may themselves perform
several time-consuming tasks which the agent is not aware of,
resulting in idle agents that could run for an extended period of
time. In order to maintain a reliable agentic system, customers
should implement controls to manage agentic timeout.

One approach to controlling agentic runtime or lifecycle is to
implement runtime timeouts on the external infrastructure. For
example, if an agent makes a call to an AWS Lambda function
through an Action Group, consider applying a timeout to the
corresponding Lambda function. The timeout should be set to
include the maximum allowable time needed to complete a process,
accounting for additional latency for edge cases such as a Lambda
cold start. You may consider rounding this value up to avoid
unnecessary early terminations.

Alternatively, customers may consider connecting their agentic
workflows to an event system, developing an asynchronous process
management architecture. Introducing an asynchronous event system
gives users the most flexibility and visibility into agent process
lifecycle or flow. By requiring the compute underpinning an Amazon Bedrock Action Group to publish events, workload owners maintain
insight into where an agent may encounter stalled flow or process.
Consider using events to publish agent updates and take action
appropriately to prevent long-running invocations.

Error handling at the agent layer should be transparent to users.
When errors occur, communicate clear details about the issue while
maintaining system security by avoiding exposure of sensitive
internal information. The response should outline specific next
steps so that users can complete their tasks independently if the
agent remains unavailable. This approach promotes operational
resilience while maintaining security best practices, as users
receive actionable guidance without compromising system integrity.
The error messaging framework should focus on user experience by
providing alternative paths to task completion while adhering to
the principle of least-privilege in information disclosure.

### Implementation steps

1. Create an agent within Amazon Bedrock Agents.
2. Define an action group with one or more pieces of supporting
   compute infrastructure.
3. Implement control logic over the supporting infrastructure.
   - Timeouts are an effective control mechanism. Implement
     time-outs at the agent layer to terminate a session
     waiting for a prompt from a user.
   - Alternatively, timeouts can be implemented externally.
     AWS Lambda action groups can be configured with timeouts
     and dead letter queues to halt the execution of an
     external process.
   - Explore asynchronous event publishing to complement
     timeouts and other control mechanisms.

4. Develop recovery logic for the agent to prevent the build-up
   of half-completed executions.

## Resources

**Related practices:**

- [REL05-BP05](../reliability-pillar/rel_mitigate_interaction_failure_client_timeouts.md "../reliability-pillar/rel_mitigate_interaction_failure_client_timeouts.md")

**Related guides, videos, and documentation:**

- [AWS re:Invent 2023

* Simplify generative AI app development with Agents for
  Amazon Bedrock (AIM353)](https://www.youtube.com/watch?v=JNZPW82uv7w "https://www.youtube.com/watch?v=JNZPW82uv7w")

- [Automate tasks in
  your application using AI agents](../../../bedrock/latest/userguide/agents.md "../../../bedrock/latest/userguide/agents.md")

**Related examples:**

- [Best
  practices for building robust generative AI applications with
  Amazon Bedrock Agents - Part 1](https://aws.amazon.com/blogs/machine-learning/best-practices-for-building-robust-generative-ai-applications-with-amazon-bedrock-agents-part-1/ "https://aws.amazon.com/blogs/machine-learning/best-practices-for-building-robust-generative-ai-applications-with-amazon-bedrock-agents-part-1/")
- [Best
  practices for building robust generative AI applications with
  Amazon Bedrock Agents - Part 2](https://aws.amazon.com/blogs/machine-learning/best-practices-for-building-robust-generative-ai-applications-with-amazon-bedrock-agents-part-2/ "https://aws.amazon.com/blogs/machine-learning/best-practices-for-building-robust-generative-ai-applications-with-amazon-bedrock-agents-part-2/")
