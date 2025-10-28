# Manage the IPv4 addresses for your EC2

instances

You can assign a public IPv4 address to your instance when you launch it. You can view
the IPv4 addresses for your instance in the console through either the
**Instances** page or the **Network Interfaces**
page.

###### Tasks

- [Assign a public IPv4 address at launch](#public-ip-addresses "#public-ip-addresses")
- [Assign a private IPv4 address at
  launch](#assign-private-ipv4-address "#assign-private-ipv4-address")
- [View the primary IPv4 address](#view-instance-ipv4-addresses "#view-instance-ipv4-addresses")
- [View the IPv4 addresses using
  instance metadata](#view-instance-ipv4-addresses-imds "#view-instance-ipv4-addresses-imds")

## Assign a public IPv4 address at launch

Each subnet has an attribute that determines whether instances launched into that
subnet are assigned a public IP address. By default, nondefault subnets have this
attribute set to false, and default subnets have this attribute set to true. When
you launch an instance, a public IPv4 addressing feature is also available for you
to control whether your instance is assigned a public IPv4 address; you can override
the default behavior of the subnet's IP addressing attribute. The public IPv4
address is assigned from Amazon's pool of public IPv4 addresses, and is assigned to
the network interface with the device index of 0. This feature depends on certain
conditions at the time you launch your instance.

###### Considerations

- You can unassign the public IP address from your instance after launch by
  [managing the IP
  addresses associated with a network interface](managing-network-interface-ip-addresses.md "managing-network-interface-ip-addresses.md"). For more
  information about public IPv4 addresses, see [Public IPv4 addresses](using-instance-addressing.md#concepts-public-addresses "using-instance-addressing.md#concepts-public-addresses").
- You can't auto-assign a public IP address if you specify more than one
  network interface. Additionally, you cannot override the subnet setting
  using the auto-assign public IP feature if you specify an existing network
  interface for device index 0.
- Whether you assign a public IP address to your instance during launch or
  not, you can associate an Elastic IP address with your instance after it's
  launched. For more information, see [Elastic IP addresses](elastic-ip-addresses-eip.md "elastic-ip-addresses-eip.md"). You can also modify your
  subnet's public IPv4 addressing behavior. For more information, see [Modify the public IPv4
  addressing attribute for your subnet](../../../vpc/latest/userguide/subnet-public-ip.md "../../../vpc/latest/userguide/subnet-public-ip.md").

Console

###### To assign a public IPv4 address at launch

Follow the procedure to [launch an instance](ec2-launch-instance-wizard.md "ec2-launch-instance-wizard.md"), and when you configure [Network Settings](ec2-instance-launch-parameters.md#liw-network-settings "ec2-instance-launch-parameters.md#liw-network-settings"), choose
the option to **Auto-assign Public IP**.

AWS CLI

###### To assign a public IPv4 address at launch

Use the [run-instances](../../../cli/latest/reference/ec2/run-instances.md "../../../cli/latest/reference/ec2/run-instances.md") command with the
`--associate-public-ip-address` option.

```
--associate-public-ip-address
```

PowerShell

###### To assign a public IPv4 address at launch

Use the [New-EC2Instance](../../../powershell/latest/reference/items/New-EC2Instance.md "../../../powershell/latest/reference/items/New-EC2Instance.md") cmdlet with the
`-AssociatePublicIp` parameter.

```
-AssociatePublicIp $true
```

## Assign a private IPv4 address at

launch

You can specify a private IPv4 address from the IPv4 address range of the subnet,
or let Amazon EC2 chose one for you. This address is assigned to the primary network
interface.

To assign IPv4 addresses after launch, see [Assign secondary IP addresses to an
instance](instance-secondary-ip-addresses.md#assign-secondary-ip-address "instance-secondary-ip-addresses.md#assign-secondary-ip-address").

Console

###### To assign a private IPv4 address at launch

Follow the procedure to [launch an instance](ec2-launch-instance-wizard.md "ec2-launch-instance-wizard.md"). When you configure [Network Settings](ec2-instance-launch-parameters.md#liw-network-settings "ec2-instance-launch-parameters.md#liw-network-settings"), expand
**Advanced network configuration** and enter a
value for **Primary IP**.

AWS CLI

###### To assign a private IPv4 address at launch

Use the [run-instances](../../../cli/latest/reference/ec2/run-instances.md "../../../cli/latest/reference/ec2/run-instances.md") command with the
`--private-ip-address` option.

```
--private-ip-addresses `10.251.50.12`
```

To let Amazon EC2 choose the IP address, omit this option.

PowerShell

###### To assign a private IPv4 address at launch

Use the [New-EC2Instance](../../../powershell/latest/reference/items/New-EC2Instance.md "../../../powershell/latest/reference/items/New-EC2Instance.md") cmdlet with the
`-PrivateIpAddress` parameter.

```
-PrivateIpAddress `10.251.50.12`
```

To let Amazon EC2 choose the IP address, omit this parameter.

## View the primary IPv4 address

The public IPv4 address is displayed as a property of the network interface in the
console, but it's mapped to the primary private IPv4 address through NAT. Therefore,
if you inspect the properties of your network interface on your instance, for
example, through `ifconfig` (Linux) or `ipconfig` (Windows),
the public IPv4 address is not displayed.

Console

###### To view the IPv4 addresses for an instance

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the navigation pane, choose
   **Instances**.
3. Select the instance.
4. On the **Networking** tab, find
   **Public IPv4 address** and
   **Private IPv4 addresses**.
5. (Optional) The **Networking** tab also
   contains the network interfaces and Elastic IP addresses for the
   instance.

AWS CLI

###### To view the primary IPv4 address for an instance

Use the [describe-instances](../../../cli/latest/reference/ec2/describe-instances.md "../../../cli/latest/reference/ec2/describe-instances.md") command.

```
aws ec2 describe-instances \
    --instance-ids `i-1234567890abcdef0` \
    --query "Reservations[].Instances[].PrivateIpAddress" \
    --output text
```

The following is example output.

```
10.251.50.12
```

PowerShell

###### To view the primary IPv4 address for an instance

Use the [Get-EC2Instance](../../../powershell/latest/reference/items/Get-EC2Instance.md "../../../powershell/latest/reference/items/Get-EC2Instance.md") cmdlet.

```
(Get-EC2Instance `
    -InstanceId `i-1234567890abcdef0`).Instances.PrivateIpAddress
```

The following is example output.

```
10.251.50.12
```

## View the IPv4 addresses using

instance metadata

You can get the IPv4 addresses for your instance by retrieving instance metadata.
For more information, see [Use instance metadata to manage your EC2
instance](ec2-instance-metadata.md "ec2-instance-metadata.md").

###### To view the IPv4 addresses using instance metadata

1. Connect to your instance. For more information, see [Connect to your EC2 instance](connect.md "connect.md").
2. Run one of the following commands.

IMDSv2

###### Linux

Run the following command from your Linux instance.

```
TOKEN=`curl -X PUT "http://169.254.169.254/latest/api/token" -H "X-aws-ec2-metadata-token-ttl-seconds: 21600"` \
&& curl -H "X-aws-ec2-metadata-token: $TOKEN" http://169.254.169.254/latest/meta-data/local-ipv4
```

###### Windows

Run the following command from your Windows
instance.

```
[string]$token = Invoke-RestMethod -Headers @{"X-aws-ec2-metadata-token-ttl-seconds" = "21600"} `
    -Method PUT -Uri http://169.254.169.254/latest/api/token
```

```
Invoke-RestMethod -Headers @{"X-aws-ec2-metadata-token" = $token} `
    -Method GET -Uri http://169.254.169.254/latest/meta-data/local-ipv4
```

IMDSv1

###### Linux

Run the following command from your Linux instance.

```
curl http://169.254.169.254/latest/meta-data/local-ipv4
```

###### Windows

Run the following command from your Windows
instance.

```
Invoke-RestMethod http://169.254.169.254/latest/meta-data/local-ipv4
```

3. Use one of the following commands to access the public IP address. If
   there is an Elastic IP address associated with the instance, the command
   returns the Elastic IP address.

IMDSv2

###### Linux

Run the following command from your Linux instance.

```
`[ec2-user ~]$` TOKEN=`curl -X PUT "http://169.254.169.254/latest/api/token" -H "X-aws-ec2-metadata-token-ttl-seconds: 21600"` \
&& curl -H "X-aws-ec2-metadata-token: $TOKEN" http://169.254.169.254/latest/meta-data/public-ipv4
```

###### Windows

Run the following command from your Windows
instance.

```
[string]$token = Invoke-RestMethod -Headers @{"X-aws-ec2-metadata-token-ttl-seconds" = "21600"} `
    -Method PUT -Uri http://169.254.169.254/latest/api/token
```

```
Invoke-RestMethod -Headers @{"X-aws-ec2-metadata-token" = $token} `
    -Method GET -Uri http://169.254.169.254/latest/meta-data/public-ipv4
```

IMDSv1

###### Linux

Run the following command from your Linux instance.

```
curl http://169.254.169.254/latest/meta-data/public-ipv4
```

###### Windows

Run the following command from your Windows
instance.

```
Invoke-RestMethod http://169.254.169.254/latest/meta-data/public-ipv4
```
