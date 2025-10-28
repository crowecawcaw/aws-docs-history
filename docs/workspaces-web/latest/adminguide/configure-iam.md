# Configuring the IAM Identity Center authentication type for Amazon WorkSpaces Secure Browser

For the **IAM Identity Center** type (advanced), you federate IAM Identity Center with your portal.
Only select this option if the following applies to you:

- Your IAM Identity Center is configured in the same AWS account and AWS Region as your web
  portal.
- If you are using AWS Organizations, you are using a management account.
  Before creating a web portal with the IAM Identity Center authentication type, you must set up IAM Identity Center
  as a standalone provider. For more information, see [Get started with common tasks
  in IAM Identity Center](../../../singlesignon/latest/userguide/getting-started.md "../../../singlesignon/latest/userguide/getting-started.md"). Or, you can connect your SAML 2.0 IdP to IAM Identity Center. For more
  information, see [Connect to an
  external identity provider](../../../singlesignon/latest/userguide/manage-your-identity-source-idp.md "../../../singlesignon/latest/userguide/manage-your-identity-source-idp.md"). Otherwise, you won't have any users or groups to
  assign to your web portal.

If you are already using IAM Identity Center, you can choose IAM Identity Center as a provider type and follow the
steps below to add, view, or remove users or groups from your web portal.

###### Note

In order to use this authentication type, your IAM Identity Center needs to be in the same
AWS account and AWS Region as your WorkSpaces Secure Browser portal. If your IAM Identity Center is in a separate
AWS account or AWS Region, follow the instructions for the
**Standard** authentication type. For more information, see [Configuring the standard authentication type for Amazon WorkSpaces Secure Browser](configure-standard.md "configure-standard.md").

If you're using AWS Organizations, you can only create WorkSpaces Secure Browser portals integrated with IAM Identity Center
using a management account.

###### Topics

- [Creating a web portal with IAM Identity Center](web-portal-IAM.md "web-portal-IAM.md")
- [Managing your web portal with IAM Identity Center](manage-IAM.md "manage-IAM.md")
- [Adding additional users and groups to a web portal](add-users-groups.md "add-users-groups.md")
- [Viewing or removing users and groups for your web portal](remove-users-groups.md "remove-users-groups.md")
