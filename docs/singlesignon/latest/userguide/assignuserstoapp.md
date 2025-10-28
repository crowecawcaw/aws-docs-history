# Assign user access to applications in the IAM Identity Center

console

You can assign users single sign-on access to SAML 2.0 applications in the application
catalog or to custom SAML 2.0 applications.

Considerations for group assignments:

- Assign access directly to groups. To help
  simplify administration of access permissions, we recommend that you assign
  access directly to groups rather than to individual users. With groups you can
  grant or deny permissions to groups of users, instead of applying those
  permissions to each individual. If a user moves to a different organization, you
  simply move that user to a different group. The user then automatically receives
  the permissions that are needed for the new organization.
- Nested groups aren't supported. When assigning
  user access to applications, IAM Identity Center doesn't support users being added to nested
  groups. If a user is added to a nested group, they might receive a “You do not
  have any applications” message during sign-in. Assignments must be made against
  the immediate group for which the user is a member.

###### To assign user or group access to applications

###### Important

For AWS managed applications, you must add users directly from within the
relevant application consoles or through the APIs.

1. Open the [IAM Identity Center
   console](https://console.aws.amazon.com/singlesignon "https://console.aws.amazon.com/singlesignon").

###### Note

If you manage users in AWS Managed Microsoft AD, make sure that the IAM Identity Center console is
using the AWS Region where your AWS Managed Microsoft AD directory is located before
taking the next step. 2. Choose **Applications**. 3. In the list of applications, choose the application name to which you want to
assign access. 4. On the application details page, in the **Assigned users**
section, choose **Assign users**. 5. In the **Assign users** dialog box, enter a user display name
or group name. You can specify multiple users or groups by selecting the
applicable accounts as they appear in search results. 6. Choose **Assign users**.
