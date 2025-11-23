# Network interface attachments for your EC2 instance

You can create network interfaces to be used by your EC2 instances as primary or secondary
network interfaces. You must attach a network interface to an EC2 instance if it is in
the same Availability Zone as the network interface. The instance type of an instance
determines how many network interfaces you can attach to the instance. For more
information, see [Maximum IP addresses per network interface](AvailableIpPerENI.md "AvailableIpPerENI.md").

###### Considerations

- You can attach a network interface to an instance when it's running (hot attach), when
  it's stopped (warm attach), or when the instance is being launched (cold
  attach).
- You can detach secondary network interfaces when the instance is running or stopped.
  However, you can't detach the primary network interface.
- You can detach a secondary network interface from one instance and attach it to another
  instance.
- When launching an instance using the CLI, API, or an SDK, you can specify the
  primary network interface and additional network interfaces. Note that you can't
  enable the auto-assignment of public IPv4 addresses if you add a secondary
  network interface during launch.
- Launching an Amazon Linux or Windows Server instance with multiple network interfaces
  automatically configures interfaces, private IPv4 addresses, and route tables on
  the operating system of the instance.
- A warm or hot attach of an additional network interface might require you to manually
  bring up the second interface, configure the private IPv4 address, and modify the
  route table accordingly. Instances running Amazon Linux or Windows Server automatically
  recognize the warm or hot attach and configure themselves.
- You can't attach another network interface to an instance (for example, a
  NIC teaming configuration) to increase or double the network bandwidth to or
  from the dual-homed instance.
- If you attach multiple network interfaces from the same subnet to an instance, you might
  encounter networking issues such as asymmetric routing. If possible, add a
  secondary private IPv4 address on the primary network interface instead.
- For EC2 instances in an IPv6-only subnet, if you attach a secondary network interface,
  the private DNS hostname of the secondary network interface resolves to the primary
  IPv6 address for the primary network interface.
- [Windows instances] – If you add multiple network interfaces to an instance, you
  must configure the network interfaces to use static routing.

## Attach a network interface

You can attach a network interface to any instance in the same Availability Zone
as the network interface, using either the **Instances** or
**Network Interfaces** page of the Amazon EC2 console. Alternatively,
you can specify existing network interfaces when you [launch instances](ec2-launch-instance-wizard.md "ec2-launch-instance-wizard.md").

If the public IPv4 address on your instance is released, it does not receive a new
one if there is more than one network interface attached to the instance. For more
information about the behavior of public IPv4 addresses, see [Public IPv4 addresses](using-instance-addressing.md#concepts-public-addresses "using-instance-addressing.md#concepts-public-addresses").

Console

###### To attach a network interface using the Instances page

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the navigation pane, choose **Instances**.
3. Select the checkbox for the instance.
4. Choose **Actions**, **Networking**,
   **Attach network interface**.
5. Choose a VPC. The network interface can reside in the same VPC as your instance or in
   a different VPC that you own, as long as the network interface
   is in the same Availability Zone as the instance. This enables
   you to create multi-homed instances across VPCs with different
   networking and security configurations.
6. Select a network interface. If the instance supports multiple network cards,
   you can choose a network card.
7. Choose **Attach**.

###### To attach a network interface using the Network Interfaces page

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the navigation pane, choose **Network Interfaces**.
3. Select the checkbox for the network interface.
4. Choose **Actions**, **Attach**.
5. Choose an instance. If the instance supports multiple network cards, you
   can choose a network card.
6. Choose **Attach**.

AWS CLI

###### To attach a network interface

Use the following [attach-network-interface](../../../cli/latest/reference/ec2/attach-network-interface.md "../../../cli/latest/reference/ec2/attach-network-interface.md")
command.

```
aws ec2 attach-network-interface \
    --network-interface-id `eni-1234567890abcdef0` \
    --instance-id `i-1234567890abcdef0` \
    --device-index `1`
```

PowerShell

###### To attach a network interface

Use the [Add-EC2NetworkInterface](../../../powershell/latest/reference/items/Add-EC2NetworkInterface.md "../../../powershell/latest/reference/items/Add-EC2NetworkInterface.md")
cmdlet.

```
Add-EC2NetworkInterface `
    -NetworkInterfaceId `eni-1234567890abcdef0` `
    -InstanceId `i-1234567890abcdef0` `
    -DeviceIndex `1`
```

## Detach a network interface

You can detach a secondary network interface that is attached to an EC2 instance at any time,
using either the **Instances** or **Network Interfaces**
page of the Amazon EC2 console.

If you try to detach a network interface that is attached to a resource from another service,
such as an ELB load balancer, a Lambda function, a WorkSpace, or a NAT gateway, you get an
error that you do not have permission to access the resource. To find which service created
the resource attached to a network interface, check the description of the network interface.
If you delete the resource, then its network interface is deleted.

Console

###### To detach a network interface using the Instances page

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the navigation pane, choose **Instances**.
3. Select the checkbox for the instance. Check the **Network interfaces**
   section of the **Networking** tab to verify that the network interface
   is attached to an instance as a secondary network interface.
4. Choose **Actions**, **Networking**,
   **Detach network interface**.
5. Select the network interface and choose **Detach**.

###### To detach a network interface using the Network Interfaces page

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the navigation pane, choose **Network Interfaces**.
3. Select the checkbox for the network interface. Check the **Instance details**
   section of the **Details** tab to verify that the network interface is
   attached to an instance as a secondary network interface.
4. Choose **Actions**, **Detach**.
5. When prompted for confirmation, choose **Detach**.
6. If the network interface fails to detach from the instance, choose **Force
   detachment**, **Enable** and then try again. We recommend that
   force detachment only as a last resort. Forcing a detachment can prevent you from
   attaching a different network interface on the same index until you restart the instance.
   It can also prevent the instance metadata from reflecting that the network interface was
   detached until you restart the instance.

AWS CLI

###### To detach a network interface

Use the following [detach-network-interface](../../../cli/latest/reference/ec2/detach-network-interface.md "../../../cli/latest/reference/ec2/detach-network-interface.md")
command.

```
aws ec2 detach-network-interface --attachment-id `eni-attach-016c93267131892c9`
```

PowerShell

###### To detach a network interface

Use the [Dismount-EC2NetworkInterface](../../../powershell/latest/reference/items/Dismount-EC2NetworkInterface.md "../../../powershell/latest/reference/items/Dismount-EC2NetworkInterface.md")
cmdlet.

```
Dismount-EC2NetworkInterface -AttachmentId `eni-attach-016c93267131892c9`
```
