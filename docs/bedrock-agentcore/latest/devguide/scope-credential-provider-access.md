# Scope down access to credential

providers by workload identity

You can use IAM policies to control which workload identities have access to
specific credential providers. This enables fine-grained access control, ensuring
that only authorized agents can retrieve credentials for particular services.

**Access control mechanisms**

- **Workload identity-based restrictions**
  – Limit credential provider access to specific workload
  identities
- **Resource-level permissions** –
  Control access to individual credential providers using ARN-based
  policies
- **Directory-level controls** – Manage
  access at the workload identity directory level

###### Topics

- [IAM policy examples](#iam-policy-examples "#iam-policy-examples")
- [Implementation steps](#policy-implementation-steps "#policy-implementation-steps")

## IAM policy examples

The following examples demonstrate how to create IAM policies that restrict
credential provider access based on workload identity:

**Restrict API key provider access**

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "GetResourceApiKey",
      "Effect": "Allow",
      "Action": [
        "bedrock-agentcore:GetResourceApiKey"
      ],
      "Resource": [
        "arn:aws:bedrock-agentcore:us-east-1:<account_id>:workload-identity-directory/default",
        "arn:aws:bedrock-agentcore:us-east-1:<account_id>:workload-identity-directory/default/workload-identity/<workload-identity-name>",
        "arn:aws:bedrock-agentcore:us-east-1:<account_id>:token-vault/default"
      ]
    }
  ]
}
```

**Restrict OAuth2 credential provider
access**

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "GetResourceOauth2Token",
      "Effect": "Allow",
      "Action": [
        "bedrock-agentcore:GetResourceOauth2Token"
      ],
      "Resource": [
        "arn:aws:bedrock-agentcore:us-east-1:<account_id>:workload-identity-directory/default",
        "arn:aws:bedrock-agentcore:us-east-1:<account_id>:workload-identity-directory/default/workload-identity/<workload-identity-name>",
        "arn:aws:bedrock-agentcore:us-east-1:<account_id>:token-vault/default"
      ]
    }
  ]
}
```

**Allow multiple workload identities access to a
credential provider**

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "GetResourceApiKeyMultipleIdentities",
      "Effect": "Allow",
      "Action": [
        "bedrock-agentcore:GetResourceApiKey"
      ],
      "Resource": [
        "arn:aws:bedrock-agentcore:us-east-1:<account_id>:workload-identity-directory/default",
        "arn:aws:bedrock-agentcore:us-east-1:<account_id>:workload-identity-directory/default/workload-identity/agent-1",
        "arn:aws:bedrock-agentcore:us-east-1:<account_id>:workload-identity-directory/default/workload-identity/agent-2",
        "arn:aws:bedrock-agentcore:us-east-1:<account_id>:workload-identity-directory/default/workload-identity/agent-3",
        "arn:aws:bedrock-agentcore:us-east-1:<account_id>:token-vault/default"
      ]
    }
  ]
}
```

## Implementation steps

To implement workload identity-based access control for credential
providers:

1. **Identify your workload identities**
   – Use `aws bedrock-agentcore-control
list-workload-identities` to list all workload identities in
   your account. For information about creating and managing workload
   identities, see [Manage workload identities with
   AgentCore Identity](identity-manage-agent-ids.md "identity-manage-agent-ids.md").
2. **Determine credential provider ARNs**
   – Identify the specific credential providers you want to control
   access to
3. **Create IAM policies** – Write
   IAM policies that specify which workload identities can access which
   credential providers
4. **Attach policies to roles** –
   Attach the policies to the IAM roles used by your agents or
   applications
5. **Test access controls** – Verify
   that only authorized workload identities can access the specified
   credential providers

**Best practices**

- Use descriptive names for workload identities to make policy
  management easier
- Regularly audit and review access policies to ensure they align with
  your security requirements
- Consider using IAM policy conditions for additional access controls
  based on time, IP address, or other factors
- Test policies in a development environment before applying them to
  production workloads
