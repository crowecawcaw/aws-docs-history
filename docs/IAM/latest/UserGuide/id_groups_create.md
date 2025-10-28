# Create IAM groups

###### Note

As a [best practice](best-practices.md "best-practices.md"), we recommend that you require
human users to use federation with an identity provider to access AWS using temporary
credentials. If you follow the best practices, you are not managing IAM users and groups.
Instead, your users and groups are managed outside of AWS and are able to access AWS
resources as a _federated identity_. A federated identity is a user from
your enterprise user directory, a web identity provider, the AWS Directory Service, the
Identity Center directory, or any user that accesses AWS services by using credentials
provided through an identity source. Federated identities use the groups defined by their
identity provider. If you are using AWS IAM Identity Center, see [Manage identities
in IAM Identity Center](../../../singlesignon/latest/userguide/manage-your-identity-source-sso.md "../../../singlesignon/latest/userguide/manage-your-identity-source-sso.md") in the _AWS IAM Identity Center User Guide_ for information about creating
users and groups in IAM Identity Center.

You create IAM groups to manage access permissions for multiple users with similar roles
or responsibilities. By attaching policies to these groups, you can grant or revoke permissions
for entire sets of users. This simplifies your maintenance of security policies, as changes you
make to a group's permissions are automatically applied to all members of that group, ensuring
consistent access control. After you create the group, give the group permissions based on the
type of work that you expect the IAM users in the group to do, then add the IAM users to
the group.

For information about the permissions required to create an IAM group, see [Permissions required to access IAM
resources](access_permissions-required.md "access_permissions-required.md").

## To create an IAM group and attach policies

Console

1. Sign in to the AWS Management Console and open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. In the navigation pane, choose **User groups** and then choose
   **Create group**.
3. For **User group name**, type the name of the group.

###### Note

The number and size of IAM resources in an AWS account are limited. For more information, see [IAM and AWS STS quotas](reference_iam-quotas.md "reference_iam-quotas.md"). Group names can be a combination of up to 128 letters,
digits, and these characters: plus (+), equal (=), comma (,), period (.), at sign
(@), underscore (\_), and hyphen (-). Names must be unique within an account. They
aren't distinguished by case. For example, you cannot create groups named both
`ADMINS` and `admins`. 4. In the list of users, select the check box for each user that you want to add to
the group. 5. In the list of policies, select the check box for each policy that you want to
apply to all members of the group. 6. Choose **Create group**.

AWS CLI
Run the following command:

- [aws iam
  create-group](../../../cli/latest/reference/iam/create-group.md "../../../cli/latest/reference/iam/create-group.md")

API
Call the following operation:

- [CreateGroup](../APIReference/API_CreateGroup.md "../APIReference/API_CreateGroup.md")
