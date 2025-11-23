# Update an existing Recycle Bin retention rule

You can update an unlocked retention rule's
description, resource tags, and retention period at any time after creation. You
can't update a retention rule's resource type or unlock
delay period, even if the retention rule is unlocked.

You can't update a locked retention rule in any way. If you need to modify
a locked retention rule, you must first unlock it and wait for the unlock delay period to expire.

If you need to modify the unlock delay period for a locked retention
rule, you must [unlock the retention rule](recycle-bin-unlock.md "recycle-bin-unlock.md"),
and wait for the current unlock delay period to expire. When the unlock delay period
is expired, you must [relock the retention
rule](recycle-bin-lock.md "recycle-bin-lock.md") and specify the new unlock delay period.

###### Note

We recommend that you do not include personally identifying, confidential, or sensitive
information in the retention rule description.

After you update a retention rule, the changes only apply to new resources that it retains. The
changes do not affect resources that it previously sent to the Recycle Bin. For example, if
you update a retention rule's retention period, only snapshots that are deleted after the update
are retained for the new retention period. Snapshots that it sent to the Recycle Bin before the
update are still retained for the previous (old) retention period.

You can update a retention rule using one of the following methods.

Recycle Bin console

###### To update a retention rule

1. Open the Recycle Bin console at [https://console.aws.amazon.com/rbin/home/](https://console.aws.amazon.com/rbin/home/ "https://console.aws.amazon.com/rbin/home/")
2. In the navigation pane, choose **Retention rules**.
3. In the grid, select the retention rule to update, and choose
   **Actions**, **Edit retention
   rule**.
4. In the **Rule details** section, update **Retention rule name**
   and **Retention rule description** as needed.
5. In the **Rule settings** section, update the **Resource type**,
   **Resource tags to match**, and **Retention period** as needed.
6. In the **Tags** section, add or remove retention rule tags as needed.
7. Choose **Save retention rule**.

AWS CLI

###### To update a retention rule

Use the [update-rule](../../../cli/latest/reference/rbin/update-rule.md "../../../cli/latest/reference/rbin/update-rule.md")
AWS CLI command. For `--identifier`, specify the ID of the retention rule to update For
`--resource-types`, specify `EBS_VOLUME` for volumes, `EBS_SNAPSHOT` for snapshots, or `EC2_IMAGE`
for AMIs.

```
aws rbin update-rule \
--identifier `rule_ID` \
--retention-period RetentionPeriodValue=`number_of_days`,RetentionPeriodUnit=DAYS \
--resource-type `EBS_VOLUME|EBS_SNAPSHOT|EC2_IMAGE` \
--description "`rule_description`"
```

###### Example

The following example command updates retention rule `6lsJ2Fa9nh9` to retain
all snapshots for `7` days and updates its
description.

```
aws rbin update-rule \
--identifier 6lsJ2Fa9nh9 \
--retention-period RetentionPeriodValue=7,RetentionPeriodUnit=DAYS \
--resource-type EBS_SNAPSHOT \
--description "Retain for three weeks"
```
