# How Amazon Data Lifecycle Manager works

The following are the key elements of Amazon Data Lifecycle Manager.

###### Elements

- [Policies](#dlm-policies "#dlm-policies")
- [Policy schedules](#dlm-lifecycle-schedule "#dlm-lifecycle-schedule")
- [Target resource tags](#dlm-tagging-volumes "#dlm-tagging-volumes")
- [Snapshots](#dlm-ebs-snapshots "#dlm-ebs-snapshots")
- [EBS-backed AMIs](#dlm-ebs-amis "#dlm-ebs-amis")
- [Amazon Data Lifecycle Manager tags](#dlm-tagging-snapshots "#dlm-tagging-snapshots")

## Policies

With Amazon Data Lifecycle Manager, you create policies to define your backup creation and retention requirements.
These policies typically specify the following:

- **Policy type** — Defines the type of backup
  resources that the policy manages (snapshots or EBS-backed AMIs).
- **Target resources** — Defines the type of
  resources that are targeted by the policy (instances or EBS volumes).
- **Creation frequency** — Defines how often the
  policy runs and creates snapshots or AMIs.
- **Retention threshold** — Defines how long the
  policy retains snapshots or AMIs after creation.
- **Additional actions** — Defines additional
  actions that the policy should perform, such as cross-Region copying, archiving,
  or resource tagging.

Amazon Data Lifecycle Manager offers default policies and custom policies.

###### Default policies

Default policies back up all volumes and instances in a Region that do not have
recent backups. You can optionally exclude volumes and instances by specifying
exclusion parameters.

Amazon Data Lifecycle Manager supports the following default policies:

- Default policy for EBS snapshots — Targets volumes and automates the
  creation, retention, and deletion of snapshots.
- Default policy for EBS-backed AMIs — Targets instances and automates
  the creation, retention, and deregistration of EBS-backed AMIs.

You can have only one default policy per resource type in each account and AWS
Region.

###### Custom policies

Custom policies target specific resources based on their assigned tags and support
advanced features, such as fast snapshot restore, snapshot archiving, cross-account
copying, and pre and post scripts. A custom policy can include up to 4 schedules,
where each schedule can have its own creation frequency, retention threshold, and
advanced feature configuration.

Amazon Data Lifecycle Manager supports the following custom policies:

- EBS snapshot policy — Targets volumes or instances and automates the
  creation, retention, and deletion of EBS snapshots.
- EBS-backed AMI policy — Targets instances and automates the creation,
  retention, and deregistration of EBS-backed AMIs.
- Cross-account copy event policy — Automates cross-Region copy actions
  for snapshots that are shared with you.

For more information, see [Amazon Data Lifecycle Manager default policies vs custom policies](policy-differences.md "policy-differences.md").

## Policy schedules (\*custom policies

only\*)

Policy schedules define when snapshots or AMIs are created by the policy. Policies
can have up to four schedules—one mandatory schedule, and up to three optional
schedules.

Adding multiple schedules to a single policy lets you create snapshots or AMIs at
different frequencies using the same policy. For example, you can create a single
policy that creates daily, weekly, monthly, and yearly snapshots. This eliminates the
need to manage multiple policies.

For each schedule, you can define the frequency, fast snapshot restore settings
(snapshot lifecycle policies only), cross-Region copy rules, and tags. The tags that
are assigned to a schedule are automatically assigned to the snapshots or AMIs that
are created when the schedule is initiated. In addition, Amazon Data Lifecycle Manager automatically assigns
a system-generated tag based on the schedule's frequency to each snapshot or AMI.

Each schedule is initiated individually based on its frequency. If multiple schedules
are initiated at the same time, Amazon Data Lifecycle Manager creates only one snapshot or AMI and applies the
retention settings of the schedule that has the highest retention period. The tags of
all of the initiated schedules are applied to the snapshot or AMI.

- (Snapshot lifecycle policies only) If more than one of the initiated schedules
  is enabled for fast snapshot restore, then the snapshot is enabled for fast
  snapshot restore in all of the Availability Zones specified across all of the
  initiated schedules. The highest retention settings of the initiated schedules
  is used for each Availability Zone.
- If more than one of the initiated schedules is enabled for cross-Region copy,
  the snapshot or AMI is copied to all Regions specified across all of the initiated
  schedules. The highest retention period of the initiated schedules is applied.

## Target resource tags (\*custom policies

only\*)

Amazon Data Lifecycle Manager custom policies use resource tags to identify the resources to back up. When you
create a snapshot or EBS-backed AMI policy, you can specify multiple target resource tags.
All resources of the specified type (instance or volume) that have at least one of the
specified target resource tags will be targeted by the policy. For example, if you create
a snapshot policy that targets volumes and you specify `purpose=prod`,
`costcenter=prod`, and `environment=live` as target resource tags,
then the policy will target all volumes that have any of those tag-key value pairs.

If you want to run multiple policies on a resource, you can assign multiple tags to the
target resource, and then create separate policies that each target a specific resource
tag.

You can't use the `\` or `=` characters in a tag key. Target
resource tags are case sensitive. For more information, see [Tag your resources](../../../AWSEC2/latest/UserGuide/Using_Tags.md "../../../AWSEC2/latest/UserGuide/Using_Tags.md").

## Snapshots

Snapshots are the primary means to back up data from your EBS volumes. To save storage
costs, successive snapshots are incremental, containing only the volume data that changed
since the previous snapshot. When you delete one snapshot in a series of snapshots for a
volume, only the data that's unique to that snapshot is removed. The rest of the captured
history of the volume is preserved. For more information, see [Amazon EBS snapshots](ebs-snapshots.md "ebs-snapshots.md").

## EBS-backed AMIs

An Amazon Machine Image (AMI) provides the information that's required to launch an
instance. You can launch multiple instances from a single AMI when you need multiple
instances with the same configuration. Amazon Data Lifecycle Manager supports EBS-backed AMIs only. EBS-backed
AMIs include a snapshot for each EBS volume that's attached to the source instance. For
more information, see [Amazon Machine Images (AMI)](../../../AWSEC2/latest/UserGuide/AMIs.md "../../../AWSEC2/latest/UserGuide/AMIs.md").

## Amazon Data Lifecycle Manager tags

Amazon Data Lifecycle Manager applies the following system tags to all snapshots and AMIs created by a policy, to distinguish
them from snapshots and AMIs created by any other means:

- `aws:dlm:lifecycle-policy-id`
- `aws:dlm:lifecycle-schedule-name`
- `aws:dlm:expirationTime` — For snapshots created by an age-based
  schedule. Indicates when the snapshot is to be deleted from the standard tier.
- `dlm:managed`
- `aws:dlm:archived` — For snapshots that were archived by a schedule.
- `aws:dlm:pre-script` — For snapshots created with pre scripts.
- `aws:dlm:post-script` — For snapshots created with post scripts.

You can also specify custom tags to be applied to snapshots and AMIs on creation. You can't use
the `\` or `=` characters in a tag key.

The target tags that Amazon Data Lifecycle Manager uses to associate volumes with a snapshot policy can optionally be
applied to snapshots created by the policy. Similarly, the target tags that are used to associate
instances with an AMI policy can optionally be applied to AMIs created by the policy.
