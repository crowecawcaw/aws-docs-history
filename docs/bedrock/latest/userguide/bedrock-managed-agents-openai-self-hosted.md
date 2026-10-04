

# Run your first agent with self-hosted compute
<a name="bedrock-managed-agents-openai-self-hosted"></a>

This tutorial connects a local or remote host to a BMA session. The host runs `codex exec-server`, and BMA uses that connection for tool execution. The example creates IAM roles in your AWS account and uses a workspace on your host.

Complete the [prerequisites](bedrock-managed-agents-openai-prerequisites.md) first. The host needs outbound HTTPS and WebSocket connectivity to the BMA endpoint. Keep the exec-server process running while the agent uses this environment.

## Step 1: Deploy the IAM roles
<a name="bedrock-managed-agents-openai-self-hosted-step-1-deploy-the-iam-roles"></a>

From the extracted bundle root:

```
cd self-hosted
npm ci
npx cdk bootstrap
npm run deploy
```

Review the IAM changes when CDK prompts you. If another stack already owns `BedrockManagedAgentsPreviewInferenceServiceRole`, use:

```
npm run deploy -- --parameters ManageCustomerInferenceRole=false
```

The stack outputs `BmaAccessRoleArn` and `CustomerInferenceRoleArn`. Configure your normal credential tooling to use the client role, or use an existing identity with equivalent permissions. The session role is assumed by BMA; it is not the profile used by your local scripts.

## Step 2: Create a workspace and session
<a name="bedrock-managed-agents-openai-self-hosted-step-2-create-a-workspace-and-session"></a>

Select your BMA client profile and create a dedicated workspace. The path must exist on the host where the exec server runs.

```
export AWS_PROFILE=my-bma-client-profile
export BMA_REGION=us-east-1
export BMA_ENDPOINT="https://bedrock-mantle.${BMA_REGION}.api.aws"
export BMA_WORKSPACE_DIRECTORY="$PWD/workspace"
mkdir -p "$BMA_WORKSPACE_DIRECTORY/skills"

./scripts/bma/0.create-session.sh
```

The script resolves credentials from the selected profile and includes `role_arn` in its request. By default, the ARN names the example's session role in the calling account. To use another role, set `BMA_INFERENCE_ROLE_ARN` before creating the session.

A successful response includes a session ID, an environment ID, the selected model, and the session role ARN. The script saves the configuration and IDs to `scripts/bma/.bma-session.env` with owner-only permissions. It does not store AWS access keys in that file.

## Step 3: Attach the exec server
<a name="bedrock-managed-agents-openai-self-hosted-step-3-attach-the-exec-server"></a>

Open a second terminal, select the same AWS client profile, and change to the same `self-hosted/` directory:

```
export AWS_PROFILE=my-bma-client-profile
./scripts/bma/1.attach-exec-server.sh
```

The script uses `bin/codex` in the bundle root. To select a different host executable:

```
./scripts/bma/1.attach-exec-server.sh /path/to/host/codex
```

Leave this process running. Its log reports when the direct exec-server connection is established. Registration and the WebSocket handshake use AWS SigV4 authentication. A session ID alone does not grant access to the environment.

## Step 4: Submit work
<a name="bedrock-managed-agents-openai-self-hosted-step-4-submit-work"></a>

In the first terminal:

```
./scripts/bma/2.submit-turn.sh "Run: uname -a"
./scripts/bma/3.read-result.sh
```

Submitting a message starts a turn. The result script polls the session and then retrieves its durable items. Inspect the returned message and command-execution items to confirm that the agent ran the command on the execution host.

Submit another message to continue the same conversation:

```
./scripts/bma/2.submit-turn.sh "Summarize the operating system information you just retrieved."
./scripts/bma/3.read-result.sh
```

Process one turn at a time in this introductory workflow. See [sessions and results](bedrock-managed-agents-openai-sessions.md) for event streaming, cancellation, pagination, and error handling.

## Step 5: Delete the session
<a name="bedrock-managed-agents-openai-self-hosted-step-5-delete-the-session"></a>

```
./scripts/bma/4.delete-session.sh
```

The script deletes the BMA session and removes its local state file. Stop the exec-server process in the second terminal. Files created in the workspace remain on your host until you remove them.

To remove the IAM stack, switch back to your deployment profile and follow [cleanup](bedrock-managed-agents-openai-cleanup.md). Keep the stack if another active example still uses its session role.