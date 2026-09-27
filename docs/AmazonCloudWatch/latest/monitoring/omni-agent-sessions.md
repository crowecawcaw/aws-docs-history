

# Agent sessions
<a name="omni-agent-sessions"></a>

The Agent sessions view groups the traces that belong to the same conversation or user interaction, so you can follow a multi-turn exchange from start to finish and see where it went wrong across turns. For how traces, spans, and sessions relate, see [Monitor AI agents](omni-monitor-ai-agents.md).

**Why sessions need their own view**

Some failures are invisible at the single-trace level because every individual turn looks fine. The Agent sessions view surfaces the cross-turn patterns:
+ **Lost context** — the agent asks for information the user already provided, or contradicts an earlier answer.
+ **Churn** — the same tool is called with the same arguments across consecutive turns, or the user rephrases the same request repeatedly (a sign the agent is not making progress).
+ **Degradation over length** — quality that is fine on turn one and poor by turn eight, which single-trace sampling never shows.

**To follow a session**

1. Open your space, then choose `Agent sessions`.

1. Select a session to see its turns in order and read the conversation flow.

1. Select the turn where the problem starts to open its trace in [Agent traces](omni-agent-traces.md).

![A session in Agent sessions showing its turns in order with summary cards, where a later turn surfaces a problem that no single turn shows on its own.](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/images/omni-session-detail.png)


**Evaluate and reuse sessions**

Cross-turn quality checks run from this view. Select one or more sessions, and then choose an action from the toolbar:
+ **Evaluate** — score the selected sessions. Evaluation runs through Amazon Bedrock AgentCore as a background batch job, and scores appear alongside the sessions as they complete. Only evaluators that score whole sessions can run here; evaluators that score individual traces run from [Agent traces](omni-agent-traces.md). For the evaluator catalog and how scoring works, see [Evaluators and evaluations](omni-agents-evaluators.md).
+ **Create dataset** or **Add to dataset** — turn the selected sessions into test cases, so a multi-turn scenario becomes a repeatable test. You choose whether each session becomes one test case or each of its traces does. See [Datasets](omni-agents-datasets.md).

**Group traces into sessions**

Omni groups traces into sessions using the OpenTelemetry `session.id` span attribute. Agents hosted on Amazon Bedrock AgentCore, and agents built with frameworks that set the attribute natively (such as Strands Agents), are grouped automatically. Custom and non-framework agents must set the attribute themselves. Otherwise, each turn appears as an unrelated trace.

Set `session.id` on the root span of every turn that belongs to the same conversation, reusing one stable ID per conversation and starting a fresh ID when a new conversation starts:

```
from opentelemetry import trace

# Reuse the SAME id for every turn in one conversation.
session_id = "conv-8f2a1c"  # your stable per-conversation id

span = trace.get_current_span()
span.set_attribute("session.id", session_id)
```

**Note** Only `session.id` groups traces into sessions. Setting the `gen_ai.conversation.id` attribute is harmless (other tools read it), but Omni does not use it for session grouping.