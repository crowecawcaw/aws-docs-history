

Amazon Monitron is no longer open to new customers. Existing customers can continue to use the service as normal. For capabilities similar to Amazon Monitron, see our [blog post](https://aws.amazon.com/blogs/machine-learning/maintain-access-and-consider-alternatives-for-amazon-monitron).

# Editing machine class
<a name="edit-sensor-position"></a>

You can edit the machine class of a sensor from both the mobile and web apps, from either the **Asset detail** section or the **Position detail** section.

When you edit a sensor's machine class, asset condition alerts based on the updated machine class take effect from the next measurement after the update.

**Important**  
You cannot edit a sensor's machine class if it has an unresolved alert. You must resolve any alerts before editing machine class.

**Topics**
+ [To edit machine class on the mobile app](#edit-sensor-machine-class-mobile)
+ [To edit machine class on the web app](#edit-sensor-machine-class-web)
+ [To edit machine class from the position detail page](#edit-sensor-machine-class-position-detail)

## To edit machine class on the mobile app
<a name="edit-sensor-machine-class-mobile"></a>

1. From the **Assets** list, choose the asset with the sensor position you want to edit.

1. From the **Positions** list, choose the sensor with the position whose machine class you want to change.

1. Choose to see more sensor details.  
![Pump asset page showing four positions with statuses and a Pair sensor button.](http://docs.aws.amazon.com/Monitron/latest/user-guide/images/asset-detail-machine-class-mobile-app-1.png)

1. From the options that appear, choose **Edit machine class**.  
![Menu displaying Edit position name, Edit machine class, Delete position, and Delete sensor options.](http://docs.aws.amazon.com/Monitron/latest/user-guide/images/asset-detail-machine-class-mobile-app-2.png)

1. From **Edit machine class** choose the new machine class you want to assign to the sensor. Select **Save**.
**Note**  
The new machine class will take effect at the next measurement interval. The single-axis chart threshold will be updated.

**To edit a machine class from the position detail page**

1. From the **Position details** list, choose the **Actions** tab.  
![Actions dropdown button highlighted in the Position details section of the interface.](http://docs.aws.amazon.com/Monitron/latest/user-guide/images/position-detail-machine-class-mobile-app-1.png)

1. From the options that appear, choose **Edit machine class**.  
![Modal menu with options including Edit position name, Edit machine class, Delete position, and Delete sensor.](http://docs.aws.amazon.com/Monitron/latest/user-guide/images/position-detail-machine-class-mobile-app-2.png)

1. From the **Edit machine class** menu choose the new machine class you want to assign to the sensor. Choose **Next**.
**Note**  
The new machine class will take effect at the next measurement interval. The single-axis chart threshold will be updated.

## To edit machine class on the web app
<a name="edit-sensor-machine-class-web"></a>

1. From the **Assets** table, choose the **Actions** button.

1. From the options, choose **Edit machine class**.  
![Actions menu expanded showing Edit position name, Edit machine class, and Delete position options.](http://docs.aws.amazon.com/Monitron/latest/user-guide/images/asset-detail-machine-class-web-app.png)

1. From the **Edit machine class** menu choose the new machine class you want to assign to the sensor and then select **Save changes**.
**Note**  
The new machine class will take effect at the next measurement interval and impact position status. The single-axis chart threshold will be updated.

## To edit machine class from the position detail page
<a name="edit-sensor-machine-class-position-detail"></a>

1. From the **Positions** table, choose the **Actions** button.

1. From the options, choose **Edit machine class**.  
![Actions menu expanded showing Edit position name, Delete position, and Edit machine class options.](http://docs.aws.amazon.com/Monitron/latest/user-guide/images/position-detail-machine-class-web-app.png)

1. From the **Edit machine class** menu choose the new machine class you want to assign to the sensor and then select **Save changes**.
**Note**  
The new machine class will take effect at the next measurement interval. The single-axis chart threshold will be updated.