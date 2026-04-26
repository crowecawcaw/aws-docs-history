# Security Hub CSPM controls for Amazon Bedrock AgentCore

These AWS Security Hub CSPM controls evaluate the Amazon Bedrock AgentCore service and resources. The controls might
not be available in all AWS Regions. For more information, see [Availability of controls by Region](securityhub-regions.md#securityhub-regions-control-support "securityhub-regions.md#securityhub-regions-control-support").

## [BedrockAgentCore.1] Bedrock AgentCore runtimes should be configured with VPC network mode

**Category:** Protect > Secure access management > Resource not publicly accessible

**Severity:** High

**Resource type:**
`AWS::BedrockAgentCore::Runtime`

**AWS Config rule:**
[bedrockagentcore-runtime-private-network-required](../../../config/latest/developerguide/bedrockagentcore-runtime-private-network-required.md "../../../config/latest/developerguide/bedrockagentcore-runtime-private-network-required.md")

**Schedule type:** Change triggered

**Parameters:** None

This control checks whether an Amazon Bedrock AgentCore runtime is configured with VPC
network mode. The control fails if the runtime has its network mode set to
PUBLIC.

Using public network mode for Amazon Bedrock AgentCore runtimes exposes the runtime
directly to the internet, increasing the attack surface and risk of unauthorized access.
Configuring runtimes with VPC network mode ensures that runtime traffic is confined
within your private network, enabling you to apply network-level security controls such
as security groups, network ACLs, and VPC flow logs.

### Remediation

To remediate this finding, update the non-compliant Bedrock AgentCore runtime and
configure it with VPC network mode. For instructions, see [Configure Amazon
Bedrock AgentCore Runtime and tools for VPC](../../../bedrock-agentcore/latest/devguide/agentcore-vpc.md "../../../bedrock-agentcore/latest/devguide/agentcore-vpc.md") in the _Amazon Bedrock AgentCore Developer Guide_.

## [BedrockAgentCore.2] Bedrock AgentCore Gateways should require authorization for inbound requests

**Category:** Protect > Secure access management

**Severity:** High

**Resource type:**
`AWS::BedrockAgentCore::Gateway`

**AWS Config rule:**
[bedrockagentcore-gateway-authorizer-enabled](../../../config/latest/developerguide/bedrockagentcore-gateway-authorizer-enabled.md "../../../config/latest/developerguide/bedrockagentcore-gateway-authorizer-enabled.md")

**Schedule type:** Change triggered

**Parameters:** None

This control checks whether an Amazon Bedrock AgentCore Gateway requires authorization
for inbound requests. The control fails if the Bedrock AgentCore Gateway doesn't have
inbound authorization set up.

Configuring authentication on Amazon Bedrock AgentCore gateways ensures that only
authorized clients can send requests to your AI agents. Without an authorizer, any
entity with network access to the gateway endpoint can invoke your agents, potentially
leading to unauthorized data access, resource abuse, or unexpected costs. Inbound
authorization validates users who attempt to access targets through your AgentCore
gateway.

### Remediation

To set up inbound authorization for an Amazon Bedrock AgentCore Gateway, see
[Set up inbound authorization for your gateway](../../../bedrock-agentcore/latest/devguide/gateway-inbound-auth.md#gateway-inbound-auth-none "../../../bedrock-agentcore/latest/devguide/gateway-inbound-auth.md#gateway-inbound-auth-none") in the _Amazon Bedrock AgentCore Developer Guide_.
