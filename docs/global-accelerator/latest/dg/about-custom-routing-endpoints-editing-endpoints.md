

# Edit a VPC subnet endpoint for a custom routing accelerator
<a name="about-custom-routing-endpoints-editing-endpoints"></a>

You can edit Amazon Virtual Private Cloud (VPC) subnet endpoints for your custom routing accelerators so that you can change where you direct user traffic to destination Amazon EC2 instances, or allow or deny traffic to all destinations in the subnet. 

When you add and remove EC2 instances from the subnet, or enable or disable traffic to EC2 destinations, you change whether those destinations can receive traffic. However the Global Accelerator port mapping doesn't change.

The steps in this section explain how to edit VPC subnet endpoints on the AWS Global Accelerator console. To learn about using API operations with AWS Global Accelerator, see the [AWS Global Accelerator API Reference](https://docs.aws.amazon.com/global-accelerator/latest/api/Welcome.html).

# To allow or deny traffic to specific destinations


You can edit the subnet port mapping for a VPC endpoint to allow or deny traffic to specific EC2 instances and ports (destination sockets) in a subnet. 

1. Open the Global Accelerator console at [ https://console.aws.amazon.com/globalaccelerator/home](https://console.aws.amazon.com/globalaccelerator/home). 

1. On the **Accelerators** page, choose a custom routing accelerator.

1. In the **Listeners** section, for **Listener ID**, choose the ID of a listener.

1. In the **Endpoint groups** section, for **Endpoint group ID**, choose the ID of the endpoint group (AWS Region) of the VPC subnet endpoint that you want to edit.

1. Choose an endpoint subnet, and then choose **View details**.

1. On the **Endpoint** page, under **Port mappings**, choose an IP address, and then choose **Edit**.

1. Enter the ports that you want to enable traffic for, and then choose **Allow these destinations**.

# To allow or deny ALL traffic to a subnet


You can update an endpoint to allow or deny traffic to all destinations in the VPC subnet. 

1. Open the Global Accelerator console at [ https://console.aws.amazon.com/globalaccelerator/home](https://console.aws.amazon.com/globalaccelerator/home). 

1. On the **Accelerators** page, choose a custom routing accelerator.

1. In the **Listeners** section, for **Listener ID**, choose the ID of a listener.

1. In the **Endpoint groups** section, for **Endpoint group ID**, choose the ID of the endpoint group (AWS Region) of the VPC subnet endpoint that you want to update.

1. Choose **Allow/Deny all traffic**. 

1. Choose an option, to allow all traffic or deny all traffic, and then choose **Save**.