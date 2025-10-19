# How to create your emergency access configuration

Use the following mapping table to create your emergency access configuration. This
 table reflects a plan that includes two roles in the workload accounts: Read Only (RO) and
 Operations (Ops) , with corresponding trust policies and permissions policies. The trust
 policies enable the emergency access account roles to access the individual workload account roles.
 The individual workload account roles also have permissions policies for what the role can do in
 the account. The permissions policies can be [AWS managed policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies "https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies") or [customer managed policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#customer-managed-policies "https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#customer-managed-policies").



| Account | Roles to create | Trust policy | Permissions policy |
| --- | --- | --- | --- |
| Account 1 | EmergencyAccess\_RO | EmergencyAccess\_Role1\_RO | arn:aws:iam::aws:policy/ReadOnlyAccess |
| Account 1 | EmergencyAccess\_Ops | EmergencyAccess\_Role1\_Ops | arn:aws:iam::aws:policy/job-function/SystemAdministrator |
| Account 2 | EmergencyAccess\_RO | EmergencyAccess\_Role2\_RO | arn:aws:iam::aws:policy/ReadOnlyAccess |
| Account 2 | EmergencyAccess\_Ops | EmergencyAccess\_Role2\_Ops | arn:aws:iam::aws:policy/job-function/SystemAdministrator |
| Emergency access account | EmergencyAccess\_Role1\_RO EmergencyAccess\_Role1\_Ops EmergencyAccess\_Role2\_RO EmergencyAccess\_Role2\_Ops | IdP | AssumeRole for role resource in account | In this mapping plan, the emergency access account contains two read-only roles and two operations roles. These roles trust your IdP to authenticate and authorize your selected groups to access the roles by passing the names of the roles in assertions. There are corresponding read-only and operations roles in workload Account 1 and Account 2. For workload Account 1, the `EmergencyAccess_RO` role trusts the `EmergencyAccess_Role1_RO` role that resides in the emergency access account. The table specifies similar trust patterns between the workload account read-only and operations roles and the corresponding emergency access roles.
