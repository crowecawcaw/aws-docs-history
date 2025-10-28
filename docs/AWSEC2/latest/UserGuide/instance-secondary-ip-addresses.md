# Secondary IP addresses for your EC2

instances

The first IPv4 address assigned to a network interface is known as the primary IP
address. Secondary IP addresses are additional IPv4 address assigned to a network
interface. For more information, see [Multiple IP addresses](using-instance-addressing.md#multiple-ip-addresses "using-instance-addressing.md#multiple-ip-addresses").

You can also assign multiple IPv6 addresses to an instance. For more information, see
[Manage the IPv6 addresses for your EC2
instances](working-with-ipv6-addresses.md "working-with-ipv6-addresses.md").

###### Tasks

- [Assign secondary IP addresses to an
  instance](#assign-secondary-ip-address "#assign-secondary-ip-address")
- [Configure the operating system to use secondary IP
  addresses](#StepTwoConfigOS "#StepTwoConfigOS")
- [Unassign a secondary IP address from
  an instance](#unassign-secondary-ip-address "#unassign-secondary-ip-address")

## Assign secondary IP addresses to an

instance

You can assign secondary IP addresses to the network interface for an instance as
you launch the instance, or after the instance is running.

Console

###### To assign a secondary IP address at launch

1. Follow the procedure to [launch an
   instance](ec2-launch-instance-wizard.md "ec2-launch-instance-wizard.md"). When you configure [Network Settings](ec2-instance-launch-parameters.md#liw-network-settings "ec2-instance-launch-parameters.md#liw-network-settings"),
   expand **Advanced network
   configuration**.
2. For **Secondary IP**, choose
   **Automatically assign** and enter the
   number of IP addresses for Amazon EC2 to assign. Alternatively,
   choose **Manually assign** and enter the IPv4
   addresses.
3. Complete the remaining steps to launch the instance.

###### To assign a secondary IP address after launch

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the navigation pane, choose
   **Instances**.
3. Select your instance, and choose **Actions**,
   **Networking**, **Manage IP
   addresses**.
4. Expand the network interface.
5. To add an IPv4 address, under **IPv4
   addresses**, choose **Assign new IP
   address**. Enter an IPv4 address from the range of
   the subnet, or leave the field blank to let Amazon EC2 choose one for
   you.
6. Choose **Save**.

AWS CLI

###### To assign a secondary IP address at launch

Use the [run-instances](../../../cli/latest/reference/ec2/run-instances.md "../../../cli/latest/reference/ec2/run-instances.md") command with the
`--secondary-private-ip-addresses` option.

```
--secondary-private-ip-addresses `10.251.50.12`
```

To let Amazon EC2 choose the IP address, use the
`--secondary-private-ip-address-count` option instead.
The following example assigns one secondary IP address.

```
--secondary-private-ip-address-count 1
```

Alternatively, you can create a network interface. For more
information, see [Create a network interface for your EC2 instance](create-network-interface.md "create-network-interface.md").

###### To assign a secondary IP address after launch

Use the [assign-private-ip-addresses](../../../cli/latest/reference/ec2/assign-private-ip-addresses.md "../../../cli/latest/reference/ec2/assign-private-ip-addresses.md") command with the
`--private-ip-addresses` option.

```
aws ec2 assign-private-ip-addresses \
    --network-interface-ids `eni-1234567890abcdef0` \
    --private-ip-addresses `10.251.50.12`
```

To let Amazon EC2 choose the IPv4 address, use the
`--secondary-private-ip-address-count` parameter instead.
The following example assigns one IPv4 address.

```
aws ec2 assign-private-ip-addresses \
    --network-interface-ids `eni-1234567890abcdef0` \
    --secondary-private-ip-address-count 1
```

PowerShell

###### To assign a secondary IP address at launch

You must create a network interface. For more information, see
[Create a network interface for your EC2 instance](create-network-interface.md "create-network-interface.md").

###### To assign a secondary IP address after launch

Use the [Register-EC2PrivateIpAddress](../../../powershell/latest/reference/items/Register-EC2PrivateIpAddress.md "../../../powershell/latest/reference/items/Register-EC2PrivateIpAddress.md") cmdlet with the
`-PrivateIpAddress` parameter.

```
Register-EC2PrivateIpAddress `
    -NetworkInterfaceId `eni-1234567890abcdef0` `
    -PrivateIpAddress `10.251.50.12`
```

To let Amazon EC2 choose the IPv4 addresses, use the
`-SecondaryPrivateIpAddressCount` parameter instead. The
following example assigns one IPv4 address.

```
Register-EC2PrivateIpAddress `
    -NetworkInterfaceId `eni-1234567890abcdef0` `
    -SecondaryPrivateIpAddressCount 1
```

## Configure the operating system to use secondary IP

addresses

After you assign a secondary IP address to your instance, you must configure the
operating system on your instance to recognize the additional private IPv4
address.

###### Linux instances

- If you are using Amazon Linux, the ec2-net-utils package can take care of this
  step for you. It configures additional network interfaces that you attach
  while the instance is running, refreshes secondary IPv4 addresses during
  DHCP lease renewal, and updates the related routing rules. You can
  immediately refresh the list of interfaces by using one of the following
  commands, depending on your system:
  `sudo systemctl restart systemd-networkd` (AL2023) or
  `sudo service network restart` (Amazon Linux 2). You can view the
  up-to-date list using the following command: `ip addr li`.
  If you require manual control over your network configuration, you can
  remove the ec2-net-utils package. For more information, see
  [Configure your network interface
  using ec2-net-utils](../../../linux/al2/ug/ec2-net-utils.md "../../../linux/al2/ug/ec2-net-utils.md").
- If you are using another Linux distribution, see the documentation for
  your Linux distribution. Search for information about configuring additional
  network interfaces and secondary IPv4 addresses. If the instance has two or
  more interfaces on the same subnet, search for information about using
  routing rules to work around asymmetric routing.

###### Windows instances

For more information, see [Configure secondary private IPv4 addresses for Windows instances](config-windows-multiple-ip.md "config-windows-multiple-ip.md").

## Unassign a secondary IP address from

an instance

If you no longer require a secondary IP address, you can unassign it from the
instance or the network interface. When a secondary private IPv4 address is
unassigned from a network interface, the Elastic IP address (if it exists) is also
disassociated.

Console

###### To unassign a secondary private IPv4 address from an

instance

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the navigation pane, choose
   **Instances**.
3. Select an instance, choose **Actions**,
   **Networking**, **Manage IP
   addresses**.
4. Expand the network interface. For **IPv4
   addresses**, choose **Unassign**
   for the IPv4 address to unassign.
5. Choose **Save**.

AWS CLI

###### To unassign a secondary private IP address

Use the [unassign-private-ip-addresses](../../../cli/latest/reference/ec2/unassign-private-ip-addresses.md "../../../cli/latest/reference/ec2/unassign-private-ip-addresses.md") command.

```
aws ec2 unassign-private-ip-addresses \
    --network-interface `eni-1234567890abcdef0`\
    --private-ip-addresses `10.251.50.12`
```

PowerShell

###### To unassign a secondary private IP address

Use the [Unregister-EC2PrivateIpAddress](../../../powershell/latest/reference/items/Unregister-EC2PrivateIpAddress.md "../../../powershell/latest/reference/items/Unregister-EC2PrivateIpAddress.md") cmdlet.

```
Unregister-EC2PrivateIpAddress `
    -NetworkInterface `eni-1234567890abcdef0` `
    -PrivateIpAddress `10.251.50.12`
```
