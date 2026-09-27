

# Develop with the IDE extension
<a name="omni-develop-with-the-ide-extension"></a>

Use the CloudWatch Omni extension to build, test, and evaluate your agent from your IDE. The extension is available for VS Code, Kiro, and Cursor.

**Local mode and cloud mode**

The extension works against two data sources.


| Mode | What you see | What it needs | 
| --- | --- | --- | 
| Local | Traces from the agent running on your machine, stored in your project folder | Credentials for the model provider your agent calls. No AWS account connection | 
| Cloud | Traces from deployed agents — the same data your team sees in the Omni web UI | Sign-in to your space | 

Switch modes as you work. Build and test in local mode. Then switch to cloud mode to compare a local run against production traces, or to use a dataset that an operator packaged from those traces. See [Tutorial: Fix a production quality regression](omni-agents-close-the-loop.md).

Features that interact with your project's code (such as [Manage prompts](omni-agents-manage-prompts.md)) are available in local mode only. If a feature needs the other mode, the extension shows it as unavailable and names the mode it requires.

**Install and connect**

1. Install the CloudWatch Omni extension in your editor. Search for it in your editor's extensions view, or install it from the registry your editor reads: [Install for VS Code](https://marketplace.visualstudio.com/items?itemName=AmazonWebServices.amazon-cloudwatch-omni) from the VS Code Marketplace, or [Install for Kiro and Cursor](https://open-vsx.org/extension/amazonwebservices/amazon-cloudwatch-omni) from Open VSX.

1. Open your agent project. The extension creates an `.omni` folder in the project for local traces and configuration.

1. Choose local mode, or sign in to your space to use cloud mode. A space is required only for cloud mode. To create one, see [Set up Omni](omni-set-up-omni.md).

The extension sidebar shows the mode you are in and the data source it reads from.

**Onboard your project**

Onboarding instruments your project and connects the extension to your running agent. A coding agent in your editor does the work, using the Omni skills.

1. **Choose the coding agent you want to work with.** The extension installs the Omni skills that agent needs, and its guided flows run through that agent.

1. **Detect the framework and language.** The coding agent reads your dependency files and source imports to identify your agent framework and the language it is written in.

1. **Instrument the project.** The coding agent adds the OpenTelemetry instrumentation your agent needs to emit traces, choosing between AWS Distro for OpenTelemetry and OpenInference according to your framework. Where instrumentation already exists, it verifies that setup rather than replacing it. For the instrumentation itself, see [Send AI agent telemetry](omni-send-ai-agent-telemetry.md).

1. **Connect to your agent.** The coding agent sets your start command and port and starts the local server, detects your agent's request and response schema from your code and saves it, then sends a test request. Onboarding is complete when that request produces a trace.

Start onboarding from the extension's Getting Started view.

**Onboard manually instead.** A coding agent is not required. Each step is also available on its own from the configuration view, so you can set the start command, the port, and the schema yourself, and re-run a single step without repeating the others. The "Test your agent locally" section of this page walks through the start command, the server, and the test request by hand.

![The extension's onboarding view listing the setup steps, with framework detection and instrumentation complete and the connect-to-agent step in progress.](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/images/omni-ide-onboarding.png)


**Test your agent locally**

Run your instrumented agent from inside the extension and inspect the traces it produces. If your agent is not instrumented yet, see [Send AI agent telemetry](omni-send-ai-agent-telemetry.md).

1. In the extension configuration, set the command that starts your agent's server and the port it listens on. The default port is 8080.

1. Start the server. The extension starts a local collector to receive telemetry, sets the OpenTelemetry environment your agent needs, runs your start command, and waits for the port to respond.

1. Send your agent a request (from the extension, from the playground, or from your own test harness) so the invocation produces traces that reach the collector.

1. Open `Agent traces` in the extension to inspect the run. Change your code or prompts and send another request to compare.

In local mode nothing leaves your machine: the collector writes traces to the `.omni` folder in your project.

**Run your own server**

To start your agent yourself, switch the extension to external server mode. The extension still runs the collector. It writes the OpenTelemetry settings your server needs to a file in your project. Load that file before you start the server. If your server already listens on the configured port, the extension uses it and does not start a second collector.

**AI assistance in the extension**

The extension includes AI assistance for working on your agent:
+ **Analyze with AI** — ask about a trace or a failure and get an explanation based on your telemetry.
+ **Prompt recommendations** — get suggestions to improve a prompt.

You can use AI coding agents through the Omni skills in the Agent Toolkit for AWS. See [Use Omni skills](omni-use-omni-skills.md). For the AI assistant in the Omni web UI, see [Ask the Omni agent](omni-ask-the-omni-agent.md).

![A trace open in the IDE extension with the Analyze with AI panel summarizing the run and flagging the step where the failure started.](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/images/omni-analyze-with-ai.png)


**Where to go next**
+ [Manage prompts](omni-agents-manage-prompts.md) — version your agent's prompts in the project and test changes before you ship them.
+ [Use Omni skills](omni-use-omni-skills.md) — work on your agent from the coding agent you already use, through the Omni skills in the Agent Toolkit for AWS.
+ [Send AI agent telemetry](omni-send-ai-agent-telemetry.md) — instrument your agent so its runs produce the traces the extension reads.
+ [Agent traces](omni-agent-traces.md) — how to read a trace, in the extension or the Omni web UI.