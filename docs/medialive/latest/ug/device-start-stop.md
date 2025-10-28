# Starting and stopping a Link device

You must start or stop a Link only if it is configured as the source for a MediaConnect
flow. (You don't need to start or stop the device when it is configured as the source for a
MediaLive input. In this case, MediaLive automatically starts and stops the device when you start
and stop the related channel.)

You must start a device to instruct it to start streaming video content to send to
MediaConnect. After you start a device, it will always try to stream content. It will only stop
trying when you explicitly stop it. This means, for example, that if you reboot a device,
streaming will automatically resume after the reboot.

You must stop a device before you can perform the following actions:

- [Update some settings](device-edit.md "device-edit.md")
- [Attach](device-attach.md "device-attach.md") the flow to a different device or detach
  the flow from the device.

###### To start or stop a device

1. Open the MediaLive console at [https://console.aws.amazon.com/medialive/](https://console.aws.amazon.com/medialive/ "https://console.aws.amazon.com/medialive/").
2. In the navigation pane, choose **Input devices**. Find the card for
   the appropriate Link , and choose the hyperlink.
3. On the **Device details** page for the device, choose
   **Start** or **Stop**.
