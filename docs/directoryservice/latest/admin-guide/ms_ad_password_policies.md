# Understanding AWS Managed Microsoft AD password policies

AWS Managed Microsoft AD enables you to define and assign different password and account lockout
policies (also referred to as [fine-grained password policies](https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/get-started/adac/introduction-to-active-directory-administrative-center-enhancements--level-100-#fine_grained_pswd_policy_mgmt "https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/get-started/adac/introduction-to-active-directory-administrative-center-enhancements--level-100-#fine_grained_pswd_policy_mgmt")) for groups of users you manage in your AWS Managed Microsoft AD
domain. When you create an AWS Managed Microsoft AD directory, a default domain policy is created and
applied to the Active Directory. This policy includes the following settings:

| Policy                                      | Setting                 |
| ------------------------------------------- | ----------------------- |
| Enforce password history                    | 24 passwords remembered |
| Maximum password age                        | 42 days \*              |
| Minimum password age                        | 1 day                   |
| Minimum password length                     | 7 characters            |
| Password must meet complexity requirements  | Enabled                 |
| Store passwords using reversible encryption | Disabled                |

###### Note

\* The 42 day maximum password age includes the admin password.

For example, you can assign a less strict policy setting for employees that have access to
low sensitivity information only. For senior managers who regularly access confidential
information you can apply more strict settings.

The following resources provide more information on Microsoft Active Directory fine-grained
password policies and security policies:

- [Configure security policy settings](https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-10/security/threat-protection/security-policy-settings/how-to-configure-security-policy-settings "https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-10/security/threat-protection/security-policy-settings/how-to-configure-security-policy-settings")
- [Password complexity requirements](https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-10/security/threat-protection/security-policy-settings/password-must-meet-complexity-requirements "https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-10/security/threat-protection/security-policy-settings/password-must-meet-complexity-requirements")
- [Password complexity security considerations](https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-10/security/threat-protection/security-policy-settings/password-must-meet-complexity-requirements#security-considerations "https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-10/security/threat-protection/security-policy-settings/password-must-meet-complexity-requirements#security-considerations")
  AWS provides a set of fine-grained password policies in AWS Managed Microsoft AD that you can
  configure and assign to your groups. To configure the policies, you can use standard
  Microsoft policy tools such as [Active Directory Administrative Center](https://docs.microsoft.com/en-us/windows-server/identity/ad-ds/get-started/adac/active-directory-administrative-center "https://docs.microsoft.com/en-us/windows-server/identity/ad-ds/get-started/adac/active-directory-administrative-center"). To get started with the Microsoft policy
  tools, see [Installing Active Directory Administration
  Tools for AWS Managed Microsoft AD](ms_ad_install_ad_tools.md "ms_ad_install_ad_tools.md").

## How password policies are applied

There are differences in how the fine-grained password policies are applied depending on
whether the password was reset or changed. Domain users can change their own
password. An Active Directory administrator or user with the necessary permissions can [reset users passwords](ms_ad_manage_users_groups_reset_password.md "ms_ad_manage_users_groups_reset_password.md"). See the following chart for more information.

| Policy                                     | Password Reset | Password Change |
| ------------------------------------------ | -------------- | --------------- |
| Enforce password history                   | No             | Yes             |
| Maximum password age                       | Yes            | Yes             |
| Minimum password age                       | No             | Yes             |
| Minimum password length                    | Yes            | Yes             |
| Password must meet complexity requirements | Yes            | Yes             |

These differences have security implications. For example, whenever a user's password is
reset, the enforce password history and minimum password age policies are not enforced. For more
information, see Microsoft documentation on the security considerations related to [enforce password history](https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-10/security/threat-protection/security-policy-settings/enforce-password-history#security-considerations "https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-10/security/threat-protection/security-policy-settings/enforce-password-history#security-considerations") and [minimum password age](https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-10/security/threat-protection/security-policy-settings/minimum-password-age#security-considerations "https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-10/security/threat-protection/security-policy-settings/minimum-password-age#security-considerations") policies.

## Supported policy settings

AWS Managed Microsoft AD includes five fine-grained policies with a non-editable precedence value. The
policies have a number of properties you can configure to enforce the strength of passwords,
and account lock-out actions in the event of login failures. You can assign the policies to
zero or more Active Directory groups. If an end-user is a member of multiple groups and
receives more than one password policy, Active Directory enforces the policy with the lowest
precedence value.

### AWS pre-defined password policies

The following table lists the five policies included in your AWS Managed Microsoft AD directory and
their assigned precedence value. For more information, see [Precedence](#precedence "#precedence").

| Policy name        | Precedence |
| ------------------ | ---------- |
| **CustomerPSO-01** | 10         |
| **CustomerPSO-02** | 20         |
| **CustomerPSO-03** | 30         |
| **CustomerPSO-04** | 40         |
| **CustomerPSO-05** | 50         |

#### Password policy properties

You may edit the following properties in your password policies to conform to the
compliance standards that meet your business needs.

- Policy name
- [Enforce password history](https://docs.microsoft.com/en-us/windows/security/threat-protection/security-policy-settings/enforce-password-history "https://docs.microsoft.com/en-us/windows/security/threat-protection/security-policy-settings/enforce-password-history")
- [Minimum password length](https://docs.microsoft.com/en-us/windows/security/threat-protection/security-policy-settings/minimum-password-length "https://docs.microsoft.com/en-us/windows/security/threat-protection/security-policy-settings/minimum-password-length")
- [Minimum password age](https://docs.microsoft.com/en-us/windows/security/threat-protection/security-policy-settings/minimum-password-age "https://docs.microsoft.com/en-us/windows/security/threat-protection/security-policy-settings/minimum-password-age")
- [Maximum password age](https://docs.microsoft.com/en-us/windows/security/threat-protection/security-policy-settings/maximum-password-age "https://docs.microsoft.com/en-us/windows/security/threat-protection/security-policy-settings/maximum-password-age")
- [Store passwords using reversible encryption](https://docs.microsoft.com/en-us/windows/security/threat-protection/security-policy-settings/store-passwords-using-reversible-encryption "https://docs.microsoft.com/en-us/windows/security/threat-protection/security-policy-settings/store-passwords-using-reversible-encryption")
- [Password must meet complexity requirements](https://docs.microsoft.com/en-us/windows/security/threat-protection/security-policy-settings/password-must-meet-complexity-requirements "https://docs.microsoft.com/en-us/windows/security/threat-protection/security-policy-settings/password-must-meet-complexity-requirements")

You cannot modify the precedence values for these policies. For more details about how
these settings affect password enforcement, see [AD DS:
Fine-grained password policies](<https://technet.microsoft.com/en-us/library/cc770394(v=ws.10).aspx> "https://technet.microsoft.com/en-us/library/cc770394(v=ws.10).aspx") on the _Microsoft TechNet_
website. For general information about these policies, see [Password
policy](<https://technet.microsoft.com/en-us/library/hh994572(v=ws.11).aspx> "https://technet.microsoft.com/en-us/library/hh994572(v=ws.11).aspx") on the _Microsoft TechNet_ website.

### Account lockout policies

You may also modify the following properties of your password policies to specify if and
how Active Directory should lockout an account after login failures:

- Number of failed logon attempts allowed
- Account lockout duration
- Reset failed logon attempts after some duration

For general information about these policies, see [Account lockout
policy](<https://technet.microsoft.com/en-us/library/hh994563(v=ws.11).aspx> "https://technet.microsoft.com/en-us/library/hh994563(v=ws.11).aspx") on the _Microsoft TechNet_ website.

### Precedence

Policies with a lower precedence value have higher priority. You assign password
policies to Active Directory security groups. While you should apply a single policy to a
security group, a single user may receive more than one password policy. For example,
suppose `jsmith` is a member of the HR group and also a member of the MANAGERS
group. If you assign **CustomerPSO-05** (which has a precedence of 50) to
the HR group, and **CustomerPSO-04** (which has a precedence of 40) to
MANAGERS, **CustomerPSO-04** has the higher priority and Active Directory
applies that policy to `jsmith`.

If you assign multiple policies to a user or group, Active Directory determines the
resultant policy as follows:

1. A policy you assign directly to the user object applies.
2. If no policy is assigned directly to the user object, the policy with the lowest
   precedence value of all policies received by the user as a result of group membership
   applies.

For additional details, see [AD DS:
Fine-grained password policies](<https://technet.microsoft.com/en-us/library/cc770394(v=ws.10).aspx> "https://technet.microsoft.com/en-us/library/cc770394(v=ws.10).aspx") on the _Microsoft TechNet_
website.

###### Topics

- [Assigning password policies to your AWS Managed Microsoft AD users](assignpasswordpolicies.md "assignpasswordpolicies.md")
- [Delegating who can manage your AWS Managed Microsoft AD password
  policies](delegatepasswordpolicies.md "delegatepasswordpolicies.md")
  **Related AWS Security blog article**

- [How to configure even stronger password policies to help meet your security standards by
  using Directory Service for AWS Managed Microsoft AD](https://aws.amazon.com/blogs/security/how-to-configure-even-stronger-password-policies-to-help-meet-your-security-standards-by-using-aws-directory-service-for-microsoft-active-directory/ "https://aws.amazon.com/blogs/security/how-to-configure-even-stronger-password-policies-to-help-meet-your-security-standards-by-using-aws-directory-service-for-microsoft-active-directory/")
