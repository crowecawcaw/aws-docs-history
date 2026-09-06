

Amazon Monitron is no longer open to new customers. Existing customers can continue to use the service as normal. For capabilities similar to Amazon Monitron, see our [blog post](https://aws.amazon.com/blogs/machine-learning/maintain-access-and-consider-alternatives-for-amazon-monitron).

# Commissioning a Wi-Fi gateway
<a name="adding-gateway-Wi-Fi"></a>

When your gateway is mounted in your factory, you will need access to the Amazon Monitron mobile app to commission it. Amazon Monitron supports only smartphones using Android 8.0\+ or iOS 14\+ with Near Field Communication (NFC) and Bluetooth.

**Topics**
+ [To commission a gateway](#commission-gateway-wifi)

## To commission a gateway
<a name="commission-gateway-wifi"></a>

1. If Bluetooth isn't already turned on for your smartphone, turn it on.

1. Position your gateway in the location that works best for communicating with your sensors.

   The best place to mount your gateway is higher than the sensors and no more than 20 to 30 meters away. For additional help with locating your gateway, see [Placing and installing a Wi-Fi gateway](installing-gateway.md). 

1. Plug in the gateway and make sure the LED lights on top are blinking alternatively yellow and blue. 

1. Push the button on the side of the gateway to put it into commissioning mode. The lights will start rapidly blinking.  
![Orange device with smiley face being touched by a finger, connected to a power source.](http://docs.aws.amazon.com/Monitron/latest/user-guide/images/gs-gateway-turnon.png)

1. Open the mobile app on your smartphone.

1. On the **Getting Started** page or the **Gateways** page, choose **Add gateway**. 

   Amazon Monitron scans for the gateway. This can take a few moments. When Amazon Monitron finds the gateway, it displays it in the gateway list. 

1. Choose the gateway. 
**Note**  
If you are using an iOS mobile device, and you have previously paired with this particular gateway, you may need to make your device "forget" the gateway before re-pairing. For more information, see [Troubleshooting Bluetooth pairing](troubleshooting-Bluetooth-pairing-wireless.md).

   It can take a few moments for Amazon Monitron to connect to the new gateway.  
![Mobile phone connecting via Bluetooth to AWS gateway.](http://docs.aws.amazon.com/Monitron/latest/user-guide/images/gs-gateway-bluetooth.png)

   If the mobile app continues to try to connect to the gateway without success, see [Troubleshooting Wi-Fi gateway detection](gateway-failure-Wi-Fi.md).

1. After it connects to the gateway, Amazon Monitron scans for Wi-Fi networks. Choose the Wi-Fi network that you want to use. 

1. Enter your Wi-Fi password, and then choose **Connect**. 

   It can take a few minutes for the gateway to be commissioned and to connect to the Wi-Fi network. 

   If you have further difficulties, see [Resetting the Wi-Fi gateway to factory settings](commissioning-button-Wi-Fi.md).