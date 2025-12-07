This is the new _CloudFormation Template Reference Guide_.
Please update your bookmarks and links. For help getting started with CloudFormation, see the
[AWS CloudFormation User Guide](../UserGuide/Welcome.md "../UserGuide/Welcome.md").

# cfn-hup

The `cfn-hup` helper is a daemon that detects changes in resource metadata
and runs user-specified actions when a change is detected. This allows you to make
configuration updates on your running Amazon EC2 instances through the `UpdateStack`
API action.

For more information, see the [Updating a CloudFormation stack](../UserGuide/updating.stacks.md "../UserGuide/updating.stacks.md") tutorial in the
_AWS CloudFormation User Guide_.

###### Topics

- [Syntax](#cfn-hup-Syntax "#cfn-hup-Syntax")
- [Options](#cfn-hup-options "#cfn-hup-options")
- [cfn-hup.conf configuration file](#cfn-hup-config-file "#cfn-hup-config-file")
- [hooks.conf configuration
  file](#cfn-hup-hook-file "#cfn-hup-hook-file")
- [hooks.d directory](#cfn-hup-hooks-dir "#cfn-hup-hooks-dir")
- [Examples](#cfn-hup-examples "#cfn-hup-examples")
- [Related resources](#cfn-hup-related-resources "#cfn-hup-related-resources")

## Syntax

```
cfn-hup --config|-c config.dir \
        --no-daemon \
        --verbose|-v
```

## Options

| Name            | Description                                                       | Required                                                                                                                                                                                                             |
| --------------- | ----------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --- |
| `--config       | -c config.dir`                                                    | Specifies the path that the `cfn-hup` script looks for the<br>`cfn-hup.conf` and the `hooks.d`<br>directories. On Windows, the default path is<br>``system_drive`\cfn`. On Linux,<br>the default path is `/etc/cfn`. | No  |
| `--no-daemon`   | Specify this option to run the `cfn-hup` script once and<br>exit. | No                                                                                                                                                                                                                   |
| `-v, --verbose` | Specify this option to use verbose mode.                          | No                                                                                                                                                                                                                   |

## cfn-hup.conf configuration file

The `cfn-hup.conf` file stores the name of the stack and the AWS
credentials that the `cfn-hup` daemon targets.

The `cfn-hup.conf` file uses the following format:

```
[main]
stack=`<stack-name-or-id>`
```

| Name              | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | Required |
| ----------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------- |
| `stack`           | A stack name or ID.<br>_Type_: String                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | Yes      |
| `credential-file` | An owner-only credential file, in the same format used for the command<br>line tools.<br>_Type_: String<br>_Condition_: The `role` parameter<br>supersedes this parameter.                                                                                                                                                                                                                                                                                                                                                                                                                                | No       |
| `role`            | The name of an IAM role that's associated with the instance.<br>_Type_: String                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | No       |
| `region`          | The name of the AWS Region containing the stack.<br>_Example_: us-east-2                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | No       |
| `umask`           | The `umask` used by the `cfn-hup` daemon.<br>This value can be specified with or without a leading 0. In both<br>cases, it's interpreted as an octal number (similar to the Linux<br>`umask` command). This parameter has no effect on<br>Windows.<br>_Type_: Octal integer between `0` and<br>`0777`<br>_Default_: `022`, version 1.4–22<br>and higher. The default value of `022` masks group and world<br>write permissions, so files created by the `cfn-hup` daemon<br>aren't group or world writable by default. The default value for versions<br>1.4 –21 and earlier is `0`, which masks nothing. | No       |
| `interval`        | The interval used to check for changes to the resource metadata in<br>minutes.<br>_Type_: Integer<br>_Default_: `15`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | No       |
| `verbose`         | Specifies whether to use verbose logging.<br>_Type_: Boolean<br>_Default_: `false`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | No       |

## `hooks.conf` configuration

file

The user actions that the `cfn-hup` daemon calls periodically are defined
in the `hooks.conf` configuration file. The
`hooks.conf` file uses the following
_format_:

```
[hookname]
triggers=post.add `or` post.update `or` post.remove
path=Resources.`<logicalResourceId>` (.Metadata `or` .PhysicalResourceId)(.`<optionalMetadatapath>`)
action=`<arbitrary shell command>`
runas=`<runas user>`
```

When the operation is run, it is run in a copy of the current environment (that
`cfn-hup` is in), with `CFN_OLD_METADATA` set to the previous
metadata value specified by path, and `CFN_NEW_METADATA` set to the current
value.

The hooks configuration file is loaded at `cfn-hup` daemon start up only,
so new hooks will require the daemon to be restarted. A cache of previous metadata
values is stored at `/var/lib/cfn-hup/data/metadata_db`— you can
delete this cache to force `cfn-hup` to run all `post.add` actions
again.

| Name       | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | Required |
| ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------- |
| `hookname` | A unique name for this hook.<br>_Type_: String                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | Yes      |
| `triggers` | A comma-delimited list of conditions to detect.<br>_Valid values_: `post.add`,<br>`post.update`, or `post.remove`<br>_Example_: `post.add,<br>post.update`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | Yes      |
| `path`     | The path to the metadata object. Supports an arbitrarily deep path<br>within the Metadata block.<br>Path format options<br>• Resources.`<LogicalResourceId>`—<br>monitor the last updated time of the resource, triggering on any<br>change to the resource.<br>• Resources.`<LogicalResourceId>`.PhysicalResourceId—<br>monitor the physical ID of the resource, triggering only when the<br>associated resource identity changes (such as a new EC2<br>instance).<br>• Resources.`<LogicalResourceId>`.Metadata(`.optional<br>path`)— monitor the metadata of a resource<br>for changes (a metadata subpath may be specified to an arbitrarily<br>deep level to monitor specific values). | Yes      |
| `action`   | An arbitrary shell command that is run as given.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | Yes      |
| `runas`    | A user to run the commands as. `cfn-hup` uses the su<br>command to switch to the user.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | Yes      |

## `hooks.d` directory

To support composition of several applications deploying change notification hooks,
`cfn-hup` supports a directory named `hooks.d` that is
located in the hooks configuration directory. You can place one or more additional hooks
configuration files in the `hooks.d` directory. The additional hooks
files must use the same layout as the `hooks.conf` file.

The `cfn-hup` daemon parses and loads each file in this directory. If any
hooks in the `hooks.d` directory have the same name as a hook in
`hooks.conf`, the hooks will be merged (meaning
`hooks.d` will overwrite `hooks.conf` for any
values that both files specify).

## Examples

In the following examples, CloudFormation triggers the
`cfn-auto-reloader.conf` hooks file when you change the
`AWS::CloudFormation::Init` resource that is associated with the
`LaunchConfig` resource.

### JSON

```
...
    "LaunchConfig": {
      "Type" : "AWS::AutoScaling::LaunchConfiguration",
      "Metadata" : {
        "AWS::CloudFormation::Init" : {
...
              "/etc/cfn/hooks.d/cfn-auto-reloader.conf": {
                "content": { "Fn::Join": [ "", [
                  "[cfn-auto-reloader-hook]\n",
                  "triggers=post.update\n",
                  "path=Resources.LaunchConfig.Metadata.AWS::CloudFormation::Init\n",
                  "action=/opt/aws/bin/cfn-init -v ",
                          "         --stack ", { "Ref" : "AWS::StackName" },
                          "         --resource LaunchConfig ",
                          "         --configsets wordpress_install ",
                          "         --region ", { "Ref" : "AWS::Region" }, "\n",
                  "runas=root\n"
                ]]},
                "mode"  : "000400",
                "owner" : "root",
                "group" : "root"
              }
...
```

### YAML

```
...
  LaunchConfig:
    Type: "AWS::AutoScaling::LaunchConfiguration"
    Metadata:
      AWS::CloudFormation::Init:
...
            /etc/cfn/hooks.d/cfn-auto-reloader.conf:
              content: !Sub |
                [cfn-auto-reloader-hook]
                triggers=post.update
                path=Resources.LaunchConfig.Metadata.AWS::CloudFormation::Init
                action=/opt/aws/bin/cfn-init -v --stack ${AWS::StackName} --resource LaunchConfig --configsets wordpress_install --region ${AWS::Region}
                runas=root
              mode: "000400"
              owner: "root"
              group: "root"
...
```

## Related resources

You can also visit our GitHub repository to download [sample templates](../UserGuide/template-guide.md#sample-templates "../UserGuide/template-guide.md#sample-templates") that
use `cfn-hup`, including the following templates.

- [InstanceWithCfnInit.yaml](https://github.com/aws-cloudformation/aws-cloudformation-templates/blob/main/EC2/InstanceWithCfnInit.yaml "https://github.com/aws-cloudformation/aws-cloudformation-templates/blob/main/EC2/InstanceWithCfnInit.yaml")
- [AutoScalingRollingUpdates.yaml](https://github.com/aws-cloudformation/aws-cloudformation-templates/blob/main/AutoScaling/AutoScalingRollingUpdates.yaml "https://github.com/aws-cloudformation/aws-cloudformation-templates/blob/main/AutoScaling/AutoScalingRollingUpdates.yaml")
