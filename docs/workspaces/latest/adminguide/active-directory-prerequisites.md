# Before You Begin Using Active Directory

with WorkSpaces Pools

Before you use Microsoft Active Directory domains with WorkSpaces Pools, be aware of the
following requirements and considerations.

###### Contents

- [Active Directory
  Domain Environment](#active-directory-prerequisites-domain-environment "#active-directory-prerequisites-domain-environment")
- [Domain-Joined
  WorkSpaces in WorkSpaces Pools](#active-directory-prerequisites-streaming-instances "#active-directory-prerequisites-streaming-instances")
- [Group Policy
  Settings](#active-directory-prerequisites-group-policy-settings "#active-directory-prerequisites-group-policy-settings")
- [Smart
  Card Authentication](#active-directory-prerequisites-smart-card-authentication "#active-directory-prerequisites-smart-card-authentication")

## Active Directory

Domain Environment

- You must have a Microsoft Active Directory domain to which to join your
  WorkSpaces. If you don't have an Active Directory domain or you want to use your
  on-premises Active Directory environment, see [Active Directory Domain Services on the AWS Cloud: Quick Start Reference Deployment](../../../quickstart/latest/active-directory-ds.md "../../../quickstart/latest/active-directory-ds.md").
- You must have a domain service account with permissions to create and
  manage computer objects in the domain that you intend to use with
  WorkSpaces Pools. For information, see [How to Create a Domain Account in Active Directory](<https://msdn.microsoft.com/en-us/library/aa545262(v=cs.70).aspx> "https://msdn.microsoft.com/en-us/library/aa545262(v=cs.70).aspx") in the
  Microsoft documentation.

When you associate this Active Directory domain with WorkSpaces Pools, provide
the service account name and password. WorkSpaces Pools uses this account to
create and manage computer objects in the directory. For more information,
see [Granting Permissions to Create and
Manage Active Directory Computer Objects](active-directory-admin.md#active-directory-permissions "active-directory-admin.md#active-directory-permissions").

- When you register your Active Directory domain with WorkSpaces Pools, you must
  provide an organizational unit (OU) distinguished name. Create an OU for
  this purpose. The default Computers container is not an OU and cannot be
  used by WorkSpaces Pools. For more information, see [Finding the Organizational Unit
  Distinguished Name](active-directory-admin.md#active-directory-oudn "active-directory-admin.md#active-directory-oudn").
- The directories that you plan to use with WorkSpaces Pools must be accessible
  through their fully qualified domain names (FQDNs) through the virtual
  private cloud (VPC) in which your WorkSpaces are launched. For more information,
  see [Active Directory and Active Directory Domain Services Port
  Requirements](https://technet.microsoft.com/en-us/library/dd772723.aspx "https://technet.microsoft.com/en-us/library/dd772723.aspx") in the Microsoft documentation.

## Domain-Joined

WorkSpaces in WorkSpaces Pools

SAML 2.0-based user federation is required for application streaming from
domain-joined WorkSpaces. Also, you must use a Windows image that supports joining to an
Active Directory domain. All public images published on or after July 24, 2017
support joining an Active Directory
domain.

## Group Policy

Settings

Verify your configuration for the following Group Policy settings. If required,
update the settings as described in this section so that they don't block WorkSpaces Pools
from authenticating and logging in your domain users. Otherwise, when your users try
to log in to WorkSpaces the login may not succeed. Instead, a message displays, notifying
users that "An unknown error occurred."

- \*\*Computer Configuration > Administrative Templates
  > Windows Components > Windows Logon Options > Disable or
  > Enable software Secure Attention Sequence** — Set this to
  > **Enabled** for **Services\*\*.
- \*\*Computer Configuration > Administrative Templates
  > System > Logon > Exclude credential providers\**
  > — Ensure that the following CLSID is *not\* listed:
  > `e7c1bab5-4b49-4e64-a966-8d99686f8c7c`
- **Computer Configuration > Policies > Windows
  Settings > Security Settings > Local Policies > Security
  Options > Interactive Logon > Interactive Logon: Message text for
  users attempting to log on** — Set this to **Not
  defined**.
- **Computer Configuration > Policies > Windows
  Settings > Security Settings > Local Policies > Security
  Options > Interactive Logon > Interactive Logon: Message title for
  users attempting to log on** — Set this to **Not
  defined**.

## Smart

Card Authentication

WorkSpaces Pools supports the use of Active Directory domain passwords or smart cards
such as [Common Access Card
(CAC)](https://www.cac.mil/Common-Access-Card "https://www.cac.mil/Common-Access-Card") and [Personal Identity
Verification (PIV)](https://piv.idmanagement.gov/ "https://piv.idmanagement.gov/") smart cards for Windows sign in to WorkSpaces in
WorkSpaces Pools. For information about how to configure your Active Directory environment
to enable smart card sign in by using third-party certification authorities (CAs),
see [Guidelines for enabling smart card logon with third-party certification
authorities](https://docs.microsoft.com/en-us/troubleshoot/windows-server/windows-security/enabling-smart-card-logon-third-party-certification-authorities "https://docs.microsoft.com/en-us/troubleshoot/windows-server/windows-security/enabling-smart-card-logon-third-party-certification-authorities") in the Microsoft documentation.
