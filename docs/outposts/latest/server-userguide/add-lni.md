# Add a local network interface to an EC2 instance in an Outposts

subnet

You can add a local network interface to an Amazon EC2 instance on an Outposts subnet during or
after launch. You do so by adding a secondary network interface to the instance, using the
device index that you specified when you enabled the Outpost subnet for local network
interfaces.

###### Consideration

When you specify the secondary network interface using the console, the network
interface is created using device index 1. If this is not the device index that you
specified when you enabled the Outpost subnet for local network interfaces, you can specify
the correct device index by using the AWS CLI or an AWS SDK instead. For example, use the
following commands from the AWS CLI: [create-network-interface](../../../cli/latest/reference/ec2/create-network-interface.md "../../../cli/latest/reference/ec2/create-network-interface.md")
and [attach-network-interface](../../../cli/latest/reference/ec2/attach-network-interface.md "../../../cli/latest/reference/ec2/attach-network-interface.md").

Use the following procedure to add the local network interface after you launch the
instance. For information about adding it during instance launch, see [Launch an instance on the Outpost](launch-instance.md#launch-instances "launch-instance.md#launch-instances").

###### To add a local network interface to an EC2 instance

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the navigation pane, choose **Network and Security**,
   **Network Interfaces**.
3. **Create the network interface**
   1. Choose **Create network interface**.
   2. Select the same Outpost subnet as the instance.
   3. Verify that **Private IPv4 address** is set to
      **Auto-assign**.
   4. Select any security group. Security groups do not apply to local network
      interface, so the security group that you select is not relevant.
   5. Choose **Create network interface**.

4. **Attach the network interface to the instance**
   1. Select the check box for the newly created network interface.
   2. Choose **Actions**, **Attach**.
   3. Choose the instance.
   4. Choose **Attach**. The network interface is attached at device
      index 1. If you specified 1 as the device index for the local network interface for
      the Outpost subnet, this network interface is the local network interface for the
      instance.

## View the local network interface

While the instance is in the running state, you can use the Amazon EC2 console to view both
the elastic network interface and the local network interface for the instances in your
Outpost subnet. Select the instance and choose the **Networking**
tab.

The console displays a private IPv4 address for the local network interface from the
subnet CIDR. This address is not the IP address of the local network interface, and it is
not usable. However, this address is allocated from the subnet CIDR, so you must account for
it in your subnet sizing. You must set the IP address for the local network interface within
the guest operating system, either statically or through your DHCP server.

## Configure the operating system

After you enable local network interfaces, Amazon EC2 instances will have two network
interfaces, one of which is a local network interface. Ensure that you configure the
operating system of the Amazon EC2 instances that you launch to support a multi-homed networking
configuration.
