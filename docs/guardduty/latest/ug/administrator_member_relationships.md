# Understanding the relationship between GuardDuty administrator account and member accounts

When you use GuardDuty in a multiple-account environment, the administrator account can manage certain
aspects of GuardDuty on behalf of the member accounts. An administrator account can perform the following
primary functions:

- **Add and remove associated member accounts**
  – The process by which an administrator account can do this differs based on how you
  manage the accounts – through AWS Organizations or by GuardDuty invitation
  method.

GuardDuty recommends managing your member accounts through AWS Organizations.

- **Delegated GuardDuty administrator account enabling GuardDuty in
  management account** – If the AWS Organizations management account ever
  disables GuardDuty, the delegated GuardDuty administrator account can enable GuardDuty in the management account. However,
  it is required that the management account must have not explicitly deleted the
  [Service-linked role permissions for GuardDuty](slr-permissions.md "slr-permissions.md").
- _Configure status of member accounts_ – An administrator account
  can enable or disable the status of GuardDuty protection plans, and enable, suspend,
  or disable the status of GuardDuty on behalf of associated member accounts.

Delegated GuardDuty administrator account managed with AWS Organizations can automatically enable GuardDuty when the
AWS accounts are added as members.

- **Customize when to generate findings** –
  An administrator account can customize findings within the GuardDuty network by creating and
  managing suppression rules, trusted IP lists, and threat lists. In a
  multiple-account environment, support to configure these features is available
  only to an delegated GuardDuty administrator account. A member account can't update this
  configuration.
  The following table details the relationship between GuardDuty administrator account and member
  accounts.

###### Key for the table

- **Self** – An account can perform the
  listed action only for their own account.
- **Any** – An account can perform the
  listed action for any associated account.
- **All** – An account can perform the
  listed action and it applies to all the associated accounts. Usually, the
  account taking this action is a designated GuardDuty administrator account
- **Cells with dash (–)** – Table
  cells with dash (–) indicate that the account can't perform the listed
  action.

| **Action**                                                                                                                                               | **Through AWS Organizations**    | **By invitation**                   |
| -------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------- | ----------------------------------- |
| **Delegated GuardDuty administrator account**                                                                                                            | **Associated member<br>account** | **GuardDuty administrator account** | **Associated member<br>account** |
| Enable GuardDuty                                                                                                                                         | Any                              | –                                   | Self                             | Self |
| Enable GuardDuty automatically for the entire organization<br>(`ALL`, `NEW`, `NONE`)                                                                     | All                              | –                                   | –                                | –    |
| View all Organizations member accounts regardless of GuardDuty status                                                                                    | Any                              | –                                   | –                                | –    |
| Generate sample findings                                                                                                                                 | Self                             | Self                                | Self                             | Self |
| View all GuardDuty findings                                                                                                                              | Any                              | Self                                | Any                              | Self |
| Archive GuardDuty findings                                                                                                                               | Any                              | –                                   | Any                              | –    |
| Apply suppression rules                                                                                                                                  | All                              | –                                   | All                              | –    |
| Create trusted IP list or threat lists                                                                                                                   | All                              | –                                   | All                              | –    |
| Update trusted IP list or threat lists                                                                                                                   | All                              | –                                   | All                              | –    |
| Delete trusted IP list or threat lists                                                                                                                   | All                              | –                                   | All                              | –    |
| Set EventBridge notification frequency                                                                                                                   | All                              | –                                   | All                              | –    |
| Set Amazon S3 location for exporting findings                                                                                                            | All                              | Self                                | Self                             | Self |
| Enable one or more optional protection plans for the entire<br>organization (`ALL`, `NEW`,<br>`NONE`)<br>This doesn't include Malware Protection for S3. | All                              | –                                   | –                                | –    |
| Enable any GuardDuty protection plan for individual accounts<br>This doesn't include Malware Protection for EC2 and Malware Protection for S3.           | Any                              | –                                   | Any                              | –    |
| Malware Protection for EC2                                                                                                                               | Any                              | –                                   | Self                             | –    |
| Malware Protection for EC2 – On-demand malware scan                                                                                                      | Any                              | Self                                | Self                             | Self |
| Malware Protection for S3                                                                                                                                | –                                | Self                                | –                                | Self |
| Disassociate a member account                                                                                                                            | Any+                             | –                                   | Any                              | –    |
| Disassociate from an administrator account                                                                                                               | –                                | –                                   | –                                | Self |
| Delete a disassociated member account                                                                                                                    | Any                              | –                                   | Any                              | –    |
| Suspend GuardDuty                                                                                                                                        | Any\*                            | –                                   | Any\*                            | –    |
| Disable GuardDuty                                                                                                                                        | Any\*                            | –                                   | Any\*                            | Self |

+Indicates that the delegated GuardDuty administrator account can take this action
only if they have not set up the auto-enable preferences to `ALL` the
organization members.

\*Indicates that a delegated GuardDuty administrator account can't disable GuardDuty in a
member account directly. The delegated GuardDuty administrator account must first disassociate the member account, and
then delete them. After this, each member account can disable GuardDuty in their own
accounts. For more information about performing these tasks in your organization, see
[Continually managing your member accounts within GuardDuty](maintaining-guardduty-organization-delegated-admin.md "maintaining-guardduty-organization-delegated-admin.md").

## Understanding member relationship status

GuardDuty API operations such as [ListMembers](../APIReference/API_ListMembers.md "../APIReference/API_ListMembers.md") and [GetMembers](../APIReference/API_GetMembers.md "../APIReference/API_GetMembers.md") return a
`relationshipStatus` field for each member account. This field indicates
the current state of the relationship between the administrator account and the member account.
Check this value when you want to confirm that GuardDuty is actively monitoring a member
account. It also helps you troubleshoot why a member account didn't finish onboarding
or is no longer being monitored. The following list describes the possible
values.

**`Created`**

The administrator account has added this account as a member (for example, by
calling CreateMembers), but the member relationship isn't
active yet.

**`Invited`**

The administrator account has sent an invitation to this member account, and the
invitation is waiting to be accepted.

**`Enabled`**

This member account is associated with the administrator account, and GuardDuty is
actively monitoring the member account.

**`Disabled`**

This member account is associated with the administrator account, but GuardDuty isn't
actively monitoring the member account.

**`Removed`**

This member account is no longer associated with the administrator account. This
status typically indicates that the administrator account removed the
association.

**`Resigned`**

This member account is no longer associated with the administrator account. This
status typically indicates that the member account removed itself from
the association.

**`Deleted`**

This member account no longer exists in GuardDuty.

**`EmailVerificationInProgress`**

This member account's invitation is pending email address
verification.

**`EmailVerificationFailed`**

This member account's invitation didn't pass email address
verification.

**`RegionDisabled`**

This member account can't be monitored because GuardDuty isn't enabled or
isn't available in the current AWS Region.

**`AccountSuspended`**

This member's AWS account is in a suspended state.

**`CannotCreateDetectorInOrganizationMasterAccount`**

GuardDuty can't create a detector in the AWS Organizations management account,
typically because the required service-linked role permissions are
missing.
