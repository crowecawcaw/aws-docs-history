# Updating software on a Link device

Link devices automatically install updates when they are powered on, assuming
that the MediaLive channels that use the device have stopped.

However, if you don't stop your channels frequently, you should start a maintenance
window at a convenient time. The device will install software updates some time in the next
two hours.

You don't have to stop either the device or the channels before starting a maintenance
window. MediaLive handles the update smoothly.

###### To start a maintenance window for a device

1. Open the MediaLive console at [https://console.aws.amazon.com/medialive/](https://console.aws.amazon.com/medialive/ "https://console.aws.amazon.com/medialive/").
2. In the navigation pane, choose **Input devices**. Find the card for
   the Link that you want to update, and choose the hyperlink.
3. On the **Device details** page for the device, choose
   **Other device actions** then **Start
   maintenance**, then confirm the request.

The maintenance window starts. The update will start some time during the next two
hours. When the update starts, any channels that are using the device will lose input
briefly, but the channels won't stop or fail.

When the reboot is complete, the device connection status changes to **Connected**. If the device was streaming prior to the reboot, it
automatically resumes streaming output.
