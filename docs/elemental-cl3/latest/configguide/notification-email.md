

# Email notification
<a name="notification-email"></a>

You can configure AWS Elemental Conductor Live to email you notifications when alerts occur. 

**Note**  
Don't configure worker nodes to send email notifications. Conductor Live sends operational status for all nodes in the cluster and all transcoding channels.

Conductor Live uses open relay to send email notifications. Before subscribing to notifications, make sure that your network allows receipt of open relay email. If your network doesn't allow open relay messages, you must also configure a Sendmail relay server with another mail server.

**Important**  
If you subscribe to email notifications in a network that doesn't allow open relay messages and you do not relay the messages, the generated messages will collect on the Conductor Live system hard drive, eventually filling the partition and causing disk alert errors.

**To set up email notifications**

1. On the Conductor Live web interface, subscribe to all or some alerts using the steps described here:  
**Subscribe to all alerts**  

   1. On the Conductor Live web interface, go to the **Settings** page and make sure that you're on the **General** tab.

   1. Complete the **Global Alert Notification** fields as described in the following table and choose **Update**:    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/elemental-cl3/latest/configguide/notification-email.html)  
**Subscribe to individual alerts**  

   1. On the Conductor Live web interface, go to the **Stats** page and choose **Notifications**.

   1. On the **Notifications** page, find the alert that you want to be notified on and choose the plus sign (\+) to expand it.

   1. Complete the fields as described in the following table and choose **Save**.    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/elemental-cl3/latest/configguide/notification-email.html)

   1. For each alert that you want to be notified on, find the alert, then expand and complete the fields.

1. If your network doesn't allow open relay messages, configure the sendmail server to relay the messages. For steps, see [Configure sendmail relay server](notification-email-sendmail.md).