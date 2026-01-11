# Troubleshooting IAM Identity Center issues

The following can help you troubleshoot some common issues you might encounter while setting
up or using the IAM Identity Center console.

## Issues creating an account instance of IAM Identity Center

Several restrictions might apply when creating an account instance of IAM Identity Center. If you are
unable to create an account instance through the IAM Identity Center console, or the setup experience of a
supported AWS managed application, verify the following use cases:

- Check other AWS Regions in the AWS account in which you are attempting to create
  the account instance. You are limited to one instance of IAM Identity Center per AWS account. To
  enable the application, either switch to the AWS Region with the instance of IAM Identity Center or
  switch to an account without an instance of IAM Identity Center.
- If your organization enabled IAM Identity Center before September 14, 2023, your administrator might
  need to opt-in to account instance creation. Work with your administrator to enable
  account instance creation from the IAM Identity Center console in the management account.
- Your administrator might have created a Service Control Policy to limit creation of
  account instances of IAM Identity Center. Work with your administrator add your account to the allow
  list.

## You receive an error when you attempt to

view the list of cloud applications that are preconfigured to work with IAM Identity Center

This following error occurs when you have a policy that allows
`sso:ListApplications` but not other IAM Identity Center APIs. Update your policy to address
this error.

The `ListApplications` permission authorizes multiple APIs:

- The `ListApplications` API.
- An internal API similar to the `ListApplicationProviders` API used in the
  IAM Identity Center console.

To help resolve duplication, the internal API now also authorizes using the
`ListApplicationProviders` action. To allow the public
`ListApplications` API but deny the internal API, your policy must include a
statement denying the `ListApplicationProviders` action:

```

      "Statement": [
    {
         "Effect": "Deny",
         "Action": "sso:ListApplicationProviders",
         "Resource": "*"
    },
    {
        "Effect": "Allow",
        "Action": "sso:ListApplications",
        "Resource": "`<instanceArn>`" // (or "*" for all instances)
    }
]

```

To allow the internal API but deny `ListApplications`, the policy needs to
allow only `ListApplicationProviders`. The `ListApplications` API is
denied if not explicitly allowed.

```

      "Statement": [
    {
         "Effect": "Allow",
         "Action": "sso:ListApplicationProviders",
         "Resource": "*"
    }
]

```

When your policies are updated, contact Support to have this proactive measure removed.

## Issues regarding contents of SAML assertions created by IAM Identity Center

IAM Identity Center provides a web-based debug experience for the SAML assertions created and sent by
IAM Identity Center, including attributes within these assertions, when accessing AWS accounts and SAML
applications from the AWS access portal. To see the details of a SAML assertion that IAM Identity Center
generates, use the following steps.

1. Sign in to the AWS access portal.
2. While you are signed into the portal, hold the **Shift** key down,
   choose the application tile, and then release the **Shift** key.
3. Examine the information on the page titled **You are now in
   administrator mode**. To keep this information for future reference, choose
   **Copy XML**, and paste the contents elsewhere.
4. Choose **Send to <application>** to continue. This
   option sends the assertion to the service provider.

###### Note

Some browser configurations and operating systems may not support this procedure. This
procedure has been tested on Windows 10 using Firefox, Chrome, and Edge browsers.

## Specific users fail to synchronize into IAM Identity Center from an external SCIM

provider

If your Identity Provider (IdP) is configured to provision users into IAM Identity Center using SCIM
synchronization, you may encounter synchronization failures during the user provisioning
process. This may indicate that the user configuration in your IdP is not compatible with the
IAM Identity Center requirements. When this happens, the IAM Identity Center SCIM APIs will return error messages that
provide insights into the root cause of the issue. You can locate these error messages in your
IdP's logs or UI. Alternatively, you may find more detailed information about the provisioning
failures in the [AWS CloudTrail
logs](../../../awscloudtrail/latest/userguide/tutorial-event-history.md "../../../awscloudtrail/latest/userguide/tutorial-event-history.md").

For more information on the IAM Identity Center SCIM implementations, including the specifications of
required, optional, and unsupported parameters and operations for user objects, see [IAM Identity Center
SCIM Implementation Developer Guide](../developerguide/what-is-scim.md "../developerguide/what-is-scim.md") in the _SCIM Developer
Guide_

The following are a couple of common reasons for this error:

1. The user object in the IdP lacks a first (given) name, a last (family) name, and/or a
   display name.

**Error Message:**
**`"2 validation errors detected: Value at
 `'name.givenName'`failed to satisfy constraint: Member must
 satisfy regular expression pattern: [\\p{L}\\p{M}\\p{S}\\p{N}\\p{P}\\t\\n\\r ]+; Value
 at`'name.givenName'` failed to satisfy constraint: Member must
 have length greater than or equal to 1"`**

    1. **Solution:** Add a first (given), last (family), and
     display name for the user object. In addition, ensure that the SCIM provisioning
     mappings for user objects at your IdP are configured to send nonempty values for all
     of these attributes.

2. More than one value for a single attribute is being sent for the user (also known as
   “multi-value attributes”). For example, the user may have both a work and a home phone
   number specified in the IdP, or multiple emails or physical addresses, and your IdP is
   configured to try to synchronize multiple or all values for that attribute.

**Error Message:**
**`"List attribute `emails` exceeds allowed limit of
 1"`**

    1. **Solution options:**


    	1. Update your SCIM provisioning mappings for user objects at your IdP to send
    	 only a single value for a given attribute. For example, configure a mapping that
    	 sends only the work phone number for each user.
    	2. If the additional attributes can safely be removed from the user object at the
    	 IdP, you can remove the additional values, leaving either one or zero values set
    	 for that attribute for the user.
    	3. If the attribute is not needed for any actions in AWS, remove the mapping
    	 for that attribute from the SCIM provisioning mappings for user objects at your
    	 IdP.

3. Your IdP is trying to match users in the target (IAM Identity Center, in this case) based on
   multiple attributes. Since user names are guaranteed unique within a given IAM Identity Center instance,
   you only need to specify `username` as the attribute used for matching.
   1. **Solution:** Ensure that your SCIM configuration in
      your IdP is using only a single attribute for matching with users in IAM Identity Center. For
      example, mapping `username` or `userPrincipalName` in the IdP to
      the `userName` attribute in SCIM for provisioning to IAM Identity Center will be correct
      and sufficient for most implementations.

## Duplicate user or group error when provisioning

users or groups with an external identity provider

If you experience IAM Identity Center synchronization issues when provisioning users or groups in an
external identity provider (IdP), it could be due to your external IdP users or groups not
having unique attribute values. You may receive the following error messages in your external
IdP:

**`Refused to create a new, duplicate resource`**

You can experience this problem in the following scenarios:

- **Scenario 1**
  - You're using customized non-unique attributes in your external IdP for
    attributes that must be unique in IAM Identity Center. Existing IAM Identity Center users or groups fail to
    synchronize to your IdP.

- **Scenario 2**
  - You attempt to create users that have duplicate attributes for attributes that
    must be unique in IAM Identity Center.
    - For example, you create or have an existing IAM Identity Center user with the following
      attributes:
      - **Username:** Jane Doe
      - **Primary Email
        Address:**
        `jane_doe@example.com`

    - Then you attempt to create another user in your external IdP with the
      following attributes:
      - **Username:** Richard Doe
      - **Primary Email
        Address:**
        `jane_doe@example.com`

            + The external IdP attempts to synchronize and create the user in IAM Identity Center.
             However, these actions fail as both users have duplicate values for a
             primary email address which must be unique.

The username, primary email address, and externalID must be unique in order for your external
IdP users to successfully synchronize to IAM Identity Center. Similarly, the group name must
be unique for your external IdP groups to successfully synchronize to IAM Identity Center.

The solution is to review your identity source's attributes and ensure they are unique.

## Users can’t sign in when their user name is in UPN format

Users might not be able to sign in to the AWS access portal based on the format they use to
enter in their user name on the sign in page. For the most part, users can sign in to the user
portal using either their plain user name, their down-level logon name (DOMAIN\UserName) or
their UPN logon name (`UserName@Corp.Example.com`). The exception to this is when
IAM Identity Center is using a connected directory that has been enabled with MFA and the verification mode
has been set to either **Context-aware** or **Always-on**. In this scenario, users must sign in with their down-level logon name
(DOMAIN\UserName). For more information, see [MFA for Identity Center directory
users](enable-mfa.md "enable-mfa.md"). For general information about user name formats used to sign
in to Active Directory, see [User Name
Formats](https://docs.microsoft.com/en-us/windows/desktop/secauthn/user-name-formats "https://docs.microsoft.com/en-us/windows/desktop/secauthn/user-name-formats") on the Microsoft documentation website.

## I get a ‘Cannot perform the operation on the protected role' error

when modifying an IAM role

When reviewing IAM Roles in an account, you may notice role names beginning with
‘AWSReservedSSO\_’. These are the roles which the IAM Identity Center service has created in the account, and
they came from assigning a permission set to the account. Attempting to modify these roles
from within the IAM console will result in the following error:

```
'Cannot perform the operation on the protected role 'AWSReservedSSO_`RoleName_Here`' - this role is only modifiable by AWS'
```

These roles can only be modified from the IAM Identity Center Administrator console, which is in the
management account of AWS Organizations. Once modified, you can then push the changes down to the AWS
accounts that it is assigned to.

## Directory users cannot reset their password

When a directory user resets their password using the **Forgot
Password?** option during sign-in of the AWS access portal, their new password must
adhere to the default password policy as described in [Password requirements when managing identities
in IAM Identity Center](password-requirements.md "password-requirements.md").

If a user enters a password that adheres to the policy and then receives the error
`We couldn't update your password`, check to see if AWS CloudTrail recorded the
failure. This can be done by searching in the Event History console of CloudTrail using the
following filter:

```
"UpdatePassword"
```

If the message states the following, then you may need to contact support:

```
"errorCode": "InternalFailure",
      "errorMessage": "An unknown error occurred“
```

Another possible cause of this issue is in the naming convention that was applied to the
user name value. Naming conventions must follow specific patterns such as 'surname.givenName'.
However, some user names can be quite long, or contain special characters, and this can cause
characters to be dropped in the API call, thereby resulting in an error. You may want to
attempt a password reset with a test user in the same manner to verify if this is the
case.

If the issue persists, contact the [AWS Support Center](https://console.aws.amazon.com/support/home#/ "https://console.aws.amazon.com/support/home#/").

## My user is referenced in a permission set but can’t access the

assigned accounts or applications

This issue can occur if you’re using System for Cross-domain Identity Management (SCIM)
for Automatic Provisioning with an external identity provider. Specifically, when a user, or
the group the user was a member of, is deleted then re-created using the same user name (for
users) or name (for groups) in the identity provider, a new unique internal identifier is
created for the new user or group in IAM Identity Center. However, IAM Identity Center still has a reference to the old
identifier in its permission database, such that the name of the user or group still appears
in the UI, but access fails. This is because the underlying user or group ID to which the UI
refers no longer exists.

To restore AWS account access in this case, you can remove access for the old user or
group from the AWS account(s) where it was originally assigned, and then reassign access
back to the user or group. This updates the permission set with the correct identifier for the
new user or group. Similarly, to restore application access, you can remove access for the
user or group from the assigned users list for that application, then add the user or group
back again.

You can also check to see if AWS CloudTrail recorded the failure by searching your CloudTrail logs for
SCIM synchronization events that reference the name of the user or group in question.

## I cannot get my application from the application catalog configured

correctly

If you added an application from the application catalog in IAM Identity Center, be aware that each
service provider provides their own detailed documentation. You can access this information
from the **Configuration** tab for the application in the IAM Identity Center
console.

If the problem is related to setting up the trust between the service provider's
application and IAM Identity Center, make sure to check the instruction manual for troubleshooting
steps.

## Error 'An unexpected error has occurred' when a user tries to sign in

using an external identity provider

This error may occur for multiple reasons, but one common reason is a mis-match between
the user information carried in the SAML request, and the information for the user in
IAM Identity Center.

In order for an IAM Identity Center user to sign in successfully when using an external IdP as the
identity source, the following must be true:

- The SAML nameID format (configured at your identity provider) must be ‘email’
- The nameID value must be a properly (RFC2822)-formatted string
  (user@domain.com)
- The nameID value must exactly match the user name of an existing user in IAM Identity Center (it
  doesn’t matter if the email address in IAM Identity Center matches or not – the inbound match is based
  on username)
- The IAM Identity Center implementation of SAML 2.0 federation supports only 1 assertion in the SAML
  response between the identity provider and IAM Identity Center. It does not support encrypted SAML
  assertions.
- The following statements apply if [Attributes for access control](attributesforaccesscontrol.md "attributesforaccesscontrol.md") is enabled in your IAM Identity Center account:
  - The number of attributes mapped in the SAML request must be 50 or less.
  - The SAML request must not contain multi-valued attributes.
  - The SAML request must not contain multiple attributes with the same name.
  - The attribute must not contain structured XML as the value.
  - The Name format must be a SAML specified format, not generic format.

###### Note

IAM Identity Center does not perform “just in time” creation of users or groups for new users or
groups via SAML federation. This means that the user must be pre-created in IAM Identity Center, either
manually or via automatic provisioning, in order to sign in to IAM Identity Center.

This error can also occur when the Assertion Consumer Service (ACS) endpoint configured in
your identity provider does not match the ACS URL provided by your IAM Identity Center instance. Ensure that
these two values match exactly.

Additionally, you can troubleshoot external identity provider sign-in failures further by
going to AWS CloudTrail and filtering on the event name
**ExternalIdPDirectoryLogin**.

## Error 'Attributes for access control failed to enable'

This error may occur if the user enabling ABAC does not have the
`iam:UpdateAssumeRolePolicy` permissions required to enable [Attributes for access control](attributesforaccesscontrol.md "attributesforaccesscontrol.md").

## I get a 'Browser not supported' message when I attempt to register a

device for MFA

WebAuthn is currently supported in Google Chrome, Mozilla Firefox, Microsoft Edge and
Apple Safari web browsers, as well as Windows 10 and Android platforms. Some components of
WebAuthn support may be varied, such as platform authenticator support across macOS and iOS
browsers. If users attempt to register WebAuthn devices on an unsupported browser or platform,
they will see certain options greyed out that are not supported, or they will receive an error
that all supported methods are not supported. In these cases, please refer to [FIDO2: Web
Authentication (WebAuthn)](https://fidoalliance.org/fido2/fido2-web-authentication-webauthn/ "https://fidoalliance.org/fido2/fido2-web-authentication-webauthn/") for more information about browser/platform support. For
more information about WebAuthn in IAM Identity Center, see [FIDO2 authenticators](mfa-types.md#mfa-types-fido2 "mfa-types.md#mfa-types-fido2").

## Active Directory “Domain Users” group does not properly sync into

IAM Identity Center

The Active Directory Domain Users group is the default “primary group” for AD user
objects. Active Directory primary groups and their memberships cannot be read by IAM Identity Center. When
assigning access to IAM Identity Center resources or applications, use groups other than the Domain Users
group (or other groups assigned as primary groups) to have group membership properly reflected
in the IAM Identity Center identity store.

## Invalid MFA credentials error

This error can occur when a user attempts to sign in to IAM Identity Center using an account from an
external identity provider (for example, Okta or Microsoft Entra
ID) before their account is fully provisioned to IAM Identity Center using the SCIM protocol.
After the user account is provisioned to IAM Identity Center, this issue should be resolved. Confirm that
the account has been provisioned to IAM Identity Center. If not, check the provisioning logs in the external
identity provider.

## I get a 'An unexpected error has occurred' message when I attempt to

register or sign in using an authenticator app

Time-based one-time password (TOTP) systems, such as those used by IAM Identity Center in combination
with code-based authenticator apps, rely on time synchronization between the client and the
server. Ensure that the device where your authenticator app is installed is correctly
synchronized to a reliable time source, or manually set the time on your device to match a
reliable source, such as NIST ([https://www.time.gov/](https://www.time.gov/ "https://www.time.gov/")) or other local/regional equivalents.

## I get an 'It's not you, it is us' error when attempting to sign in to IAM Identity Center

This error indicates there is a setup problem with your instance of IAM Identity Center or the external
identity provider (IdP) IAM Identity Center is using as its identity source. We recommend you verify the
following:

- Verify the date and time settings on the device you are using to sign in. We recommend
  that you set the date and time to be set automatically. If that is not available, we
  recommend syncing your date and time to a known Network Time Protocol (NTP) server.
- Verify that the IdP certificate uploaded to IAM Identity Center is the same as what was provided by
  your IdP. You can check the certificate from the IAM Identity Center console by navigating to
  **Settings**. In the **Identity Source** tab choose
  **Action** and then choose **Manage Authentication**.
  If the IdP and IAM Identity Center certificates do not match, import a new certificate to IAM Identity Center.
- Ensure the NameID format in your identity provider's metadata file is the following:
  - `urn:oasis:name:tc:SAML:1.1:nameid-format:emailAddress`

- If you are using AD Connector from AWS Directory Service as your identity provider, verify that
  the credentials for the service account are correct and have not expired. See [Update your
  AD Connector service account credentials in AWS Directory Service](../../../directoryservice/latest/admin-guide/ad_connector_update_creds.md "../../../directoryservice/latest/admin-guide/ad_connector_update_creds.md") for more
  information.

## My users are not receiving emails from IAM Identity Center

All emails sent by the IAM Identity Center service will come from either the address
`no-reply@signin.aws` or `no-reply@login.awsapps.com`. Your mail
system must be configured so that it accepts emails from these sender email addresses and
doesn't handle them as junk or spam.

## Error: You cannot delete/modify/remove/assign access to permission

sets provisioned in the management account

This message indicates that the [Delegated administration](delegated-admin.md "delegated-admin.md") feature has been enabled and that the operation you
previously attempted can only be successfully performed by someone who has management account
permissions in AWS Organizations. To resolve this issue, sign in as a user who has these permissions
and try performing the task again or assign this task to someone who has the correct
permissions. For more information, see [Register a member account](delegated-admin-how-to-register.md "delegated-admin-how-to-register.md").

## Error: Session token not found or invalid

This error can occur when a client, such as a web browser, AWS Toolkit, or
AWS CLI, tries to use a session that is revoked or invalidated on the server side. To correct
this issue, return to the client application or website and try again, including logging in
again if prompted. This might sometimes require you to also cancel pending requests, such as a
pending connection attempt from the AWS Toolkit within your IDE.

## Group members from trusted domains do not sync to IAM Identity Center

If a security group syncs successfully to IAM Identity Center, but its members from a trusted on-premises
domain do not appear in the IAM Identity Center, this can be caused by the group resides in AWS Managed Microsoft AD
and contains Foreign Security Principal (FSPs) representing users from a trusted domain.

Try the following steps to troubleshoot:

- Sync groups directly from the trusted domain: Instead of syncing a group from AWS Managed Microsoft AD that
  contains cross-domain members, create and sync the group directly from the trusted on-premises
  domain. This approach works because IAM Identity Center can access actual user objects in the source domain.
- Verify service account permissions: Ensure the IAM Identity Center service account has the required
  permissions on user objects in the trusted domain: ReadProperties and ListContents permission.
