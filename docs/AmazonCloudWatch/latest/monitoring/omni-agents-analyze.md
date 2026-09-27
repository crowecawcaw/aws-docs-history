

# Analyze agent behavior
<a name="omni-agents-analyze"></a>

Use these views to understand what your agent did and why: to debug failures, find slow steps, and follow multi-turn conversations. They read the traces your agent sends. For the underlying concepts, see [Monitor AI agents](omni-monitor-ai-agents.md).
+ [Agent traces](omni-agent-traces.md) — inspect a single agent run, span by span.
+ [Agent sessions](omni-agent-sessions.md) — follow a multi-turn conversation across runs.
+ [Agent topology](omni-agent-topology.md) — see how agents, tools, and models call each other.

**Which view to start with**
+ You know which run failed. Open it in Agent traces and follow the spans.
+ The problem is conversational (a user says the agent "forgot" or "went in circles"). Start in Agent sessions, which shows the agent's behavior across turns.
+ You have a symptom but no specific run ("this tool fails often," "something got slow"). Filter by errors, latency, or token usage in Agent traces and Agent sessions to find the runs that show why. Use the agent topology to see how your agent's components connect.

These views focus on individual runs. For production and fleet-wide monitoring across your agents in the Omni web UI, see [Monitor agents in the web UI](omni-monitor-agents-in-the-web-ui.md).