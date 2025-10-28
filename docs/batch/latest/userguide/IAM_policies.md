# AWS Batch IAM policies, roles, and permissions

By default, users don't have permission to create or modify AWS Batch resources or to perform tasks using the
AWS Batch API, AWS Batch console, or the AWS CLI. To allow users to perform these actions, create IAM policies that grant
users permission for the specific resources and API operations. Then, attach the policies to the users or groups that
require those permissions.

When you attach a policy to a user or group of users, the policy either allows or denies the permissions to
perform specific tasks on specific resources. For more information, see [Permissions and Policies](../../../IAM/latest/UserGuide/PermissionsAndPolicies.md "../../../IAM/latest/UserGuide/PermissionsAndPolicies.md") in the
_IAM User Guide_. For more information about managing and creating custom IAM policies, see
[Managing IAM Policies](../../../IAM/latest/UserGuide/ManagingPolicies.md "../../../IAM/latest/UserGuide/ManagingPolicies.md").

AWS Batch makes calls to other AWS services on your behalf. As a result, AWS Batch must authenticate using your
credentials. More specifically, AWS Batch authenticates by creating an IAM role and policy that provides these
permissions. Then, it associates the role with your compute environments when you create them. For more information,
see [Amazon ECS instance role](instance_IAM_role.md "instance_IAM_role.md"), [IAM Roles](../../../IAM/latest/UserGuide/roles-toplevel.md "../../../IAM/latest/UserGuide/roles-toplevel.md"), [Using Service-Linked Roles](../../../IAM/latest/UserGuide/using-service-linked-roles.md "../../../IAM/latest/UserGuide/using-service-linked-roles.md"), and [Creating a Role to Delegate
Permissions to an AWS Service](../../../IAM/latest/UserGuide/id_roles_create_for-service.md "../../../IAM/latest/UserGuide/id_roles_create_for-service.md") in the _IAM User Guide_.

###### Topics

- [IAM policy structure](iam-policy-structure.md "iam-policy-structure.md")
- [Resource: Example policies for AWS Batch](ExamplePolicies_BATCH.md "ExamplePolicies_BATCH.md")
- [Resource: AWS Batch managed policy](batch_managed_policies.md "batch_managed_policies.md")
