# Attaching and detaching a Link device

If you are using a Link device as the source for a MediaConnect flow, you must attach
the flow to the device. You can also detach the flow to stop using the device as the source
for that flow.

###### To attach a device to a flow

1. Obtain the information about the flow from the person who created the flow.
2. Open the MediaLive console at [https://console.aws.amazon.com/medialive/](https://console.aws.amazon.com/medialive/ "https://console.aws.amazon.com/medialive/").
3. In the navigation pane, choose **Input devices**. Find the card for
   the appropriate Link , and choose the hyperlink.
4. Choose **Attach MediaConnect flow**. Complete the fields:
   - Flow ARN: The ARN of the flow that you obtained from the MediaConnect user. Either
     choose **List of ARNs** and select the ARN, or choose
     **Manual input** and type the ARN.

   - Source name: Type the name that you obtained from the MediaConnect user. Keep in mind
     that the flow might an have more than one source, so make sure that you obtain the
     correct name.
   - Secret ARN: The ARN of the secret that holds the encryption key to use with this
     flow. You obtained this value from the MediaConnect user.
   - Role ARN: The ARN of the role that MediaLive must assume. Obtain this value from
     your IAM administrator.

5. Choose **Save**.

The device is attached to the specified flow. When you later start the device, MediaLive
uses the role ARN to obtain the encryption key that is stored in the secret. MediaLive
delivers the key to the device, and the device encrypts the content that it streams. The
MediaConnect flow uses the same key to decrypt the content as it receives it.

###### To detach a flow from device

1. Open the MediaLive console at [https://console.aws.amazon.com/medialive/](https://console.aws.amazon.com/medialive/ "https://console.aws.amazon.com/medialive/").
2. In the navigation pane, choose **Input devices**. Find the card for
   the appropriate Link , and choose the hyperlink.

If the **Device details** page displays information about a MediaConnect
flow, then you know that the device is currently attached to a flow. 3. Choose **Remove MediaConnect flow**. Then choose
**Save**.
**To detach a device from an input**

To remove the connection between a device an Elemental Link input, you can do either of these
changes:

- You can [Editing an input](edit-input.md "edit-input.md") so that it is connected to a different
  device.
- You can [delete the input](delete-input.md "delete-input.md"). Note that you can't
  modify an Elemental Link input so that it doesn't have a device connected to it.
