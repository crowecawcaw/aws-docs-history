

# Understanding AWS Managed Microsoft AD password policies
<a name="ms_ad_password_policies"></a>

AWS Managed Microsoft AD enables you to define and assign different password and account lockout policies (also referred to as [fine-grained password policies](https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/get-started/adac/introduction-to-active-directory-administrative-center-enhancements--level-100-#fine_grained_pswd_policy_mgmt)) for groups of users you manage in your AWS Managed Microsoft AD domain. When you create an AWS Managed Microsoft AD directory, a default domain policy is created and applied to the Active Directory. This policy includes the following settings:



| Policy | Setting | 
| --- | --- | 
| Enforce password history | 24 passwords remembered | 
| Maximum password age | 42 days \* | 
| Minimum password age | 1 day | 
| Minimum password length | 7 characters | 
| Password must meet complexity requirements | Enabled | 
| Store passwords using reversible encryption | Disabled | 

**Note**  
\* The 42 day maximum password age includes the admin password.

For example, you can assign a less strict policy setting for employees that have access to low sensitivity information only. For senior managers who regularly access confidential information you can apply more strict settings.

The following resources provide more information on Microsoft Active Directory fine-grained password policies and security policies:
+ [Configure security policy settings](https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-10/security/threat-protection/security-policy-settings/how-to-configure-security-policy-settings)
+ [Password complexity requirements](https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-10/security/threat-protection/security-policy-settings/password-must-meet-complexity-requirements)
+ [Password complexity security considerations](https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-10/security/threat-protection/security-policy-settings/password-must-meet-complexity-requirements#security-considerations)

AWS provides a set of fine-grained password policies in AWS Managed Microsoft AD that you can configure and assign to your groups. To configure the policies, you can use standard Microsoft policy tools such as [Active Directory Administrative Center](https://docs.microsoft.com/en-us/windows-server/identity/ad-ds/get-started/adac/active-directory-administrative-center). To get started with the Microsoft policy tools, see [Installing Active Directory Administration Tools for AWS Managed Microsoft AD](ms_ad_install_ad_tools.md).

## How password policies are applied
<a name="how_password_policies_applied"></a>

 There are differences in how the fine-grained password policies are applied depending on whether the password was reset or changed. Domain users can change their own password. An Active Directory administrator or user with the necessary permissions can [ reset users passwords](ms_ad_manage_users_groups_reset_password.md). See the following chart for more information.



| Policy | Password Reset | Password Change | 
| --- | --- | --- | 
| Enforce password history | ![](http://docs.aws.amazon.com/directoryservice/latest/admin-guide/images/icon-no.png) No | ![](http://docs.aws.amazon.com/directoryservice/latest/admin-guide/images/icon-yes.png) Yes | 
| Maximum password age | ![](http://docs.aws.amazon.com/directoryservice/latest/admin-guide/images/icon-yes.png) Yes | ![](http://docs.aws.amazon.com/directoryservice/latest/admin-guide/images/icon-yes.png) Yes | 
| Minimum password age | ![](http://docs.aws.amazon.com/directoryservice/latest/admin-guide/images/icon-no.png) No | ![](http://docs.aws.amazon.com/directoryservice/latest/admin-guide/images/icon-yes.png) Yes | 
| Minimum password length | ![](http://docs.aws.amazon.com/directoryservice/latest/admin-guide/images/icon-yes.png) Yes | ![](http://docs.aws.amazon.com/directoryservice/latest/admin-guide/images/icon-yes.png) Yes | 
| Password must meet complexity requirements | ![](http://docs.aws.amazon.com/directoryservice/latest/admin-guide/images/icon-yes.png) Yes | ![](http://docs.aws.amazon.com/directoryservice/latest/admin-guide/images/icon-yes.png) Yes | 

 These differences have security implications. For example, whenever a user's password is reset, the enforce password history and minimum password age policies are not enforced. For more information, see Microsoft documentation on the security considerations related to [enforce password history](https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-10/security/threat-protection/security-policy-settings/enforce-password-history#security-considerations) and [minimum password age](https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-10/security/threat-protection/security-policy-settings/minimum-password-age#security-considerations) policies.

## Supported policy settings
<a name="supportedpolicysettings"></a>

AWS Managed Microsoft AD includes five fine-grained policies with a non-editable precedence value. The policies have a number of properties you can configure to enforce the strength of passwords, and account lock-out actions in the event of login failures. You can assign the policies to zero or more Active Directory groups. If an end-user is a member of multiple groups and receives more than one password policy, Active Directory enforces the policy with the lowest precedence value.

### AWS pre-defined password policies
<a name="supportedpwdpolicies"></a>

The following table lists the five policies included in your AWS Managed Microsoft AD directory and their assigned precedence value. For more information, see [Precedence](#precedence).



| Policy name | Precedence | 
| --- | --- | 
| CustomerPSO-01 | 10 | 
| CustomerPSO-02 | 20 | 
| CustomerPSO-03 | 30 | 
| CustomerPSO-04 | 40 | 
| CustomerPSO-05 | 50 | 

#### Password policy properties
<a name="passwordpolicyprop"></a>

You may edit the following properties in your password policies to conform to the compliance standards that meet your business needs.
+ Policy name
+ [Enforce password history](https://docs.microsoft.com/en-us/windows/security/threat-protection/security-policy-settings/enforce-password-history)
+ [Minimum password length](https://docs.microsoft.com/en-us/windows/security/threat-protection/security-policy-settings/minimum-password-length)
+ [Minimum password age](https://docs.microsoft.com/en-us/windows/security/threat-protection/security-policy-settings/minimum-password-age)
+ [Maximum password age](https://docs.microsoft.com/en-us/windows/security/threat-protection/security-policy-settings/maximum-password-age)
+ [Store passwords using reversible encryption](https://docs.microsoft.com/en-us/windows/security/threat-protection/security-policy-settings/store-passwords-using-reversible-encryption)
+ [Password must meet complexity requirements](https://docs.microsoft.com/en-us/windows/security/threat-protection/security-policy-settings/password-must-meet-complexity-requirements)

You cannot modify the precedence values for these policies. For more details about how these settings affect password enforcement, see [AD DS: Fine-grained password policies](https://technet.microsoft.com/en-us/library/cc770394(v=ws.10).aspx) on the *Microsoft TechNet* website. For general information about these policies, see [Password policy](https://technet.microsoft.com/en-us/library/hh994572(v=ws.11).aspx) on the *Microsoft TechNet* website.

### Account lockout policies
<a name="supportedlockoutpolicies"></a>

You may also modify the following properties of your password policies to specify if and how Active Directory should lockout an account after login failures:
+ Number of failed logon attempts allowed
+ Account lockout duration
+ Reset failed logon attempts after some duration

For general information about these policies, see [Account lockout policy](https://technet.microsoft.com/en-us/library/hh994563(v=ws.11).aspx) on the *Microsoft TechNet* website.

### Precedence
<a name="precedence"></a>

Policies with a lower precedence value have higher priority. You assign password policies to Active Directory security groups. While you should apply a single policy to a security group, a single user may receive more than one password policy. For example, suppose `jsmith` is a member of the HR group and also a member of the MANAGERS group. If you assign **CustomerPSO-05** (which has a precedence of 50) to the HR group, and **CustomerPSO-04** (which has a precedence of 40) to MANAGERS, **CustomerPSO-04** has the higher priority and Active Directory applies that policy to `jsmith`.

If you assign multiple policies to a user or group, Active Directory determines the resultant policy as follows:

1. A policy you assign directly to the user object applies.

1. If no policy is assigned directly to the user object, the policy with the lowest precedence value of all policies received by the user as a result of group membership applies.

For additional details, see [AD DS: Fine-grained password policies](https://technet.microsoft.com/en-us/library/cc770394(v=ws.10).aspx) on the *Microsoft TechNet* website.

**Topics**
+ [How password policies are applied](#how_password_policies_applied)
+ [Supported policy settings](#supportedpolicysettings)
+ [Assigning password policies to your AWS Managed Microsoft AD users](assignpasswordpolicies.md)
+ [Delegating who can manage your AWS Managed Microsoft AD password policies](delegatepasswordpolicies.md)

**Related AWS Security blog article**
+ [How to configure even stronger password policies to help meet your security standards by using Directory Service for AWS Managed Microsoft AD](https://aws.amazon.com/blogs/security/how-to-configure-even-stronger-password-policies-to-help-meet-your-security-standards-by-using-aws-directory-service-for-microsoft-active-directory/)