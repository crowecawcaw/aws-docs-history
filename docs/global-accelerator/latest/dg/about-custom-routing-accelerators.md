#

Create a custom routing accelerator in Global Accelerator

This section provides steps for how to create a custom accelerator on the console. To work with Global Accelerator
programmatically, see the [AWS Global Accelerator API Reference](../api/Welcome.md "../api/Welcome.md").

# To create a custom routing accelerator

1. Open the Global Accelerator console at [https://us-west-2.console.aws.amazon.com/globalaccelerator/home#GlobalAcceleratorHome:](https://us-west-2.console.aws.amazon.com/globalaccelerator/home#GlobalAcceleratorHome: "https://us-west-2.console.aws.amazon.com/globalaccelerator/home#GlobalAcceleratorHome:").
2. Choose **Create accelerator**.
3. Provide a name for your accelerator.
4. For **Accelerator type**, select **Custom routing**.
5. Optionally, if you have brought your own IP address range to AWS (BYOIP), you can specify static IP addresses
   for your accelerator from that address pool. Make this choice for each of the two static IP addresses for your accelerator.
   - For each static IP address, choose the IP address pool to use.
   - If you chose your own IP address pool, also choose a specific IP address from the pool. If you
     chose the default Amazon IP address pool, Global Accelerator assigns a specific IP address to your accelerator.

6. Optionally, add one or more tags to help you identify your accelerator resources.
7. Choose **Next** to go to the next pages in the wizard to add listeners, endpoint groups,
   and VPC subnet endpoints.
