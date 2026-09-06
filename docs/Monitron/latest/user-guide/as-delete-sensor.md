

Amazon Monitron is no longer open to new customers. Existing customers can continue to use the service as normal. For capabilities similar to Amazon Monitron, see our [blog post](https://aws.amazon.com/blogs/machine-learning/maintain-access-and-consider-alternatives-for-amazon-monitron).

# Deleting a sensor
<a name="as-delete-sensor"></a>

Deleting a sensor prevents Amazon Monitron from collecting more data with it. It doesn't delete the data that it has already collected. 

**Topics**
+ [To delete a sensor in the mobile app](#delete-sensor-mobile)
+ [To delete a sensor in the web app](#delete-sensor-web)

## To delete a sensor in the mobile app
<a name="delete-sensor-mobile"></a>

1. From the **Assets** list, choose the asset that is paired to the sensor that you want to delete. 

1. Choose the sensor. 

1. Under **Sensor**, choose **Actions**.

1. Choose **Delete sensor**. 

1. Choose **Delete**.   
![Dialog box confirming deletion of a sensor paired to "Left bearing 1" with Cancel and Delete options.](http://docs.aws.amazon.com/Monitron/latest/user-guide/images/delete-sensor-warning.png)

   After a sensor has been deleted, the status for that position says **No sensor**.   
![Mobile app interface showing asset details with sensor positions and health statuses.](http://docs.aws.amazon.com/Monitron/latest/user-guide/images/remove_sensor.png)

## To delete a sensor in the web app
<a name="delete-sensor-web"></a>
+ Choose **Delete** from the **Sensor details** tab.  
![Asset management interface showing sensor details for Position name 3 with a warning status.](http://docs.aws.amazon.com/Monitron/latest/user-guide/images/web-delete-sensor-1.png)