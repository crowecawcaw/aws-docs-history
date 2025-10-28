# Protect an Amazon EC2 AMI from deregistration

You can turn on _deregistration protection_ on an AMI to
prevent accidental or malicious deletion. When you turn on deregistration protection, the AMI
can’t be deregistered by any user, regardless of their IAM permissions. If you want to
deregister the AMI, you must first turn off the deregistration protection on it.

When you turn on deregistration protection on an AMI, you have the option to include a
24-hour cooldown period. This cooldown period is the time during which deregistration
protection remains in effect after you turn it off. During this cooldown period, the AMI can’t
be deregistered. When the cooldown period ends, the AMI can be deregistered.

Deregistration protection is turned off by default on all existing and new AMIs.

## Turn on deregistration protection

Use the following procedures to turn on deregistration protection.

Console

###### To turn on deregistration protection

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the navigation pane, choose **AMIs**.
3. From the filter bar, choose **Owned by me** to list your
   available AMIs, or choose **Disabled images** to list your
   disabled AMIs.
4. Select the AMI on which you want to turn on deregistration protection, and
   then choose **Actions**, **Manage AMI deregistration
   protection**.
5. In the **Manage AMI deregistration protection** dialog box,
   you can turn on deregistration protection with or without a cooldown period.
   Choose one of the following options:
   - **Enable with a 24-hour cooldown period** – With a
     cooldown period, the AMI can’t be deregistered for 24 hours when
     deregistration protection is turned off.
   - **Enable without cooldown** – Without a cooldown
     period, the AMI can be deregistered immediately when deregistration protection
     is turned off.

6. Choose **Save**.

AWS CLI

###### To turn on deregistration protection

Use the [enable-image-deregistration-protection](../../../cli/latest/reference/ec2/enable-image-deregistration-protection.md "../../../cli/latest/reference/ec2/enable-image-deregistration-protection.md") command. To enable the
optional cooldown period, include the `--with-cooldown` option.

```
aws ec2 enable-image-deregistration-protection \
    --image-id `ami-0abcdef1234567890` \
    --with-cooldown
```

PowerShell

###### To turn on deregistration protection

Use the [Enable-EC2ImageDeregistrationProtection](../../../powershell/latest/reference/items/Enable-EC2ImageDeregistrationProtection.md "../../../powershell/latest/reference/items/Enable-EC2ImageDeregistrationProtection.md") cmdlet. To enable the
optional cooldown period, set the `-WithCooldown` parameter
to `true`.

```
Enable-EC2ImageDeregistrationProtection `
    -ImageId `ami-0abcdef1234567890` `
    -WithCooldown $true
```

## Turn off deregistration protection

Use the following procedures to turn off deregistration protection.

If you chose to include a 24-hour cooldown period when you turned on deregistration
protection for the AMI, then, when you turn off deregistration protection, you won’t
immediately be able to deregister the AMI. The cooldown period is the 24-hour time period
during which deregistration protection remains in effect even after you turn it off.
During this cooldown period, the AMI can’t be deregistered. After the cooldown period
ends, the AMI can be deregistered.

Console

###### To turn off deregistration protection

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the navigation pane, choose **AMIs**.
3. From the filter bar, choose **Owned by me** to list your
   available AMIs, or choose **Disabled images** to list your
   disabled AMIs.
4. Select the AMI to turn off deregistration protection, and then choose
   **Actions**, **Manage AMI deregistration
   protection**.
5. In the **Manage AMI deregistration protection** dialog box,
   choose **Disable**.
6. Choose **Save**.

AWS CLI

###### To turn off deregistration protection

Use the [disable-image-deregistration-protection](../../../cli/latest/reference/ec2/disable-image-deregistration-protection.md "../../../cli/latest/reference/ec2/disable-image-deregistration-protection.md") command.

```
aws ec2 disable-image-deregistration-protection --image-id `ami-0abcdef1234567890`
```

PowerShell

###### To turn off deregistration protection

Use the [Disable-EC2ImageDeregistrationProtection](../../../powershell/latest/reference/items/Disable-EC2ImageDeregistrationProtection.md "../../../powershell/latest/reference/items/Disable-EC2ImageDeregistrationProtection.md") cmdlet.

```
Disable-EC2ImageDeregistrationProtection -ImageId `ami-0abcdef1234567890`
```
