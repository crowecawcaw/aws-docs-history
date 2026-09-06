# AWS Agent Registry integration

With Amazon Quick, you can connect to the [AWS Agent Registry](../../../bedrock-agentcore/latest/devguide/registry.md "../../../bedrock-agentcore/latest/devguide/registry.md"). Use this integration to surface the remote Model Context Protocol (MCP) servers registered in your Agent Registry as native Quick connectors. Your organization can maintain a single source of truth for its MCP servers in the Agent Registry while giving Quick users governed access to them.

As an account administrator, you link one Agent Registry to your Quick account from the Quick administration console. After the registry is linked, you see the registry's remote MCP records as pre-configured connector cards on the **Connectors** page. You can then create a connector from one. The connector works like any other Quick connector across Quick Chat, agents, apps, Amazon Quick Flows, and Amazon Quick Research.

Everything happens through the Quick administration console and the **Connectors** page. There is no separate command line or SDK to install. Records are read from the Agent Registry when the **Connectors** page loads. Nothing from the Agent Registry is copied into Quick.

## What is supported

The following table shows which Agent Registry records and configurations Amazon Quick supports.

AWS Agent Registry support in Amazon Quick| Supported | Not supported |
| --- | --- |
| MCP records that use the `mcpServer` descriptor. | Skill and custom record types. |
| Agent records accessed through the MCP protocol (records that use the `mcpServer` descriptor). | Agent-to-agent (A2A) descriptors. |
| Remote MCP servers that expose a remote server URL. | Local MCP endpoints, such as `npx`, `docker`, and local or standard input/output (stdio) servers. |

For more information about the account, Region, authorization, and status requirements that a registry must meet, see [Prerequisites](#aws-agent-registry-prerequisites "#aws-agent-registry-prerequisites").

## Prerequisites

Before an administrator can link a registry, make sure that all of the following are in place:

- **Registry location** – An AWS Agent Registry exists in the same AWS account and the same AWS Region as your Quick account. Cross-account and cross-Region registries are not supported.
- **Registry configuration** – The registry uses AWS IAM (`AWS_IAM`) authorization with Signature Version 4 (SigV4) and is in the `READY` status. Registries that use JSON Web Token (JWT) authorization are not supported and do not appear in the Quick administration console.
- **Registry namespace** – Only registries in the `agent-registry` namespace are supported. Older Amazon Bedrock AgentCore registries in the `bedrock-agentcore` namespace are not supported.
- **One registry for each account** – You can connect one Agent Registry for each Quick account.
- **Administrator access** – The administrator signs in to the Quick administration console with an IAM identity that has permission to list and view registries. For more information, see [IAM permissions](#aws-agent-registry-permissions "#aws-agent-registry-permissions").

## IAM permissions

The integration uses two distinct sets of permissions that apply to different steps. Keep them separate.

**Administrator identity (to browse and select a registry)**

The IAM identity that the administrator uses to sign in to the administration console needs the following permissions on the registry. Without these permissions, the **AWS Agent Registry** page cannot list your registries.

- `agent-registry:ListRegistries`

**Service role (to load records on the Connectors page)**

How you satisfy this requirement depends on which service role your account uses:

- **Quick-managed role** (`aws-quicksight-agent-registry-role-v0`) – Quick grants these permissions automatically when the administrator enables the registry. No action is required.
- **Customer-managed service role** – An administrator must manually add the following permissions to the role for the connected registry:

  - `agent-registry:ListDiscoverableRegistryRecords`
  - `agent-registry:SearchDiscoverableRegistryRecords`
  - `agent-registry:GetDiscoverableRegistryRecord`

If a customer-managed role is missing these permissions, the **Connectors** page cannot load registry records. Quick detects the customer-managed role and displays the role ARN and the required permissions so that the administrator knows exactly what to add. For a complete policy example, see [IAM policy reference](#aws-agent-registry-policy-reference "#aws-agent-registry-policy-reference").

## Link a registry (administrator)

After the prerequisites and IAM permissions are in place, you link the registry as an account administrator.

1. In the Quick administration console, go to **Manage account** -> **Permissions** -> **AWS Agent Registry**.
2. Review the list of AWS Agent Registries in your account. Only registries that meet the requirements in [Prerequisites](#aws-agent-registry-prerequisites "#aws-agent-registry-prerequisites") appear.
3. Turn on the toggle for the registry that you want to connect. Only one registry can be active for each account.
4. Confirm the selection. Quick grants the account's service role the read-only Agent Registry permissions that it needs and links the registry to your Quick account.

###### Note

When your account uses the Quick-managed service role, linking the registry is the entire administrator action. You do not need to create a role or edit a trust policy. Quick sets up the trust relationship and permissions for you when you enable the registry.

## Create a connector (user)

After an administrator links a registry, you can create a connector from it.

1. Open the **Connectors** page.
2. Choose the **Create for your team** tab. Registry-sourced connectors appear on this tab, not on the **Available** tab.
3. Find the MCP connector sourced from the registry by searching or browsing. Each connector comes pre-populated with its MCP server URL, name, and description.
4. Choose the connector to begin setup.
5. Complete the **Authenticate** step by configuring or signing in with the required credentials, such as OAuth. The Agent Registry does not store authentication credentials, so each user provides or authenticates with their own credentials.
6. On the **Manage permissions** step, choose which tools to turn on or turn off.
7. Choose **Create and continue**.
8. Share the connector with the appropriate user groups.

###### Note

Registry-sourced connectors are classified as **Custom MCP** connectors. This classification matters for settings such as [custom permissions](custom-permissions.md "custom-permissions.md").

## After setup

After a connector is created, it is available across Quick Chat, agents, apps, Amazon Quick Flows, and Amazon Quick Research, like any other Quick connector.

The connector is an independent Quick resource. Removing the registry link in the administration console does not delete connectors that were already created from it.

## Manage connectors

To edit, share, or delete a connector that you created from the Agent Registry, see [Managing existing integrations](integration-workflows.md#managing-existing-integrations "integration-workflows.md#managing-existing-integrations").

## Troubleshooting

- **Registries do not appear on the AWS Agent Registry page** – Confirm that the administrator's IAM identity has the `agent-registry:ListRegistries` permission. Also confirm that the registry uses AWS IAM authorization (registries that use JWT authorization are not listed), is in the `READY` status, and is in the same AWS account and Region as your Quick account.
- **The Connectors page cannot load registry records** – If your account uses a customer-managed service role, confirm that the role has the required `agent-registry` permissions for the connected registry. Quick displays the role ARN and the required permissions so that you know what to add. For the policy, see [IAM policy reference](#aws-agent-registry-policy-reference "#aws-agent-registry-policy-reference").

## Limitations

- Only remote MCP servers are supported. Local MCP endpoints, such as `npx`, `docker`, and local or stdio servers, are not supported.
- Only MCP records and agent records accessed through the MCP protocol are supported. Agent-to-agent (A2A) descriptors, skill records, and custom records are not supported.

For more information about account, Region, authorization, and registry-count requirements, see [Prerequisites](#aws-agent-registry-prerequisites "#aws-agent-registry-prerequisites").

## IAM policy reference

If your account uses the Quick-managed role (`aws-quicksight-agent-registry-role-v0`), you do not need this policy. Quick provisions the role and attaches the required Agent Registry permissions automatically when the administrator enables a registry. This policy applies only when your account uses a customer-managed service role.

If your account uses a customer-managed service role, attach a policy with the following permissions, scoped to the registry that you are connecting. Replace the example resource ARN with your registry's ARN.

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "agent-registry:ListDiscoverableRegistryRecords",
        "agent-registry:SearchDiscoverableRegistryRecords",
        "agent-registry:GetDiscoverableRegistryRecord"
      ],
      "Resource": [
        "arn:aws:agent-registry:us-west-2:111122223333:registry/AbCdEf012345",
        "arn:aws:agent-registry:*:111122223333:registry/AbCdEf012345/record/*"
      ]
    }
  ]
}
```
