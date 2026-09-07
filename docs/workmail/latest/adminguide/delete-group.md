

End of support notice: On March 31, 2027, AWS will end support for Amazon WorkMail. After March 31, 2027, you will no longer be able to access the Amazon WorkMail console or Amazon WorkMail resources. For more information, see [Amazon WorkMail end of support](https://docs.aws.amazon.com/workmail/latest/adminguide/workmail-end-of-support.html). 

# Deleting a group
<a name="delete-group"></a>

Before you can delete a group, you must first disable that group. For information about disabling groups, see [Disabling groups](disable-group.md).

**To delete a group**

1. Open the Amazon WorkMail console at [https://console.aws.amazon.com/workmail/](https://console.aws.amazon.com/workmail/).

   If necessary, change the AWS Region. In the bar at the top of the console window, open the **Select a Region** list and choose a Region. For more information, see [Regions and endpoints](https://docs.aws.amazon.com/general/latest/gr/rande.html) in the *Amazon Web Services General Reference*.

1. In the navigation pane, choose **Organizations**, then choose the name of your organization.

1. In the navigation pane, choose **Groups**.

1. Select the check box next to the disabled group that you want to delete and choose **Delete**.

   The **Delete** dialog box appears.

1. In the **Enter the group name to confirm deletion** box, enter the name of the group, then choose **Delete **.

**Note**  
To permanently delete a group, use the `DeleteGroup` API action for Amazon WorkMail. For more information, see [DeleteGroup](https://docs.aws.amazon.com/workmail/latest/APIReference/API_DeleteGroup.html) in the *Amazon WorkMail API Reference*.