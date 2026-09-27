

# Use Omni skills
<a name="omni-use-omni-skills"></a>

You can use CloudWatch Omni from the AI coding agent you already develop with — including Claude Code, Cursor, Kiro, and Codex — by installing the Omni skills from the [Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/quick-start.html). A skill is a set of task-focused instructions, reference material, and scripts that your coding agent loads when a task matches, so it can complete Omni tasks: set up instrumentation, query your telemetry, or work with alerts and dashboards.

**Note**  
This page is about using Omni from your own coding agent. For the AI assistance built into the IDE extension, see [Develop with the IDE extension](omni-develop-with-the-ide-extension.md). For the AI assistant in the Omni web UI, see [Ask the Omni agent](omni-ask-the-omni-agent.md).

**How skills work with your AWS credentials**

When you give your coding agent an Omni task, the agent activates the matching skill and follows its instructions. The scripts included with the skills call the public AWS API endpoints that power Omni (Amazon CloudWatch, Amazon Bedrock AgentCore, and Amazon Bedrock) using the AWS credentials configured in your environment, for example the credentials you get from running `aws sso login`. This is the same authentication the public API uses.

**What your coding agent can do with Omni**

With the Omni skills installed, your coding agent can help you:
+ Set up Omni observability for your application or AI agent, including instrumentation.
+ Query the telemetry in your CloudWatch Dataset and work with the results.
+ Manage Omni resources such as alerts, dashboards, and agent evaluations.
+ Build datasets from traces for agent evaluation.
+ Connect external integrations such as Slack.

**Install the Omni skills**

Before you begin, you need:
+ An AWS account with Omni set up. See [Set up Omni](omni-set-up-omni.md).
+ AWS credentials configured in your development environment.
+ A coding agent that supports skills, such as Claude Code, Cursor, Kiro, or Codex.

**To install and use the Omni skills**

1. Install the skills from the [Getting started](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/quick-start.html) page in the Agent Toolkit for AWS User Guide, which has installation instructions for each supported coding agent.

1. Give your coding agent an Omni task, such as "Set up Omni observability for this application" or "Instrument this agent and send its traces to Omni."

1. Verify the result in the Omni web UI. For example, confirm that traces arrive or that the alert or dashboard the agent created matches what you asked for.