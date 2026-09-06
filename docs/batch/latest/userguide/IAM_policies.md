

# AWS Batch IAM policies, roles, and permissions
<a name="IAM_policies"></a>

By default, users don't have permission to create or modify AWS Batch resources or to perform tasks using the AWS Batch API, AWS Batch console, or the AWS CLI. To allow users to perform these actions, create IAM policies that grant users permission for the specific resources and API operations. Then, attach the policies to the users or groups that require those permissions.

When you attach a policy to a user or group of users, the policy either allows or denies the permissions to perform specific tasks on specific resources. For more information, see [Permissions and Policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/PermissionsAndPolicies.html) in the *IAM User Guide*. For more information about managing and creating custom IAM policies, see [Managing IAM Policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/ManagingPolicies.html).

AWS Batch makes calls to other AWS services on your behalf. As a result, AWS Batch must authenticate using your credentials. More specifically, AWS Batch authenticates by creating an IAM role and policy that provides these permissions. Then, it associates the role with your compute environments when you create them. For more information, see [Amazon ECS instance role](instance_IAM_role.md), [IAM Roles](https://docs.aws.amazon.com/IAM/latest/UserGuide/roles-toplevel.html), [Using Service-Linked Roles](https://docs.aws.amazon.com/IAM/latest/UserGuide/using-service-linked-roles.html), and [Creating a Role to Delegate Permissions to an AWS Service](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-service.html) in the *IAM User Guide*.

**Note**  
For information about controlling who can apply capacity tags to Amazon ECS Managed Instances compute environments, see [Control access to capacity tags with `batch:SetCapacityTags`](capacity-tags-access-policy.md).

**Topics**
+ [IAM policy structure](iam-policy-structure.md)
+ [Resource: Example policies for AWS Batch](ExamplePolicies_BATCH.md)
+ [Resource: AWS Batch managed policy](batch_managed_policies.md)
+ [Control access to capacity tags with `batch:SetCapacityTags`](capacity-tags-access-policy.md)