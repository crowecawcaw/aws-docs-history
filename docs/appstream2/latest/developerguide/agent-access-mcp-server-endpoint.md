

# Connecting to the MCP server
<a name="agent-access-mcp-server-endpoint"></a>

This topic explains how to connect an agent to the Amazon WorkSpaces Applications Model Context Protocol (MCP) server. Connecting involves negotiating an MCP protocol version with the server and authorizing each request. This topic covers the endpoint the agent calls, how it authorizes its requests, and how it identifies a streaming session.

Agents connect to the MCP server at the following endpoint:

```
https://agentaccess-mcp.{{region}}.api.aws/mcp
```

Replace {{region}} with your Region code. For the supported Regions and their endpoints, see [WorkSpaces Applications MCP endpoints](allowed-domains.md#allowed-domains-mcp-endpoints).

The MCP server is hosted in the AWS cloud and uses Streamable HTTP as its transport protocol. You don't need to install or maintain any server components.

**Note**  
Before an agent can connect, the fleet associated with your stack must be running and have available capacity.

## Supported MCP protocol versions
<a name="agent-access-mcp-server-protocol-versions"></a>

The MCP server supports the following versions of the Model Context Protocol. Your MCP client negotiates the version with the server when it connects.


| Version | Type | 
| --- | --- | 
| 2025-03-26 | Stateful | 
| 2025-06-18 | Stateful | 
| 2025-11-25 | Stateful | 
| 2026-07-28 | Stateless | 

Version 2026-07-28 is the stateless MCP protocol. With the stateless protocol, the agent ends the session with the `close_session` tool. For more information about the tool, see [Available tools](agent-access-mcp-server-tools.md). With the earlier MCP protocol versions, you end the session by closing the MCP client in your agent code, which sends an HTTP `DELETE` request. For more information, see [Session cleanup](agent-access-mcp-server-session-cleanup.md).

## Request authorization
<a name="agent-access-mcp-server-authorization"></a>

You can authorize requests in one of two ways: SigV4 signing or OAuth 2.1 authorization through AWS Sign-In.

### SigV4 signing
<a name="agent-access-mcp-server-authorization-sigv4"></a>

To use Signature Version 4 (SigV4), sign each request using IAM credentials with the service name `agentaccess-mcp`. The following Python example shows the general connection pattern using `mcp-proxy-for-aws`:

```
from mcp_proxy_for_aws import aws_iam_streamablehttp_client

async with aws_iam_streamablehttp_client(
    endpoint="https://agentaccess-mcp.{{region}}.api.aws/mcp",
    aws_service="agentaccess-mcp",
    aws_region="{{region}}",
    headers={
        # Fleet-type-specific headers (see the following subsections)
    },
    metadata={
        # Fleet-type-specific metadata (see the following subsections)
    },
) as (read, write, _):
    # Use read/write streams with your MCP client
    ...
```

For other languages, write your own SigV4 signing logic for outgoing MCP requests or use a library that supports SigV4 signing. For more information about `mcp-proxy-for-aws`, see [mcp-proxy-for-aws](https://github.com/aws/mcp-proxy-for-aws) on GitHub.

### OAuth 2.1 authorization
<a name="agent-access-mcp-server-connect-oauth"></a>

As an alternative to signing requests with IAM credentials, the MCP server supports OAuth 2.1 authorization through AWS Sign-In, the same way as the AWS MCP Server. AWS Sign-In acts as the authorization server. It issues short-lived, scoped access tokens, and the MCP server accepts these tokens as bearer tokens. OAuth uses your existing IAM identities, permissions, and organizational controls. When you authorize an agent, it can access the MCP server on your behalf without gaining extra permissions. AWS still checks every request against your IAM policies.

OAuth-compatible MCP clients, such as Kiro, Claude Code, Cursor, Codex, and Gemini, can connect directly to the MCP server endpoint without local proxy software. AWS Sign-In supports two authorization models:
+ **Interactive authorization** – This model is for agents that can open a browser. The client registers through dynamic client registration and redirects you to an AWS Sign-In page to authenticate and approve access. AWS Sign-In then issues and refreshes the access tokens.
+ **Non-interactive authorization** – This model is for agents that already have AWS credentials and run without a browser (headless authorization). The agent exchanges its SigV4-signed credentials for a short-lived access token by using the OAuth client credentials grant.

OAuth authorization for the MCP server works the same way as it does for the AWS MCP Server, using the MCP server endpoint (`https://agentaccess-mcp.{{region}}.api.aws/mcp`). For setup, required IAM permissions, and governance and monitoring options, see [OAuth 2.1 authentication for AWS MCP Server](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/oauth-authentication.html) in the *Agent Toolkit for AWS User Guide* and [Sign-In with OAuth 2.0](https://docs.aws.amazon.com/signin/latest/userguide/oauth-sign-in-overview.html) in the *AWS Sign-In User Guide*.

## Session identification
<a name="agent-access-mcp-server-session-id"></a>

How you identify the streaming session depends on your fleet type.

**Note**  
At any given time, only one agent can connect to a unique session. Named users, specified through the `UserId` parameter, can have only one active session per fleet at a time. To run multiple agents concurrently, each agent must connect to its own unique session.

### Connecting with non-domain-joined fleets
<a name="agent-access-mcp-server-connect-ndj"></a>

For non-domain-joined fleets, you can connect in one of two ways. Provide the stack and user ID as headers, and the MCP server creates the streaming session for you. This suits statically configured MCP clients, because they can hold a fixed pair of headers. However, they cannot generate a streaming URL or replace one when it expires. Alternatively, generate a streaming URL yourself and pass it as a header. Use this approach when you need control over session creation, such as setting the validity period.

To connect with the stack and user ID, pass the following headers on every request:
+ `x-amzn-agentaccess-workspaces-applications-stack`. The stack name or ARN.
+ `x-amzn-agentaccess-workspaces-applications-user-id`. The user ID for the session.

**Note**  
The `x-amzn-agentaccess-workspaces-applications-user-id` header is optional. If you omit it, the MCP server derives the user identity from the authenticated session. It uses the AWS `SourceIdentity` when one is present, and the caller's IAM principal otherwise. `SourceIdentity` preserves a user's original corporate identity when they assume an IAM role. This holds even when roles are chained through an external identity provider (IdP).

```
from mcp_proxy_for_aws import aws_iam_streamablehttp_client

# Connect to the MCP server with the stack and user ID
async with aws_iam_streamablehttp_client(
    endpoint="https://agentaccess-mcp.{{region}}.api.aws/mcp",
    aws_service="agentaccess-mcp",
    aws_region="{{region}}",
    headers={
        "x-amzn-agentaccess-workspaces-applications-stack": "{{stack-name-or-arn}}",
        "x-amzn-agentaccess-workspaces-applications-user-id": "{{user-id}}",
    },
) as (read, write, _):
    ...
```

To connect with a streaming URL instead, generate one using the `CreateStreamingURL` API and pass it as the `x-amzn-agentaccess-streaming-session-url` header on every request. No agent-specific parameters are required. The stack's agent access configuration determines the agent behavior.

```
import boto3
from mcp_proxy_for_aws import aws_iam_streamablehttp_client

# Generate streaming URL
appstream = boto3.client("appstream", region_name="{{region}}")
response = appstream.create_streaming_url(
    StackName="{{stack-name}}",
    FleetName="{{fleet-name}}",
    UserId="{{user-id}}",
)
streaming_url = response["StreamingURL"]

# Connect to MCP server
async with aws_iam_streamablehttp_client(
    endpoint="https://agentaccess-mcp.{{region}}.api.aws/mcp",
    aws_service="agentaccess-mcp",
    aws_region="{{region}}",
    headers={
        "x-amzn-agentaccess-streaming-session-url": streaming_url,
    },
) as (read, write, _):
    ...
```

For more information about the CreateStreamingURL API, see [CreateStreamingURL](https://docs.aws.amazon.com/appstream2/latest/APIReference/API_CreateStreamingURL.html) in the *Amazon AppStream 2.0 API Reference*.

### Connecting with domain-joined fleets
<a name="agent-access-mcp-server-connect-dj"></a>

When agents access domain-joined streaming instances, the connection must be federated through a Security Assertion Markup Language (SAML) provider. This requirement applies to both traditional and agent sessions. For agent sessions, [Certificate-Based Authentication](certificate-based-authentication.md) is required.

**Note**  
Domain join is supported on Windows only.

Because domain-joined streaming instances require access through SAML, your MCP client must provide a signed SAML assertion instead of a streaming URL. Encoded SAML assertions exceed HTTP header size limits. To stay within those limits, use the `metadata` field in `mcp-proxy-for-aws`:

```
from mcp_proxy_for_aws import aws_iam_streamablehttp_client

# saml_response: your signed, base64-encoded SAML assertion
# stack_arn: the ARN of the AppStream stack for the AD user

async with aws_iam_streamablehttp_client(
    endpoint="https://agentaccess-mcp.{{region}}.api.aws/mcp",
    aws_service="agentaccess-mcp",
    aws_region="{{region}}",
    metadata={
        "saml_response": saml_response,
        "stack_arn": stack_arn,
    },
) as (read, write, _):
    ...
```

**Note**  
The `metadata` parameter was added in `mcp-proxy-for-aws` version 1.6.1. Earlier versions cannot inject the `_meta` field without additional development. To upgrade, run `pip install -U mcp-proxy-for-aws`.

For more information about setting up SAML federation with WorkSpaces Applications, see [Setting up SAML](https://docs.aws.amazon.com/appstream2/latest/developerguide/active-directory-overview.html) in the *Amazon WorkSpaces Applications Administration Guide*. For more information and a complete working example, see the [sample-code-for-workspaces-agent-access](https://github.com/aws-samples/sample-code-for-workspaces-agent-access/tree/main) repository in AWS Samples on GitHub.

## Compatible frameworks
<a name="agent-access-mcp-server-frameworks"></a>

You can connect from any MCP-compatible framework that supports Streamable HTTP and SigV4 signing. For the agents, frameworks, and tools that work with agent access, see [Supported agents, frameworks, and LLMs](agent-access-agents-llms.md).