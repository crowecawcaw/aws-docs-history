# Provision users and groups from an external identity provider using SCIM

IAM Identity Center supports automatic provisioning (synchronization) of user and group information
 from your identity provider (IdP) into IAM Identity Center using the System for Cross-domain Identity
 Management (SCIM) v2.0 protocol. When you configure SCIM synchronization, you create a
 mapping of your identity provider (IdP) user attributes to the named attributes in IAM Identity Center.
 This causes the expected attributes to match between IAM Identity Center and your IdP. You configure this
 connection in your IdP using your SCIM endpoint for IAM Identity Center and a bearer token that you create
 in IAM Identity Center.

###### Topics

* [Considerations for using automatic
 provisioning](#auto-provisioning-considerations "#auto-provisioning-considerations")
* [How to monitor access token expiry](#access-token-expiry "#access-token-expiry")
* [Generate an access token](generate-token.md "generate-token.md")
* [Enable automatic provisioning](how-to-with-scim.md "how-to-with-scim.md")
* [Delete an access token](delete-token.md "delete-token.md")
* [Disable automatic provisioning](disable-provisioning.md "disable-provisioning.md")
* [Rotate an access token](rotate-token.md "rotate-token.md")
* [Manual provisioning](#provision-manually "#provision-manually")

## Considerations for using automatic
 provisioning


Before you begin deploying SCIM, we recommend that you first review the following
 important considerations about how it works with IAM Identity Center. For additional provisioning
 considerations, see the [IAM Identity Center identity source tutorials](tutorials.md "tutorials.md") applicable
 to your IdP.



* If you are provisioning a primary email address, this attribute value must be
 unique for each user. In some IdPs, the primary email address might not be a real
 email address. For example, it might be a Universal Principal Name (UPN) that only
 looks like an email. These IdPs may have a secondary or “other” email address that
 contains the user’s real email address. You must configure SCIM in your IdP to map the
 non-Null unique email address to the IAM Identity Center primary email address attribute. And you
 must map the users non-Null unique sign-in identifier to the IAM Identity Center user name
 attribute. Check to see whether your IdP has a single value that is both the sign-in
 identifier and the user’s email name. If so, you can map that IdP field to both the
 IAM Identity Center primary email and the IAM Identity Center user name.
* For SCIM synchronization to work, every user must have a **First
 name**, **Last name**, **Username** and
 **Display name** value specified. If any of these values are
 missing from a user, that user will not be provisioned.
* If you need to use third-party applications, you will first need to map the
 outbound SAML subject attribute to the user name attribute. If the third-party
 application needs a routable email address, you must provide the email attribute to
 your IdP.
* SCIM provisioning and update intervals are controlled by your identity provider.
 Changes to users and groups in your identity provider are only reflected in IAM Identity Center
 after your identity provider sends those changes to IAM Identity Center. Check with your identity
 provider for details on the frequency of user and group updates.
* Currently, multivalue attributes (such as multiple emails or phone numbers for a
 given user) are not provisioned with SCIM. Attempts to synchronize multivalue
 attributes into IAM Identity Center with SCIM will fail. To avoid failures, ensure that only a
 single value is passed for each attribute. If you have users with multivalue
 attributes, remove or modify the duplicate attribute mappings in SCIM at your IdP for
 the connection to IAM Identity Center.
* Verify that the `externalId` SCIM mapping at your IdP corresponds to a
 value that is unique, always present, and least likely to change for your users. For
 example, your IdP might provide a guaranteed `objectId` or other identifier
 that’s not affected by changes to user attributes like name and email. If so, you can
 map that value to the SCIM `externalId` field. This ensures that your users
 won’t lose AWS entitlements, assignments, or permissions if you need to change their
 name or email.
* Users who have not yet been assigned to an application or AWS account cannot be
 provisioned into IAM Identity Center. To synchronize users and groups, make sure that they are
 assigned to the application or other setup that represents your IdP’s connection to
 IAM Identity Center.
* User deprovisioning behavior is managed by the identity provider and may vary by
 their implementation. Check with your identity provider for details on user
 deprovisioning.
* After setting up automatic provisioning with SCIM for your IdP, you can no longer
 add or edit users in the IAM Identity Center console. If you need to add or modify a user, you must
 do so from your external IdP or identity source.

For more information about IAM Identity Center’s SCIM implementation, see the [IAM Identity Center SCIM Implementation Developer Guide](../developerguide/what-is-scim.md "../developerguide/what-is-scim.md").


## How to monitor access token expiry


SCIM access tokens are generated with a validity of one year. When your SCIM access
 token is set to expire in 90 days or less, AWS sends you reminders in the IAM Identity Center console
 and over the AWS Health Dashboard to help you rotate the token. By rotating the SCIM
 access token before it expires, you continually secure automatic provisioning of user and
 group information. If the SCIM access token expires, the synchronization of user and group
 information from your identity provider into IAM Identity Center stops, so automatic provisioning can no
 longer make updates or create and delete information. Disruption to automatic provisioning
 may impose increased security risks and impact access to your services.


The Identity Center console reminders persist until you rotate the SCIM access token and
 delete any unused or expired access tokens. The AWS Health Dashboard events are
 renewed weekly between 90 to 60 days, twice per week from 60 to 30 days, three times per
 week from 30 to 15 days, and daily from 15 days until the SCIM access tokens expires.
 


## Manual provisioning


Some IdPs do not have System for Cross-domain Identity Management (SCIM) support or
 have an incompatible SCIM implementation. In those cases, you can manually provision users
 through the IAM Identity Center console. When you add users to IAM Identity Center, ensure that you set the user name
 to be identical to the user name that you have in your IdP. At a minimum, you must have a
 unique email address and user name. For more information, see [Username and email address uniqueness](users-groups-provisioning.md#username-email-unique "users-groups-provisioning.md#username-email-unique").


You must also manage all groups manually in IAM Identity Center. To do this, you create the groups
 and add them using the IAM Identity Center console. These groups do not need to match what exists in
 your IdP. For more information, see [Groups](users-groups-provisioning.md#groups-concept "users-groups-provisioning.md#groups-concept").
