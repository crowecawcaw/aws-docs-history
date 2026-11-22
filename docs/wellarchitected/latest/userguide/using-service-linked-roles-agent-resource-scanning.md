

AWS Well-Architected Agent is in preview release and is subject to change.

# Service-linked role permissions for AWS Well-Architected Agent resource scanning

AWS Well-Architected Agent uses the service-linked role named ``. AWS WA Agent uses this service-linked role to discover and read resource configuration data across the accounts in your organization when you enable the agent's organization integration.

The `` service-linked role trusts the following service to assume the role:
+ `scanning.agent.wellarchitected.amazonaws.com`

The role uses an ARN of the following form:

```
arn:aws:iam::{{account}}:role/aws-service-role/scanning.agent.wellarchitected.amazonaws.com/
```

The role permissions policy is the AWS managed policy named `AWSWellArchitectedAgentResourceScanningServiceRolePolicy`. This policy grants AWS WA Agent read-only access to AWS resource configurations, security settings, and operational data to generate optimization recommendations. Because this is a large read-only policy, see the reference for the full list of actions and conditions. For more details about this policy, including the full JSON policy document, see [AWSWellArchitectedAgentResourceScanningServiceRolePolicy](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSWellArchitectedAgentResourceScanningServiceRolePolicy.html) in the *AWS Managed Policy Reference*.

You must configure permissions to allow your users, groups, or roles to create, edit, or delete a service-linked role. For more information, see [Service-linked role permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/using-service-linked-roles.html#service-linked-role-permissions) in the *IAM User Guide*.

## Creating a service-linked role for AWS WA Agent resource scanning
<a name="using-service-linked-roles-agent-resource-scanning-creating"></a>

You don't need to manually create the `` service-linked role. AWS WA Agent creates this service-linked role for you automatically when you enable the agent's organization integration. How the role is created depends on the account type:
+ **Management account** – AWS WA Agent creates the role inline when you enable the agent's organization integration.
+ **Member accounts** – AWS Organizations provisions the role automatically after you enable trusted access for the agent. This provisioning is asynchronous. It typically completes in under two minutes and is bounded at 8 hours.

For more information about enabling trusted access, see [Trusted access with AWS Organizations](agent-preferences.md#agent-preferences-trusted-access).

If you delete this service-linked role and then need to create it again, you can use the same process to recreate the role in your account. When you enable the agent's organization integration again, AWS WA Agent creates the service-linked role for you again.

## Editing a service-linked role for AWS WA Agent resource scanning
<a name="using-service-linked-roles-agent-resource-scanning-editing"></a>

AWS Well-Architected does not allow you to edit the `` service-linked role. After you create a service-linked role, you cannot change the name of the role because various entities might reference the role. However, you can edit the description of the role using IAM. For more information, see [Editing a service-linked role](https://docs.aws.amazon.com/IAM/latest/UserGuide/using-service-linked-roles.html#edit-service-linked-role) in the *IAM User Guide*.

## Deleting a service-linked role for AWS WA Agent resource scanning
<a name="using-service-linked-roles-agent-resource-scanning-deleting"></a>

If you no longer need to use AWS Well-Architected Agent, we recommend that you delete the `` service-linked role.

You must first disable trusted access for AWS Well-Architected Agent before you can delete the service-linked role. AWS Well-Architected enforces this order: the service does not allow you to delete the role while trusted access is still enabled. For information about disabling trusted access, see [Trusted access with AWS Organizations](agent-preferences.md#agent-preferences-trusted-access).

If you attempt to delete the role before disabling trusted access, the service returns `CanBeDeleted=false`, and the reason appears in the `Reason` field of `GetServiceLinkedRoleDeletionStatus` as one of the following messages. Both conditions are retryable.
+ The organization has trusted access enabled for AWS Well-Architected; disable trusted access before deleting this service-linked role.
+ AWS Well-Architected could not verify the organization’s trusted access status; retry the deletion later.

**Note**  
If AWS Well-Architected Agent is using the role when you try to delete the resources, the deletion might fail. If that happens, wait for a few minutes and try the operation again.

After you disable trusted access, you can delete the service-linked role manually by using the IAM console, the AWS Command Line Interface (AWS CLI), or the AWS API. For more information, see [Deleting a service-linked role](https://docs.aws.amazon.com/IAM/latest/UserGuide/using-service-linked-roles.html#delete-service-linked-role) in the *IAM User Guide*.

## Supported AWS Regions for AWS WA Agent resource scanning service-linked roles
<a name="using-service-linked-roles-agent-resource-scanning-regions"></a>

AWS Well-Architected supports using the `` service-linked role in the following AWS Regions.