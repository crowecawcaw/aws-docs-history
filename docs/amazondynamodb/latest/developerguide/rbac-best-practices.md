# DynamoDB resource-based policy best practices

This topic describes the best practices for defining access permissions for your DynamoDB
resources and the actions allowed on these resources.

## Simplify access control to DynamoDB

resources

If the AWS Identity and Access Management principals that need access to a DynamoDB resource are part of the same
AWS account as the resource owner, an IAM identity-based policy is not required for each
principal. A resource-based policy that is attached to the given resources will suffice.
This type of configuration simplifies access control.

## Protect your DynamoDB resources with resource-based

policies

For all DynamoDB tables and streams, create resource-based policies to enforce access
control for these resources. Resource-based policies enable you to centralize permissions at
the resource level, simplify access control to DynamoDB tables, indexes, and streams, and
reduce administration overhead. If no resource-based policy is specified for a table or a
stream, access to the table or stream will be implicitly denied, unless identity-based
policies associated with the IAM principals allow access.

## Apply least-privilege permissions

When you set permissions with resource-based policies for DynamoDB resources, grant only
the permissions required to perform an action. You do this by defining the actions that can
be taken on specific resources under specific conditions, also known as least-privilege
permissions. You might start with broad permissions while you explore the permissions that
are required for your workload or use case. As your use case matures, you can work to reduce
the permissions that you grant to work toward least privilege.

## Analyze cross-account access activity

for generating least-privilege policies

IAM Access Analyzer reports cross-account access to external entities specified in
resource-based policies, and provides visibility to help you refine permissions and conform
to least privilege. For more information about policy generation, see [IAM Access Analyzer policy generation](../../../IAM/latest/UserGuide/access-analyzer-policy-generation.md "../../../IAM/latest/UserGuide/access-analyzer-policy-generation.md").

## Use IAM Access Analyzer to generate least-privilege

policies

To grant only the permissions required to perform a task, you can generate policies
based on your access activity that is logged in AWS CloudTrail. IAM Access Analyzer analyzes the
services and actions that your policies use.
