# Macie administrator and member account

relationships

If you centrally manage multiple Amazon Macie accounts as an organization, the Macie administrator has
access to Amazon Simple Storage Service (Amazon S3) inventory data, policy findings, and certain Macie settings and
resources for associated member accounts. The administrator can also enable automated sensitive data discovery and
run sensitive data discovery jobs to detect sensitive data in S3 buckets that member accounts own. Support
for specific tasks varies based on whether a Macie administrator account is associated with a member
account through AWS Organizations or by invitation.

The following table provides details about the relationship between Macie administrator and member
accounts. It indicates the default permissions for each type of account. To further restrict
access to Macie features and operations, you can use custom [AWS Identity and Access Management (IAM) policies](security-iam.md "security-iam.md").

In the table:

- **Self** indicates that the account can't perform the task for
  any associated accounts.
- **Any** indicates that the account can perform the task for an
  individual associated account.
- **All** indicates that the account can perform the task and
  the task applies to all associated accounts.
  A dash (–) indicates that the account can’t perform the task.

| **Task**                                                                                                                                                               | **Through AWS Organizations** | **By invitation** |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------- | ----------------- | ---------- | ---- |
| **Administrator**                                                                                                                                                      | **Member**                    | **Administrator** | **Member** |
| Enable Macie                                                                                                                                                           | Any                           | –                 | Self       | Self |
| Review the organization's account inventory [1](#accounts-mgmt-relationships-note-inventory "#accounts-mgmt-relationships-note-inventory")                             | All                           | –                 | All        | –    |
| Add a member account                                                                                                                                                   | Any                           | –                 | Any        | –    |
| Review statistics and metadata for S3 buckets                                                                                                                          | All                           | Self              | All        | Self |
| Review policy findings                                                                                                                                                 | All                           | Self              | All        | Self |
| Suppress (archive) policy findings [2](#accounts-mgmt-relationships-note-suppress-policy "#accounts-mgmt-relationships-note-suppress-policy")                          | All                           | –                 | All        | –    |
| Publish policy findings [3](#accounts-mgmt-relationships-note-publish-policy "#accounts-mgmt-relationships-note-publish-policy")                                       | Self                          | Self              | Self       | Self |
| Configure a repository for sensitive data discovery results [4](#accounts-mgmt-relationships-note-sddr "#accounts-mgmt-relationships-note-sddr")                       | Self                          | Self              | Self       | Self |
| Create and use allow lists                                                                                                                                             | Self                          | Self              | Self       | Self |
| Create and use custom data identifiers                                                                                                                                 | Self                          | Self              | Self       | Self |
| Configure automated sensitive data discovery settings                                                                                                                  | All                           | –                 | All        | –    |
| Enable or disable automated sensitive data discovery                                                                                                                   | Any                           | –                 | Any        | –    |
| Review automated sensitive data discovery statistics, data, and results [5](#accounts-mgmt-relationships-note-asdd-sdfs "#accounts-mgmt-relationships-note-asdd-sdfs") | All                           | Self              | All        | Self |
| Create and run sensitive data discovery jobs [6](#accounts-mgmt-relationships-note-jobs "#accounts-mgmt-relationships-note-jobs")                                      | Any                           | Self              | Any        | Self |
| Review the details of sensitive data discovery jobs [7](#accounts-mgmt-relationships-note-job-details "#accounts-mgmt-relationships-note-job-details")                 | Self                          | Self              | Self       | Self |
| Review sensitive data findings [8](#accounts-mgmt-relationships-note-jobs-sdfs "#accounts-mgmt-relationships-note-jobs-sdfs")                                          | Self                          | Self              | Self       | Self |
| Suppress (archive) sensitive data findings [8](#accounts-mgmt-relationships-note-jobs-sdfs "#accounts-mgmt-relationships-note-jobs-sdfs")                              | Self                          | Self              | Self       | Self |
| Publish sensitive data findings [8](#accounts-mgmt-relationships-note-jobs-sdfs "#accounts-mgmt-relationships-note-jobs-sdfs")                                         | Self                          | Self              | Self       | Self |
| Configure Macie to retrieve sensitive data samples for findings                                                                                                        | Self                          | Self              | Self       | Self |
| Retrieve sensitive data samples for findings [9](#accounts-mgmt-relationships-note-sdsamples "#accounts-mgmt-relationships-note-sdsamples")                            | Self                          | Self              | Self       | Self |
| Configure publication destinations for findings                                                                                                                        | Self                          | Self              | Self       | Self |
| Set the publication frequency for findings                                                                                                                             | All                           | Self              | All        | Self |
| Create sample findings                                                                                                                                                 | Self                          | Self              | Self       | Self |
| Review account quotas and estimated usage costs                                                                                                                        | All                           | Self              | All        | Self |
| Suspend Macie [10](#accounts-mgmt-relationships-note-suspend "#accounts-mgmt-relationships-note-suspend")                                                              | Any                           | –                 | Any        | Self |
| Disable Macie [11](#accounts-mgmt-relationships-note-disable "#accounts-mgmt-relationships-note-disable")                                                              | Self                          | Self              | Self       | Self |
| Remove (disassociate) a member account                                                                                                                                 | Any                           | –                 | Any        | –    |
| Disassociate from an administrator account                                                                                                                             | –                             | –                 | –          | Self |
| Delete an association with another account [12](#accounts-mgmt-relationships-note-delete "#accounts-mgmt-relationships-note-delete")                                   | Any                           | –                 | Any        | Self |

1. The administrator for an organization in AWS Organizations can review all accounts in
   the organization, including accounts that haven’t enabled Macie. The administrator
   for an invitation-based organization can review only those accounts that they add to
   their inventory.
2. Only an administrator can suppress policy findings. If an
   administrator creates a suppression rule, Macie applies the rule to policy
   findings for all accounts in the organization unless the rule is configured to
   exclude specific accounts. If a member creates a suppression rule, Macie doesn’t
   apply the rule to policy findings for the member’s account.
3. Only the account that owns an affected resource can publish policy findings for
   the resource to AWS Security Hub CSPM. Both administrator and member accounts automatically
   publish policy findings for an affected resource to Amazon EventBridge.
4. If an administrator enables automated sensitive data discovery or configures a job to analyze
   objects in S3 buckets that a member account owns, Macie stores the sensitive data
   discovery results in the repository for the administrator account.
5. Only an administrator can access sensitive data findings that automated sensitive data discovery
   produces. Both an administrator and a member can review other types of data
   that automated sensitive data discovery produces for the member's account.
6. A member can configure a job to analyze objects only in S3 buckets that their
   account owns. An administrator can configure a job to analyze objects in
   buckets that their account owns or a member account owns. For information about how
   quotas are applied and costs are calculated for multiple-account jobs, see [Understanding estimated
   usage costs](account-mgmt-costs-calculations.md "account-mgmt-costs-calculations.md").
7. Only the account that creates a job can access the job's details. This includes
   job-related details in the S3 bucket inventory.
8. Only the account that creates a job can access, suppress, or publish sensitive
   data findings that the job produces. Only an administrator can access, suppress, or
   publish sensitive data findings that automated sensitive data discovery produces.
9. If a sensitive data finding applies to an S3 object that a member account owns, the
   administrator might be able to retrieve samples of sensitive data reported by
   the finding. This depends on the source of the finding, and configuration settings
   and resources in the administrator account and the member account. For more
   information, see [Configuration options
   for retrieving sensitive data samples](findings-retrieve-sd-options.md "findings-retrieve-sd-options.md").
10. For an administrator to suspend Macie for their own account, the
    administrator must first disassociate their account from all member
    accounts.
11. For an administrator to disable Macie for their own account, the
    administrator must first disassociate their account from all member accounts,
    and delete the associations between their account and all of those accounts. The
    administrator for an organization in AWS Organizations can do this by working with the
    organization's management account to designate a different account as the
    administrator account.

For a member of an AWS Organizations organization to disable Macie, the administrator
must first disassociate the member's account from their administrator account. In
an invitation-based organization, the member can disassociate their account from its
administrator account, and then disable Macie. 12. The administrator for an organization in AWS Organizations can delete an association
with a member account after they disassociate the account from their
administrator account. The account continues to appear in the administrator's
account inventory, but its status indicates that it's not a member account. In an
invitation-based organization, an administrator and a member can delete an
association with another account after they disassociate their account from the
other account. The other account then stops appearing in their account
inventory.
