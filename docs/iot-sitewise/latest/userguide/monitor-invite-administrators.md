# Invite administrators in SiteWise Monitor

To get started in your new portal, you must assign a portal administrator. The portal
administrator creates projects, chooses project owners, and assigns assets to projects.
Portal administrators can see all of your AWS IoT SiteWise assets.

Based on the user authentication service, choose one of the following options:

IAM Identity Center
If you're using SiteWise Monitor for the first time, you can choose the user that you
created earlier to be the portal administrator. If you want to add another user as a
portal administrator, you can create an IAM Identity Center user from this page. Alternatively, you
can connect an external identity provider to IAM Identity Center. For more information, see the
[AWS IAM Identity Center User Guide](../../../singlesignon/latest/userguide.md "../../../singlesignon/latest/userguide.md").

###### To invite administrators

1. Select the check boxes for the users that you want as your portal
   administrators. This adds the users to the **Portal
   administrators** list.

###### Note

If you use IAM Identity Center as your identity store, and you're signed in to your AWS Organizations
management account, you can choose **Create user** to create an IAM Identity Center user. IAM Identity Center sends the
new user an email for them to set their password. You can then assign the user to the portal as an administrator. For more information, see
[Manage identities in IAM Identity Center](../../../singlesignon/latest/userguide/manage-your-identity-source-sso.md "../../../singlesignon/latest/userguide/manage-your-identity-source-sso.md"). 2. (Optional) Choose **Send invite to selected users**. Your
email client opens, and an invitation is populated in the message body.

You can customize the email before you send it to your portal administrators.
You can also send the email to your portal administrators later. If you're trying
SiteWise Monitor for the first time and adding your new IAM Identity Center or IAM user or role as the
portal administrator, you don't need to email yourself. 3. If you add a user that you don't want as an administrator, clear the check box
for that user. 4. When you're finished inviting portal administrators, choose
**Next**.

IAM
You can choose a user or role to be the portal administrator. If you want
to add another user or role as a portal administrator, you can create a user or
role in the IAM console. For more information, see [Creating an IAM user in your AWS
account](../../../IAM/latest/UserGuide/id_users_create.md "../../../IAM/latest/UserGuide/id_users_create.md") and [Creating IAM
roles](../../../IAM/latest/UserGuide/id_roles_create.md "../../../IAM/latest/UserGuide/id_roles_create.md") in the _IAM User Guide_.

###### To invite administrators

1. Do the following:
   - Choose **IAM users** to add an IAM user as your
     portal administrator.
   - Choose **IAM roles** to add an IAM role as your
     portal administrator.

2. Select the check boxes for the users or roles that you want as your portal
   administrators. This adds the users or roles to the **Portal
   administrators** list.
3. If you add a user or role that you don't want as an administrator, clear the
   check box for that user or role.
4. When you're finished inviting portal administrators, choose
   **Next**.

###### Important

Users or roles must have the `iotsitewise:DescribePortal`
permission to sign in to the portal.

###### Note

If you use IAM Identity Center as your identity store, and you're signed in to your AWS Organizations
management account, you can choose **Create user** to create an IAM Identity Center user. IAM Identity Center sends the
new user an email for them to set their password. You can then assign the user to the portal as an administrator. For more information, see
[Manage identities in IAM Identity Center](../../../singlesignon/latest/userguide/manage-your-identity-source-sso.md "../../../singlesignon/latest/userguide/manage-your-identity-source-sso.md").

You can change the list of portal administrators later. For more information, see [Add or remove portal administrators in AWS IoT SiteWise](portal-change-admins.md "portal-change-admins.md").

###### Note

Because only a portal administrator can create projects and assign assets to them, you
should specify at least one portal administrator.

As the last step, you add users who can access your new portal.
