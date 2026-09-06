

# Creating an ActiveMQ broker user
<a name="amazon-mq-listing-managing-users"></a>

An ActiveMQ *user* is a person or an application that can access the queues and topics of an ActiveMQ broker. You can configure users to have specific permissions. For example, you can allow some users to access the [ActiveMQ Web Console](https://activemq.apache.org/web-console.html).

A *group* is a semantic label. You can assign a group to a user and configure permissions for groups to send to, receive from, and administer specific queues and topics.

**Note**  
You can't configure groups independently of users. A group label is created when you add at least one user to it and deleted when you remove all users from it.

**Note**  
 The `activemq-webconsole` group in ActiveMQ on Amazon MQ has admin permissions on all queues and topics. All users in this group will have admin access. 

The following examples show how you can create, edit, and delete Amazon MQ broker users using the AWS Management Console.

## Create a new ActiveMQ broker user
<a name="create-new-user-console"></a>

1. Sign in to the [Amazon MQ console](https://console.aws.amazon.com/amazon-mq/).

1. From the broker list, choose the name of your broker (for example, **MyBroker**) and then choose **View details**.

   On the **{{MyBroker}}** page, in the **Users** section, all the users for this broker are listed.  
![Table showing two users with their console access and group information.](http://docs.aws.amazon.com/amazon-mq/latest/developer-guide/images/amazon-mq-tutorials-list-users.png)

1. Choose **Create user**.

1. In the **Create user** dialog box, type a **Username** and **Password**.

1. (Optional) Type the names of groups to which the user belongs, separated by commas (for example: `Devs, Admins`).

1. (Optional) To enable the user to access the [ActiveMQ Web Console](https://activemq.apache.org/web-console.html), choose **ActiveMQ Web Console**.

1. Choose **Create user**.
**Important**  
Making changes to a user does *not* apply the changes to the user immediately. To apply your changes, you must wait for the next maintenance window or [reboot the broker](amazon-mq-rebooting-broker.md).