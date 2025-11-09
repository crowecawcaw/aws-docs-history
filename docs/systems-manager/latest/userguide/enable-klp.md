AWS Systems Manager Change Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see
[AWS Systems Manager Change Manager availability change](change-manager-availability-change.md "change-manager-availability-change.md").

# Turning on Kernel Live Patching using Run Command

To turn on Kernel Live Patching, you can either run `yum` commands on your managed
nodes or use Run Command and a custom Systems Manager document (SSM document) that you
create.

For information about turning on Kernel Live Patching by running `yum` commands
directly on the managed node, see [Enable Kernel Live Patching](../../../AWSEC2/latest/UserGuide/al2-live-patching.md#al2-live-patching-prereq "../../../AWSEC2/latest/UserGuide/al2-live-patching.md#al2-live-patching-prereq") in the _Amazon EC2 User Guide_.

###### Note

When you turn on Kernel Live Patching, if the kernel already running on the
managed node is _earlier_ than
`kernel-4.14.165-131.185.amzn2.x86_64` (the minimum
supported version), the process installs the latest available kernel version and
reboots the managed node. If the node is already running
`kernel-4.14.165-131.185.amzn2.x86_64` or later, the
process doesn't install a newer version and doesn't reboot the node.

###### To turn on Kernel Live Patching using Run Command (console)

1. Open the AWS Systems Manager console at [https://console.aws.amazon.com/systems-manager/](https://console.aws.amazon.com/systems-manager/ "https://console.aws.amazon.com/systems-manager/").
2. In the navigation pane, choose **Run Command**.
3. Choose **Run command**.
4. In the **Command document** list, choose the custom SSM
   document `AWS-ConfigureKernelLivePatching`.
5. In the **Command parameters** section, specify whether
   you want managed nodes to reboot as part of this operation.
6. For information about working with the remaining controls on this page,
   see [Running commands from the console](running-commands-console.md "running-commands-console.md").
7. Choose **Run**.

###### To turn on Kernel Live Patching (AWS CLI)

- Run the following command on your local machine.

Linux & macOS

```
aws ssm send-command \
    --document-name "AWS-ConfigureKernelLivePatching" \
    --parameters "EnableOrDisable=Enable" \
    --targets "Key=instanceids,Values=`instance-id`"
```

Windows Server

```
aws ssm send-command ^
    --document-name "AWS-ConfigureKernelLivePatching" ^
    --parameters "EnableOrDisable=Enable" ^
    --targets "Key=instanceids,Values=`instance-id`"
```

Replace `instance-id` with the ID of the Amazon Linux 2
managed node on which you want to turn on the feature, such as
i-02573cafcfEXAMPLE. To turn on the feature on multiple managed nodes, you can
use either of the following formats.

    + `--targets
     "Key=instanceids,Values=`instance-id1`,`instance-id2`"`
    + `--targets
     "Key=tag:`tag-key`,Values=`tag-value`"`

For information about other options you can use in the command, see
[send-command](../../../cli/latest/reference/ssm/send-command.md "../../../cli/latest/reference/ssm/send-command.md") in the
_AWS CLI Command Reference_.
