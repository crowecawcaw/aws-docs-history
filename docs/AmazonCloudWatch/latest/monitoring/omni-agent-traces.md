

# Agent traces
<a name="omni-agent-traces"></a>

Use Agent traces to find the agent runs you need to inspect, open a run to see what the agent did, and act on what you find: score runs with evaluators, turn failures into dataset test cases, and compare runs side by side. A trace records one complete agent run; a span records one operation within it, such as a model invocation, a tool call, or a retrieval. For the full trace, span, and session vocabulary, see [Monitor AI agents](omni-monitor-ai-agents.md).

For traces of requests crossing your services and dependencies, see [Application traces](omni-application-traces.md).

**Open Agent traces**

In the launcher, under Agent observability, choose `Agent traces`, then select the time range you want to investigate. The summary above the results shows totals for the selected range, such as Total traces, Traces with errors, duration, and token usage.

The IDE extension has the same view for the traces your agent produces while you develop. In local mode it reads the runs on your machine. See [Develop with the IDE extension](omni-develop-with-the-ide-extension.md).

**Find the runs to inspect**

The traces list supports several ways to narrow the results:
+ **Filter.** Use the filter panel to narrow by agent, status, latency, token usage, and other trace properties.
+ **Filter by evaluation score.** Narrow the list to traces a specific evaluator scored above or below a threshold. For example, filter on a score range such as 0.0 to 0.5 to surface runs that completed without an error but failed evaluation. A high score range collects examples of the behavior you want to preserve.
+ **Search.** The search box above the table narrows the traces already loaded, matching text anywhere in a trace ID, a run's input, or its output. It reports how many of the loaded traces matched, and highlights the matching text in them. It matches no other field and does not re-query your time range, so use the filter panel to narrow by anything else (an evaluator or its score, for example).

Trace context does not propagate by itself: both sides of each hop must be instrumented. If an agent's caller is not instrumented, the agent's runs still appear here. They start at the agent.

**Inspect a run**

Select a trace to open it. The header shows the trace ID and span count, and the run's spans open in execution order so you can follow what the agent did step by step.

![](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/images/omni-agent-trace-detail.png)


Two controls change what the detail shows:
+ **The view control** changes how the spans are drawn: a timeline of span bars to follow timing and parent-child structure, or a raw view of the span records.
+ **The Trace and Span controls** change the scope of the detail panel:
  + **Trace** shows the whole run: the run's input and output, its status, latency, token usage, and its evaluation results.
  + **Span** shows one operation. Select a span to see the service that produced it, the span's own input and output, its timing and status, its attributes, and — for a tool call — the tool's parameters.

**Reading evaluation results.** The Trace scope lists every evaluation recorded for the run, each with the evaluator's name and score. Expand a result to read its explanation: the judge model's reasoning for why the run received that score. Rule-based evaluators report the score alone, with no explanation. A result that scored one tool call links to that span, so you can jump from the score to the operation it judged.

**Pivot to related telemetry.** From an open run you can open the logs that carry the same trace ID (**Show logs for this trace**), open the agent's own metrics (**Show agent metrics**), and, when your space is connected to the AWS DevOps Agent, start an investigation from a failed run (**Investigate**). See [Investigate with the AWS DevOps Agent](omni-investigate-with-the-aws-devops-agent.md).

**Act on what you find**

Select one or more runs in the traces list, then choose an action:

![](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/images/omni-agent-traces-actions.png)

+ **Evaluate.** Pick the evaluators to run, and scores appear alongside the traces as they complete, each with its explanation on the trace. Two kinds of evaluator cannot run here. Session-level evaluators score whole conversations; run them from [Agent sessions](omni-agent-sessions.md). Evaluators that require an expected response need ground truth a live trace does not carry; run those against a dataset instead. See [Evaluators and evaluations](omni-agents-evaluators.md).
+ **Create dataset** or **Add to dataset.** Turn the selected runs into test cases: each run's input becomes the test input, and its response and tool calls seed the expected outcome for you to review. Add failing runs before you fix them so that the fix can be verified against a test case. See [Datasets](omni-agents-datasets.md).
+ **Compare.** Select exactly two traces to see them side by side. Comparing a failing run with a successful one shows where the behavior diverged.

For the end-to-end workflow that runs through this page (find a failing run, package it, fix it, verify the fix), see [Tutorial: Fix a production quality regression](omni-agents-close-the-loop.md).

**When traces are missing or incomplete**

What you see on this page depends on the telemetry your agent sends. These checks cover the common gaps:
+ No traces appear. Confirm the time range, and verify that the agent is sending traces to your space. See [Send AI agent telemetry](omni-send-ai-agent-telemetry.md).
+ A run has only one or a few flat spans. The agent's internal operations are not instrumented, so there is nothing deeper to inspect. See [Send AI agent telemetry](omni-send-ai-agent-telemetry.md).
+ Inputs, outputs, or tool parameters are blank. The instrumentation does not capture that content. The symptom table in [Send AI agent telemetry](omni-send-ai-agent-telemetry.md) maps each gap to the configuration that fixes it.
+ Logs do not appear from the **Show logs for this trace** pivot. Confirm the agent's logs reach your space and carry the trace ID for correlation.

**Where to go next**


|  |  | 
| --- |--- |
| To do this | See | 
| Follow a conversation across runs | [Agent sessions](omni-agent-sessions.md) | 
| See your agent's structure and where runs fail in it | [Agent topology](omni-agent-topology.md) | 
| Score runs continuously instead of on demand | [Evaluators and evaluations](omni-agents-evaluators.md) | 
| Manage the test sets you build from runs | [Datasets](omni-agents-datasets.md) | 
| Query trace records directly with SQL | [Explore and query your telemetry](omni-explore-and-query-your-telemetry.md) | 
| Walk the find, fix, verify workflow end to end | [Tutorial: Fix a production quality regression](omni-agents-close-the-loop.md) | 
| Investigate traces of requests across your services | [Application traces](omni-application-traces.md) | 