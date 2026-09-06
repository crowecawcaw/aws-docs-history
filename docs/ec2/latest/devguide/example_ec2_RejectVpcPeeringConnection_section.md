

# Use `RejectVpcPeeringConnection` with a CLI
<a name="example_ec2_RejectVpcPeeringConnection_section"></a>

The following code examples show how to use `RejectVpcPeeringConnection`.

------
#### [ CLI ]

**AWS CLI**  
**To reject a VPC peering connection**  
This example rejects the specified VPC peering connection request.  
Command:  

```
aws ec2 reject-vpc-peering-connection --vpc-peering-connection-id {{pcx-1a2b3c4d}}
```
Output:  

```
{
    "Return": true
}
```
+  For API details, see [RejectVpcPeeringConnection](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/reject-vpc-peering-connection.html) in *AWS CLI Command Reference*. 

------
#### [ PowerShell ]

**Tools for PowerShell V4**  
**Example 1: The above example denies the request for VpcPeering request id pcx-01a2b3ce45fe67eb8**  

```
Deny-EC2VpcPeeringConnection -VpcPeeringConnectionId pcx-01a2b3ce45fe67eb8
```
+  For API details, see [RejectVpcPeeringConnection](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*. 

**Tools for PowerShell V5**  
**Example 1: The above example denies the request for VpcPeering request id pcx-01a2b3ce45fe67eb8**  

```
Deny-EC2VpcPeeringConnection -VpcPeeringConnectionId pcx-01a2b3ce45fe67eb8
```
+  For API details, see [RejectVpcPeeringConnection](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*. 

------

For a complete list of AWS SDK developer guides and code examples, see [Create Amazon EC2 resources using an AWS SDK](sdk-general-information-section.md). This topic also includes information about getting started and details about previous SDK versions.