# Monitor AI agent performance with observability and analytics

After you set up your AI agents, you can monitor their performance using AI agent
observability and analytics. Connect Customer provides the following capabilities to track AI agent
performance:

- **ListSpans API:** Detailed span-level data
  about each AI agent invocation, including tool calls and nested operations.
  This data is available in real-time. To learn more, see [ListSpans API guide](../APIReference/API_amazon-q-connect_ListSpans.md "../APIReference/API_amazon-q-connect_ListSpans.md").
- **GetMetricDataV2 API:** Programmatic access to
  AI agent metrics with support for filtering and grouping. To learn more, see
  [GetMetricDataV2
  in the Connect Customer API Reference](../APIReference/API_GetMetricDataV2.md "../APIReference/API_GetMetricDataV2.md") and see [Metric definitions](metrics-definitions.md "metrics-definitions.md") for metric definitions and
  calculation logic details. For the full list of AI agent metrics, see [AI agent metrics](ai-agent-metrics.md "ai-agent-metrics.md").
- **Amazon Connect data lake:** Raw metric data
  available through the Connect Customer data lake for custom reporting and analysis. To
  learn more, see [Data type definitions](data-type-definitions.md "data-type-definitions.md"). The following AI
  agent data lake tables are refreshed every 15 minutes:

  - [AI Agent](data-type-definitions.md#data-lake-ai-agent "data-type-definitions.md#data-lake-ai-agent")
  - [AI Agent Knowledge Base](data-type-definitions.md#data-lake-ai-agent-knowledge-base "data-type-definitions.md#data-lake-ai-agent-knowledge-base")
  - [AI Prompt](data-type-definitions.md#data-lake-ai-prompt "data-type-definitions.md#data-lake-ai-prompt")
  - [AI Session](data-type-definitions.md#data-lake-ai-session "data-type-definitions.md#data-lake-ai-session")
  - [AI Tool](data-type-definitions.md#data-lake-ai-tool "data-type-definitions.md#data-lake-ai-tool")

- **CloudWatch Streaming:** CloudWatch Logs into the entire
  AI journey including the conversation, spans, triggers, intents,
  recommendations, tools. To learn more, see [Monitor AI agents using
  CloudWatch](monitor-ai-agents.md "monitor-ai-agents.md").
- **AI agent performance dashboard:** Pre-built
  visualizations that you can access from the Connect Customer admin website by choosing
  Dashboard, AI agent performance dashboard. To learn more, see [AI Agent performance dashboard](ai-agent-performance-dashboard.md "ai-agent-performance-dashboard.md").

![AI agent performance dashboard in the Connect Customer admin website.](images/ai-agent-performance-dashboard-overview.png)

###### Contents

- [AI agent metrics](ai-agent-metrics.md "ai-agent-metrics.md")
- [AI agent traces](ai-agent-traces.md "ai-agent-traces.md")
- [Monitor AI agents using
  CloudWatch](monitor-ai-agents.md "monitor-ai-agents.md")
