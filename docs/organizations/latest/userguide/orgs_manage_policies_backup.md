# Backup policies

Backup policies allow you to centrally manage and apply backup plans to the AWS resources across an organization's accounts.

[AWS Backup](../../../aws-backup/latest/devguide.md "../../../aws-backup/latest/devguide.md") enables you to create [backup
plans](../../../aws-backup/latest/devguide/about-backup-plans.md "../../../aws-backup/latest/devguide/about-backup-plans.md") that define how to back up your AWS resources. The rules in the plan
include a variety of settings, such as the backup frequency, the time window during which
the backup occurs, the AWS Region containing the resources to back up and the vault in
which to store the backup. You can then apply a backup plan to groups of AWS resources
identified by using tags. You must also identify an AWS Identity and Access Management (IAM) role that grants AWS Backup
permission to perform the backup operation on your behalf.

Backup policies in AWS Organizations combine all of those pieces into [JSON](https://json.org "https://json.org") text documents. You can attach a backup policy to any of the elements in
your organization's structure, such as the root, organizational units (OUs), and individual
accounts. Organizations applies inheritance rules to combine the policies in the organization's root,
any parent OUs, or attached to the account. This results in an [effective backup policy](orgs_manage_policies_effective.md "orgs_manage_policies_effective.md") for each
account. This effective policy instructs AWS Backup how to automatically back up your AWS
resources.

## How backup policies work

Backup policies give you granular control over backing up your resources at whatever level
your organization requires. For example, you can specify in a policy attached to the
organization's root that all Amazon DynamoDB tables must be backed up. That policy can include a
default backup frequency. You can then attach a backup policy to OUs that override the
backup frequency according to the requirements of each OU. For example, the
`Developers` OU might specify a backup frequency of once per week, while the
`Production` OU specifies once per day.

You can create partial backup policies that individually include only part of the required
information to successfully back up your resources. You can attach these policies to
different parts of the organization tree, such as the root or a parent OU, with the
intention of those partial policies being inherited by lower-level OUs and accounts. When
Organizations combines all of the policies for an account by using inheritance rules, the resulting
effective policy must have all the required elements. Otherwise, AWS Backup considers the policy
not valid and does not back up the affected resources.

###### Important

AWS Backup can only perform a successful backup when it is invoked by a _complete_ effective policy that has all of the required
elements.

Although a partial policy strategy as described earlier can work, if an effective
policy for an account is incomplete, it results in errors or resources that are not
successfully backed up. As an alternate strategy, consider requiring that all backup
policies be complete and valid by themselves. Use _default_ values
supplied by policies attached higher in the hierarchy, and override them where needed in
child policies by including [inheritance child control
operators](policy-operators.md "policy-operators.md").

The effective backup plan for each AWS account in the organization appears in the AWS Backup
console as an immutable plan for that account. You can view it, but not change it.
You can, however, add or remove backup plan tags using [TagResource](../../../aws-backup/latest/devguide/API_TagResource.md "../../../aws-backup/latest/devguide/API_TagResource.md") and [UntagResource](../../../aws-backup/latest/devguide/API_UntagResource.md "../../../aws-backup/latest/devguide/API_UntagResource.md") APIs.

When AWS Backup begins a backup based on a policy-created backup plan, you can see the status
of the backup job in the AWS Backup console. A user in a member account can see the status and
any errors for the backup jobs in that member account. If you also enable trusted service
access with AWS Backup, a user in the organization's management account can see the status and errors
for all backup jobs in the organization. For more information, see [Enabling
cross-account management](../../../aws-backup/latest/devguide/manage-cross-account.md#enable-cross-account "../../../aws-backup/latest/devguide/manage-cross-account.md#enable-cross-account") in the _AWS Backup Developer Guide_.
