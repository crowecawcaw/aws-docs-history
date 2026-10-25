

# Considerations for changing your identity source
<a name="manage-your-identity-source-considerations"></a>

Although you can change your identity source at any time, we recommend that you consider how this change might affect your current deployment. 

Changing your identity source to or from Active Directory behaves differently depending on the direction:
+ When you change from Active Directory to the Identity Center directory or an external identity provider (IdP), IAM Identity Center retains your users, groups, memberships, and assignments.
+ When you change to Active Directory from the Identity Center directory or an external IdP, or between two Active Directory directories, IAM Identity Center removes your users, groups, memberships, and assignments.

When you change between the Identity Center directory and an external IdP, or between two external IdPs, IAM Identity Center preserves your users, groups, memberships, and assignments.

Before you change the identity source for IAM Identity Center, review the following considerations. If you want to proceed with changing your identity source, see [Change your identity source](manage-your-identity-source-change.md) for more information.

## Changing your identity source from Active Directory
<a name="changing-from-active-directory"></a>

IAM Identity Center supports changing your identity source from Active Directory to the Identity Center directory or an external IdP, retaining your users, groups, memberships, and their assignments.

**Important**  
After you change your identity source from Active Directory, the default AWS access portal URL changes. The `https://d-xxxxxxxxxx.awsapps.com/start` URL and any custom alias URL are no longer supported. If you don't update bookmarks, allow-lists, and other references, users and automated systems that use the old URL lose access to the access portal.

### Before you begin
<a name="changing-from-active-directory-before-you-begin"></a>

Before you change your identity source from Active Directory, complete the following tasks:
+ Review the following considerations. Pay attention to potential disruption in sign-in and multi-factor authentication (MFA), and to the change in the portal URL.
+ Back up your configuration. Export your current users, groups, memberships, and assignments so that you can restore them if needed. For more information, see [Managing identity source transition for IAM Identity Center](https://aws.amazon.com/blogs/security/managing-identity-source-transition-for-aws-iam-identity-center/).
+ Validate your configuration in a test environment that mirrors production, including connected applications, before you change production.
+ Confirm that your target identity source is ready. For an external IdP, confirm that it supports System for Cross-domain Identity Management (SCIM) 2.0. Also confirm that it matches existing users and groups by a stable identifier (typically user name), so that it takes over users instead of creating duplicates. Confirm that every user has a user name, given name, family name, and display name populated.
+ Schedule a maintenance window and notify users that the change might interrupt access portal sign-in.

### Considerations
<a name="changing-from-active-directory-considerations"></a>

**User sign-out**  
Users who are signed in are signed out and must sign in again the next time they access or refresh their session.

**MFA**  
MFA behavior depends on your target identity source:  
+ If you change to the Identity Center directory, IAM Identity Center retains your IAM Identity Center MFA settings and user MFA settings.
+ If you change to an external IdP, your external IdP handles MFA.

**Remote Authentication Dial-In User Service (RADIUS) MFA**  
If you use RADIUS MFA through AWS Directory Service, it no longer applies to AWS access portal sign-in after the change.  
To require MFA, turn on MFA in IAM Identity Center. Users must register their MFA devices again.

**AWS access portal URL**  
Your `https://d-xxxxxxxxxx.awsapps.com/start` and custom alias URLs are no longer supported after the change. Your dual-stack URL (`https://ssoins-<instance-id>.portal.<region>.app.aws`) continues to be supported. Communicate the supported URL and update bookmarks and allow-lists.

**Active Directory synchronization**  
IAM Identity Center stops syncing from Active Directory. Your directory in Directory Service remains intact, but it's no longer connected, and changes that you make in Active Directory after this point don't appear in IAM Identity Center.

**New authoritative identity source**  
How you manage identities depends on your target identity source:  
+ If you change to the Identity Center directory, IAM Identity Center becomes the authoritative source. You manage users, groups, and memberships in IAM Identity Center, by using the console or the Identity Store API. Users who are synced from Active Directory don't have an IAM Identity Center password and can't sign in without one. Turn on [Email one-time password](userswithoutpwd.md) so that users created with API or CLI who have no password can choose one at first sign-in.
+ If you change to an external IdP, your external IdP becomes the authoritative source. After the change, connect your IdP and configure SCIM provisioning. You then manage users, groups, and memberships in your IdP, which provisions them into IAM Identity Center. For sign-in to work, the attribute that your IdP sends as the Security Assertion Markup Language (SAML) `NameID` must match the user name in IAM Identity Center.

**Attributes for access control**  
IAM Identity Center keeps your attributes for access control configuration. Review it after the change, because attribute values from Active Directory no longer update.

**Data removal when reversing the change**  
If you later change your identity source to Active Directory, IAM Identity Center permanently removes all users, groups, memberships, and assignments. For more information, see [Changing your identity source to Active Directory](#changing-to-active-directory).

For information about how IAM Identity Center provisions users and groups, see [Microsoft AD directory](manage-your-identity-source-ad.md), [Manage users in the Identity Center directory](manage-your-identity-source-sso.md), or [External identity providers](manage-your-identity-source-idp.md).

**Note**  
Changing your identity source doesn't delete your AWS Managed Microsoft AD instance. Keep it for a few days after the change, until you've validated that all access and permissions work as expected.

## Changing your identity source to Active Directory
<a name="changing-to-active-directory"></a>

When you change your identity source to Active Directory from the Identity Center directory or an external IdP, or between two different Active Directory directories, IAM Identity Center removes your users, groups, memberships, and assignments.

**Warning**  
Changing your identity source to Active Directory permanently deletes all users, groups, memberships, and assignments in IAM Identity Center. This data loss is irreversible. Before you proceed, back up your configuration and reapply assignments after the change.

This change also changes the Identity Store ID, which affects your access portal URL and encryption configuration.

**Important**  
Changing your identity source type to Active Directory changes the Identity Store ID. The change to the Identity Store ID has the following implications:  
Your default AWS access portal URL changes. Communicate the new URL to your workforce and update bookmarks, gateway or firewall allow-lists, and configurations that reference this URL. If you don't update these references, users and automated systems that use the old URL lose access to the access portal.
The encryption context for your customer managed AWS KMS key changes. If you use a customer managed AWS KMS key for encryption at rest, with the encryption context configured in the key policy, the encryption context for the Identity Store changes. For example, in the Identity Store Amazon Resource Name (ARN) `arn:aws:identitystore::444455556666:identitystore/d-922763e9b3`, `d-922763e9b3` is the Identity Store ID. To prevent service disruption, temporarily modify your AWS KMS key policy to use a wildcard pattern: `arn:aws:identitystore::444455556666:identitystore/*`. If you don't update the key policy, encryption and decryption operations fail and service is disrupted.

Consider the following:

**User, group, membership, and assignment deletion**  
IAM Identity Center permanently removes all users, groups, group memberships, and assignments. The change doesn't affect user or group information in the external IdP or Active Directory.

**Rebuild after the change**  
After you change to Active Directory, synchronize your users and groups from Active Directory into IAM Identity Center, and then reapply assignments.

**Assignment retention on identity deletion in Active Directory**  
In Active Directory, when you delete identities (in Active Directory or the synced identities), IAM Identity Center keeps the corresponding assignments. In the Identity Center directory, when you delete identities, IAM Identity Center also deletes their assignments.

**No outbound synchronization for APIs**  
If you use Active Directory as your identity source, use the [Create, Update, and Delete](https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_Operations.html) APIs with caution. If you use these APIs to change users or groups, your identity source doesn't automatically reflect those changes, because IAM Identity Center doesn't support outbound synchronization.

**Multi-Region support**  
Multi-Region support is not available for Active Directory as an identity source. If you have replicated IAM Identity Center to additional Regions or plan to, you must use an external identity provider or the Identity Center directory. For more information, see [Using IAM Identity Center across multiple AWS Regions](multi-region-iam-identity-center.md).

For information about how IAM Identity Center provisions users and groups, see [Microsoft AD directory](manage-your-identity-source-ad.md).

## Changing from IAM Identity Center to an external IdP
<a name="changing-from-idc-and-idp"></a>

If you change your identity source from IAM Identity Center to an external identity provider (IdP), consider the following: 
+ **Assignments and memberships work with correct assertions** – your user assignments, group assignments, and group memberships continue to work as long as the new IdP sends the correct assertions (for example, SAML nameIDs). These assertions must match the user names and groups in IAM Identity Center.
+ **No outbound synchronization** – IAM Identity Center doesn't support outbound synchronization, so your external IdP will not automatically update with changes to users and groups that you make in IAM Identity Center. 
+ **SCIM provisioning** – if you are using SCIM provisioning, changes to users and groups in your identity provider reflect only in IAM Identity Center after your identity provider sends those changes to IAM Identity Center. See [Considerations for using automatic provisioning](provision-automatically.md#auto-provisioning-considerations).
+ **Rollback** – you can revert your identity source back to using IAM Identity Center at any time. See [Changing from an external IdP to IAM Identity Center](#changing-from-idp-and-idc).
+ **Existing user sessions are revoked on session duration expiry** – Once you change your identity source to an external identity provider, active user sessions persist for the remainder of the maximum session duration configured in the console. For example, if the AWS access portal session duration is set to eight hours, and you changed the identity source in the fourth hour, active user sessions persist for an additional four hours. To revoke user sessions, see [View and end active sessions for your workforce users](end-active-sessions.md).

  If users are deleted or disabled in the IAM Identity Center console using Identity Store APIs, users with active sessions can continue to access integrated applications and accounts. For information about authentication session duration and user behavior, see [Understanding authentication sessions in IAM Identity Center](authconcept.md).
**Note**  
You cannot revoke user sessions from the IAM Identity Center console after you've deleted the user.

For information about how IAM Identity Center provisions users and groups, see [External identity providers](manage-your-identity-source-idp.md).

## Changing from an external IdP to IAM Identity Center
<a name="changing-from-idp-and-idc"></a>

If you change your identity source from an external identity provider (IdP) to IAM Identity Center, consider the following: 
+ IAM Identity Center preserves all your assignments.
+ **Force password reset** – Users who had passwords in IAM Identity Center can continue signing in with their old passwords. For users who were in the external IdP and weren't in IAM Identity Center, an administrator must force a password reset. 
+ **Existing user sessions are revoked on session duration expiry** – Once you change your identity source to IAM Identity Center, active user sessions persist for the remaining duration of the maximum session duration configured in the console. For example, if the AWS access portal session duration is eight hours, and you changed the identity source at the fourth hour, active user sessions continue to run for an additional four hours. To revoke user sessions, see [View and end active sessions for your workforce users](end-active-sessions.md). 

  If users are deleted or disabled in the IAM Identity Center console using Identity Store APIs, users with active sessions can continue to access integrated applications and accounts. For information about authentication session duration and user behavior, see [Understanding authentication sessions in IAM Identity Center](authconcept.md).
**Note**  
You will not be able to revoke user sessions from the IAM Identity Center console after you've deleted the user.

For information about how IAM Identity Center provisions users and groups, see [Manage users in the Identity Center directory](manage-your-identity-source-sso.md).

## Changing from one external IdP to another external IdP
<a name="changing-from-one-idp-to-another-idp"></a>

If you are already using an external IdP as your identity source for IAM Identity Center and you change to a different external IdP, consider the following:
+ **Assignments and memberships work with correct assertions** – IAM Identity Center preserves all of your assignments. The user assignments, group assignments, and group memberships continue to work as long as the new IdP sends the correct assertions (for example, SAML nameIDs). 

   These assertions must match the user names in IAM Identity Center when your users authenticate through the new external IdP. 
+ **SCIM provisioning** – If you are using SCIM for provisioning into IAM Identity Center, we recommend that you review the IdP-specific information in this guide and the documentation provided by the IdP to ensure that the new provider matches users and groups correctly when SCIM is enabled. 
+ **Existing user sessions are revoked on session duration expiry** – Once you change your identity source to different external identity provider, active user sessions persist for the remaining duration of the maximum session duration configured in the console. For example, if the AWS access portal session duration is eight hours, and you changed the identity source at the fourth hour, active user sessions persist for an additional four hours. To revoke user sessions, see [View and end active sessions for your workforce users](end-active-sessions.md). 

  If users are deleted or disabled in the IAM Identity Center console using Identity Store APIs, users with active sessions can continue to access integrated applications and accounts. For information about authentication session duration and user behavior, see [Understanding authentication sessions in IAM Identity Center](authconcept.md).
**Note**  
You cannot revoke user sessions from the IAM Identity Center console after you've deleted the user.

For information about how IAM Identity Center provisions users and groups, see [External identity providers](manage-your-identity-source-idp.md).