

Amazon Monitron is no longer open to new customers. Existing customers can continue to use the service as normal. For capabilities similar to Amazon Monitron, see our [blog post](https://aws.amazon.com/blogs/machine-learning/maintain-access-and-consider-alternatives-for-amazon-monitron).

# Retrieving MAC address details
<a name="mac-address-ethernet-gateway"></a>

To retrieve your Amazon Monitron gateway's Media Access Control (MAC) address, you can scan the QR code on the gateway device with your mobile phone. Amazon Monitron returns both the MAC address and gateway ID when you scan the QR code.

If you are an IT admin, you can use the scanned MAC address to ensure gateway devices are configured with the correct network settings before they are commissioned. If you are a technician commissioning gateways, you can use the scanned MAC address to troubleshoot any networking issues with your IT admin.

**Note**  
Retrieving MAC addresses by scanning QR codes is only supported for the Amazon Monitron mobile app.

The following procedure shows you how to retrieve your gateway device's MAC address.

1. Navigate to the **Gateways** page.

1. Select the scan icon.  
![Scan icon highlighted in the Gateways search bar.](http://docs.aws.amazon.com/Monitron/latest/user-guide/images/scan-1.png)

1. Amazon Monitron will display a message explaining what scanning a QR code will do. Select **Continue**.  
![Explanation of Scan Gateways QR feature with options to scan for details or find MAC address.](http://docs.aws.amazon.com/Monitron/latest/user-guide/images/scan-2.png)

1. On the **Scan QR Code** page, scan the gateway QR code using your mobile phone camera.

   When the scan successfully completes, Amazon Monitron displays the Gateway ID and MAC address on the **Scan QR Code** page in the mobile app.  
![Scan gateway QR page displaying Gateway ID 30aea4f85652 and MAC address 3333-4444-1111-2222.](http://docs.aws.amazon.com/Monitron/latest/user-guide/images/scan-5.png)

   You can also select the copy icon (![Icon representing the copy or duplicate function with two overlapping squares.](http://docs.aws.amazon.com/Monitron/latest/user-guide/images/copy-icon.png)) to copy the MAC address.
**Note**  
If not already enabled, Amazon Monitron may need permissions to access your camera to scan the QR code. These permissions must be enabled from the settings page of your mobile device before you can successfully scan a device QR code. Amazon Monitron will prompt you to enable camera access during the scanning process if permissions haven't already been granted.

   **On Android devices**  
![Pop-up requesting camera access permission for Amazon Monitron app on Android device.](http://docs.aws.amazon.com/Monitron/latest/user-guide/images/scan-3.png)

   **On iOS devices**  
![Permission dialog requesting camera access for Monitron app to scan gateway QR code.](http://docs.aws.amazon.com/Monitron/latest/user-guide/images/scan-4.png)