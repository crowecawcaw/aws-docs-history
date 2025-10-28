# Transferring a Link device to another

account

You can transfer a device to a different AWS account, to transfer ownership of the
device to that account. The recipient of a transfer must accept or reject the incoming
transfer in order for the transfer to be finalized. After the transfer is finalized, all
charges for use of the device are applied to the new account.

###### Topics

- [Initiating a device transfer](#device-transfer-send "#device-transfer-send")
- [Cancelling an outgoing device transfer](#device-transfer-cancel "#device-transfer-cancel")
- [Accepting a device transfer](#device-transfer-receive "#device-transfer-receive")

## Initiating a device transfer

###### To transfer a Link to another AWS account

1. Open the MediaLive console at [https://console.aws.amazon.com/medialive/](https://console.aws.amazon.com/medialive/ "https://console.aws.amazon.com/medialive/").
2. In the navigation pane, choose **Input devices**. Find the card
   for the Link that you want to transfer and choose the hyperlink.
3. On the **Device details** page for the device, choose
   **Other device actions** then **Transfer device**.
4. On the **Transfer input device** dialog, choose
   **Transfer to another AWS account**, enter the AWS account to
   transfer to, and type an optional message. Then choose
   **Transfer**.
5. In the navigation pane, choose **Input devices**, then choose
   **Device transfers**. The transfer request appears in the
   **Outgoing transfers** tab.

The transfer is pending until the recipient accepts the device. While the transfer
is pending, you can cancel the request, as described in the following section.

If the recipient accepts the transfer, the device no longer appears in any of your
device lists.

If the recipient rejects the transfer, the device appears again on your
**Input devices** page.

## Cancelling an outgoing device transfer

You can cancel a device transfer while the request is pending.

###### To cancel an outgoing device transfer

1. Open the MediaLive console at [https://console.aws.amazon.com/medialive/](https://console.aws.amazon.com/medialive/ "https://console.aws.amazon.com/medialive/").
2. In the navigation pane, choose **Input Devices**. Choose
   **Device transfers**, then choose the **Outgoing
   transfers** tab.
3. In the list of transfers, choose the transfer you want to cancel, then choose
   **Cancel**.

## Accepting a device transfer

The owner of a device can transfer a device to your AWS account. For example,
someone in your organization might transfer the device from one AWS account in your
organization to another AWS account.

If you are expecting to receive a device transfer, you should regularly check the
**Incoming transfers** tab on the **Device transfers**
page. You must accept the transfer. You can't use the device until you have accepted the
transfer.

###### To accept a device transfer

1. Open the MediaLive console at [https://console.aws.amazon.com/medialive/](https://console.aws.amazon.com/medialive/ "https://console.aws.amazon.com/medialive/").
2. In the navigation pane, choose **Input devices**. Choose
   **Device transfers**, then choose the **Incoming
   transfers** tab.
3. In the list of transfers, choose the device that you want to accept, then choose
   **Accept** or **Reject**.
4. In the navigation pane, choose **Input devices** again. The
   device now appears in the list of devices on the **Input devices**
   page.
