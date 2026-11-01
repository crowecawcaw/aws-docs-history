

# Use `AssociateDhcpOptions` with a CLI
<a name="example_ec2_AssociateDhcpOptions_section"></a>

The following code examples show how to use `AssociateDhcpOptions`.

------
#### [ CLI ]

**AWS CLI**  
**Example 1: To associate a DHCP options set with your VPC**  
The following `associate-dhcp-options` example associates the specified DHCP options set with the specified VPC.  

```
aws ec2 associate-dhcp-options \
    --dhcp-options-id {{dopt-d9070ebb}} \
    --vpc-id {{vpc-a01106c2}}
```
This command produces no output.  
For more information, see [Work with DHCP option sets](https://docs.aws.amazon.com/vpc/latest/userguide/DHCPOptionSet.html) in the *Amazon VPC User Guide*.  
**Example 2: To associate the default DHCP options set with your VPC**  
The following `associate-dhcp-options` example associates the default DHCP options set with the specified VPC.  

```
aws ec2 associate-dhcp-options \
    --dhcp-options-id {{default}} \
    --vpc-id {{vpc-a01106c2}}
```
This command produces no output.  
For more information, see [Work with DHCP option sets](https://docs.aws.amazon.com/vpc/latest/userguide/DHCPOptionSet.html) in the *Amazon VPC User Guide*.  
+  For API details, see [AssociateDhcpOptions](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/associate-dhcp-options.html) in *AWS CLI Command Reference*. 

------
#### [ PowerShell ]

**Tools for PowerShell V4**  
**Example 1: This example associates the specified DHCP options set with the specified VPC.**  

```
Register-EC2DhcpOption -DhcpOptionsId dopt-1a2b3c4d -VpcId vpc-12345678
```
**Example 2: This example associates the default DHCP options set with the specified VPC.**  

```
Register-EC2DhcpOption -DhcpOptionsId default -VpcId vpc-12345678
```
+  For API details, see [AssociateDhcpOptions](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*. 

**Tools for PowerShell V5**  
**Example 1: This example associates the specified DHCP options set with the specified VPC.**  

```
Register-EC2DhcpOption -DhcpOptionsId dopt-1a2b3c4d -VpcId vpc-12345678
```
**Example 2: This example associates the default DHCP options set with the specified VPC.**  

```
Register-EC2DhcpOption -DhcpOptionsId default -VpcId vpc-12345678
```
+  For API details, see [AssociateDhcpOptions](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*. 

------

For a complete list of AWS SDK developer guides and code examples, see [Create Amazon EC2 resources using an AWS SDK](sdk-general-information-section.md). This topic also includes information about getting started and details about previous SDK versions.