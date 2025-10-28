# Use `CreateVpnGateway` with a CLI

The following code examples show how to use `CreateVpnGateway`.

CLI

**AWS CLI**

**To create a virtual private gateway**

This example creates a virtual private gateway.

Command:

```
`aws ec2 create-vpn-gateway --type `ipsec.1``

```

Output:

```
{
    "VpnGateway": {
        "AmazonSideAsn": 64512,
        "State": "available",
        "Type": "ipsec.1",
        "VpnGatewayId": "vgw-9a4cacf3",
        "VpcAttachments": []
    }
}
```

**To create a virtual private gateway with a specific Amazon-side ASN**

This example creates a virtual private gateway and specifies the Autonomous System Number (ASN) for the Amazon side of the BGP session.

Command:

```
`aws ec2 create-vpn-gateway --type `ipsec.1` --amazon-side-asn `65001``

```

Output:

```
{
    "VpnGateway": {
        "AmazonSideAsn": 65001,
        "State": "available",
        "Type": "ipsec.1",
        "VpnGatewayId": "vgw-9a4cacf3",
        "VpcAttachments": []
    }
}
```

- For API details, see
  [CreateVpnGateway](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/create-vpn-gateway.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/create-vpn-gateway.html")
  in _AWS CLI Command Reference_.

PowerShell

**Tools for PowerShell V4**

**Example 1: This example creates the specified virtual private gateway.**

```
New-EC2VpnGateway -Type ipsec.1

```

**Output:**

```
AvailabilityZone :
State            : available
Tags             : {}
Type             : ipsec.1
VpcAttachments   : {}
VpnGatewayId     : vgw-1a2b3c4d
```

- For API details, see
  [CreateVpnGateway](../../../powershell/v4/reference.md "../../../powershell/v4/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V4)_.

**Tools for PowerShell V5**

**Example 1: This example creates the specified virtual private gateway.**

```
New-EC2VpnGateway -Type ipsec.1

```

**Output:**

```
AvailabilityZone :
State            : available
Tags             : {}
Type             : ipsec.1
VpcAttachments   : {}
VpnGatewayId     : vgw-1a2b3c4d
```

- For API details, see
  [CreateVpnGateway](../../../powershell/v5/reference.md "../../../powershell/v5/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V5)_.

For a complete list of AWS SDK developer guides and code examples, see
[Create Amazon EC2 resources using an AWS SDK](sdk-general-information-section.md "sdk-general-information-section.md").
This topic also includes information about getting started and details about previous SDK versions.
