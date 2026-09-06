

# Receiving the Snow Family device
<a name="receive-device-sw"></a>

**Important**  
Snow Family devices are the property of AWS. Tampering with a Snow device is a violation of the AWS Acceptable Use Policy.

**Topics**
+ [Verify your hardware](#verify-hardware)
+ [Setting up a Snowball Edge](#receive.swsbe)
+ [Connecting to your local network](#getting-started-connect)

## Verify your hardware
<a name="verify-hardware"></a>

Verify the hardware you've received against the information in the following table. Contact Support if there is a discrepancy.


**Snowball Edge hardware**  

| Item | Quantity | 
| --- | --- | 
| Snowball Edge | 1 | 
| Power cable | 1 | 

## Setting up a Snowball Edge
<a name="receive.swsbe"></a>

When you receive the Snowball Edge, you might notice that it doesn't come in a box. The device is its own physically rugged shipping container. When the device first arrives, inspect it for damage or obvious tampering. If you notice anything that looks suspicious about the device, don't connect it to your internal network. Instead, contact AWS Support and inform them of the issue so that a new device can be shipped to you.

**Important**  
The Snowball Edge is the property of AWS. Tampering with an Snowball Edge is a violation of the AWS Acceptable Use Policy.

The device looks like the following image.

![Snowball Edge device showing front panel and top of device with E ink screen.](http://docs.aws.amazon.com/snow/latest/swsbe-pack/images/SnowballEdgeAppliance.png)


## Connecting to your local network
<a name="getting-started-connect"></a>

### Connect your Snowball Edge to your local network
<a name="connect-swsbe"></a>

Using the following procedure, you connect the Snowball Edge to your local network. The device doesn't need to be connected to the internet. The device has three doors: a front, a back, and a top.

**To connect the device to your network**

1. Open the front and back doors, sliding them inside the device door slots. Doing this gives you access to the touch screen on the LCD display embedded in the front of the device, and the power and network ports in the back.

1. Open the top door and remove the provided power cable from the cable nook, and plug the device into power.

1. Choose one of your RJ45, SFP\+, or QSFP\+ network cables, and plug the device into your network. The network ports are on the back of the device.

1. Power on the Snowball Edge by pressing the power button above the LCD display.

1. When the device is ready, the LCD display shows a short video while the device is getting ready to start. After about 10 minutes, the device is ready to be unlocked.

1. (Optional) Change the default network settings through the LCD display by choosing **CONNECTION**. 

   You can change your IP address to a different static address, which you provide by using the following procedure.

**To change the IP address of an Snowball Edge**

1. On the LCD display, choose **CONNECTION**. 

   A screen appears that shows you the current network settings for the Snowball Edge. The IP address below the drop-down box is automatically updated to reflect the DHCP address that the Snowball Edge requested. 

1. (Optional) Change the IP address to a static IP address. You can also keep it as is.

The device is now connected to your network.

**Important**  
To prevent corrupting your data, don't disconnect the Snowball Edge or change its connection settings while it's in use.