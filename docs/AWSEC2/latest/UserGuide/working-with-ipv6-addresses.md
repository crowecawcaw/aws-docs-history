# Manage the IPv6 addresses for your EC2

instances

If your VPC and subnet have IPv6 CIDR blocks associated with them, you can assign an
IPv6 address to your instance during or after launch. You can access the IPv6 addresses
for your instances in the console on either the **Instances** page or
the **Network Interfaces** page. The following tasks configure IP
addresses for your instances. To configure IP addresses for your network interfaces
instead, see [Manage the IP addresses for your network interface](managing-network-interface-ip-addresses.md "managing-network-interface-ip-addresses.md").

###### Tasks

- [Assign an IPv6 address to an instance](#assign-ipv6-address "#assign-ipv6-address")
- [View the IPv6 addresses for an
  instance](#view-ipv6-addresses "#view-ipv6-addresses")
- [View IPv6 addresses using instance
  metadata](#view-ipv6-addresses-imds "#view-ipv6-addresses-imds")
- [Unassign an IPv6 address from an
  instance](#unassign-ipv6-address "#unassign-ipv6-address")

## Assign an IPv6 address to an instance

You can specify an IPv6 address from the IPv6 address range of the subnet, or let
Amazon EC2 choose one for you. This address is assigned to the primary network interface.
Note that the following instance types do not support IPv6 addresses:
C1, M1, M2, M3, and T1.

Console

###### To assign an IPv6 address at launch

Follow the procedure to [launch an instance](ec2-launch-instance-wizard.md "ec2-launch-instance-wizard.md"). When you configure [Network Settings](ec2-instance-launch-parameters.md#liw-network-settings "ec2-instance-launch-parameters.md#liw-network-settings"), choose
the option to **Auto-assign IPv6 IP**. If you don't
see this option, the selected subnet does not have an associated
IPv6 CIDR block.

###### To assign an IPv6 address after launch

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the navigation pane, choose
   **Instances**.
3. Select your instance, and choose **Actions**,
   **Networking**, **Manage IP
   addresses**.
4. Expand the network interface. Under **IPv6
   addresses**, choose **Assign new IP
   address**.
5. Enter an IPv6 address from the range of the subnet, or leave
   the field blank to let Amazon EC2 choose the IPv6 address for you. If
   you don't see this option, the instance subnet does not have an
   associated IPv6 CIDR block.
6. Choose **Save**.

AWS CLI

###### To assign an IPv6 address at launch

Use the [run-instances](../../../cli/latest/reference/ec2/run-instances.md "../../../cli/latest/reference/ec2/run-instances.md") command with the
`--ipv6-addresses` option. The following example
assigns two IPv6 addresses.

```
--ipv6-addresses Ipv6Address=`2001:db8::1234:5678:1.2.3.4` Ipv6Address=`2001:db8::1234:5678:5.6.7.8`
```

To let Amazon EC2 choose the IPv6 addresses, use the
`--ipv6-address-count` option instead. The following
example assigns two IPv6 addresses.

```
--ipv6-address-count 2
```

###### To assign an IPv6 address after launch

Use the [assign-ipv6-addresses](../../../cli/latest/reference/ec2/assign-ipv6-addresses.md "../../../cli/latest/reference/ec2/assign-ipv6-addresses.md") command. The following example
assigns two IPv6 addresses.

```
aws ec2 assign-ipv6-addresses \
    --network-interface-id `eni-1234567890abcdef0` \
    --ipv6-addresses `2001:db8::1234:5678:1.2.3.4` `2001:db8::1234:5678:5.6.7.8`
```

To let Amazon EC2 choose the IPv6 addresses, use the
`--ipv6-address-count` option instead. The following
example assigns two IPv6 addresses.

```
aws ec2 assign-ipv6-addresses \
    --network-interface-id `eni-1234567890abcdef0` \
    --ipv6-address-count 2
```

PowerShell

###### To assign an IPv6 address at launch

Use the [New-EC2Instance](../../../powershell/latest/reference/items/New-EC2Instance.md "../../../powershell/latest/reference/items/New-EC2Instance.md") cmdlet with the
`-Ipv6Address` parameter. The following example
assigns two IPv6 addresses.

```
-Ipv6Address $ipv6addr1,$ipv6addr2
```

Define the IPv6 addresses as follows.

```
$ipv6addr1 = New-Object Amazon.EC2.Model.InstanceIpv6Address
$ipv6addr1.Ipv6Address = "`2001:db8::1234:5678:1.2.3.4`"
$ipv6addr2 = New-Object Amazon.EC2.Model.InstanceIpv6Address
$ipv6addr2.Ipv6Address = "`2001:db8::1234:5678:5.6.7.8`"
```

To let Amazon EC2 choose the IPv6 addresses, use the
`-Ipv6AddressCount` parameter instead. The following
example assigns two IPv6 addresses.

```
-Ipv6AddressCount 2
```

###### To assign an IPv6 address after launch

Use the [Register-EC2Ipv6AddressList](../../../powershell/latest/reference/items/Register-EC2Ipv6AddressList.md "../../../powershell/latest/reference/items/Register-EC2Ipv6AddressList.md") cmdlet. The following
example assigns two IPv6 addresses.

```
Register-EC2Ipv6AddressList `
    -NetworkInterfaceId `eni-1234567890abcdef0` `
    -Ipv6Address "`2001:db8::1234:5678:1.2.3.4`","`2001:db8::1234:5678:5.6.7.8`"
```

To let Amazon EC2 choose the IPv6 addresses, use the
`-Ipv6AddressCount` parameter instead. The following
example assigns two IPv6 addresses.

```
Register-EC2Ipv6AddressList `
    -NetworkInterfaceId `eni-1234567890abcdef0` `
    -Ipv6AddressCount 2
```

## View the IPv6 addresses for an

instance

You can view the IPv6 addresses for your instances.

Console

###### To view the IPv6 addresses for an instance

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the navigation pane, choose
   **Instances**.
3. Select the instance.
4. On the **Networking** tab, locate
   **IPv6 addresses**.

AWS CLI

###### To view the IPv6 address for an instance

Use the [describe-instances](../../../cli/latest/reference/ec2/describe-instances.md "../../../cli/latest/reference/ec2/describe-instances.md") command.

```
aws ec2 describe-instances \
    --instance-ids `i-1234567890abcdef0` \
    --query "Reservations[*].Instances[].Ipv6Address" \
    --output text
```

The following is example output.

```
2001:db8::1234:5678:1.2.3.4
```

PowerShell

###### To view the IPv6 address for an instance

Use the [Get-EC2Instance](../../../powershell/latest/reference/items/Get-EC2Instance.md "../../../powershell/latest/reference/items/Get-EC2Instance.md") cmdlet.

```
(Get-EC2Instance `
    -InstanceId `i-1234567890abcdef0`).Instances.Ipv6Address
```

The following is example output.

```
2001:db8::1234:5678:1.2.3.4
```

## View IPv6 addresses using instance

metadata

After you connect to your instance, you can retrieve the IPv6 addresses using
instance metadata. First, you must get the MAC address of the instance from
`http://169.254.169.254/latest/meta-data/network/interfaces/macs/`.

IMDSv2

###### Linux

Run the following command from your Linux instance.

```
TOKEN=`curl -X PUT "http://169.254.169.254/latest/api/token" -H "X-aws-ec2-metadata-token-ttl-seconds: 21600"` \
&& curl -H "X-aws-ec2-metadata-token: $TOKEN" http://169.254.169.254/latest/meta-data/network/interfaces/macs/`mac-address`/ipv6s
```

###### Windows

Run the following cmdlets from your Windows instance.

```
[string]$token = Invoke-RestMethod -Headers @{"X-aws-ec2-metadata-token-ttl-seconds" = "21600"} `
    -Method PUT -Uri http://169.254.169.254/latest/api/token
```

```
Invoke-RestMethod -Headers @{"X-aws-ec2-metadata-token" = $token} `
    -Method GET -Uri http://169.254.169.254/latest/meta-data/network/interfaces/macs/`mac-address`/ipv6s
```

IMDSv1

###### Linux

Run the following command from your Linux instance.

```
curl http://169.254.169.254/latest/meta-data/network/interfaces/macs/`mac-address`/ipv6s
```

###### Windows

Run the following cmdlet from your Windows instance.

```
Invoke-RestMethod -Uri http://169.254.169.254/latest/meta-data/network/interfaces/macs/`mac-address`/ipv6s
```

## Unassign an IPv6 address from an

instance

You can unassign an IPv6 address from an instance at any time.

Console

###### To unassign an IPv6 address from an instance

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the navigation pane, choose
   **Instances**.
3. Select your instance, and choose **Actions**,
   **Networking**, **Manage IP
   addresses**.
4. Expand the network interface. Under **IPv6
   addresses**, choose **Unassign**
   next to the IPv6 address.
5. Choose **Save**.

AWS CLI

###### To unassign an IPv6 address from an instance

Use the [unassign-ipv6-addresses](../../../cli/latest/reference/ec2/unassign-ipv6-addresses.md "../../../cli/latest/reference/ec2/unassign-ipv6-addresses.md") command.

```
aws ec2 unassign-ipv6-addresses \
    --network-interface-id `eni-1234567890abcdef0` \
    --ipv6-addresses `2001:db8::1234:5678:1.2.3.4`
```

PowerShell

###### To unassign an IPv6 address from an instance

Use the [Unregister-EC2Ipv6AddressList](../../../powershell/latest/reference/items/Unregister-EC2Ipv6AddressList.md "../../../powershell/latest/reference/items/Unregister-EC2Ipv6AddressList.md") cmdlet.

```
Unregister-EC2Ipv6AddressList `
    -NetworkInterfaceId `eni-1234567890abcdef0` `
    -Ipv6Address `2001:db8::1234:5678:1.2.3.4`
```
