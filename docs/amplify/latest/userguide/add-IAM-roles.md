# Using IAM roles with Amplify applications

An IAM role is an IAM identity with specific permissions. The role's permissions
determine what the identity can and cannot do in AWS. You can create IAM roles in your
AWS account and use them to delegate permissions to Amplify Hosting. To learn more about
roles, see [IAM
roles](../../../IAM/latest/UserGuide/id_roles.md "../../../IAM/latest/UserGuide/id_roles.md") in the _IAM User Guide_.

You can use the following types of IAM roles to grant Amplify Hosting the permissions
it needs to perform actions on your behalf or run compute code that accesses other AWS
resources.

**IAM service role**

Amplify assumes this role to perform actions on your behalf. This role is
required for applications with backend resources.

**IAM SSR Compute role**

Allows a server-side rendered (SSR) application to securely access specific AWS
resources.

**IAM SSR CloudWatch Logs role**

When you deploy an SSR app, the app requires an IAM service role that Amplify
assumes to allow Amplify to access Amazon CloudWatch Logs.

###### Topics

- [Adding a service role with permissions to deploy backend resources](amplify-service-role.md "amplify-service-role.md")
- [Adding an SSR Compute role to allow access to AWS resources](amplify-SSR-compute-role.md "amplify-SSR-compute-role.md")
- [Adding a service role with permissions to access CloudWatch Logs](cloudwatch-logs-role.md "cloudwatch-logs-role.md")
