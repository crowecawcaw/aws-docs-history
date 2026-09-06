

# Monitor AI coding agents with Amazon CloudWatch Coding Agent Insights
<a name="coding-agents-insights"></a>

AI coding agents such as OpenAI Codex, Claude Code, and GitHub Copilot emit OpenTelemetry (OTel) telemetry about how your developers use them—token consumption, per-turn latency, tool calls, API requests, and approvals. When you send this telemetry to Amazon CloudWatch, you can monitor adoption, attribute usage and cost to teams and departments, and spot performance or reliability issues across your developer fleet.

CloudWatch provides **Coding Agent Insights**, a set of ready-to-use dashboards in the console under **GenAI Observability**, **Coding Agent Insights**. The dashboards let you slice and dice usage across organizational attributes such as organization, department, team, cost center, and user, so you can compare adoption and cost across your fleet. You can also export the underlying data as CSV for further analysis. You don't create or import these dashboards. They appear automatically and populate as soon as your agents send metrics in the expected shape. Your only task is to configure each agent to publish its OTel metrics to CloudWatch.

**Important**  
The Coding Agent Insights dashboards rely on a specific metric and attribute shape. Each agent's native OTel metrics carry the dashboard's core dimensions (such as `model` and `token_type`). Identity and organizational attributes (such as `user.email`, `team.id`, `department`, `cost_center`, and `organization`) must be sent as OTel *resource* attributes. The setup guides in this section configure each agent to emit telemetry in this shape. If you change the metric names or move identity attributes off the resource, the dashboards might not populate.

## Prerequisites
<a name="coding-agents-insights-prereqs"></a>

Coding agents send metrics to the CloudWatch native OTLP metrics endpoint. Before you configure an agent, become familiar with the endpoint. For more information, see [OTLP Endpoints](CloudWatch-OTLPEndpoint.md) and [Getting started](CloudWatch-OTLPGettingStarted.md).

## Setup guides
<a name="coding-agents-insights-guides"></a>

Choose the guide for your coding agent. Each guide covers one or more setup paths, so you can pick the approach that matches how your developers run the agent.

**Topics**
+ [Claude Code](coding-agents-claude-code.md) — Configure Claude Code using a bearer token (individuals and small teams) or an enterprise rollout with corporate SSO.
+ [Set up OpenTelemetry for OpenAI Codex](coding-agents-codex.md) — Configure OpenAI Codex using a bearer token (individuals and small teams) or an enterprise rollout with corporate single sign-on (SSO).
+ [Set up OpenTelemetry for GitHub Copilot](coding-agents-copilot.md) — Configure GitHub Copilot using a bearer token.

## View the dashboards
<a name="coding-agents-insights-view"></a>

After an agent starts sending metrics, view the dashboards in the console.

**To view the Coding Agent Insights dashboards**

1. Open the CloudWatch console at [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/).

1. In the navigation pane, choose **GenAI Observability**, and then choose **Coding Agent Insights**.

1. Choose the tab for your coding agent. Metrics typically appear within a few minutes of the agent sending data.

**Note**  
Metrics are queryable with PromQL, so you can also build your own dashboards and alarms. For more information, see [PromQL querying](CloudWatch-PromQL-Querying.md).