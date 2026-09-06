

# Use `CreateCustomerGateway` with a CLI
<a name="example_ec2_CreateCustomerGateway_section"></a>

The following code examples show how to use `CreateCustomerGateway`.

------
#### [ CLI ]

**AWS CLI**  
**To create a customer gateway**  
This example creates a customer gateway with the specified IP address for its outside interface.  
Command:  

```
aws ec2 create-customer-gateway --type {{ipsec.1}} --public-ip {{12.1.2.3}} --bgp-asn {{65534}}
```
Output:  

```
{
    "CustomerGateway": {
        "CustomerGatewayId": "cgw-0e11f167",
        "IpAddress": "12.1.2.3",
        "State": "available",
        "Type": "ipsec.1",
        "BgpAsn": "65534"
    }
}
```
+  For API details, see [CreateCustomerGateway](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/create-customer-gateway.html) in *AWS CLI Command Reference*. 

------
#### [ PowerShell ]

**Tools for PowerShell V4**  
**Example 1: This example creates the specified customer gateway.**  

```
New-EC2CustomerGateway -Type ipsec.1 -PublicIp 203.0.113.12 -BgpAsn 65534
```
**Output:**  

```
BgpAsn            : 65534
CustomerGatewayId : cgw-1a2b3c4d
IpAddress         : 203.0.113.12
State             : available
Tags              : {}
Type              : ipsec.1
```
+  For API details, see [CreateCustomerGateway](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*. 

**Tools for PowerShell V5**  
**Example 1: This example creates the specified customer gateway.**  

```
New-EC2CustomerGateway -Type ipsec.1 -PublicIp 203.0.113.12 -BgpAsn 65534
```
**Output:**  

```
BgpAsn            : 65534
CustomerGatewayId : cgw-1a2b3c4d
IpAddress         : 203.0.113.12
State             : available
Tags              : {}
Type              : ipsec.1
```
+  For API details, see [CreateCustomerGateway](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*. 

------

For a complete list of AWS SDK developer guides and code examples, see [Create Amazon EC2 resources using an AWS SDK](sdk-general-information-section.md). This topic also includes information about getting started and details about previous SDK versions.