# Get started with Amazon Bedrock AgentCore

This quickstart gets you from zero to a running agent in a few minutes using the AgentCore CLI. You will install the CLI, scaffold a project, test locally, deploy to AWS, and invoke your agent.

Two ways to build an agent on AgentCore, same CLI:

- **Managed harness**. You declare the agent in a config file (model, prompt, tools, memory) and AgentCore runs the loop for you. No framework, no orchestration code. Good path when you want the fastest route from idea to a running agent. [Learn more](harness.md "harness.md").
- **Code-based agent**. You write the agent loop in Python using a framework you already know (Strands, LangGraph, Google ADK, or OpenAI Agents), and deploy it to AgentCore Runtime. Full control over orchestration logic.
  This page walks through the code-based flow. For harness, see [What is the AgentCore harness](harness.md "harness.md").

## Sign up for an AWS account

### Sign up for an AWS account

To get started with AWS, you need an AWS account. For information about creating an AWS account, see [Getting started with an AWS account](../../../accounts/latest/reference/getting-started.md "../../../accounts/latest/reference/getting-started.md") in the _AWS Account Management Reference Guide_.

## Prerequisites

- **Node.js 20 or later.** The AgentCore CLI is distributed as an npm package. Check with `node --version`. Install from [nodejs.org](https://nodejs.org "https://nodejs.org") if needed.
- **npm.** Included with Node.js.
- **An AWS account with credentials configured.** Configure via AWS CLI, environment variables, or an AWS profile. See [Configuring the AWS CLI](../../../cli/latest/userguide/cli-configure-files.md "../../../cli/latest/userguide/cli-configure-files.md").
- **Python 3.10 or later** (for agent code). Check with `python3 --version`.
- **IAM permissions.** Your identity needs permissions to make AgentCore API calls and to assume the CDK bootstrap roles used during deployment. See [Use the AgentCore CLI](runtime-permissions.md#runtime-permissions-cli "runtime-permissions.md#runtime-permissions-cli").
- **Model access.** Amazon Bedrock enables access to foundation models by default. Available models include Amazon Nova, Anthropic Claude, Meta Llama, and Mistral AI models. To use non-foundation models, follow the [model access steps](../../../bedrock/latest/userguide/model-access.md#model-access-sdk-step4 "../../../bedrock/latest/userguide/model-access.md#model-access-sdk-step4").
- **Docker.** Required only if you choose the `Container` build type. The default `CodeZip` build type does not require Docker.

## Step 1: Install the AgentCore CLI

```
npm install -g @aws/agentcore
```

Verify:

```
agentcore --version
```

###### Note

If this reports an error instead of a version number, an older Python `agentcore` command is shadowing the npm one on your `PATH`. This happens if you previously installed the `bedrock-agentcore-starter-toolkit` pip package, and is most common on Windows. Run `pip uninstall bedrock-agentcore-starter-toolkit`, then open a new terminal and try again.

To update later, rerun the install command or `agentcore update`. Source and issues: [agentcore-cli on GitHub](https://github.com/aws/agentcore-cli "https://github.com/aws/agentcore-cli").

## Step 2: Create your project

```
agentcore create
```

The interactive wizard first asks what you want to build:

- **Harness** - A managed config-based agent loop. No framework or orchestration code required. See [What is the AgentCore harness](harness.md "harness.md").
- **Agent** - A code-based agent using a framework you choose, deployed to AgentCore Runtime.
- **Skip** - Create the project structure without an agent. Add one later with `agentcore add`.

If you choose **Agent**, the wizard continues with:

- **Framework** - Strands Agents (recommended), LangChain/LangGraph, Google Agent Development Kit, or OpenAI Agents SDK
- **Model provider** - Amazon Bedrock, Anthropic, OpenAI, or Gemini
- **Memory** - None, short-term only, or long-term and short-term
- **Build type** - CodeZip (default) or Container

You can also pass flags directly to create a code-based agent:

```
agentcore create \
  --project-name MyProject \
  --name MyAgent \
  --language Python \
  --framework Strands \
  --model-provider Bedrock \
  --memory none \
  --build CodeZip
```

For all available commands and options, see [AgentCore CLI reference](agentcore-cli-reference.md "agentcore-cli-reference.md").

### Build types

- `CodeZip` (default) packages your code in a zip file and uploads it to Amazon S3. This build type does not require Docker.
- `Container` builds and deploys a container image. This build type requires a running Docker daemon.

### Project structure

`agentcore create` generates shared project configuration and a different application structure for code-based agents and harnesses:

###### Example

Code-based agent

```
MyProject/
├── AGENTS.md
├── README.md
├── agentcore/
│   ├── agentcore.json
│   ├── aws-targets.json
│   └── cdk/
└── app/
    └── MyAgent/
        ├── main.py
        ├── pyproject.toml
        ├── README.md
        ├── model/
        ├── mcp_client/
        └── skills/
```

Harness

```
MyHarnessProject/
├── AGENTS.md
├── README.md
├── agentcore/
│   ├── agentcore.json
│   ├── aws-targets.json
│   └── cdk/
└── app/
    └── MyHarness/
        ├── harness.json
        └── system-prompt.md
```

Key files:

- `agentcore/agentcore.json` - The main configuration file. It defines your agents, harnesses, memory stores, gateways, credentials, and other resources. The `agentcore add` and `agentcore remove` commands manage this file.
- `agentcore/aws-targets.json` - The AWS accounts and Regions for deployment.
- `agentcore/.env.local` - Local secrets, such as API keys for model providers.
- `app/` - The application directory. A code-based agent contains an entrypoint and dependencies. A harness contains `harness.json` and `system-prompt.md`.

## Step 3: Test locally

```
cd MyProject
agentcore dev
```

`agentcore dev` creates a Python virtual environment, installs dependencies, starts a local server with hot reload, and opens the **agent inspector** in your browser so you can chat with the agent, inspect traces, and browse project resources. Code changes are picked up automatically.

## Step 4: Deploy your agent

```
agentcore deploy
```

Deploy:

1. Packages your code into a zip artifact (or builds a container if `--build Container`)
2. Uses AWS CDK under the hood to synthesize and provision resources
3. Creates an AgentCore Runtime endpoint for your agent
4. Configures CloudWatch logging and observability

First deploy takes a few minutes while CDK bootstraps your account. Subsequent deploys are faster.

Preview what will change without deploying:

```
agentcore deploy --dry-run
```

Check status:

```
agentcore status
```

## Step 5: Invoke your deployed agent

```
agentcore invoke --prompt "Hello, what can you do?"
```

If your agent has payments configured, provide payment context at invoke time:

```
agentcore invoke \
  --prompt "Access https://example-x402-merchant.com/paid-api" \
  --payment-instrument-id <INSTRUMENT_ID> \
  --auto-session \
  --payment-user-id user@example.com
```

That’s the loop. Iterate on `app/MyAgent/main.py`, test with `agentcore dev`, deploy with `agentcore deploy`, invoke with `agentcore invoke`.

## Add capabilities to your project

`agentcore add` manages resources in `agentcore.json`. Run it without arguments for the interactive menu, or target a resource directly.

```
agentcore add memory        # Store conversation context
agentcore add agent         # Add a second agent to the same project
agentcore add gateway       # Connect external APIs/tools through Gateway
agentcore add credential    # Add an API key for a non-Bedrock provider
agentcore add evaluator     # Quality evaluation
agentcore add payment-manager   # Payments: create a payment manager
agentcore add payment-connector # Payments: link a payment provider
```

Each add command scaffolds the config and prompts for required values. After adding, run `agentcore deploy` to provision.

Deep dives for the capabilities you can attach:

- [AgentCore Memory](memory.md "memory.md") - short-term and long-term memory, retrieval strategies
- [AgentCore Gateway](gateway.md "gateway.md") - governed connectivity to APIs and MCP servers
- [AgentCore Browser](browser-tool.md "browser-tool.md") - managed web browsing for agents
- [AgentCore Code Interpreter](code-interpreter-tool.md "code-interpreter-tool.md") - sandboxed code execution
- [AgentCore Identity](identity.md "identity.md") - OAuth, API key credential providers, workload identity
- [AgentCore Observability](observability.md "observability.md") - traces, logs, and metrics in CloudWatch
- [AgentCore VPC](agentcore-vpc.md "agentcore-vpc.md") - run agents inside your VPC
- [AgentCore Payments](payments.md "payments.md") - microtransaction payments for agents via x402

## View logs and traces

```
# Stream recent logs
agentcore logs

# Filter
agentcore logs --since 30m --level error
agentcore logs --query "timeout"

# List recent traces
agentcore traces list

# Get a specific trace
agentcore traces get <trace-id>
```

## Troubleshoot

**Permission denied errors**

Verify your credentials with `aws sts get-caller-identity`. Make sure that your identity has the permissions in [Use the AgentCore CLI](runtime-permissions.md#runtime-permissions-cli "runtime-permissions.md#runtime-permissions-cli").

**Model access denied**

Amazon Bedrock enables access to foundation models by default. To use a non-foundation model, follow the [model access steps](../../../bedrock/latest/userguide/model-access.md#model-access-sdk-step4 "../../../bedrock/latest/userguide/model-access.md#model-access-sdk-step4").

**Deployment errors**

Run `agentcore deploy --verbose` to show resource-level deployment events. The CLI checks the AWS CDK bootstrap status. If bootstrap is required, interactive deployment asks for confirmation. `agentcore deploy --yes` approves the bootstrap operation without a prompt.

**Port already in use**

Run `agentcore dev --port 3000` to use a different local port.

**Configuration validation errors**

Run `agentcore validate` to check the project configuration.

For more information, see [Troubleshoot Amazon Bedrock AgentCore Runtime](runtime-troubleshooting.md "runtime-troubleshooting.md").

## Clean up

```
agentcore remove all
agentcore deploy
```

`remove all` resets the configuration. The follow-up `deploy` detects the empty state and tears down the resources in your account.

## Next steps

- [What is the AgentCore harness](harness.md "harness.md") - the config-based path to a running agent. Use any model, connect to tools, persist state, deploy in your VPC, and graduate to code when you need it.
- [AgentCore code samples](https://github.com/awslabs/amazon-bedrock-agentcore-samples "https://github.com/awslabs/amazon-bedrock-agentcore-samples") - end-to-end examples across frameworks and capabilities.
