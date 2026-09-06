

# Use `DescribeInternetGateways` with a CLI
<a name="example_ec2_DescribeInternetGateways_section"></a>

The following code examples show how to use `DescribeInternetGateways`.

Action examples are code excerpts from larger programs and must be run in context. You can see this action in context in the following code example: 
+  [Create a basic virtual private network](example_vpc_GettingStartedCLI_section.md) 

------
#### [ CLI ]

**AWS CLI**  
**To describe an internet gateway**  
The following `describe-internet-gateways` example describes the specified internet gateway.  

```
aws ec2 describe-internet-gateways \
    --internet-gateway-ids {{igw-0d0fb496b3EXAMPLE}}
```
Output:  

```
{
    "InternetGateways": [
        {
            "Attachments": [
                {
                    "State": "available",
                    "VpcId": "vpc-0a60eb65b4EXAMPLE"
                }
            ],
            "InternetGatewayId": "igw-0d0fb496b3EXAMPLE",
            "OwnerId": "123456789012",
            "Tags": [
                {
                    "Key": "Name",
                    "Value": "my-igw"
                }
            ]
        }
    ]
}
```
For more information, see [Internet gateways](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Internet_Gateway.html) in the *Amazon VPC User Guide*.  
+  For API details, see [DescribeInternetGateways](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-internet-gateways.html) in *AWS CLI Command Reference*. 

------
#### [ PowerShell ]

**Tools for PowerShell V4**  
**Example 1: This example describes the specified Internet gateway.**  

```
Get-EC2InternetGateway -InternetGatewayId igw-1a2b3c4d
```
**Output:**  

```
Attachments       InternetGatewayId     Tags
-----------       -----------------     ----
{vpc-1a2b3c4d}    igw-1a2b3c4d          {}
```
**Example 2: This example describes all your Internet gateways.**  

```
Get-EC2InternetGateway
```
**Output:**  

```
Attachments       InternetGatewayId     Tags
-----------       -----------------     ----
{vpc-1a2b3c4d}    igw-1a2b3c4d          {}
{}                igw-2a3b4c5d          {}
```
+  For API details, see [DescribeInternetGateways](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*. 

**Tools for PowerShell V5**  
**Example 1: This example describes the specified Internet gateway.**  

```
Get-EC2InternetGateway -InternetGatewayId igw-1a2b3c4d
```
**Output:**  

```
Attachments       InternetGatewayId     Tags
-----------       -----------------     ----
{vpc-1a2b3c4d}    igw-1a2b3c4d          {}
```
**Example 2: This example describes all your Internet gateways.**  

```
Get-EC2InternetGateway
```
**Output:**  

```
Attachments       InternetGatewayId     Tags
-----------       -----------------     ----
{vpc-1a2b3c4d}    igw-1a2b3c4d          {}
{}                igw-2a3b4c5d          {}
```
+  For API details, see [DescribeInternetGateways](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*. 

------

For a complete list of AWS SDK developer guides and code examples, see [Create Amazon EC2 resources using an AWS SDK](sdk-general-information-section.md). This topic also includes information about getting started and details about previous SDK versions.