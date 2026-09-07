

End of support notice: On March 31, 2027, AWS will end support for Amazon WorkMail. After March 31, 2027, you will no longer be able to access the Amazon WorkMail console or Amazon WorkMail resources. For more information, see [Amazon WorkMail end of support](https://docs.aws.amazon.com/workmail/latest/adminguide/workmail-end-of-support.html). 

# Editing resource details
<a name="edit_resource"></a>

You can edit a resource's general details, including name, description, type, and email address, booking options, and delegates. 

**To edit general resource details**



1. Open the Amazon WorkMail console at [https://console.aws.amazon.com/workmail/](https://console.aws.amazon.com/workmail/).

   If necessary, change the AWS Region. In the bar at the top of the console window, open the **Select a Region** list and choose a Region. For more information, see [Regions and endpoints](http://docs.aws.amazon.com/general/latest/gr/index.html?rande.html) in the *Amazon Web Services General Reference*.

1. In the navigation pane, choose **Organizations**, then choose the name of your organization.

1. In the navigation pane, choose **Resources**, and then select the resource to edit.

1. On the **Resource details** page, update the **Resource name**, **Description**, **Resource Type**, or **Email address** as needed.

1. By default, resources are displayed in the global address list. To hide the resource from the global address list, clear the **Show in global address list** check box.

1. Choose **Save changes**.

You can configure a resource to accept or decline booking requests automatically.

You can edit the resource's booking options.

**To change a resource's booking options**

1. Open the Amazon WorkMail console at [https://console.aws.amazon.com/workmail/](https://console.aws.amazon.com/workmail/).

   

   If necessary, change the AWS Region. In the bar at the top of the console window, open the **Select a Region** list and choose a Region. For more information, see [Regions and endpoints](http://docs.aws.amazon.com/general/latest/gr/index.html?rande.html) in the *Amazon Web Services General Reference*.

1. In the navigation pane, choose **Organizations**, and then choose the name of your organization.

1. In the navigation pane, choose **Resources**, and then select the resource to edit. A page appears and displays **Resource details**.

1. Under **Booking options** choose **Edit**.

1. As required, select or clear the check box next to an option to enable or disable the option.
**Note**  
When you disable any of the automatic booking options, you must create a delegate to handle the booking requests. The next steps explain how to create delegate. 

You can add a delegate to control booking requests for a resource that doesn't have automatic booking options configured. Resource delegates automatically receive copies of all booking requests and have full access to the resource calendar. In addition, they must accept all booking requests for a resource.

**To add a resource delegate**

1. Open the Amazon WorkMail console at [https://console.aws.amazon.com/workmail/](https://console.aws.amazon.com/workmail/).

   If necessary, change the AWS Region. In the bar at the top of the console window, open the **Select a Region** list and choose a Region. For more information, see [Regions and endpoints](http://docs.aws.amazon.com/general/latest/gr/index.html?rande.html) in the *Amazon Web Services General Reference*.

1. In the navigation pane, choose **Organizations**, then choose the name of your organization.

1. In the navigation pane, choose **Resources**, and then select the name of the resource to which you want to add a delegate.

1. (Optional) In the **Booking options** tab, choose **Edit**, clear the **Automatically accept all resource requests** check box, and then choose **Save**.

1. Choose the **Delegates** tab, and then choose **Add delegate**. 

   The **Add delegate** dialog box appears.

1. Open the **Search delegates** list and choose a delegate, then choose **Save**.

**To remove a resource delegate**

1. Open the Amazon WorkMail console at [https://console.aws.amazon.com/workmail/](https://console.aws.amazon.com/workmail/).

   If necessary, change the AWS Region. In the bar at the top of the console window, open the **Select a Region** list and choose a Region. For more information, see [Regions and endpoints](http://docs.aws.amazon.com/general/latest/gr/index.html?rande.html) in the *Amazon Web Services General Reference*.

1. In the navigation pane, choose **Organizations**, and then choose the name of the organization from which you want to remove delegates. 

1. In the navigation pane, choose **Resources**, and then select the name of the resource from which you want to remove a delegate.

1. Choose **Delegates**, and then choose the delegate to remove.

1. Chooose **Remove**.