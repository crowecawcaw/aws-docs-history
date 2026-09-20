

This is version 2.20 of the AWS Elemental Statmux documentation. This is the latest version. For prior versions, see the *Previous Versions* section of [AWS Elemental Statmux and AWS Elemental Live Documentation](https://docs.aws.amazon.com/elemental-live).

# Email Notification
<a name="notification-email"></a>

You can configure AWS Elemental Statmux to email you notifications when alerts occur. 

AWS Elemental Statmux uses open relay to send email notifications. Before subscribing to notifications, make sure that your network allows receipt of open relay email. If your network doesn't allow open relay messages, you must also configure a Sendmail relay server with another mail server.

**Important**  
If you subscribe to email notifications in a network that doesn't allow open relay messages and you do not relay the messages, the generated messages will collect on the AWS Elemental Statmux system hard drive, eventually filling the partition and causing disk alert errors.

**To set up email notifications**

1. On the AWS Elemental Statmux web interface, subscribe to all or some alerts using the steps described here:  
**Subscribe to all alerts**  

   1. On the AWS Elemental Statmux web interface, go to the **Settings** page and ensure that you're on the **General** tab.

   1. Complete the **Global Alert Notification** fields, using the instructions in the following table as a guide. Choose **Update**.


<table>
<thead>
  <tr><th>Field</th><th>Instructions</th></tr>
</thead>
<tbody>
  <tr><td><b>Notification: Email</b></td><td>Enter the email address of the alert recipient. Required if you don't provide a URL in the <b>Web Callback URL</b> field.</td></tr>
  <tr><td><b>Notification: Web Callback URL</b></td><td>If you want to receive web server notifications too, enter the URL of the appropriate <code>.php</code> file on your web server.For instructions on how to configure your web server for notifications, see <a href="notification-web.md">Web Callback Notification</a>.</td></tr>
  <tr><td><b>Notify</b></td><td>Select when you want to be notified, either when the alert is raised or when it's cleared. You can choose both options.</td></tr>
  <tr><td><b>Notes</b></td><td>Add optional notes as needed.</td></tr>
</tbody>
</table>
  
**Subscribe to individual alerts**  

   1. On the AWS Elemental Statmux web interface, hover over **Stats** page and choose **Alerts**.

   1. On the **Alerts** page, choose **Configure Alerts**.

   1. In the list of alerts, locate the alert that you want to be notified on and choose it to expand it.

   1. Complete the fields, using the instructions in the following table as a guide. Choose **Update**.


<table>
<thead>
  <tr><th>Field</th><th>Instructions</th></tr>
</thead>
<tbody>
  <tr><td><b>Notification: Email</b></td><td>Enter the email address of the alert recipient. This is required if you don't provide a URL in the <b>Web Callback URL</b> field.</td></tr>
  <tr><td><b>Notification: Web Callback URL</b></td><td>If you want to receive web server notifications too, enter the URL of the appropriate <code>.php</code> file on your web server.For instructions on how to configure your web server for notifications, see <a href="notification-web.md">Web Callback Notification</a>.</td></tr>
  <tr><td><b>Notify</b></td><td>Select when you want to be notified, either when the alert is raised or when it's cleared. You can choose both options.</td></tr>
  <tr><td><b>Notes</b></td><td>Add optional notes as needed.</td></tr>
</tbody>
</table>


   1. Locate, expand, and complete the fields for each alert on which you want to be notified.

1. If your network doesn't allow open relay messages, configure the Sendmail server to relay the messages. For steps, see [Configure Sendmail Relay Server](notification-email-sendmail.md).