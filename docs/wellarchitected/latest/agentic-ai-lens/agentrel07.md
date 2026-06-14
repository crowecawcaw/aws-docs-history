# Agent monitoring, management and recovery

Agent systems that decompose workflows into recoverable stages,
classify failures for targeted retry, and implement end-to-end
distributed tracing recover smoothly from the failures that occur
across their many components.

| AGENTREL07: How do fault tolerant agent systems recover? |
| -------------------------------------------------------- |
|                                                          |

## Capability intent

- Agent workflows are decomposed into stages with persisted
  outputs and explicit validation between them, so failures
  are contained to the affected stage rather than cascading
  through the whole workflow.
- Failures are classified before any recovery action is taken,
  so retries apply to transient errors, fallbacks apply to
  persistent ones, and only genuinely unrecoverable failures
  reach human attention.
- Retries use exponential backoff with jitter and a retry
  budget, so widespread upstream failures don't produce
  unbounded retry storms.
- Self-healing responses address common failure patterns
  directly (prompt refinement, tool substitution, context
  reconstruction) before escalating to fallbacks.
- End-to-end distributed tracing covers every agent
  invocation, with agent-specific annotations and
  framework-level reasoning steps captured in the same trace
  view.
- Traces, metrics, and logs are correlated in unified
  dashboards, so operators diagnose incidents from evidence
  rather than by pivoting between tools.

## Maturity levels

These levels summarize what each stage of maturity looks like
for agent monitoring, management and recovery as a whole.

| Level | Name      | What it looks like                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| ----- | --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 1     | Initial   | Agent workflows run as monolithic processes, so any<br>failure causes a complete restart and lost work. Retries<br>are applied uniformly, including to non-retryable<br>errors, and without exponential backoff or jitter.<br>Tracing is limited to the application boundary, and<br>incident responders reconstruct the execution path from<br>logs. Recovery actions are manual.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| 2     | Emerging  | A few long-running workflows are split into stages, and<br>retries use exponential backoff for a limited set of<br>known-transient errors.<br>[Amazon CloudWatch](../../../AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.md "../../../AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.md") alarms notify operators on elevated<br>error rates. Tracing is added for critical paths but<br>doesn't propagate across queue boundaries. Failure<br>classification exists in one-time code rather than a<br>shared library.                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| 3     | Defined   | Workflows are orchestrated in<br>[AWS Step Functions](../../../step-functions/latest/dg/welcome.md "../../../step-functions/latest/dg/welcome.md") with state persistence at every<br>transition and<br>[redrive](../../../step-functions/latest/dg/redrive-executions.md "../../../step-functions/latest/dg/redrive-executions.md")<br>enabled for incremental recovery. Failure classification<br>is standardized in a shared library, and retries use<br>exponential backoff with full jitter.<br>[Amazon<br>Bedrock AgentCore Observability](../../../bedrock-agentcore/latest/devguide/observability.md "../../../bedrock-agentcore/latest/devguide/observability.md") captures<br>end-to-end traces across agent components, and<br>[Amazon<br>Bedrock AgentCore Policy](../../../bedrock-agentcore/latest/devguide/policy.md "../../../bedrock-agentcore/latest/devguide/policy.md") enforces retry budgets.<br>Stage-level validation helps prevent errors from<br>propagating through later stages. |
| 4     | Proactive | Self-healing responses address common failure patterns<br>directly (prompt refinement, tool substitution, context<br>reconstruction) before fallbacks engage. Fallback<br>strategies route persistent failures to degraded<br>responses, cached answers, or human review queues rather<br>than returning errors. Distributed tracing includes<br>agent-specific annotations and<br>[Strands<br>Agents](https://strandsagents.com/docs/user-guide/observability-evaluation/traces/ "https://strandsagents.com/docs/user-guide/observability-evaluation/traces/") reasoning steps, and trace context<br>propagates through every communication path including<br>asynchronous messages.<br>[Amazon<br>Bedrock AgentCore Evaluations](../../../bedrock-agentcore/latest/devguide/evaluations.md "../../../bedrock-agentcore/latest/devguide/evaluations.md") validate that<br>recovered outputs match pre-failure quality baselines.                                                                            |
| 5     | Optimized | Recovery strategies are continuously refined based on<br>recovery metrics and trace analysis. Fallback paths are<br>tested alongside primary implementations, and stage<br>decomposition is driven by observed failure and timeout<br>patterns. Trace-based alerting fires on anomalies before<br>they become incidents, and correlated dashboards turn<br>traces, metrics, and logs into a single investigative<br>surface. The organization publishes internal recovery<br>patterns and shares lessons across teams.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |

## Common issues to watch for

- Long-running workflows run as monolithic processes, so a
  failure late in the workflow loses all progress and forces
  complete restart.
- Retry logic is applied uniformly to every failure, retrying
  non-retryable errors that will never succeed and delaying
  the human intervention that would resolve them.
- Retries run at fixed intervals without exponential backoff
  or jitter, producing thundering-herd effects that amplify
  incidents rather than recovering from them.
- Only retry-based recovery is implemented, so persistent
  failures after retries become user-visible errors instead of
  degrading through a fallback.
- Tracing stops at the application boundary or at queue
  boundaries, so debugging failures in multi-agent systems
  depends on manual log correlation across services.
- Traces are captured without agent-specific annotations, so
  trace queries can't be filtered down to the specific agent,
  task type, or model that failed.

###### Best practices

- [AGENTREL07-BP01 Design workflows in stages with incremental recovery](agentrel07-bp01.md "agentrel07-bp01.md")
- [AGENTREL07-BP02 Enable automatic recovery from agent execution failures](agentrel07-bp02.md "agentrel07-bp02.md")
- [AGENTREL07-BP03 Implement distributed tracing to track system dependencies and facilitate recovery](agentrel07-bp03.md "agentrel07-bp03.md")
