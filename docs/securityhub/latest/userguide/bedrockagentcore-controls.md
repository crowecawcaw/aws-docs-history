

# Security Hub CSPM controls for Amazon Bedrock AgentCore
<a name="bedrockagentcore-controls"></a>

These AWS Security Hub CSPM controls evaluate the Amazon Bedrock AgentCore service and resources. The controls might not be available in all AWS Regions. For more information, see [Availability of controls by Region](securityhub-regions.md#securityhub-regions-control-support).

## [BedrockAgentCore.1] Bedrock AgentCore runtimes should be configured with VPC network mode
<a name="bedrockagentcore-1"></a>

**Category:** Protect > Secure access management > Resource not publicly accessible

**Severity:** High

**Resource type:** `AWS::BedrockAgentCore::Runtime`

**AWS Config rule:** [bedrockagentcore-runtime-private-network-required](https://docs.aws.amazon.com/config/latest/developerguide/bedrockagentcore-runtime-private-network-required.html)

**Schedule type:** Change triggered

**Parameters:** None

This control checks whether an Amazon Bedrock AgentCore runtime is configured with VPC network mode. The control fails if the runtime has its network mode set to PUBLIC.

Using public network mode for Amazon Bedrock AgentCore runtimes exposes the runtime directly to the internet, increasing the attack surface and risk of unauthorized access. Configuring runtimes with VPC network mode ensures that runtime traffic is confined within your private network, enabling you to apply network-level security controls such as security groups, network ACLs, and VPC flow logs.

### Remediation
<a name="bedrockagentcore-1-remediation"></a>

To remediate this finding, update the non-compliant Bedrock AgentCore runtime and configure it with VPC network mode. For instructions, see [Configure Amazon Bedrock AgentCore Runtime and tools for VPC](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/agentcore-vpc.html) in the *Amazon Bedrock AgentCore Developer Guide*.

## [BedrockAgentCore.2] Bedrock AgentCore Gateways should require authorization for inbound requests
<a name="bedrockagentcore-2"></a>

**Category:** Protect > Secure access management

**Severity:** High

**Resource type:** `AWS::BedrockAgentCore::Gateway`

**AWS Config rule:** [bedrockagentcore-gateway-authorizer-enabled](https://docs.aws.amazon.com/config/latest/developerguide/bedrockagentcore-gateway-authorizer-enabled.html)

**Schedule type:** Change triggered

**Parameters:** None

This control checks whether an Amazon Bedrock AgentCore Gateway requires authorization for inbound requests. The control fails if the Bedrock AgentCore Gateway doesn't have inbound authorization set up.

Configuring authentication on Amazon Bedrock AgentCore gateways ensures that only authorized clients can send requests to your AI agents. Without an authorizer, any entity with network access to the gateway endpoint can invoke your agents, potentially leading to unauthorized data access, resource abuse, or unexpected costs. Inbound authorization validates users who attempt to access targets through your AgentCore gateway.

### Remediation
<a name="bedrockagentcore-2-remediation"></a>

To set up inbound authorization for an Amazon Bedrock AgentCore Gateway, see [Set up inbound authorization for your gateway](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway-inbound-auth.html#gateway-inbound-auth-none) in the *Amazon Bedrock AgentCore Developer Guide*.

## [BedrockAgentCore.3] Bedrock AgentCore Memory should be encrypted with customer managed AWS KMS keys
<a name="bedrockagentcore-3"></a>

**Related requirements:** NIST.800-53.r5 AU-9, NIST.800-53.r5 CA-9(1), NIST.800-53.r5 CM-3(6), NIST.800-53.r5 SC-7(10), NIST.800-53.r5 SC-12(2), NIST.800-53.r5 SC-13, NIST.800-53.r5 SC-28, NIST.800-53.r5 SC-28(1), NIST.800-53.r5 SI-7(6)

**Category:** Protect > Data protection > Encryption of data at rest

**Severity:** Medium

**Resource type:** `AWS::BedrockAgentCore::Memory`

**AWS Config rule:** [bedrock-agentcore-memory-encryption-enabled](https://docs.aws.amazon.com/config/latest/developerguide/bedrock-agentcore-memory-encryption-enabled.html)

**Schedule type:** Change triggered

**Parameters:** None

This control checks whether an Amazon Bedrock AgentCore Memory is encrypted at rest with a customer managed AWS KMS key. The control fails if the Bedrock AgentCore Memory isn't encrypted with a customer managed KMS key.

Using a customer managed KMS key for encryption of Amazon Bedrock AgentCore memory provides enhanced security over the default service managed key. Customer managed KMS keys give you full control over the encryption key lifecycle and access policies. Additionally, all encryption key usage can be logged and monitored through AWS CloudTrail for auditability.

### Remediation
<a name="bedrockagentcore-3-remediation"></a>

To encrypt your Amazon Bedrock AgentCore Memory with a customer managed KMS key, see [Encrypt your Amazon Bedrock AgentCore Memory](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/storage-encryption.html) in the *Amazon Bedrock AgentCore Developer Guide*.

## [BedrockAgentCore.4] Bedrock AgentCore Gateway should be encrypted with customer managed AWS KMS keys
<a name="bedrockagentcore-4"></a>

**Related requirements:** NIST.800-53.r5 AU-9, NIST.800-53.r5 CA-9(1), NIST.800-53.r5 CM-3(6), NIST.800-53.r5 SC-7(10), NIST.800-53.r5 SC-12(2), NIST.800-53.r5 SC-13, NIST.800-53.r5 SC-28, NIST.800-53.r5 SC-28(1), NIST.800-53.r5 SI-7(6)

**Category:** Protect > Data protection > Encryption of data at rest

**Severity:** Medium

**Resource type:** `AWS::BedrockAgentCore::Gateway`

**AWS Config rule:** [bedrockagentcore-gateway-encryption-enabled](https://docs.aws.amazon.com/config/latest/developerguide/bedrockagentcore-gateway-encryption-enabled.html)

**Schedule type:** Change triggered

**Parameters:** None

This control checks whether an Amazon Bedrock AgentCore Gateway is encrypted at rest with a customer managed AWS KMS key. The control fails if the Bedrock AgentCore Gateway isn't encrypted with a customer managed KMS key.

By default, Amazon Bedrock AgentCore encrypts gateway data with AWS managed keys. Using a customer managed KMS key gives you full control over the encryption key lifecycle, including rotation, access policies, and auditing through AWS CloudTrail. This helps meet compliance requirements that mandate customer-controlled encryption for sensitive AI workloads.

### Remediation
<a name="bedrockagentcore-4-remediation"></a>

To encrypt your Bedrock AgentCore Gateway with a customer managed KMS key, see [Encrypt your AgentCore gateway with a customer-managed KMS key](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway-encryption.html) in the *Amazon Bedrock AgentCore Developer Guide*.

## [BedrockAgentCore.5] Bedrock AgentCore custom browsers should not use public network mode
<a name="bedrockagentcore-5"></a>

**Category:** Protect > Secure network configuration > Resources within VPC

**Severity:** High

**Resource type:** `AWS::BedrockAgentCore::BrowserCustom`

**AWS Config rule:** [bedrockagentcore-browsercustom-network-mode-not-public](https://docs.aws.amazon.com/config/latest/developerguide/bedrockagentcore-browsercustom-network-mode-not-public.html)

**Schedule type:** Change triggered

**Parameters:** None

This control checks whether an Amazon Bedrock AgentCore custom browser is configured with public network mode. The control fails if the network mode is set to public.

Using PUBLIC network mode for Amazon Bedrock AgentCore custom browsers exposes browser sessions directly to the internet, increasing the attack surface and risk of unauthorized access. Configuring browsers with VPC network mode ensures that browser traffic is confined within your private network, enabling you to apply network-level security controls such as security groups, network ACLs, and VPC flow logs.

### Remediation
<a name="bedrockagentcore-5-remediation"></a>

To remediate this finding, delete the non-compliant Bedrock AgentCore custom browser and recreate it with VPC network mode. For instructions, see [Configure Amazon Bedrock AgentCore Runtime and tools for VPC](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/agentcore-vpc.html#agentcore-configuration) in the *Amazon Bedrock AgentCore Developer Guide*.

## [BedrockAgentCore.6] Bedrock AgentCore custom browsers should have session recording enabled
<a name="bedrockagentcore-6"></a>

**Category:** Identify > Logging

**Severity:** Medium

**Resource type:** `AWS::BedrockAgentCore::BrowserCustom`

**AWS Config rule:** [bedrockagentcore-browsercustom-recording-enabled](https://docs.aws.amazon.com/config/latest/developerguide/bedrockagentcore-browsercustom-recording-enabled.html)

**Schedule type:** Change triggered

**Parameters:** None

This control checks whether an Amazon Bedrock AgentCore custom browser has session recording enabled with an S3 destination configured. The control fails if a custom browser does not have recording enabled or does not have an S3 location configured for storing recordings.

Session recording for Bedrock AgentCore custom browsers ensures full auditability of browser interactions, enabling detection of unauthorized access, data exfiltration, or malicious activity during automated browsing sessions.

### Remediation
<a name="bedrockagentcore-6-remediation"></a>

For instructions on how to enable browser session recording, see [Session Recording and Replay](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/browser-session-recording.html) in the *Amazon Bedrock AgentCore Developer Guide*.

## [BedrockAgentCore.7] Bedrock AgentCore custom code interpreters should use a private network configuration
<a name="bedrockagentcore-7"></a>

**Category:** Protect > Secure network configuration > Resources within VPC

**Severity:** High

**Resource type:** `AWS::BedrockAgentCore::CodeInterpreterCustom`

**AWS Config rule:** [bedrockagentcore-codeinterpreter-networkmode-check](https://docs.aws.amazon.com/config/latest/developerguide/bedrockagentcore-codeinterpreter-networkmode-check.html)

**Schedule type:** Change triggered

**Parameters:** None

This control checks whether an Amazon Bedrock AgentCore custom code interpreter is configured with a private network mode. The control fails if the network mode is set to `PUBLIC` or `SANDBOX`.

Configuring Bedrock AgentCore custom code interpreters with a private network mode ensures that code execution environments are isolated within your VPC. Public or sandbox network modes expose the code interpreter to the internet, increasing the risk of unauthorized access and data exfiltration. Using private network mode restricts network access and helps protect sensitive data processed during code interpretation.

### Remediation
<a name="bedrockagentcore-7-remediation"></a>

To remediate this finding, delete the non-compliant Bedrock AgentCore custom code interpreter and recreate it with VPC network mode. For instructions, see [Configuring VPC access for runtime and tools](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/agentcore-vpc.html#agentcore-configuration) in the *Amazon Bedrock AgentCore Developer Guide*.