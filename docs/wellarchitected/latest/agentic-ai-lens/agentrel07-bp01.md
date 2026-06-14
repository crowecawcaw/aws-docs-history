# AGENTREL07-BP01 Design workflows in stages with incremental recovery

Monolithic workflows lose everything on a single failure. Explicit
stage boundaries with persisted outputs contain failures to the
affected stage and let recovery start from the last completed
checkpoint rather than the beginning.

**Desired outcome:**

- You have workflows decomposed into discrete stages at natural
  checkpoints where completed work has independent value.
- You persist stage outputs durably so recovery resumes from the
  last completed stage.
- You validate stage outputs before advancing so errors don't
  propagate silently through subsequent stages.

**Common anti-patterns:**

- Running workflows as monolithic processes without stage
  boundaries, so any failure forces a complete restart.
- Defining stages at too coarse a granularity, losing large
  amounts of work within a stage when it fails.
- Skipping stage output validation, allowing errors to propagate
  through subsequent stages.

**Benefits of establishing this best
practice:**

- Work loss stays minimal because recovery resumes from the last
  completed stage.
- Recovery is faster because redundant recomputation of completed
  stages is avoided.
- Stage boundaries contain failures, improving error isolation.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

[AWS Step Functions](../../../step-functions/latest/dg/welcome.md "../../../step-functions/latest/dg/welcome.md") persists execution state at every state
transition and enables recovery from the last completed step
rather than restarting entirely. The built-in retry with
exponential backoff handles transient errors within a step, and
the redrive capability restarts the workflow from the point of
failure without re-executing completed steps. This combination,
persistence plus selective retry plus redrive, is what gives
incremental recovery its teeth.
[Amazon
Bedrock AgentCore Runtime](../../../bedrock-agentcore/latest/devguide/agents-tools-runtime.md "../../../bedrock-agentcore/latest/devguide/agents-tools-runtime.md") provides the execution surface
for individual agent steps within the workflow.

Place stage boundaries where completed work has independent value.
A parsed document, a validated query, and a retrieved and
summarized context are all natural boundaries. If a stage produces
a half-built artifact that is useless on its own, the boundary is
in the wrong place.

Quality protection follows stage design. Stage output validation
between stages, checking schema conformance and quality thresholds
before advancing, keeps errors from propagating.
[Amazon
Bedrock AgentCore Evaluations](../../../bedrock-agentcore/latest/devguide/evaluations.md "../../../bedrock-agentcore/latest/devguide/evaluations.md") can verify that recovered
workflow outputs match pre-failure quality baselines, so
incremental recovery doesn't silently degrade quality. Stage-level
timeouts prevent stuck stages from blocking progress indefinitely.
Stage-level metrics through
[Amazon
Bedrock AgentCore Observability](../../../bedrock-agentcore/latest/devguide/observability.md "../../../bedrock-agentcore/latest/devguide/observability.md"), including success rate,
execution time, and timeout frequency, identify stages that need
optimization.

### Implementation steps

1. **Decompose workflows into discrete
   stages:** Place boundaries at natural checkpoints
   where completed work has independent value.
2. **Implement with Step Functions for
   durable state:** Use
   [AWS Step Functions](../../../step-functions/latest/dg/welcome.md "../../../step-functions/latest/dg/welcome.md") with built-in retry and exponential
   backoff per step.
3. **Configure redrive for recovery from
   the point of failure:** Restart failed workflows
   without re-executing completed steps.
4. **Implement stage output
   validation:** Check schema conformance and quality
   thresholds between stages so errors don't propagate.
5. **Configure stage-level timeouts with
   recovery paths:** Handle stages that fail after
   exhausting retries.
6. **Monitor stage-level
   metrics:** Use
   [Amazon
   Bedrock AgentCore Observability](../../../bedrock-agentcore/latest/devguide/observability.md "../../../bedrock-agentcore/latest/devguide/observability.md") to find stages that
   need optimization.

## Resources

**Related best practices:**

- [AGENTREL03-BP03
  Implement comprehensive state management and checkpoint-based
  recovery](agentrel03-bp03.md "agentrel03-bp03.md")
- [AGENTREL07-BP02 Enable
  automatic recovery from agent execution failures](agentrel07-bp02.md "agentrel07-bp02.md")
- [AGENTREL07-BP03
  Implement distributed tracing to track system dependencies and
  facilitate recovery](agentrel07-bp03.md "agentrel07-bp03.md")

**Related documents:**

- [AWS Step Functions](../../../step-functions/latest/dg/welcome.md "../../../step-functions/latest/dg/welcome.md")
- [Amazon
  Bedrock AgentCore Runtime](../../../bedrock-agentcore/latest/devguide/agents-tools-runtime.md "../../../bedrock-agentcore/latest/devguide/agents-tools-runtime.md")
- [Build
  resilient generative AI agents](https://aws.amazon.com/blogs/architecture/build-resilient-generative-ai-agents "https://aws.amazon.com/blogs/architecture/build-resilient-generative-ai-agents")
- [Planning
  for failure: How to make generative AI workloads more
  resilient](https://aws.amazon.com/blogs/publicsector/planning-for-failure-how-to-make-generative-ai-workloads-more-resilient/ "https://aws.amazon.com/blogs/publicsector/planning-for-failure-how-to-make-generative-ai-workloads-more-resilient/")

**Related videos:**

- [AWS 2025 - AgentCore now GA: From Prototype to Production](https://www.youtube.com/watch?v=WyGK8UcAxKo "https://www.youtube.com/watch?v=WyGK8UcAxKo")

**Related services:**

- [AWS Step Functions](https://aws.amazon.com/step-functions/ "https://aws.amazon.com/step-functions/")
- [Amazon
  Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/ "https://aws.amazon.com/bedrock/agentcore/")
- [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/ "https://aws.amazon.com/cloudwatch/")
