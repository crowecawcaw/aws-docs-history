

# Use `AttachInternetGateway` with a CLI
<a name="example_ec2_AttachInternetGateway_section"></a>

The following code examples show how to use `AttachInternetGateway`.

Action examples are code excerpts from larger programs and must be run in context. You can see this action in context in the following code examples: 
+  [Create a basic virtual private network](example_vpc_GettingStartedCLI_section.md) 
+  [Getting started with graph databases](example_ec2_GettingStarted_064_section.md) 
+  [Virtual private network with private servers](example_vpc_GettingStartedPrivate_section.md) 

------
#### [ CLI ]

**AWS CLI**  
**To attach an internet gateway to your VPC**  
The following `attach-internet-gateway` example attaches the specified internet gateway to the specific VPC.  

```
aws ec2 attach-internet-gateway \
    --internet-gateway-id {{igw-0d0fb496b3EXAMPLE}} \
    --vpc-id {{vpc-0a60eb65b4EXAMPLE}}
```
This command produces no output.  
For more information, see [Internet gateways](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Internet_Gateway.html) in the *Amazon VPC User Guide*.  
+  For API details, see [AttachInternetGateway](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/attach-internet-gateway.html) in *AWS CLI Command Reference*. 

------
#### [ PowerShell ]

**Tools for PowerShell V4**  
**Example 1: This example attaches the specified Internet gateway to the specified VPC.**  

```
Add-EC2InternetGateway -InternetGatewayId igw-1a2b3c4d -VpcId vpc-12345678
```
**Example 2: This example creates a VPC and an Internet gateway, and then attaches the Internet gateway to the VPC.**  

```
$vpc = New-EC2Vpc -CidrBlock 10.0.0.0/16
New-EC2InternetGateway | Add-EC2InternetGateway -VpcId $vpc.VpcId
```
+  For API details, see [AttachInternetGateway](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*. 

**Tools for PowerShell V5**  
**Example 1: This example attaches the specified Internet gateway to the specified VPC.**  

```
Add-EC2InternetGateway -InternetGatewayId igw-1a2b3c4d -VpcId vpc-12345678
```
**Example 2: This example creates a VPC and an Internet gateway, and then attaches the Internet gateway to the VPC.**  

```
$vpc = New-EC2Vpc -CidrBlock 10.0.0.0/16
New-EC2InternetGateway | Add-EC2InternetGateway -VpcId $vpc.VpcId
```
+  For API details, see [AttachInternetGateway](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*. 

------

For a complete list of AWS SDK developer guides and code examples, see [Create Amazon EC2 resources using an AWS SDK](sdk-general-information-section.md). This topic also includes information about getting started and details about previous SDK versions.