This is version 2.18 of the AWS Elemental Server documentation.
This is the latest version. For prior versions, see
the _Previous Versions_ section of [AWS Elemental Conductor File and AWS Elemental Server Documentation](../../../elemental-server.md "../../../elemental-server.md").

# Web Callback Notification

You can configure AWS Elemental Server to send you web callback notifications when alerts
occur.

To receive web callback notifications, you must have a web server that supports a
service-side script such as nodeJS or PHP. Use the following steps to configure this server
with PHP install to receive alert notifications from AWS Elemental Server.

###### To set up web callback notifications

1. Use a text editor such as Notepad on a Windows system or Nano on Linux to create a
   `.php` file containing the following text.

```
<?php
    function get_raw_post(){
        $data = @file_get_contents('php://input');
        if ($data){
            return $data;
        }
            return "nothing passed";
        }

    $file = "../webcallback/notify";
    $fh = fopen($file, "a");
    $data = get_raw_post();
    fwrite($fh, $data);
    fclose($fh);
?>
```

2. Save the file in a directory on your web server.
3. Subscribe to all or some alerts using the steps described here:

**Subscribe to all alerts**

    1. On the AWS Elemental Server web interface, go to the **Settings** page and ensure that you're on the **General** tab.
    2. Complete the **Global Alert Notification** fields as described in the
     following table and choose **Update**.

| Field                              | Instructions                                                                                                                                                                                                                                                                                                |
| ---------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Notification: Email**            | If you want to receive email notifications too, enter the email address of the alert recipient. If your network doesn't allow open relay messages, see [Configure Sendmail Relay Server](notification-email-sendmail.md "notification-email-sendmail.md") to configure a sendmail server to relay messages. |
| **Notification: Web Callback URL** | Enter the URL of the appropriate `.php` file on your web server.Required if you don't provide an address in the **Email** field.                                                                                                                                                                            |
| **Notify**                         | Select when you want to be notified, either when the alert is raised, or when it's cleared. You can choose both options.                                                                                                                                                                                    |
| **Notes**                          | Add optional notes as needed.                                                                                                                                                                                                                                                                               | **Subscribe to individual alerts** 1. On the AWS Elemental Server web interface, hover over **Stats** page and choose **Alerts**. 2. On the **Alerts** page, choose **Configure Alerts**. 3. In the list of alerts, locate the alert that you want to be notified on and choose it to expand it. 4. Complete the fields as described in the following table and choose **Update**.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| Field                              | Instructions                                                                                                                                                                                                                                                                                                |
| ---                                | ---                                                                                                                                                                                                                                                                                                         |
| **Notification: Email**            | If you want to receive email notifications too, enter the email address of the alert recipient. If your network doesn't allow open relay messages, see [Configure Sendmail Relay Server](notification-email-sendmail.md "notification-email-sendmail.md") to configure a sendmail server to relay messages. |
| **Notification: Web Callback URL** | Enter the URL of the appropriate `.php` file on your web server.Required if you don't provide an address in the **Email** field.                                                                                                                                                                            |
| **Notify**                         | Select when you want to be notified, either when the alert is raised or when it's cleared. You can choose both options.                                                                                                                                                                                     |
| **Notes**                          | Add optional notes as needed.                                                                                                                                                                                                                                                                               | 5. Locate, expand, and complete the fields for each alert that you want to be notified on. 4. Test your setup by typing the following at the command line of the AWS Elemental Server node: ``curl -X POST -d `"param1=value1&param2=value2" https://yourdomain.com`/webcallback/notification.php`` 5. Open your `notify.php` to check that it was updated. The text of your file should contain something like this: `<?xml version="1.0" encoding="UTF-8"?> <job href="/jobs/3401"> <node>earhart</node> <user_data></user_data> <submitted>2014-11-14 01:27:05 -0800</submitted> <priority>50</priority> <status>preprocessing</status> <pct_complete>0</pct_complete> <average_fps>0.0</average_fps> <elapsed>0</elapsed> <start_time>2014-11-14 01:27:06 -0800</start_time> <elapsed_time_in_words>00:00:00</elapsed_time_in_words> </job> param1=value&param2=value2` 6. Enter your web callback URL into a web browser to see the HTTP post. |
