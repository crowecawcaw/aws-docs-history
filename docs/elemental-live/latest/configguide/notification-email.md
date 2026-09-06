

# Email notification
<a name="notification-email"></a>

You can configure AWS Elemental Live to email you notifications when alerts occur. 

Elemental Live uses open relay to send email notifications. Before subscribing to notifications, make sure that your network allows receipt of open relay email. If your network doesn't allow open relay messages, you must also configure a Sendmail relay server with another mail server.

**Important**  
If you subscribe to email notifications in a network that doesn't allow open relay messages and you do not relay the messages, the generated messages will collect on the Elemental Live system hard drive, eventually filling the partition and causing disk alert errors.

**To set up email notifications**

1. On the Elemental Live web interface, subscribe to all or some alerts using the steps described here:  
**Subscribe to all alerts**  

   1. On the Elemental Live web interface, go to the **Settings** page and ensure that you're on the **General** tab.

   1. Complete the **Global Alert Notification** fields, using the instructions in the following table as a guide. Choose **Update**.    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/elemental-live/latest/configguide/notification-email.html)  
**Subscribe to individual alerts**  

   1. On the Elemental Live web interface, hover over **Stats** page and choose **Alerts**.

   1. On the **Alerts** page, choose **Configure Alerts**.

   1. In the list of alerts, locate the alert that you want to be notified on and choose it to expand it.

   1. Complete the fields, using the instructions in the following table as a guide. Choose **Update**.    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/elemental-live/latest/configguide/notification-email.html)

   1. Locate, expand, and complete the fields for each alert on which you want to be notified.

1. If your network doesn't allow open relay messages, configure the Sendmail server to relay the messages. For steps, see [Configure Sendmail relay server](notification-email-sendmail.md).