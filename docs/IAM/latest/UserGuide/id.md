# IAM Identities

An IAM identity can be associated with one or more policies, which determine what actions
an identity is authorized to perform, on which AWS resources, and under what conditions. IAM
identities include IAM users, IAM groups, and IAM roles. An IAM entity is a type
of identity that represents a human user or programmatic workload that can be authenticated and
then authorized to perform actions in AWS accounts. IAM entities include IAM users and
IAM roles. For definitions for commonly used terms, see [Terms](introduction_identity-management.md#intro-structure-terms "introduction_identity-management.md#intro-structure-terms").

You can federate existing identities from an external identity provider. These identities
will assume IAM roles to access AWS resources. For more information, see [Identity providers and federation into AWS](id_roles_providers.md "id_roles_providers.md").

You can also use AWS IAM Identity Center to create and manage identities and access to AWS resources.
IAM Identity Center permission sets automatically create the IAM roles needed to provide access to
resources. For more information, see [What is IAM Identity Center?](../../../singlesignon/latest/userguide/what-is.md "../../../singlesignon/latest/userguide/what-is.md")

The AWS account root user is an AWS account principal that is created when your AWS account is
established. The root user has access to all AWS services and resources in the account. For more
information, see [IAM root user](#id_root "#id_root").

###### Note

- Follow the [Security best practices in
  IAM](best-practices-use-cases.md "best-practices-use-cases.md") when working with IAM identities.
- Follow the [root user best practices for your
  AWS account](root-user-best-practices.md "root-user-best-practices.md") when working with the root user.
- If you're having trouble signing in, see [Sign in to the
  AWS Management Console](../../../signin/latest/userguide/console-sign-in-tutorials.md "../../../signin/latest/userguide/console-sign-in-tutorials.md").

## IAM root user

When you first create an AWS account, you begin with one sign-in identity that has
complete access to all AWS services and resources in the account. This identity is called
the AWS account _root user_. For more information, see [AWS account root
user.](id_root-user.md "id_root-user.md")

## IAM users

An _IAM user_ is an identity within your AWS account that has
specific permissions for a single person or application. For more information, see [IAM users](id_users.md "id_users.md").

## IAM user groups

An _IAM user group_ is an identity that specifies a collection of
IAM users. For more information, see [User groups](id_groups.md "id_groups.md").

## IAM roles

An _IAM role_ is an identity within your AWS account that has
specific permissions. It's similar to an IAM user, but isn't associated with a specific
person. For more information, see [IAM roles](id_roles.md "id_roles.md").
