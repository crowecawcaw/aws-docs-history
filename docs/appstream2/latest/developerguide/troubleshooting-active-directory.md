# Troubleshooting Active Directory

The following are issues that might occur when you set up and use Active
Directory with Amazon WorkSpaces Applications. For help troubleshooting notification codes, see
[Troubleshooting Notification Codes](troubleshooting-notification-codes.md "troubleshooting-notification-codes.md").

###### Issues

- [My image builders and fleet instances are stuck in the PENDING state.](#troubleshooting-active-directory-1 "#troubleshooting-active-directory-1")
- [My users aren't able to log in with the SAML application.](#troubleshooting-active-directory-2 "#troubleshooting-active-directory-2")
- [My fleet instances work for one user but don't cycle correctly.](#troubleshooting-active-directory-3 "#troubleshooting-active-directory-3")
- [My user Group Policy objects aren't being successfully applied.](#troubleshooting-active-directory-4 "#troubleshooting-active-directory-4")
- [My WorkSpaces Applications streaming instances aren't joining the Active Directory domain.](#troubleshooting-active-directory-5 "#troubleshooting-active-directory-5")
- [User login is taking a long time to complete on a domain-joined streaming session.](#troubleshooting-active-directory-6 "#troubleshooting-active-directory-6")
- [My users can't access a domain resource in a domain-joined streaming session, but they can access the resource from a domain-joined image builder.](#troubleshooting-active-directory-8 "#troubleshooting-active-directory-8")
- [My users receive the error “Certificate-Based Authentication not available” and are prompted to enter their domain password. Or users receive the error “Disconnected from session” when they are starting a session enabled with certificate-based authentication.](#troubleshooting-active-directory-9 "#troubleshooting-active-directory-9")
- [I'm experiencing domain join failures after changing the Active Directory (AD) service account.](#troubleshooting-active-directory-10 "#troubleshooting-active-directory-10")

## My image builders and fleet instances are stuck in the PENDING state.

Image builders and fleet instances can take up to 25 minutes to move into a ready
state and become available. If your instances are taking longer than 25 minutes to
become available, in Active Directory, verify whether new computer objects were
created in the correct organizational units (OUs). If there are new objects, the
streaming instances will be available soon. If the objects aren't there, check the
directory configuration details in your WorkSpaces Applications Directory Config: Directory name (the
fully qualified domain name of the directory, service account sign-in credentials,
and the OU distinguished name.

Image builder and fleet errors are displayed in the WorkSpaces Applications console on the
**Notifications** tab for the fleet or image builder. Fleet
errors are also available using the WorkSpaces Applications API through the
[DescribeFleets](../APIReference/API_DescribeFleets.md "../APIReference/API_DescribeFleets.md") operation or the CLI command
[describe-fleets](../../../cli/latest/reference/appstream/describe-fleets.md "../../../cli/latest/reference/appstream/describe-fleets.md").

## My users aren't able to log in with the SAML application.

WorkSpaces Applications relies on the SAML_Subject "NameID" attribute from your identity provider
to populate the username field to log in your user. The username can either be
formatted as "``domain`\username`", or
 "`user@domain.com`". If you are using
 "``domain`\username`" format,
`domain` can either be the NetBIOS
name or the fully qualified domain name. If using "`user@domain.com`"
format, the UserPrincipalName attribute can be used. If you've verified your
SAML_Subject attribute is configured correctly and the problem persists, contact AWS Support. For more information, see [AWS Support Center](https://console.aws.amazon.com/support/home#/ "https://console.aws.amazon.com/support/home#/").

## My fleet instances work for one user but don't cycle correctly.

Fleet instances are cycled after a user completes a session, ensuring that each
user has a new instance. When the cycled fleet instance is brought online, it joins
the domain using the computer name of the previous instance. To ensure that this
operation happens successfully, the service account requires **Change Password** and **Reset Password**
permissions on the organizational unit (OU) to which the computer object is joining.
Check the service account permissions and try again. If the problem persists,
contact AWS Support. For more information, see [AWS Support Center](https://console.aws.amazon.com/support/home#/ "https://console.aws.amazon.com/support/home#/").

## My user Group Policy objects aren't being successfully applied.

By default, computer objects apply computer-level policies based on the OU in
which the computer object resides, while applying user-level policies based on the
OU in which the user resides. If your user-level policies aren't being applied, you
can do one of the following:

- Move the user-level policies to the OU in which the user Active Directory
  object resides
- Enable computer-level loopback processing, which applies the user-level
  policies in the computer object OU.

For more information, see [Loopback processing of Group Policy](https://support.microsoft.com/en-us/help/231287/loopback-processing-of-group-policy "https://support.microsoft.com/en-us/help/231287/loopback-processing-of-group-policy") at Microsoft Support.

## My WorkSpaces Applications streaming instances aren't joining the Active Directory domain.

The Active Directory domain to use with WorkSpaces Applications must be accessible through its
fully qualified domain name (FQDN) through the VPC in which your streaming instances
are launched.

###### To test that your domain is accessible

1. Launch an Amazon EC2 instance in the same VPC, subnet, and security groups that
   you use with WorkSpaces Applications.
2. Manually join the EC2 instance to your Active Directory domain by using the
   FQDN (for example, `yourdomain.example.com`) with the service
   account that you intend to use with WorkSpaces Applications. Use the following command in a
   Windows PowerShell console:

```
`netdom join `computer` /domain:`FQDN` /OU:`path` /ud:`user` /pd:`password``
```

If this manual join fails, go to the next step. 3. If you cannot manually join to your domain, open a command prompt and
verify that you can resolve the FQDN using the `nslookup`
command. For example:

```
`nslookup `yourdomain.exampleco.com``
```

Successful name resolution returns a valid IP address. If you are unable
to resolve your FQDN, you might need to update your VPC DNS servers by using
a DHCP option set for your domain. Then, come back to this step. For more
information, see [DHCP Options Sets](../../../vpc/latest/userguide/VPC_DHCP_Options.md "../../../vpc/latest/userguide/VPC_DHCP_Options.md") in the
_Amazon VPC User Guide_. 4. If the FQDN resolves, use the `telnet` command to validate
connectivity.

```
`telnet `yourdomain.exampleco.com` 389`
```

A successful connection shows a blank command prompt window without any
connection errors. You might need to install the Telnet Client feature on
your EC2 instance. For more information, see [Install
Telnet Client](https://technet.microsoft.com/en-us/library/cc771275.aspx "https://technet.microsoft.com/en-us/library/cc771275.aspx") in the Microsoft documentation.

If you were not able to manually join the EC2 instance to your domain, but were
successful in resolving the FQDN and testing connectivity with the Telnet Client,
your VPC security groups might be preventing access. Active Directory requires
certain network port settings. For more information, see [Active Directory
and Active Directory Domain Services Port Requirements](https://technet.microsoft.com/en-us/library/dd772723.aspx "https://technet.microsoft.com/en-us/library/dd772723.aspx") in the Microsoft
documentation.

## User login is taking a long time to complete on a domain-joined streaming session.

WorkSpaces Applications performs a Windows login action after users provide their domain password.
After successful authentication, WorkSpaces Applications launches the application. The login and launch times are impacted by many variables, such as
network contention for the domain controllers or the time it takes to apply Group Policy settings
to the streaming instance. If domain authentication takes too long to complete, try performing
the following actions.

- Minimize the network latency from your WorkSpaces Applications Region to your domain
  controllers by choosing the correct domain controllers. For example, if your
  fleet is in `us-east-1`, use domain controllers with high bandwidth and low
  latency to `us-east-1` through Active Directory Sites and Services zone
  mappings. For more information, see [Active
  Directory Sites and Services](https://technet.microsoft.com/en-us/library/cc730868.aspx "https://technet.microsoft.com/en-us/library/cc730868.aspx") in the Microsoft
  documentation.
- Ensure that your Group Policy settings and user login scripts don't take
  prohibitively long to apply or run.

If your domain users' login to WorkSpaces Applications fails with the message "An unknown error
occurred," you might need to update the Group Policy settings described in [Before You Begin Using Active Directory with Amazon WorkSpaces Applications](active-directory-prerequisites.md "active-directory-prerequisites.md"). Otherwise, these settings might
prevent WorkSpaces Applications from authenticating and logging in your domain users.

## My users can't access a domain resource in a domain-joined streaming session, but they can access the resource from a domain-joined image builder.

Confirm that your fleet is created in the same VPC, subnets, and security groups
as your image builder, and that your user has the permissions required to access and
use the domain resource.

## My users receive the error “Certificate-Based Authentication not available” and are prompted to enter their domain password. Or users receive the error “Disconnected from session” when they are starting a session enabled with certificate-based authentication.

These errors occur if certificate-based authentication was unsuccessful for the
session. The “Certificate-Based Authentication not available” error is displayed
when certificate-based authentication is enabled to allow fallback to password
logon. The “Disconnected from session” error is displayed when certificate-based
authentication is enabled without fallback.

The user can refresh the page on the web client or reconnect from the client for
Windows, as this may be an intermittent issue with certificate-based authentication.
If the problem continues, certificate-based authentication failure can result from
one of the following issues:

- WorkSpaces Applications could not communicate with AWS Private CA, or AWS Private CA
  did not issue the certificate. Check CloudTrail to determine if a certificate was
  issued. For more information, see [What Is AWS CloudTrail?](../../../awscloudtrail/latest/userguide/cloudtrail-user-guide.md "../../../awscloudtrail/latest/userguide/cloudtrail-user-guide.md") and [Manage Certificate-based Authentication](certificate-based-authentication-manage.md "certificate-based-authentication-manage.md").
- The domain controller has no domain controller certificate for smart card
  logon, or it is expired. For more information, see step 7.a in [Prerequisites](certificate-based-authentication-prereq.md "certificate-based-authentication-prereq.md").
- The certificate is not trusted. For more information, see step 7.c in
  [Prerequisites](certificate-based-authentication-prereq.md "certificate-based-authentication-prereq.md").
- The userPrincipalName format for the SAML_Subject NameID is not formatted
  properly, or does not resolve to the actual domain for the user. For more
  information, see step 1 in [Prerequisites](certificate-based-authentication-prereq.md "certificate-based-authentication-prereq.md").
- The (optional) ObjectSid attribute in your SAML assertion does not match
  the Active Directory security identifier (SID) for the user specified in the
  SAML_Subject NameID. Confirm that the attribute mapping is correct in your
  SAML federation, and that your SAML identity provider is synchronizing the
  SID attribute for the Active Directory user.
- The WorkSpaces Applications agent does not support certificate-based authentication. Use
  WorkSpaces Applications agent version 10-13-2022 or later.
- There are Group Policy settings that are modifying the default Active
  Directory settings for smart card logon, or taking action if a smart card is
  removed from a smart card reader. These settings may cause additional
  unexpected behavior other than the errors listed above. Certificate-based
  authentication presents a virtual smart card to the instance operating
  system, and removes it after logon is complete. For more information, see
  [Primary Group Policy settings for smart cards](https://learn.microsoft.com/en-us/windows/security/identity-protection/smart-cards/smart-card-group-policy-and-registry-settings#primary-group-policy-settings-for-smart-cards "https://learn.microsoft.com/en-us/windows/security/identity-protection/smart-cards/smart-card-group-policy-and-registry-settings#primary-group-policy-settings-for-smart-cards") and [Additional smart card Group Policy settings and registry keys](https://learn.microsoft.com/en-us/windows/security/identity-protection/smart-cards/smart-card-group-policy-and-registry-settings#additional-smart-card-group-policy-settings-and-registry-keys "https://learn.microsoft.com/en-us/windows/security/identity-protection/smart-cards/smart-card-group-policy-and-registry-settings#additional-smart-card-group-policy-settings-and-registry-keys").
  Do not enable **Smart card sign in for Active Directory**
  in your stack if you want to use certificate-based authentication. For more
  information, see [Smart Cards](feature-support-USB-devices-qualified.md#feature-support-USB-devices-qualified-smart-cards "feature-support-USB-devices-qualified.md#feature-support-USB-devices-qualified-smart-cards").
- The CRL distribution point for the private CA is not online or accessible
  from either the WorkSpaces Applications fleet instance or the domain controller. For more
  information, see step 5 in [Prerequisites](certificate-based-authentication-prereq.md "certificate-based-authentication-prereq.md").

Additional troubleshooting steps involve reviewing the WorkSpaces Applications instance Windows
event logs. A common event to review for logon failure is [4625(F): An account failed to log on](https://learn.microsoft.com/en-us/windows/security/threat-protection/auditing/event-4625 "https://learn.microsoft.com/en-us/windows/security/threat-protection/auditing/event-4625"). For more information about
capturing log information, see [Persisting application and Windows event logs](../../../whitepapers/latest/best-practices-for-deploying-amazon-appstream-2/monitoring.md#persisting-application-and-windows-event-logs "../../../whitepapers/latest/best-practices-for-deploying-amazon-appstream-2/monitoring.md#persisting-application-and-windows-event-logs"). Alternatively, to
troubleshoot an active WorkSpaces Applications session as an administrator, you can connect to the
logs using an Event Viewer on another computer. For more information, see [How to Select Computers in Event Viewer](https://learn.microsoft.com/en-us/host-integration-server/core/how-to-select-computers-in-event-viewer1 "https://learn.microsoft.com/en-us/host-integration-server/core/how-to-select-computers-in-event-viewer1"). Or ,you can connect by using
Remote Desktop to connect to the instance private IP address from another computer
that can connect to Remote Desktop Services in your WorkSpaces Applicationsvirtual private cloud
(VPC). Use the AWS CLI to determine the IP address for the session based on the
AWS Region, WorkSpaces Applications stack name, fleet name, user ID, and authentication type. For
more information, see the [AWS Command Line Interface.](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appstream/index.html#cli-aws-appstream "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appstream/index.html#cli-aws-appstream")

If the problem persists, contact AWS Support. For more information, see
[AWS Support Center](https://console.aws.amazon.com/support/home#/ "https://console.aws.amazon.com/support/home#/").

## I'm experiencing domain join failures after changing the Active Directory (AD) service account.

If you have an existing fleet with an image based on the August 2024 [Microsoft Windows Server operating system update](https://learn.microsoft.com/en-us/windows-server/get-started/windows-server-release-info "https://learn.microsoft.com/en-us/windows-server/get-started/windows-server-release-info"), and if you change
your Active Directory (AD) service account for that fleet, your fleet instances
might encounter domain join failures during provisioning.

Microsoft has released a patch [KB5020276](https://support.microsoft.com/en-us/topic/kb5020276-netjoin-domain-join-hardening-changes-2b65a0f3-1f4c-42ef-ac0f-1caaf421baf8 "https://support.microsoft.com/en-us/topic/kb5020276-netjoin-domain-join-hardening-changes-2b65a0f3-1f4c-42ef-ac0f-1caaf421baf8"), which modifies the behavior of domain join operations.
WorkSpaces Applications reuses existing computer objects when joining your streaming instances to
your AD domains. This computer object is generated using the AD service account that
you provide when you create a fleet or Directory Config with WorkSpaces Applications. Prior to this
Microsoft patch, new AD service accounts could reuse existing computer objects
created by WorkSpaces Applications, as long as they had "Create Computer Object" permissions
configured in the organizational unit (OU).

When the Microsoft patch is enforced, starting on August 13, 2024, and if you
change your AD service account for an existing WorkSpaces Applications fleet, the new service account
will no longer be able to reuse the existing computer objects in the AD. This
results in domain join failures on WorkSpaces Applications fleets, with one of the following error
messages under fleet notifications:

- DOMAIN_JOIN_INTERNAL_SERVICE_ERROR "The group name could not be
  found."
- An account with the same name exists in Active Directory. Re-using the
  account was blocked by security policy

To control which account can reuse the existing computer objects, Microsoft has
implemented a new Group Policy setting called **Domain controller: Allow
computer account re-use during domain join**. This setting allows you
to specify a list of trusted service accounts that bypass the check during the
domain join operation. For your self-managed AD configuration, we recommend
following the [Microsoft documented steps](https://support.microsoft.com/en-us/topic/kb5020276-netjoin-domain-join-hardening-changes-2b65a0f3-1f4c-42ef-ac0f-1caaf421baf8#bkmk_take_action "https://support.microsoft.com/en-us/topic/kb5020276-netjoin-domain-join-hardening-changes-2b65a0f3-1f4c-42ef-ac0f-1caaf421baf8#bkmk_take_action") to add your AD service account to the new
allow list policy, using Group Policies on a domain controller.

For Managed Active Directory (MAD), you must restart your WorkSpaces Applications fleet after you
make changes to your WorkSpaces Applications domain join service account.

If the problem persists, contact AWS Support. For more information, see
[AWS Support Center](https://console.aws.amazon.com/support/home#/ "https://console.aws.amazon.com/support/home#/").
