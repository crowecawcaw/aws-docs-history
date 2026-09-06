

# Search Relevance Agent in Amazon OpenSearch Service
<a name="application-search-relevance-agent"></a>

The Search Relevance Agent is a feature in Amazon OpenSearch Service that automates search relevance tuning tasks. Through a chat interface in OpenSearch UI, you can find relevance issues, get tuning tips, and run workflows using natural language. With the Search Relevance Agent, you can take a data-driven approach instead of tuning manually.

The agent analyzes user behavior signals and query patterns. It generates hypotheses and validates them through offline evaluation against pre-labeled datasets. You can improve search relevance without deep search expertise.

The following screenshot shows the Search Relevance Workbench in OpenSearch UI.

![The Search Relevance Workbench showing search configurations, experiments navigation, and the AI Assistant chat panel.](http://docs.aws.amazon.com/opensearch-service/latest/developerguide/images/search-relevance-workbench.png)


## Getting started
<a name="application-search-relevance-agent-getting-started"></a>

To start the Search Relevance Agent, enter the `/search-relevance` slash command in the **AI Assistant** chat. The agent behavior depends on your current workspace context:
+ If you're not in a Search workspace, the agent prompts you to navigate to or create a Search workspace.
+ If you're already in a Search workspace, the slash command navigates you to the **Search Relevance Workbench** page. You can then ask follow-up questions about search relevance in the **AI Assistant** chat.

The Search Relevance Agent has the same region availability as the other agentic AI features. For more information, see [Region availability](application-ai-assistant.md#application-ai-assistant-regions).

## Key benefits
<a name="application-search-relevance-agent-benefits"></a>

Search relevance tuning is complex. Intent gaps exist in ambiguous queries. Search data often contains noise or gaps at scale. Manual tuning cycles can take months. The Search Relevance Agent addresses these challenges with the following benefits:
+ **Faster diagnosis and resolution** – Reduce the time to find and fix relevance issues from days to hours. The agent automates root-cause analysis and tuning workflows for rapid iteration.
+ **Reduced dependency on search experts** – With the Search Relevance Agent, you can tune search quality through guided workflows without needing specialized expertise.
+ **Data-validated improvements** – Replace intuition-based tuning with automated evaluation loops. The agent tests changes against real queries and datasets. You can confirm that improvements are measurable and free of unintended regressions.
+ **Full control of the process** – You keep full oversight using a collaborative approach. You remain the decision-maker, steering the agent's direction and refining recommendations.

## Capabilities
<a name="application-search-relevance-agent-capabilities"></a>

With the Search Relevance Agent, you can run end-to-end experiments with query domain-specific language (DSL) through the Search Relevance Workbench. You can do the following tasks:
+ Create query sets and judgment lists (human-rated query-result pairs)
+ Run controlled tests and quantify impact using standard relevance metrics
+ Refine search fields, adjust weights, and tune boost functions (rules that increase the relevance score of specific results)

You can enter the conversation at any stage of the search improvement cycle. Start with a diagnostic check or bring specific hypotheses for immediate testing. The agent uses User Behavior Insights (UBI) data when available for deeper optimization, but UBI is not required to begin.