# Identify the root volume type determined by your

AMI

The AMI that you use to launch an EC2 instance determines the type of the root volume.
The root volume of an EC2 instance is either an EBS volume or an instance store volume.

[Nitro-based instances](instance-types.md#instance-hypervisor-type "instance-types.md#instance-hypervisor-type") support only EBS root volumes. The following previous generation
instance types are the only instance types that support instance store root volumes:
C1, C3, D2, I2, M1, M2, M3, R3, and X1.

Console

###### To identify the root volume type determined by an AMI

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the navigation pane, choose **AMIs**, and select the AMI.
3. On the **Details** tab, check the value of **Root device
   type** as follows:
   - `ebs` – Instances launched from this AMI will get an EBS root
     volume
   - `instance store` – Instances launched from this AMI will get an
     instance store root volume.

AWS CLI

###### To identify the root volume type determined by an AMI

Use the [describe-images](../../../cli/latest/reference/ec2/describe-images.md "../../../cli/latest/reference/ec2/describe-images.md")
command.

```
aws ec2 describe-images \
    --image-ids `ami-0abcdef1234567890` \
    --query Images[].RootDeviceType
```

The following is example output.

```
ebs
```

PowerShell

###### To identify the root volume type determined by an AMI

Use the [Get-EC2Image](../../../powershell/latest/reference/items/Get-EC2Image.md "../../../powershell/latest/reference/items/Get-EC2Image.md")
cmdlet.

```
(Get-EC2Image `
    -ImageId `ami-0abcdef1234567890`).RootDeviceType.Value
```

The following is example output.

```
ebs
```
