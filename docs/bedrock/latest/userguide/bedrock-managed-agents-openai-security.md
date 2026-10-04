

# Security and IAM roles
<a name="bedrock-managed-agents-openai-security"></a>

A session uses three identities: the caller, the role that the service assumes, and the identity used by the execution environment. Use separate IAM roles for these tasks. Give each identity only the permissions it needs.

## Authenticate API requests
<a name="bedrock-managed-agents-openai-security-authenticate-api-requests"></a>

The preview examples use AWS Signature Version 4. Resolve credentials through an AWS profile or the standard AWS credential provider chain. Sign with service `bedrock-mantle` and the Region of the endpoint.

For temporary credentials, the signing implementation must include the session token. The supplied shell and Python examples do this automatically. They do not require an OpenAI API key.

## Configure the session role
<a name="bedrock-managed-agents-openai-security-configure-the-session-role"></a>

Supply a same-account IAM role ARN in `role_arn` when creating a session. You can use a role created by the examples or an existing role configured for BMA.

The following trust policy allows BMA to assume a role on behalf of the specified account. Replace `123456789012` with your account ID:

```
{
  "Version": "2012-10-17",
  "Statement": [{
    "Effect": "Allow",
    "Principal": {"Service": "bedrock-mantle.amazonaws.com"},
    "Action": "sts:AssumeRole",
    "Condition": {
      "StringEquals": {"aws:SourceAccount": "123456789012"},
      "ArnLike": {"aws:SourceArn": "arn:aws:bedrock-mantle:*:123456789012:*"}
    }
  }]
}
```

The role needs permission to invoke the selected model. For example:

```
{
  "Version": "2012-10-17",
  "Statement": [{
    "Effect": "Allow",
    "Action": "bedrock-mantle:CreateInference",
    "Resource": "*",
    "Condition": {
      "StringEquals": {"bedrock-mantle:Model": "openai.gpt-5.6-luna"}
    }
  }]
}
```

 `CreateInference` does not use a model-specific resource ARN. The model condition narrows this statement. Update it if the role must support other models.

For an AgentCore environment, also grant `bedrock-agentcore:InvokeAgentRuntime` and `bedrock-agentcore:StopRuntimeSession` on the Runtime used by the session. Scope these permissions to your Runtime ARN and its Runtime endpoint ARN. A stop request that specifies a qualifier is authorized against the endpoint ARN. Grant permissions for other AWS integrations only when the application uses them.

The example role supports the bundle's integration scenarios. Review its generated policy and narrow it for your application before adopting the example in a production workload.

## Grant permission to pass the role
<a name="bedrock-managed-agents-openai-security-grant-permission-to-pass-the-role"></a>

The identity calling `CreateAgentSession` needs `iam:PassRole` on the session role. Add this statement to the client identity's policy, replacing the role ARN:

```
{
  "Effect": "Allow",
  "Action": "iam:PassRole",
  "Resource": "arn:aws:iam::123456789012:role/BedrockManagedAgentsPreviewInferenceServiceRole",
  "Condition": {
    "StringEquals": {"iam:PassedToService": "bedrock-mantle.amazonaws.com"}
  }
}
```

Changing `BMA_INFERENCE_ROLE_ARN` does not grant permission to pass a different role. Update the caller's policy for that exact role as well.

## BMA client permissions
<a name="bedrock-managed-agents-openai-security-bma-client-permissions"></a>

The introductory workflow uses these existing preview action names:

```
bedrock-mantle:CreateAgentSession
bedrock-mantle:GetAgentSession
bedrock-mantle:ListAgentSessions
bedrock-mantle:CreateAgentSessionEvent
bedrock-mantle:ListAgentSessionEvents
bedrock-mantle:ListAgentSessionItems
bedrock-mantle:DeleteAgentSession
```

A self-hosted exec server also needs `bedrock-mantle:RegisterEnvironment` and `bedrock-mantle:ConnectEnvironment`. Use the generated `BmaAccessRole` policy as a starting point for the preview's project-scoped permissions.

AgentCore uses its separate Runtime execution role for environment registration and connection. The supplied Runtime role also has permissions for its image, logs, metrics, and filesystems, with trust conditions restricting assumptions to the account and Runtime resources.

## Protect the execution environment
<a name="bedrock-managed-agents-openai-security-protect-the-execution-environment"></a>

Commands and MCP tools run with the access available to the execution environment. Use a dedicated workspace and a restricted operating-system identity. Provide only the files, credentials, network destinations, and tools needed for the task.

Keep deployment credentials separate from the runtime. For actions with external effects, enforce authorization and any required human review in the application or tool implementation. Treat instructions from documents, websites, and tool responses as untrusted input.

## Data protection and cleanup
<a name="bedrock-managed-agents-openai-security-data-protection-and-cleanup"></a>

The AgentCore example blocks public S3 access, requires TLS for bucket access, and enables bucket versioning and S3-managed server-side encryption. Skills and generated outputs are stored in customer-owned resources with their own IAM and lifecycle controls.

The preview does not expose a customer-managed KMS key option for service-managed session data. Configuring encryption on your own storage resources is a separate concern.

Avoid including credentials or sensitive data in agent instructions, explicit MCP environment values, or diagnostic logs. Deleting a BMA session does not remove copies of data held in customer-managed files or external tools. Apply the appropriate retention and deletion controls to those resources.