

# Add an endpoint group for a custom routing accelerator in Global Accelerator
<a name="about-custom-routing-endpoint-groups.create-endpoint-group"></a>

You work with an endpoint group for your custom routing accelerator on the AWS Global Accelerator console or by using an API operation. You can add or remove VPC subnet endpoints from an endpoint group at any time.

This section explains how to create endpoint groups for your custom routing accelerator on the AWS Global Accelerator console. To learn about using API operations with Global Accelerator, see the [AWS Global Accelerator API Reference](https://docs.aws.amazon.com/global-accelerator/latest/api/Welcome.html).

# To add an endpoint group for a custom routing accelerator


1. Open the Global Accelerator console at [ https://us-west-2.console.aws.amazon.com/globalaccelerator/home\#GlobalAcceleratorHome:](https://us-west-2.console.aws.amazon.com/globalaccelerator/home#GlobalAcceleratorHome:). 

1. On the **Accelerators** page, choose a custom routing accelerator.

1. In the **Listeners** section, for **Listener ID**, choose the ID of the listener that you want to add an endpoint group to.

1. Choose **Add endpoint group**.

1. In the section for a listener, specify a Region for the endpoint group.

1. For **Ports and protocols sets**, enter port ranges and protocols for your Amazon EC2 instances.
   + Enter a **From port** and a **To port** to specify a range of ports.
   + For each port range, specify the protocol or protocols for that range.

   The port range doesn't have to be a subset of your listener port range, but there must be enough total ports in the listener port range to support the total number of ports that you specify for the endpoint groups in your custom routing accelerator.

1. Choose **Save**.

1. Optionally, choose **Add endpoint group** to add additional endpoint groups for this listener. You can also choose another listener and add endpoint groups.

1. Choose **Add endpoint group**.