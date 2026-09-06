

# Reference the latest AMIs using Systems Manager public parameters
<a name="finding-an-ami-parameter-store"></a>

AWS Systems Manager provides public parameters for public AMIs maintained by AWS. You can use the public parameters when launching instances to ensure that you're using the latest AMIs. For example, the public parameter `/aws/service/ami-amazon-linux-latest/al2023-ami-kernel-default-arm64` is available in all Regions and always points to the latest version of the Amazon Linux 2023 AMI for arm64 architecture in a given Region.

The public parameters are available from the following paths:
+ **Linux** – `/aws/service/ami-amazon-linux-latest`
+ **Windows** – `/aws/service/ami-windows-latest`

For more information, see [Working with public parameters](https://docs.aws.amazon.com/systems-manager/latest/userguide/parameter-store-public-parameters.html) in the *AWS Systems Manager User Guide*.

## Find the SSM parameter for a public AMI
<a name="find-ssm-parameter-for-ami"></a>

When you describe a public AMI, the response includes the associated AWS Systems Manager (SSM) parameter in the `PublicSsmParameterName` field. Use this parameter to identify the SSM parameter that always points to the latest version of that AMI.

------
#### [ Console ]

**To find the SSM parameter for a public AMI**

1. Open the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/).

1. In the navigation pane, choose **AMIs**.

1. Select a public AMI.

1. On the **Details** tab, find **Public SSM parameter name**.

------
#### [ AWS CLI ]

**To find the SSM parameter for a public AMI**  
Use the [describe-images](https://docs.aws.amazon.com/cli/latest/reference/ec2/describe-images.html) command. The response includes the `PublicSsmParameterName` field for public AMIs that have an associated SSM parameter.

```
aws ec2 describe-images \
    --image-ids {{ami-0abcdef1234567890}}
```

The following example output shows the `PublicSsmParameterName` field. Some fields are omitted for brevity.

```
{
    "Images": [
        {
            "ImageId": "ami-0abcdef1234567890",
            "Name": "al2023-ami-2023.7.20260601.0-kernel-6.1-x86_64",
            ...
            "PublicSsmParameterName": "aws/service/ami-amazon-linux-latest/al2023-ami-kernel-default-x86_64"
        }
    ]
}
```

------
#### [ PowerShell ]

**To find the SSM parameter for a public AMI**  
Use the [Get-EC2Image](https://docs.aws.amazon.com/powershell/latest/reference/items/Get-EC2Image.html) cmdlet. The response includes the `PublicSsmParameterName` field for public AMIs that have an associated SSM parameter.

```
Get-EC2Image -ImageId {{ami-0abcdef1234567890}}
```

The following example output shows the `PublicSsmParameterName` field. Some fields are omitted for brevity.

```
ImageId                : ami-0abcdef1234567890
Name                   : al2023-ami-2023.7.20260601.0-kernel-6.1-x86_64
...
PublicSsmParameterName : aws/service/ami-amazon-linux-latest/al2023-ami-kernel-default-x86_64
```

------

## List the Amazon Linux AMIs
<a name="list-ami-amazon-linux-latest"></a>

------
#### [ AWS CLI ]

**To list the Linux AMIs in the current AWS Region**  
Use the following [get-parameters-by-path](https://docs.aws.amazon.com/cli/latest/reference/ssm/get-parameters-by-path.html) command. The value for the `--path` parameter is specific to Linux AMIs.

```
aws ssm get-parameters-by-path \
    --path /aws/service/ami-amazon-linux-latest \
    --query "Parameters[].Name"
```

------
#### [ PowerShell ]

**To list the Linux AMIs in the current AWS Region**  
Use the [Get-SSMParametersByPath](https://docs.aws.amazon.com/powershell/latest/reference/items/Get-SSMParametersByPath.html) cmdlet.

```
Get-SSMParametersByPath `
    -Path "/aws/service/ami-amazon-linux-latest" | `
    Sort-Object Name | Format-Table Name
```

------

## List the Windows AMIs
<a name="list-ami-windows-latest"></a>

------
#### [ AWS CLI ]

**To list the Windows AMIs in the current AWS Region**  
Use the following [get-parameters-by-path](https://docs.aws.amazon.com/cli/latest/reference/ssm/get-parameters-by-path.html) command. The value for the `--path` parameter is specific to Windows AMIs.

```
aws ssm get-parameters-by-path \
    --path /aws/service/ami-windows-latest \
    --query "Parameters[].Name"
```

------
#### [ PowerShell ]

**To list the Windows AMIs in the current AWS Region**  
Use the [Get-SSMParametersByPath](https://docs.aws.amazon.com/powershell/latest/reference/items/Get-SSMParametersByPath.html) cmdlet.

```
Get-SSMParametersByPath `
    -Path "/aws/service/ami-windows-latest" | `
    Sort-Object Name | Format-Table Name
```

------

## Launch an instance using a public parameter
<a name="launch-instance-public-parameter"></a>

To specify the public parameter when launching an instance, use the following syntax: `resolve:ssm:{{public-parameter}}`, where `resolve:ssm` is the standard prefix and `{{public-parameter}}` is the path and name of the public parameter.

------
#### [ AWS CLI ]

**To launch an instance using a public parameter**  
Use the [run-instances](https://docs.aws.amazon.com/cli/latest/reference/ec2/run-instances.html) command with the `--image-id` option. This example specifies a Systems Manager public parameter for the image ID to launch an instance using the latest Amazon Linux 2023 AMI

```
--image-id resolve:ssm:{{/aws/service/ami-amazon-linux-latest/al2023-ami-kernel-default-x86_64}}
```

------
#### [ PowerShell ]

**To launch an instance using a public parameter**  
Use the [New-EC2Instance](https://docs.aws.amazon.com/powershell/latest/reference/items/New-EC2Instance.html) cmdlet with the `-ImageId` parameter. This example specifies a Systems Manager public parameter for the image ID to launch an instance using the latest AMI for Windows Server 2022.

```
-ImageId "resolve:ssm:{{/aws/service/ami-windows-latest/Windows_Server-2022-English-Full-Base}}"
```

------

For more examples that use Systems Manager parameters, see [Query for the latest Amazon Linux AMI IDs Using AWS Systems Manager Parameter Store](https://aws.amazon.com/blogs/compute/query-for-the-latest-amazon-linux-ami-ids-using-aws-systems-manager-parameter-store/) and [Query for the Latest Windows AMI Using AWS Systems Manager Parameter Store](https://aws.amazon.com/blogs/mt/query-for-the-latest-windows-ami-using-systems-manager-parameter-store/).