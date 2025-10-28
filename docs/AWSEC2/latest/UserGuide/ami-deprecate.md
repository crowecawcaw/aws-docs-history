# Deprecate an Amazon EC2 AMI

You can deprecate an AMI to indicate that it is out of date and should not be used. You can
also specify a future deprecation date for an AMI, indicating when the AMI will be out of
date. For example, you might deprecate an AMI that is no longer actively maintained, or you
might deprecate an AMI that has been superseded by a newer version. By default, deprecated
AMIs do not appear in AMI listings, preventing new users from using out-of-date AMIs.
However, existing users and launch services, such as launch templates and Auto Scaling groups, can
continue to use a deprecated AMI by specifying its ID. To delete the AMI so that users and
services cannot use it, you must [deregister](deregister-ami.md "deregister-ami.md") it.

After an AMI is deprecated:

- For AMI users, the deprecated AMI does not appear in [DescribeImages](../APIReference/API_DescribeImages.md "../APIReference/API_DescribeImages.md")
  API calls unless you specify its ID or specify that deprecated AMIs must appear. AMI
  owners continue to see deprecated AMIs in [DescribeImages](../APIReference/API_DescribeImages.md "../APIReference/API_DescribeImages.md")
  API calls.
- For AMI users, the deprecated AMI is not available to select via the EC2 console.
  For example, a deprecated AMI does not appear in the AMI catalog in the launch
  instance wizard. AMI owners continue to see deprecated AMIs in the EC2
  console.
- For AMI users, if you know the ID of a deprecated AMI, you can continue to launch instances
  using the deprecated AMI by using the API, CLI, or the SDKs.
- Launch services, such as launch templates and Auto Scaling groups, can continue to
  reference deprecated AMIs.
- EC2 instances that were launched using an AMI that is subsequently deprecated are not
  affected, and can be stopped, started, and rebooted.
  You can deprecate both private and public AMIs.

###### Contents

- [Costs](#ami-deprecate-costs "#ami-deprecate-costs")
- [Considerations](#ami-deprecate-limitations "#ami-deprecate-limitations")
- [Deprecate an AMI](#deprecate-ami "#deprecate-ami")
- [Describe deprecated AMIs](#describe-deprecate-ami "#describe-deprecate-ami")
- [Cancel AMI deprecation](#cancel-deprecate-ami "#cancel-deprecate-ami")

## Costs

When you deprecate an AMI, the AMI is not deleted. The AMI owner continues to pay for the
AMI's snapshots. To stop paying for the snapshots, the AMI owner must delete the AMI by
[deregistering](deregister-ami.md "deregister-ami.md") it.

## Considerations

- To deprecate an AMI, you must be the owner of the AMI.
- AMIs that have not been used recently to launch an instance
  might be good candidates for deprecation or deregistering. For
  more information, see [Check when an Amazon EC2 AMI was last used](ami-last-launched-time.md "ami-last-launched-time.md").
- You can create Amazon Data Lifecycle Manager EBS-backed AMI policies to automate the deprecation of
  EBS-backed AMIs. For more information, see [Create AMI lifecycle policies](../../../ebs/latest/userguide/ami-policy.md "../../../ebs/latest/userguide/ami-policy.md").
- By default, the deprecation date of all public AMIs is set to two years from the AMI
  creation date. You can set the deprecation date to earlier than two years. To cancel the
  deprecation date, or to move the deprecation to a later date, you must make the AMI
  private by only [sharing it with specific AWS
  accounts](sharingamis-explicit.md "sharingamis-explicit.md").

## Deprecate an AMI

You can deprecate an AMI on a specific date and time. You must be the owner of the
AMI.

The upper limit for the deprecation date is 10 years from now, except for public AMIs,
where the upper limit is 2 years from the creation date. You can't specify a date in
the past.

Console

###### To deprecate an AMI on a specific date

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the left navigator, choose **AMIs**.
3. From the filter bar, choose **Owned by
   me**.
4. Select the AMI, and then choose **Actions**, **Manage AMI
   Deprecation**. You can select multiple AMIs to set the
   same deprecation date of several AMIs at once.
5. Select the **Enable** checkbox, and then enter the deprecation date and
   time.
6. Choose **Save**.

AWS CLI

###### To deprecate an AMI on a specific date

Use the [enable-image-deprecation](../../../cli/latest/reference/ec2/enable-image-deprecation.md "../../../cli/latest/reference/ec2/enable-image-deprecation.md") command. If you specify a value for seconds,
Amazon EC2 rounds the seconds to the nearest minute.

```
aws ec2 enable-image-deprecation \
    --image-id `ami-0abcdef1234567890` \
    --deprecate-at "`2025-04-15T13:17:12.000Z`"
```

PowerShell

###### To deprecate an AMI on a specific date

Use the [Enable-EC2ImageDeprecation](../../../powershell/latest/reference/items/Enable-EC2ImageDeprecation.md "../../../powershell/latest/reference/items/Enable-EC2ImageDeprecation.md")
cmdlet. If you specify a value for seconds, Amazon EC2 rounds
the seconds to the nearest minute.

```
Enable-EC2ImageDeprecation `
    -ImageId `ami-0abcdef1234567890` `
    -DeprecateAt `2025-04-15T13:17:12.000Z`
```

## Describe deprecated AMIs

You can view the deprecation date and time of an AMI, and filter AMIs by
deprecation date.

Console

###### To view the deprecation date of an AMI

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the left navigator, choose **AMIs**, and then select the AMI.
3. Check the **Deprecation time** field (if you selected the checkbox
   next to the AMI, it's located on the **Details**
   tab). The field shows the deprecation date and time of the AMI. If
   the field is empty, the AMI is not deprecated.

###### To filter AMIs by deprecation date

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the left navigator, choose **AMIs**.
3. From the filter bar, choose **Owned by me** or
   **Private images** (private images include AMIs
   that are shared with you as well as owned by you).
4. In the Search bar, enter `Deprecation time`
   (as you enter the letters, the **Deprecation time**
   filter appears), and then choose an operator and a date and
   time.

AWS CLI
When you describe all AMIs, the results depend on whether you are an
AMI user or the AMI owner.

- AMI user – By default, when you
  describe all AMIs, deprecated AMIs that are shared with you but not
  owned by you are excluded. To include deprecated AMIs in the results,
  specify the `--include-deprecated` option.
- AMI owner – When you describe
  all AMIs, all AMIs that you own, including deprecated AMIs, are
  included. You can't exclude deprecated AMIs that you own by using
  the `--no-include-deprecated` option.

###### To include deprecated AMIs when describing all AMIs for an account

Use the following [describe-images](../../../cli/latest/reference/ec2/describe-images.md "../../../cli/latest/reference/ec2/describe-images.md") command.

```
aws ec2 describe-images
    --owners `123456789012` \
    --include-deprecated
```

###### To describe the deprecated AMIs for your account

Use the following [describe-images](../../../cli/latest/reference/ec2/describe-images.md "../../../cli/latest/reference/ec2/describe-images.md") command.

```
aws ec2 describe-images \
    --owners self \
    --query "Images[?DeprecationTime!=null].ImageId" \
    --output text
```

The following is example output.

```
ami-0abcdef1234567890
```

###### To describe the deprecation date of an AMI

Use the following [describe-images](../../../cli/latest/reference/ec2/describe-images.md "../../../cli/latest/reference/ec2/describe-images.md") command. If `DeprecationTime`
is not present in the output, the AMI is not deprecated or set
to deprecate at a future date.

```
aws ec2 describe-images \
    --image-ids `ami-0abcdef1234567890` \
    --query Images[].DeprecationTime \
    --output text
```

The following is example output.

```
2025-05-01T00:00:00.000Z
```

PowerShell

###### To list the deprecated AMIs for your account

Use the [Get-EC2Image](../../../powershell/latest/reference/items/Get-EC2Image.md "../../../powershell/latest/reference/items/Get-EC2Image.md")
cmdlet.

```
(Get-EC2Image -Owner self | Where-Object {$_.DeprecationTime -ne $null}).ImageId
```

The following is example output.

```
ami-0abcdef1234567890
```

###### To describe the deprecation date of an AMI

Use the [Get-EC2Image](../../../powershell/latest/reference/items/Get-EC2Image.md "../../../powershell/latest/reference/items/Get-EC2Image.md")
cmdlet. If `DeprecationTime` is not present in the output,
the AMI is not deprecated or set to deprecate at a future date.

```
(Get-EC2Image -ImageId `ami-0abcdef1234567890`).DeprecationTime
```

The following is example output.

```
2025-05-01T00:00:00.000Z
```

## Cancel AMI deprecation

You can cancel the deprecation of an AMI, which removes the deprecation
date and time. You must be the AMI owner to perform this procedure.

Console

###### To cancel the deprecation of an AMI

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the left navigator, choose **AMIs**.
3. From the filter bar, choose **Owned by
   me**.
4. Select the AMI, and then choose **Actions**, **Manage AMI
   Deprecation**. You can select multiple AMIs to cancel
   the deprecation of several AMIs at once.
5. Clear the **Enable** checkbox, and then choose
   **Save**.

AWS CLI

###### To cancel the deprecation of an AMI

Use the following [disable-image-deprecation](../../../cli/latest/reference/ec2/disable-image-deprecation.md "../../../cli/latest/reference/ec2/disable-image-deprecation.md") command.

```
aws ec2 disable-image-deprecation --image-id `ami-0abcdef1234567890`
```

PowerShell

###### To cancel the deprecation of an AMI

Use the [Disable-EC2ImageDeprecation](../../../powershell/latest/reference/items/Disable-EC2ImageDeprecation.md "../../../powershell/latest/reference/items/Disable-EC2ImageDeprecation.md")
cmdlet.

```
Disable-EC2ImageDeprecation -ImageId `ami-0abcdef1234567890`
```
