# Deleting a group

Before you can delete a group, you must first disable that group. For information about disabling groups,
see [Disabling groups](disable-group.md "disable-group.md").

###### To delete a group

1. Open the Amazon WorkMail console at
   [https://console.aws.amazon.com/workmail/](https://console.aws.amazon.com/workmail/ "https://console.aws.amazon.com/workmail/").

If necessary, change the AWS Region. In the bar at the top of the console window, open the **Select a Region** list and choose a Region. For more information, see [Regions and endpoints](../../../general/latest/gr/rande.md "../../../general/latest/gr/rande.md") in the
_Amazon Web Services General Reference_. 2. In the navigation pane, choose **Organizations**, then choose the name of your organization. 3. In the navigation pane, choose **Groups**. 4. Select the check box next to the disabled group that you want to delete and choose **Delete**.

The **Delete** dialog box appears. 5. In the **Enter the group name to confirm deletion** box,
enter the name of the group, then choose **Delete** .

###### Note

To permanently delete a group, use the `DeleteGroup` API action for Amazon WorkMail. For more information, see [DeleteGroup](../APIReference/API_DeleteGroup.md "../APIReference/API_DeleteGroup.md") in the _Amazon WorkMail API Reference_.
