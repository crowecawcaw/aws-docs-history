# Using Link with a MediaConnect flow

You can set up a Link UHD as the source for a MediaConnect flow.

###### Topics

- [Set up the device in the network](#device-use-flow-step-hardware "#device-use-flow-step-hardware")
- [Set up the Link input device](#device-use-flow-step-device "#device-use-flow-step-device")
- [Set up the device for the flow](#device-use-flow-step-use "#device-use-flow-step-use")
- [Monitor the device](#device-use-flow-step-monitor "#device-use-flow-step-monitor")

## Set up the device in the network

Follow this procedure if the Link device is new to your organization.

1. Set up the device on the internet. For more information, see [Deploying the Link hardware](elink-setup-device.md "elink-setup-device.md").
2. Ask your IAM administrator to give you IAM permissions to work with the
   Link input device interface. See [Setting up users with IAM permissions](device-iam-for-user.md "device-iam-for-user.md").
3. Ask your IAM administrator to set up MediaLive as a trusted entity. See [Setting up MediaLive as a trusted entity](device-iam-for-medialive.md "device-iam-for-medialive.md").
4. Sign in to the AWS Management Console and open the MediaLive console at [https://console.aws.amazon.com/medialive/](https://console.aws.amazon.com/medialive/ "https://console.aws.amazon.com/medialive/").
5. Find out if your organization obtained your device from an AWS reseller. If so,
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

**Device is being used for a flow**

A message specifies that the device is already being used as a source for another
MediaConnect flow.

You can attach a different flow to this device. You should check with other people
in your organization to confirm that you can change the usage. You don't have to detach
the existing flow, but you might need to [stop the
device](device-start-stop.md "device-start-stop.md") to set it to idle.

As soon as the device is idle, it's ready for you to set it up. See the next
procedure.

**Device is being used for inputs**

A message specifies that the device is already being used as an input source.

To use this device for a flow, you must first decommission the current usage. You
should check with other people in your organization to confirm that no one else plans to
use this device is its current usage. Then make a note of all the inputs that this
device is attached to. You must [delete each input](delete-input.md "delete-input.md").

After you delete the last input, the device is ready for you to set it up. See the
next procedure.

## Set up the device for the flow

Use MediaLive to set up the device.

1. Ask the MediaConnect user in your organization to create a flow. Make sure of the
   following:
   - The flow must be in the Region that you identified.
   - The flow must use the protocol described as Zixi push for a Link device, and
     must be set up for a source that is encrypted with AES 128 with a static key. For
     more information, see the section about creating a flow with a standard source in
     [the AWS Elemental MediaConnect user
     guide](../../../mediaconnect/latest/ug/flows-create-standard-source.md "../../../mediaconnect/latest/ug/flows-create-standard-source.md")

2. Obtain the following information from the MediaConnect user:
   - The ARN for the flow.
   - The name of the source for the flow.
   - The ARN for the secret. This secret contains an encryption key. The device will
     use the encryption key to encrypt the content. MediaConnect must use the same key to
     decrypt the content it receives.

3. Obtain the following information from your IAM user:
   - The ARN for the role for MediaLive to use to access the flow and the secret. For
     more information, see [Setting up MediaLive as a trusted entity](device-iam-for-medialive.md "device-iam-for-medialive.md").

4. Configure the device. If the device was previously used with a different input or
   flow, review the current configuration and make any necessary changes. For optimum
   performance, the device must be correctly configured.

For more information, see [Configuring a Link device](device-edit.md "device-edit.md"). 5. Choose **Attach MediaConnect flow** or **Edit MediaConnect
flow** and specify the new flow. For more information, see [Attaching and detaching a Link device](device-attach.md "device-attach.md").

After the flow has become active, you can start the device. (We don't recommend that you
start the device before the flow is active.) At the top of the **Device
details** tab, choose **Start**. The device starts to stream.

## Monitor the device

You can use MediaLive to monitor the device.

- You can [view thumbnails](monitoring-link-device-thumbnails.md "monitoring-link-device-thumbnails.md") of
  the content, if the device is streaming.
- You can [look at metrics to monitor](eml-metrics-input-devices.md "eml-metrics-input-devices.md")
  the performance of the device.
