# Applying kernel live patches using Run Command

To apply kernel live patches, you can either run `yum` commands on your
managed nodes or use Run Command and the SSM document
`AWS-RunPatchBaseline`.

For information about applying kernel live patches by running `yum`
commands directly on the managed node, see [Apply kernel live patches](../../../AWSEC2/latest/UserGuide/al2-live-patching.md#al2-live-patching-apply "../../../AWSEC2/latest/UserGuide/al2-live-patching.md#al2-live-patching-apply") in the
_Amazon EC2 User Guide_.

###### To apply kernel live patches using Run Command (console)

1. Open the AWS Systems Manager console at [https://console.aws.amazon.com/systems-manager/](https://console.aws.amazon.com/systems-manager/ "https://console.aws.amazon.com/systems-manager/").
2. In the navigation pane, choose **Run Command**.
3. Choose **Run command**.
4. In the **Command document** list, choose the SSM
   document `AWS-RunPatchBaseline`.
5. In the **Command parameters** section, do one of the
   following:
   - If you're checking whether new kernel live patches are available,
     for **Operation**, choose `Scan`. For
     **Reboot Option**, if don't want your managed
     nodes to reboot after this operation, choose `NoReboot`.
     After the operation is complete, you can check for new patches and
     compliance status in Compliance.
   - If you checked patch compliance already and are ready to apply
     available kernel live patches, for **Operation**,
     choose `Install`. For **Reboot Option**,
     if you don't want your managed nodes to reboot after this operation,
     choose `NoReboot`.

6. For information about working with the remaining controls on this page,
   see [Running commands from the console](running-commands-console.md "running-commands-console.md").
7. Choose **Run**.

###### To apply kernel live patches using Run Command (AWS CLI)

1. To perform a `Scan` operation before checking your results in
   Compliance, run the following command from your local machine.

Linux & macOS

```
aws ssm send-command \
    --document-name "AWS-RunPatchBaseline" \
    --targets "Key=InstanceIds,Values=`instance-id`" \
    --parameters '{"Operation":["Scan"],"RebootOption":["RebootIfNeeded"]}'
```

Windows Server

```
aws ssm send-command ^
    --document-name "AWS-RunPatchBaseline" ^
    --targets "Key=InstanceIds,Values=`instance-id`" ^
    --parameters {\"Operation\":[\"Scan\"],\"RebootOption\":[\"RebootIfNeeded\"]}
```

For information about other options you can use in the command, see
[send-command](../../../cli/latest/reference/ssm/send-command.md "../../../cli/latest/reference/ssm/send-command.md") in the
_AWS CLI Command Reference_. 2. To perform an `Install` operation after checking your results
in Compliance, run the following command from your local machine.

Linux & macOS

```
aws ssm send-command \
    --document-name "AWS-RunPatchBaseline" \
    --targets "Key=InstanceIds,Values=`instance-id`" \
    --parameters '{"Operation":["Install"],"RebootOption":["NoReboot"]}'
```

Windows Server

```
aws ssm send-command ^
    --document-name "AWS-RunPatchBaseline" ^
    --targets "Key=InstanceIds,Values=`instance-id`" ^
    --parameters {\"Operation\":[\"Install\"],\"RebootOption\":[\"NoReboot\"]}
```

In both of the preceding commands, replace `instance-id`
with the ID of the Amazon Linux 2 managed node on which you want to apply kernel live
patches, such as i-02573cafcfEXAMPLE. To turn on the feature on multiple managed nodes,
you can use either of the following formats.

- `--targets
"Key=instanceids,Values=`instance-id1`,`instance-id2`"`
- `--targets
 "Key=tag:`tag-key`,Values=`tag-value`"`
  For information about other options you can use in these commands, see
  [send-command](../../../cli/latest/reference/ssm/send-command.md "../../../cli/latest/reference/ssm/send-command.md") in the _AWS CLI Command Reference_.
