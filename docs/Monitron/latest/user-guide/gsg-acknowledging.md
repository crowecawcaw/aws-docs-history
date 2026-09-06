

Amazon Monitron is no longer open to new customers. Existing customers can continue to use the service as normal. For capabilities similar to Amazon Monitron, see our [blog post](https://aws.amazon.com/blogs/machine-learning/maintain-access-and-consider-alternatives-for-amazon-monitron).

# Step 3: Viewing and acknowledging a machine abnormality
<a name="gsg-acknowledging"></a>

The longer Amazon Monitron monitors a position, the more it fine-tunes its baseline and increases its accuracy. 

When an **Alarm** or a **Warning** is triggered, Amazon Monitron sends a notification to the mobile app that is displayed as an icon in the upper right of your screen ( ![Red warning icon with exclamation mark inside a white triangle.](http://docs.aws.amazon.com/Monitron/latest/user-guide/images/notification.png) ). 

Choosing the notification icon opens the **Notifications** page, which lists all pending notifications. 

![Notifications page showing an alarm notification for Pump Position 1 dated 11/02/2020.](http://docs.aws.amazon.com/Monitron/latest/user-guide/images/notification1.png)


When you receive a notification, you must view and acknowledge it. This doesn't fix the issue with the asset, it just lets Amazon Monitron know that you are aware of it. 

**To view and acknowledge an abnormality**

1. On the **Assets** list, choose the asset with the alarm.   
![Assets list showing Sorter 1 with error icon, Sorter 2 with warning icon, and multiple items with success icons.](http://docs.aws.amazon.com/Monitron/latest/user-guide/images/asset_list2.png)

1. Choose the position with the alarm to view the issue.    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/Monitron/latest/user-guide/gsg-acknowledging.html)

1. To confirm that you are aware of the issue, choose **Acknowledge**. 

   Note that the text on the following screens also indicates whether the alert notification was triggered based on the equipment's vibration or temperature, or by the vibration ISO thresholds or machine learning models. This information can be used by technicians to investigate and fix the issue. After an abnormality has been acknowledged and repaired, resolve the issue in the mobile app.   
![Vibration monitoring dashboard showing alarm status and total vibration chart for pump main.](http://docs.aws.amazon.com/Monitron/latest/user-guide/images/mobile-understand-sensor-measurement.png)

   The status of the asset changes to:   
![Blue button labeled "Maintenance" indicating a system or service status.](http://docs.aws.amazon.com/Monitron/latest/user-guide/images/maintenance-badge.png)

After the alarm has been acknowledged, the abnormality can be examined and fixed as appropriate.