# Rebooting a Link device

You can remotely reboot a Link device from the AWS console. You don't need
physical access to the device.

Typically, you reboot the device only as a last resort, to resolve a problem with the
device response or with the content that is streaming.

You don't have to stop either the device or the channels before rebooting. MediaLive handles
the reboot smoothly.

###### To reboot a device

1. Open the MediaLive console at [https://console.aws.amazon.com/medialive/](https://console.aws.amazon.com/medialive/ "https://console.aws.amazon.com/medialive/").
2. In the navigation pane, choose **Input devices**. Find the card for
   the Link that you want to reboot, and choose the hyperlink.
3. On the **Device details** page for the device, choose
   **Other device actions** then **Reboot
   device**, then confirm the request.

Any MediaLive channels or MediaConnect flows that are using the device will lose input briefly,
but the channels or flows won't stop or fail.

When the reboot is complete, the device connection status changes to **Connected**. If the device was streaming prior to the reboot, it
automatically resumes streaming.
