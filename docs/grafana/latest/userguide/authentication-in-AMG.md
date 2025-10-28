# Authenticate users in Amazon Managed Grafana

workspaces

Individual users sign into your workspaces, to edit and view your dashboards. You
can assign users to your workspaces and [give them user, editor, or administrator permissions](AMG-manage-users-and-groups-AMG.md "AMG-manage-users-and-groups-AMG.md"). To get started, you
create (or use an existing) identity provider to authenticate users.

Users are authenticated to use the Grafana console in an Amazon Managed Grafana workspace by single
sign-on using your organization’s identity provider, instead of by using IAM. Each
workspace can use one or both of the following authentication methods:

- User credentials stored in identity providers (IdPs) that support Security
  Assertion Markup Language 2.0 (SAML 2.0)
- AWS IAM Identity Center. AWS Single-sign-on (**AWS SSO**) was rebranded to
  **IAM Identity Center**.
  For each of your workspaces, you can use SAML, IAM Identity Center, or both. If you begin by using one
  method, you can switch to using the other.

You must give your users (or groups that they belong to) permissions to the workspace
before they can access functionality within the workspace. For more information about
giving permissions to your users, see [Manage user and group access to
Amazon Managed Grafana workspaces](AMG-manage-users-and-groups-AMG.md "AMG-manage-users-and-groups-AMG.md").

###### Topics

- [Use SAML with your Amazon Managed Grafana
  workspace](authentication-in-AMG-SAML.md "authentication-in-AMG-SAML.md")
- [Use AWS IAM Identity Center with your Amazon Managed Grafana
  workspace](authentication-in-AMG-SSO.md "authentication-in-AMG-SSO.md")
