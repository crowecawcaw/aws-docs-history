# Turning off Kernel Live Patching using Run Command

To turn off Kernel Live Patching, you can either run `yum` commands on your
managed nodes or use Run Command and the custom SSM document
`AWS-ConfigureKernelLivePatching`.

###### Note

If you no longer need to use Kernel Live Patching, you can turn it off at any
time. In most cases, turning off the feature isn't necessary.

For information about turning off Kernel Live Patching by running `yum` commands
directly on the managed node, see [Enable Kernel Live Patching](../../../AWSEC2/latest/UserGuide/al2-live-patching.md#al2-live-patching-enable "../../../AWSEC2/latest/UserGuide/al2-live-patching.md#al2-live-patching-enable") in the _Amazon EC2 User Guide_.

###### Note

When you turn off Kernel Live Patching, the process uninstalls the Kernel Live Patching plugin and
then reboots the managed node.

###### To turn off Kernel Live Patching using Run Command (console)

1. Open the AWS Systems Manager console at [https://console.aws.amazon.com/systems-manager/](https://console.aws.amazon.com/systems-manager/ "https://console.aws.amazon.com/systems-manager/").
2. In the navigation pane, choose **Run Command**.
3. Choose **Run command**.
4. In the **Command document** list, choose the SSM
   document `AWS-ConfigureKernelLivePatching`.
5. In the **Command parameters** section, specify values for
   required parameters.
6. For information about working with the remaining controls on this page,
   see [Running commands from the console](running-commands-console.md "running-commands-console.md").
7. Choose **Run**.

###### To turn off Kernel Live Patching (AWS CLI)

- Run a command similar to the following.

Linux & macOS

```
aws ssm send-command \
    --document-name "AWS-ConfigureKernelLivePatching" \
    --targets "Key=instanceIds,Values=`instance-id`" \
    --parameters "EnableOrDisable=Disable"
```

Windows Server

```
aws ssm send-command ^
    --document-name "AWS-ConfigureKernelLivePatching" ^
    --targets "Key=instanceIds,Values=`instance-id`" ^
    --parameters "EnableOrDisable=Disable"
```

Replace `instance-id` with the ID of the Amazon Linux 2
managed node on which you want to turn off the feature, such as
i-02573cafcfEXAMPLE. To turn off the feature on multiple managed nodes, you can
use either of the following formats.

    + `--targets
     "Key=instanceids,Values=`instance-id1`,`instance-id2`"`
    + `--targets
     "Key=tag:`tag-key`,Values=`tag-value`"`

For information about other options you can use in the command, see
[send-command](../../../cli/latest/reference/ssm/send-command.md "../../../cli/latest/reference/ssm/send-command.md") in the
_AWS CLI Command Reference_.
