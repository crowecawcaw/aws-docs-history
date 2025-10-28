# Using AWS Elemental Link for a MediaLive input

You can set up an HD device or a UHD device as the source for a MediaLive input. You can then
attach the input to a MediaLive channel.

## Set up the device

Follow this procedure if the Link device is new to your organization,

1. Set up the device on the internet. For more information, see [Deploying the Link hardware](elink-setup-device.md "elink-setup-device.md").
2. Ask your IAM administrator to give you IAM permissions to work with the
   Link input device interface. See [Setting up users with IAM permissions](device-iam-for-user.md "device-iam-for-user.md").
3. Sign in to the AWS Management Console and open the MediaLive console at [https://console.aws.amazon.com/medialive/](https://console.aws.amazon.com/medialive/ "https://console.aws.amazon.com/medialive/").
4. Find out if your organization obtained your device from an AWS reseller. If so,
   you must [claim it](device-claim.md "device-claim.md").

## Set up the Link input device

Use MediaLive to perform these steps.

1. Open the MediaLive console at [https://console.aws.amazon.com/medialive/](https://console.aws.amazon.com/medialive/ "https://console.aws.amazon.com/medialive/").
2. In the navigation pane, choose **Input devices**. The devices that
   you have access to appear in the **Device list** page. Find the device
   that you want. If you can't find it, follow the troubleshooting tips in [Viewing your Link devices](device-view.md "device-view.md").
3. Get set up in the correct Region. The device and the flow must be in the same
   Region. Follow these steps to get aligned:
   - Decide on the Region where you will work.

   - If you want to work in a different Region, [transfer the device](device-transfer-region.md "device-transfer-region.md") now. Then switch the
     MediaLive console to that Region. From now on, make sure that you work in this
     Region.

4. When the device appears in the **Device list** page, choose the
   link on the individual card to display the **Device details** page.
5. Check the message on the **Attachments** tab to determine how the
   device is currently being used.

**Device is not being used**

A message specifies that the device isn't being used, which means that it isn't
connected to a MediaLive input or a MediaConnect flow.

In this case, the device is ready for you to set it up. See the next
procedure.

**Device is being used for inputs**

A message specifies that the device is already being used as an input source. You
can set up the device as the source for another input, to a maximum of four inputs for a
device. Make a note of the current Region. You will have to use the device in the
existing Region.

In this case, the device is ready for you to set it up. See the next
procedure.

**Device is being used for a flow**

A message specifies that the device is already being used as a source for a MediaConnect
flow.

To use this device for a flow, you must first decommission the current usage. You
should check with other people in your organization to confirm that no one else plans to
use this device is its current usage. Then choose **Detach MediaConnect
flow**.

After the card clears, the device is ready for you to set it up. See the next
procedure.

## Configure the device

Use MediaLive to set up the device.

1. Get set up in the correct Region. The device, the input, and the channel must be in
   the same Region, and you must work in that Region. Follow these steps to get
   aligned:
   - Decide on the Region where you will work. If the device is already being used as
     an input, you must work in the current Region. Otherwise, you can choose the
     Region.

   - If you want to work in a different Region and you can do so, [transfer the device](device-transfer-region.md "device-transfer-region.md") now. Then switch the
     console to that Region. From now on, make sure that you work in this Region.

2. Configure the device. If the device was previously used with a different input or
   flow, review the current configuration and make any necessary changes. For optimum
   performance, the device must be correctly configured.

For more information, see [Configuring a Link device](device-edit.md "device-edit.md"). 3. Create an Elemental Link input in MediaLive. When you create the input, specify the device as
the source. For more information, see [Identifying content in an AWS Elemental Link source](extract-contents-link.md "extract-contents-link.md") and [Setting up an Elemental Link input](input-create-link-device.md "input-create-link-device.md").

As soon as you create the input, the input appears in the [Device details page](device-view.md "device-view.md"), in the
**Attachments** tab. 4. When you are ready to use the Elemental Link input in a channel, attach the input to a
channel, in the same way as you attach any input. For information, see [The procedure to attach inputs](attach-inputs-procedure.md "attach-inputs-procedure.md").

Typically, you attach the input to the channel after the operator at the upstream
system has powered on the AWS Elemental Link hardware device, connected it to the internet, and
started sending a video stream. You wait to attach the input, in order to avoid charges
for an idle input and for a running channel. 5. There are rules for combinations of devices, inputs, and channels. For more
information, see [MediaLive feature rules and limits](eml-limitations-and-rules.md "eml-limitations-and-rules.md").

## Monitor the device

You can use MediaLive to monitor the device.

- You can [view thumbnails](monitoring-link-device-thumbnails.md "monitoring-link-device-thumbnails.md") of
  the content, if the device is streaming.
- You can [look at metrics to monitor](eml-metrics-input-devices.md "eml-metrics-input-devices.md")
  the performance of the device.
