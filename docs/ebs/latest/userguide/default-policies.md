# Create Amazon Data Lifecycle Manager default policies

To create periodic EBS-backed AMIs from instances, use the default policy
for EBS-backed AMIs. To create snapshots of all volumes regardless of their
attachment state, or if you want to exclude specific volumes, use the default
policy for EBS snapshots.

This section explains how to create default policies.

###### Topics

- [Considerations for default policies](#default-policy-considerations "#default-policy-considerations")
- [Create default policy for Amazon EBS snapshots](#default-snapshot-policy "#default-snapshot-policy")
- [Create default policy for EBS-backed AMIs](#default-ami-policy "#default-ami-policy")
- [Enable default policies across accounts and Regions](dlm-stacksets.md "dlm-stacksets.md")

## Considerations for default policies

Keep the following in mind when working with default policies:

- Default policies do not back up target resources (instances or volumes) that
  have recent backups (snapshots or AMIs). The creation frequency determines
  which resources are backed up. A volume or instance is backed up only if its
  last snapshot or AMI is older than the policy's creation frequency. For
  example, if you specify a creation frequency of 3 days, the default policy for
  EBS snapshots will create a snapshot of a volume only if its last snapshot is
  older than 3 days.
- By default, default policies target all instances or volumes in the Region,
  unless exclusion parameters are specified.
- Default policies will create a minimum set of unique snapshots. For example,
  if you enable the EBS-backed AMI policy and the EBS snapshot policy, the
  snapshot policy will not duplicate snapshots of volumes that were already backed
  up by the EBS-backed AMI policy.
- Default policies will only start targeting resources that are at least 24
  hours old.
- If you delete a volume or terminate an instance targeted by a default policy,
  Amazon Data Lifecycle Manager will continue to delete the previously created backups (snapshots or AMIs)
  according to the retention period up to, but not including, the last backup. You
  must manually delete this backup if it is not required.

If you want Amazon Data Lifecycle Manager to delete the last backup, you can enable _extend
deletion_.

- If a default policy is deleted or enters the error or disabled state, Amazon Data Lifecycle Manager
  stops deleting the previously created backups (snapshots or AMIs). If you want
  Amazon Data Lifecycle Manager to continue deleting backups, including the last one, you must enable
  _extend deletion_ before deleting the policy or before the
  policy's state changes to disabled or deleted.
- When you create and enable a default policy, Amazon Data Lifecycle Manager randomly assigns targeted
  resources to a four-hour time window. Targeted resources are backed up during
  their assigned window at the specified creation frequency. For example, if a
  policy has a creation frequency of 3 days, and a target resource is assigned
  to the 12:00 - 16:00 window, that resource will be backed up between 12:00 -
  16:00 every 3 days.

## Create default policy for Amazon EBS snapshots

The following procedure shows you how to create a default policy for EBS snapshots.

Console

###### To create a default policy for EBS snapshots

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the navigation panel, choose **Lifecycle Manager** and
   then choose **Create lifecycle policy**.
3. For **Policy type**, choose **Default policy**
   and then choose **EBS snapshot policy**.
4. For **Description**, enter a brief description for the
   policy.
5. For **IAM role**, choose the IAM role that has permissions
   to manage snapshots.

We recommend that you choose **Default** to use the default
IAM role provided by Amazon Data Lifecycle Manager. However, you can also use a custom IAM role that
you previously created.

[Show moreShow less](# "#") 6. For **Creation frequency**, specify how often you want the policy to
run and create snapshots of your volumes.

The frequency that you specify also determines which volumes are backed up.
The policy will only back up volumes that have not been backed up by any other
means within the specified frequency. For example, if you specify a creation
frequency of 3 days, the policy will only create snapshots of volumes that have
not been backed up within the last 3 days.

[Show moreShow less](# "#") 7. For **Retention period**, specify how long you want the policy
to retain the snapshots that it creates. When a snapshot reaches the retention
threshold, it is automatically deleted. The retention period must be greater than
or equal to the creation frequency. 8. (_Optional_) Configure the **Exclusion parameters**
to exclude specific volumes from the scheduled backups. Excluded volumes will
not be backed up when the policy runs.

    1. To exclude boot volumes, select  **Exclude boot volumes**.
     If you exclude boot volumes, only data (non-boot) volumes will be backed
     up by the policy. In other words, it will not create snapshots of volumes
     that are attached to instances as a boot volume.
    2. To exclude specific volume types, choose **Exclude specific
     volume types**, and then select the volume types to exclude.
     Only volumes of the remaining types will be backed up by the policy.
    3. To exclude volumes that have specific tags, choose **Add tag**,
     and then specify the tag keys and values. The policy will not create snapshots
     of volumes that have any of the specified tags.

[Show moreShow less](# "#") 9. (_Optional_) In the **Advanced settings**,
specify additional actions that the policy should perform.

    1. To copy assigned tags from the source volumes to their snapshots, select
     **Copy tags from volumes**.
    2. With **Extend deletion** disabled:




    	* If a source volume is deleted, Amazon Data Lifecycle Manager continues to delete previously
    	 created snapshots up to, but not including, the last one based on the
    	 retention period. If you want Amazon Data Lifecycle Manager to delete all snapshots,
    	 including the last one, select **Extend deletion**.
    	* If a policy is deleted or enters the `error` or `disabled`
    	 state, Amazon Data Lifecycle Manager stops deleting snapshots. If you want Amazon Data Lifecycle Manager to continue
    	 deleting snapshots, including the last one, select **Extend
    	 deletion**.
    ###### Note

    If you enable extend deletion, you override both behaviors described above
     simultaneously.
    3. To copy snapshots created by the policy to other Regions, select
     **Create cross-Region copy** and then select up to 3
     destination Regions.




    	* If the source snapshot is encrypted, or if encryption by default
    	 is enabled for the destination Region, the copied snapshots are
    	 encrypted using the default KMS key for EBS encryption in the
    	 destination Region.
    	* If the source snapshot is unencrypted and encryption by default
    	 is disabled for the destination Region, the copied snapshots are
    	 unencrypted.

[Show moreShow less](# "#") 10. (_Optional_) To add a tag to the policy, choose **Add
tag** and then specify the tag key and value pair. 11. Choose **Create default policy**.

###### Note

If you get the `Role with name AWSDataLifecycleManagerDefaultRole already exists` error,
see [Troubleshoot Amazon Data Lifecycle Manager issues](dlm-troubleshooting.md "dlm-troubleshooting.md") for more information.

AWS CLI

###### To create a default policy for EBS snapshots

Use the [create-lifecycle-policy](../../../cli/latest/reference/dlm/create-lifecycle-policy.md "../../../cli/latest/reference/dlm/create-lifecycle-policy.md") command. You can specify the request parameters
in one of two methods, depending on your use case or preferences:

- **Method 1**

```
`$` aws dlm create-lifecycle-policy \
--state `ENABLED | DISABLED` \
--description "`policy_description`" \
--execution-role-arn `role_arn` \
--default-policy VOLUME \
--create-interval `creation_frequency_in_days (1-7)` \
--retain-interval `retention_period_in_days (2-14)` \
`--copy-tags | --no-copy-tags` \
`--extend-deletion | --no-extend-deletion` \
--cross-region-copy-targets TargetRegion=`destination_region_code` \
--exclusions ExcludeBootVolumes=`true | false`, ExcludeTags=[{Key=`tag_key`,Value=`tag_value`}], ExcludeVolumeTypes="`standard | gp2 | gp3 | io1 | io2 | st1 | sc1`"
```

For example, to create a default policy for EBS snapshots that targets all
volumes in the Region, uses the default IAM role, runs daily (default), and retains
snapshots for 7 days (default), you need to specify the following parameters:

```
`$` aws dlm create-lifecycle-policy \
--state ENABLED \
--description "Daily default snapshot policy" \
--execution-role-arn arn:aws:iam::`account_id`:role/AWSDataLifecycleManagerDefaultRole \
--default-policy VOLUME
```

- **Method 2**

```
`$` aws dlm create-lifecycle-policy \
--state `ENABLED | DISABLED` \
--description "`policy_description`" \
--execution-role-arn `role_arn` \
--default-policy VOLUME \
--policy-details file://policyDetails.json
```

Where `policyDetails.json` includes the following:

```
{
    "PolicyLanguage": "SIMPLIFIED",
    "PolicyType": "EBS_SNAPSHOT_MANAGEMENT",
    "ResourceType": "VOLUME",
    "CopyTags": `true | false`,
    "CreateInterval": `creation_frequency_in_days (1-7)`,
    "RetainInterval": `retention_period_in_days (2-14)`,
    "ExtendDeletion": `true | false`,
    "CrossRegionCopyTargets": [{"TargetRegion":"`destination_region_code`"}],
    "Exclusions": {
        "ExcludeBootVolume": `true | false`,
		"ExcludeVolumeTypes": ["`standard | gp2 | gp3 | io1 | io2 | st1 | sc1`"],
        "ExcludeTags": [{
            "Key": "`exclusion_tag_key`",
            "Value": "`exclusion_tag_value`"
        }]
    }
}
```

## Create default policy for EBS-backed AMIs

The following procedure shows you how to create a default policy for EBS-backed AMIs.

Console

###### To create a default policy for EBS-backed AMIs

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the navigation panel, choose **Lifecycle Manager** and
   then choose **Create lifecycle policy**.
3. For **Policy type**, choose **Default policy**
   and then choose **EBS-backed AMI policy**.
4. For **Description**, enter a brief description for the
   policy.
5. For **IAM role**, choose the IAM role that has permissions
   to manage AMIs.

We recommend that you choose **Default** to use the default
IAM role provided by Amazon Data Lifecycle Manager. However, you can also use a custom IAM role that
you previously created.

[Show moreShow less](# "#") 6. For **Creation frequency**, specify how often you want the policy to
run and create AMIs from your instances.

The frequency that you specify also determines which instances are backed up.
The policy will only back up instances that have not been backed up by any other
means within the specified frequency. For example, if you specify a creation
frequency of 3 days, the policy will only create AMIs from instances that have
not been backed up within the last 3 days.

[Show moreShow less](# "#") 7. For **Retention period**, specify how long you want the policy
to retain the AMIs that it creates. When an AMI reaches the retention threshold,
it is automatically deregistered and its associated snapshots are deleted. The
retention period must be greater than or equal to the creation frequency. 8. (_Optional_) Configure the **Exclusion parameters**
to exclude specific instances from the scheduled backups. Excluded instances will
not be backed up when the policy runs.

    1. To exclude instances that have specific tags, choose **Add tag**,
     and then specify the tag keys and values. The policy will not create AMIs
     from instances that have any of the specified tags.

[Show moreShow less](# "#") 9. (_Optional_) In the **Advanced settings**,
specify additional actions that the policy should perform.

    1. To copy assigned tags from the source instances to their AMIs, select
     **Copy tags from instances**.
    2. With **Extend deletion** disabled:




    	* If a source instance is terminated, Amazon Data Lifecycle Manager continues to deregister
    	 previously created AMIs up to, but not including, the last one based on
    	 the retention period. If you want Amazon Data Lifecycle Manager to deregister all AMIs,
    	 including the last one, select **Extend deletion**.
    	* If a policy is deleted or enters the `error` or `disabled`
    	 state, Amazon Data Lifecycle Manager stops deregistering AMIs. If you want Amazon Data Lifecycle Manager to continue deregistering AMIs,
    	 including the last one, select **Extend deletion**.
    ###### Note

    If you enable extended deletion, you override both behaviors described
     above simultaneously.
    3. To copy AMIs created by the policy to other Regions, select
     **Create cross-Region copy** and then select up to 3
     destination Regions.




    	* If the source AMI is encrypted, or if encryption by default
    	 is enabled for the destination Region, the copied AMIs are
    	 encrypted using the default KMS key for EBS encryption in the
    	 destination Region.
    	* If the source AMI is unencrypted and encryption by default
    	 is disabled for the destination Region, the copied AMIs are
    	 unencrypted.

[Show moreShow less](# "#") 10. (_Optional_) To add a tag to the policy, choose
**Add tag** and then specify the tag key and value
pair. 11. Choose **Create default policy**.

###### Note

If you get the `Role with name AWSDataLifecycleManagerDefaultRoleForAMIManagement already exists` error,
see [Troubleshoot Amazon Data Lifecycle Manager issues](dlm-troubleshooting.md "dlm-troubleshooting.md") for more information.

AWS CLI

###### To create a default policy for EBS-backed AMIs

Use the [create-lifecycle-policy](../../../cli/latest/reference/dlm/create-lifecycle-policy.md "../../../cli/latest/reference/dlm/create-lifecycle-policy.md") command. You can specify the request parameters
in one of two methods, depending on your use case or preferences:

- **Method 1**

```
`$` aws dlm create-lifecycle-policy \
--state `ENABLED | DISABLED` \
--description "`policy_description`" \
--execution-role-arn `role_arn` \
--default-policy INSTANCE \
--create-interval `creation_frequency_in_days (1-7)` \
--retain-interval `retention_period_in_days (2-14)` \
`--copy-tags | --no-copy-tags` \
`--extend-deletion | --no-extend-deletion` \
--cross-region-copy-targets TargetRegion=`destination_region_code` \
--exclusions ExcludeTags=[{Key=`tag_key`,Value=`tag_value`}]
```

For example, to create a default policy for EBS-backed AMIs that targets all
instances in the Region, uses the default IAM role, runs daily (default), and retains
AMIs for 7 days (default), you need to specify the following parameters:

```
`$` aws dlm create-lifecycle-policy \
--state ENABLED \
--description "Daily default AMI policy" \
--execution-role-arn arn:aws:iam::`account_id`:role/AWSDataLifecycleManagerDefaultRoleForAMIManagement \
--default-policy INSTANCE
```

- **Method 2**

```
`$` aws dlm create-lifecycle-policy \
--state `ENABLED | DISABLED` \
--description "`policy_description`" \
--execution-role-arn `role_arn` \
--default-policy INSTANCE \
--policy-details file://policyDetails.json
```

Where `policyDetails.json` includes the following:

```
{
    "PolicyLanguage": "SIMPLIFIED",
    "PolicyType": "IMAGE_MANAGEMENT",
    "ResourceType": "INSTANCE",
    "CopyTags": `true | false`,
    "CreateInterval": `creation_frequency_in_days (1-7)`,
    "RetainInterval": `retention_period_in_days (2-14)`,
    "ExtendDeletion": `true | false`,
	"CrossRegionCopyTargets": [{"TargetRegion":"`destination_region_code`"}],
    "Exclusions": {
        "ExcludeTags": [{
            "Key": "`exclusion_tag_key`",
            "Value": "`exclusion_tag_value`"
        }]
    }
}
```
