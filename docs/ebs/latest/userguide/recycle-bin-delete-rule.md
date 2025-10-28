# Delete a Recycle Bin retention rule to stop it

from retaining resources

You can delete a retention rule at any time. When you delete a retention rule, it no longer
retains new resources in the Recycle Bin after they have been deleted. Resources
that were sent to the Recycle Bin before the retention rule was deleted continue
to be retained in the Recycle Bin according to the retention period defined in the
retention rule. When the period expires, the resource is permanently deleted from
the Recycle Bin.

You can delete a retention rule using one of the following methods.

Recycle Bin console

###### To delete a retention rule

1. Open the Recycle Bin console at [https://console.aws.amazon.com/rbin/home/](https://console.aws.amazon.com/rbin/home/ "https://console.aws.amazon.com/rbin/home/")
2. In the navigation pane, choose **Retention rules**.
3. In the grid, select the retention rule to delete, and choose
   **Actions**, **Delete retention
   rule**.
4. When prompted, enter the confirmation message and choose **Delete retention rule**.

AWS CLI

###### To delete a retention rule

Use the [delete-rule](../../../cli/latest/reference/rbin/delete-rule.md "../../../cli/latest/reference/rbin/delete-rule.md")
AWS CLI command. For `--identifier`, specify the ID of the retention rule to delete.

```
aws rbin delete-rule --identifier `rule_ID`
```

###### Example

The following example command deletes retention rule `6lsJ2Fa9nh9`.

```
aws rbin delete-rule --identifier 6lsJ2Fa9nh9
```
