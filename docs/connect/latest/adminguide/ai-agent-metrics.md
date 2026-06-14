# AI agent metrics

The following metrics are available for monitoring AI agent performance. For
information about creating AI agents, see [Create AI agents](create-ai-agents.md "create-ai-agents.md").
For information about creating AI prompts, see [Create AI
prompts](create-ai-prompts.md "create-ai-prompts.md"). For information about AI agent MCP tools, see [AI agent MCP tools](ai-agent-mcp-tools.md "ai-agent-mcp-tools.md").

###### Contents

- [Active AI Agents](#metric-active-ai-agents "#metric-active-ai-agents")
- [AI Agent Invocations](#metric-ai-agent-invocations "#metric-ai-agent-invocations")
- [AI Agent Invocation Success](#metric-ai-agent-invocation-success "#metric-ai-agent-invocation-success")
- [AI Agent Invocation Success Rate](#metric-ai-agent-invocation-success-rate "#metric-ai-agent-invocation-success-rate")
- [AI Agent Response Helpful](#metric-ai-agent-response-helpful "#metric-ai-agent-response-helpful")
- [AI Agent Response Not Helpful](#metric-ai-agent-response-not-helpful "#metric-ai-agent-response-not-helpful")
- [AI Handoffs](#metric-ai-handoffs "#metric-ai-handoffs")
- [AI Handoff Rate](#metric-ai-handoff-rate "#metric-ai-handoff-rate")
- [AI Response Completion Rate](#metric-ai-response-completion-rate "#metric-ai-response-completion-rate")
- [AI Involved Contacts](#metric-ai-involved-contacts "#metric-ai-involved-contacts")
- [AI Prompt Invocation Success](#metric-ai-prompt-invocation-success "#metric-ai-prompt-invocation-success")
- [AI Prompt Invocation Success Rate](#metric-ai-prompt-invocation-success-rate "#metric-ai-prompt-invocation-success-rate")
- [AI Prompt Invocations](#metric-ai-prompt-invocations "#metric-ai-prompt-invocations")
- [AI Tool Invocation Success](#metric-ai-tool-invocation-success "#metric-ai-tool-invocation-success")
- [AI Tool Invocation Success Rate](#metric-ai-tool-invocation-success-rate "#metric-ai-tool-invocation-success-rate")
- [AI Tool Invocations](#metric-ai-tool-invocations "#metric-ai-tool-invocations")
- [AI Tool Parameter Accuracy](#metric-ai-tool-parameter-accuracy "#metric-ai-tool-parameter-accuracy")
- [AI Tool Selection Accuracy](#metric-ai-tool-selection-accuracy "#metric-ai-tool-selection-accuracy")
- [AI Tool Utilization Accuracy](#metric-ai-tool-utilization-accuracy "#metric-ai-tool-utilization-accuracy")
- [Average AI Agent Conversation Turns](#metric-avg-ai-agent-conversation-turns "#metric-avg-ai-agent-conversation-turns")
- [Average AI Conversation Turns](#metric-avg-ai-conversation-turns "#metric-avg-ai-conversation-turns")
- [Average AI Prompt Invocation Latency](#metric-avg-ai-prompt-invocation-latency "#metric-avg-ai-prompt-invocation-latency")
- [Average AI Tool Invocation Latency](#metric-avg-ai-tool-invocation-latency "#metric-avg-ai-tool-invocation-latency")
- [Completeness Score](#metric-completeness-score "#metric-completeness-score")
- [Faithfulness Score](#metric-faithfulness-score "#metric-faithfulness-score")
- [Goal Success Rate](#metric-goal-success-rate "#metric-goal-success-rate")
- [Knowledge Content References](#metric-knowledge-content-references "#metric-knowledge-content-references")
- [Proactive Intents Answered](#metric-proactive-intents-answered "#metric-proactive-intents-answered")
- [Proactive Intents Detected](#metric-proactive-intents-detected "#metric-proactive-intents-detected")
- [Proactive Intents Engaged](#metric-proactive-intents-engaged "#metric-proactive-intents-engaged")
- [Proactive Intent Engagement Rate](#metric-proactive-intent-engagement-rate "#metric-proactive-intent-engagement-rate")
- [Proactive Intent Response Rate](#metric-proactive-intent-response-rate "#metric-proactive-intent-response-rate")

## Active AI Agents

This metric measures the total number of unique [AI Agents](create-ai-agents.md "create-ai-agents.md"), where
each AI Agent is identified by its unique combination of Name and Version.

- **Metric type:** Integer
- **Metric category:** AI Agent
- **GetMetricDataV2 API metric
  identifier:** `ACTIVE_AI_AGENTS`
- **Dashboard location:** AI Agent Performance
  Dashboard, Active AI Agents

## AI Agent Invocations

This metric measures the total count of [AI Agent](create-ai-agents.md "create-ai-agents.md")
invocations across all AI Agents per instance.

- **Metric type:** Integer
- **Metric category:** AI Agent
- **GetMetricDataV2 API metric
  identifier:** `AI_AGENT_INVOCATIONS`
- **Dashboard location:** AI Agent Performance
  Dashboard, AI Agent Invocation Count

## AI Agent Invocation Success

This metric measures the number of [AI Agent](create-ai-agents.md "create-ai-agents.md")
invocations that executed successfully without technical failures such as API errors,
timeouts, or system issues.

- **Metric type:** Integer
- **Metric category:** AI Agent
- **GetMetricDataV2 API metric
  identifier:**
  `AI_AGENT_INVOCATION_SUCCESS`

## AI Agent Invocation Success Rate

This metric measures the percentage of [AI Agent](create-ai-agents.md "create-ai-agents.md")
invocations that executed successfully without technical failures.

- **Metric type:** Percent
- **Metric category:** AI Agent
- **GetMetricDataV2 API metric
  identifier:**
  `AI_AGENT_INVOCATION_SUCCESS_RATE`
- **Dashboard location:** AI Agent Performance
  Dashboard, AI Agent Invocation Success Rate

## AI Agent Response Helpful

This metric measures the count of AI suggestions rated as helpful with a
thumbs-up.

- **Metric type:** Integer
- **Metric category:** AI Agent
- **GetMetricDataV2 API metric
  identifier:**
  `AI_AGENT_RESPONSE_HELPFUL`
- **Dashboard location:** AI Agent Performance
  Dashboard, AI Agent Response Helpful

###### Note

This metric is updated every 6 hours. This metric is available as part of
Connect Customer AI.

## AI Agent Response Not Helpful

This metric measures the count of AI suggestions rated as unhelpful with a
thumbs-down.

- **Metric type:** Integer
- **Metric category:** AI Agent
- **GetMetricDataV2 API metric
  identifier:**
  `AI_AGENT_RESPONSE_NOT_HELPFUL`
- **Dashboard location:** AI Agent Performance
  Dashboard, AI Agent Response Not Helpful

###### Note

This metric is updated every 6 hours. This metric is available as part of
Connect Customer AI.

## AI Handoffs

This metric measures the total count of contacts handled by [AI agents](create-ai-agents.md "create-ai-agents.md") that
escalated to human agents. This metric is specifically applicable to self-service
use cases where AI agents initially handle customer inquiries.

- **Metric type:** Integer
- **Metric category:** AI Session
- **GetMetricDataV2 API metric
  identifier:** `AI_HANDOFFS`

## AI Handoff Rate

This metric measures the percentage of contacts handled by [AI agents](create-ai-agents.md "create-ai-agents.md") that
had escalation to human agents or additional support.

- **Metric type:** Percent
- **Metric category:** AI Session
- **GetMetricDataV2 API metric
  identifier:** `AI_HANDOFF_RATE`
- **Dashboard location:** AI Agent Performance
  Dashboard, Handoff Rate

## AI Response Completion Rate

This metric measures the percentage of AI sessions that successfully responded to
incoming customer requests.

- **Metric type:** Percent
- **Metric category:** AI Session
- **GetMetricDataV2 API metric
  identifier:**
  `AI_RESPONSE_COMPLETION_RATE`
- **Dashboard location:** AI Agent Performance
  Dashboard, Response Completion Rate

## AI Involved Contacts

This metric measures the total count of customer contacts where [AI Agents](create-ai-agents.md "create-ai-agents.md") were
involved, either providing self-service automation or assisting human agents in
resolving customer inquiries.

- **Metric type:** Integer
- **Metric category:** AI Session
- **GetMetricDataV2 API metric
  identifier:** `AI_INVOLVED_CONTACTS`
- **Dashboard location:** AI Agent Performance
  Dashboard, AI Involved Contacts

## AI Prompt Invocation Success

This metric measures the number of [AI Prompt](create-ai-prompts.md "create-ai-prompts.md")
invocations that executed successfully without errors.

- **Metric type:** Integer
- **Metric category:** AI Prompt
- **GetMetricDataV2 API metric
  identifier:**
  `AI_PROMPT_INVOCATION_SUCCESS`

## AI Prompt Invocation Success Rate

This metric measures the percentage of [AI Prompt](create-ai-prompts.md "create-ai-prompts.md")
invocations that executed successfully.

- **Metric type:** Percent
- **Metric category:** AI Prompt
- **GetMetricDataV2 API metric
  identifier:**
  `AI_PROMPT_INVOCATION_SUCCESS_RATE`
- **Dashboard location:** AI Agent Performance
  Dashboard, AI Prompt Invocation Success Rate

## AI Prompt Invocations

This metric measures the total count of [AI Prompt](create-ai-prompts.md "create-ai-prompts.md")
invocations.

- **Metric type:** Integer
- **Metric category:** AI Prompt
- **GetMetricDataV2 API metric
  identifier:**
  `AI_PROMPT_INVOCATIONS`
- **Dashboard location:** AI Agent Performance
  Dashboard, AI Prompt Invocation Count

## AI Tool Invocation Success

This metric measures the total number of [AI Tool](ai-agent-mcp-tools.md "ai-agent-mcp-tools.md")
invocations that executed successfully.

- **Metric type:** Integer
- **Metric category:** AI Tool
- **GetMetricDataV2 API metric
  identifier:**
  `AI_TOOL_INVOCATION_SUCCESS`

## AI Tool Invocation Success Rate

This metric measures the percentage of AI Tool invocations that executed
successfully.

- **Metric type:** Percent
- **Metric category:** AI Tool
- **GetMetricDataV2 API metric
  identifier:**
  `AI_TOOL_INVOCATION_SUCCESS_RATE`
- **Dashboard location:** AI Agent Performance
  Dashboard, AI Tool Invocation Success Rate

## AI Tool Invocations

This metric measures the total count of AI Tool invocations.

- **Metric type:** Integer
- **Metric category:** AI Tool
- **GetMetricDataV2 API metric
  identifier:** `AI_TOOL_INVOCATIONS`
- **Dashboard location:** AI Agent Performance
  Dashboard, AI Tool Invocation Count

## AI Tool Parameter Accuracy

This metric measures the rate of tool invocations where [AI Agents](create-ai-agents.md "create-ai-agents.md")
provided the correct parameters. Value is between 0-1, where 1 indicates perfect
parameter accuracy.

- **Metric type:** Double
- **Metric category:** AI Tool
- **GetMetricDataV2 API metric
  identifier:**
  `AI_TOOL_PARAMETER_ACCURACY`
- **Dashboard location:** AI Agent Performance
  Dashboard, AI Tool Parameter Accuracy

**Evaluation Criteria:**

This metric uses an automated LLM-based evaluation that analyzes the parameters
passed to each tool call against the conversation context and the tool's parameter
definitions. Each tool call is scored as either correct or incorrect based on the
following criteria:

- **Presence:** Are all required parameters
  present and correctly populated?
- **Accuracy:** Are parameter values
  explicitly justified by the conversation context, rather than inferred or
  assumed?
- **Precision:** Are there any extra,
  irrelevant, or fabricated parameters included?

###### Note

This metric is updated every 24 hours. This metric is available as part of
Connect Customer AI.

## AI Tool Selection Accuracy

This metric measures the rate of correct tool selections by [AI Agents](create-ai-agents.md "create-ai-agents.md"). Value
is between 0-1, where 1 indicates optimal selection.

- **Metric type:** Double
- **Metric category:** AI Tool
- **GetMetricDataV2 API metric
  identifier:**
  `AI_TOOL_SELECTION_ACCURACY`
- **Dashboard location:** AI Agent Performance
  Dashboard, AI Tool Selection Accuracy

**Evaluation Criteria:**

This metric uses an automated LLM-based evaluation that analyzes each tool call
made by the AI agent. Each tool call is scored as either correct or incorrect based
on the following criteria:

- **Appropriateness:** Was the selected tool
  the right one for fulfilling the customer's request?
- **Necessity:** Did the AI agent avoid
  unnecessary or incorrect tool calls?
- **Optimal selection:** Was there a more
  appropriate tool available that the AI agent missed?

###### Note

This metric is updated every 24 hours. This metric is available as part of
Connect Customer AI.

## AI Tool Utilization Accuracy

This metric measures the rate of correct tool utilization by [AI Agents](create-ai-agents.md "create-ai-agents.md"),
including proper parameters and selection. Value is between 0-1, where 1 indicates
perfect utilization.

- **Metric type:** Double
- **Metric category:** AI Tool
- **GetMetricDataV2 API metric
  identifier:**
  `AI_TOOL_UTILIZATION_ACCURACY`
- **Dashboard location:** AI Agent Performance
  Dashboard, AI Tool Utilization Accuracy

**Evaluation Criteria:**

This metric is the combined score of AI Tool Selection Accuracy and AI Tool
Parameter Accuracy.

###### Note

This metric is updated every 24 hours. This metric is available as part of
Connect Customer AI.

## Average AI Agent Conversation Turns

This metric measures the average number of conversation turns that [AI Agents](create-ai-agents.md "create-ai-agents.md") took
to reach an outcome.

- **Metric type:** Double
- **Metric category:** AI Agent
- **GetMetricDataV2 API metric
  identifier:**
  `AVG_AI_AGENT_CONVERSATION_TURNS`
- **Dashboard location:** AI Agent Performance
  Dashboard, Avg. AI agent conversation turns

## Average AI Conversation Turns

This metric measures the average number of conversation turns across all AI
involved contacts.

- **Metric type:** Double
- **Metric category:** AI Session
- **GetMetricDataV2 API metric
  identifier:**
  `AVG_AI_CONVERSATION_TURNS`
- **Dashboard location:** AI Agent Performance
  Dashboard, Avg. AI Conversation Turns

## Average AI Prompt Invocation Latency

This metric measures the average invocation latency of [AI Prompts](create-ai-prompts.md "create-ai-prompts.md") in
milliseconds.

- **Metric type:** Double
- **Metric category:** AI Prompt
- **GetMetricDataV2 API metric
  identifier:**
  `AVG_AI_PROMPT_INVOCATION_LATENCY`
- **Dashboard location:** AI Agent Performance
  Dashboard, Avg. AI Prompt Invocation Latency

## Average AI Tool Invocation Latency

This metric measures the average invocation latency of AI Tools in
milliseconds.

- **Metric type:** Double
- **Metric category:** AI Tool
- **GetMetricDataV2 API metric
  identifier:**
  `AVG_AI_TOOL_INVOCATION_LATENCY`
- **Dashboard location:** AI Agent Performance
  Dashboard, Avg. AI Tool Invocation Latency

## Completeness Score

This metric measures the proportion of sessions where the Orchestration [AI Agent](create-ai-agents.md "create-ai-agents.md")
responses fully address all parts of customer requests rather than providing partial
or incomplete answers. Value is between 0-1, where 1 indicates complete responses
across all sessions.

- **Metric type:** Double
- **Metric category:** AI Session
- **GetMetricDataV2 API metric
  identifier:** `COMPLETENESS_SCORE`
- **Dashboard location:** AI Agent Performance
  Dashboard, Avg. Completeness Score

**Evaluation Criteria:**

This metric uses an automated LLM-based evaluation that analyzes each customer
turn and the AI agent's response. When a customer message contains multiple
requests or questions, the evaluation checks whether each one was addressed. This
metric is evaluated using the following criteria:

- **Multi-request coverage:** Were all
  explicit requests within a single turn identified and addressed by the
  agent?
- **Definition of covered:** Was each request
  either directly answered, acknowledged with intent to act on, or explained
  as not possible due to policy/constraints?
- **Immediate response scope:** Only the
  agent's responses before the next message are evaluated; later resolution
  doesn't count retroactively

###### Note

This metric is updated every 24 hours. This metric is available as part of
Connect Customer AI.

## Faithfulness Score

This metric measures the proportion of sessions where the Orchestration [AI Agent](create-ai-agents.md "create-ai-agents.md")
responses remain faithful to the conversational context, including messages and tool
call results. Value is between 0-1, where 1 indicates perfect contextual
fidelity.

- **Metric type:** Double
- **Metric category:** AI Session
- **GetMetricDataV2 API metric
  identifier:** `FAITHFULNESS_SCORE`
- **Dashboard location:** AI Agent Performance
  Dashboard, Avg. Faithfulness Score

**Evaluation Criteria:**

This metric uses an automated LLM-based evaluation that analyzes each AI agent
response against the conversation context. Each response is assessed for
faithfulness and checked for hallucination based on the following criteria:

- **Accuracy of representation:** Does the
  response accurately represent information from the conversation
  context?
- **Consistency:** Does the response maintain
  consistency with facts stated in the conversation?
- **Supported inferences:** Are any inferences
  the response makes reasonably supported by the context?
- **Correct attribution:** Does the response
  correctly attribute statements and information to the right source in the
  conversation without fabricating or misaligning claims?

###### Note

This metric is updated every 24 hours. This metric is available as part of
Connect Customer AI.

## Goal Success Rate

This metric measures the proportion of sessions where the Orchestration [AI Agent](create-ai-agents.md "create-ai-agents.md")
successfully resolved customer issues. Value is between 0-1, where 1 indicates
successful resolution across all sessions.

- **Metric type:** Double
- **Metric category:** AI Session
- **GetMetricDataV2 API metric
  identifier:** `GOAL_SUCCESS_RATE`
- **Dashboard location:** AI Agent Performance
  Dashboard, Goal Success Rate

**Evaluation Criteria:**

This metric uses an automated LLM-based evaluation that analyzes the complete
conversation trace for each AI agent session. Each session is scored as either
successful or unsuccessful based on four dimensions:

- **Goal achievement:** Did the AI agent
  fulfill the customer's primary objective?
- **Outcome quality:** Is the final result
  accurate and free of errors?
- **Completeness:** Were all aspects of the
  request addressed?
- **Appropriateness:** Did the AI agent use
  suitable tools and approaches?

###### Note

This metric is updated every 24 hours. This metric is available as part of
Connect Customer AI.

## Knowledge Content References

This metric measures the count of knowledge content articles referenced by [AI
Agents](create-ai-agents.md "create-ai-agents.md").

- **Metric type:** Integer
- **Metric category:** AI Knowledge
  Base
- **GetMetricDataV2 API metric
  identifier:**
  `KNOWLEDGE_CONTENT_REFERENCES`
- **Dashboard location:** AI Agent Performance
  Dashboard, Knowledge Base Reference Count

## Proactive Intents Answered

This metric measures the number of proactive intents (customer queries) that were
successfully answered by [AI Agents](create-ai-agents.md "create-ai-agents.md") during
AI sessions.

- **Metric type:** Integer
- **Metric category:** AI Session
- **GetMetricDataV2 API metric
  identifier:**
  `PROACTIVE_INTENTS_ANSWERED`

## Proactive Intents Detected

This metric measures the number of proactive intents (customer queries) detected
during AI sessions, particularly for Agent Assistance use cases.

- **Metric type:** Integer
- **Metric category:** AI Session
- **GetMetricDataV2 API metric
  identifier:**
  `PROACTIVE_INTENTS_DETECTED`

## Proactive Intents Engaged

This metric measures the number of proactive intents (customer queries) that were
engaged with by human agents during AI sessions.

- **Metric type:** Integer
- **Metric category:** AI Session
- **GetMetricDataV2 API metric
  identifier:**
  `PROACTIVE_INTENTS_ENGAGED`

## Proactive Intent Engagement Rate

This metric measures the percentage of detected proactive intents that were
clicked or engaged with by human agents.

- **Metric type:** Percent
- **Metric category:** AI Session
- **GetMetricDataV2 API metric
  identifier:**
  `PROACTIVE_INTENT_ENGAGEMENT_RATE`
- **Dashboard location:** AI Agent Performance
  Dashboard, Proactive Intent Engagement Rate

## Proactive Intent Response Rate

This metric measures the percentage of engaged proactive intents that were
successfully fulfilled by [AI
Agents](create-ai-agents.md "create-ai-agents.md").

- **Metric type:** Percent
- **Metric category:** AI Session
- **GetMetricDataV2 API metric
  identifier:**
  `PROACTIVE_INTENT_RESPONSE_RATE`
