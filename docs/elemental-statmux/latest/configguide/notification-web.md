

This is version 2.20 of the AWS Elemental Statmux documentation. This is the latest version. For prior versions, see the *Previous Versions* section of [AWS Elemental Statmux and AWS Elemental Live Documentation](https://docs.aws.amazon.com/elemental-live).

# Web Callback Notification
<a name="notification-web"></a>

You can configure AWS Elemental Statmux to send you web callback notifications when alerts occur. 

To receive web callback notifications, you must have a web server that supports php scripting. Use the following steps to configure this server to receive alert notifications from AWS Elemental Statmux.

**To set up web callback notifications**

1. Use a text editor such as Notepad on a Windows system or Nano on Linux to create a `.php` file containing the following text:

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

1. Save the file in a directory on your web server. 

1. Subscribe to all or some alerts using the steps described here:  
**Subscribe to all alerts**  

   1. On the AWS Elemental Statmux web interface, go to the **Settings** page and ensure that you're on the **General** tab.

   1. Complete the **Global Alert Notification** fields, using the instructions in the following table as a guide. Choose **Update**.    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/elemental-statmux/latest/configguide/notification-web.html)  
**Subscribe to individual alerts**  

   1. On the AWS Elemental Statmux web interface, hover over **Stats** page and choose **Alerts**.

   1. On the **Alerts** page, choose **Configure Alerts**.

   1. In the list of alerts, locate the alert that you want to be notified on and choose it to expand it.

   1. Complete the fields, using the instructions in the following table as a guide. Choose **Update**.    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/elemental-statmux/latest/configguide/notification-web.html)

   1. Locate, expand, and complete the fields for each alert of which you want to be notified.

1. Test your setup by typing the following at the command line of the AWS Elemental Statmux node:

   ```
   curl -X POST -d {{"param1=value1&param2=value2" http://yourdomain.com}}/webcallback/notification.php
   ```

1. Open your `notify.php` to check that it was updated. The text of your file should contain something like this:

   ```
   <?xml version="1.0" encoding="UTF-8"?>
   <job href="/jobs/3401">
     <node>earhart</node>
     <user_data></user_data>
     <submitted>2014-11-14 01:27:05 -0800</submitted>
     <priority>50</priority>
     <status>preprocessing</status>
     <pct_complete>0</pct_complete>
     <average_fps>0.0</average_fps>
     <elapsed>0</elapsed>
     <start_time>2014-11-14 01:27:06 -0800</start_time>
     <elapsed_time_in_words>00:00:00</elapsed_time_in_words>
   </job>
   param1=value&param2=value2
   ```

1. Enter your web callback URL into a web browser to see the HTTP post.