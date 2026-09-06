

# AGENTSEC03-BP02 Separate agent and human user permission
<a name="agentsec03-bp02"></a>

 Identity propagation alone isn't enough when agents act on behalf of users. Distinct agent service identities, with hard trust boundaries helping prevent assumption of human-designated roles, keep audit attribution unambiguous and stop a misconfigured agent from escalating into a human identity space. 

 **Desired outcome:** 
+  Agent actions and human actions are distinguishable in audit logs, with separate identities that help prevent agents from inheriting or assuming human user permissions. 
+  Dedicated agent service identities are scoped to only the permissions required for automated operations, and audit logs attribute every action unambiguously to either an agent or a human actor. 
+  Trust policies help prevent agents from assuming human-designated identities, with organization-level guardrails providing a secondary boundary in multi-account environments. 

 **Common anti-patterns:** 
+  Reusing human user IAM credentials or roles for agent authentication, making it impossible to distinguish agent actions from human actions in audit logs. 
+  Allowing agents to assume human IAM roles through role chaining, enabling access to resources that should be restricted to human users and creating a privilege-escalation path. 
+  Using a single shared service account for multiple agents, reducing the risk of attribution of specific actions to individual agents and complicating incident response. 
+  Relying only on agent-level IAM policies without role trust policy restrictions or multi-account guardrails, leaving open the assumption path where an affected agent role could still assume a human role. 

 **Benefits of establishing this best practice:** 
+  Separate identities produce unambiguous audit attribution that clearly distinguishes agent actions from human actions. 
+  Trust policies refuse assumption by agent principals, with optional organization-level guardrails adding a multi-account ceiling. 
+  Consistent agent identity tagging and naming conventions enable filtering and analysis of agent activity patterns during incident investigations. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance"></a>

 Two separations matter here and they are often collapsed in practice. Identity separation means the agent operates under a service identity distinct from any human identity, whether that human is an operator managing AWS resources or an application user interacting with the agent's service. Permission separation means the agent's identity carries only the permissions it needs for its tasks and never inherits the permissions of human identities. These apply to both patterns (agents acting autonomously and agents acting on behalf of a user), but the way user context flows through a call differs: autonomous agents operate under their service identity alone, while agents acting on behalf of a user carry that user's context forward as token claims without the agent ever assuming the user's credentials. Human operator identities (which authenticate through IAM Identity Center for AWS access) and application user identities (which authenticate through a separate customer-facing identity provider and have no AWS identity at all) are themselves distinct layers. 

 For agents that operate on AWS, create dedicated IAM roles for each agent type as the agent's service identity, with a naming convention (for example, agent-role-<agent-name>) that distinguishes them from human operator roles, and apply PrincipalType: Agent as a consistent tag. Principal tags surface in AWS CloudTrail events primarily for management-plane API calls made with session tags. For service-specific events that don't surface principal tags, filter by the agent role ARN naming convention as the primary signal and treat the tag as a secondary filter. Use AWS IAM Identity Center for all human operator access and migrate any human operators still using account-specific IAM users off those identities. Application users are typically outside this migration, they authenticate through the application's own identity provider, and their identity flows into agent calls as token claims. Configure Service Control Policies (SCPs) in AWS Organizations that explicitly deny agents (identified by tag) from assuming roles in the human operator identity boundary, for example denying sts:AssumeRole for any principal tagged as an agent attempting to assume roles tagged as human-operator. 

 Amazon Bedrock AgentCore introduces two identity constructs that support this separation. The AgentCore Runtime **execution role** is a regular IAM role assumed by the Runtime process to reach AWS services the agent depends on (model invocations, tool calls to AWS APIs, memory reads and writes). The AgentCore **Workload Identity** is an agent-specific identity registered in the AgentCore Identity directory, distinct from any IAM role, and used to issue and verify agent-scoped tokens and vault third-party tokens obtained on behalf of users. When an agent acts on behalf of an application user, it calls GetWorkloadAccessTokenForJWT with the user's access token from the application's identity provider. [Amazon Bedrock AgentCore Identity](https://docs.aws.amazon.com/bedrock/latest/userguide/agentcore-identity.html) verifies the user token and returns an agent-specific workload access token that embeds the user context as claims, so the call chain carries both "who the agent is" and "who the user is" without the agent ever assuming the user's credentials or an IAM role on the user's behalf. 

 For agents that need to reach third-party OAuth resources on behalf of users, AgentCore Identity orchestrates the authorization code grant flow and secures the resulting access tokens in a token vault scoped per agent identity and per user. One agent can't retrieve tokens obtained for a different user, and as long as the third-party access token remains valid the agent can retrieve it from the vault without requiring the user to re-authenticate. 

 Amazon Cognito provides an alternative for organizations already standardized on Cognito user pools. The same principle (the agent carries both its own identity and the user's context as token claims) can be implemented outside AgentCore Identity. The pattern described in [Empower AI agents with user context using Amazon Cognito](https://aws.amazon.com/blogs/security/empower-ai-agents-with-user-context-using-amazon-cognito/) uses [Amazon Cognito](https://aws.amazon.com/cognito/) user pools: the agent authenticates through the client credentials flow while passing the user's token as additional context through the aws\_client\_metadata request parameter, and a [pre-token-generation Lambda trigger](https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-lambda-pre-token-generation.html) verifies the user token and injects an onBehalfOf claim into the agent's access token before issuance. The resulting JWT identifies the agent in its sub claim and the user in its onBehalfOf claim, producing a single token that downstream authorization layers can evaluate. This is a custom extension built on Cognito trigger hooks, not a native Cognito feature, and it complements the AgentCore pattern rather than replacing it. For authorization on top of the resulting token, resource servers can evaluate claims directly, or externalize policy to a service such as [Amazon Verified Permissions](https://aws.amazon.com/verified-permissions/) using Cedar (a choice orthogonal to whether you use AgentCore Identity or the Cognito pattern). 

 When an agent invokes a tool through AgentCore Gateway, the gateway operates under its own execution role (one per gateway) and the outbound authentication applied to the target depends on the target type (see the [AgentCore Gateway outbound auth reference](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway-outbound-auth.html) for details). User context propagates through the gateway so downstream services can enforce user-level authorization, and the gateway never substitutes an IAM identity for the user or re-authenticates as the user against downstream services. 

 Configure [CloudTrail with advanced event selectors](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/logging-data-events-with-cloudtrail.html) to capture agent API calls, including data events for agent-invoked services where visibility beyond management-plane events matters. Enable AgentCore data events so operations against AgentCore Memory, Gateway, and Runtime are logged alongside management-plane events. Amazon CloudWatch Logs Insights queries filtered by agent role ARN patterns give dedicated agent activity dashboards. For SQL-based analysis over time, deliver CloudTrail logs to Amazon S3 and query them with Amazon Athena (see AGENTSEC05-BP01). 

 For multi-agent systems where a parent agent directly assumes a sub-agent's IAM role (for example, calling sts:AssumeRole before invoking the sub-agent in the same account), use role session names that include the parent agent's identifier so the chain is visible in CloudTrail. For A2A communication that routes through AgentCore Runtime, each agent runs under its own independent execution role session and there is no IAM role chain. Use correlation identifiers propagated through the A2A message (see AGENTSEC05-BP02) to reconstruct the agent-to-agent call graph. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Audit and rename agent roles:** Identify any IAM roles shared between agents and human users, and create dedicated agent-specific roles with a consistent naming convention (for example, agent-role-<agent-name>). 

1.  **Tag agent roles consistently:** Apply PrincipalType: Agent and AgentName: <name> tags to every agent IAM role for filtering and monitoring. 

1.  **Move human operators to IAM Identity Center:** Configure AWS IAM Identity Center for all human operator access and migrate any operators still on account-specific IAM users. 

1.  **Enforce the agent-to-human boundary through SCPs:** Deploy Service Control Policies in AWS Organizations that deny agents (identified by tag) from assuming human-operator roles, creating a hard boundary between the identity spaces. 

1.  **Register Workload Identities for on-behalf-of flows:** Register agent Workload Identities in [Amazon Bedrock AgentCore Identity](https://docs.aws.amazon.com/bedrock/latest/userguide/agentcore-identity.html) for agents that act on behalf of users, and use GetWorkloadAccessTokenForJWT to create agent-scoped tokens that embed user context as claims for downstream authorization. 

1.  **Enable CloudTrail with AgentCore data events:** Turn on advanced event selectors including AgentCore data events, and build Amazon CloudWatch Logs Insights queries filtered by agent role ARN patterns for dedicated agent activity dashboards. 

1.  **Analyze with Athena over time:** Deliver AWS CloudTrail logs to Amazon S3 and use Amazon Athena for SQL-based analysis of agent compared to human activity patterns over time for compliance reporting and long-term trend analysis. 

1.  **Name sessions for attribution:** Implement role session naming conventions that include agent identifiers (and parent agent identifiers for delegation chains) for clear attribution in multi-agent systems. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [AGENTSEC03-BP01 Implement strong authentication for agent identities](agentsec03-bp01.html) 
+  [AGENTSEC03-BP03 Implement least privilege with dynamic boundaries](agentsec03-bp03.html) 
+  [AGENTSEC05-BP01 Implement comprehensive logging and decision artifact storage](agentsec05-bp01.html) 

 **Related documents:** 
+  [AWS CloudTrail best practices](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/best-practices-security.html) 
+  [AWS IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/what-is.html) 
+  [Securing AI agents with Amazon Bedrock AgentCore Identity](https://aws.amazon.com/blogs/security/securing-ai-agents-with-amazon-bedrock-agentcore-identity/) 
+  [Empower AI agents with user context using Amazon Cognito](https://aws.amazon.com/blogs/security/empower-ai-agents-with-user-context-using-amazon-cognito/) 
+  [Amazon Bedrock AgentCore Identity documentation](https://docs.aws.amazon.com/bedrock/latest/userguide/agentcore-identity.html) 
+  [AgentCore Identity supported authentication patterns](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/common-use-cases.html) 

 **Related services:** 
+  [AWS Identity and Access Management](https://aws.amazon.com/iam/) 
+  [AWS IAM Identity Center](https://aws.amazon.com/iam/identity-center/) 
+  [AWS CloudTrail](https://aws.amazon.com/cloudtrail/) 
+  [AWS Organizations](https://aws.amazon.com/organizations/) 
+  [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) 
+  [Amazon Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/) 
+  [Amazon Cognito](https://aws.amazon.com/cognito/) 
+  [Amazon Verified Permissions](https://aws.amazon.com/verified-permissions/) 