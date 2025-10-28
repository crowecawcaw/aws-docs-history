# Enable EBS optimization for an Amazon EC2 instance

You can manually enable EBS optimization only for previous generation instances types
that optionally support EBS optimization. If you enable EBS optimization for these
instance types, there is [additional hourly fee](https://aws.amazon.com/ec2/previous-generation/#EBS-optimized_instances "https://aws.amazon.com/ec2/previous-generation/#EBS-optimized_instances")

###### Prerequisites

- Verify that the instance type requires that you enable EBS optimization. For
  more information, see [EBS optimization supported](ebs-optimized.md#previous "ebs-optimized.md#previous").
- To you enable EBS optimization after launch, you must stop the instance.

###### Warning

When you stop an instance, the data on any instance store volumes is erased.
To keep data from instance store volumes, be sure to back it up to persistent storage.

Console

###### To enable Amazon EBS optimization during launch

In the Launch instances wizard, select the required instance type. Expand the
**Advanced details** section, then for **EBS-optimized instance**,
select **Enable**.

If the selected instance type does not support Amazon EBS optimization, the drop-down is disabled.
If the instance type is Amazon EBS-optimized by default, Enable is already selected.

###### To enable Amazon EBS optimization after launch

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the navigation pane, choose **Instances**, and select the
   instance.
3. Stop the instance. Choose **Actions**, **Instance
   state**, **Stop instance**.
4. With the instance still selected, choose **Actions**,
   **Instance settings**, **Change instance type**.
5. Select **EBS-optimized** and then choose **Apply**.

If the instance type is Amazon EBS-optimized by default, or if it does not support Amazon EBS optimization,
the checkbox is disabled. 6. Restart the instance. Choose **Instance state**, **Start instance**.

AWS CLI

###### To enable Amazon EBS optimization during launch

Use the [run-instances](../../../cli/latest/reference/ec2/run-instances.md "../../../cli/latest/reference/ec2/run-instances.md")
command with the `--ebs-optimized` option.

###### To enable Amazon EBS optimization after launch

1. If the instance is running, stop it by using the
   [stop-instances](../../../cli/latest/reference/ec2/stop-instances.md "../../../cli/latest/reference/ec2/stop-instances.md")
   command.

```
aws ec2 stop-instances --instance-ids `i-1234567890abcdef0`
```

2. Enable EBS optimization by using the
   [modify-instance-attribute](../../../cli/latest/reference/ec2/modify-instance-attribute.md "../../../cli/latest/reference/ec2/modify-instance-attribute.md")
   command with the `--ebs-optimized` option.

```
aws ec2 modify-instance-attribute \
    --instance-id `i-1234567890abcdef0` \
    --ebs-optimized
```

PowerShell

###### To enable Amazon EBS optimization during launch

Use the [New-EC2Instance](../../../powershell/latest/reference/items/New-EC2Instance.md "../../../powershell/latest/reference/items/New-EC2Instance.md")
cmdlet with the `-EbsOptimized` option.

###### To enable Amazon EBS optimization after launch

1. If the instance is running, stop it by using the
   [Stop-EC2Instance](../../../powershell/latest/reference/items/Stop-EC2Instance.md "../../../powershell/latest/reference/items/Stop-EC2Instance.md") cmdlet.

```
Stop-EC2Instance -InstanceId `i-1234567890abcdef0`
```

2. Enable EBS optimization by using the
   [Edit-EC2InstanceAttribute](../../../powershell/latest/reference/items/Edit-EC2InstanceAttribute.md "../../../powershell/latest/reference/items/Edit-EC2InstanceAttribute.md")
   cmdlet with the `-EbsOptimized` option.

```
Edit-EC2InstanceAttribute `
    -InstanceId `i-1234567890abcdef0` `
    -EbsOptimized $true
```
