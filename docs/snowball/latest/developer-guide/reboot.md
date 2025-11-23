AWS Snowball Edge is no longer available to new customers. New customers should explore [AWS DataSync](https://aws.amazon.com/datasync/ "https://aws.amazon.com/datasync/") for online transfers, [AWS Data Transfer Terminal](https://aws.amazon.com/data-transfer-terminal/ "https://aws.amazon.com/data-transfer-terminal/") for
secure physical transfers, or AWS Partner solutions. For edge computing, explore [AWS Outposts](https://aws.amazon.com/outposts/ "https://aws.amazon.com/outposts/").

# Rebooting the Snowball Edge device

Before you reboot a Snowball Edge device, make sure that all data transfer to the device has stopped.

###### To reboot the device using the power button:

1. When all communication with the device has ended, turn it off by pressing the
   power button located above the LCD screen. It takes about 20 seconds for the device to
   shut down. While the device is shutting down, the LCD screen displays a message indicating the device is shutting down.

![Shutdown message on LCD screen.](images/shutdown-screen.png)

###### Note

If the LCD screen is displaying the shutdown message when the device is not actually being shut down, press the **Restart display** button on the screen to return the screen to normal operation.

![Shutdown message on LCD screen with Restart display button near bottom center.](images/shutdown-screen-restart.png) 2. Press the power button. When the device is ready, the LCD display shows a short video while the device is getting ready to start. After about 10 minutes, the device is ready to be unlocked. 3. Unlock the device. See [Unlocking the Snowball Edge](unlockdevice.md "unlockdevice.md").

###### To reboot the device using the Snowball Edge client:

1. When all communication with the device has ended, use the `reboot-device` command to reboot it. When the device is ready, the LCD display shows a short video while the device is getting ready to start. After about 10 minutes, the device is ready to be unlocked.

```

  snowballEdge reboot-device --profile `profile-name`

```

2. Unlock the device. See [Unlocking the Snowball Edge](unlockdevice.md "unlockdevice.md").
