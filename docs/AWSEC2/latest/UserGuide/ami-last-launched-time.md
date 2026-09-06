

# Check when an Amazon EC2 AMI was last used
<a name="ami-last-launched-time"></a>

Amazon EC2 automatically tracks the date and time when an AMI was last used to launch an instance. If you have an AMI that has not been used to launch an instance in a long time, consider whether the AMI is a good candidate for [deregistration](deregister-ami.md) or [deprecation](ami-deprecate.md).

**Considerations**
+ When an AMI is used to launch an instance, there is a 24-hour delay before that usage is reported.
+ You must be the owner of the AMI to get the last launched time.
+ AMI usage data is available starting April 2017.

------
#### [ Console ]

**To view the last launched time of an AMI**

1. Open the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/).

1. In the left navigation pane, choose **AMIs**.

1. From the filter bar, choose **Owned by me**.

1. Select the checkbox for the AMI.

1. On the **Details** tab, find **Last launched time**.

------
#### [ AWS CLI ]

**To view the last launched time by describing the AMI**  
Use the [describe-images](https://docs.aws.amazon.com/cli/latest/reference/ec2/describe-images.html) command. If `LastLaunchedTime` is not present in the output, verify that you own the AMI.

```
aws ec2 describe-images \
    --image-id {{ami-0abcdef1234567890}} \
    --query Images[].LastLaunchedTime \
    --output text
```

The following is example output.

```
2025-02-17T20:22:19Z
```

**To view the last launched time attribute of an AMI**  
Use the [describe-image-attribute](https://docs.aws.amazon.com/cli/latest/reference/ec2/describe-image-attribute.html) command. You must be the owner of the specified AMI.

```
aws ec2 describe-image-attribute \
    --image-id {{ami-0abcdef1234567890}} \
    --attribute lastLaunchedTime \
    --query LastLaunchedTime.Value \
    --output text
```

The following is example output.

```
2025-02-17T20:22:19Z
```

------
#### [ PowerShell ]

**To view the last launched time by describing the AMI**  
Use the [Get-EC2Image](https://docs.aws.amazon.com/powershell/latest/reference/items/Get-EC2Image.html) cmdlet. If `LastLaunchedTime` is not present in the output, verify that you own the AMI.

```
(Get-EC2Image -ImageId {{ami-0abcdef1234567890}}).LastLaunchedTime
```

The following is example output.

```
2025-02-17T20:22:19Z
```

**To view the last launched time attribute of an AMI**  
Use the [Get-EC2ImageAttribute](https://docs.aws.amazon.com/powershell/latest/reference/items/Get-EC2ImageAttribute.html) cmdlet. You must be the owner of the specified AMI.

```
(Get-EC2ImageAttribute `
    -ImageId {{ami-0abcdef1234567890}} `
    -Attribute LastLaunchedTime).LastLaunchedTime
```

The following is example output.

```
2025-02-17T20:22:19Z
```

------