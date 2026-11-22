

AWS Well-Architected Agent is in preview release and is subject to change.

# Service-linked role permissions for AWS Well-Architected Tool organization sharing and resource discovery

AWS Well-Architected Tool uses the service-linked role named `AWSServiceRoleForWellArchitected`. This service-linked role carries two AWS managed policies that support two AWS WA Tool capabilities: organization resource sharing and resource discovery. AWS WA Tool uses the role to retrieve information about the organization it is a member of when you activate resource sharing with AWS Organizations, and to access AWS services and resources that relate to AWS WA Tool resources when you turn on Discovery support.

The `AWSServiceRoleForWellArchitected` service-linked role trusts the following service to assume the role:
+ `wellarchitected.amazonaws.com`

**Organization sharing policy**

The organization resource sharing permissions policy, the AWS managed policy named `AWSWellArchitectedOrganizationsServiceRolePolicy`, grants AWS WA Tool administrative permissions in AWS Organizations that are required to support AWS WA Tool integration with Organizations. For the full list of permissions granted by this policy, see [AWS managed policy: AWSWellArchitectedOrganizationsServiceRolePolicy](security-iam-awsmanpol.md#security-iam-awsmanpol-AWSWellArchitectedOrganizationsServiceRolePolicy).

**Resource discovery policy**

The resource discovery permissions policy is the AWS managed policy named ``. This policy allows AWS WA Tool to access AWS services and resources that relate to AWS WA Tool resources on your behalf. At a high level, the policy grants read access to Trusted Advisor checks (`trustedadvisor:DescribeChecks` and `trustedadvisor:DescribeCheckItems`), CloudFormation stacks (`cloudformation:DescribeStacks` and `cloudformation:ListStackResources`), AWS Resource Groups (`resource-groups:ListGroupResources`) and resource tags (`tag:GetResources`), and management of AppRegistry attribute groups scoped to `AWS_WellArchitected-*` resources. For the full list of permissions granted by this policy, see [AWS managed policy: AWSWellArchitectedDiscoveryServiceRolePolicy](security-iam-awsmanpol.md#security-iam-awsmanpol-AWSWellArchitectedDiscoveryServiceRolePolicy). You can also view the policy details, including the full JSON policy document, in [AWSWellArchitectedDiscoveryServiceRolePolicy](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSWellArchitectedDiscoveryServiceRolePolicy.html) in the *AWS Managed Policy Reference*.

You must configure permissions to allow your users, groups, or roles to create, edit, or delete a service-linked role. For more information, see [Service-linked role permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/using-service-linked-roles.html#service-linked-role-permissions) in the *IAM User Guide*.

## Creating a service-linked role for AWS WA Tool organization sharing and resource discovery
<a name="using-service-linked-roles-tool-org-sharing-creating"></a>

You don't need to manually create the `AWSServiceRoleForWellArchitected` service-linked role. AWS WA Tool creates the service-linked role for you automatically when you activate AWS Organizations support, or when you turn on Discovery support, by using the AWS WA Tool console. For the organization sharing capability, you must use the AWS WA Tool console to activate sharing so that the service-linked role is created. If you activate trusted access by using the AWS Organizations console or the `enable-aws-service-access` AWS CLI command, the service-linked role isn't created and you can't share resources within your organization. For more information about activating sharing, see [Activate resource sharing within AWS Organizations](sharing.md#getting-started-sharing-orgs). For the resource discovery capability, AWS WA Tool creates the service-linked role when you turn on **Activate Discovery support** in the AWS WA Tool console. For more information, see [Activating support in AWS WA Tool for other AWS services](activate-integrations.md).

## Editing a service-linked role for AWS WA Tool organization sharing and resource discovery
<a name="using-service-linked-roles-tool-org-sharing-editing"></a>

AWS Well-Architected does not allow you to edit the `AWSServiceRoleForWellArchitected` service-linked role. After you create a service-linked role, you cannot change the name of the role because various entities might reference the role. However, you can edit the description of the role using IAM. For more information, see [Editing a service-linked role](https://docs.aws.amazon.com/IAM/latest/UserGuide/using-service-linked-roles.html#edit-service-linked-role) in the *IAM User Guide*.

## Deleting a service-linked role for AWS WA Tool organization sharing and resource discovery
<a name="using-service-linked-roles-tool-org-sharing-deleting"></a>

If you no longer need to share resources with your entire organization or OUs, we recommend that you disable resource sharing and delete the `AWSServiceRoleForWellArchitected` service-linked role. You must first disable resource sharing with AWS Organizations before you can delete the service-linked role. For information about disabling resource sharing, see [Activate resource sharing within AWS Organizations](sharing.md#getting-started-sharing-orgs).

If you also use Discovery support, turn off **Activate Discovery support** in the AWS WA Tool console before you delete the service-linked role. For more information, see [Activating support in AWS WA Tool for other AWS services](activate-integrations.md).

After you disable resource sharing, you can delete the service-linked role manually by using the IAM console, the AWS Command Line Interface (AWS CLI), or the AWS API. For more information, see [Deleting a service-linked role](https://docs.aws.amazon.com/IAM/latest/UserGuide/using-service-linked-roles.html#delete-service-linked-role) in the *IAM User Guide*.

## Supported AWS Regions for the AWS WA Tool service-linked role
<a name="using-service-linked-roles-tool-org-sharing-regions"></a>

AWS Well-Architected supports using the `AWSServiceRoleForWellArchitected` service-linked role in the following AWS Regions.