

Amazon Monitron is no longer open to new customers. Existing customers can continue to use the service as normal. For capabilities similar to Amazon Monitron, see our [blog post](https://aws.amazon.com/blogs/machine-learning/maintain-access-and-consider-alternatives-for-amazon-monitron).

# Understanding asset status
<a name="anom-monitor-assets"></a>

When a sensor detects a machine abnormality, the status of the asset changes. When a problem occurs, you can see it in the **Assets** list in the Amazon Monitron app. 

**Topics**
+ [The Assets list](#anom-asset-list)
+ [Asset and position status](#anom-asset-icons)
+ [Notifications](#anom-notifications)

## The Assets list
<a name="anom-asset-list"></a>

The **Assets** list displays every asset in your site or project, showing the assets for the site or project that you are currently viewing. For more information about sites and projects, see [Navigating between projects and sites in the mobile app](SM-working-project-and-site.md).

When you open the Amazon Monitron mobile app, it displays the list of assets associated with the site or project that you last worked with. To navigate to the **Assets** list from elsewhere in the app, use the following procedure.

**To open the assets list in either the mobile app or the web app**

1. Choose the menu icon (☰). 

1. Choose **Assets**.

   The assets list is displayed.    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/Monitron/latest/user-guide/anom-monitor-assets.html)

## Asset and position status
<a name="anom-asset-icons"></a>

The **Assets** list shows the status of each listed asset with an icon, as shown in the following table. 


| Status | Meaning | 
| --- | --- | 
|  ![Green circular icon with a white checkmark symbol inside.](http://docs.aws.amazon.com/Monitron/latest/user-guide/images/healthy_icon.png)  |  **Healthy state**: The status of all sensor positions on the asset is healthy.  | 
|  ![Yellow triangular warning sign with black exclamation mark.](http://docs.aws.amazon.com/Monitron/latest/user-guide/images/warning_icon.png)  |  **Warning state**: A warning has been triggered for one of the positions of this asset, indicating that Amazon Monitron has detected early signs of potential failure. Amazon Monitron identifies warning conditions by analyzing equipment vibration and temperature, using a combination of machine learning and ISO vibration standards. | 
|  ![Red hexagonal warning sign with exclamation mark indicating caution or alert.](http://docs.aws.amazon.com/Monitron/latest/user-guide/images/alarm_icon.png)  | **Alarm state**: An alarm has been triggered for one of the positions of this asset, indicating that the machine vibration and temperature is out of the normal range at this position. We recommend that you investigate the issue at the earliest opportunity. An equipment failure might occur if the issue isn't addressed.  | 
|  ![Wrench icon on a blue square background, representing a tool or settings symbol.](http://docs.aws.amazon.com/Monitron/latest/user-guide/images/acknowledged_icon.png)  | **Acknowledged state**: The warning or alarm state of the position has been acknowledged by a technician, but the asset has not yet been fixed.  | 
| No sensor | **No sensor**: At least one position for the asset doesn't currently have a sensor paired to it. | 

To learn more about a problem, choose the asset and look at the status of underlying sensor positions. 


|  |  | 
| --- |--- |
|  ![Sorter 1 interface showing 1 alarm and 0 acknowledged positions, with Pos.1 in alarm state.](http://docs.aws.amazon.com/Monitron/latest/user-guide/images/unhealthy_asset.png)  |  ![Asset list showing Sorter 1 with two positions: Pos. 1 in Alarm status and Pos. 2 Healthy.](http://docs.aws.amazon.com/Monitron/latest/user-guide/images/webapp_unhealthy-asset.png)  | 

Amazon Monitron uses icons similar to the asset status icons to show the status of sensor positions. 


| Status | Meaning | 
| --- | --- | 
|  ![Green oval button with the text "Healthy" indicating a positive status.](http://docs.aws.amazon.com/Monitron/latest/user-guide/images/healthy.png)  | The position is healthy. All measured values are within the normal range.  | 
|  ![Yellow triangular warning sign with black exclamation mark.](http://docs.aws.amazon.com/Monitron/latest/user-guide/images/warning_icon.png)  |  **Warning state**: A warning has been triggered for one of the positions of this asset, indicating that Amazon Monitron has detected early signs of potential failure. Amazon Monitron identifies warning conditions by analyzing equipment vibration and temperature, using a combination of machine learning and ISO vibration standards. | 
|  ![Red oval button labeled "Alarm" indicating an alert or warning notification.](http://docs.aws.amazon.com/Monitron/latest/user-guide/images/alarm.png)  | An alarm has been triggered for this position, indicating that the machine vibration and temperature is out of the normal range at this position. We recommend that you investigate the issue at the earliest opportunity. An equipment failure might occur if the issue isn't addressed.  | 
|  ![Blue button with white text reading "Acknowledged".](http://docs.aws.amazon.com/Monitron/latest/user-guide/images/acknowledged.png)  | The warning or alarm state of the position has been acknowledged by a technician, but not yet fixed. | 
| No sensor | No sensors are currently paired with the position.  | 

## Notifications
<a name="anom-notifications"></a>

When a warning or an alarm alert is generated, Amazon Monitron sends a notification to the admin user and technician in the app. Authorized personnel can also see notifications by choosing the notification icon in the mobile app when it displays an alert symbol ( ![Red warning icon with exclamation mark inside a white triangle.](http://docs.aws.amazon.com/Monitron/latest/user-guide/images/notification.png) ). 

Choosing the notification icon opens the **Notifications** page, which lists all pending notifications. 


|  |  | 
| --- |--- |
|  ![Notifications list showing alarm and warning entries with position names, vibration and temperature detection details.](http://docs.aws.amazon.com/Monitron/latest/user-guide/images/mobileapp_notification.png)  |  ![Notifications panel showing alarms and warnings for positions with vibration and temperature alerts.](http://docs.aws.amazon.com/Monitron/latest/user-guide/images/webapp_notification.png)  | 