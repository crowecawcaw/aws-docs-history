# AWS Resilience Hub access

permissions reference

You can use AWS Identity and Access Management (IAM) to manage access to the application resources and
create IAM policies that apply to users, groups, or roles.

Every AWS Resilience Hub application can be configured to use the [Invoker
role](security-iam-resilience-hub-invoker-role.md "security-iam-resilience-hub-invoker-role.md") (an IAM role), or use the
current IAM user permissions (along with a set of predefined roles for
cross-account and scheduled assessment). In this role, you can attach a policy that
defines the permissions required by AWS Resilience Hub to access other AWS resources or
application resources. The invoker role must have a trust policy that is added to
AWS Resilience Hub Service Principal.

To manage permissions for your application, we recommend using [AWS managed policies for AWS Resilience Hub](security-iam-awsmanpol.md "security-iam-awsmanpol.md"). You can use these managed policies without
any modifications, or you can use them as a starting point to write your own
restrictive policies. Policies can restrict user permissions at the resource level
for different actions by using additional optional conditions.

If your application resources are in different accounts (secondary/resource
accounts), you must setup a new role in each account that contains your application
resources.

###### Note

If you define VPC endpoints for your workload resources, ensure that the VPC endpoint policies provide
read-only access to AWS Resilience Hub for accessing the resources. For more information,
see [Control access to VPC endpoints using endpoint policies](../../../vpc/latest/privatelink/vpc-endpoints-access.md "../../../vpc/latest/privatelink/vpc-endpoints-access.md").

**Topics**

- [Using IAM
  role](security-iam-resilience-hub-using-iam-role.md "security-iam-resilience-hub-using-iam-role.md")
- [Using current IAM user permissions](security-iam-resilience-hub-current-user-permissions.md "security-iam-resilience-hub-current-user-permissions.md")
