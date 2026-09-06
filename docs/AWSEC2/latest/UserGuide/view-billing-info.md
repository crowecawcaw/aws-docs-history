

# Finding AMI billing and usage details
<a name="view-billing-info"></a>

The following properties can help you verify AMI charges on your bill:
+ **Platform details**
+ **Usage operation**
+ **AMI ID**

------
#### [ Console ]

**To find the AMI billing information for an AMI**

1. Open the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/).

1. In the navigation pane, choose **AMIs**.

1. Select the AMI.

1. On the **Details** tab, find **Platform details** and **Usage operation**.

**To find the AMI billing information for an instance**

1. Open the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/).

1. In the navigation pane, choose **Instances**.

1. Select the instance.

1. On the **Details** tab, expand **Instance details** and find **Platform details** and **Usage operation**.

------
#### [ AWS CLI ]

**To find the AMI billing information for an AMI**  
Use the [describe-images](https://docs.aws.amazon.com/cli/latest/reference/ec2/describe-images.html) command.

```
aws ec2 describe-images \
    --image-ids {{ami-0abcdef1234567890}} \
    --query "Images[].{PlatformDetails:PlatformDetails,UsageOperation:UsageOperation}"
```

The following is example output for a Linux AMI.

```
[
    {
        "PlatformDetails": "Linux/UNIX",
        "UsageOperation": "RunInstances"
    }
]
```

**To find the AMI billing information for an instance**  
Use the [describe-instances](https://docs.aws.amazon.com/cli/latest/reference/ec2/describe-instances.html) command.

```
aws ec2 describe-instances \
    --instance-ids {{i-1234567890abcdef0}} \
    --query "Reservations[].Instances[].{PlatformDetails:PlatformDetails,UsageOperation:UsageOperation}"
```

The following is example output for a Windows instance.

```
[
    {
        "PlatformDetails": "Windows",
        "UsageOperation": "RunInstances:0002"
    }
]
```

------
#### [ PowerShell ]

**To find the AMI billing information for an AMI**  
Use the [Get-EC2Image](https://docs.aws.amazon.com/powershell/latest/reference/items/Get-EC2Image.html) cmdlet.

```
Get-EC2Image `
    -ImageId {{ami-0abcdef1234567890}} | `
    Format-List PlatformDetails, UsageOperation
```

The following is example output for a Linux AMI.

```
PlatformDetails : Linux/UNIX
UsageOperation  : RunInstances
```

**To find the AMI billing information for an instance**  
Use the [Get-EC2Instance](https://docs.aws.amazon.com/powershell/latest/reference/items/Get-EC2Instance.html) cmdlet.

```
(Get-EC2Instance `
    -InstanceId {{i-1234567890abcdef0}}).Instances | `
    Format-List PlatformDetails, UsageOperation
```

The following is example output for a Windows instance.

```
PlatformDetails : Windows
UsageOperation  : RunInstances:0002
```

------