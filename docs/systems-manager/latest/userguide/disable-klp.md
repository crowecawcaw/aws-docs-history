

• The AWS Systems Manager CloudWatch Dashboard will no longer be available after April 30, 2026. Customers can continue to use Amazon CloudWatch console to view, create, and manage their Amazon CloudWatch dashboards, just as they do today. For more information, see [Amazon CloudWatch Dashboard documentation](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.html). 

# Turning off Kernel Live Patching using Run Command
<a name="disable-klp"></a>

To turn off Kernel Live Patching, you can either run `yum` commands on your managed nodes or use Run Command and the custom SSM document `AWS-ConfigureKernelLivePatching`.

**Note**  
If you no longer need to use Kernel Live Patching, you can turn it off at any time. Usually, turning off the feature isn't necessary.

For information about turning off Kernel Live Patching by running `yum` commands directly on the managed node, see [Enable Kernel Live Patching](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/al2-live-patching.html#al2-live-patching-enable) in the *Amazon EC2 User Guide*.

**Note**  
When you turn off Kernel Live Patching, the process uninstalls the Kernel Live Patching plugin and then reboots the managed node.

**To turn off Kernel Live Patching using Run Command (console)**

1. Open the AWS Systems Manager console at [https://console.aws.amazon.com/systems-manager/](https://console.aws.amazon.com/systems-manager/).

1. In the navigation pane, choose **Run Command**.

1. Choose **Run command**.

1. In the **Command document** list, choose the SSM document `AWS-ConfigureKernelLivePatching`.

1. In the **Command parameters** section, specify values for required parameters.

1. For information about working with the remaining controls on this page, see [Running commands from the console](running-commands-console.md).

1. Choose **Run**.

**To turn off Kernel Live Patching (AWS CLI)**
+ Run a command similar to the following.

------
#### [ Linux & macOS ]

  ```
  aws ssm send-command \
      --document-name "AWS-ConfigureKernelLivePatching" \
      --targets "Key=instanceIds,Values={{instance-id}}" \
      --parameters "EnableOrDisable=Disable"
  ```

------
#### [ Windows Server ]

  ```
  aws ssm send-command ^
      --document-name "AWS-ConfigureKernelLivePatching" ^
      --targets "Key=instanceIds,Values={{instance-id}}" ^
      --parameters "EnableOrDisable=Disable"
  ```

------

  Replace {{instance-id}} with the ID of the Amazon Linux 2 managed node on which you want to turn off the feature, such as i-02573cafcfEXAMPLE. To turn off the feature on multiple managed nodes, you can use either of the following formats.
  + `--targets "Key=instanceids,Values={{instance-id1}},{{instance-id2}}"`
  + `--targets "Key=tag:{{tag-key}},Values={{tag-value}}"`

  For information about other options you can use in the command, see [send-command](https://docs.aws.amazon.com/cli/latest/reference/ssm/send-command.html) in the *AWS CLI Command Reference*.