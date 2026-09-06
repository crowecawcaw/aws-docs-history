

# Create a custom routing accelerator in Global Accelerator
<a name="about-custom-routing-accelerators.creating-editing"></a>

This section provides steps for how to create a custom accelerator on the console. To work with Global Accelerator programmatically, see the [AWS Global Accelerator API Reference](https://docs.aws.amazon.com/global-accelerator/latest/api/Welcome.html).

# To create a custom routing accelerator


1. Open the Global Accelerator console at [ https://us-west-2.console.aws.amazon.com/globalaccelerator/home\#GlobalAcceleratorHome:](https://us-west-2.console.aws.amazon.com/globalaccelerator/home#GlobalAcceleratorHome:). 

1. Choose **Create accelerator**.

1. Provide a name for your accelerator.

1. For **Accelerator type**, select **Custom routing**.

1. Optionally, if you have brought your own IP address range to AWS (BYOIP), you can specify static IP addresses for your accelerator from that address pool. Make this choice for each of the two static IP addresses for your accelerator.
   + For each static IP address, choose the IP address pool to use.
   + If you chose your own IP address pool, also choose a specific IP address from the pool. If you chose the default Amazon IP address pool, Global Accelerator assigns a specific IP address to your accelerator.

1. Optionally, add one or more tags to help you identify your accelerator resources.

1. Choose **Next** to go to the next pages in the wizard to add listeners, endpoint groups, and VPC subnet endpoints.