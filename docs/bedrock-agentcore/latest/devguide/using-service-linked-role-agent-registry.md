# Using service-linked roles for AWS Agent Registry

###### Migration Now Open

AWS Agent Registry has launched under the new `agent-registry` namespace. Support for the public preview `bedrock-agentcore` namespace will be discontinued on September 17, 2026. For migration instructions, see [Comprehensive registry migration guide](registry-faq.md "registry-faq.md").

AWS Agent Registry uses AWS Identity and Access Management (IAM) [service-linked roles](../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-linked-role "../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-linked-role"). A service-linked role is a unique type of IAM role that is linked directly to AWS Agent Registry. Service-linked roles are predefined by AWS Agent Registry and include all the permissions that the service requires to call other AWS services on your behalf.

AWS Agent Registry uses the service-linked role named **AWSServiceRoleForAgentRegistry**. This role provides the permissions necessary for AWS Agent Registry to discover resources across your organization’s member accounts (auto-detection), manage registry records on your behalf, set up AWS Config configuration recorders for resource tracking, and publish CloudWatch metrics. The role permissions policy associated with `AWSServiceRoleForAgentRegistry` is named [`AWSAgentRegistryServiceRolePolicy`](../../../aws-managed-policy/latest/reference/AWSAgentRegistryServiceRolePolicy.md "../../../aws-managed-policy/latest/reference/AWSAgentRegistryServiceRolePolicy.md"). For the complete policy document, see [AWSAgentRegistryServiceRolePolicy](../../../aws-managed-policy/latest/reference/AWSAgentRegistryServiceRolePolicy.md "../../../aws-managed-policy/latest/reference/AWSAgentRegistryServiceRolePolicy.md") in the _AWS Managed Policy Reference Guide_.

## Service-linked role permissions for AWS Agent Registry

AWS Agent Registry uses the service-linked role named `AWSServiceRoleForAgentRegistry`, which allows AWS Agent Registry to call AWS services on your behalf.

The `AWSServiceRoleForAgentRegistry` service-linked role trusts the following services to assume the role:

- `agent-registry.amazonaws.com`

The role permissions policy named [`AWSAgentRegistryServiceRolePolicy`](../../../aws-managed-policy/latest/reference/AWSAgentRegistryServiceRolePolicy.md "../../../aws-managed-policy/latest/reference/AWSAgentRegistryServiceRolePolicy.md") allows AWS Agent Registry to complete the following actions:

### AWS Organizations access

AWS Agent Registry reads organization metadata to support auto-detection of resources across member accounts.

- `organizations:DescribeAccount` — Retrieve details about member accounts in your organization.
- `organizations:DescribeOrganization` — Retrieve information about the organization.
- `organizations:ListAccounts` — List all accounts in the organization.
- `organizations:ListDelegatedAdministrators` — Identify delegated administrators registered for auto-detection.

These actions apply to all resources (`*`).

### AWS Config service-linked role creation

AWS Agent Registry creates the AWS Config service-linked role when setting up configuration recorders for resource tracking in member accounts.

- `iam:CreateServiceLinkedRole` — Create the `AWSServiceRoleForConfig` role.

This action is restricted to the resource `arn:aws:iam::*:role/aws-service-role/config.amazonaws.com/AWSServiceRoleForConfig` and is conditioned on `iam:AWSServiceName` equaling `config.amazonaws.com`.

### AWS Config configuration recorder management

AWS Agent Registry manages service-linked configuration recorders to track supported resources for auto-detection.

- `config:PutServiceLinkedConfigurationRecorder` — Create or update a configuration recorder for auto-detection.
- `config:DeleteServiceLinkedConfigurationRecorder` — Remove the configuration recorder when auto-detection is disabled.
- `config:DescribeConfigurationRecorders` — Describe configuration recorders (read access).
- `config:DescribeConfigurationRecorderStatus` — Check the status of configuration recorders.

Write actions (`Put` and `Delete`) are conditioned on `config:ConfigurationRecorderServicePrincipal` equaling `agent-registry.amazonaws.com`, which means only recorders owned by AWS Agent Registry can be modified.

Read actions (`Describe`) are scoped to resources matching `arn:aws:config:*:*:configuration-recorder/AWSConfigurationRecorderForAgentRegistry*`.

### Registry record management

AWS Agent Registry manages registry records as part of auto-detection — creating, updating, and removing records when resources are discovered, changed, or deleted in member accounts.

- `agent-registry:CreateRegistryRecord` — Create a record for a newly discovered resource.
- `agent-registry:DeleteRegistryRecord` — Remove a record when the source resource is deleted.
- `agent-registry:GetRegistryRecord` — Read a record to check its current state.
- `agent-registry:ListRegistryRecords` — List records in a registry.
- `agent-registry:UpdateRegistryRecord` — Update a record when the source resource changes.

These actions are scoped to `arn:aws:agent-registry:*:*:registry/*` and conditioned on `aws:ResourceAccount` matching `${aws:PrincipalAccount}`, which means the role can only manage records in registries owned by the same account.

### CloudWatch metrics

AWS Agent Registry publishes operational metrics to Amazon CloudWatch for monitoring.

- `cloudwatch:PutMetricData` — Publish metrics to CloudWatch.

This action is conditioned on `cloudwatch:namespace` being either `AWS/AgentRegistry` or `AWS/Usage`, and on `aws:ResourceAccount` matching `${aws:PrincipalAccount}`. The role can only send metric data to these specific namespaces within the same account.

### Permissions summary

| Capability                 | Actions                                                                                                                                                                                                                              |
| -------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Read organization metadata | `organizations:DescribeAccount`, `organizations:DescribeOrganization`, `organizations:ListAccounts`, `organizations:ListDelegatedAdministrators`                                                                                     |
| Set up AWS Config          | `iam:CreateServiceLinkedRole` (for Config), `config:PutServiceLinkedConfigurationRecorder`, `config:DeleteServiceLinkedConfigurationRecorder`, `config:DescribeConfigurationRecorders`, `config:DescribeConfigurationRecorderStatus` |
| Manage registry records    | `agent-registry:CreateRegistryRecord`, `agent-registry:DeleteRegistryRecord`, `agent-registry:GetRegistryRecord`, `agent-registry:ListRegistryRecords`, `agent-registry:UpdateRegistryRecord`                                        |
| Publish metrics            | `cloudwatch:PutMetricData`                                                                                                                                                                                                           |

You must configure permissions to allow an IAM entity (such as a user, group, or role) to create, edit, or delete a service-linked role. For more information, see [Service-linked role permissions](../../../IAM/latest/UserGuide/using-service-linked-roles.md#service-linked-role-permissions "../../../IAM/latest/UserGuide/using-service-linked-roles.md#service-linked-role-permissions") in the _IAM User Guide_.

## Creating the service-linked role for AWS Agent Registry

You don’t usually need to manually create the service-linked role. When you create a registry in AWS Agent Registry in the AWS Management Console, the AWS CLI, or the AWS API, AWS Agent Registry creates the service-linked role for you.

###### Note

The first time you create a registry, you must be granted the `iam:CreateServiceLinkedRole` permission in an identity-based policy.

###### Important

For an **organization-scoped registry encrypted with a customer managed key**, the service-linked role must already exist in the registry administrator account (typically the delegated administrator) before you call `CreateRegistry` — it is not created for you as part of that call. The registry administrator’s KMS key policy names the `AWSServiceRoleForAgentRegistry` role as a principal, and IAM rejects any key policy that references a principal that does not yet exist.

Create the role in the registry administrator account first, either by enabling trusted access for auto-detection (which provisions it through ASLRP) or by running `aws iam create-service-linked-role --aws-service-name agent-registry.amazonaws.com`.

In all other cases — including non-organization-scoped registries encrypted with a customer managed key — `CreateRegistry` creates the service-linked role for you if it doesn’t already exist.

For related setup steps, see [Policy statement for the service-linked role](registry-kms-key-policy.md#registry-encryption-key-policy-slr "registry-kms-key-policy.md#registry-encryption-key-policy-slr") and [Step 1: Enable trusted access and create the service-linked role](registry-organizations.md#registry-organizations-step1 "registry-organizations.md#registry-organizations-step1").

If you delete this service-linked role and then need to create it again, you can use the same process to recreate the role in your account. When you create a registry in AWS Agent Registry, AWS Agent Registry creates the service-linked role for you again.

You can also use the IAM console to create a service-linked role with the **AWS Agent Registry** use case. In the AWS CLI or the AWS API, create a service-linked role with the `agent-registry.amazonaws.com` service name:

```
aws iam create-service-linked-role --aws-service-name "agent-registry.amazonaws.com"
```

For more information, see [Creating a service-linked role](../../../IAM/latest/UserGuide/using-service-linked-roles.md#create-service-linked-role "../../../IAM/latest/UserGuide/using-service-linked-roles.md#create-service-linked-role") in the _IAM User Guide_. If you delete this service-linked role, you can use this same process to create the role again.

## Editing the service-linked role for AWS Agent Registry

AWS Agent Registry does not allow you to edit the `AWSServiceRoleForAgentRegistry` service-linked role. After you create a service-linked role, you can’t change the name of the role because various entities might reference the role.

## Deleting the service-linked role for AWS Agent Registry

If you no longer need to use a feature or service that requires a service-linked role, we recommend that you delete that role. This prevents you from having an unused entity that isn’t actively monitored or maintained. However, you must clean up the resources for your service-linked role before you can manually delete it.

To delete the `AWSServiceRoleForAgentRegistry` role, you must first:

1. Disable auto-detection on any organization-scoped registries.
2. Delete all registries in AWS Agent Registry.

###### Important

If you delete the `AWSServiceRoleForAgentRegistry` service-linked role while registries still exist, auto-detection stops working — new resources are not discovered and existing records are not updated or removed. CloudWatch metrics for AWS Agent Registry also stop being published. To restore functionality, recreate the role by creating a new registry or by running `aws iam create-service-linked-role --aws-service-name "agent-registry.amazonaws.com"`.

###### Note

If AWS Agent Registry is using the role when you try to delete the resources, then the deletion might fail. If that happens, wait for a few minutes and try the operation again.

**To manually delete the service-linked role using IAM**

Use the IAM console, the AWS CLI, or the AWS API to delete the `AWSServiceRoleForAgentRegistry` service-linked role. For more information, see [Deleting a service-linked role](../../../IAM/latest/UserGuide/using-service-linked-roles.md#delete-service-linked-role "../../../IAM/latest/UserGuide/using-service-linked-roles.md#delete-service-linked-role") in the _IAM User Guide_.

## Supported Regions for AWS Agent Registry service-linked roles

AWS Agent Registry supports using the `AWSServiceRoleForAgentRegistry` service-linked role in every Region where AWS Agent Registry is available.
