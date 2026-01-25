# Get started with the Amazon Bedrock AgentCore starter

toolkit in TypeScript

This tutorial shows you how to use the Amazon Bedrock AgentCore [starter toolkit](https://github.com/aws/bedrock-agentcore-starter-toolkit "https://github.com/aws/bedrock-agentcore-starter-toolkit")
to deploy a TypeScript agent to an Amazon Bedrock AgentCore Runtime.

The starter toolkit is a Command Line Interface (CLI) toolkit that you can use to deploy
AI agents to an Amazon Bedrock AgentCore Runtime. This tutorial shows you how to create and deploy
a TypeScript agent using the [bedrock-agentcore](https://www.npmjs.com/package/bedrock-agentcore "https://www.npmjs.com/package/bedrock-agentcore") SDK.

For information about the HTTP protocol that the agent uses, see [HTTP protocol contract](runtime-http-protocol-contract.md "runtime-http-protocol-contract.md").

###### Topics

- [Prerequisites](#ts-prerequisites "#ts-prerequisites")
- [Step 1: Set up project and install dependencies](#ts-setup-project "#ts-setup-project")
- [Step 2: Create your agent project](#ts-create-agent "#ts-create-agent")
- [Step 3: Configure your agent](#ts-configure-agent "#ts-configure-agent")
- [Step 4: Test your agent locally](#ts-test-locally "#ts-test-locally")
- [Step 5: Enable observability for your
  agent](#ts-enable-observability "#ts-enable-observability")
- [Step 6: Deploy to Amazon Bedrock AgentCore Runtime](#ts-deploy-runtime "#ts-deploy-runtime")
- [Step 7: Test your deployed agent](#ts-test-deployed-agent "#ts-test-deployed-agent")
- [Step 8: Invoke your agent
  programmatically](#ts-invoke-programmatically "#ts-invoke-programmatically")
- [Step 9: Clean up](#ts-clean-up "#ts-clean-up")
- [Find your resources](#ts-find-resources "#ts-find-resources")
- [Common issues and solutions](#ts-common-issues "#ts-common-issues")
- [Advanced: Streaming responses](#ts-streaming-responses "#ts-streaming-responses")

## Prerequisites

Before you start, make sure you have:

- **AWS Account** with credentials configured. To
  configure your AWS credentials, see [Configuration and credential file settings in the AWS CLI.](../../../cli/latest/userguide/cli-configure-files.md "../../../cli/latest/userguide/cli-configure-files.md")
- **Node.js 20+** installed
- **Python 3.10+** installed (required for the starter toolkit CLI)
- **AWS Permissions**: To create and deploy an
  agent with the starter toolkit, you must have appropriate permissions. For
  information, see [Use the starter toolkit](runtime-permissions.md#runtime-permissions-starter-toolkit "runtime-permissions.md#runtime-permissions-starter-toolkit").
- **Model access**: If your agent uses Amazon Bedrock models, ensure the required models are
  [enabled](../../../bedrock/latest/userguide/model-access-modify.md "../../../bedrock/latest/userguide/model-access-modify.md") in the Amazon Bedrock console.

## Step 1: Set up project and install dependencies

Create a project folder and initialize your TypeScript project:

```
mkdir agentcore-typescript-quickstart
cd agentcore-typescript-quickstart
npm init -y
```

Install the required packages:

- **bedrock-agentcore** - The Amazon Bedrock AgentCore SDK
  for building AI agents in TypeScript
- **@strands-agents/sdk** - The [Strands Agents](https://strandsagents.com/latest/ "https://strandsagents.com/latest/") SDK
- **@opentelemetry/auto-instrumentations-node** - OpenTelemetry instrumentation for observability
- **typescript** - TypeScript compiler

```
npm install bedrock-agentcore @strands-agents/sdk @opentelemetry/auto-instrumentations-node
npm install --save-dev typescript @types/node tsx
```

Install the starter toolkit CLI (requires Python):

```
pip install --upgrade bedrock-agentcore-starter-toolkit
```

Verify installation:

```
agentcore --help
```

## Step 2: Create your agent project

Create a `tsconfig.json` file with the following content:

```
{
  "compilerOptions": {
    "target": "ES2022",
    "module": "NodeNext",
    "moduleResolution": "NodeNext",
    "outDir": "./dist",
    "rootDir": ".",
    "strict": true,
    "esModuleInterop": true,
    "skipLibCheck": true,
    "declaration": true
  },
  "include": ["*.ts"],
  "exclude": ["node_modules", "dist"]
}
```

Update your `package.json` to add the required configuration:

```
{
  "name": "agentcore-typescript-quickstart",
  "version": "1.0.0",
  "type": "module",
  "main": "dist/agent.js",
  "scripts": {
    "build": "tsc",
    "start": "node dist/agent.js",
    "dev": "npx tsx --watch agent.ts"
  },
  "engines": {
    "node": ">=20.0.0"
  },
  "dependencies": {
    "bedrock-agentcore": "^0.2.0",
    "@strands-agents/sdk": "^0.1.5",
    "@opentelemetry/auto-instrumentations-node": "^0.56.0"
  },
  "devDependencies": {
    "@types/node": "^22.0.0",
    "typescript": "^5.5.0",
    "tsx": "^4.0.0"
  }
}
```

Create an `agent.ts` file with your agent code:

```
import { BedrockAgentCoreApp } from 'bedrock-agentcore/runtime';
import { Agent } from '@strands-agents/sdk';

// Create a Strands agent
const agent = new Agent();

// Create and start the server
const app = new BedrockAgentCoreApp({
  invocationHandler: {
    process: async (payload, context) => {
      const prompt = (payload as { prompt?: string }).prompt ?? 'Hello!';
      console.log(`Session ${context.sessionId} - Received prompt:`, prompt);

      const result = await agent.invoke(prompt);
      return result;
    }
  }
});

app.run();
```

Build your TypeScript project:

```
npm run build
```

## Step 3: Configure your agent

Run the `agentcore configure` command to set up your agent for deployment:

```
agentcore configure --entrypoint agent.ts
```

The command will:

- Detect your TypeScript project automatically
- Prompt you for an agent name
- Configure container deployment (required for TypeScript)
- Create a `.bedrock_agentcore.yaml` configuration file

###### Note

TypeScript projects require container deployment. The direct code deploy option is only available for Python projects.

## Step 4: Test your agent locally

Before deploying to AWS, test your agent locally using the development server:

```
agentcore dev
```

- This command starts a local server that mimics the AgentCore Runtime environment
- For TypeScript, it runs `npm run dev` or uses `tsx` to watch your files
- The server runs on `http://localhost:8080` by default

In a separate terminal, test your agent:

```
agentcore invoke --dev '{"prompt": "Hello!"}'
```

## Step 5: Enable observability for your

agent

[Amazon Bedrock AgentCore Observability](observability.md "observability.md") helps you trace, debug, and monitor agents
that you host in Amazon Bedrock AgentCore Runtime. First enable CloudWatch Transaction Search
by following the instructions at [Enabling Amazon Bedrock AgentCore runtime observability](observability-configure.md#observability-configure-builtin "observability-configure.md#observability-configure-builtin"). To observe your agent,
see [View observability data for your Amazon Bedrock AgentCore agents](observability-view.md "observability-view.md").

## Step 6: Deploy to Amazon Bedrock AgentCore Runtime

Deploy your agent to AgentCore Runtime:

```
agentcore deploy
```

This command:

- Builds your container using AWS CodeBuild (no Docker required
  locally)
- Creates necessary AWS resources (IAM roles, ECR repository, etc.)
- Deploys your agent to Amazon Bedrock AgentCore Runtime
- Configures CloudWatch logging

In the output from `agentcore deploy` note the following:

- The Amazon Resource Name (ARN) of the agent. You need it to invoke the agent
  with the [InvokeAgentRuntime](../APIReference/API_InvokeAgentRuntime.md "../APIReference/API_InvokeAgentRuntime.md") operation.
- The location of the logs in Amazon CloudWatch Logs

If the deployment fails check for [common issues](#ts-common-issues "#ts-common-issues").

## Step 7: Test your deployed agent

Test your deployed agent:

```
agentcore invoke '{"prompt": "tell me a joke"}'
```

If you see a response, your agent is now running in an Amazon Bedrock AgentCore
Runtime and can be invoked. If not, check for [common issues](#ts-common-issues "#ts-common-issues").

## Step 8: Invoke your agent

programmatically

You can invoke the agent using the AWS SDK [InvokeAgentRuntime](../APIReference/API_InvokeAgentRuntime.md "../APIReference/API_InvokeAgentRuntime.md")
operation. To call `InvokeAgentRuntime`, you need the ARN of the agent that
you noted in Step 6. You can also get the ARN from
the `bedrock_agentcore:` section of the
`.bedrock_agentcore.yaml` (hidden) file that the toolkit creates.

Create a file named `invoke-agent.ts` and add the following code:

```
import {
  BedrockAgentCoreClient,
  InvokeAgentRuntimeCommand
} from '@aws-sdk/client-bedrock-agentcore';
import { randomUUID } from 'crypto';

const agentArn = '`Agent ARN`';
const prompt = 'Tell me a joke';

// Initialize the Amazon Bedrock AgentCore client
const client = new BedrockAgentCoreClient({ region: 'us-west-2' });

// Invoke the agent
const command = new InvokeAgentRuntimeCommand({
  agentRuntimeArn: agentArn,
  runtimeSessionId: randomUUID(),
  payload: JSON.stringify({ prompt }),
  contentType: 'application/json',
  qualifier: 'DEFAULT',
});

const response = await client.send(command);
const textResponse = await response.response?.transformToString();

console.log('Response:', textResponse);
```

Run the code with the following command:

```
npx tsx invoke-agent.ts
```

If successful, you should see a response from your agent. If the call fails, check the
logs that you noted in [Step 6: Deploy to Amazon Bedrock AgentCore Runtime](#ts-deploy-runtime "#ts-deploy-runtime").

###### Note

If you plan on integrating your agent with OAuth, you can't use the AWS SDK to
call `InvokeAgentRuntime`. Instead, make a HTTPS request to
`InvokeAgentRuntime`. For more information, see [Authenticate and authorize with Inbound Auth and Outbound Auth](runtime-oauth.md "runtime-oauth.md").

## Step 9: Clean up

If you no longer want to host the agent in the AgentCore Runtime, use the `destroy` command
to delete the AWS resources that the starter toolkit
created for you.

```
agentcore destroy
```

## Find your resources

After deployment, view your resources in the AWS Console:

| Resource locations   | Resource                                                                          | Location |
| -------------------- | --------------------------------------------------------------------------------- | -------- |
| **Agent Logs**       | CloudWatch → Log groups →<br>`/aws/bedrock-agentcore/runtimes/{agent-id}-DEFAULT` |
| **Container Images** | ECR → Repositories →<br>`bedrock-agentcore-{agent-name}`                          |
| **Build Logs**       | CodeBuild → Build history                                                         |
| **IAM Role**         | IAM → Roles → Search for "BedrockAgentCore"                                       |

## Common issues and solutions

Common issues and solutions when getting started with the Amazon Bedrock AgentCore starter
toolkit for TypeScript. For more troubleshooting information, see [Troubleshoot Amazon Bedrock AgentCore Runtime](runtime-troubleshooting.md "runtime-troubleshooting.md").

**Permission denied errors**

Verify your AWS credentials and permissions:

- Verify AWS credentials: `aws sts
get-caller-identity`
- Check you have the required policies attached
- Review caller permissions policy for detailed requirements

**TypeScript compilation errors**

Ensure your TypeScript configuration is correct:

- Verify `tsconfig.json` exists and has correct settings
- Run `npm run build` locally to check for errors
- Ensure `"type": "module"` is set in `package.json`

**CodeBuild build error**

Check build logs and permissions:

- Check CodeBuild project logs in AWS console
- Verify your `package.json` has a `build` script
- Ensure all dependencies are listed in `package.json`

**Port 8080 in use (local only)**

Find and stop processes that are using port 8080:

Use `lsof -ti:8080` to get a list of process using port 8080.

Use `kill -9
 `PID``to stop the process. Replace`PID` with
the process ID.

**Region mismatch**

Verify the AWS Region with `aws configure get region` and
make sure resources are in same Region

**Module not found errors**

Ensure your imports use the correct paths:

- Use `bedrock-agentcore/runtime` for the runtime module
- Run `npm install` to ensure all dependencies are installed

## Advanced: Streaming responses

Your TypeScript agent can return streaming responses using async generators. This is useful for long-running operations or when you want to provide incremental updates to the client:

```
import { BedrockAgentCoreApp } from 'bedrock-agentcore/runtime';

// Streaming handler using async generator
const streamingHandler = async function* (request: unknown, context: { sessionId: string }) {
  yield { event: 'start', sessionId: context.sessionId };

  // Simulate processing steps
  for (let i = 0; i < 5; i++) {
    yield {
      event: 'progress',
      step: i + 1,
      data: `Processing step ${i + 1}`,
    };
  }

  yield { event: 'complete', result: 'done' };
};

const app = new BedrockAgentCoreApp({
  invocationHandler: { process: streamingHandler },
});

app.run();
```

The server automatically handles streaming responses using Server-Sent Events (SSE).
