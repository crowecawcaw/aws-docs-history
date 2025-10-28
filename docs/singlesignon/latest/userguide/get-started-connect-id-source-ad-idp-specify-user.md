# Connect Active Directory

and specify a user

If you are already using Active Directory, the following topics will help you prepare to
connect your directory to IAM Identity Center.

You can connect an AWS Managed Microsoft AD directory or a self-managed directory in Active Directory
with IAM Identity Center.

###### Note

IAM Identity Center doesn't support SAMBA4-based Simple AD as an identity source.

**AWS Managed Microsoft AD**

1. Review the guidance in [Microsoft AD
   directory](manage-your-identity-source-ad.md "manage-your-identity-source-ad.md").
2. Follow the steps in [Connect a directory in AWS Managed Microsoft AD to IAM Identity Center](connectawsad.md "connectawsad.md").
3. Configure Active Directory to synchronize the user to whom you want to grant
   administrative permissions into IAM Identity Center. For more information, see [Synchronize an administrative user into
   IAM Identity Center](#sync-admin-user-from-ad "#sync-admin-user-from-ad").
   **Self-managed directory in Active Directory**

4. Review the guidance in [Microsoft AD
   directory](manage-your-identity-source-ad.md "manage-your-identity-source-ad.md").
5. Follow the steps in [Connect a self-managed directory in Active Directory to
   IAM Identity Center](connectonpremad.md "connectonpremad.md").
6. Configure Active Directory to synchronize the user to whom you want to grant
   administrative permissions into IAM Identity Center. For more information, see [Synchronize an administrative user into
   IAM Identity Center](#sync-admin-user-from-ad "#sync-admin-user-from-ad").
   **External IdP**

7. Review the guidance in [External identity providers](manage-your-identity-source-idp.md "manage-your-identity-source-idp.md").
8. Follow the steps in [How to connect to an external identity provider](how-to-connect-idp.md "how-to-connect-idp.md").
9. Configure your IdP to provision users into IAM Identity Center.

###### Note

Before you set up automatic, group-based provisioning of all your workforce
identities from your IdP into IAM Identity Center, we recommend that you sync the one user to whom you
want to grant administrative permissions into IAM Identity Center.

## Synchronize an administrative user into

IAM Identity Center

After you connect your Active Directory to IAM Identity Center, you can specify a user to whom you
want to grant administrative permissions, and then synchronize that user from your directory
into IAM Identity Center.

1. Open the [IAM Identity Center
   console](https://console.aws.amazon.com/singlesignon "https://console.aws.amazon.com/singlesignon").
2. Choose **Settings**.
3. On the **Settings** page, choose the **Identity
   source** tab, choose **Actions**, and then choose
   **Manage Sync**.
4. On the **Manage Sync** page, choose the **Users**
   tab, and then choose **Add users and groups**.
5. On the **Users** tab, under **User**, enter the
   exact user name and choose **Add**.
6. Under **Added Users and Groups**, do the following:
   1. Confirm that the user to whom you want to grant administrative permissions is
      specified.
   2. Select the check box to the left of the user name.
   3. Choose **Submit**.

7. In the **Manage sync** page, the user that you specified appears in
   the **Users in sync scope** list.
8. In the navigation pane, choose **Users**.
9. On the **Users** page, it might take some time for the user that
   you specified to appear in the list. Choose the refresh icon to update the list of
   users.

At this point, your user doesn't have access to the management account. You will set up
administrative access to this account by creating an administrative permission set and
assigning the user to that permission set. For more information, see [Create a permission set](howtocreatepermissionset.md "howtocreatepermissionset.md").
