

Amazon Monitron is no longer open to new customers. Existing customers can continue to use the service as normal. For capabilities similar to Amazon Monitron, see our [blog post](https://aws.amazon.com/blogs/machine-learning/maintain-access-and-consider-alternatives-for-amazon-monitron).

# Step 1: Add a Gateway
<a name="gs-adding-gateway"></a>

In Amazon Monitron, sensors collect data from machines and pass it to gateways, which transmit the data to the AWS Cloud and thus to Amazon Monitron for analysis. These gateways are usually mounted on the wall of a factory within 20 to 30 meters from the sensor and connect to the AWS Cloud using the local Wi-Fi network.

Before adding a gateway, make sure that Bluetooth is turned on for your smartphone. You can only add gateways using the mobile app.

**Topics**
+ [To add a Wi-Fi gateway](#gs-adding-wifi-gateway)
+ [To add an Ethernet gateway](#gs-adding-ethernet-gateway)

## To add a Wi-Fi gateway
<a name="gs-adding-wifi-gateway"></a>

1. Choose the menu icon (☰), and then choose **Getting Started**.  
![Menu options including Assets, Gateways, Users, Sites, with Getting started highlighted.](http://docs.aws.amazon.com/Monitron/latest/user-guide/images/getting-started.png)

1. Choose **Add gateway**.   
![Step 1 of getting started shows icons for gateways and instructions to connect them.](http://docs.aws.amazon.com/Monitron/latest/user-guide/images/gs-gateway.png)

1. In your factory, position your gateway in the location that works best for communicating with your sensors.

   The best place to mount your gateway is higher than the sensors and no more than 20 to 30 meters away. For more information about locating gateways, see [Where to Install Your Gateway](https://docs.aws.amazon.com/Monitron/latest/user-guide/installing-gateway.html#where-gateway) in the *Amazon Monitron User Guide*. 

1. Plug the gateway in and make sure that the LED lights on the top alternatively blink yellow and blue.   
![Orange rectangular device with a smiling face and a hand pointing to it.](http://docs.aws.amazon.com/Monitron/latest/user-guide/images/gs-gateway-turnon.png)

1. Push the button on the side of the gateway to put it into commissioning mode. The lights will start blinking rapidly.

1. In the mobile app, choose **Next**. 

1. Choose **Add gateway**. 

   Amazon Monitron searches for the gateway, which can take a few moments. When it finds it, the gateway appears in the gateway list. 

   If it can't find the gateway, see [Setting Up Gateways](https://docs.aws.amazon.com/Monitron/latest/user-guide/gateways.html) in the *Amazon Monitron User Guide* for possible solutions.

1. When you see the new gateway in the list, choose it. 

   It can take a few moments for Amazon Monitron to connect to the new gateway.  
![Smartphone connecting to AWS service via Bluetooth, represented by icons and symbols.](http://docs.aws.amazon.com/Monitron/latest/user-guide/images/gs-gateway-bluetooth.png)

1. After it connects to the gateway, Amazon Monitron scans for Wi-Fi networks. Choose the Wi-Fi network that you want to use. 
**Note**  
When the gateway is successfully connected, Amazon Monitron displays the gateway device ID and MAC ID in the mobile app.

1. Enter your Wi-Fi password, and then choose **Connect**. 

   It can take a few minutes for the gateway to be commissioned. 

## To add an Ethernet gateway
<a name="gs-adding-ethernet-gateway"></a>

1. If Bluetooth isn't already turned on for your smartphone, turn it on.

1. Position your gateway in the location that works best for communicating with your sensors.

   The best place to mount your gateway is higher than the sensors and no more than 20 to 30 meters away.For additional help with locating your gateway, see [Placing and installing an Ethernet gateway](installing-gateway-ethernet.md). 

1. Plug in the gateway and make sure the network light (yellow) and the Bluetooth light (blue) on the front of your gateway are blinking alternatively.

1. Push the **Config** button on the gateway to put it into commissioning mode. the Bluetooth and network LED lights will start flashing rapidly.  
![Button labeled "CONFIG" with a circular icon next to it.](http://docs.aws.amazon.com/Monitron/latest/user-guide/images/ethernet-config-button.png)

1. Open the mobile app on your smartphone.

1. On the **Getting started** page or the **Gateways** page, choose **Add gateway**. 

   Amazon Monitron scans for the gateway. This can take a few moments. when Amazon Monitron finds the gateway, it displays it in the gateway list. 

1. Choose the gateway. 

   It can take a few moments for Amazon Monitron to connect to the new gateway.  
![Smartphone connecting via Bluetooth to an Amazon device with a smile logo.](http://docs.aws.amazon.com/Monitron/latest/user-guide/images/phone-bluetooth-ethernet-gateway.png)

   If the mobile app continues to try to connect to the gateway without success, see [Troubleshooting Ethernet gateway detection](troubleshooting-gateway-detection-ethernet.md).
**Note**  
When the gateway is successfully connected, Amazon Monitron displays the gateway device ID and MAC ID in the mobile app.

1. After it connects to the gateway, Amazon Monitron will provide two options for you to configure the network connection for your gateway.  
![Network configuration options for Monitron Gateway: Automatic (DHCP) or Manual.](http://docs.aws.amazon.com/Monitron/latest/user-guide/images/ethernet-network-configuration.png)

1. Choose your network configuation.

   It can take a few minutes for the gateway to be commissioned and to connect to the network.

   If you have further difficulties making the gateway work, it might be helpful to reset it. For more information, see [Troubleshooting Ethernet gateway detection](troubleshooting-gateway-detection-ethernet.md).

   1. If you choose automatic (DHCP), Amazon Monitron will automatically configure the network to connect the gateway.

   1. If you choose **manual**, enter your IP address, subnet mask, router, preferred DNS server, and alternate DNS server (optional) information. then choose **connect**.

![Network configuration form with fields for IP address, subnet mask, router, and DNS servers.](http://docs.aws.amazon.com/Monitron/latest/user-guide/images/ethernet-IP-DNS-settings.png)
