#

Add a VPC subnet endpoint for a custom routing accelerator

You add Amazon Virtual Private Cloud (VPC) subnet endpoints to endpoint groups in your custom routing accelerators so
that you can direct user traffic to destination Amazon EC2 instances in the subnet.

When you add and remove EC2 instances from the subnet, or enable or disable traffic to EC2 destinations,
you change whether those destinations can receive traffic. However the Global Accelerator port mapping doesn't change.

To allow traffic to some destinations in the subnet, but not all, enter IP addresses for each EC2 instance
that you want to allow, along with the ports on the instance that you want to receive traffic. The IP addresses
that you specify must be for EC2 instances in the subnet. You can specify a port or range of ports, from the
ports that are mapped for the subnet.

You can remove the VPC subnet from your accelerator by removing it from an endpoint group. Removing a
subnet doesn't affect the subnet itself, but Global Accelerator can no longer direct traffic to the subnet or to the Amazon EC2
instances in it. In addition, Global Accelerator will reclaim the port mapping for the VPC subnet
to potentially use them for new subnets that you add.

The steps in this section explain how to add VPC subnet endpoints on the AWS Global Accelerator console. To learn about
using API operations with AWS Global Accelerator, see the [AWS Global Accelerator API Reference](../api/Welcome.md "../api/Welcome.md").

# To add a VPC subnet endpoint

1. Open the Global Accelerator console at [https://console.aws.amazon.com/globalaccelerator/home](https://console.aws.amazon.com/globalaccelerator/home "https://console.aws.amazon.com/globalaccelerator/home").
2. On the **Accelerators** page, choose a custom routing accelerator.
3. In the **Listeners** section, for **Listener ID**,
   choose the ID of a listener.
4. In the **Endpoint groups** section, for **Endpoint group ID**, choose the
   ID of the endpoint group (AWS Region) that you want to add the VPC subnet endpoint to.
5. In the **Endpoints** section, choose **Add endpoint**.
6. On the **Add endpoints** page, for **Endpoint**, choose a VPC subnet.

If you don't have any VPCs, there aren't any items in the list. To continue, add
at least one VPC, then come back to the steps here, and choose a VPC from the list. 7. For VPC subnet endpoint that you add, you can choose to allow or deny traffic to all destinations
in the subnet, or you can allow traffic to only specific EC2 instances and ports. The default is
to deny traffic to all destinations in the subnet. 8. Choose **Add endpoint**.
