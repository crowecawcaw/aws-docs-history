#

Add a cross-account BYOIP address in Global Accelerator

Follow the steps in this section to configure cross-account bring your own IP (BYOIP) ID addresses using
the Global Accelerator console.

This section explains how to use a BYOIP IP address by using
the AWS Global Accelerator console. To learn about using API operations with Global Accelerator, see the [AWS Global Accelerator API Reference](../api/Welcome.md "../api/Welcome.md").

You can change the BYOIP addresses that you use for your accelerator, but some restrictions apply. For more
information, see [How to update an accelerator to change an IP address](using-byoip.md#using-byoip.update-accelerator.how-to "using-byoip.md#using-byoip.update-accelerator.how-to").

# To use a cross-account BYOIP

IP address

1. Open the Global Accelerator console at [https://console.aws.amazon.com/globalaccelerator/home](https://console.aws.amazon.com/globalaccelerator/home "https://console.aws.amazon.com/globalaccelerator/home").
2. Choose **Create accelerator**.
3. Provide a name for your accelerator.
4. Select an **Accelerator type**.
5. For **IP address type**, select **IPv4**.
6. Select the **Use a static IP address from a CIDR authorized for cross-account** check box.
7. Select the account ID for the owner of the cross-account attachment that specifies you as a principal and that
   includes the BYOIP address block that has been shared with you.

Note that because you must choose one account to select addresses from, if you select two BYOIP IP addresses
when you create an accelerator, the IP addresses must have the same owner and be authorized in the same cross-
account attachment. 8. Specify one or both static IP addresses for your accelerator.

    * For each static IP address, choose the IP address pool to use.


    ###### Note

    You must choose a different IP address pool for each static IP address. This restriction is because Global Accelerator
     assigns each address range to a different network zone, for high availability.
    * If you chose your own IP address pool, also choose a specific IP address from the pool. If you
     choose the default Amazon IP address pool, Global Accelerator assigns a specific IP address to your accelerator.

9. Optionally, add one or more tags to help you identify your accelerator resources.
10. Choose **Next** to add listeners, endpoint groups, and endpoints.
