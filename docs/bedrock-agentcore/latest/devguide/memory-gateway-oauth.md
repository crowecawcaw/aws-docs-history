# Authenticate end users to Memory with OAuth

The Amazon Bedrock AgentCore Memory data plane authenticates callers with AWS Signature Version 4 (SigV4) only. When your backend or agent calls Memory on behalf of many users, Memory sees only your backend’s IAM role — it cannot verify or enforce which end user a given request is for. Keeping one user’s data separate from another’s depends entirely on your application code setting the correct `actorId` and namespace on each request; nothing at the Memory layer prevents a request handling User A from reading User B’s data.

By fronting Memory with an [AgentCore Gateway](memory-gateway-connector.md "memory-gateway-connector.md") configured for OAuth (`CUSTOM_JWT`) inbound authentication, you add OAuth support that Memory does not have on its own. The caller presents the end user’s JWT with the request, the gateway validates it, and access-control policies enforce isolation based on the token’s claims — at the infrastructure layer, independent of your application logic. The gateway then calls Memory under its gateway execution role, acting as a bridge between the OAuth-authenticated caller and Memory’s IAM-authenticated data plane.

###### Note

This page builds on the AgentCore Memory connector. Set up a gateway with a Memory connector target first. For more information, see [Access AgentCore Memory through a gateway](memory-gateway-connector.md "memory-gateway-connector.md").

## How the gateway bridges OAuth to Memory

When a gateway uses `CUSTOM_JWT` inbound authentication in front of a Memory connector target:

1. The caller sends a request to the gateway with a JWT bearer token issued by your OpenID Connect provider. Depending on your application, the token can represent an end user or the agent itself, and can carry end-user information in its claims.
2. The gateway validates the token against the provider you configured, and the token’s claims (such as `sub` and `client_id`) become available to the gateway’s access-control policies as principal tags.
3. If a policy allows the request, the gateway forwards it to the Memory data plane under its gateway execution role (the `GATEWAY_IAM_ROLE` outbound credential mode).

###### Tip

In a typical chatbot or agent architecture, the end user does not call Memory directly. Your agent or backend service is the HTTP caller, and it passes the end user’s JWT along with each Memory request — the token "travels with" the request. The gateway authenticates that token and evaluates policies against its claims, so access is enforced for the end user _the token represents_, even though the agent is the entity making the call.

This is why fine-grained access control matters: with it, you can ensure a request reaches only the Memory data that belongs to the authenticated end user carried in the token, rather than trusting the agent to set the correct `actorId` and namespace itself.

With an agent application, your end users can sign in through a standard OAuth identity provider — for example, Amazon Cognito or any OpenID Connect provider — and you can enforce per-user Memory isolation based on the authenticated end user’s identity. Your application does not distribute AWS credentials to end users, and Memory does not need to natively understand OAuth.

Configuring the `CUSTOM_JWT` authorizer (the OpenID Connect discovery URL, allowed audience and clients, and scopes) is a standard gateway inbound-authorization task and is not specific to Memory. For the authorizer configuration, see [Create an AgentCore gateway](gateway-create.md "gateway-create.md"). For how JWT claims map to the `AgentCore::OAuthUser` principal and its tags, see [Core concepts](policy-core-concepts.md "policy-core-concepts.md").

###### Note

OAuth (`CUSTOM_JWT`) inbound is compatible only with the `GATEWAY_IAM_ROLE` outbound credential mode. The `CALLER_IAM_CREDENTIALS` mode forwards the caller’s IAM identity, which does not exist for a JWT-authenticated caller, so it is rejected at target creation. For the full compatibility matrix, see [Inbound and outbound authentication modes](memory-gateway-connector.md#memory-gateway-connector-auth-modes "memory-gateway-connector.md#memory-gateway-connector-auth-modes").

## Enforce per-user access to Memory

Authenticating callers with OAuth is what makes identity-based authorization possible, but authentication alone does not limit what a caller can do. Any request with a valid token can still reach every actor, session, and namespace in the Memory resource. To ensure each request can only access Memory data belonging to the authenticated end user — whose identity is carried in the JWT — add access-control policies with fine-grained access control. For how to write those policies, see [Fine-grained access control for Memory](memory-gateway-fgac.md "memory-gateway-fgac.md").
