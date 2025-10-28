# Identity and access management in AWS Artifact

When you sign up for AWS, you provide an email address and password that are
associated with your AWS account. These are your
_root credentials_,
and they provide complete access to all of your AWS resources, including resources
for AWS Artifact. However, we strongly recommend that you don't use the root account for
everyday access. We also recommend that you don't share account credentials with others
to give them complete access to your account.

Instead of signing in to your AWS account with root credentials or sharing your
credentials with others, you should create a special user identity called an
_IAM
user_ for yourself and for anyone who might need access to a document or
agreement in AWS Artifact. With this approach, you can provide individual sign-in information for
each user, and you can grant each user only the permissions that they need to work with
specific documents. You can also grant multiple IAM users the same permissions by granting
the permissions to an IAM group and adding the IAM users to the group.

If you already manage user identities outside AWS, you can use IAM
_identity
providers_ instead of creating IAM users. For more information, see
[Identity providers and
federation](../../../IAM/latest/UserGuide/id_roles_providers.md "../../../IAM/latest/UserGuide/id_roles_providers.md") in the
_IAM User Guide_.

###### Contents

- [Granting user access](grant-access.md "grant-access.md")
- [Migrating to fine-grained permissions for AWS Artifact reports](migrating-reports-to-v2-permissions.md "migrating-reports-to-v2-permissions.md")
- [Migrating to fine-grained permissions for AWS Artifact agreements](migrating-agreements-to-v2-permissions.md "migrating-agreements-to-v2-permissions.md")
- [Example IAM policies in commercial AWS Regions](example-iam-policies.md "example-iam-policies.md")
- [Example IAM policies in AWS GovCloud (US) Regions](example-govcloud-iam-policies.md "example-govcloud-iam-policies.md")
- [Using AWS managed policies](security-iam-awsmanpol.md "security-iam-awsmanpol.md")
- [Using service-linked roles](using-service-linked-roles.md "using-service-linked-roles.md")
- [Using IAM condition keys](using-condition-keys.md "using-condition-keys.md")
