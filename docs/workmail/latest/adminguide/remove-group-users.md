

End of support notice: On March 31, 2027, AWS will end support for Amazon WorkMail. After March 31, 2027, you will no longer be able to access the Amazon WorkMail console or Amazon WorkMail resources. For more information, see [Amazon WorkMail end of support](https://docs.aws.amazon.com/workmail/latest/adminguide/workmail-end-of-support.html). 

# Removing members from a group
<a name="remove-group-users"></a>

Use the Amazon WorkMail console to remove members from a group.

**Note**  
If Amazon WorkMail is integrated with a connected Active Directory or Microsoft Active Directory, you can use Active Directory to manage your group members. However, doing so can create the time needed to propagate your changes to Amazon WorkMail.

**To remove members from a group**

1. Open the Amazon WorkMail console at [https://console.aws.amazon.com/workmail/](https://console.aws.amazon.com/workmail/).

   If necessary, change the AWS Region. In the bar at the top of the console window, open the **Select a Region** list and choose a Region. For more information, see [Regions and endpoints](https://docs.aws.amazon.com/general/latest/gr/rande.html) in the *Amazon Web Services General Reference*.

1. In the navigation pane, choose **Organizations**, then choose the name of your organization.

1. In the navigation pane, choose **Groups**, then choose the name of the group.

1. On the **Group details** page, choose the **Members** tab.

1. Select the member to remove from the group.

1. Choose **Remove**.

Your changes can take a few minutes to propagate.