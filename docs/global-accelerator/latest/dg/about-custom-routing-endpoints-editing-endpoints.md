#

Edit a VPC subnet endpoint for a custom routing accelerator

You can edit Amazon Virtual Private Cloud (VPC) subnet endpoints for your custom routing accelerators so
that you can change where you direct user traffic to destination Amazon EC2 instances, or allow or deny traffic
to all destinations in the subnet.

When you add and remove EC2 instances from the subnet, or enable or disable traffic to EC2 destinations,
you change whether those destinations can receive traffic. However the Global Accelerator port mapping doesn't change.

The steps in this section explain how to edit VPC subnet endpoints on the AWS Global Accelerator console. To learn about
using API operations with AWS Global Accelerator, see the [AWS Global Accelerator API Reference](../api/Welcome.md "../api/Welcome.md").

# To allow or deny traffic to specific destinations

You can edit the subnet port mapping for a VPC endpoint to allow or deny traffic to specific EC2 instances
and ports (destination sockets) in a subnet.

1. Open the Global Accelerator console at [https://console.aws.amazon.com/globalaccelerator/home](https://console.aws.amazon.com/globalaccelerator/home "https://console.aws.amazon.com/globalaccelerator/home").
2. On the **Accelerators** page, choose a custom routing accelerator.
3. In the **Listeners** section, for **Listener ID**,
   choose the ID of a listener.
4. In the **Endpoint groups** section, for **Endpoint group ID**, choose the
   ID of the endpoint group (AWS Region) of the VPC subnet endpoint that you want to edit.
5. Choose an endpoint subnet, and then choose **View details**.
6. On the **Endpoint** page, under **Port mappings**, choose an
   IP address, and then choose **Edit**.
7. Enter the ports that you want to enable traffic for, and then choose
   **Allow these destinations**.

# To allow or deny ALL traffic to a subnet

You can update an endpoint to allow or deny traffic to all destinations in the VPC subnet.

1. Open the Global Accelerator console at [https://console.aws.amazon.com/globalaccelerator/home](https://console.aws.amazon.com/globalaccelerator/home "https://console.aws.amazon.com/globalaccelerator/home").
2. On the **Accelerators** page, choose a custom routing accelerator.
3. In the **Listeners** section, for **Listener ID**,
   choose the ID of a listener.
4. In the **Endpoint groups** section, for **Endpoint group ID**, choose the
   ID of the endpoint group (AWS Region) of the VPC subnet endpoint that you want to update.
5. Choose **Allow/Deny all traffic**.
6. Choose an option, to allow all traffic or deny all traffic, and then choose
   **Save**.
