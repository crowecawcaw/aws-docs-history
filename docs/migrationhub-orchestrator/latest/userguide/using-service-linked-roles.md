AWS Migration Hub will no longer be open to new customers starting November 7, 2025. To continue using the service, sign up prior to November 7, 2025. For capabilities similar to AWS Migration Hub, explore [AWS Transform](https://aws.amazon.com/transform "https://aws.amazon.com/transform").

# Using service-linked roles for

Migration Hub Orchestrator

Migration Hub Orchestrator uses AWS Identity and Access Management (IAM)[service-linked roles](../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-linked-role "../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-linked-role"). A service-linked role is a unique type of IAM role that is
linked directly to Migration Hub Orchestrator. Service-linked roles are predefined by Migration Hub Orchestrator and
include all of the permissions that the service requires to call other AWS services on your
behalf.

A service-linked role makes setting up Migration Hub Orchestrator easier because you don’t have to
manually add the necessary permissions. Migration Hub Orchestrator defines the permissions of its
service-linked roles, and unless you make changes to the configuration, only Migration Hub Orchestrator can
assume its roles. Configurable permissions include the trust policy and the permissions policy.
You can't attach the permissions policy to any other IAM entity.

For information about other services that support service-linked roles, see [AWS Services That Work with IAM](../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md "../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md") and look for the services that have **Yes** in the **Service-Linked Role**
column. Follow the **Yes** link to view the service-linked role
documentation for that service, if applicable.

## Service-linked role permissions for Migration Hub Orchestrator

Migration Hub Orchestrator uses the service-linked role named
**AWSServiceRoleForMigrationHubOrchestrator** and associates it with the
**AWSMigrationHubOrchestratorServiceRolePolicy** IAM policy – Provides access to AWS Migration Hub and AWS Application Discovery Service. This policy also grants permissions for storing reports in Amazon Simple Storage Service (Amazon S3).

The **AWSServiceRoleForMigrationHubOrchestrator** service-linked role
trusts the following services to assume the role:

- `migrationhub-orchestrator.amazonaws.com`

The role permissions policy allows Migration Hub Orchestrator to complete the following actions.

AWS Application Discovery Service actions

`discovery:ListConfigurations`

`discovery:DescribeConfigurations`

AWS Launch Wizard actions

`launchwizard:DescribeProvisionedApp`

`launchwizard:GetDeployment`

`launchwizard:ListDeployments`

`launchwizard:ListProvisionedApps`

Amazon Elastic Compute Cloud actions

`ec2:DescribeInstances`

`ec2:CreateLaunchTemplateVersion`

`ec2:ModifyLaunchTemplate`

`ec2:DescribeImportImageTasks`

`ec2:DescribeLaunchTemplates`

AWS Migration Hub actions

`mgh:GetHomeRegion`

Amazon EC2 Systems Manager actions
`ssm:SendCommand`

`ssm:GetCommandInvocation`

`ssm:CancelCommand`

`ssm:DescribeInstanceInformation`

`ssm:GetCommandInvocatio`

Amazon S3 actions

`s3:GetObject`

`s3:ListBucket`

Amazon EventBridge actions

`events:PutTargets`

`events:DescribeRule`

`events:DeleteRule`

`events:PutRule`

`events:RemoveTargets`

AWS Application Migration Service actions

`mgn:GetReplicationConfiguration`

`mgn:GetLaunchConfiguration`

`mgn:StartCutover`

`mgn:FinalizeCutover`

`mgn:StartTest`

`mgn:UpdateReplicationConfiguration`

`mgn:DescribeSourceServers`

`mgn:MarkAsArchived`

`mgn:ChangeServerLifeCycleState`

`mgn:StartReplication`

To view the permissions for this policy, see [AWSMigrationHubOrchestratorServiceRolePolicy](../../../aws-managed-policy/latest/reference/AWSMigrationHubOrchestratorServiceRolePolicy.md "../../../aws-managed-policy/latest/reference/AWSMigrationHubOrchestratorServiceRolePolicy.md") in the
_AWS Managed Policy Reference Guide_.

To view the update history of this policy, see [Migration Hub Orchestrator updates to AWS managed
policies](security-iam-awsmanpol.md#security-iam-awsmanpol-updates "security-iam-awsmanpol.md#security-iam-awsmanpol-updates").

You must configure permissions to allow an IAM entity (such as a user, group, or role)
to create, edit, or delete a service-linked role. For more information, see [Service-Linked Role Permissions](../../../IAM/latest/UserGuide/using-service-linked-roles.md#service-linked-role-permissions "../../../IAM/latest/UserGuide/using-service-linked-roles.md#service-linked-role-permissions") in the
_IAM User Guide_.

## Creating a service-linked role for Migration Hub Orchestrator

You don't need to manually create a service-linked role. When you
agree to allow Migration Hub to create a service-linked role (SLR) in your account in the AWS Management Console, Migration Hub Orchestrator creates the service-linked role for
you.

If you delete this service-linked role, and then need to create it again, you can use the
same process to recreate the role in your account. When you agree to allow Migration Hub to create a service-linked role (SLR) in your account,
Migration Hub Orchestrator creates the service-linked role for you again.

## Editing a service-linked role for Migration Hub Orchestrator

Migration Hub Orchestrator does not allow you to edit the
**AWSServiceRoleForMigrationHubOrchestrator** service-linked role. After
you create a service-linked role, you cannot change the name of the role because various
entities might reference the role. However, you can edit the description of the role using the
Migration Hub Orchestrator console, CLI, or API.

## Deleting a service-linked role for Migration Hub Orchestrator

**To manually delete the service-linked role using
IAM**

Use the IAM console, the AWS CLI, or the AWS API to delete the **AWSServiceRoleForMigrationHubOrchestrator** service-linked role. For more
information, see [Deleting a Service-Linked Role](../../../IAM/latest/UserGuide/using-service-linked-roles.md#delete-service-linked-role "../../../IAM/latest/UserGuide/using-service-linked-roles.md#delete-service-linked-role") in the _IAM User Guide_.

When deleting Migration Hub Orchestrator resources used by the
**AWSServiceRoleForMigrationHubOrchestrator** SLR, you cannot have any
running assessments (tasks for generating recommendations). No background assessments can be
running, either. If assessments are running, the SLR deletion fails in the IAM console. If
the SLR deletion fails, you can retry the deletion after all background tasks have completed.
You don’t need to clean up any created resources before you delete the SLR.

## Supported Regions for Migration Hub Orchestrator service-linked roles

Migration Hub Orchestrator supports using service-linked roles in all of the regions where the service
is available. For more information, see [AWS Regions and Endpoints](../../../general/latest/gr/rande.md "../../../general/latest/gr/rande.md").
