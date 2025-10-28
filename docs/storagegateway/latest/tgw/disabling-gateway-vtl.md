# Deactivating Your Tape Gateway

You deactivate a Tape Gateway if the Tape Gateway has failed and you want to recover
the tapes from the failed gateway to another gateway.

To recover the tapes, you must first deactivate the failed gateway. Deactivating a
Tape Gateway locks down the virtual tapes in that gateway. That is, any data that you
might write to these tapes after deactivating the gateway isn't sent to AWS. You can
only deactivate a gateway on the Storage Gateway console if the gateway is no longer
connected to AWS. If the gateway is connected to AWS, you can't deactivate the
Tape Gateway.

You deactivate a Tape Gateway as part of data recovery. For more information about
recovering tapes, see [You Need to Recover a Virtual Tape
from a Malfunctioning Tape Gateway](Main_TapesIssues-vtl.md#creating-recovery-tape-vtl "Main_TapesIssues-vtl.md#creating-recovery-tape-vtl").

###### To deactivate your gateway

1. Open the Storage Gateway console at
   [https://console.aws.amazon.com/storagegateway/home](https://console.aws.amazon.com/storagegateway/ "https://console.aws.amazon.com/storagegateway/").
2. In the navigation pane, choose **Gateways**, and then choose
   the failed gateway.
3. Choose the **Details** tab for the gateway to display the
   deactivate gateway message.
4. Choose **Create recovery tapes**.
5. Choose **Disable gateway**.
