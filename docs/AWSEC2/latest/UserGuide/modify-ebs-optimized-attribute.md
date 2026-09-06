

# Enable EBS optimization for an Amazon EC2 instance
<a name="modify-ebs-optimized-attribute"></a>

You can manually enable EBS optimization only for previous generation instances types that optionally support EBS optimization. If you enable EBS optimization for these instance types, there is an [additional hourly fee](https://aws.amazon.com/ec2/previous-generation/#EBS-optimized_instances)

**Prerequisites**
+ Verify that the instance type requires that you enable EBS optimization. For more information, see [EBS optimization supported](ebs-optimized.md#previous).
+ To enable EBS optimization after launch, you must stop the instance.
**Warning**  
When you stop an instance, the data on instance store volumes is lost. To preserve this data, back it up to persistent storage.

------
#### [ Console ]

**To enable Amazon EBS optimization during launch**  
In the Launch instances wizard, select the required instance type. Expand the **Advanced details** section, then for **EBS-optimized instance**, select **Enable**.

If the selected instance type does not support Amazon EBS optimization, the drop-down is disabled. If the instance type is Amazon EBS-optimized by default, Enable is already selected.

**To enable Amazon EBS optimization after launch**

1. Open the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/).

1. In the navigation pane, choose **Instances**, and select the instance.

1. Stop the instance. Choose **Actions**, **Instance state**, **Stop instance**.

1. With the instance still selected, choose **Actions**, **Instance settings**, **Change instance type**.

1. Select **EBS-optimized** and then choose **Apply**.

   If the instance type is Amazon EBS-optimized by default, or if it does not support Amazon EBS optimization, the checkbox is disabled.

1. Restart the instance. Choose **Instance state**, **Start instance**.

------
#### [ AWS CLI ]

**To enable Amazon EBS optimization during launch**  
Use the [run-instances](https://docs.aws.amazon.com/cli/latest/reference/ec2/run-instances.html) command with the `--ebs-optimized` option.

**To enable Amazon EBS optimization after launch**

1. If the instance is running, stop it by using the [stop-instances](https://docs.aws.amazon.com/cli/latest/reference/ec2/stop-instances.html) command.

   ```
   aws ec2 stop-instances --instance-ids {{i-1234567890abcdef0}}
   ```

1. Enable EBS optimization by using the [modify-instance-attribute](https://docs.aws.amazon.com/cli/latest/reference/ec2/modify-instance-attribute.html) command with the `--ebs-optimized` option.

   ```
   aws ec2 modify-instance-attribute \
       --instance-id {{i-1234567890abcdef0}} \
       --ebs-optimized
   ```

------
#### [ PowerShell ]

**To enable Amazon EBS optimization during launch**  
Use the [New-EC2Instance](https://docs.aws.amazon.com/powershell/latest/reference/items/New-EC2Instance.html) cmdlet with the `-EbsOptimized` option.

**To enable Amazon EBS optimization after launch**

1. If the instance is running, stop it by using the [Stop-EC2Instance](https://docs.aws.amazon.com/powershell/latest/reference/items/Stop-EC2Instance.html) cmdlet.

   ```
   Stop-EC2Instance -InstanceId {{i-1234567890abcdef0}}
   ```

1. Enable EBS optimization by using the [Edit-EC2InstanceAttribute](https://docs.aws.amazon.com/powershell/latest/reference/items/Edit-EC2InstanceAttribute.html) cmdlet with the `-EbsOptimized` option.

   ```
   Edit-EC2InstanceAttribute `
       -InstanceId {{i-1234567890abcdef0}} `
       -EbsOptimized $true
   ```

------