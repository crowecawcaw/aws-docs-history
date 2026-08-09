# IAM Permissions

###### Migration Now Open

AWS Agent Registry has launched under the new `agent-registry` namespace. Support for the public preview `bedrock-agentcore` namespace will be discontinued on September 17, 2026. For migration instructions, see [Comprehensive registry migration guide](registry-faq.md "registry-faq.md").

## Registry actions

To create, manage, or use registries, attach an identity-based policy to your IAM identity that allows it to perform [AWS Agent Registry-related actions](../../../service-authorization/latest/reference/list_amazonagentregistry.md "../../../service-authorization/latest/reference/list_amazonagentregistry.md"). For comprehensive permissions, you can use the [AgentRegistryFullAccess](../../../aws-managed-policy/latest/reference/AgentRegistryFullAccess.md "../../../aws-managed-policy/latest/reference/AgentRegistryFullAccess.md") managed policy.

For greater security and control, you can create your own custom policy by reducing the permissions in the full access policy.

###### Note

In the `bedrock-agentcore` namespace, the actions listed below are covered by the `BedrockAgentCoreFullAccess` managed policy. In the `agent-registry` namespace, they are covered by the new `AgentRegistryFullAccess` managed policy. Each table below shows both namespaces during the migration window. For the complete migration mapping, see [Comprehensive registry migration guide](registry-faq.md "registry-faq.md").

## Registry control plane actions

###### Example

AWS Agent Registry namespace

| Action                          | Description                            | Access level |
| ------------------------------- | -------------------------------------- | ------------ |
| `agent-registry:CreateRegistry` | Grants permission to create a registry | Write        |
| `agent-registry:GetRegistry`    | Grants permission to get a registry    | Read         |
| `agent-registry:UpdateRegistry` | Grants permission to update a registry | Write        |
| `agent-registry:DeleteRegistry` | Grants permission to delete a registry | Write        |
| `agent-registry:ListRegistries` | Grants permission to list registries   | List         |

Amazon Bedrock AgentCore namespace (to be deprecated)

| Action                             | Description                            | Access level |
| ---------------------------------- | -------------------------------------- | ------------ |
| `bedrock-agentcore:CreateRegistry` | Grants permission to create a registry | Write        |
| `bedrock-agentcore:GetRegistry`    | Grants permission to get a registry    | Read         |
| `bedrock-agentcore:UpdateRegistry` | Grants permission to update a registry | Write        |
| `bedrock-agentcore:DeleteRegistry` | Grants permission to delete a registry | Write        |
| `bedrock-agentcore:ListRegistries` | Grants permission to list registries   | List         |

## Registry record control plane actions

###### Example

AWS Agent Registry namespace

| Action                                           | Description                                                          | Access level |
| ------------------------------------------------ | -------------------------------------------------------------------- | ------------ |
| `agent-registry:CreateRegistryRecord`            | Grants permission to create a registry record                        | Write        |
| `agent-registry:GetRegistryRecord`               | Grants permission to get a registry record                           | Read         |
| `agent-registry:UpdateRegistryRecord`            | Grants permission to update a registry record                        | Write        |
| `agent-registry:DeleteRegistryRecord`            | Grants permission to delete a registry record                        | Write        |
| `agent-registry:ListRegistryRecords`             | Grants permission to list registry records                           | List         |
| `agent-registry:SubmitRegistryRecordForApproval` | Grants permission to submit a registry record for approval           | Write        |
| `agent-registry:UpdateRegistryRecordStatus`      | Grants permission to approve, reject, or deprecate a registry record | Write        |

Amazon Bedrock AgentCore namespace (to be deprecated)

| Action                                              | Description                                                          | Access level |
| --------------------------------------------------- | -------------------------------------------------------------------- | ------------ |
| `bedrock-agentcore:CreateRegistryRecord`            | Grants permission to create a registry record                        | Write        |
| `bedrock-agentcore:GetRegistryRecord`               | Grants permission to get a registry record                           | Read         |
| `bedrock-agentcore:UpdateRegistryRecord`            | Grants permission to update a registry record                        | Write        |
| `bedrock-agentcore:DeleteRegistryRecord`            | Grants permission to delete a registry record                        | Write        |
| `bedrock-agentcore:ListRegistryRecords`             | Grants permission to list registry records                           | List         |
| `bedrock-agentcore:SubmitRegistryRecordForApproval` | Grants permission to submit a registry record for approval           | Write        |
| `bedrock-agentcore:UpdateRegistryRecordStatus`      | Grants permission to approve, reject, or deprecate a registry record | Write        |

## Registry data plane actions

###### Example

AWS Agent Registry namespace

| Action                                             | Description                                                                                                      | Access level |
| -------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ------------ |
| `agent-registry:SearchDiscoverableRegistryRecords` | Grants permission to search approved registry records                                                            | Read         |
| `agent-registry:ListDiscoverableRegistryRecords`   | Grants permission to list approved registry records                                                              | List         |
| `agent-registry:GetDiscoverableRegistryRecord`     | Grants permission to retrieve an approved registry record. Also authorizes `BatchGetDiscoverableRegistryRecord`. | Read         |
| `agent-registry:InvokeRegistryMcp`                 | Grants permission to invoke the registry MCP endpoint                                                            | Read         |

Amazon Bedrock AgentCore namespace (to be deprecated)

| Action                                    | Description                                           | Access level |
| ----------------------------------------- | ----------------------------------------------------- | ------------ |
| `bedrock-agentcore:SearchRegistryRecords` | Grants permission to search registry records          | Read         |
| `bedrock-agentcore:InvokeRegistryMcp`     | Grants permission to invoke the registry MCP endpoint | Read         |

###### Note

For invoking the registry MCP endpoint, you need both the search action and the `InvokeRegistryMcp` action. In the `agent-registry` namespace, the search action is `agent-registry:SearchDiscoverableRegistryRecords`; in the `bedrock-agentcore` namespace it is `bedrock-agentcore:SearchRegistryRecords`.

###### Note

`BatchGetDiscoverableRegistryRecord` does not have its own IAM action. Each requested record is authorized against `agent-registry:GetDiscoverableRegistryRecord`. Grant `GetDiscoverableRegistryRecord` to use `BatchGetDiscoverableRegistryRecord`.

## Workload identity actions (required for registry lifecycle)

The following actions are required for registry-managed workload identity operations. These actions use the `bedrock-agentcore` namespace and are called by the service on your behalf during `CreateRegistry` and `DeleteRegistry` workflows.

| Action                                     | Description                                                                             | Access level |
| ------------------------------------------ | --------------------------------------------------------------------------------------- | ------------ |
| `bedrock-agentcore:CreateWorkloadIdentity` | Grants permission to create a workload identity for a registry                          | Write        |
| `bedrock-agentcore:GetWorkloadIdentity`    | Grants permission to retrieve workload identity details (used for idempotency on retry) | Read         |
| `bedrock-agentcore:DeleteWorkloadIdentity` | Grants permission to delete a workload identity when a registry is deleted              | Write        |

###### Note

The `GetWorkloadIdentity` permission is required to support idempotent retries of the `CreateRegistry` workflow. Without this permission, if a registry creation is retried (for example, after a transient failure), the workflow cannot verify the existing workload identity and will fail.

## IAM service-linked role actions (required for registry lifecycle)

The following action is required during registry lifecycle management. This action uses the `iam` namespace and is called by the service on your behalf during the `CreateRegistry` workflow.

| Action                        | Description                                                                | Access level |
| ----------------------------- | -------------------------------------------------------------------------- | ------------ |
| `iam:CreateServiceLinkedRole` | Grants permission to create the service-linked role for AWS Agent Registry | Write        |

###### Note

The `CreateServiceLinkedRole` permission is required during registry creation to enable service to publish CloudWatch metrics in your account after the registry is created. Without this permission, registry creation will fail.

## Registry resource types

The following resource types are defined for AWS Agent Registry:

###### Example

AWS Agent Registry namespace

| Resource type   | ARN format                                                                          |
| --------------- | ----------------------------------------------------------------------------------- |
| Registry        | `arn:aws:agent-registry:{region}:{account}:registry/{registryId}`                   |
| Registry record | `arn:aws:agent-registry:{region}:{account}:registry/{registryId}/record/{recordId}` |

Amazon Bedrock AgentCore namespace (to be deprecated)

| Resource type   | ARN format                                                                             |
| --------------- | -------------------------------------------------------------------------------------- |
| Registry        | `arn:aws:bedrock-agentcore:{region}:{account}:registry/{registryId}`                   |
| Registry record | `arn:aws:bedrock-agentcore:{region}:{account}:registry/{registryId}/record/{recordId}` |
