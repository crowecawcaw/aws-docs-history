

# Ask the Omni agent
<a name="omni-ask-the-omni-agent"></a>

The Omni agent is the AI assistant built into the CloudWatch Omni web UI. Ask about your systems in plain language, and the agent answers from the telemetry available to it: it writes and runs queries, correlates signals across telemetry, and builds views and dashboards on demand.

**Note**  
CloudWatch Omni supports AI agents on three surfaces. This page covers the agent in the Omni web UI. For AI assistance while developing an AI agent in the IDE extension, see [Develop with the IDE extension](omni-develop-with-the-ide-extension.md). To use Omni from your own coding agent, see [Use Omni skills](omni-use-omni-skills.md). The Omni agent can also delegate an investigation to the AWS DevOps Agent. See [Investigate with the AWS DevOps Agent](omni-investigate-with-the-aws-devops-agent.md).

**Where you can ask**

Ask from the input on the Omni home page, or open the chat panel in any thread. Each conversation is saved as a thread you can return to and rename. See [Threads](omni-threads.md).

The agent can read what you have open on screen, so you can ask about "this alert" or "the service I'm looking at" without naming it. The agent runs long tasks, such as investigations and dashboard builds, in the background, and you can track them on the **Task Shelf**.

With the Slack integration connected, you can also have the agent respond to your team's Slack conversations. See [Connect Slack](omni-connect-slack.md).

**What you can ask**

The agent can do the same work as the pages in the web UI. Some examples, by task:


| To do this | Example prompts | 
| --- | --- | 
| Query your telemetry | "Show me the 5xx errors on checkout-service in the last hour" · "Which services logged timeout errors today?" | 
| Check on something | "How is payment-api doing?" · "Is anything firing right now?" | 
| Investigate a problem | "Why is checkout-service slow?" · "Dig into the errors on orders-api" | 
| Work with Omni alerts | "Alert me when p99 latency on checkout-service stays above 2 seconds" · "Change that alert's threshold to 3 seconds" | 
| Build dashboards | "Build a dashboard for the payment service" · "Save this investigation as a dashboard" | 
| Understand dependencies | "What depends on the orders database?" · "What does checkout-service call?" | 
| Measure AI agent quality | "Score yesterday's traces for correctness" · "Turn these failing traces into a dataset" | 
| Run commands | "/settings" opens the Settings page. Type "/" to see available commands. | 

**Queries.** When the agent writes a query for you, it shows the exact query it ran, so you can check it, refine it, or run it yourself in Explore. For the query syntax, see [Explore and query your telemetry](omni-explore-and-query-your-telemetry.md).

**Investigations.** A status question gets a quick lookup. When you ask why something is broken, the agent runs a multi-step investigation: it checks for anomalies, maps the services involved, and gathers evidence across your telemetry, then reports the likely cause with the concrete numbers and log lines behind it. It proposes the next step, and you choose the direction. You can also start an investigation from a service page. See [Monitor a service](omni-monitor-a-service.md).

**Alerts.** The agent creates Omni alerts, not CloudWatch alarms. It can create an alert from a plain-language condition, change an existing one, and answer questions about the alerts you have. Creating and changing are deliberate: the agent grounds the threshold in your data, shows you the specific alert it intends to create or change, and acts only after you confirm. It does not delete alerts. Manage them on the Alerts page. See [Alerts](omni-alerts.md).

**Dashboards.** Describe the dashboard you want and the agent composes it in your thread, where you can refine it section by section and save it. It can also turn a finished investigation into a dashboard. See [Dashboards](omni-dashboards.md).

**AI agent quality.** For the AI agents you monitor, the agent can score traces with your evaluators and add traces to an evaluation dataset — for example, packaging failing runs into a regression set. See [Evaluate agent quality](omni-agents-evaluate.md).

**How the agent works with you**

Answers are grounded in your live data: the agent re-checks current state rather than answering from earlier conversation, and when a lookup returns nothing, it says so instead of guessing. It also remembers durable context across your threads, such as the services and Regions you work with, so you do not re-explain your environment in every conversation.

The agent is scoped to observability. It declines unrelated work, such as general coding tasks, and offers to help with your telemetry instead.

**Limitations**
+ It reads only your space and your own conversations. It cannot read another person's threads.
+ It creates and changes alerts with your confirmation, but never deletes them, and it cannot rename an alert. You delete an alert yourself on the **Alerts** page.
+ It can be wrong. It shows its queries and evidence so you can verify. Check both before acting on a finding, and use the feedback controls on a response to rate it.

**Permissions and data access**

The agent works with your permissions: it can read only the telemetry you have access to (the space's logs and traces, plus metrics queried from CloudWatch Metrics). Its permissions are the same as yours in the Omni web UI. Actions that change something, such as creating an alert, always require your confirmation in the conversation. For permission levels, see [Control access to your space](omni-control-access-to-your-space.md).

**Investigations with the AWS DevOps Agent**

If your space is connected to the AWS DevOps Agent, the Omni agent automatically delegates root cause analysis to it, and you can track the investigation's progress from the conversation. See [Investigate with the AWS DevOps Agent](omni-investigate-with-the-aws-devops-agent.md).