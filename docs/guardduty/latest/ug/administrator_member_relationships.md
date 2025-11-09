# Understanding the relationship

between GuardDuty administrator account and member accounts

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
| -------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------- | ----------------------------------- | -------------------------------- | ---- |
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
[Continually
managing your member accounts within GuardDuty](maintaining-guardduty-organization-delegated-admin.md "maintaining-guardduty-organization-delegated-admin.md").
