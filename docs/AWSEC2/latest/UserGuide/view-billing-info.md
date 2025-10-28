# Finding AMI billing and usage details

The following properties can help you verify AMI charges on your bill:

- **Platform details**
- **Usage operation**
- **AMI ID**

Console

###### To find the AMI billing information for an AMI

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the navigation pane, choose **AMIs**.
3. Select the AMI.
4. On the **Details** tab, find
   **Platform details** and
   **Usage operation**.

###### To find the AMI billing information for an instance

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the navigation pane, choose **Instances**.
3. Select the instance.
4. On the **Details** tab, expand **Instance details**
   and find **Platform details** and **Usage operation**.

AWS CLI

###### To find the AMI billing information for an AMI

Use the [describe-images](../../../cli/latest/reference/ec2/describe-images.md "../../../cli/latest/reference/ec2/describe-images.md")
command.

```
aws ec2 describe-images \
    --image-ids `ami-0abcdef1234567890` \
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

###### To find the AMI billing information for an instance

Use the [describe-instances](../../../cli/latest/reference/ec2/describe-instances.md "../../../cli/latest/reference/ec2/describe-instances.md")
command.

```
aws ec2 describe-instances \
    --instance-ids `i-1234567890abcdef0` \
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

PowerShell

###### To find the AMI billing information for an AMI

Use the [Get-EC2Image](../../../powershell/latest/reference/items/Get-EC2Image.md "../../../powershell/latest/reference/items/Get-EC2Image.md")
cmdlet.

```
Get-EC2Image `
    -ImageId `ami-0abcdef1234567890` | `
    Format-List PlatformDetails, UsageOperation
```

The following is example output for a Linux AMI.

```
PlatformDetails : Linux/UNIX
UsageOperation  : RunInstances
```

###### To find the AMI billing information for an instance

Use the [Get-EC2Instance](../../../powershell/latest/reference/items/Get-EC2Instance.md "../../../powershell/latest/reference/items/Get-EC2Instance.md")
cmdlet.

```
(Get-EC2Instance `
    -InstanceId `i-1234567890abcdef0`).Instances | `
    Format-List PlatformDetails, UsageOperation
```

The following is example output for a Windows instance.

```
PlatformDetails : Windows
UsageOperation  : RunInstances:0002
```
