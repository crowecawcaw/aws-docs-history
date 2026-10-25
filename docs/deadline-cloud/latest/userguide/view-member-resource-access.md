

# View and change resource access for a user or group
<a name="view-member-resource-access"></a>

Use the **Resource access** tab to check what one user or group can reach, for example when someone changes teams or leaves your organization. You find the tab on the details page for each user and group. On the tab, you can see every farm, queue, and fleet that the user or group can access, in every AWS Region. You can also change or revoke that access. For information about assigning access starting from a farm, queue, or fleet, see [Assign permissions to users and groups](assign-permissions-procedure.md).

**To view resource access for a user or group**

1. Sign in to the AWS Management Console and open the Deadline Cloud [console](https://console.aws.amazon.com/deadlinecloud/home).

1. In the left navigation pane, choose **User management**.

1. On the **User management** page, choose the **Users** or **Groups** tab.

1. Choose the name of the user or group to open its details page.

1. On the details page, choose the **Resource access** tab.

   The following screenshot shows the **Resource access** tab for a user. The user has direct access to three farms in the Tokyo, Ireland, and Virginia Regions, and access to one queue through the Lighting group.  
![Resource access table with the Revoke access and Change access level buttons above it.](https://docs.aws.amazon.com/deadline-cloud/latest/userguide/images/user-resource-access.png)

1. In the table, review the **Resource type**, **Resource**, **Access level**, **Region**, and **Granted through** values for each farm, queue, or fleet.

Access to a farm includes the queues and fleets inside it, and those aren't listed separately. A user with the owner level on a farm shows one row for the farm rather than a row for every resource in it.

The **Granted through** column shows where each access level comes from:
+ **Direct** means the user or group was added to the resource itself. You can change or revoke this access on the **Resource access** tab.
+ The name of a group means the user inherits the access from that group. To change it, change the group's access level on the resource, or change which groups the user belongs to in your identity source.

**To change an access level**

1. On the **Resource access** tab, select the resources to change.

1. Choose **Change access level**.

1. Choose the new access level, and then choose **Change access level**. Every resource you selected is set to that level.

**To revoke access**

1. On the **Resource access** tab, select the resources to revoke.

1. Choose **Revoke access**.

1. Review the list of resources, and then choose **Revoke access**. Revoking access to a farm also revokes access to the queues and fleets inside it.

Some rows can't be changed on this tab:
+ Access that a user inherits from a group is changed on the group.
+ Access to a job comes from submitting that job, so it isn't editable at all.

Clear those rows from your selection to use the **Change access level** and **Revoke access** buttons.

When Deadline Cloud can't check a Region, the tab names that Region rather than leaving it out, so a partial list is never mistaken for a complete one. An account policy that blocks a Region produces this result, and no action is needed. If you expect access in a Region that the tab names, confirm that the Region isn't blocked for your account, and then choose the refresh button.