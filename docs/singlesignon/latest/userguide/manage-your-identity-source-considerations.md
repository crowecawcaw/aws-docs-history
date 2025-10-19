# Considerations for changing
 your identity source

Although you can change your identity source at any time, we recommend that you consider
 how this change might affect your current deployment. 

If you are already managing users and groups in one identity source, changing to a
 different identity source might remove all user and group assignments that you configured in
 IAM Identity Center. If this occurs, all users, including the administrative user in IAM Identity Center, will lose
 single sign-on access to their AWS accounts and applications.

Before you change the identity source for IAM Identity Center, review the following considerations
 before you proceed. If you want to proceed with changing your identity source, see [Change your identity source](manage-your-identity-source-change.md "manage-your-identity-source-change.md") for more information.


## Changing between IAM Identity Center
 directory and Active Directory


If you are already managing users and groups in Active Directory, we recommend that you
 consider connecting your directory when you enable IAM Identity Center and choose your identity
 source. Do this before you create any users and groups in the default Identity Center
 directory and make any assignments. 


###### Important

When changing your identity source type in IAM Identity Center to or from Active Directory be aware that the Identity Store ID will change. This can have the following implications:


* Your default AWS access portal URL will change. You will need to communicate the new URL to your workforce and update bookmarks, gatewall or firewall allow-lists, and configurations where this URL is referenced. We recommend you perform this change in a scheduled maintenance window to minimize disruption to your users.
* If you are using a customer managed KMS key for encryption at rest in IAM Identity Center, and have configured the KMS key policy with the encryption context, be aware that the encryption context for the Identity Store will change. For instance, in the Identity Store ARN "arn:aws:identitystore::123456789012:identitystore/d-922763e9b3", "d-922763e9b3" is the Identity Store ID. To prevent service disruption during this transition, temporarily modify your KMS key policy to use a wildcard pattern: "arn:aws:identitystore::123456789012:identitystore/\*".

If you are already managing users and groups in the default Identity Center directory,
 consider the following:



* Assignments removed and users and groups
 deleted – Changing your identity source to Active Directory
 deletes your users and groups from the Identity Center directory. This change also
 removes your assignments. In this case, after you change to Active Directory,
 you must synchronize your users and groups from Active Directory into the
 Identity Center directory, and then reapply their assignments.


If you choose to not use Active Directory, you must create your users and
 groups in the Identity Center directory, and then make assignments.
* Assignments aren't deleted when identities are
 deleted – When identities are deleted in the Identity Center
 directory, corresponding assignments also get deleted in IAM Identity Center. However in
 Active Directory, when identities are deleted (either in Active Directory or the
 synced identities), corresponding assignments aren't deleted.
* No outbound synchronization for APIs –
 If you use Active Directory as your identity source, we recommend that you use
 the [Create, Update,
 and Delete](../APIReference/API_Operations.md "../APIReference/API_Operations.md") APIs with caution. IAM Identity Center doesn't support outbound
 synchronization, so your identity source doesn't automatically update with the
 changes that you make to users or groups using these APIs.
* Access portal URL will change – Changing
 your identity source between IAM Identity Center and Active Directory also changes the URL for
 the AWS access portal.
* If users are deleted or disabled in the IAM Identity Center console using Identity Store APIs,
 users with active sessions can continue to access integrated applications and
 accounts. For information about authentication session duration
 and user behavior, see [Understanding authentication sessions in IAM Identity Center](authconcept.md "authconcept.md").

For information about how IAM Identity Center provisions users and groups, see [Microsoft AD
 directory](manage-your-identity-source-ad.md "manage-your-identity-source-ad.md").


## Changing from IAM Identity Center to an external
 IdP


If you change your identity source from IAM Identity Center to an external identity provider (IdP),
 consider the following: 



* Assignments and memberships work with correct
 assertions – your user assignments, group assignments, and
 group memberships continue to work as long as the new IdP sends the correct
 assertions (for example, SAML nameIDs). These assertions must match the user
 names and groups in IAM Identity Center.
* No outbound synchronization – IAM Identity Center
 doesn't support outbound synchronization, so your external IdP will not
 automatically update with changes to users and groups that you make in IAM Identity Center.
* SCIM provisioning – if you are using
 SCIM provisioning, changes to users and groups in your identity provider reflect
 only in IAM Identity Center after your identity provider sends those changes to IAM Identity Center. See
 [Considerations for using automatic
 provisioning](provision-automatically.md#auto-provisioning-considerations "provision-automatically.md#auto-provisioning-considerations").
* Rollback – you can revert your identity
 source back to using IAM Identity Center at any time. See [Changing from an external IdP to
 IAM Identity Center](#changing-from-idp-and-idc "#changing-from-idp-and-idc").
* Existing user sessions are revoked on session duration
 expiry – Once you change your identity source to an external
 identity provider, active user sessions persist for the remainder of the maximum
 session duration configured in the console. For example, if the AWS access portal
 session duration is set to eight hours, and you changed the identity source in
 the fourth hour, active user sessions persist for an additional four hours. To
 revoke user sessions, see [View and end active sessions for your workforce users](end-active-sessions.md "end-active-sessions.md").


If users are deleted or disabled in the IAM Identity Center console using Identity Store APIs,
 users with active sessions can continue to access integrated applications and
 accounts. For information about authentication session duration
 and user behavior, see [Understanding authentication sessions in IAM Identity Center](authconcept.md "authconcept.md").


###### Note

You cannot revoke user sessions from the IAM Identity Center console after
 you've deleted the user.

For information about how IAM Identity Center provisions users and groups, see [External identity providers](manage-your-identity-source-idp.md "manage-your-identity-source-idp.md").


## Changing from an external IdP to
 IAM Identity Center


If you change your identity source from an external identity provider (IdP) to IAM Identity Center,
 consider the following: 



* IAM Identity Center preserves all your assignments.
* Force password reset – Users who had
 passwords in IAM Identity Center can continue signing in with their old passwords. For users
 who were in the external IdP and weren't in IAM Identity Center, an administrator must force a
 password reset.
* Existing user sessions are revoked on session duration
 expiry – Once you change your identity source to IAM Identity Center,
 active user sessions persist for the remaining duration of the maximum session
 duration configured in the console. For example, if the AWS access portal session
 duration is eight hours, and you changed the identity source at the fourth hour,
 active user sessions continue to run for an additional four hours. To revoke
 user sessions, see [View and end active sessions for your workforce users](end-active-sessions.md "end-active-sessions.md"). 


If users are deleted or disabled in the IAM Identity Center console using Identity Store APIs,
 users with active sessions can continue to access integrated applications and
 accounts. For information about authentication session duration
 and user behavior, see [Understanding authentication sessions in IAM Identity Center](authconcept.md "authconcept.md").


###### Note

You will not be able to revoke user sessions from the IAM Identity Center console after
 you've deleted the user.

For information about how IAM Identity Center provisions users and groups, see [Manage users in the Identity Center directory](manage-your-identity-source-sso.md "manage-your-identity-source-sso.md").


## Changing from one external IdP to
 another external IdP


If you are already using an external IdP as your identity source for IAM Identity Center and you
 change to a different external IdP, consider the following:



* Assignments and memberships work with correct
 assertions – IAM Identity Center preserves all of your assignments. The
 user assignments, group assignments, and group memberships continue to work as
 long as the new IdP sends the correct assertions (for example, SAML nameIDs). 


 These assertions must match the user names in IAM Identity Center when your users
 authenticate through the new external IdP.
* SCIM provisioning – If you are using
 SCIM for provisioning into IAM Identity Center, we recommend that you review the IdP-specific
 information in this guide and the documentation provided by the IdP to ensure
 that the new provider matches users and groups correctly when SCIM is enabled.
* Existing user sessions are revoked on session duration
 expiry – Once you change your identity source to different
 external identity provider, active user sessions persist for the remaining
 duration of the maximum session duration configured in the console. For example,
 if the AWS access portal session duration is eight hours, and you changed the identity
 source at the fourth hour, active user sessions persist for an additional four
 hours. To revoke user sessions, see [View and end active sessions for your workforce users](end-active-sessions.md "end-active-sessions.md"). 


If users are deleted or disabled in the IAM Identity Center console using Identity Store APIs,
 users with active sessions can continue to access integrated applications and
 accounts. For information about authentication session duration
 and user behavior, see [Understanding authentication sessions in IAM Identity Center](authconcept.md "authconcept.md").


###### Note

You cannot revoke user sessions from the IAM Identity Center console after
 you've deleted the user.

For information about how IAM Identity Center provisions users and groups, see [External identity providers](manage-your-identity-source-idp.md "manage-your-identity-source-idp.md").


## Changing
 between Active Directory and an external IdP


If you change your identity source from an external IdP to Active Directory, or from
 Active Directory to an external IdP, consider the following:



* Users, groups, and assignments are deleted
 – All users, groups, and assignments are deleted from IAM Identity Center. No user or
 group information is affected in either the external IdP or Active Directory.
* Provisioning users – If you change to an
 external IdP, you must configure IAM Identity Center to provision your users. Alternatively,
 you must manually provision the users and groups for the external IdP before you
 can configure assignments.
* Create assignments and groups – If you
 change to Active Directory, you must create assignments with the users and
 groups that are in your directory in Active Directory.
* If users are deleted or disabled in the IAM Identity Center console using Identity Store APIs,
 users with active sessions can continue to access integrated applications and
 accounts. For information about authentication session duration
 and user behavior, see [Understanding authentication sessions in IAM Identity Center](authconcept.md "authconcept.md").

For information about how IAM Identity Center provisions users and groups, see [Microsoft AD
 directory](manage-your-identity-source-ad.md "manage-your-identity-source-ad.md").
