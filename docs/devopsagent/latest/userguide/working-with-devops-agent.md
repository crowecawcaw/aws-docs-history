# Working with DevOps Agent

## Working with DevOps Agent

AWS DevOps Agent works alongside your operations team across the full incident lifecycle — from detection through investigation, recovery, and prevention. The following topics describe how to use DevOps Agent to manage each phase of this lifecycle.

## Autonomous incident response

When an incident is detected — whether through a built-in integration with your ticketing system, a webhook from your monitoring tools, or a manual trigger — DevOps Agent automatically begins an investigation. The agent analyzes metrics, logs, traces, code changes, and deployment history to determine a root cause and propose a mitigation plan. If you need additional help, you can escalate directly to AWS Support from the DevOps Agent Space web app, which automatically shares the investigation context with support engineers so you don't have to repeat what the agent already found. For more information, see [Autonomous incident response](working-with-devops-agent-autonomous-incident-response.md "working-with-devops-agent-autonomous-incident-response.md").

## On-demand DevOps tasks

At any point during the incident lifecycle, you can interact with DevOps Agent through a conversational chat interface. Ask questions about your AWS resources, system health, alarm status, and deployment history using natural language. Chat is context-aware — when you're viewing a specific investigation, you can steer the agent to explore particular hypotheses, focus on specific logs, or update its root cause analysis. You can also query resource configurations, error trends, and investigation insights across your environment without navigating between consoles. For more information, see [On Demand DevOps Tasks](working-with-devops-agent-on-demand-devops-tasks.md "working-with-devops-agent-on-demand-devops-tasks.md").

## Proactive incident prevention

After resolving incidents, DevOps Agent analyzes patterns across your investigation history to generate recommendations that prevent future incidents and reduce mean time to detection. Recommendations span four areas: observability posture, testing gaps, code changes, and infrastructure architecture. The agent runs evaluations weekly and updates recommendations as new incidents occur. You can accept, reject, or track recommendations, and the agent learns from your feedback to refine future suggestions. For more information, see [Proactive incident prevention](working-with-devops-agent-proactive-incident-prevention.md "working-with-devops-agent-proactive-incident-prevention.md").

## Interfacing with the DevOps Agent

AWS DevOps Agent supports multiple access methods including the web app console, MCP integration for IDEs, Agent Client Protocol (ACP), webhooks for event-driven automation, and direct API access. For more information, see [Interfacing with the DevOps Agent](working-with-devops-agent-interfacing-with-the-devops-agent-index.md "working-with-devops-agent-interfacing-with-the-devops-agent-index.md").

## Custom Agents

Custom agents let you define your own AI agents tailored to your infrastructure and workflows. You configure a system prompt, select which MCP tools the agent can use, and assign skills that provide domain knowledge. Custom agents run on demand or on a schedule to automate recurring operational work such as generating reports, auditing configurations, and analyzing trends. For more information, see [Custom Agents](working-with-devops-agent-custom-agents-index.md "working-with-devops-agent-custom-agents-index.md").
