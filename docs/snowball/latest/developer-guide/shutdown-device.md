

AWS Snowball Edge is no longer available to new customers. New customers should explore [AWS DataSync](https://aws.amazon.com/datasync/) for online transfers, [AWS Data Transfer Terminal](https://aws.amazon.com/data-transfer-terminal/) for secure physical transfers, or AWS Partner solutions. For edge computing, explore [AWS Outposts](https://aws.amazon.com/outposts/). 

# Shutting down the device with AWS OpsHub
<a name="shutdown-device"></a>

Follow these steps to use AWS OpsHub to shut down your Snow device.

**Important**  
We highly recommend that you suspend all activities on the device before you shut down the device. Shutting down a device stops running instances and interrupts any writing to Amazon S3 buckets on the device.

**To shut down a device**

1. On the AWS OpsHub dashboard, find your device under **Devices**. Then choose the device to open the device details page.

1. Choose the **Device Power** menu, then choose **Shutdown**. A dialog box appears.  
![Device details page showing Device Power menu open with Shutdown chosen.](http://docs.aws.amazon.com/snowball/latest/developer-guide/images/opshub-device-shutdown-console.png)

1. In the dialog box, choose **Shutdown**. Your device starts to shut down.  
![Shutdown device window showing Shutdown button at lower right.](http://docs.aws.amazon.com/snowball/latest/developer-guide/images/opshub-shutdown-window-console.png)

   While the device shuts down, the LCD screen displays a message indicating the device is shutting down.  
![Shutdown message on LCD screen.](http://docs.aws.amazon.com/snowball/latest/developer-guide/images/shutdown-screen.png)