# Use `DescribeImageAttribute` with a CLI

The following code examples show how to use `DescribeImageAttribute`.

CLI

**AWS CLI**

**To describe the launch permissions for an AMI**

This example describes the launch permissions for the specified AMI.

Command:

```
`aws ec2 describe-image-attribute --image-id `ami-5731123e` --attribute `launchPermission``

```

Output:

```
{
    "LaunchPermissions": [
        {
            "UserId": "123456789012"
        }
    ],
    "ImageId": "ami-5731123e",
}
```

**To describe the product codes for an AMI**

This example describes the product codes for the specified AMI. Note that this AMI has no product codes.

Command:

```
`aws ec2 describe-image-attribute --image-id `ami-5731123e` --attribute `productCodes``

```

Output:

```
{
    "ProductCodes": [],
    "ImageId": "ami-5731123e",
}
```

- For API details, see
  [DescribeImageAttribute](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-image-attribute.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-image-attribute.html")
  in _AWS CLI Command Reference_.

PowerShell

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

- For API details, see
  [DescribeImageAttribute](../../../powershell/v4/reference.md "../../../powershell/v4/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V4)_.

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

- For API details, see
  [DescribeImageAttribute](../../../powershell/v5/reference.md "../../../powershell/v5/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V5)_.

For a complete list of AWS SDK developer guides and code examples, see
[Create Amazon EC2 resources using an AWS SDK](sdk-general-information-section.md "sdk-general-information-section.md").
This topic also includes information about getting started and details about previous SDK versions.
