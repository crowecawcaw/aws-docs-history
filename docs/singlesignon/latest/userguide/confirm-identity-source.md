# Confirm your identity sources in IAM Identity Center

Your identity source in IAM Identity Center defines where your users and groups are managed. After you
enable IAM Identity Center, confirm that you are using the identity source of your choice. If you already have
an assigned identity source, you can continue to use it.

If you are already managing users and groups in Active Directory or an
external IdP, we recommend that you consider connecting this identity source when you enable
IAM Identity Center and choose your identity source. This should be done before you create any users and
groups in the default Identity Center directory and make any assignments.

If you are already managing users and groups in one identity source in IAM Identity Center, changing to a
different identity source might remove all user and group assignments that you configured in
IAM Identity Center. If this occurs, all users, including the administrative user in IAM Identity Center, will lose single
sign-on access to their AWS accounts and applications. For more information, see [Considerations for changing
your identity source](manage-your-identity-source-considerations.md "manage-your-identity-source-considerations.md").

To confirm your identity source

1. Open the [IAM Identity Center
   console](https://console.aws.amazon.com/singlesignon "https://console.aws.amazon.com/singlesignon").
2. On the **Dashboard** page, below the **Recommended setup
   steps** section, choose **Confirm your identity source**. You can
   also access this page by choosing **Settings** and choosing the
   **Identity source** tab.
3. There is no action if you want to keep your assigned identity source. If you prefer to
   change it, choose **Actions**, and then choose **Change identity
   source**.

You can choose one of the following as your identity source:

**Identity Center directory**

When you enable IAM Identity Center for the first time, it is automatically configured with an
Identity Center directory as your default identity source. If you aren't already using
another external identity provider, you can get started creating your users and groups, and
assign their level of access to your AWS accounts and applications. For a tutorial on
using this identity source, see [Configure user access with the default IAM Identity Center
directory](quick-start-default-idc.md "quick-start-default-idc.md").

**Active Directory**

If you are already managing users and groups in either your AWS Managed Microsoft AD directory using
AWS Directory Service or your self-managed directory in Active Directory (AD), we recommend
that you connect that directory when you enable IAM Identity Center. Don't create any users and groups in
the default Identity Center directory. IAM Identity Center uses the connection provided by the AWS Directory Service
to synchronize user, group, and membership information from your source directory in Active
Directory to the IAM Identity Center identity store. For more information, see [Microsoft AD
directory](manage-your-identity-source-ad.md "manage-your-identity-source-ad.md").

###### Note

IAM Identity Center doesn't support SAMBA4-based Simple AD as an identity source.

**External identity provider**

For external identity providers (IdPs) such as Okta or Microsoft
Entra ID, you can use IAM Identity Center to authenticate identities from the IdPs through the
Security Assertion Markup Language (SAML) 2.0 standard. The SAML protocol doesn't provide a
way to query the IdP to learn about users and groups. You make IAM Identity Center aware of those users
and groups by provisioning them into IAM Identity Center. You can perform automatic provisioning
(synchronization) of user and group information from your IdP into IAM Identity Center using the System
for Cross-domain Identity Management (SCIM) v2.0 protocol if your IdP supports SCIM.
Otherwise, you can manually provision your users and groups by manually entering the user
names, email address, and groups into IAM Identity Center.

For detailed instructions on setting up your identity source, see [IAM Identity Center identity source tutorials](tutorials.md "tutorials.md").

###### Note

If you plan to use an external identity provider, note that the external IdP, not
IAM Identity Center, manages multi-factor authentication (MFA) settings. MFA in IAM Identity Center isn't supported for
use by external identity providers. For more information, see [Prompt users for MFA](mfa-getting-started.md "mfa-getting-started.md").
