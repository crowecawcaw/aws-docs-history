

# Troubleshooting
<a name="bedrock-managed-agents-openai-troubleshooting"></a>

Use the HTTP response, session error details, event stream, and execution-environment logs together. An API request can be accepted before the agent or its execution environment is ready to complete work.

## Session creation returns HTTP 400
<a name="bedrock-managed-agents-openai-troubleshooting-session-creation-returns-http-400"></a>

Check the response body. Confirm that the request includes `agent.model`, `environment`, and a same-account `role_arn`. Older examples that rely on an inference role by name without passing its ARN must be updated.

Use the preview's supported input types and tool configuration. Subagent configuration and provider-specific fields outside the supported surface can cause validation errors.

The supplied scripts print API error bodies to standard error so they remain visible when a command fails.

## Access is denied
<a name="bedrock-managed-agents-openai-troubleshooting-access-is-denied"></a>

Run `aws sts get-caller-identity` with the selected profile. Confirm that:

1. The caller has the required BMA action permissions.

1. The caller can pass the exact session role, with `iam:PassedToService` set to `bedrock-mantle.amazonaws.com`.

1. The session role trusts the BMA service principal and permits inference for the selected model.

1. For AgentCore, the session role can invoke and stop the configured Runtime.

1. The execution identity can register and connect to the BMA environment.

An identity used to deploy a stack is not automatically the identity used by the session scripts. Check `AWS_PROFILE` in each terminal.

## An endpoint or API returns HTTP 404
<a name="bedrock-managed-agents-openai-troubleshooting-an-endpoint-or-api-returns-http-404"></a>

Check the Region, endpoint, and path. Session operations use `/openai/v1/agents/sessions`; model discovery uses `/v1/models`.

For an existing session, check that its ID belongs to the same Region and has not been deleted. A 404 can also indicate unavailable preview access or an API that is not deployed. The dedicated turn-list and turn-retrieval routes are not used by this guide.

## The exec server does not connect
<a name="bedrock-managed-agents-openai-troubleshooting-the-exec-server-does-not-connect"></a>

Verify that the executable matches the host's operating system and architecture and supports `codex exec-server`. Use version 0.154.0 or later for these examples.

Check that the environment ID came from the session you intend to use. Use direct transport and SigV4 signing, with the correct Region and `bedrock-mantle` signing service. Confirm outbound HTTPS and WebSocket connectivity through the host's network path.

Keep the attach process running. Its diagnostic log reports registration or WebSocket errors. A running process is not sufficient evidence of a connected environment; look for the connection acknowledgement.

## A session remains in progress
<a name="bedrock-managed-agents-openai-troubleshooting-a-session-remains-in-progress"></a>

Check whether the exec server is connected and whether the active command is still running. Read the event stream for progress, and inspect the Runtime or host logs for failures.

The result script's default timeout is 300 seconds. You can change it with `BMA_POLL_TIMEOUT`, but first determine why the turn is not finishing. Use a cancel event if the task should stop. Cancellation does not undo completed tool actions.

## The event stream appears to wait without output
<a name="bedrock-managed-agents-openai-troubleshooting-the-event-stream-appears-to-wait-without-output"></a>

The events endpoint is a live SSE connection. Open it before submitting a turn, then submit work in another terminal. Do not attempt to parse the response as a JSON array. Use the items endpoint to retrieve durable output from completed work.

## A skill or MCP server is missing
<a name="bedrock-managed-agents-openai-troubleshooting-a-skill-or-mcp-server-is-missing"></a>

For a skill, confirm that the execution environment contains `<skill-name>/SKILL.md` beneath a configured capability directory. Verify the path inside the actual host or container, not just on the deployment machine.

For an MCP server, check its absolute executable path, arguments, working directory, required dependencies, and allowed tool names. The server must speak the MCP STDIO protocol on standard output. Send diagnostic messages to standard error.

For AgentCore, wait for S3 Files synchronization and create a new session after deploying changed image content. Updating the Runtime definition does not replace processes in an already-running session.

## CDK reports that the environment is not bootstrapped
<a name="bedrock-managed-agents-openai-troubleshooting-cdk-reports-that-the-environment-is-not-bootstrapped"></a>

Set `AWS_REGION` and `AWS_DEFAULT_REGION` explicitly, then run `npx cdk bootstrap` in that account and Region. A profile configured for one Region does not override conflicting environment variables.

## CloudFormation reports an existing IAM role
<a name="bedrock-managed-agents-openai-troubleshooting-cloudformation-reports-an-existing-iam-role"></a>

The two examples use the same default session-role name. Set `ManageCustomerInferenceRole=false` for a stack that should reuse the existing role. Confirm that the existing role has the required trust and permissions. CloudFormation does not adopt it automatically.

## AgentCore deployment fails
<a name="bedrock-managed-agents-openai-troubleshooting-agentcore-deployment-fails"></a>

Read the failing CloudFormation resource's status reason. Common prerequisites include a Linux ARM64 Codex binary, a working Docker build environment, available VPC and networking quotas, and Availability Zones enabled for the account.

The example's storage mount targets and Runtime can take several minutes to become available. Wait for stack completion before starting a session. Do not treat an in-progress resource as a completed deployment.

During deletion, security groups and subnets can wait for network interfaces created by the service to be released. Inspect the interface's association and the CloudFormation status reason. Remove the associated service resources through their normal service APIs; do not force-detach a service-owned interface. Contact AWS Support if the dependency persists after service cleanup.

If EC2 reports `OperationNotPermitted` with `You are not allowed to manage 'ela-attach' attachments`, the attachment must be released by the associated service. Request service-side assistance with the Runtime ID, Region, and network interface IDs. Retain the failed stack and its deployment role so that you can retry stack deletion after the dependency is cleared. Increasing the caller's IAM permissions does not resolve this attachment restriction.

## Generated output is not yet in S3
<a name="bedrock-managed-agents-openai-troubleshooting-generated-output-is-not-yet-in-s3"></a>

Confirm that the agent wrote to `/mnt/output`, that the Runtime reported the mount as writable, and that the command succeeded. S3 Files synchronization is asynchronous. Retry the S3 read after the file synchronizes, and use the bucket name from the stack outputs.

## Information to retain for support
<a name="bedrock-managed-agents-openai-troubleshooting-information-to-retain-for-support"></a>

Record the AWS Region, approximate UTC time, request ID, session ID, HTTP status, model ID, and relevant error text. Include the exec-server version and execution-environment type. Remove credentials and sensitive prompt or tool data before sharing logs.