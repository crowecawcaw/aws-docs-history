

# Use `ModifySubnetAttribute` with a CLI
<a name="example_ec2_ModifySubnetAttribute_section"></a>

The following code examples show how to use `ModifySubnetAttribute`.

Action examples are code excerpts from larger programs and must be run in context. You can see this action in context in the following code example: 
+  [Create a basic virtual private network](example_vpc_GettingStartedCLI_section.md) 

------
#### [ CLI ]

**AWS CLI**  
**To change a subnet's public IPv4 addressing behavior**  
This example modifies subnet-1a2b3c4d to specify that all instances launched into this subnet are assigned a public IPv4 address. If the command succeeds, no output is returned.  
Command:  

```
aws ec2 modify-subnet-attribute --subnet-id {{subnet-1a2b3c4d}} --map-public-ip-on-launch
```
**To change a subnet's IPv6 addressing behavior**  
This example modifies subnet-1a2b3c4d to specify that all instances launched into this subnet are assigned an IPv6 address from the range of the subnet.  
Command:  

```
aws ec2 modify-subnet-attribute --subnet-id {{subnet-1a2b3c4d}} --assign-ipv6-address-on-creation
```
For more information, see IP Addressing in Your VPC in the *AWS Virtual Private Cloud User Guide*.  
+  For API details, see [ModifySubnetAttribute](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/modify-subnet-attribute.html) in *AWS CLI Command Reference*. 

------
#### [ PowerShell ]

**Tools for PowerShell V4**  
**Example 1: This example enables public IP addressing for the specified subnet.**  

```
Edit-EC2SubnetAttribute -SubnetId subnet-1a2b3c4d -MapPublicIpOnLaunch $true
```
**Example 2: This example disables public IP addressing for the specified subnet.**  

```
Edit-EC2SubnetAttribute -SubnetId subnet-1a2b3c4d -MapPublicIpOnLaunch $false
```
+  For API details, see [ModifySubnetAttribute](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*. 

**Tools for PowerShell V5**  
**Example 1: This example enables public IP addressing for the specified subnet.**  

```
Edit-EC2SubnetAttribute -SubnetId subnet-1a2b3c4d -MapPublicIpOnLaunch $true
```
**Example 2: This example disables public IP addressing for the specified subnet.**  

```
Edit-EC2SubnetAttribute -SubnetId subnet-1a2b3c4d -MapPublicIpOnLaunch $false
```
+  For API details, see [ModifySubnetAttribute](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*. 

------

For a complete list of AWS SDK developer guides and code examples, see [Create Amazon EC2 resources using an AWS SDK](sdk-general-information-section.md). This topic also includes information about getting started and details about previous SDK versions.