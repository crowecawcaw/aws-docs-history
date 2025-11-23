# Create a Recycle Bin retention rule

When you create a retention rule, you must specify the following required parameters:

- The resource type to protect (volumes, snapshots, or AMIs).
- The type of retention rule (tag-level or Region-level). Tag-level rules protect only
  resources that have specific tags. Region-level rules protect all resources in the Region,
  but can exclude resources that have specific tags.
- The retention period to retain resources after they are deleted. After this period expires, the
  resources are permanently deleted from the Recycle Bin. The supported retention periods are:

      + EBS volumes: 1 - 7 days
      + EBS snapshots and EBS-backed AMIs: 1 - 365 days

  You can also optionally specify a rule name and description of up to 255 characters each, and
  tags to help you identify and organize your rules. We recommend that you do not include personally
  identifying, confidential, or sensitive information in the name, description, or tags.

You can also optionally lock Region-level retention rules on creation.
If you lock a retention rule on creation, you must also specify the unlock delay period,
which can be 7 to 30 days. Retention rules remain unlocked by default unless you explicitly
lock them.

###### Note

Retention rules function only in the Regions in which they are created. If you intend to use
Recycle Bin in other Regions, you must create additional retention rules in those Regions.

You can create a Recycle Bin retention rule using one of the following methods.

Recycle Bin console

###### To create a tag-level retention rule

1. Open the Recycle Bin console at [https://console.aws.amazon.com/rbin/home/](https://console.aws.amazon.com/rbin/home/ "https://console.aws.amazon.com/rbin/home/")
2. In the navigation pane, choose **Retention rules**, and then choose
   **Create retention rule**.
3. (_Optional_) For **Retention rule name**, enter
   a descriptive name for the retention rule.
4. (_Optional_) For **Retention rule description**,
   enter a brief description for the retention rule.
5. For **Resource type**, select the type of resource for the retention
   rule to protect. The retention rule will retain only resources of this type in the
   Recycle Bin.
6. For **Select the resources to retain**, choose **Retain
   resources that have specific tags**.
7. For **Resource tags**, enter the tag key and value pairs to use to
   identify the resources to retain in the Recycle Bin. Only resources of the specified
   type that have at least one of the specified tag will be retained by the retention
   rule.
8. For **Retention period**, enter the number of days to retain deleted
   resources in the Recycle Bin.
9. Choose **Create retention rule**.

###### To create a Region-level retention rule

1. Open the Recycle Bin console at [https://console.aws.amazon.com/rbin/home/](https://console.aws.amazon.com/rbin/home/ "https://console.aws.amazon.com/rbin/home/")
2. In the navigation pane, choose **Retention rules**, and then choose
   **Create retention rule**.
3. (_Optional_) For **Retention rule name**, enter
   a descriptive name for the retention rule.
4. (_Optional_) For **Retention rule description**,
   enter a brief description for the retention rule.
5. For **Resource type**, select the type of resource for the retention
   rule to protect. The retention rule will retain only resources of this type in the
   Recycle Bin.
6. For **Select the resources to retain**, choose **Retain all
   resources**.
7. (_Optional_) To exclude resources that have specific tags, for
   **Exclusion tags**, enter up to five tag key and value pairs to use
   to identify the resources to exclude. Resources that have any of these tags are ignored
   by the retention rule.
8. For **Retention period**, enter the number of days to retain deleted
   resources in the Recycle Bin.
9. (_Optional_) To lock the retention rule, for **Rule lock
   settings**, select **Lock**, and then for **Unlock delay
   period**, specify the unlock delay period in days. A locked retention rule
   can't be modified or deleted. To modify or delete the rule, you must first unlock it and
   then wait for the unlock delay period to expire. For more information, see
   [Lock a Recycle Bin retention rule to prevent
   it from being updated or deleted](recycle-bin-lock.md "recycle-bin-lock.md")

To leave the retention rule unlocked, for **Rule lock settings**, keep
**Unlock** selected. An unlocked retention rule can be modified or
deleted at any time.

###### Note

You can't lock Region-level retention rules that have exclusion tags. 10. Choose **Create retention rule**.

AWS CLI

###### To create a retention rule

Use the [create-rule](../../../cli/latest/reference/rbin/create-rule.md "../../../cli/latest/reference/rbin/create-rule.md")
AWS CLI command. For `--retention-period`, specify the number of days to retain deleted snapshots
in the Recycle Bin. For `--resource-type`, specify `EBS_VOLUME` for volumes, `EBS_SNAPSHOT` for snapshots, or
`EC2_IMAGE` for AMIs. To create a tag-level retention rule, for `--resource-tags`,
specify the tags to use to identify the resources that are to be retained. To create a Region-level
retention rule, omit `--resource-tags`, and optionally specify `--exclude-resource-tags`,
to exclude resources that have specific tags. To lock a Region-level retention
rule, include `--lock-configuration`, and specify the unlock delay period in days.

```
aws rbin create-rule \
--retention-period RetentionPeriodValue=`number_of_days`,RetentionPeriodUnit=DAYS \
--resource-type `EBS_VOLUME|EBS_SNAPSHOT|EC2_IMAGE` \
--description "`rule_description`" \
--lock-configuration 'UnlockDelay={UnlockDelayUnit=DAYS,UnlockDelayValue=`unlock_delay_in_days`}' \
--resource-tags ResourceTagKey=`tag_key`,ResourceTagValue=`tag_value` \
--exclude-resource-tags ResourceTagKey=`tag_key`,ResourceTagValue=`tag_value`
```

###### Example 1

The following example command creates an unlocked
Region-level retention rule that retains all deleted
snapshots for a period of `7` days.

```
aws rbin create-rule \
--retention-period RetentionPeriodValue=7,RetentionPeriodUnit=DAYS \
--resource-type EBS_SNAPSHOT \
--description "Match all snapshots"
```

###### Example 2

The following example command creates a tag-level rule that retains deleted snapshots
that are tagged with `purpose=production` for a period of
`7` days.

```
aws rbin create-rule \
--retention-period RetentionPeriodValue=7,RetentionPeriodUnit=DAYS \
--resource-type EBS_SNAPSHOT \
--description "Match snapshots with a specific tag" \
--resource-tags ResourceTagKey=purpose,ResourceTagValue=production
```

###### Example 3

The following example command creates a locked
Region-level retention rule that retains all deleted snapshots for a
period of `7` days. The
retention rule is locked with an unlock delay period of 7
days.

```
aws rbin create-rule \
--retention-period RetentionPeriodValue=7,RetentionPeriodUnit=DAYS \
--resource-type EBS_SNAPSHOT \
--description "Match all snapshots" \
--lock-configuration 'UnlockDelay={UnlockDelayUnit=DAYS,UnlockDelayValue=7}'
```

###### Example 4

The following example command creates an unlocked
Region-level retention rule that retains all deleted snapshots, except
snapshots that are tagged with `purpose:testing`, for a period of
`7` days.

```
aws rbin create-rule \
--retention-period RetentionPeriodValue=7,RetentionPeriodUnit=DAYS \
--resource-type EBS_SNAPSHOT \
--description "Match only production snapshots" \
--exclude-resource-tags ResourceTagKey=purpose,ResourceTagValue=testing
```
