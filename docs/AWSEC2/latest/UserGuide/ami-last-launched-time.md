# Check when an Amazon EC2 AMI was last used

Amazon EC2 automatically tracks the date and time when an AMI was last used to launch an
instance. If you have an AMI that has not been used to launch an instance in a long
time, consider whether the AMI is a good candidate for [deregistration](deregister-ami.md "deregister-ami.md") or [deprecation](ami-deprecate.md "ami-deprecate.md").

###### Considerations

- When an AMI is used to launch an instance, there is a 24-hour delay before that usage is
  reported.
- You must be the owner of the AMI to get the last launched time.
- AMI usage data is available starting April 2017.

Console

###### To view the last launched time of an AMI

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the left navigation pane, choose **AMIs**.
3. From the filter bar, choose **Owned by me**.
4. Select the checkbox for the AMI.
5. On the **Details** tab, find **Last launched time**.

AWS CLI

###### To view the last launched time by describing the AMI

Use the [describe-images](../../../cli/latest/reference/ec2/describe-images.md "../../../cli/latest/reference/ec2/describe-images.md")
command. If `LastLaunchedTime` is not present in the output,
verify that you own the AMI.

```
aws ec2 describe-images \
    --image-id `ami-0abcdef1234567890` \
    --query Images[].LastLaunchedTime \
    --output text
```

The following is example output.

```
2025-02-17T20:22:19Z
```

###### To view the last launched time attribute of an AMI

Use the [describe-image-attribute](../../../cli/latest/reference/ec2/describe-image-attribute.md "../../../cli/latest/reference/ec2/describe-image-attribute.md") command. You must be the owner
of the specified AMI.

```
aws ec2 describe-image-attribute \
    --image-id `ami-0abcdef1234567890` \
    --attribute lastLaunchedTime \
    --query LastLaunchedTime.Value \
    --output text
```

The following is example output.

```
2025-02-17T20:22:19Z
```

PowerShell

###### To view the last launched time by describing the AMI

Use the [Get-EC2Image](../../../powershell/latest/reference/items/Get-EC2Image.md "../../../powershell/latest/reference/items/Get-EC2Image.md")
cmdlet. If `LastLaunchedTime` is not present in the output,
verify that you own the AMI.

```
(Get-EC2Image -ImageId `ami-0abcdef1234567890`).LastLaunchedTime
```

The following is example output.

```
2025-02-17T20:22:19Z
```

###### To view the last launched time attribute of an AMI

Use the [Get-EC2ImageAttribute](../../../powershell/latest/reference/items/Get-EC2ImageAttribute.md "../../../powershell/latest/reference/items/Get-EC2ImageAttribute.md")
cmdlet. You must be the owner of the specified AMI.

```
(Get-EC2ImageAttribute `
    -ImageId `ami-0abcdef1234567890` `
    -Attribute LastLaunchedTime).LastLaunchedTime
```

The following is example output.

```
2025-02-17T20:22:19Z
```
