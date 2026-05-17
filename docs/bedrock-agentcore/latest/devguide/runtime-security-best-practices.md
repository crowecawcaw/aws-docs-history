# Security best practices for AgentCore Runtime

This topic consolidates security best practices for Amazon Bedrock AgentCore Runtime. Use these recommendations to secure your agent deployments, protect data, and follow the principle of least privilege.

###### Topics

- [Session isolation and data protection](#security-bp-session-isolation "#security-bp-session-isolation")
- [IAM and least privilege](#security-bp-iam-least-privilege "#security-bp-iam-least-privilege")
- [Resource-based policies and cross-account access](#security-bp-resource-policies "#security-bp-resource-policies")
- [Confused deputy prevention](#security-bp-confused-deputy "#security-bp-confused-deputy")
- [Authentication best practices](#security-bp-authentication "#security-bp-authentication")
- [Credential and secret management](#security-bp-credentials "#security-bp-credentials")
- [Network security](#security-bp-network "#security-bp-network")
- [Encryption](#security-bp-encryption "#security-bp-encryption")
- [Auditing and monitoring](#security-bp-auditing "#security-bp-auditing")
- [Shared responsibility model](#security-bp-shared-responsibility "#security-bp-shared-responsibility")
- [Command execution security](#security-bp-command-execution "#security-bp-command-execution")

## Session isolation and data protection

Amazon Bedrock AgentCore Runtime provides strong isolation boundaries through dedicated microVMs. Follow these practices to maintain data protection:

- **Understand the isolation boundary** — Each user session runs in a dedicated microVM with isolated CPU, memory, and filesystem. Commands and agent code cannot access other customers' workloads or escape the VM boundary. After session completion, the entire microVM is terminated and memory is sanitized.
- **Enforce session-to-user mappings in your backend** — AgentCore does not enforce session-to-user mappings. Your client backend must maintain the relationship between users and their session IDs, and implement lifecycle management such as maximum number of sessions per user.
- **Be aware of filesystem permission behavior** — When using [persistent file systems](runtime-filesystem-configurations.md "runtime-filesystem-configurations.md"), permissions are stored but not enforced within the session. `chmod` and `stat` work correctly, but access checks always succeed because the agent runs as the only user in the microVM.
- **Understand credential exposure within the VM** — Any code or actor running inside the microVM can access execution role credentials by calling the metadata endpoint (MMDS). Scope your execution role permissions carefully. For more information, see [Credentials Management](security-credentials-management.md "security-credentials-management.md").

## IAM and least privilege

Apply the principle of least privilege to all IAM policies associated with your AgentCore Runtime resources:

- **Do not use CLI-generated policies in production** — The IAM policies created by the AgentCore CLI are designed for development and testing purposes. These permissions grant broad access and are not suitable for production. Create custom IAM policies that restrict permissions to only the specific resources and actions required. For the full reference, see [IAM Permissions for AgentCore Runtime](runtime-permissions.md "runtime-permissions.md").
- **Scope permissions to specific runtime ARNs** — Avoid wildcard resource statements. Use the full ARN of your runtime resources in IAM policy `Resource` fields.
- **Restrict `InvokeAgentRuntimeForUser`** — Only trusted principals should have this permission. Scope it to specific runtime resources using IAM resource conditions.
- **Deny user-id delegation where not needed** — For runtimes where user-id delegation is not required, explicitly deny the action:

```
{
   "Statement": [
      {
         "Sid": "DenyUserIdDelegation",
         "Effect": "Deny",
         "Action": "bedrock-agentcore:InvokeAgentRuntimeForUser",
         "Resource": "arn:aws:bedrock-agentcore:REGION:ACCOUNT_ID:runtime/*"
      }
   ]
}
```

- **Prevent privilege escalation** — Ensure that the execution role associated with your runtime has equal or fewer privileges than the principals who can invoke it. For more information, see [Credentials Management](security-credentials-management.md "security-credentials-management.md").
- **Use IAM condition keys to enforce VPC deployments** — Use `bedrock-agentcore:subnets` and `bedrock-agentcore:securityGroups` condition keys to require that all runtimes are deployed in approved VPCs. For examples, see [Use VPC condition keys with AgentCore Runtime](security-vpc-condition.md "security-vpc-condition.md").
- **Use IAM Access Analyzer** — Validate your IAM policies to ensure they adhere to best practices and least-privilege principles.

## Resource-based policies and cross-account access

Resource-based policies provide fine-grained access control directly on your runtime resources:

- **Understand hierarchical authorization** — For runtime API operations such as `InvokeAgentRuntime` and `InvokeAgentRuntimeCommand`, AWS evaluates policies on both the agent runtime and the agent endpoint. Both must allow the action.
- **Configure both resources for cross-account access** — To grant cross-account access, create resource-based policies on both the agent runtime and the agent endpoint. If either resource lacks an explicit allow, the request is denied.
- **Remember that explicit deny always wins** — If any policy (identity-based or resource-based) explicitly denies an action, access is denied regardless of other policies.

For complete details, see [Resource-based policies for Amazon Bedrock AgentCore](resource-based-policies.md "resource-based-policies.md").

## Confused deputy prevention

Protect your execution roles from the confused deputy problem by using global condition context keys in trust policies:

- **Use `aws:SourceArn` and `aws:SourceAccount`** — Add these conditions to your execution role trust policy to limit which AgentCore resources can assume the role:

```
{
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "Service": "bedrock-agentcore.amazonaws.com"
      },
      "Action": "sts:AssumeRole",
      "Condition": {
        "StringEquals": {
          "aws:SourceAccount": "123456789012"
        },
        "ArnLike": {
          "aws:SourceArn": "arn:aws:bedrock-agentcore:us-east-1:123456789012:*"
        }
      }
    }
  ]
}
```

- **Use the full ARN when possible** — If you know the specific runtime resource, use its full ARN in `aws:SourceArn` instead of wildcards.

For more information, see [Cross-service confused deputy prevention](cross-service-confused-deputy-prevention.md "cross-service-confused-deputy-prevention.md").

## Authentication best practices

AgentCore Runtime supports IAM SigV4 and JWT bearer token authentication. Follow these practices to secure access:

- **Choose the right authentication method** — Use IAM SigV4 for service-to-service calls within AWS. Use JWT bearer token authentication when end users authenticate directly through an identity provider. A runtime can support one method at a time; create separate versions for different authentication types.
- **Configure JWT authorizers completely** — When using JWT authentication, configure all available validation fields: discovery URL, allowed audiences, allowed clients, allowed scopes, and required custom claims.
- **Never hardcode tokens in production code** — Use secure token retrieval mechanisms. Hardcoded tokens are a security risk in source control and deployed artifacts.
- **Derive user-id from the authenticated principal** — The `X-Amzn-Bedrock-AgentCore-Runtime-User-Id` value should be derived from the authenticated principal’s context (IAM caller identity or user token claims), not from arbitrary client-supplied values. This prevents authenticated users from impersonating other users.
- **Configure VPC endpoint policies for your auth method** — VPC endpoint policies can only restrict callers based on IAM principals, not OAuth users. For OAuth-based requests, set `Principal` to `*` in the endpoint policy. For SigV4-based authentication, specify the allowed IAM identities.

For implementation details, see [Authenticate and authorize with Inbound Auth and Outbound Auth](runtime-oauth.md "runtime-oauth.md").

## Credential and secret management

Protect credentials used by your agents and runtime environments:

- **Use AgentCore Identity for outbound authentication** — AgentCore Identity manages OAuth credentials and API keys securely, preventing credential exposure in agent code or logs. Use it for all third-party service access (Slack, GitHub, Zoom).
- **Understand MMDS credential exposure** — The MicroVM Metadata Service (MMDS) provides execution role credentials to any code running in the VM, similar to EC2’s IMDS. Scope execution role permissions to only what your agent requires.
- **Run containers as non-root users** — When building custom container images, configure them to run as a non-root user. This limits the impact of potential code execution vulnerabilities.
- **Separate user-delegated and autonomous credentials** — Use user-delegated authentication (Authorization Code Grant) when your agent acts on behalf of a specific user. Use autonomous authentication (Client Credentials Grant) when the agent operates independently.

For more information, see [Credentials Management](security-credentials-management.md "security-credentials-management.md") and [AgentCore Identity](identity.md "identity.md").

## Network security

Secure network access to and from your AgentCore Runtime environments:

- **Deploy runtimes in a VPC for private resource access** — Configure VPC connectivity to access private databases, internal APIs, and services without exposing them to the internet. For configuration details, see [Configure AgentCore Runtime for VPC](agentcore-vpc.md "agentcore-vpc.md").
- **Use AWS PrivateLink for API access** — Create interface VPC endpoints for the AgentCore data plane (`com.amazonaws.region.bedrock-agentcore`) and control plane (`com.amazonaws.region.bedrock-agentcore-control`) to avoid internet traversal. For more information, see [Use AWS PrivateLink](vpc-interface-endpoints.md "vpc-interface-endpoints.md").
- **Apply least privilege to security groups** — Define outbound rules that allow only the minimum required traffic. Do not open broad outbound access unless necessary.
- **Configure required VPC endpoints for container agents** — For VPC-mode container agents, configure VPC endpoints for ECR (`com.amazonaws.region.ecr.dkr`, `com.amazonaws.region.ecr.api`), S3 (`com.amazonaws.region.s3` gateway endpoint), and CloudWatch Logs (`com.amazonaws.region.logs`). The S3 gateway endpoint eliminates NAT gateway data processing charges for ECR image layer pulls.
- **Scope the S3 gateway endpoint policy for container agents** — Restrict the S3 gateway endpoint policy to only the bucket that Amazon ECR uses for image layer storage:

```
{
  "Statement": [
    {
      "Sid": "AllowECRLayerAccess",
      "Principal": "*",
      "Action": [
        "s3:GetObject"
      ],
      "Effect": "Allow",
      "Resource": ["arn:aws:s3:::prod-region-starport-layer-bucket/*"]
    }
  ]
}
```

Replace `region` with your AWS Region identifier (for example, `us-east-2`).

- **Scope the S3 gateway endpoint policy for direct code deploy agents** — For zip-based deployments, restrict the policy to the internal service-owned code artifact bucket:

```
{
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": "*",
      "Action": "s3:GetObject",
      "Resource": [
        "arn:aws:s3:::acr-code-*-region-an",
        "arn:aws:s3:::acr-code-*-region-an/*"
      ]
    }
  ]
}
```

Replace `region` with your AWS Region identifier (for example, `us-west-2`). If you also use [persistent file systems](runtime-filesystem-configurations.md "runtime-filesystem-configurations.md"), add the session storage bucket to this policy. For more information, see [Configure AgentCore Runtime for VPC](agentcore-vpc.md "agentcore-vpc.md").

- **Use private subnets with NAT gateways** — Public subnets do not provide internet access for AgentCore Runtime. Always place runtime ENIs in private subnets with a route to a NAT gateway for outbound internet access.
- **Transport security** — All connections use TLS 1.2 or higher. WebSocket connections use WSS (WebSocket Secure) over HTTPS.
- **Enforce header limits** — Custom headers are limited to 4KB per value and 20 headers per runtime. The `Authorization` header is reserved for agents with OAuth inbound access.

## Encryption

AgentCore Runtime protects data with encryption at rest and in transit:

- **Encryption in transit** — All communication between clients and AgentCore Runtime, and between AgentCore Runtime and its dependencies, is protected using TLS 1.2 or higher. This is configured by default and requires no additional setup.
- **Encryption at rest** — Data at rest is encrypted using AWS owned encryption keys from AWS Key Management Service (AWS KMS) by default.
- **Use TLS 1.3 where possible** — While TLS 1.2 is the minimum, AWS recommends TLS 1.3 for improved security and performance.

For more information, see [Data encryption](data-encryption.md "data-encryption.md").

## Auditing and monitoring

Implement comprehensive auditing to detect and investigate security events:

- **Enable CloudTrail logging** — AWS CloudTrail records API calls including `InvokeAgentRuntime`, `InvokeAgentRuntimeCommand`, and control plane operations. Each record includes caller identity, timestamp, source IP address, and response status.
- **Use CloudWatch Logs for command auditing** — AgentCore Runtime sends the request ID and input command to your agent’s CloudWatch Logs log group. Use these logs to maintain an audit trail of commands executed in your sessions.
- **Correlate logs using request IDs** — Use the request ID to correlate CloudTrail records (who called the API) with CloudWatch Logs (what command was executed).
- **Set up metric filters and alarms** — Configure CloudWatch Logs metric filters to detect unexpected command patterns or unauthorized access attempts. Create alarms to notify your team of anomalies.
- **Log user-id delegation relationships** — When using the `X-Amzn-Bedrock-AgentCore-Runtime-User-Id` header, log the relationship between the authenticated IAM principal and the user-id value for audit purposes.
- **Enable VPC Flow Logs** — For VPC-connected runtimes, enable VPC Flow Logs to audit network-level traffic and identify unexpected communication patterns.
- **Review CloudTrail logs regularly** — Periodically review logs for unauthorized access attempts, especially for sensitive workloads.

## Shared responsibility model

Understand the division of security responsibilities between AWS and you:

###### AWS responsibilities:

- Secure infrastructure and microVM isolation at the hardware level
- OS kernel patching for all deployment modes
- Language runtime patching for direct code deployments
- Network infrastructure security
- Service availability and resilience

###### Your responsibilities:

- Agent code security and dependency management
- IAM access controls and resource policies
- Security of commands executed in runtime sessions
- Session-to-user mapping enforcement
- Container image updates (for container deployments) — rebuild with the latest secure base image regularly
- Input validation and prompt injection prevention
- Network configuration (security groups, VPC endpoints, route tables)

###### Important

For direct code deployments, AgentCore Runtime applies security patches to the runtime OS automatically. AgentCore Runtime does not apply security patches to programming language runtimes after they reach their end of support date. Deprecated runtimes are provided as-is and may contain unpatched vulnerabilities. For supported runtimes, see [Supported runtimes for code deployment](runtime-code-deploy-supported-runtimes.md "runtime-code-deploy-supported-runtimes.md").

###### Note

Security patches can expose issues with existing code that relies on previous insecure behavior. If this risk is not acceptable, use container images to deploy your agent.

## Command execution security

When using `InvokeAgentRuntimeCommand`, apply these security practices:

- **Understand the security boundary** — Commands have full access to the container filesystem and any configured credentials or secrets within the microVM. The isolation boundary is the microVM itself.
- **Use deterministic operations for deterministic tasks** — Use `InvokeAgentRuntimeCommand` for operations like tests, git, and builds. Don’t route deterministic operations through the LLM via `InvokeAgentRuntime`.
- **Restrict who can execute commands** — Use IAM policies to limit which principals can call `InvokeAgentRuntimeCommand`. Not all users who can invoke an agent should be able to execute arbitrary commands.
- **Keep traffic within your network** — Configure VPC endpoints to avoid internet traversal for command execution API calls.
- **Set appropriate timeouts** — Configure command timeouts based on expected execution duration to prevent resource waste from runaway processes.

For complete details, see [Execute commands in runtime sessions](runtime-execute-command.md "runtime-execute-command.md").
