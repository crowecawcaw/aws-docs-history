

# Remediating exposures for Azure Graph users
<a name="exposure-azure-graph-user"></a>

AWS Security Hub can generate exposure findings for Azure Graph users.

On the Security Hub console, the Azure Graph user involved in an exposure finding and its identifying information are listed in the **Resources** section of the finding details. Programmatically, you can retrieve resource details with the [GetFindingsV2](https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_GetFindingsV2.html) operation of the Security Hub CSPM API.

After identifying the resource involved in an exposure finding, you can delete the resource if you don't need it. Deleting a nonessential resource can reduce your exposure profile and AWS costs. If the resource is essential, follow these recommended remediation steps to help mitigate the risk. The remediation topics are divided based on the type of trait. 

A single exposure finding contains issues identified in multiple remediation topics. Conversely, you can address an exposure finding and bring down its severity level by addressing just one remediation topic. Your approach to risk remediation depends on your organizational requirements and workloads.

**Note**  
 The remediation guidance provided in this topic might require additional consultation in other Microsoft Azure resources. 

**Contents**
+ [Misconfiguration traits for Azure Graph users](#azure-graph-user-misconfiguration)
  + [The role associated with the Azure Graph user has an administrative access role assignment](#administrative-access-policy)
  + [The Azure Graph user does not have MFA enabled](#user-mfa-disabled)

## Misconfiguration traits for Azure Graph users
<a name="azure-graph-user-misconfiguration"></a>

Here are misconfiguration traits for Azure Graph users and suggested remediation steps.

### The role associated with the Azure Graph user has an administrative access role assignment
<a name="administrative-access-policy"></a>

 The Azure Graph user has an administrative Azure role-based access control (Azure RBAC) role assignment, such as `Owner`, `Contributor`, or `User Access Administrator`. The assignment is often at a broad scope, such as a subscription or management group. Administrative role assignments grant broad permissions, so an attacker can use a compromised user account to move laterally, access data, or manipulate resources across your environment. Following standard security principles, grant least privilege and limit privileged administrator role assignments. 

**Remediation**  
Take one or more of the following actions to address this exposure:

**Review and identify administrative role assignments**  
 In the Azure portal, review the user's role assignments. Look for privileged administrator roles such as `Owner`, `Contributor`, or `User Access Administrator`, and for custom roles that use a wildcard (`*`) in their `Actions`. For more information, see [List Azure role assignments](https://learn.microsoft.com/en-us/azure/role-based-access-control/role-assignments-list-portal) in the Microsoft Azure documentation. 

**Implement least privilege access**  
 Remove unnecessary privileged role assignments and replace them with the least-privileged built-in role, assigned at the narrowest scope. Prefer job-function roles over privileged administrator roles. Keep the number of subscription owners to a minimum — Microsoft recommends no more than three. 

 Assign roles to groups rather than individual users. Use Microsoft Entra Privileged Identity Management to make privileged roles eligible for just-in-time, time-bound activation instead of granting standing access. For more information, see [Best practices for Azure RBAC](https://learn.microsoft.com/en-us/azure/role-based-access-control/best-practices) in the Microsoft Azure documentation. 

### The Azure Graph user does not have MFA enabled
<a name="user-mfa-disabled"></a>

 The Azure Graph user can sign in interactively without multifactor authentication (MFA). Without MFA, an account is protected only by a password, which leaves it vulnerable to phishing, password spray, and credential-stuffing attacks. A single compromised password is enough for an attacker to sign in. Following standard security principles, require MFA for all users with interactive sign-in. 

**Remediation: Require multifactor authentication**  
 Require MFA for the user through a Microsoft Entra Conditional Access policy. For broad coverage, enable security defaults or a Conditional Access policy that requires MFA for all users. Prioritize a dedicated policy for administrators. 

 Where possible, require phishing-resistant methods — such as FIDO2 security keys, passkeys, or Windows Hello for Business — through a Conditional Access authentication strength. Avoid permitting phishable methods such as SMS or voice. For more information, see [Plan a multifactor authentication deployment](https://learn.microsoft.com/en-us/entra/identity/authentication/howto-mfa-getstarted) in the Microsoft Azure documentation. 