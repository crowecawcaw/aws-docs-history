

# Use `DescribeImageAttribute` with a CLI
<a name="example_ec2_DescribeImageAttribute_section"></a>

The following code examples show how to use `DescribeImageAttribute`.

------
#### [ CLI ]

**AWS CLI**  
**Example 1: To describe the launch permissions for an AMI**  
The following `describe-image-attribute` example describes the launch permissions for the specified AMI.  

```
aws ec2 describe-image-attribute \
    --image-id {{ami-5731123e}} \
    --attribute {{launchPermission}}
```
Output:  

```
{
    "LaunchPermissions": [
        {
            "UserId": "123456789012"
        }
    ],
    "ImageId": "ami-5731123e"
}
```
For more information, see [Share an AMI with specific AWS accounts](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/sharingamis-explicit.html) in the *Amazon EC2 User Guide*.  
**Example 2: To describe the product codes for an AMI**  
The following `describe-image-attribute` example describes the product codes for the specified AMI. Note that this AMI has no product codes.  

```
aws ec2 describe-image-attribute \
    --image-id {{ami-5731123e}} \
    --attribute {{productCodes}}
```
Output:  

```
{
    "ProductCodes": [],
    "ImageId": "ami-5731123e"
}
```
For more information, see [Paid AMIs in the AWS Marketplace for Amazon EC2 instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/paid-amis.html) in the *Amazon EC2 User Guide*.  
+  For API details, see [DescribeImageAttribute](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-image-attribute.html) in *AWS CLI Command Reference*. 

------
#### [ PowerShell ]

**Tools for PowerShell V4**  
**Example 1: This example gets the description for the specified AMI.**  

```
Get-EC2ImageAttribute -ImageId ami-12345678 -Attribute description
```
**Output:**  

```
BlockDeviceMappings : {}
Description         : My image description
ImageId             : ami-12345678
KernelId            :
LaunchPermissions   : {}
ProductCodes        : {}
RamdiskId           :
SriovNetSupport     :
```
**Example 2: This example gets the launch permissions for the specified AMI.**  

```
Get-EC2ImageAttribute -ImageId ami-12345678 -Attribute launchPermission
```
**Output:**  

```
BlockDeviceMappings : {}
Description         :
ImageId             : ami-12345678
KernelId            :
LaunchPermissions   : {all}
ProductCodes        : {}
RamdiskId           :
SriovNetSupport     :
```
**Example 3: This example test whether enhanced networking is enabled.**  

```
Get-EC2ImageAttribute -ImageId ami-12345678 -Attribute sriovNetSupport
```
**Output:**  

```
BlockDeviceMappings : {}
Description         :
ImageId             : ami-12345678
KernelId            :
LaunchPermissions   : {}
ProductCodes        : {}
RamdiskId           :
SriovNetSupport     : simple
```
+  For API details, see [DescribeImageAttribute](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*. 

**Tools for PowerShell V5**  
**Example 1: This example gets the description for the specified AMI.**  

```
Get-EC2ImageAttribute -ImageId ami-12345678 -Attribute description
```
**Output:**  

```
BlockDeviceMappings : {}
Description         : My image description
ImageId             : ami-12345678
KernelId            :
LaunchPermissions   : {}
ProductCodes        : {}
RamdiskId           :
SriovNetSupport     :
```
**Example 2: This example gets the launch permissions for the specified AMI.**  

```
Get-EC2ImageAttribute -ImageId ami-12345678 -Attribute launchPermission
```
**Output:**  

```
BlockDeviceMappings : {}
Description         :
ImageId             : ami-12345678
KernelId            :
LaunchPermissions   : {all}
ProductCodes        : {}
RamdiskId           :
SriovNetSupport     :
```
**Example 3: This example test whether enhanced networking is enabled.**  

```
Get-EC2ImageAttribute -ImageId ami-12345678 -Attribute sriovNetSupport
```
**Output:**  

```
BlockDeviceMappings : {}
Description         :
ImageId             : ami-12345678
KernelId            :
LaunchPermissions   : {}
ProductCodes        : {}
RamdiskId           :
SriovNetSupport     : simple
```
+  For API details, see [DescribeImageAttribute](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*. 

------

For a complete list of AWS SDK developer guides and code examples, see [Create Amazon EC2 resources using an AWS SDK](sdk-general-information-section.md). This topic also includes information about getting started and details about previous SDK versions.