

# Delete quick responses in Connect Customer
<a name="delete-qr"></a>

This topic explains how to use the Connect Customer admin website to delete a quick response. To delete a quick response programmatically, see [DeleteQuickResponse](https://docs.aws.amazon.com/amazon-q-connect/latest/APIReference/API_DeleteQuickResponse.html) in the *agent assist API Reference Guide*.

**Important**  
You can't undo a deletion.
Agents can't see or use deleted quick responses.

**To delete a response**

1. Log in to the Connect Customer admin website at https://*instance name*.my.connect.aws/. Use an **Admin** account, or an account assigned to a security profile that has **Content Management - Quick responses - Delete** permission.

1. On the navigation bar, choose **Content Management**, then **Quick responses**.  
![Menu showing Content Management and Quick responses.](http://docs.aws.amazon.com/connect/latest/adminguide/images/agent-application-1.png)

1. On the **Quick responses** page, select the checkbox next to the response that you want to delete. You can select a maximum of 20 responses.

1. Choose **Delete**.

   A success message appears:  
![A green checkmark and the words Successfully Deleted selected Quick response.](http://docs.aws.amazon.com/connect/latest/adminguide/images/deletion-success-message.png)

**Note**  
If the **Delete** button is inactive, sign in to a Connect Customer account that has the required security profile, or ask another admin for help.
Remain on the page until the delete operation finishes. 