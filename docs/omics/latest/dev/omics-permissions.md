# IAM permissions for HealthOmics

You can use AWS Identity and Access Management (IAM) to manage access to the HealthOmics API and resources such as stores and workflows. For
users and applications in your account that use HealthOmics, you manage permissions in a permissions policy that you can
apply to IAM users, groups, or roles.

To manage permissions for users and applications in your accounts, [use the
policies that HealthOmics provides](permissions-user.md "permissions-user.md"), or write your own. The HealthOmics console uses multiple services to get
information about your function's configuration and triggers. You can use the provided policies as-is, or as a
starting point for more restrictive policies.

HealthOmics uses IAM [service roles](permissions-service.md "permissions-service.md") to access other services on your
behalf. For example, you would create or choose a service role when you run a workflow that reads data from Amazon S3. For some features,
you also need to [configure permissions on resources in other services](permissions-resource.md "permissions-resource.md").
Review these requirements before you start working with HealthOmics

For more information about IAM, see [What is IAM?](../../../IAM/latest/UserGuide/introduction.md "../../../IAM/latest/UserGuide/introduction.md") in the
_IAM User Guide_.

###### Topics

- [Identity-based IAM policies for HealthOmics](permissions-user.md "permissions-user.md")
- [Service roles for AWS HealthOmics](permissions-service.md "permissions-service.md")
- [Amazon ECR permissions](permissions-ecr.md "permissions-ecr.md")
- [HealthOmics Resource permissions](permissions-resource.md "permissions-resource.md")
- [Permissions for data access using Amazon S3 URIs](s3-sharing.md "s3-sharing.md")
