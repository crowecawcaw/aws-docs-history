# Using service-linked roles for AWS Agent Registry

###### Migration Now Open

AWS Agent Registry has launched under the new `agent-registry` namespace. Support for the public preview `bedrock-agentcore` namespace will be discontinued on September 17, 2026. For migration instructions, see [Comprehensive registry migration guide](registry-faq.md "registry-faq.md").

AWS Agent Registry uses AWS Identity and Access Management (IAM) [service-linked roles](../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-linked-role "../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-linked-role"). A service-linked role is a unique type of IAM role that is linked directly to AWS Agent Registry. Service-linked roles are predefined by AWS Agent Registry and include all the permissions that the service requires to call other AWS services on your behalf.

AWS Agent Registry uses the service-linked role named **AWSServiceRoleForAgentRegistry**, which provides the permissions necessary for the service to publish registry-related CloudWatch metrics to your account. The role permissions policy associated with `AWSServiceRoleForAgentRegistry` is named `AWSAgentRegistryServiceRolePolicy`.

## Service-linked role permissions for AWS Agent Registry

AWS Agent Registry uses the service-linked role named `AWSServiceRoleForAgentRegistry`, which allows AWS Agent Registry to call AWS services on your behalf.

The `AWSServiceRoleForAgentRegistry` service-linked role trusts the following services to assume the role:

- `agent-registry.amazonaws.com`

The role permissions policy named `AWSAgentRegistryServiceRolePolicy` allows AWS Agent Registry to complete the following actions on the specified resources:

- Action: `cloudwatch:PutMetricData` on all AWS resources

###### Note

The policy includes the condition key `{"StringEquals": {"cloudwatch:namespace": "AWS/AgentRegistry"}}`, which means that the service-linked role can only send metric data to the `AWS/AgentRegistry` CloudWatch namespace.

You must configure permissions to allow an IAM entity (such as a user, group, or role) to create, edit, or delete a service-linked role. For more information, see [Service-linked role permissions](../../../IAM/latest/UserGuide/using-service-linked-roles.md#service-linked-role-permissions "../../../IAM/latest/UserGuide/using-service-linked-roles.md#service-linked-role-permissions") in the _IAM User Guide_.

## Creating the service-linked role for AWS Agent Registry

You don’t need to manually create a service-linked role. When you create a registry in AWS Agent Registry in the AWS Management Console, the AWS CLI, or the AWS API, AWS Agent Registry creates the service-linked role for you.

###### Note

The first time you create a registry, you must be granted the `iam:CreateServiceLinkedRole` permission in an identity-based policy.

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

To delete the `AWSServiceRoleForAgentRegistry` role, you must first delete all registries in AWS Agent Registry.

###### Note

If AWS Agent Registry is using the role when you try to delete the resources, then the deletion might fail. If that happens, wait for a few minutes and try the operation again.

**To manually delete the service-linked role using IAM**

Use the IAM console, the AWS CLI, or the AWS API to delete the `AWSServiceRoleForAgentRegistry` service-linked role. For more information, see [Deleting a service-linked role](../../../IAM/latest/UserGuide/using-service-linked-roles.md#delete-service-linked-role "../../../IAM/latest/UserGuide/using-service-linked-roles.md#delete-service-linked-role") in the _IAM User Guide_.

## Supported Regions for AWS Agent Registry service-linked roles

AWS Agent Registry supports using the `AWSServiceRoleForAgentRegistry` service-linked role in every Region where AWS Agent Registry is available.
