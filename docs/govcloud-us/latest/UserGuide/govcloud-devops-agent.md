

# AWS DevOps Agent in AWS GovCloud (US)

 AWS DevOps Agent is an AI-powered, always-available agent that spans release management and production operations, from reviewing release readiness and release testing to investigating and preventing operational issues across AWS, multicloud, and on-premises environments.

The agent learns your resources and their relationships, works with your observability tools, code repositories, and CI/CD pipelines, and correlates telemetry, code, and deployment data to identify root causes and propose mitigations. You interact with the agent through the AWS DevOps Agent web app, the API and CLI, and the third-party tools that you connect to an Agent Space.

**Important**  
When you connect a third-party provider, remote MCP server, or remote agent to an Agent Space, data from your associated accounts may leave the AWS GovCloud (US) Regions. Do not connect these to an Agent Space whose associated accounts contain export-controlled data, unless the provider meets your export compliance requirements.

## Region availability
<a name="region-availability"></a>

 AWS DevOps Agent is available in the following AWS GovCloud (US) Regions:
+  AWS GovCloud (US-West) 

## How AWS DevOps Agent differs
<a name="feature-diffs"></a>
+ You can associate only AWS GovCloud (US) accounts with an Agent Space in the AWS GovCloud (US) Regions. Accounts in the standard AWS partition cannot be associated with an AWS GovCloud (US) Agent Space, and AWS GovCloud (US) accounts cannot be associated with an Agent Space in a standard AWS Region.
+ To associate another AWS GovCloud (US) account with an Agent Space, the caller must have the `iam:PassRole` permission for the role being associated, with the `iam:PassedToService` condition key set to `aidevops.amazonaws.com`.
+ An Agent Space in AWS GovCloud (US-West) can discover and monitor resources in both AWS GovCloud (US-West) and AWS GovCloud (US-East).
+ Amazon Resource Names (ARNs) for AWS DevOps Agent resources use the pattern `arn:aws-us-gov:aidevops:us-gov-west-1:account-id:agentspace/agent-space-id `.
+ The endpoint that third-party providers such as GitHub or GitLab use to deliver webhook events to AWS DevOps Agent is `https://us-gov.event-ai.global.api.aws`.
+  AWS DevOps Agent uses only foundation models that are available in Amazon Bedrock in the AWS GovCloud (US) Regions. Some agent capabilities use different Anthropic Claude model versions than in other AWS Regions. Cross-Region inference is not used.
+ Interface VPC endpoints (AWS PrivateLink) for the AWS DevOps Agent API endpoints are not available. Use the public Regional endpoints.
+ Topology enrichment for Amazon EKS clusters is not available. The topology shows an EKS cluster as a single node and does not include Kubernetes namespaces, pods, or their relationships.
+ Sandbox (preview) is not available.
+ Release management (release readiness review and release testing) (preview) is not available.
+ Signing in to the AWS DevOps Agent web app with AWS IAM Identity Center or with an external identity provider (for example, Okta or Microsoft Entra ID) is not available. To sign in to the web app, use the IAM authentication link from the AWS GovCloud (US) console.
+ Persistent cross-session memory for the chat assistant is not available.
+ Private connections to third-party or self-hosted tool providers over AWS PrivateLink are not available. Connections to third-party providers use public endpoints.
+  AWS CloudTrail data events for AWS DevOps Agent are not available. CloudTrail management events are available.

## Documentation
<a name="documentation"></a>
+  [AWS DevOps Agent documentation](https://docs.aws.amazon.com/devopsagent/latest/userguide/) 

## Export-controlled content
<a name="itar-boundary"></a>

For AWS Services architected within the AWS GovCloud (US) Regions, the following list explains how certain components of data may leave the AWS GovCloud (US) Regions in the normal course of the service offerings. The list can be used as a guide to help meet applicable customer compliance obligations. Data not included in the following list remains within the AWS GovCloud (US) Regions.
+  AWS DevOps Agent metadata is not permitted to contain export-controlled data. This metadata includes all of the configuration data that you enter when creating and maintaining Agent Spaces, custom agents, skills, and agent instructions.
+ Do not enter export-controlled data in the following fields:
  + Agent Space name
  + Agent Space description
  + Custom agent name
  + Custom agent instructions
  + Skill name
  + Agent instruction name
+ When you connect a third-party provider (for example, a source-code, CI/CD, observability, or incident-management provider), the agent can send investigation context, telemetry queries, and tool requests to that provider’s endpoints when it uses the provider. These requests can include data from your associated accounts. Third-party providers might not offer an AWS GovCloud (US) or FedRAMP-authorized variant, and their endpoints may be located outside the AWS GovCloud (US) Regions. You are responsible for confirming that each provider that you connect meets your compliance requirements.
+ When you connect a remote MCP server or remote agent, the agent can send tool invocation payloads to the server URL that you specify when it uses that server or agent. That URL may be located outside the AWS GovCloud (US) Regions.
+ When you connect a third-party provider, remote MCP server, or remote agent to an Agent Space, the agent can include content from your chat and from your Agent Space configuration, such as the Agent Space name, in the requests that it sends to that destination. If the destination’s endpoints are located outside the AWS GovCloud (US) Regions, do not enter export-controlled data in the chat or in the Agent Space configuration.