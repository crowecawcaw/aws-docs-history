# Troubleshoot AgentCore Runtime

This troubleshooting topic helps you identify and resolve common issues when working with
AgentCore Runtime. By following these solutions, you can quickly diagnose and fix problems
with your agent runtimes.

###### Topics

- [My agent invocations fail with 504 Gateway Timeout errors](#troubleshoot-runtime-timeout "#troubleshoot-runtime-timeout")
- [My Docker build fails with "403 Forbidden" when pulling Python base
  images](#troubleshoot-runtime-docker-403 "#troubleshoot-runtime-docker-403")
- [I get "Unknown service: 'bedrock-agent-core-runtime'" error when using
  boto3](#troubleshoot-runtime-boto3 "#troubleshoot-runtime-boto3")
- [I get "AccessDeniedException" when trying to create an Amazon Bedrock AgentCore
  Runtime](#troubleshoot-runtime-access-denied "#troubleshoot-runtime-access-denied")
- [My Docker build fails with "exec /bin/sh: exec format error"](#troubleshoot-runtime-exec-format "#troubleshoot-runtime-exec-format")
- [What are the requirements for Docker containers used with Amazon Bedrock AgentCore
  Runtime?](#troubleshoot-runtime-requirements "#troubleshoot-runtime-requirements")
- [My long-running tool gets interrupted after 15 minutes](#troubleshoot-runtime-long-running "#troubleshoot-runtime-long-running")
- [How do I access the runtimeSessionId in my agent code for tagging or grouping
  resources?](#troubleshoot-runtime-session-id "#troubleshoot-runtime-session-id")
- [I have RuntimeClientError (403) issues](#runtime-client-error "#runtime-client-error")
- [I have missing or empty CloudWatch Logs](#missing-cloudwatch-logs "#missing-cloudwatch-logs")
- [I have payload format issues](#payload-format-issues "#payload-format-issues")
- [I need help understanding HTTP error codes](#common-error-codes "#common-error-codes")
- [I need recommendations for testing my agent](#testing-recommendations "#testing-recommendations")
- [I need help debugging container issues](#debugging-container-issues "#debugging-container-issues")
- [I need help troubleshooting MCP protocol agents](#troubleshooting-mcp-protocol "#troubleshooting-mcp-protocol")
- [Best practices](#best-practices "#best-practices")

## My agent invocations fail with 504 Gateway Timeout errors

**When this occurs:** During agent invocation via SDK
or console

**Why this happens:** Multiple factors can prevent
your agent from responding within the timeout period

Several factors can cause this:

- **Container Issues:** Make sure your Docker
  image exposes port 8080 and has the `/invocations` path
- **ARM64 Compatibility:** Currently your
  container must be ARM64 compatible
- **Retry Logic:** Review retry mechanisms for
  handling transient issues

## My Docker build fails with "403 Forbidden" when pulling Python base

images

**When this occurs:** During `docker
 build` or `docker run` when using `public.ecr.aws`
base images

**Why this happens:** ECR Public authentication
issues — expired or missing authentication is a common issue.

**Solution:** Either login to ECR Public or logout
completely:

```

# Option 1: Login to ECR Public
aws ecr-public get-login-password --region us-east-1 | docker login --username AWS --password-stdin public.ecr.aws

# Option 2: Logout (recommended for avoiding token expiration)
docker logout public.ecr.aws

# Option 3: Use Docker Hub directly in Dockerfile
FROM python:3.10-slim
# instead of public.ecr.aws/docker/library/python:3.10-slim

```

## I get "Unknown service: 'bedrock-agent-core-runtime'" error when using

boto3

**When this occurs:** When invoking Amazon Bedrock AgentCore
APIs using boto3 SDK

**Why this happens:** Outdated boto3 library — common
issue as most installations don't have latest SDK

**Solution:** Update to latest boto3 and botocore
versions:

```

pip install --upgrade boto3 botocore

# Minimum versions: boto3 1.39.8+, botocore 1.33.8+

```

## I get "AccessDeniedException" when trying to create an Amazon Bedrock AgentCore

Runtime

**When this occurs:** During agent creation via
console, SDK, or CLI

**Why this happens:** Either your user lacks
permissions, or the execution role isn't properly configured for
Amazon Bedrock AgentCore

**Solution:** Several factors can cause this:

- **Missing permissions for the caller.** Make
  sure that the caller's credentials has
  `bedrock-agentcore:CreateAgentRuntime`.
- **Execution Role cannot be assumed by Bedrock
  Amazon Bedrock AgentCore.** Make sure that the execution role follows
  this guidance on [permissions for Amazon Bedrock AgentCore Runtime execution
  role](runtime-permissions.md "runtime-permissions.md").

## My Docker build fails with "exec /bin/sh: exec format error"

**When this occurs:** When building containers for
Amazon Bedrock AgentCore deployment

**Why this happens:** Building ARM64 containers on
x86 systems without proper cross-platform setup

**Solution:** Build ARM64 compatible containers. You can
consider using [buildx](https://github.com/docker/buildx "https://github.com/docker/buildx") for
cross-platform builds. Alternatively, you can use CodeBuild. For example code, see the
[Amazon Bedrock AgentCore Samples](https://github.com/awslabs/amazon-bedrock-agentcore-samples/ "https://github.com/awslabs/amazon-bedrock-agentcore-samples/").

## What are the requirements for Docker containers used with Amazon Bedrock AgentCore

Runtime?

Review [Amazon Bedrock AgentCore Runtime requirements](runtime-service-contract.md "runtime-service-contract.md") for full details.

In summary, your Docker container must meet these requirements:

- **Port:** Expose port 8080 (additional ports
  will be supported soon)
- **Endpoint:** Must have
  `/invocations` path available
- **Architecture:** Must be ARM64
  compatible
- **Response:** Should handle the expected
  payload format

## My long-running tool gets interrupted after 15 minutes

For information, see [Handle asynchronous and long running agents with Amazon Bedrock
Amazon Bedrock AgentCore Runtime](runtime-long-run.md "runtime-long-run.md") for full details.

**When this occurs:** During long-running agent
operations or complex workflows

**Why this happens:** Amazon Bedrock AgentCore automatically
terminates sessions after 15 minutes of inactivity

**Example solution:** Implement ping handlers with
HEALTHY_BUSY status for async tasks:

```

import asyncio
from bedrock_agentcore.runtime import BedrockAgentCoreApp

app = BedrockAgentCoreApp()

@app.entrypoint
async def long_running_agent(payload, context):
    # For long-running tasks, create async task with ping handler
    async def ping_handler():
        while task_running:
            await context.ping(status="HEALTHY_BUSY")
            await asyncio.sleep(30)  # Ping every 30 seconds

    # Start ping handler
    ping_task = asyncio.create_task(ping_handler())

    # Your long-running work here
    result = await perform_long_task()

    # Clean up
    ping_task.cancel()
    return result

```

## How do I access the runtimeSessionId in my agent code for tagging or grouping

resources?

**When this applies:** You want to group, tag, or
trace resources (e.g., S3 objects, logs) by the current agent runtime
session.

**Solutions:**

- If you're using the Bedrock Agents SDK, use
  `context.session_id`.
- If you're building a custom runtime server, extract it from the
  `X-Amzn-Bedrock-AgentCore-Runtime-Session-Id` HTTP
  header.

**Solution 1:** For agents using the Bedrock
Amazon Bedrock AgentCore SDK, use `context.session_id` from your agent
entrypoint

```

@app.entrypoint
def my_agent(payload, context):
    session_id = context.session_id

    # Use session_id for S3 object tagging/organization
    s3_client = boto3.client('s3')
    s3_client.put_object(
        Bucket='my-bucket',
        Key=f'agent-outputs/{session_id}/output.json',
        Body=json.dumps(result),
        Tagging=f'SessionId={session_id}'
    )
    return result

```

**Solution 2:** For custom runtime HTTP
servers

The runtime session ID is passed in this HTTP header. Parse it from the incoming
request and use it for tagging, correlation, or downstream propagation.

```

X-Amzn-Bedrock-AgentCore-Runtime-Session-Id: <value>

```

## I have RuntimeClientError (403) issues

###### Problem

You receive a 403 "RuntimeClientError" when attempting to invoke your agent
runtime.

###### Causes

This error typically occurs due to:

- Container startup failures
- Permissions issues with execution role
- Authentication issues with bearer token

###### Resolution

Follow these steps to resolve the issue:

1. **Check CloudWatch Logs**: Any issues with
   starting up the container will reflect as a 403 - RuntimeClientError.
   Navigate to the following CloudWatch log group to check for startup
   errors:

```
/aws/bedrock-agentcore/runtimes/<agent_id>-<endpoint_name>/[runtime-logs]
```

2. **Verify Execution Role**: Ensure your
   agent's execution role has the necessary permissions. For more information, see
   [AgentCore Runtime execution role](runtime-permissions.md#runtime-permissions-execution-role "runtime-permissions.md#runtime-permissions-execution-role").
3. **Validate Authentication**: For MCP protocol
   agents, ensure your bearer token is valid and not expired.

## I have missing or empty CloudWatch Logs

###### Problem

You encounter errors but don't see any relevant logs in CloudWatch.

###### Solution

Try these approaches to diagnose the issue:

1. **Check Correct Log Group**: Ensure you're
   looking in the right CloudWatch log group. The standard pattern is:

```
/aws/bedrock-agentcore/runtimes/<agent_id>-<endpoint_name>/runtime-logs
```

2. **Run Locally for Diagnostics**: If there are
   no CloudWatch Logs, try running the agent container locally using the exact
   same payload you used for invocation in AgentCore Runtime. This can help
   identify issues that might not be visible in the logs.
3. **Enable Verbose Logging**: Update your agent
   code to include more detailed logging, especially around the entry points
   and any error handling logic.

## I have payload format issues

###### Problem

Your agent runtime invocation fails even though the container starts
successfully.

###### Resolution

Follow these steps to resolve payload format issues:

1. **Verify Payload Structure**: Ensure your
   payload structure matches what your agent expects. Pay special attention
   to:
   - If your agent code expects `input` keyword in the
     payload, make sure to include it:

   ```
   {
       "input": {
           "prompt": "Your question here"
       }
   }
   ```

   - Not just:

   ```
   {
        "prompt": "Your question here"
   }
   ```

2. **Check Documentation**: Review the expected
   input format in the documentation.

## I need help understanding HTTP error codes

###### Problem

Your agent returns HTTP error codes that are difficult to interpret.

###### Resolution

Here are the most common error codes and their meanings:

**422 Unprocessable Entity**

This happens when the container encounters validation issues with the
input payload.

Common causes:

- Missing required fields in the payload (e.g., missing "input"
  field)
- Incorrect data types for fields
- Invalid format for the payload

**403 Forbidden**

Authentication or authorization issues.

Check your bearer token or IAM permissions.

**500 Internal Server Error**

Runtime exceptions in your agent code.

Check CloudWatch logs for detailed stack traces.

## I need recommendations for testing my agent

To systematically debug agent runtime issues:

###### Test locally first

Before deploying to AgentCore Runtime:

- Run your agent container locally using the same Docker image
- Verify it works with the exact same payload

###### Compare payloads

Ensure consistency between environments:

- Ensure the payload structure between local testing and AgentCore Runtime
  invocation is identical
- Pay special attention to nesting of fields like "input" and
  "prompt"

## I need help debugging container issues

If you suspect container-related issues:

###### Pull and run locally

Test your container image on your local machine:

```
docker pull <your-ecr-repo-uri>
docker run -p 8080:8080 <your-ecr-repo-uri>
```

###### Test with curl

Send test requests to your local container:

```
curl -X POST http://localhost:8080/invocations \
     -H "Content-Type: application/json" \
     -d '{"input": {"prompt": "Hello world!"}}'
```

###### Check container logs

Examine the container's output for errors:

```
docker logs <container-id>
```

## I need help troubleshooting MCP protocol agents

For MCP protocol agents, follow these specific troubleshooting steps:

###### Verify endpoint path

MCP servers should listen on `0.0.0.0:8000/mcp/`

###### Use MCP Inspector

Test with the MCP Inspector tool:

1. Install and run the MCP Inspector: `npx
@modelcontextprotocol/inspector`
2. Connect to your local server at
   `http://localhost:8000/mcp`
3. For deployed agents, use the properly URL-encoded endpoint

###### Authentication issues

Check authentication configuration:

- Ensure bearer token is correctly set in the headers
- Verify your Cognito user pool is correctly set up

## Best practices

###### Enable comprehensive logging

Implement thorough logging in your agent:

- Include request/response logging in your agent
- Log critical paths and error conditions

###### Use structured error handling

Implement clear error reporting:

- Return clear error messages with specific codes
- Include actionable information in error responses

###### Test incremental changes

Follow a methodical testing approach:

- When modifying your agent, test locally before deployment
- Validate payload compatibility with both local and deployed
  environments

###### Monitor performance

Set up monitoring for your agent:

- Use CloudWatch metrics to track invocation patterns
- Set up alarms for error rates and latency
