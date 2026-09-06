

# Use `EnableVpcClassicLink` with a CLI
<a name="example_ec2_EnableVpcClassicLink_section"></a>

The following code examples show how to use `EnableVpcClassicLink`.

------
#### [ CLI ]

**AWS CLI**  
**To enable a VPC for ClassicLink**  
This example enables vpc-8888888 for ClassicLink.  
Command:  

```
aws ec2 enable-vpc-classic-link --vpc-id {{vpc-88888888}}
```
Output:  

```
{
  "Return": true
}
```
+  For API details, see [EnableVpcClassicLink](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/enable-vpc-classic-link.html) in *AWS CLI Command Reference*. 

------
#### [ PowerShell ]

**Tools for PowerShell V4**  
**Example 1: This example enables VPC vpc-0123456b789b0d12f for ClassicLink**  

```
Enable-EC2VpcClassicLink -VpcId vpc-0123456b789b0d12f
```
**Output:**  

```
True
```
+  For API details, see [EnableVpcClassicLink](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*. 

**Tools for PowerShell V5**  
**Example 1: This example enables VPC vpc-0123456b789b0d12f for ClassicLink**  

```
Enable-EC2VpcClassicLink -VpcId vpc-0123456b789b0d12f
```
**Output:**  

```
True
```
+  For API details, see [EnableVpcClassicLink](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*. 

------

For a complete list of AWS SDK developer guides and code examples, see [Create Amazon EC2 resources using an AWS SDK](sdk-general-information-section.md). This topic also includes information about getting started and details about previous SDK versions.