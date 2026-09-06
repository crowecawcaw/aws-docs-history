

# Use `DescribeVpcClassicLinkDnsSupport` with a CLI
<a name="example_ec2_DescribeVpcClassicLinkDnsSupport_section"></a>

The following code examples show how to use `DescribeVpcClassicLinkDnsSupport`.

------
#### [ CLI ]

**AWS CLI**  
**To describe ClassicLink DNS support for your VPCs**  
This example describes the ClassicLink DNS support status of all of your VPCs.  
Command:  

```
aws ec2 describe-vpc-classic-link-dns-support
```
Output:  

```
{
  "Vpcs": [
    {
      "VpcId": "vpc-88888888",
      "ClassicLinkDnsSupported": true
    },
    {
      "VpcId": "vpc-1a2b3c4d",
      "ClassicLinkDnsSupported": false
    }
  ]
}
```
+  For API details, see [DescribeVpcClassicLinkDnsSupport](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-vpc-classic-link-dns-support.html) in *AWS CLI Command Reference*. 

------
#### [ PowerShell ]

**Tools for PowerShell V4**  
**Example 1: This example describes the ClassicLink DNS support status of VPCs for the region eu-west-1**  

```
Get-EC2VpcClassicLinkDnsSupport -VpcId vpc-0b12d3456a7e8910d -Region eu-west-1
```
**Output:**  

```
ClassicLinkDnsSupported VpcId
----------------------- -----
False                   vpc-0b12d3456a7e8910d
False                   vpc-12cf3b4f
```
+  For API details, see [DescribeVpcClassicLinkDnsSupport](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*. 

**Tools for PowerShell V5**  
**Example 1: This example describes the ClassicLink DNS support status of VPCs for the region eu-west-1**  

```
Get-EC2VpcClassicLinkDnsSupport -VpcId vpc-0b12d3456a7e8910d -Region eu-west-1
```
**Output:**  

```
ClassicLinkDnsSupported VpcId
----------------------- -----
False                   vpc-0b12d3456a7e8910d
False                   vpc-12cf3b4f
```
+  For API details, see [DescribeVpcClassicLinkDnsSupport](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*. 

------

For a complete list of AWS SDK developer guides and code examples, see [Create Amazon EC2 resources using an AWS SDK](sdk-general-information-section.md). This topic also includes information about getting started and details about previous SDK versions.