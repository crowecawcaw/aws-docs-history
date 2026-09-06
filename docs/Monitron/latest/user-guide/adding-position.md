

Amazon Monitron is no longer open to new customers. Existing customers can continue to use the service as normal. For capabilities similar to Amazon Monitron, see our [blog post](https://aws.amazon.com/blogs/machine-learning/maintain-access-and-consider-alternatives-for-amazon-monitron).

# Adding a sensor position
<a name="adding-position"></a>

When you pair a sensor to an asset, you record the type of position. The type of position tells Amazon Monitron how to assess the position when it analyzes the data from that sensor.

You can create and update asset positions from both the Amazon Monitron web app and the Amazon Monitron mobile app. Using the apps, you can:
+ Add a new position to an existing asset
+ Add a new position to new asset
+ Pair a new sensor with an existing position
+ Add a new position to an existing asset without assigned position

**Topics**
+ [To add a sensor position on the web app](#adding-position-web)
+ [To add a sensor position on the mobile app](#adding-position-mobile)

## To add a sensor position on the web app
<a name="adding-position-web"></a>

1. Choose the sensor whose position you want to create or edit from the **Assets** list.

1. Select the **Add position** button.  
![Asset management interface showing list of assets and positions with status indicators.](http://docs.aws.amazon.com/Monitron/latest/user-guide/images/web-app-add-position-1.png)

1. In the dialog box that opens, enter your **Position name**, **Position type** and **Machine class**.    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/Monitron/latest/user-guide/adding-position.html)

1. Choose **Save**.

1. Your position is added to the asset.  
![Asset management interface showing positions with various statuses and types.](http://docs.aws.amazon.com/Monitron/latest/user-guide/images/web-app-add-position-4.png)

## To add a sensor position on the mobile app
<a name="adding-position-mobile"></a>

1. Choose the sensor whose position you want to create or edit from the **Assets** list.

1. Select the **Add position** button.  
![Asset management interface showing 6 positions with various status indicators.](http://docs.aws.amazon.com/Monitron/latest/user-guide/images/mobile-app-add-position-1.png)

1. In the dialog box that opens, enter your **Posion name**, **Position type**, and **Machine class**.  
![Dialog box for adding a position with fields for name, type, and machine class.](http://docs.aws.amazon.com/Monitron/latest/user-guide/images/mobile-app-add-position-2.png)

1. Choose **Next**.

1. Re-scan your sensor with your mobile device to save the position.  
![Dialog prompting user to hold phone near sensor to scan for position details.](http://docs.aws.amazon.com/Monitron/latest/user-guide/images/mobile-app-add-position-4.png)

1. Your position is added to the asset.  
![Asset detail page showing positions list with various health statuses and Add position button.](http://docs.aws.amazon.com/Monitron/latest/user-guide/images/mobile-app-add-position-6.png)