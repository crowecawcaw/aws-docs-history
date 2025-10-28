# Transferring a Link device to another

Region

You can transfer a device to a different AWS Region. (If instead you want to transfer
the device to a different Availability Zone in the existing Region, see [Configuring a Link device](device-edit.md "device-edit.md").)

1. Open the MediaLive console at [https://console.aws.amazon.com/medialive/](https://console.aws.amazon.com/medialive/ "https://console.aws.amazon.com/medialive/").
2. In the navigation pane, choose **Input devices**. Find the card for
   the Link that you want to transfer, and choose the hyperlink.
3. On the **Device details** page for the device, choose
   **Other device actions** then **Transfer device**.
4. On the **Transfer input device** dialog, choose **Transfer
   to another AWS Region**, and enter the Region. Then choose
   **Transfer**. The transfer occurs immediately. There is no need to
   confirm the transfer.
5. To locate the moved device, switch to the target Region. Choose **Input
   devices** in the left navigation pane. The devices that you have access to
   appear.

You should [review the configuration](device-edit.md "device-edit.md") because any
customizations (such as the Availability Zone) are deleted during the transfer.
