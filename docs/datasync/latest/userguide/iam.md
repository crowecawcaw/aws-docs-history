# Identity and access management in AWS DataSync

AWS uses security credentials to identify you and to grant you access to your AWS
resources. You can use features of AWS Identity and Access Management (IAM) to allow other users, services, and
applications to use your AWS resources fully or in a limited way, without sharing your
security credentials.

By default, IAM identities (users, groups, and roles) don't have permission to create,
view, or modify AWS resources. To allow users, groups, and roles to access AWS DataSync resources
and interact with the DataSync console and API, we recommend that you use an IAM policy that
grants them permission to use the specific resources and API actions that they will need. You
then attach the policy to the IAM identity that requires access. For an overview of the basic
elements for a policy, see [Access management for AWS DataSync](managing-access-overview.md "managing-access-overview.md").

###### Topics

- [Access management for AWS DataSync](managing-access-overview.md "managing-access-overview.md")
- [AWS managed policies for AWS DataSync](security-iam-awsmanpol.md "security-iam-awsmanpol.md")
- [IAM customer managed policies for
  AWS DataSync](using-identity-based-policies.md "using-identity-based-policies.md")
- [Using service-linked roles for
  DataSync](using-service-linked-roles.md "using-service-linked-roles.md")
- [Permissions for tagging DataSync resources during
  creation](supported-iam-actions-tagging.md "supported-iam-actions-tagging.md")
- [Cross-service confused deputy
  prevention](cross-service-confused-deputy-prevention.md "cross-service-confused-deputy-prevention.md")
