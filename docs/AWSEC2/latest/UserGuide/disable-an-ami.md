# Disable an Amazon EC2 AMI

You can disable an AMI to prevent it from being used for instance launches. You can't launch
new instances from a disabled AMI. You can re-enable a disabled AMI so that it can be used
again for instance launches.

You can disable both private and public AMIs.

To reduce storage costs for disabled EBS-backed AMIs that are rarely used, but which need
to be retained long term, you can archive their associated snapshots. For more information,
see [Archive
Amazon EBS snapshots](../../../ebs/latest/userguide/snapshot-archive.md "../../../ebs/latest/userguide/snapshot-archive.md") in the _Amazon EBS User Guide_.

###### Contents

- [How AMI disable works](#how-disable-ami-works "#how-disable-ami-works")
- [Costs](#ami-disable-costs "#ami-disable-costs")
- [Prerequisites](#ami-disable-prerequisites "#ami-disable-prerequisites")
- [Required IAM permissions](#ami-disable-iam-permissions "#ami-disable-iam-permissions")
- [Disable an AMI](#disable-ami "#disable-ami")
- [Describe disabled AMIs](#describe-disabled-ami "#describe-disabled-ami")
- [Re-enable a disabled AMI](#re-enable-a-disabled-ami "#re-enable-a-disabled-ami")

## How AMI disable works

###### Warning

Disabling an AMI removes all its launch permissions.

###### When an AMI is disabled:

- The AMI's state changes to `disabled`.
- A disabled AMI can't be shared. If an AMI was public or previously shared, it is made
  private. If an AMI was shared with an AWS account, organization, or Organizational
  Unit, they lose access to the disabled AMI.
- A disabled AMI does not appear in [DescribeImages](../APIReference/API_DescribeImages.md "../APIReference/API_DescribeImages.md") API calls by default.
- A disabled AMI does not appear under the **Owned by me** console filter.
  To find disabled AMIs, use the **Disabled images** console
  filter.
- A disabled AMI is not available to select for instance launches in the EC2 console. For
  example, a disabled AMI does not appear in the AMI catalog in the launch instance
  wizard or when creating a launch template.
- Launch services, such as launch templates and Auto Scaling groups, can continue to reference
  disabled AMIs. Subsequent instance launches from a disabled AMI will fail, so we
  recommend updating launch templates and Auto Scaling groups to reference available AMIs
  only.
- EC2 instances that were previously launched using an AMI that is subsequently disabled are
  not affected, and can be stopped, started, and rebooted.
- You can't delete snapshots associated with disabled AMIs. Attempting to delete an
  associated snapshot results in the `snapshot is currently in use` error.

###### When an AMI is re-enabled:

- The AMI's state changes to `available`, and it can be used to launch
  instances.
- The AMI can be shared.
- AWS accounts, organizations, and Organizational Units that lost access to the AMI when it
  was disabled do not regain access automatically, but the AMI can be shared with them
  again.

## Costs

When you disable an AMI, the AMI is not deleted. If the AMI is an EBS-backed AMI, you
continue to pay for the AMI's EBS snapshots. If you want to keep the AMI, you might be
able to reduce your storage costs by archiving the snapshots. For more information, see
[Archive Amazon EBS snapshots](../../../ebs/latest/userguide/snapshot-archive.md "../../../ebs/latest/userguide/snapshot-archive.md") in the _Amazon EBS User Guide_.
If you don't want to keep the AMI and its snapshots, you must deregister the AMI and
delete the snapshots. For more information, see [Deregister an AMI](deregister-ami.md "deregister-ami.md").

## Prerequisites

To disable or re-enable an AMI, you must be the owner of the AMI.

## Required IAM permissions

To disable and re-enable an AMI, you must have the following IAM permissions:

- `ec2:DisableImage`
- `ec2:EnableImage`

## Disable an AMI

You can disable an AMI by using the EC2 console or the AWS Command Line Interface (AWS CLI). You must be the
AMI owner to perform this procedure.

Console

###### To disable an AMI

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the left navigation pane, choose **AMIs**.
3. From the filter bar, choose **Owned by
   me**.
4. Select the AMI, and then choose **Actions**, **Disable
   AMI**. You can select multiple AMIs to disable at
   once.
5. In the **Disable AMI** window, choose **Disable
   AMI**.

AWS CLI

###### To disable an AMI

Use the following [disable-image](../../../cli/latest/reference/ec2/disable-image.md "../../../cli/latest/reference/ec2/disable-image.md") command.

```
aws ec2 disable-image --image-id `ami-0abcdef1234567890`
```

PowerShell

###### To disable an AMI

Use the [Disable-EC2Image](../../../powershell/latest/reference/items/Disable-EC2Image.md "../../../powershell/latest/reference/items/Disable-EC2Image.md")
cmdlet.

```
Disable-EC2Image -ImageId `ami-0abcdef1234567890`
```

## Describe disabled AMIs

You can view disabled AMIs in the EC2 console and by using the AWS CLI.

You must be the AMI owner to view disabled AMIs. Because disabled AMIs are made private, you
can't view disabled AMIs if you're not the owner.

Console

###### To view disabled AMIs

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the left navigation pane, choose **AMIs**.
3. From the filter bar, choose **Disabled images**.

![The Disabled images filter.](images/ami-filter-by-disabled-images.png)

AWS CLI
By default, when you describe all AMIs, the disabled AMIs are not
included in the results. To include disabled AMIs in the results,
specify the `--include-disabled` option. The `State`
field for an AMI is `disabled` if the AMI is disabled.

###### To include disabled AMIs when describing all AMIs for an account

Use the following [describe-images](../../../cli/latest/reference/ec2/describe-images.md "../../../cli/latest/reference/ec2/describe-images.md") command.

```
aws ec2 describe-images \
    --owners `123456789012` \
    --include-disabled
```

###### To list the disabled AMIs for your account

Use the following [describe-images](../../../cli/latest/reference/ec2/describe-images.md "../../../cli/latest/reference/ec2/describe-images.md") command.

```
aws ec2 describe-images \
    --owners self \
    --include-disabled \
    --filters Name=state,Values=disabled \
    --query Images[].ImageId \
    --output text
```

The following is example output.

```
ami-0abcdef1234567890
```

###### To describe the status of an AMI

Use the following [describe-images](../../../cli/latest/reference/ec2/describe-images.md "../../../cli/latest/reference/ec2/describe-images.md") command. If `DeprecationTime`
is not present in the output, the AMI is not deprecated or set
to deprecate at a future date.

```
aws ec2 describe-images \
    --image-ids `ami-0abcdef1234567890` \
    --query Images[].State \
    --output text
```

The following is example output.

```
disabled
```

PowerShell
By default, when you describe all AMIs, the disabled AMIs are not
included in the results. To include disabled AMIs in the results,
specify the `-IncludeDisabled` parameter. The `State`
field for an AMI is `disabled` if the AMI is disabled.

###### To list the disabled AMIs for your account

Use the [Get-EC2Image](../../../powershell/latest/reference/items/Get-EC2Image.md "../../../powershell/latest/reference/items/Get-EC2Image.md")
cmdlet.

```
(Get-EC2Image `
    -Owner self `
    -IncludeDisabled $true | Where-Object {$_.State -eq "disabled"}).ImageId
```

The following is example output.

```
ami-0abcdef1234567890
```

###### To describe the status of an AMI

Use the [Get-EC2Image](../../../powershell/latest/reference/items/Get-EC2Image.md "../../../powershell/latest/reference/items/Get-EC2Image.md")
cmdlet.

```
(Get-EC2Image -ImageId `ami-0abcdef1234567890`).State.Value
```

The following is example output.

```
disabled
```

## Re-enable a disabled AMI

You can re-enable a disabled AMI. You must be the AMI owner to perform this procedure.

Console

###### To re-enable a disabled AMI

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the left navigation pane, choose **AMIs**.
3. From the filter bar, choose **Disabled images**.
4. Select the AMI, and then choose **Actions**, **Enable
   AMI**. You can select multiple AMIs to re-enable
   several AMIs at once.
5. In the **Enable AMI** window, choose **Enable**.

AWS CLI

###### To re-enable a disabled AMI

Use the following [enable-image](../../../cli/latest/reference/ec2/enable-image.md "../../../cli/latest/reference/ec2/enable-image.md") command.

```
aws ec2 enable-image --image-id `ami-0abcdef1234567890`
```

PowerShell

###### To re-enable a disabled AMI

Use the [Enable-EC2Image](../../../powershell/latest/reference/items/Enable-EC2Image.md "../../../powershell/latest/reference/items/Enable-EC2Image.md")
cmdlet.

```
Enable-EC2Image -ImageId `ami-0abcdef1234567890`
```
