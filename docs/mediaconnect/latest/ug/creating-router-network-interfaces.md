

# Creating a router network interface in MediaConnect
<a name="creating-router-network-interfaces"></a>

Router network interfaces determine how your router communicates with other network resources and the internet. You can configure these interfaces to connect either through the public internet or through your Amazon Virtual Private Cloud (VPC), depending on your networking requirements. The interface type you choose affects the security settings and accessibility of your router connections.

You can create up to five router network interfaces in each AWS Region. Keep in mind that network interfaces are Regional resources, and you can only use them with router I/Os that are in the same Region.

## Prerequisites
<a name="create-router-network-interfaces-prerequisites"></a>
+ You have an AWS account.
+ You know the AWS Region where you want to create the router network interface.

For VPC network interfaces:
+ You have [set up MediaConnect as a trusted service ](mediaconnect/latest/ug/security-iam-trusted-entity.html) in IAM. 
+ You have created a VPC subnet and associated security groups in Amazon VPC. The subnet you choose determines the availability zone and network range for your network interface, while the security groups act as a virtual firewall.

  For more information about VPCs, see the [*Amazon VPC User Guide*](https://docs.aws.amazon.com/vpc/latest/userguide/). For information about configuring security groups to work with your VPC interface, see [ Security group considerations](https://docs.aws.amazon.com/mediaconnect/latest/ug/vpc-interface-security-groups.html).

## Procedure
<a name="create-router-network-interfaces-procedure"></a>

Follow these steps to create a router network interface.b<a name="create-primary-network-interface-procedure"></a>

**To create a router network interface**

1. Open the MediaConnect console at [https://console.aws.amazon.com/mediaconnect/](https://console.aws.amazon.com/mediaconnect/).

1. In the navigation pane, choose **Router network interfaces**.

1. Choose **Create router network interface**.

1. Under **Router network interface details**, provide the following information:

   1. **Name** - Enter a name that helps you identify the purpose of this network interface.
**Tip**  
Including details like location or use case (for example, **Studio-A-Public** or **NYC-VPC**) makes it easier to manage multiple network interfaces.

   1. **Region** - Specify where you want to create this router network interface. Create your network interface in a Region where you plan to set up routing - you'll need this interface when creating router inputs and outputs.

   1. **Interface type** - Choose one of the following options:
      + For public internet connectivity:
        + Choose **Public interface**.
        + Decide whether you want to block all inbound connections.
        + In **Allowed CIDR blocks**, specify up to 10 IP address ranges (for example, `203.0.113.0/24`). These blocks determine which IP addresses can connect to your router network interface.
      + For VPC connectivity:
        + Choose **VPC interface**.
        + Select a subnet from your VPC. For best performance, choose a subnet in the same Availability Zone as your other AWS resources.
        + Select up to five security groups to control access. These act as virtual firewalls for your router network interface.

1. Choose **Create router network interface**.

## Next steps
<a name="create-router-network-interfaces-next-steps"></a>

After creating a network interface, you can:
+ [Review your network interfaces](viewing-router-network-interfaces.md) to ensure your network setup is complete
+ [Update your router network interface settings if needed](editing-router-network-interface.md)
+ [Delete unused router network interfaces](deleting-router-network-interface.md)

## Additional resources
<a name="create-router-network-interfaces-additional-resources"></a>

To create network interfaces programmatically, see the following page in the *MediaConnect API Reference*:
+ [CreateRouterNetworkInterface](https://docs.aws.amazon.com/mediaconnect/latest/api/API_CreateRouterNetworkInterface.html)

This includes information about how to use the `CreateRouterNetworkInterface` operation and its parameters in one of the language-specific AWS SDKs. 