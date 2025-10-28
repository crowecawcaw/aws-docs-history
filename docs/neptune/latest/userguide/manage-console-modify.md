# Modifying a Neptune DB Cluster Using the

Console

When you modify a DB instance using the AWS Management Console, you can choose to apply the changes right
away by selecting **Apply Immediately**. If you choose to apply changes
immediately, your new changes and any changes in the pending modifications queue are applied at
once.

If you don't choose to apply changes immediately, the changes are put into the pending
modifications queue. During the next maintenance window, any pending changes in the queue are
applied.

###### Important

If any pending modifications require downtime, choosing to apply changes immediately can
cause unexpected downtime for the DB instance in question. There is no downtime for the other
DB instances in the DB cluster.

###### Note

When you modify a DB cluster in Neptune, the **Apply Immediately**
setting only affects changes to the **DB cluster identifier**, **IAM
DB authentication**. All other modifications are applied immediately, regardless of
the value of the **Apply Immediately** setting.

###### To modify a DB cluster using the console

1. Sign in to the AWS Management Console, and open the Amazon Neptune console at [https://console.aws.amazon.com/neptune/home](https://console.aws.amazon.com/neptune/home "https://console.aws.amazon.com/neptune/home").
2. In the navigation pane, choose **Clusters**, and then choose the DB
   cluster that you want to modify.
3. Choose **Actions**, and then choose **Modify
   cluster**. The **Modify DB cluster** page appears.
4. Change any of the settings that you want.

###### Note

On the console, some instance level changes only apply to the current DB instance,
whereas others apply to the entire DB cluster. To change a setting that modifies the
entire DB cluster at the instance level on the console, follow the instructions in [Modifying a DB Instance in a DB
Cluster](#manage-console-modify-instance "#manage-console-modify-instance"). 5. When all the changes are as you want them, choose **Continue** and
check the summary. 6. To apply the changes immediately, select **Apply immediately**. 7. On the confirmation page, review your changes. If they are correct, choose
**Modify cluster** to save your changes.

To edit your changes, choose **Back**, or to cancel your changes,
choose **Cancel**.

## Modifying a DB Instance in a DB

Cluster

###### To modify a DB Instance in a DB cluster using the console

1. Sign in to the AWS Management Console, and open the Amazon Neptune console at [https://console.aws.amazon.com/neptune/home](https://console.aws.amazon.com/neptune/home "https://console.aws.amazon.com/neptune/home").
2. In the navigation pane, choose **Instances**, and then choose the DB
   instance that you want to modify.
3. Choose **Instance actions**, and then choose
   **Modify**. The **Modify DB Instance** page
   appears.
4. Change any of the settings that you want.

###### Note

Some settings apply to the entire DB cluster and must be changed at the cluster
level. To change those settings, follow the instructions in [Modifying a Neptune DB Cluster Using the
Console](manage-console-modify.md "manage-console-modify.md").

In the AWS Management Console, some instance-level changes apply only to the current DB
instance, whereas others apply to the entire DB cluster. 5. When all the changes are as you want them, choose **Continue** and
check the summary. 6. To apply the changes immediately, select **Apply
immediately**. 7. On the confirmation page, review your changes. If they are correct, choose
**Modify DB Instance** to save your changes.

To edit your changes, choose **Back**, or to cancel your changes,
choose **Cancel**.
