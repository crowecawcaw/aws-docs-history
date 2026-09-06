

Amazon Monitron is no longer open to new customers. Existing customers can continue to use the service as normal. For capabilities similar to Amazon Monitron, see our [blog post](https://aws.amazon.com/blogs/machine-learning/maintain-access-and-consider-alternatives-for-amazon-monitron).

# Commissioning an Ethernet gateway
<a name="adding-gateway-ethernet"></a>

When your gateway is mounted in your factory, you will need access to the Amazon Monitron mobile app to commission it. Amazon Monitron supports only smartphones using Android 8.0\+ or iOS 14\+ with near field communication (NFC) and Bluetooth.

**Topics**
+ [To commission a gateway](#commission-gateway-ethernet)

## To commission a gateway
<a name="commission-gateway-ethernet"></a>

1. If Bluetooth isn't already turned on for your smartphone, turn it on.

1. Position your gateway in the location that works best for communicating with your sensors.

   The best place to mount your gateway is higher than the sensors and no more than 20 to 30 meters away. For additional help with locating your gateway, see [Placing and installing an Ethernet gateway](installing-gateway-ethernet.md).

1. Plug in the gateway and make sure the network light (yellow) and the Bluetooth light (blue) on the front of your gateway are blinking alternately.

1. Push the **Config** button on the gateway to put it into commissioning mode. The Bluetooth and network LED lights will start flashing rapidly.  
![CONFIG button with orange LED indicator light.](http://docs.aws.amazon.com/Monitron/latest/user-guide/images/ethernet-config-button.png)

1. Open the mobile app on your smartphone.

1. On the **Getting started** page or the **Gateways** page, choose **Add gateway**. 

   Amazon Monitron scans for the gateway. This can take a few moments. When Amazon Monitron finds the gateway, it displays it in the gateway list.

1. Choose the gateway. 
**Note**  
If you are using an iOS mobile device, and you have previously paired with this particular gateway, then you may need to make your device "forget" the gateway before re-pairing. For more information, see [Troubleshooting Bluetooth pairing](troubleshooting-Bluetooth-pairing-ethernet.md).

   It can take a few moments for Amazon Monitron to connect to the new gateway.  
![Mobile device connecting via Bluetooth to Amazon Monitron gateway device.](http://docs.aws.amazon.com/Monitron/latest/user-guide/images/phone-bluetooth-ethernet-gateway.png)

   If the mobile app continues to try to connect to the gateway without success, see [Troubleshooting Ethernet gateway detection](troubleshooting-gateway-detection-ethernet.md).
**Note**  
When the gateway is successfully connected, Amazon Monitron displays the gateway device ID and MAC ID in the mobile app.

1. After it connects to the gateway, Amazon Monitron will provide two options for you to configure the network connection for your gateway.  
![Network configuration dialog with Automatic DHCP and Manual options for Monitron Gateway.](http://docs.aws.amazon.com/Monitron/latest/user-guide/images/ethernet-network-configuration.png)

1. Choose your network configuation.

   It can take a few minutes for the gateway to be commissioned and to connect to the network.

   If you have further difficulties making the gateway work, it might be helpful to reset it. For more information, see [Resetting the Ethernet gateway to factory settings](commissioning-button-ethernet.md).

   1. If you choose automatic (DHCP), Amazon Monitron will automatically configure the network to connect to the gateway.

   1. If you choose **manual**, enter your IP address, subnet mask, router, preferred DNS server, and alternate DNS server (optional) information. Then choose **connect**.

![Configure network dialog with fields for IP Address, Subnet mask, Router, and DNS servers.](http://docs.aws.amazon.com/Monitron/latest/user-guide/images/ethernet-IP-DNS-settings.png)
