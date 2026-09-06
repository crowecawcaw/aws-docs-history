

Amazon Monitron is no longer open to new customers. Existing customers can continue to use the service as normal. For capabilities similar to Amazon Monitron, see our [blog post](https://aws.amazon.com/blogs/machine-learning/maintain-access-and-consider-alternatives-for-amazon-monitron).

# Deleting an asset
<a name="as-delete-assets"></a>

Deleting an asset removes all associated sensors and their positions, in addition to any historical data associated with them. 

**Topics**
+ [To delete an asset](#asset-delete)

## To delete an asset
<a name="asset-delete"></a>

1. From the app's main menu, choose **Assets**.

1. Choose the asset that you want to delete. 

1. For **Asset details**, choose **Actions**. 

1. Choose **Delete asset**.   
![Delete option highlighted in a dropdown menu on a mobile interface.](http://docs.aws.amazon.com/Monitron/latest/user-guide/images/delete-asset.png)

1. Choose one of the following options.
   + If there are no sensors paired with the asset, choose **Delete** and go to the next step.  
![Delete Asset 6 confirmation dialog with warning about deleting positions and measurements.](http://docs.aws.amazon.com/Monitron/latest/user-guide/images/delete-asset-warning.png)
   + If there are sensors paired with the asset, delete them.

     Choose **Delete sensors and positions**. When you delete a sensor or position, all historical measurements taken at this position will also be deleted.  
![Dialog box confirming deletion of Asset name 5 with Delete sensors and positions button.](http://docs.aws.amazon.com/Monitron/latest/user-guide/images/delete-asset-sensors.png)

     It can take some time for Amazon Monitron to delete all the paired sensors and positions.

1. Choose **Delete**.  
![Delete Asset 5 dialog box with warning message and Delete button highlighted.](http://docs.aws.amazon.com/Monitron/latest/user-guide/images/delete-asset-sensors2.png)