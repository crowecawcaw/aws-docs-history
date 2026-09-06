

# Use `DescribeVpnGateways` with a CLI
<a name="example_ec2_DescribeVpnGateways_section"></a>

The following code examples show how to use `DescribeVpnGateways`.

Action examples are code excerpts from larger programs and must be run in context. You can see this action in context in the following code example: 
+  [Get started with dedicated network connections](example_directconnect_GettingStarted_051_section.md) 

------
#### [ CLI ]

**AWS CLI**  
**To describe your virtual private gateways**  
This example describes your virtual private gateways.  
Command:  

```
aws ec2 describe-vpn-gateways
```
Output:  

```
{
    "VpnGateways": [
        {
            "State": "available",
            "Type": "ipsec.1",
            "VpnGatewayId": "vgw-f211f09b",
            "VpcAttachments": [
                {
                    "State": "attached",
                    "VpcId": "vpc-98eb5ef5"
                }
            ]
        },
        {
            "State": "available",
            "Type": "ipsec.1",
            "VpnGatewayId": "vgw-9a4cacf3",
            "VpcAttachments": [
                {
                    "State": "attaching",
                    "VpcId": "vpc-a01106c2"
                }
            ]
        }
    ]
}
```
+  For API details, see [DescribeVpnGateways](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-vpn-gateways.html) in *AWS CLI Command Reference*. 

------
#### [ PowerShell ]

**Tools for PowerShell V4**  
**Example 1: This example describes the specified virtual private gateway.**  

```
Get-EC2VpnGateway -VpnGatewayId vgw-1a2b3c4d
```
**Output:**  

```
AvailabilityZone :
State            : available
Tags             : {}
Type             : ipsec.1
VpcAttachments   : {vpc-12345678}
VpnGatewayId     : vgw-1a2b3c4d
```
**Example 2: This example describes any virtual private gateway whose state is either pending or available.**  

```
$filter = New-Object Amazon.EC2.Model.Filter
$filter.Name = "state"
$filter.Values = @( "pending", "available" )

Get-EC2VpnGateway -Filter $filter
```
**Example 3: This example describes all your virtual private gateways.**  

```
Get-EC2VpnGateway
```
+  For API details, see [DescribeVpnGateways](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*. 

**Tools for PowerShell V5**  
**Example 1: This example describes the specified virtual private gateway.**  

```
Get-EC2VpnGateway -VpnGatewayId vgw-1a2b3c4d
```
**Output:**  

```
AvailabilityZone :
State            : available
Tags             : {}
Type             : ipsec.1
VpcAttachments   : {vpc-12345678}
VpnGatewayId     : vgw-1a2b3c4d
```
**Example 2: This example describes any virtual private gateway whose state is either pending or available.**  

```
$filter = New-Object Amazon.EC2.Model.Filter
$filter.Name = "state"
$filter.Values = @( "pending", "available" )

Get-EC2VpnGateway -Filter $filter
```
**Example 3: This example describes all your virtual private gateways.**  

```
Get-EC2VpnGateway
```
+  For API details, see [DescribeVpnGateways](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*. 

------

For a complete list of AWS SDK developer guides and code examples, see [Create Amazon EC2 resources using an AWS SDK](sdk-general-information-section.md). This topic also includes information about getting started and details about previous SDK versions.