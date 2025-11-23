# Using Active Directory as an identity source

If you are managing users in either your AWS Managed Microsoft AD directory using Directory Service or your
self-managed directory in Active Directory (AD), you can change your IAM Identity Center identity source
to work with those users. We recommend that you consider connecting this identity source
when you enable IAM Identity Center and choose your identity source. Doing this before you create any
users and groups in the default Identity Center directory will help you avoid the additional
configuration that is required if you change your identity source later.

To use Active Directory as your identity source, your configuration must meet the following prerequisites:

- If you are using AWS Managed Microsoft AD, you must enable IAM Identity Center in the same AWS Region where your
  AWS Managed Microsoft AD directory is set up. IAM Identity Center stores the assignment data in the same Region
  as the directory. To administer IAM Identity Center, you might need to switch to the Region where IAM Identity Center is configured.
  Also, note that the AWS access portal uses the same access URL as your directory.
- Use an Active Directory residing in the management account:

You must have an existing AD Connector or AWS Managed Microsoft AD directory set up in AWS Directory Service, and it
must reside within your AWS Organizations management account. You can connect only one AD Connector directory or one directory in
AWS Managed Microsoft AD at a time. If you need to support multiple domains or forests, use AWS Managed Microsoft AD. For more information, see:

    + [Connect a directory in AWS Managed Microsoft AD to IAM Identity Center](connectawsad.md "connectawsad.md")
    + [Connect a self-managed directory in Active Directory to
     IAM Identity Center](connectonpremad.md "connectonpremad.md")

- Use an Active Directory residing in the delegated
  administrator account:

If you plan to enable an IAM Identity Center delegated administrator and use Active Directory as your
IAM Identity Center identity source, you can use an existing AD Connector or AWS Managed Microsoft AD
directory set up in AWS Directory residing in the delegated admin account.

If you decide to change the IAM Identity Center identity source from any other source to Active Directory, or
change it from Active Directory to any other source, the directory must reside in (be
owned by) the IAM Identity Center delegated administrator member account if one exists; otherwise,
it must be in the management account.
This tutorial guides you through the basic set up for using Active Directory as an IAM Identity Center identity source.

If you are already using Active Directory , the following topics will help you prepare to
connect your directory to IAM Identity Center.

###### Note

If you plan to connect an AWS Managed Microsoft AD directory or a self-managed directory in Active
Directory and you are not using RADIUS MFA with AWS Directory Service, enable MFA in IAM Identity Center.

**AWS Managed Microsoft AD**

1. Review the guidance in [Microsoft AD
   directory](manage-your-identity-source-ad.md "manage-your-identity-source-ad.md").
2. Follow the steps in [Connect a directory in AWS Managed Microsoft AD to IAM Identity Center](connectawsad.md "connectawsad.md").
3. Configure Active Directory to synchronize the user to whom you want to grant
   administrative permissions into IAM Identity Center. For more information, see [Synchronize an administrative user into
   IAM Identity Center](get-started-connect-id-source-ad-idp-specify-user.md#sync-admin-user-from-ad "get-started-connect-id-source-ad-idp-specify-user.md#sync-admin-user-from-ad").
   **Self-managed directory in Active Directory**

4. Review the guidance in [Microsoft AD
   directory](manage-your-identity-source-ad.md "manage-your-identity-source-ad.md").
5. Follow the steps in [Connect a self-managed directory in Active Directory to
   IAM Identity Center](connectonpremad.md "connectonpremad.md").
6. Configure Active Directory to synchronize the user to whom you want to grant
   administrative permissions into IAM Identity Center. For more information, see [Synchronize an administrative user into
   IAM Identity Center](get-started-connect-id-source-ad-idp-specify-user.md#sync-admin-user-from-ad "get-started-connect-id-source-ad-idp-specify-user.md#sync-admin-user-from-ad").
   After you connect your directory to IAM Identity Center, you can specify a user to whom you want to
   grant administrative permissions, and then synchronize that user from your directory into
   IAM Identity Center.

7. Open the [IAM Identity Center
   console](https://console.aws.amazon.com/singlesignon "https://console.aws.amazon.com/singlesignon").
8. Choose **Settings**.
9. On the **Settings** page, choose the **Identity
   source** tab, choose **Actions**, and then choose
   **Manage Sync**.
10. On the **Manage Sync** page, choose the
    **Users** tab, and then choose **Add users and
    groups**.
11. On the **Users** tab, under **User**, enter
    the exact username and choose **Add**.
12. Under **Added Users and Groups**, do the following:
    1. Confirm that the user to whom you want to grant administrative permissions is
       specified.
    2. Select the check box to the left of the username.
    3. Choose **Submit**.

13. In the **Manage sync** page, the user that you specified appears
    in the **Users in sync scope** list.
14. In the navigation pane, choose **Users**.
15. On the **Users** page, it might take some time for the user that
    you specified to appear in the list. Choose the refresh icon to update the list of
    users.
    At this point, your user doesn't have access to the management account. You will set up
    administrative access to this account by creating an administrative permission set
    and assigning the user to that permission set. For more information, see [Create a permission set](howtocreatepermissionset.md "howtocreatepermissionset.md").
