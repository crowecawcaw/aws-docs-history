

# Agent identity

When an AI agent works in a streaming session on behalf of a person, you need to know two things: which agent acted, and which user it acted for. With *agent identity*, you use the identity provider (IdP) that you already use for your workforce, such as Microsoft Entra ID or Okta, to answer both questions. Each agent has its own identity in your IdP, unique to that agent and separate from the identity of any user. Your IdP signs the identities of the agent and of the user, so both are cryptographically verified rather than reported by the agent itself. AWS carries both identities through to the Model Context Protocol (MCP) server that controls the streaming session, and to the records in AWS CloudTrail.

With agent identity, you can do the following:
+ **Attribute every action**. CloudTrail records which agent acted and which user it acted for, so that you can answer audit questions without having to correlate logs from different systems.
+ **Reuse your IdP controls**. The user signs in through your IdP, so the multi-factor authentication, conditional access, and consent policies that you already enforce also apply when an agent acts for the user.
+ **Control access in IAM policies**. Both identities arrive as IAM session tags, so you can write policies that require them, or that allow only specific agents to reach specific stacks.
+ **Avoid long-lived credentials**. The agent receives temporary AWS credentials for each session. It doesn't store a password or an AWS access key.

## How agent identity works
<a name="agent-access-agent-identity-how-it-works"></a>

Agent identity builds on two standard mechanisms: the OAuth 2.0 on-behalf-of (OBO) token exchange that your IdP supports, and IAM web identity federation. It works as follows:

1. The user signs in to your IdP through the agent, and the agent receives a token for that user.

1. The agent exchanges the user's token at your IdP for a new access token that represents the agent acting on behalf of the user. This is the OBO exchange. Your IdP adds claims to the new token that identify both the agent and the user.

1. The agent calls the AWS Security Token Service (AWS STS) `AssumeRoleWithWebIdentity` operation with the access token. AWS STS validates the token against the IAM OpenID Connect (OIDC) identity provider that you registered, and returns temporary credentials for an IAM role. The claims in the token become session tags and the source identity of the role session.

1. The agent signs its requests to the MCP server with those credentials. The MCP server uses the source identity as the user of the streaming session.

1. CloudTrail records the role assumption with both identities. It also records the user on the MCP `initialize` request and, if you log data events, on every tool call that follows. Tool calls are data events, which CloudTrail doesn't log by default. For more information, see [Monitoring](agent-access-mcp-server-monitoring.md) and [Logging data events](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/logging-data-events-with-cloudtrail.html) in the *CloudTrail User Guide*.

The agent doesn't supply the identity values itself. They come only from the token that your IdP signed, which is why you can rely on them for authorization and audit.

## Identity attributes
<a name="agent-access-agent-identity-attributes"></a>

Configure your IdP to add the following claims to the access token that it issues in the OBO exchange. Session tag keys are case sensitive, so use the same spelling in your IdP claims and in your IAM policies.


**Identity claims for agent identity**  

| Session tag or claim | Value | Use | 
| --- | --- | --- | 
| AgentAccessAgentId | The agent's immutable object ID in your IdP | Identifies the agent in policies and audit records | 
| AgentAccessAgentName (optional) | The agent's display name | Display only. Display names can change, so don't use this tag in policies. | 
| AgentAccessUserId | The user's short name | Identifies the user that the agent acts for | 
| Source identity | The user's short name | Becomes the user of the streaming session, and appears on every later CloudTrail event | 

Session tags and the source identity do different jobs, so you need both:
+ **Session tags** are available to IAM policy evaluation for the whole role session, and CloudTrail records them on the `AssumeRoleWithWebIdentity` event. Later events don't repeat them.
+ **The source identity** can't be changed after the session is created, and CloudTrail records it on every event that the session produces, including tool calls when you log data events.

For more information, see [Pass session tags in AWS STS](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_session-tags.html) and [Monitor and control actions taken with assumed roles](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp_control-access_monitor.html) in the *IAM User Guide*.

## Choose a setup for your fleet type
<a name="agent-access-agent-identity-choose"></a>

The setup depends on whether your fleet is joined to an Active Directory domain:
+ **Non-domain-joined fleets**. The agent runs one OBO exchange and calls `AssumeRoleWithWebIdentity`. The MCP server creates the streaming session for the user named by the source identity. For more information, see [Agent identity for non-domain-joined fleets](agent-access-agent-identity-ndj.md).
+ **Domain-joined fleets**. Windows must log the user on to the domain, so the agent also obtains a SAML assertion from your IdP. The assertion carries the user's Active Directory attributes, and certificate-based authentication uses them to log on without a password. For more information, see [Agent identity for domain-joined fleets](agent-access-agent-identity-dj.md).

The examples in these topics use Microsoft Entra ID. You can use any IdP that supports OIDC, an OBO or token exchange grant, and custom claims in access tokens, such as Okta. For domain-joined fleets, your IdP must also be able to return a SAML assertion from the OBO or token exchange.

## Security considerations
<a name="agent-access-agent-identity-security"></a>
+ **Protect your IdP configuration**. AWS trusts the claims that your IdP signs, and can't check that your claim mapping is correct. Treat the claim mapping and the IAM OIDC identity provider as security-critical configuration. Restrict who can change them, and review changes with the same care as a role trust policy.
+ **Scope each role to specific stacks**. Grant the WorkSpaces Applications permissions in the role only on the stacks that the agent needs. This is where you authorize the agent, as distinct from the user it acts for. Use a separate role for each agent that needs different access.
+ **Require both identities**. Use `Null` conditions in the role trust policy so that a token that is missing either identity can't be used to assume the role. Put the conditions in a statement that doesn't include `sts:SetSourceIdentity`. Otherwise, the role assumption fails. For an example, see [Step 2: Configure IAM](agent-access-agent-identity-ndj.md#agent-access-agent-identity-ndj-iam).
+ **Use a signed client assertion**. Have the agent authenticate to your IdP with a private key JWT instead of a client secret. If you keep the private key in AWS KMS, the agent never holds the key itself.
+ **Revoke access at any time**. Disabling the user in your IdP, or changing the role trust policy, prevents new sessions. It doesn't affect temporary credentials that AWS STS already issued, which stay valid until they expire at the end of the role session. To stop an agent that already has credentials, remove permissions from the role or revoke the role's active sessions. After the credentials expire, the agent needs a new OBO exchange to continue. For more information, see [Revoke IAM role temporary security credentials](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_revoke-sessions.html) in the *IAM User Guide*.