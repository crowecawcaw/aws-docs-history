

# Use `AssociateRouteTable` with a CLI
<a name="example_ec2_AssociateRouteTable_section"></a>

The following code examples show how to use `AssociateRouteTable`.

Action examples are code excerpts from larger programs and must be run in context. You can see this action in context in the following code examples: 
+  [Create a basic virtual private network](example_vpc_GettingStartedCLI_section.md) 
+  [Getting started with graph databases](example_ec2_GettingStarted_064_section.md) 
+  [Virtual private network with private servers](example_vpc_GettingStartedPrivate_section.md) 
+  [Working with network peering connections](example_ec2_GettingStarted_015_section.md) 

------
#### [ CLI ]

**AWS CLI**  
**To associate a route table with a subnet**  
This example associates the specified route table with the specified subnet.  
Command:  

```
aws ec2 associate-route-table --route-table-id {{rtb-22574640}} --subnet-id {{subnet-9d4a7b6c}}
```
Output:  

```
{
    "AssociationId": "rtbassoc-781d0d1a"
}
```
+  For API details, see [AssociateRouteTable](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/associate-route-table.html) in *AWS CLI Command Reference*. 

------
#### [ PowerShell ]

**Tools for PowerShell V4**  
**Example 1: This example associates the specified route table with the specified subnet.**  

```
Register-EC2RouteTable -RouteTableId rtb-1a2b3c4d -SubnetId subnet-1a2b3c4d
```
**Output:**  

```
rtbassoc-12345678
```
+  For API details, see [AssociateRouteTable](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*. 

**Tools for PowerShell V5**  
**Example 1: This example associates the specified route table with the specified subnet.**  

```
Register-EC2RouteTable -RouteTableId rtb-1a2b3c4d -SubnetId subnet-1a2b3c4d
```
**Output:**  

```
rtbassoc-12345678
```
+  For API details, see [AssociateRouteTable](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*. 

------

For a complete list of AWS SDK developer guides and code examples, see [Create Amazon EC2 resources using an AWS SDK](sdk-general-information-section.md). This topic also includes information about getting started and details about previous SDK versions.