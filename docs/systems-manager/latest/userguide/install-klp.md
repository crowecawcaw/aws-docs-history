

• The AWS Systems Manager CloudWatch Dashboard will no longer be available after April 30, 2026. Customers can continue to use Amazon CloudWatch console to view, create, and manage their Amazon CloudWatch dashboards, just as they do today. For more information, see [Amazon CloudWatch Dashboard documentation](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.html). 

# Applying kernel live patches using Run Command
<a name="install-klp"></a>

To apply kernel live patches, you can either run `yum` commands on your managed nodes or use Run Command and the SSM document `AWS-RunPatchBaseline`. 

For information about applying kernel live patches by running `yum` commands directly on the managed node, see [Apply kernel live patches](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/al2-live-patching.html#al2-live-patching-apply) in the *Amazon EC2 User Guide*.

**To apply kernel live patches using Run Command (console)**

1. Open the AWS Systems Manager console at [https://console.aws.amazon.com/systems-manager/](https://console.aws.amazon.com/systems-manager/).

1. In the navigation pane, choose **Run Command**.

1. Choose **Run command**.

1. In the **Command document** list, choose the SSM document `AWS-RunPatchBaseline`.

1. In the **Command parameters** section, do one of the following:
   + If you're checking whether new kernel live patches are available, for **Operation**, choose `Scan`. For **Reboot Option**, if don't want your managed nodes to reboot after this operation, choose `NoReboot`. After the operation is complete, you can check for new patches and compliance status in Compliance.
   + If you checked patch compliance already and are ready to apply available kernel live patches, for **Operation**, choose `Install`. For **Reboot Option**, if you don't want your managed nodes to reboot after this operation, choose `NoReboot`.

1. For information about working with the remaining controls on this page, see [Running commands from the console](running-commands-console.md).

1. Choose **Run**.

**To apply kernel live patches using Run Command (AWS CLI)**

1. To perform a `Scan` operation before checking your results in Compliance, run the following command from your local machine.

------
#### [ Linux & macOS ]

   ```
   aws ssm send-command \
       --document-name "AWS-RunPatchBaseline" \
       --targets "Key=InstanceIds,Values={{instance-id}}" \
       --parameters '{"Operation":["Scan"],"RebootOption":["RebootIfNeeded"]}'
   ```

------
#### [ Windows Server ]

   ```
   aws ssm send-command ^
       --document-name "AWS-RunPatchBaseline" ^
       --targets "Key=InstanceIds,Values={{instance-id}}" ^
       --parameters {\"Operation\":[\"Scan\"],\"RebootOption\":[\"RebootIfNeeded\"]}
   ```

------

   For information about other options you can use in the command, see [send-command](https://docs.aws.amazon.com/cli/latest/reference/ssm/send-command.html) in the *AWS CLI Command Reference*.

1. To perform an `Install` operation after checking your results in Compliance, run the following command from your local machine.

------
#### [ Linux & macOS ]

   ```
   aws ssm send-command \
       --document-name "AWS-RunPatchBaseline" \
       --targets "Key=InstanceIds,Values={{instance-id}}" \
       --parameters '{"Operation":["Install"],"RebootOption":["NoReboot"]}'
   ```

------
#### [ Windows Server ]

   ```
   aws ssm send-command ^
       --document-name "AWS-RunPatchBaseline" ^
       --targets "Key=InstanceIds,Values={{instance-id}}" ^
       --parameters {\"Operation\":[\"Install\"],\"RebootOption\":[\"NoReboot\"]}
   ```

------

In both of the preceding commands, replace {{instance-id}} with the ID of the Amazon Linux 2 managed node on which you want to apply kernel live patches, such as i-02573cafcfEXAMPLE. To turn on the feature on multiple managed nodes, you can use either of the following formats.
+ `--targets "Key=instanceids,Values={{instance-id1}},{{instance-id2}}"`
+ `--targets "Key=tag:{{tag-key}},Values={{tag-value}}"`

For information about other options you can use in these commands, see [send-command](https://docs.aws.amazon.com/cli/latest/reference/ssm/send-command.html) in the *AWS CLI Command Reference*.