

# Custom agent outputs
<a name="custom-agents-custom-agent-outputs"></a>

Custom agents produce text responses in the invocation trajectory and can create persistent resources within your Agent Space — artifacts and recommendations. They can also send notifications to your configured notification channels as they work. While agents can additionally perform actions through Model Context Protocol (MCP) tools — such as creating tickets or updating external systems — this page covers the outputs tied directly to your Agent Space.

## Text responses
<a name="text-responses"></a>

Every custom agent produces text responses during invocation. These are the agent's messages — explanations, summaries, answers, and conclusions — recorded in the invocation trajectory. Text responses require no additional configuration.

## Artifacts
<a name="artifacts"></a>

Artifacts are structured visual reports that can contain text, charts, tables, and topology diagrams. They are persisted in your Agent Space and can be viewed from the invocation trajectory or the Artifacts page.

Artifacts support four element types:
+ **Text** – Markdown-formatted text blocks for summaries, explanations, and context.
+ **Charts** – Line and bar charts for visualizing metrics, trends, and comparisons over time.
+ **Tables** – Tabular data displays with sortable columns and configurable formatting.
+ **Topology diagrams** – Resource relationship maps showing services, dependencies, and their connections.

### Producing artifacts
<a name="producing-artifacts"></a>

Artifact creation is a built-in capability available to all custom agents. No additional skill assignment or configuration is required. Include instructions in your system prompt describing what artifact to produce, and the agent activates the required tools automatically.

For example:

```
## Output
Produce a single artifact titled "Weekly Investigation Report" containing:
- A table listing each investigation with title, status, and resolution time.
- A chart showing investigation counts by root cause category.
- A summary paragraph with key trends.
```

The agent handles the details of composing and persisting the artifact. You only need to describe what the artifact should contain in your system prompt.

### Viewing artifacts
<a name="viewing-artifacts"></a>

After an invocation completes, any artifacts produced appear as links at the end of the invocation trajectory. Choose an artifact link to view its rendered content — charts, tables, and topology diagrams are displayed as interactive visual elements.

You can also browse all artifacts in your Agent Space from the **Artifacts** page. Use the search field to find artifacts by title.

## Notifications
<a name="notifications"></a>

Notifications let you follow a running agent in real time. A custom agent sends short progress updates to your configured notification channels while it works. For example, a notification might appear as a message in the chat thread for the invocation. Unlike text responses, which are recorded in the invocation trajectory, notifications reach you as work happens, so you learn about a notable finding when it occurs rather than only at the end.

The agent sends each notification to the notification channels set up for your Agent Space, such as a connected Slack channel. If you have not set up a notification channel, the agent still runs as normal; it just does not send a notification. To set up a chat channel, follow the steps in [Connecting Slack](connecting-to-ticketing-and-chat-connecting-slack.md).

### Producing notifications
<a name="producing-notifications"></a>

Sending notifications is a built-in capability available to all custom agents. No additional skill assignment or configuration is required. Include instructions in your system prompt describing when the agent should notify you, and the agent activates the required tools automatically.

For example:

```
## Notifications
Send a notification whenever you find a resource in a non-compliant state, and
one at the end summarizing what you found. Keep each notification to a short
title and a one- or two-sentence body.
```

Each notification has a title and a body. You control whether and when the agent sends notifications through your system prompt instructions, together with the findings of the invocation. If you give no notification instructions, you do not receive notifications.

When a custom agent delegates work to a subagent, that subagent can send notifications too, so a finding that surfaces deep in a long invocation still reaches you as it happens. To learn how delegation works, see [Custom Agents](working-with-devops-agent-custom-agents-index.md).

### Viewing notifications
<a name="viewing-notifications"></a>

Notifications appear in your configured notification channels as they are sent during the invocation. For example, they can appear as messages in the chat thread for the invocation, linked back to the invocation so you can open it for full detail. The agent's complete reasoning and results remain available in the invocation trajectory regardless of which notifications were sent.

## Recommendations
<a name="recommendations"></a>

Recommendations are actionable suggestions that appear on the **Improvements** page of your DevOps Agent web app. Custom agents can create recommendations to surface findings, propose changes, or suggest operational enhancements based on their analysis.

### Producing recommendations
<a name="producing-recommendations"></a>

Recommendation creation is a built-in capability available to all custom agents. No additional skill assignment or configuration is required. Include instructions in your system prompt describing when and how to create recommendations, and the agent activates the required tools automatically.

For example:

```
## Output
For each configuration that does not meet the standard, create a recommendation with:
- A clear title describing the issue.
- A summary explaining the risk and the recommended corrective action.
```

Each recommendation has a title and a summary. Recommendations are created with a status of "Proposed" and can be accepted, rejected, or closed by your team from the Improvements page.

### Viewing recommendations
<a name="viewing-recommendations"></a>

After an invocation completes, any recommendations produced appear as links at the end of the invocation trajectory. They also appear on the **Improvements** page alongside recommendations generated by the built-in proactive prevention capability. Use the search field to find recommendations by title, or filter by status and category.