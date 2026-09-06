

Amazon Monitron is no longer open to new customers. Existing customers can continue to use the service as normal. For capabilities similar to Amazon Monitron, see our [blog post](https://aws.amazon.com/blogs/machine-learning/maintain-access-and-consider-alternatives-for-amazon-monitron).

# Amazon Monitron alerts
<a name="how-it-works-alerts"></a>

To track equipment health, the Amazon Monitron mobile app displays an icon for each asset, so you can see its condition at a glance.

The following table shows the status icons you may see for your asset.


| Alert icon | Alert definition | 
| --- | --- | 
|  ![Green circular icon with a white checkmark symbol inside.](http://docs.aws.amazon.com/Monitron/latest/user-guide/images/healthy_icon.png)  | **Healthy:** The machine is working normally. | 
|  ![Red hexagonal warning sign with exclamation mark indicating caution or alert.](http://docs.aws.amazon.com/Monitron/latest/user-guide/images/alarm_icon.png)  | **Alarm**: An alarm has been triggered for one of the positions of this asset, indicating that the machine vibration and temperature are out of the normal range at this position. We recommend that you investigate the issue at the earliest opportunity. An equipment failure might occur if the issue isn't addressed. | 
|  ![Yellow triangular warning sign with black exclamation mark.](http://docs.aws.amazon.com/Monitron/latest/user-guide/images/warning_icon.png)  | **Warning**: A warning has been triggered for one of the positions of this asset, indicating that Amazon Monitron has detected early signs of potential failure. Amazon Monitron identifies warning conditions by analyzing equipment vibration and temperature, using a combination of machine learning and ISO vibration standards. | 
|  ![Wrench icon on a blue square background, representing a tool or settings symbol.](http://docs.aws.amazon.com/Monitron/latest/user-guide/images/acknowledged_icon.png)  | **Maintenance**: Someone has acknowledged the alarm and is looking into the issue. | 
|  ![Checkmark and X icons in a gray circle, representing selection or validation options.](http://docs.aws.amazon.com/Monitron/latest/user-guide/images/sensor-healthy-offline-asset-list.png)  | **Asset Healthy-offline:** Sensor is offline and the last recorded state was **Healthy**. No new alerts will be generated till the sensor returns online. | 
|  ![Healthy status badge with a close or dismiss button.](http://docs.aws.amazon.com/Monitron/latest/user-guide/images/sensor-position-healthy-offline.png)  | **Position Healthy-offline:** Sensor is offline and the last recorded state was **Healthy**. No new alerts will be generated till the position returns online. | 
|  ![Hexagonal warning icon with an exclamation mark and a crossed-out circle.](http://docs.aws.amazon.com/Monitron/latest/user-guide/images/sensor-alarm-offline-asset-list.png)  | **Asset Alarm-offline:** Sensor is offline and the last recorded state was an **Alarm**. No new alerts will be generated till the sensor returns online. | 
|  ![Alarm icon with an X symbol for dismissing or closing the alarm notification.](http://docs.aws.amazon.com/Monitron/latest/user-guide/images/sensor-position-alarm-offline.png)  | **Position Alarm-offline:** Sensor is offline and the last recorded state was an **Alarm**. No new alerts will be generated till the position returns online. | 
|  ![Warning icon with an exclamation mark inside a triangle and an X symbol.](http://docs.aws.amazon.com/Monitron/latest/user-guide/images/sensor-warning-offline-asset-list.png)  | **Asset Warning-offline:** Sensor is offline and the last recorded state was a **Warning**. No new alerts will be generated till the sensor returns online. | 
|  ![Warning message icon with an X button for dismissal.](http://docs.aws.amazon.com/Monitron/latest/user-guide/images/sensor-position-warning-offline.png)  | **Position Warning-offline:** Sensor is offline and the last recorded state was a **Warning**. No new alerts will be generated till the position returns online. | 
|  ![Icon showing a wrench with a close or cancel symbol.](http://docs.aws.amazon.com/Monitron/latest/user-guide/images/sensor-maintenance-offline-asset-list.png)  | **Asset Maintenance-offline:** Sensor is offline and the last recorded state was **Maintenance**. No new alerts will be generated till the sensor returns online. | 
|  ![Gray button labeled "Maintenance" with an X icon for dismissal or closure.](http://docs.aws.amazon.com/Monitron/latest/user-guide/images/sensor-position-maintenance-offline.png)  | **Position Maintenance-offline:** Sensor is offline and the last recorded state was **Maintenance**. No new alerts will be generated till the position returns online. | 