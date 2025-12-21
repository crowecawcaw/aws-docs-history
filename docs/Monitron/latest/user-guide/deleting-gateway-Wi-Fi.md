Amazon Monitron is no longer open to new customers. Existing customers can
continue to use the service as normal. For capabilities similar to Amazon
Monitron, see our [blog post](https://aws.amazon.com/blogs/machine-learning/maintain-access-and-consider-alternatives-for-amazon-monitron "https://aws.amazon.com/blogs/machine-learning/maintain-access-and-consider-alternatives-for-amazon-monitron").

# Deleting a Wi-Fi gateway

Sensors need a gateway to relay their data to the AWS Cloud.
Deleting a gateway might cause some sensors to lose their connection. Exercise
caution before deleting a gateway.

When you delete a gateway, sensors switch their connection to another gateway that
is within range, if there is one. Data transmission from the sensor continues
uninterrupted. If no gateway is within range, data transmission is interrupted and
the data might be lost.

###### Topics

- [To delete a gateway using the
  mobile app](#delete-gateway-wifi-mobile "#delete-gateway-wifi-mobile")
- [To delete a gateway using the web
  app](#delete-gateway-wifi-web "#delete-gateway-wifi-web")

## To delete a gateway using the

mobile app

1. Navigate to the **Gateways** page.
2. Choose the vertical ellipses icon (
   ![Three vertical dots representing a menu or more options in a user interface.](/images/Monitron/latest/user-guide/images/details.png)
   ) next to the gateway that you want to delete.
3. Choose **Delete gateway**.
4. Choose **Delete** again.

## To delete a gateway using the web

app

1. Navigate to the [Viewing the list of gateways](wi-fi-gateway-list.md "wi-fi-gateway-list.md").
2. Select the gateway from the table.
3. Choose **Delete gateway**.
