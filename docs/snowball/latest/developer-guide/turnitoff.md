Effective November 7, 2025, AWS Snowball Edge will only be available to existing customers. If you would like to use AWS Snowball Edge,
sign up prior to that date. New customers should explore [AWS DataSync](https://aws.amazon.com/datasync/ "https://aws.amazon.com/datasync/") for online transfers, [AWS Data Transfer Terminal](https://aws.amazon.com/data-transfer-terminal/ "https://aws.amazon.com/data-transfer-terminal/") for
secure physical transfers, or AWS Partner solutions. For edge computing, explore [AWS Outposts](https://aws.amazon.com/outposts/ "https://aws.amazon.com/outposts/").

# Powering off the Snowball Edge

When you've finished transferring data on to the AWS Snowball Edge device, prepare it for its
return trip to AWS. Before you continue, make sure that all data transfer
to the device has stopped. If you were using the NFS interface to transfer data, disable
it before you power off the device. For more information, see [Managing the NFS interface](shared-using-nfs.md "shared-using-nfs.md").

When all communication with the device has ended, turn it off by pressing the power
button located above the LCD screen. It takes about 20 seconds for the device to shut
down. While the device is shutting down, the LCD screen displays a message indicating
the device is shutting down.

![Shutdown message on LCD screen.](images/shutdown-screen.png)

###### Note

If the LCD screen is displaying the shutdown message when the device is not
actually being shut down, press the **Restart display** button on
the screen to return the screen to normal operation.

![Shutdown message on LCD screen with Restart display button near bottom center.](images/shutdown-screen-restart.png)
After the device shuts down, the shipping information appears on the E Ink display. If
return shipping information does not appear on the E Ink display, contact Support.

**Next:**
[Returning the Snowball Edge device](return-device.md "return-device.md")
