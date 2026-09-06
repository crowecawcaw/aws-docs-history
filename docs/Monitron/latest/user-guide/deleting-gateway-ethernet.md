

Amazon Monitron is no longer open to new customers. Existing customers can continue to use the service as normal. For capabilities similar to Amazon Monitron, see our [blog post](https://aws.amazon.com/blogs/machine-learning/maintain-access-and-consider-alternatives-for-amazon-monitron).

# Deleting an Ethernet gateway
<a name="deleting-gateway-ethernet"></a>

Sensors need a gateway to relay their data to the AWS Cloud. Deleting a gateway might cause some sensors to lose their connection. Exercise caution before deleting a gateway. 

When you delete a gateway, sensors switch their connection to another gateway that is within range, if there is one, and data transmission from the sensor continues uninterrupted. If no gateway is within range, data transmission is interrupted and the data might be lost.

When you delete a gateway which is currently offline, you must perform a factory reset of the device before commissioning it again.

**Topics**
+ [Deleting an Ethernet gateway using the mobile app](#deleting-gateway-ethernet-mobile)
+ [Deleting an Ethernet gateway using the web app](#deleting-gateway-ethernet-web)

## Deleting an Ethernet gateway using the mobile app
<a name="deleting-gateway-ethernet-mobile"></a>

1. Using the mobile app, navigate to the **Gateways** page. 

1. Choose the vertical ellipses icon ( ![Three vertical dots representing a menu or more options in a user interface.](http://docs.aws.amazon.com/Monitron/latest/user-guide/images/details.png)) next to the gateway that you want to delete. 

1. Choose **Delete Gateway**. 

1. Choose **Delete** again. 

## Deleting an Ethernet gateway using the web app
<a name="deleting-gateway-ethernet-web"></a>

1.  Navigate to the [list of Wi-Fi gateways.](ethernet-gateway-list.md)

1. Select the gateway from the table.

1. Choose **Delete gateway**.