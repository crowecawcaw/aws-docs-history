# IAM role creation

To create a role, you can use the AWS Management Console, the AWS CLI, the Tools for Windows PowerShell, or the IAM API.

If you use the AWS Management Console, a wizard guides you through the steps for creating a role. The
wizard has slightly different steps depending on whether you're creating a role for an AWS
service, for an AWS account, or for a SAML or OIDC federated principal.

###### Roles for IAM users

Create this role to delegate permissions within your AWS account or to roles defined in
other AWS accounts that you own. A user in one account can switch to a role in the same or a
different account. While using the role, the user can perform only the actions and access only
the resources permitted by the role; their original user permissions are suspended. When the
user exits the role, the original user permissions are restored.

For more information, see [Create a role to give permissions to an IAM
user](id_roles_create_for-user.md "id_roles_create_for-user.md").

For more information about creating roles for cross account access, see [Create a role using custom trust policies](id_roles_create_for-custom.md "id_roles_create_for-custom.md") .

###### Roles for AWS services

Create this role to delegate permissions to a service that can perform actions on your
behalf. A [service role](id_roles.md#iam-term-service-role "id_roles.md#iam-term-service-role") that you pass to a service
must have an IAM policy with the permissions that allow the service to perform actions
associated with that service. Different permissions are required for each AWS
service.

For more information about creating service roles, see [Create a role to delegate permissions to an
AWS service](id_roles_create_for-service.md "id_roles_create_for-service.md").

For more information about creating service-linked roles, see [Create a service-linked role](id_roles_create-service-linked-role.md "id_roles_create-service-linked-role.md").

###### Roles for identity federation

Create this role to delegate permissions to users that already have identities outside of
AWS. When you use an identity provider, you don't have to create custom sign-in code or
manage your own user identities. Your external users sign in through an IdP, and you can give
those external identities permissions to use AWS resources in your account. Identity
providers help keep your AWS account secure because you don't have to distribute or embed
long-term security credentials, such as access keys, in your application.

For more information, see [Create a role for a third-party identity provider](id_roles_create_for-idp.md "id_roles_create_for-idp.md") .
