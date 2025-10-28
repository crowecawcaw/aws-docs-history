# Get workload access token

Understanding what workload access tokens are, how to obtain them, and the
security aspects of working with them is essential for building secure agent
applications. This section covers the key concepts and implementation patterns you
need to know.

###### Topics

- [What is a workload access
  token?](#workload-access-token-overview "#workload-access-token-overview")
- [How Runtime and Gateway
  automatically obtain tokens](#how-runtime-gateway-obtain-tokens "#how-runtime-gateway-obtain-tokens")
- [How to manually retrieve
  workload access tokens](#manual-token-retrieval-patterns "#manual-token-retrieval-patterns")
- [Security controls for
  GetWorkloadAccessTokenForUserId API](#security-controls-getuserid-api "#security-controls-getuserid-api")

## What is a workload access

token?

A workload access token is an AWS-signed opaque access token that enables
agents to access first-party AgentCore services, such as outbound credential
providers. Runtime automatically delivers workload access tokens to agent
execution instances as payload headers, eliminating the need for manual token
management in most scenarios.

**Key characteristics**

- **First-party services only** –
  Workload access tokens are exclusively for accessing AWS first-party
  AgentCore services and cannot be used for external services
- **Automatic delivery** – Runtime
  and Gateway automatically provide these tokens to agents during
  execution
- **Security by design** –
  Runtime-managed agent identities cannot retrieve workload access tokens
  directly, preventing token extraction and misuse
- **User and agent identity binding**
  – Tokens contain both user identity and agent identity
  information for secure credential access

## How Runtime and Gateway

automatically obtain tokens

When an agent is invoked through AgentCore Runtime or Gateway with inbound
authentication, the service automatically handles workload access token
generation:

1. Runtime validates the inbound identity provider OAuth token (issuer,
   signature)
2. Runtime extracts issuer and sub claims from the OAuth token
   representing user identity
3. Runtime fetches the associated workload identity of the agent
4. Runtime invokes `GetWorkloadAccessTokenForJWT` with both
   user identity and agent workload identity
5. Runtime passes the workload access token to agent code as part of the
   invocation payload header

This automatic process ensures agents receive properly scoped tokens without
manual intervention.

## How to manually retrieve

workload access tokens

There are two patterns to use to retrieve the workload access token depending
on how you are able to identify the end user of the agent:

- If the agent’s caller has a JWT identifying the end user, request a
  workload access token based on the agent’s identity and the end-user
  JWT. When you provide a JWT, AgentCore Identity will validate the JWT to ensure
  it is correctly signed and unexpired, and it will use its “iss” and
  “sub” claims to uniquely identify the user. Credentials stored by the
  agent on behalf of the user will be associated with this information,
  and future retrievals by the agent will require a valid workload access
  token containing the same information.
- If the agent’s caller does not have a JWT identifying the end user,
  request a workload access token based on the agent’s identity and a
  unique string identifying the user.

The examples below illustrate using the AgentCore SDK to retrieve a workload
access token using these two methods:

```
from bedrock_agentcore.services.identity import IdentityClient

identity_client= IdentityClient("us-east-1")# Obtain a token using the IAM identity of the caller to authenticate the agent and providing a JWT containing the identity of the end user.
# This is the recommended pattern whenever a JWT is available for the user.
workload_access_token= identity_client.get_workload_access_token(workload_name= "my-demo-agent", user_token= "insert-jwt-here")# Obtain a token using the IAM identity of the caller to authenticate the agent and providing a string representing the identity of the end user.
# Use this pattern when a JWT is not available for the user.
workload_access_token= identity_client.get_workload_access_token(workload_name= "my-demo-agent", user_id= "insert-user-name-or-identifier")
```

## Security controls for

`GetWorkloadAccessTokenForUserId` API

The `GetWorkloadAccessTokenForUserId` API implements several
security controls to prevent unauthorized access:

- **Workload identity validation** –
  The API verifies that the requesting identity has permission to act on
  behalf of the specified workload identity
- **Service-managed identity restriction**
  – Runtime-managed and Gateway-managed workload identities cannot
  retrieve tokens directly. This prevents agents from extracting tokens
  for misuse
- **IAM permission requirements**
  – Callers must have appropriate IAM permissions including
  `GetWorkloadAccessToken`,
  `GetWorkloadAccessTokenForUserId`, and
  `GetWorkloadAccessTokenForJWT`
- **Token scoping** – Tokens are
  scoped to the specific user-agent pair, ensuring credentials stored
  under one user cannot be accessed by another
- **User ID partitioning for multiple identity
  providers** – When using multiple identity providers,
  partition your user IDs using the pattern
  ``provider_id`+`user_id``
  to prevent user collisions between different providers. For example, use
  `cognito+user123` and `auth0+user123` to
  distinguish users with the same identifier across different identity
  providers

If you encounter the error "WorkloadIdentity is linked to a service and cannot
retrieve an access token by the caller," this indicates the workload identity is
managed by Runtime or Gateway and cannot retrieve tokens directly. This
restriction helps maintain security boundaries and prevents unauthorized token
access.

For additional security controls, you can implement fine-grained access
policies to restrict which workload identities can access specific credential
providers. For more information, see [Scope down access to credential
providers by workload identity](scope-credential-provider-access.md "scope-credential-provider-access.md").
