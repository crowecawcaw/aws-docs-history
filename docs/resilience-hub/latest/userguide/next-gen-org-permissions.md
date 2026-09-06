

# Required IAM permissions for delegated administrator setup
<a name="next-gen-org-permissions"></a>

The following IAM permissions are required for each role in the Organizations integration:

**Management account**

The management account needs permissions to:
+ `organizations:EnableAWSServiceAccess`
+ `organizations:RegisterDelegatedAdministrator`
+ `iam:CreateServiceLinkedRole` (for the management account's own SLR)

**Delegated administrator account**

The DA account uses standard the next generation of Resilience Hub API permissions. Cross-account access is handled by SLRs – no additional IAM configuration is needed for viewing member account data.

**Member accounts**

Service owners in member accounts:
+ Create their own invoker roles using the same process as the single-account setup. For details, see [Setting up Next generation Resilience Hub](next-gen-setting-up.md).
+ Can see and apply org-level policies published by the DA.
+ The SLR handles DA cross-account visibility automatically – no additional IAM changes are required in member accounts.

The following table summarizes what the DA can and cannot do:


| Action | Supported | 
| --- | --- | 
| View member account services, findings, and dependencies | Yes | 
| Create org-level systems that reference member services | Yes | 
| Associate member services to org-level systems | Yes | 
| Create org-level policies | Yes | 
| Delete member account services | No | 
| Start assessments on member services | Yes | 
| Modify member account resources | No | 

Destructive operations on member resources are not supported through DA cross-account access. The DA manages org-level systems and policies and views member data.