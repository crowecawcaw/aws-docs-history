

# Delete an ActiveMQ broker user
<a name="delete-existing-user-console"></a>

 When you no longer need a user, you can delete the user. 

1. Sign in to the [Amazon MQ console](https://console.aws.amazon.com/amazon-mq/).

1. From the broker list, choose the name of your broker (for example, **MyBroker**) and then choose **View details**.

   On the **{{MyBroker}}** page, in the **Users** section, all the users for this broker are listed.  
![Table showing two users with their console access and group information.](http://docs.aws.amazon.com/amazon-mq/latest/developer-guide/images/amazon-mq-tutorials-list-users.png)

1. Select a your sign-in credentials (for example, **{{MyUser}}**) and then choose **Delete**.

1. To confirm deleting the user, in the **Delete {{MyUser}}?** dialog box, choose **Delete**.
**Important**  
Making changes to a user does *not* apply the changes to the user immediately. To apply your changes, you must wait for the next maintenance window or [reboot the broker](amazon-mq-rebooting-broker.md).