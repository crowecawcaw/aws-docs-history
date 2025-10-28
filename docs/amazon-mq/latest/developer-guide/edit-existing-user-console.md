# Edit an ActiveMQ broker user

To edit an existing user, do the following:

1. Sign in to the [Amazon MQ console](https://console.aws.amazon.com/amazon-mq/ "https://console.aws.amazon.com/amazon-mq/").
2. From the broker list, choose the name of your broker (for example, **MyBroker**)
   and then choose **View details**.

On the **`MyBroker`** page, in the **Users** section, all the users for this broker are listed.

![Table showing two users with their console access and group information.](images/amazon-mq-tutorials-list-users.png) 3. Select your sign-in credentials and choose **Edit**.

The **Edit user** dialog box is displayed. 4. (Optional) Type a new **Password**. 5. (Optional) Add or remove the names of groups to which the user belongs,
separated by commas (for example: `Managers, Admins`). 6. (Optional) To enable the user to access the [ActiveMQ Web
Console](http://activemq.apache.org/web-console.html "http://activemq.apache.org/web-console.html"), choose **ActiveMQ Web
Console**. 7. To save the changes to the user, choose **Done**.

###### Important

Making changes to a user does _not_ apply the changes to the user immediately.
To apply your changes, you must wait for the next maintenance window
or [reboot the broker](amazon-mq-rebooting-broker.md "amazon-mq-rebooting-broker.md").
