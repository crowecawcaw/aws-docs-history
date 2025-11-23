#

Getting started with a custom routing accelerator

This section provides steps for creating a custom routing accelerator, which routes traffic deterministically
to Amazon EC2 instance destinations in virtual private cloud (VPC) subnet endpoints.

**Tasks**

- [Before you begin](#getting-started-before-you-begin-custom "#getting-started-before-you-begin-custom")
- [Step 1: Create a custom routing accelerator](#getting-started-accelerator-custom "#getting-started-accelerator-custom")
- [Step 2: Add listeners](#getting-started-create-listeners-custom "#getting-started-create-listeners-custom")
- [Step 3: Add endpoint groups](#getting-started-add-endpoint-groups-custom "#getting-started-add-endpoint-groups-custom")
- [Step 4: Add endpoints](#getting-started-add-endpoints-custom "#getting-started-add-endpoints-custom")
- [Step 5 (optional): Delete your accelerator](#getting-started-delete-accelerator-custom "#getting-started-delete-accelerator-custom")

##

Before you begin

Before you create a custom routing accelerator, create a resource that you can add as an endpoint to direct
traffic to. A custom routing accelerator endpoint must be a virtual private cloud (VPC) subnet, which can
include multiple Amazon EC2 instances. For instructions for creating the resources see
the following:

- Create a VPC subnet. For more information, see [Create and Configure Your VPC](../../../directoryservice/latest/admin-guide/gsg_create_vpc.md "../../../directoryservice/latest/admin-guide/gsg_create_vpc.md") in the _Directory Service Administration Guide_.
- Optionally, launch one or more Amazon EC2 instances in your VPC. For more information, see [Create your EC2 resources and launch
  your EC2 instance](../../../efs/latest/ug/gs-step-one-create-ec2-resources.md "../../../efs/latest/ug/gs-step-one-create-ec2-resources.md") in the _Amazon EC2 User Guide_.

When you create a resource to add to Global Accelerator, be aware of the following:

- When you add an EC2 instance endpoint in Global Accelerator, you enable
  internet traffic to flow directly to and from the endpoint in a VPC
  by targeting it in a private subnet. The VPC that contains the EC2 instance
  must have an [internet gateway](../../../vpc/latest/userguide/VPC_Internet_Gateway.md "../../../vpc/latest/userguide/VPC_Internet_Gateway.md")
  attached to it, to indicate that the VPC accepts internet traffic. For more information,
  see [Secure VPC connections in AWS Global Accelerator](secure-vpc-connections.md "secure-vpc-connections.md").

Before you create a custom routing accelerator, make sure that you review the best practices described in
[Guidelines and restrictions for custom routing accelerators](about-custom-routing-guidelines.md "about-custom-routing-guidelines.md").

##

Step 1: Create a custom routing accelerator

## To create an accelerator

1. Open the Global Accelerator console at [https://us-west-2.console.aws.amazon.com/globalaccelerator/home#GlobalAcceleratorHome:](https://us-west-2.console.aws.amazon.com/globalaccelerator/home#GlobalAcceleratorHome: "https://us-west-2.console.aws.amazon.com/globalaccelerator/home#GlobalAcceleratorHome:").
2. Provide a name for your accelerator.
3. For **Accelerator type**, select **Custom routing**.
4. Optionally, add one or more tags to help you identify your accelerator resources.
5. Choose **Next** to add listeners, endpoint groups, and VPC subnet endpoints.

## Step 2: Add listeners

Create a listener to process inbound connections from your users to Global Accelerator.

The range that you specify when you create a listener defines how many listener port and destination IP address
combinations that you can use with your custom routing accelerator. For maximum flexibility, we recommend that you specify a large port range.
Each listener port range that you specify must include a minimum of 16 ports.

## To create a listener

1. On the **Add listener** page, enter the ports or port ranges that you want to associate with the
   listener. Listeners support ports 1-65535.
2. Choose the protocol or protocols for the ports that you entered.
3. Optionally, choose **Add listener** to add an additional listener.
4. When you're finished adding listeners, choose **Next**.

##

Step 3: Add endpoint groups

Add one or more endpoint groups, each of which is associated with a specific AWS Region. For each endpoint
group, specify one or more sets of port ranges and protocols. Global Accelerator uses these to direct traffic to Amazon EC2 instances
in subnets in the Region.

For each port range that you provide, you also specify the protocol to use: UDP, TCP, or both UDP and TCP.

## To add an endpoint group

1.  On the **Add endpoint groups** page, in the section for a listener,
    choose a **Region**.
2.  For **Ports and protocols sets**, enter port ranges and protocols for
    your Amazon EC2 instances.

        * Enter a **From port** and a **To port**
         to specify a range of ports.
        * For each port range, specify the protocol or protocols for that range.

    The port range doesn't have to be a subset of your listener port range, but there must be enough
    total ports in the listener port range to support the total number of ports that you specify.

3.  Choose **Save**.
4.  Optionally, choose **Add endpoint group** to add additional endpoint
    groups for this listener or other listeners.
5.  Choose **Next**.

##

Step 4: Add VPC subnet endpoints

Add one or more virtual private cloud (VPC) subnet endpoints for this regional endpoint group. Endpoints for custom routing accelerators
define the VPC subnets that can receive traffic through a custom routing accelerator. Each subnet can contain one or many Amazon EC2
instance destinations.

When you add a VPC subnet endpoint, Global Accelerator generates new port mappings that you can use to
route traffic to the destination EC2 instance IP addresses in the subnet. Then you can use the Global Accelerator API to get a
static list of all the port mappings for the subnet, and use the mapping to deterministically direct traffic
to specific EC2 instances.

## To add endpoints

1.  On the **Add endpoints** page, in the section for the endpoint group that
    you want to add the endpoint to, choose a subnet ID for **Endpoint**.
2.  Optionally, do one of the following to enable traffic to EC2 instance destinations in the subnet:

        * To allow traffic to be directed to all EC2 endpoints and ports on the subnet,
         select **Allow all traffic**
        * To allow traffic to specific EC2 endpoints and ports on the subnet,
         select **Allow traffic to specific destination socket addresses**.
         Then specify the IP addresses and ports or port ranges to allow. Finally, choose
         **Allow these destinations**.

    By default, no traffic is allowed to subnet endpoints. If you don't
    select an option to allow traffic, traffic is denied to all destinations in the subnet.

###### Note

If you want to enable traffic to specific EC2 instances and ports in the subnet, you can
do that programmatically. For more information, see [AllowCustomRoutingTraffic](../api/API_AllowCustomRoutingTraffic.md "../api/API_AllowCustomRoutingTraffic.md") in the
_AWS Global Accelerator API Reference_. 3. Choose **Next**.

After you choose **Next**, on the Global Accelerator, dashboard you'll see a message
that your accelerator is in progress. When the process is finished, the accelerator status
in the dashboard is **Active**.

##

Step 5 (optional): Delete your accelerator

If you created an accelerator as a test or if you're no longer using an accelerator, you can
delete it. On the console, disable the accelerator, and then you can delete it. You don't
have to remove listeners and endpoint groups from the accelerator.

To delete an accelerator by using an API operation instead of the console, you must first
remove all listeners and endpoint groups that are associated with the accelerator as well
as disable it. For more information, see the [DeleteCustomRoutingAccelerator](../api/API_DeleteCustomRoutingAccelerator.md "../api/API_DeleteCustomRoutingAccelerator.md")
operation in the _AWS Global Accelerator API Reference_.

Be aware of the following when you delete an accelerator:

- When you create an accelerator, Global Accelerator provides you with a set of two static IP addresses. The IP
  addresses are assigned to your accelerator for as long as it exists, even if
  you disable the accelerator and it no longer accepts or routes traffic.
  However, when you _delete_ an accelerator, you lose the
  static IP addresses that are assigned to the accelerator, so you can no longer
  route traffic by using them. As a best practice, ensure that you have
  permissions in place to avoid inadvertently deleting accelerators. You can use
  IAM policies like tag-based permissions with Global Accelerator to limit the users who
  have permissions to delete an accelerator. For more information, see [ABAC with Global Accelerator](security_iam_service-with-iam.md#security_iam_service-with-iam-tags "security_iam_service-with-iam.md#security_iam_service-with-iam-tags").

## To delete an accelerator

1. Open the Global Accelerator console at [https://console.aws.amazon.com/globalaccelerator/home](https://console.aws.amazon.com/globalaccelerator/home "https://console.aws.amazon.com/globalaccelerator/home").
2. Choose the accelerator that you want to delete.
3. Choose **Edit**.
4. Choose **Disable accelerator**, and then choose
   **Save**.
5. Choose the accelerator that you want to delete.
6. Choose **Delete accelerator**.
7. In the confirmation dialog box, choose **Delete**.
